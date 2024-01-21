#!/usr/bin/python3
"""ensure everytime application start to reload updates"""


from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
