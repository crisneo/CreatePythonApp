import os
import sys
import unittest
from pathlib import Path
from unittest.loader import TestLoader

"""include src folder for locating app modules"""
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))+"\\src\\createpythonapp")

from helpers.fshelper import FsHelper
from projcreator import ProjectCreator


class CreatePythoAppTests(unittest.TestCase):    
    def test_CreateProjectCreator(self):
        fh = FsHelper()
        pc = ProjectCreator(fh, '.')
        self.assertEqual(fh, pc.fsHelper)

if __name__ == '__main__':
    unittest.main()