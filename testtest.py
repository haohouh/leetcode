import unittest

def my_fuc(a,b):
    return a + b

class Mytest(unittest.TestCase):
    def test_myfuc(self):
        self.assertEqual(my_fuc(1,2),3)


if __name__ == "__main__":
    unittest.main()
        