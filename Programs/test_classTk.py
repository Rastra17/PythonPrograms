#An Unit Testing program which tests each unit in classTk python file

import unittest

from classTk import Geto
import tkinter as tk


class TEST(unittest.TestCase):
    def test_get(self):
        test = Geto(tk.Tk())
        self.assertEqual(test.miracle[-1], "Rastra")

if __name__=='__main__':
    unittest.main()