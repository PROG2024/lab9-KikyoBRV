"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
import unittest
from counter import Counter


class TestCounterSingleton(unittest.TestCase):

    def test_singleton_instance(self):
        # Test that multiple instances refer to the same object
        counter1 = Counter()
        counter2 = Counter()

        self.assertIs(counter1, counter2)

    def test_shared_count(self):
        # Test that all references share the same count
        counter1 = Counter()
        counter2 = Counter()

        counter1.increment()
        self.assertEqual(counter1.count, 1)
        self.assertEqual(counter2.count, 1)

        counter2.increment()
        self.assertEqual(counter1.count, 2)
        self.assertEqual(counter2.count, 2)


if __name__ == '__main__':
    unittest.main()
