#!/usr/bin/python3
""" Module: test_db_storage """

import unittest
import pep8


class testDBSorage(unittest.TestCase):
    """ class test for db storage """

    def test_pep8_conformance(self):
        """Test that we conforms to PEP8.
        """
        style = pep8.StyleGuide()
        result = style.check_files(["models/engine/db_storage.py"])
        self.assertEqual(result.total_errors, 0, "Fix pep8")
