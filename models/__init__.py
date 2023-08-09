#!/usr/bin/python3
""" __init__ file of the engine module """
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
