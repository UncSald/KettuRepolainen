import pytest
from app import app

# Fixture that provides a test client for making requests to the Flask app
# This client simulates real HTTP requests to the application, so we can test the app's behavior
@pytest.fixture
def client():
    """
    Provides a test client for making requests to the Flask app during testing.
    """
    with app.test_client() as client:
        yield client  # Return the test client to the test function

# Test function for the '/references' route
def test_get_references(client):
    """
    Test the '/references' route to ensure it returns a correct response with HTTP status 200.
    The test checks that:
    - The response status code is 200, indicating success.
    - The response data is a JSON list.
    - The first item in the response contains keys "title" and "author".
    """
    # Make a GET request to the '/references' route
    response = client.get("/references")

    # Check that the status code is 200, meaning the request was successful
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    # Check that the response body is a list (JSON format)
    assert isinstance(response.json, list), f"Expected response to be a list, got {type(response.json)}"

    # Check that the first item in the list contains the key 'title' (the structure of the reference)
    assert "title" in response.json[0], "'title' key not found in the first reference"

    # Check that the first item in the list contains the key 'author'
    assert "author" in response.json[0], "'author' key not found in the first reference"
