# Test Frontend
import unittest
from unittest.mock import patch
from Front import *

@patch('builtins.print')
@patch('builtins.input')


class TestFront(unittest.TestCase):
    def test_exception(self, patch_input, patch_print):
        with self.assertRaises(Exception):
            raise Exception("Error")
    def test_start(self, patch_input, patch_print):
        self.start = Juego()
        self.assertEqual(self.start.fin, False)
    def test_visual(self, patch_input, patch_print):
        self.visual = Juego()
        patch_print.return_value = ["1", "2", "3", "4", "5", "6", "7", "8"]
    def test_posicion(self, patch_input, patch_print):
        self.posicion = Juego()
        patch_input.return_value = ["1", "2", "3", "4", "5", "6", "7", "8"]

        




if __name__ == '__main__':
    unittest.main()