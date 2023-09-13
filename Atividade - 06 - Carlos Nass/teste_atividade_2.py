import unittest
from atividade_2 import WorkHoursCalculator

class TestWorkHoursCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = WorkHoursCalculator()

    def test_HoursDifference(self):
        self.assertEqual(self.calculator.HoursDifference('06:00', '14:30'), 8.5)
        self.assertEqual(self.calculator.HoursDifference('11:00', '13:30'), 2.5)

    def test_WorkHours(self):
        hours = [('09:00', '17:30'), ('07:15', '15:45'), ('11:00', '13:30')]
        self.assertEqual(self.calculator.WorkHours(hours), 19.5)

    def test_ValidateFormat(self):
        self.assertTrue(self.calculator.ValidateFormat('04:00'))
        self.assertTrue(self.calculator.ValidateFormat('11:45'))
        self.assertFalse(self.calculator.ValidateFormat('6:00'))
        self.assertFalse(self.calculator.ValidateFormat('02:99'))
        self.assertFalse(self.calculator.ValidateFormat('0500'))

    def test_InsertTimeout(self):
        self.calculator.InsertTimeout('02-030')
        self.assertEqual(self.calculator.timeout, 2.5)
        self.calculator.InsertTimeout('01-000')
        self.assertEqual(self.calculator.timeout, 1)

    def test_WorkHoursWithTimeout(self):
        hours = [('09:00', '17:30'), ('07:15', '15:45'), ('11:00', '13:30')]
        self.calculator.InsertTimeout('01-030')
        self.assertEqual(self.calculator.WorkHours(hours), 18.0)

if __name__ == '__main__':
    unittest.main()
