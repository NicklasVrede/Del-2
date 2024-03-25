from unittest import TestCase
import DictBinTree as dbt

class TestDictBinTree(TestCase):
    def setUp(self):
        self.T = dbt.createEmptyDict()
        dbt.insert(self.T, 5)
        dbt.insert(self.T, 3)
        dbt.insert(self.T, 7)

    def test_insert(self):
        self.assertEqual(self.T.rod.nøgle, 5)  # Output: 5
        self.assertEqual(self.T.rod.venstre.nøgle, 3)  # Output: 3
        self.assertEqual(self.T.rod.højre.nøgle, 7)

    def test_search(self):
        self.assertTrue(dbt.search(self.T, 5))
        self.assertTrue(dbt.search(self.T, 3))
        self.assertTrue(dbt.search(self.T, 7))
        self.assertFalse(dbt.search(self.T, 8))
        self.assertFalse(dbt.search(self.T, 2))

    def test_orderedTraversal(self):
        self.assertEqual(dbt.orderedTraversal(self.T), [3, 5, 7])

if __name__ == '__main__':
    from unittest import main
    main()

    