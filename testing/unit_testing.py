import os
os.chdir("/media/greg/Storage/packages/spelling_distortion")

from despell.despell import *

import unittest

class TestCorruptText(unittest.TestCase):

    def test1_transpose(self):
        self.assertFalse(type(transpose([""]))==str)

    def test2_corrupt_text(self):
        self.assertEqual(1,1)

if __name__ == '__main__':

    unittest.main()