import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    # self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    typewise_alert.check_and_alert(20, 50, 100)
  def test_infers_breach_as_per_limits_high(self):
    self.assertTrue(typewise_alert.infer_breach(150, 50, 100) == 'TOO_HIGH')


if __name__ == '__main__':
  unittest.main()
