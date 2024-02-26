#!/usr/bin/python3
"""
Module: Initialize models directory
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
