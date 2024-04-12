from unittest import TestCase
import DictBinTree as dbt

class TestDictBinTree(TestCase):
    def setUp(self):
        self.T = dbt.DictBinTree()
        self.T.insert(5)
        self.T.insert(3)
        self.T.insert(7)

    def test_insert(self):
        self.assertEqual(self.T.rod.k, 5)  # Output: 5
        self.assertEqual(self.T.rod.venstre.k, 3)  # Output: 3
        self.assertEqual(self.T.rod.højre.k, 7)

    def test_search(self):
        self.assertTrue(self.T.search(5))
        self.assertTrue(self.T.search(3))
        self.assertTrue(self.T.search(7))
        self.assertFalse(self.T.search(8))
        self.assertFalse(self.T.search(2))

    def test_orderedTraversal(self):
        self.assertEqual(self.T.orderedTraversal(), [3, 5, 7])
        self.assertEqual(self.T.orderedTraversal(), [3, 5, 7])
        self.assertEqual(self.T.orderedTraversal(), [3, 5, 7])

if __name__ == '__main__':
    from unittest import main
    main()

    