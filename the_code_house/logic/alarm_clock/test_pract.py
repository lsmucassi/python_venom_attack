import unittest
from alarm_clock import alarm_clock

class TestAlarmClock(unittest.TestCase):
    def test_clock(self):
        self.assertEqual(alarm_clock(1, False), '07:00')
        print("Test 1: alarm_clock(1, False), '07:00'")
        self.assertEqual(alarm_clock(5, False), '07:00')
        self.assertEqual(alarm_clock(0, True), 'off')

if __name__ == '__main__':
    unittest.main()
