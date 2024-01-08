import unittest
from fastapi.testclient import TestClient

from src.main import app
from src.setup import LOGGER


class IntegrationTestCases(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(IntegrationTestCases, self).__init__(*args, **kwargs)
        self.client = TestClient(app)

    def test_health_checkpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"developer-rating-engine": "ok"})

    def test_success(self):
        # TODO: Test for success
        pass

    def test_failure(self):
        # TODO: Test for invalid length, both vectors have different length
        pass
