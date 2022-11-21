import os
from typing import Any
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import fitz as pdf # PyMuPDF
from PIL import Image

UPLOAD_FOLDER = 'uploads'

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
    for num, page in enumerate(document):
        if pages > 99:
            # raise Exception('This file simply has too many pages.')
            return "Sir, your luggage " + file.filename + " is too big."
        if pages > 1:
            save_file_name = str(num).rjust(2,'0') + '-' + image_file_name # Add page number as leading number
        else:
            save_file_name = image_file_name
        pil_image = page.get_pixmap() # render page as image
        pil_image.save(path(save_file_name), 'PNG') # PIL image save as .png
    # TODO: We don't actually serve the contents of upload folder in any way 
    # "<br><a href=\"" + UPLOAD_FOLDER + "\"> Your Room </a>"
    return str(num) + " pieces of clothing from luggage " + file.filename  + " are now neatly organisized in your room."