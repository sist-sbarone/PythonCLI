import unittest
from klickbrick.klickbrick import hello

class HelloMethods(unittest.TestCase):

    def test_hello_no_args(self):
        self.assertEqual('Hello World', hello(None))

    def test_hello_name(self):
        self.assertEqual('Hello Jane', hello('Jane'))

if __name__ == '__main__':
    unittest.main()
