#!/usr/bin/python3
""" Module: test_console"""

import pep8
import unittest


class testConsole(unittest.TestCase):
    """ Test for console.py"""

    def test_pep8_conformance(self):
        """Test that we conforms to PEP8.
        """
        style = pep8.StyleGuide()
        result = style.check_files(["console.py"])
        self.assertEqual(result.total_errors, 0, "Fix pep8")
