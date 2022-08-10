from unittest import TestCase

from fastapi.testclient import TestClient

from ..main import get_application


class TestApp(TestCase):
    def create_app(self):
        app = get_application("core.configs.testing.settings")
        return app

    def setUp(self):
        self.client = TestClient(self.create_app())

    def test_return_404(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 404)

    def test_call_api_test(self):
        """API endpoint test is 200 for the hello endpoint"""
        client = self.client.get("/api/v1/accounts/")

        self.assertEqual(client.status_code, 200)

    def test_call_second_api_test(self):
        """API endpoint test is 200 for the hello test endpoint"""
        client = self.client.get("/api/v1/test")

        self.assertEqual(client.status_code, 200)
