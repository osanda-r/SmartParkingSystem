# Unit tests
import unittest
from main import SmartParkingSystem

class TestSystem(unittest.TestCase):
    def setUp(self):
        self.sys = SmartParkingSystem()

    def test_spot_occupancy(self):
        self.sys.process_sensor_data("A-101", True, "XYZ123")
        self.sys.process_sensor_data("A-101", False)

    def test_user_auth(self):
        assert self.sys.auth.signup("user1", "pass123")
        assert self.sys.auth.login("user1", "pass123")

    def test_payment(self):
        success = self.sys.handle_payment("A-101", 30)
        assert success

if __name__ == "__main__":
    unittest.main()
