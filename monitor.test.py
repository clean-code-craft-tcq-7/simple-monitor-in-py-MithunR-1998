import unittest
from monitor import vitals_ok


class MonitorTest(unittest.TestCase):
    def test_for_temp(self):
        #within range for temp
        self.assertTrue(vitals_ok(101, 70, 98))
        self.assertTrue(vitals_ok(102, 70, 98))
        self.assertTrue(vitals_ok(96, 70, 98))
        self.assertTrue(vitals_ok(95, 70, 98))
        
        #outside rang for temp
        self.assertFalse(vitals_ok(102.1, 70, 98))
        self.assertFalse(vitals_ok(94.9, 70, 98))

    def test_for_pulse(self):
        #within range for pulse
        self.assertTrue(vitals_ok(97, 60, 98))
        self.assertTrue(vitals_ok(97, 61, 98))
        self.assertTrue(vitals_ok(97, 99, 98))
        self.assertTrue(vitals_ok(97, 100, 98))
        
        #outside rang for pulse
        self.assertFalse(vitals_ok(97, 59.9, 98))
        self.assertFalse(vitals_ok(97, 100.1, 98))

    def test_for_spo2(self):
        #within range for spo2
        self.assertTrue(vitals_ok(97, 70, 91))
        self.assertTrue(vitals_ok(97, 70, 90))
        
        #outside rang for spo2
        self.assertFalse(vitals_ok(97, 70, 89.9))
        

if __name__ == '__main__':
  unittest.main()
