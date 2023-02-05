import unittest
import mydb
from unittest.mock import patch, Mock

class TestTotalBalance(unittest.TestCase):
    def setUp(self):
        self.data = mydb.Database(db='test.db')
        self.data.insertRecord(item_name='Milk', item_price=2, purchase_date='2023-02-01')
        self.data.insertRecord(item_name='Bread', item_price=2, purchase_date='2023-02-02')
        self.data.insertRecord(item_name='Whey Protein', item_price=27, purchase_date='2023-02-03')
        self.data.insertRecord(item_name='Eggs', item_price=1.5, purchase_date='2023-02-04')

    def test_total_balance(self):
        f = self.data.fetchRecord(query="Select sum(item_price) from expense_record")
        for i in f:
            for j in i:
                self.assertEqual(5000 - j, 5000 - 32.5)
    def test_fetchRecord(self):
            result = self.data.fetchRecord("SELECT * FROM expense_record")
            self.assertEqual(result , [('Milk', 2,'2023-02-01'),('Bread', 2,'2023-02-02'),
                                       ('Whey Protein', 27,'2023-02-03'),('Eggs', 1.5,'2023-02-04')])

    def tearDown(self):
        self.data.removeRecord(1)
        self.data.removeRecord(2)
        self.data.removeRecord(3)
        self.data.removeRecord(4)

if __name__ == '__main__':
    unittest.main()


