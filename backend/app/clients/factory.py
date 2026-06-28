from app.clients.providers.mock_client import MockClient


class AIClientFactory:
    @staticmethod
    def create():
        return MockClient()
