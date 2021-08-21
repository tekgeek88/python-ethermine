import requests

def test_ethermine_base_url_status_code_equals_200():
     response = requests.get("https://api.ethermine.org")
     assert response.status_code == 200
