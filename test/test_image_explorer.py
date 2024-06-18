# File: test/test_image_explorer.py

import unittest
from izlearn.vision import ImageExplorer

class TestImportImageExplorer(unittest.TestCase):

    def test_import(self):
        try:
            from izlearn.vision import ImageExplorer
        except ImportError:
            self.fail("ImportError: cannot import 'ImageExplorer' from 'izlearn.vision'")

if __name__ == '__main__':
    unittest.main()