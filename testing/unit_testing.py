import os
os.chdir("/media/greg/Storage/packages/spelling_distortion")

from despell.despell import *

import unittest

class TestCorruptText(unittest.TestCase):
    
    def test1_transpose(self):
        self.assertFalse(type(transpose([]))==list)

    def test_single_input_transpose(self):
        self.assertFalse(type(transpose(["1"]))==list)

    def test_input_is_list_transpose(self):

        self.assertTrue(type(transpose(["1","2"]))==list)
        self.assertTrue(type(transpose(["a","d"]))==list)

    def test_output_elements_are_str_transpose(self):

        test_input = ["1","2"]

        for i in range(len(test_input)):
            self.assertTrue(type(transpose(test_input)[i])==str)

    def test6_transpose(self):

        test_input = ["a","d"]

        for i in range(len(test_input)):
            self.assertTrue(type(transpose(test_input)[i])==str)

if __name__ == '__main__':

    unittest.main()