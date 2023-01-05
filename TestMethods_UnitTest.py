import unittest

class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("This is login test")

    @classmethod
    def tearDown(self):
        print("This is teardown")

    def test_search(self):
        print("This is search test")

    def test_advancedsearch(self):
        print("This is advanced search")

    def test_prepaidRecharge(self):
        print("This is prepaid Recharge test")

    def test_postpaidRecharge(self):
        print("This is postpaid Recharge test")


if __name__ == "__main__":
    unittest.main()