import unittest

class Apptesting(unittest.TestCase):


    @unittest.SkipTest
    def test_search(self):
        print("This is a test")

    @unittest.skip("Because I said so!")
    def test_search2(self):
        print("This is another test")

    @unittest.skipIf(1==1,"Because Logic!")
    def test_search3(self):
        print("This is one more test")

    def test_search4(self):
        print("This is the last one test")

    def test_search5(self):
        print("Psyche!")

    def test_search6(self):
        print("All right this is the last one. Bye!")

if __name__ == "__main__":
    unittest.main()