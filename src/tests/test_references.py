import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import unittest
from daos.reference_dao import ReferenceDao


class TestTodoValidation(unittest.TestCase):
    def setUp(self):
        self.dao = ReferenceDao(None)
        self.reference = [(306, 'article', 'keyword', 'author', 'title', 'journal', 1999, None, None, None, None, None, None, None, None)]

    def test_bibtex_converter(self):
        result = self.dao.convert_to_bibtex(self.reference)
        print(result)

        expected = """@article{keyword,
  author       = "author",
  title        = "title",
  journal      = "journal",
  year         = 1999
}"""

        self.assertEqual(result.strip(), expected.strip())