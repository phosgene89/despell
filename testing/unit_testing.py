import os
os.chdir("/media/greg/Storage/packages/spelling_distortion/despell_pkg/despell/despell")

import importlib
import unittest

import despell as ds

#importlib.reload(despell)

class TestCorruptText(unittest.TestCase):
    
    def test1_transpose(self):

        with self.assertRaises(AssertionError):
            ds.transpose([])

    def test_single_input_transpose(self):

        with self.assertRaises(AssertionError):
            ds.transpose(["1"])

    def test_input_is_list_transpose(self):

        self.assertTrue(type(ds.transpose(["1","2"]))==list)
        self.assertTrue(type(ds.transpose(["a","d"]))==list)

    def test_output_elements_are_str_transpose(self):

        test_input = ["1","2"]

        for i in range(len(test_input)):
            self.assertTrue(type(ds.transpose(test_input)[i])==str)

    def test6_transpose(self):

        test_input = ["a","d"]

        for i in range(len(test_input)):
            self.assertTrue(type(ds.transpose(test_input)[i])==str)

if __name__ == '__main__':

    unittest.main()