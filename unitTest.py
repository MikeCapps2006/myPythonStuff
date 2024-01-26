import cap
import unittest

class TestCap(unittest.TestCase):
    def test_one_words(self):
        text = "python"
        result = cap.cap_text(text)
        self.assertEqual(result, "Python")
    
    def test_multi_words(self):
        text = "mike's shit"
        result = cap.cap_text(text)
        self.assertEqual(result, "Mike's Shit")

if __name__ == '__main__':
    unittest.main()