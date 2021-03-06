from flask_testing import TestCase

from heartbeat.app import application


class Ping(TestCase):

    def create_app(self):
        # TODO: Use application factory.
        return application

    def test_ping_should_return_pong_message(self):
        response = self.client.get('/heartbeat/ping')
        self.assertEqual(response.json, {'message': 'pong'})
