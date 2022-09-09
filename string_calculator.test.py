import unittest
import typewise_alert

class StringCalculatorTest(unittest.TestCase):
  def given_empty_string_0_expected(self):
    self.assertTrue(string_calculator.add("") == 0)

if __name__ == '__main__':
  unittest.main()
