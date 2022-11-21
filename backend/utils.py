from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from typing import Any
import os

UPLOAD_FOLDER = 'uploads'

"""
    Save file directly with werkzeug FileStorage.save() Could be improved.
    Documentation says: 
        "Save the file to a destination path or file object."
"""
def save_file(file: FileStorage) -> str:
            print(f"{os.path.join(os.path.realpath(os.path.dirname(__file__)), UPLOAD_FOLDER, file.filename)}")
            try:
                file.save(os.path.join(os.path.realpath(os.path.dirname(__file__)), UPLOAD_FOLDER, file.filename))
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
            # Todo: Handle PDF file
            return save_file(file)
        elif file.content_type == "image/png" or "image/jpeg":
            # Todo: Handle image file
            return save_file(file)
        else:
            return "Unsupported file type"
