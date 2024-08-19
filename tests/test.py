import unittest

from speciallecture.CSVPrinter import CSVPrinter

class TestCSVPrinter(unittest.TestCase):
    def test_read(self):
        printer = CSVPrinter("./sample.csv")
        line = printer.read()
        print(line)
        self.assertEqual(3, len(line))

    def test_read2(self):
        printer = CSVPrinter("./sample.csv")
        line = printer.read()
        self.assertEqual(3, len(line[1]))

    def test_read3(self):
        try:
            printer = CSVPrinter("./sample2.csv")
            printer.read()
            unittest.TestCase.fail("this line should not be involked")
        except FileNotFoundError as e:
            pass