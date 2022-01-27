import sys
import unittest

sys.path.append("..")
import translate


class TestE2F(unittest.TestCase):     
    def test1(self): 
        self.assertEqual(translate.englishToFrench("Hello"), "Bonjour")
        self.assertEqual(translate.englishToFrench(' '), ' ')        

class TestF2E(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(translate.frenchToEngish("Bonjour"), "Hello")
        self.assertEqual(translate.frenchToEngish(' '), ' ')   

unittest.main()