import web.http as http

import pytest

@pytest.fixture
def app():
	http.app.config["TESTING"] = True
	return http.app.test_client()

class TestAPI:
	def test_index(self):
		response = app().get("/")
		assert response.status == "200 OK"
