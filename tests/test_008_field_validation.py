import unittest

from invoice_leak_detector.models import Record
from invoice_leak_detector.scoring import score_record


class DepthCheck8(unittest.TestCase):
    def test_008_field_validation(self):
        record = Record(id="invoice-008", exposure=9473, signal=0.533, urgency=1)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
