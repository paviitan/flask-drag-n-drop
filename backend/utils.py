import os
from typing import Any
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import fitz as pdf # PyMuPDF
from PIL import Image

UPLOAD_FOLDER = 'uploads'
RESOLUTION_DPI = 300 # When converting PDF to image. Default 72 gives blurry results.

"""
    Try to simplify filepath stuff. You know this would be trivial if you just made this file handler into a class?
"""
def path(filename: str) -> str:
    return os.path.join(os.path.realpath(os.path.dirname(__file__)), UPLOAD_FOLDER, filename)
"""
    Save file directly with werkzeug FileStorage.save() Could be improved.
    Documentation says: 
        "Save the file to a destination path or file object."
"""
def save_file(file: FileStorage) -> str:
            print(f"{path(file.filename)}")
            try:
                file.save(path(file.filename))
                return "File " + file.filename + " saved!"
            except(Exception):
                return Exception

"""
    Do the stuff you need based on what type of file we got.
    Returns something that Flask expects. Mostly strings that contain html.
    
    Flask actually builds on top of werkzeug so do not be alarmed of the module(s) imported here.
    https://werkzeug.palletsprojects.com/en/2.2.x/datastructures/#werkzeug.datastructures.FileStorage
"""
def file_handler(file: FileStorage) -> Any:
        print(file)
        filename = secure_filename(file.filename) # Sanitize with Werkzeug utils
        if file.content_type == "application/pdf":
            return handle_pdf(file)
            # return save_file(file)
        elif file.content_type == "image/png" or "image/jpeg":
            # Todo: Handle image file
            return save_file(file)
        else:
            return "Unsupported file type"

"""
    Takes PDF file. Saves it as a image(s). Returns download location as HTML string.
"""
def handle_pdf(file: FileStorage) -> str:
    image_file_name = file.filename.split('.',-1)[0] + '.png' # swap the file extension
    file_as_bytes = file.read()
    document = pdf.open(file.filename,file_as_bytes)
    pages = len(document)
    list_of_image_files = []
    for num, page in enumerate(document):
        if pages > 99:
            # raise Exception('This file simply has too many pages.')
            return "Sir, your luggage " + file.filename + " is too big."
        if pages > 1:
            save_file_name = str(num).rjust(2,'0') + '-' + image_file_name # Add page number as leading number
        else:
            save_file_name = image_file_name
        image: Pixmap = page.get_pixmap(dpi=RESOLUTION_DPI) # Render page as Pixmap image
        print(image)
        image.pil_save(path(save_file_name), 'PNG') # Save as .png with https://pymupdf.readthedocs.io/en/latest/pixmap.html#Pixmap.save
        list_of_image_files.append(save_file_name)
    # Generate HTML return message
    message = str(num) + " pieces of clothing from luggage " + file.filename  + " are now neatly organized in your room." + "<br>"
    for file in list_of_image_files:
        # <a href="uploads/filename"> filename </a> <br>
        message += "<a href=\"" + UPLOAD_FOLDER + "/" + file + "\">" + file + "</a>" + "<br>"
    return message