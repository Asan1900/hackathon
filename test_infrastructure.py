import unittest
from infrastructure import Infrastructure

class InfrastructureTest(unittest.TestCase):
    def setUp(self):
        self.infrastructure = Infrastructure()

    def test_network_configuration(self):
        result = self.infrastructure.check_network_configuration()
        self.assertTrue(result, "Network configuration is incorrect")

    def test_service_availability(self):
        result = self.infrastructure.check_service_availability()
        self.assertTrue(result, "Service availability check failed")

    def tearDown(self):
        self.infrastructure.cleanup()

if __name__ == '__main__':
    unittest.main()

