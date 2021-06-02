import unittest
import bankmanagement

class TestBM(unittest.TestCase):
    def test_show_records(self):
        result=bankmanagement.show_records()
        self.assertEqual(result,3)