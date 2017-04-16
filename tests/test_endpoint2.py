# content of test_endpoint2.py
from api_service import ApiService 

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"


def test_get_webhooks():
    
    api_svc = ApiService(ACCESS_TOKEN)
    result = api_svc.get_webhooks("/webhooks?page=1&per_page=1")    
    assert result.status_code == 200
    result = result.json()
    total = result ["total"]
    print ('\ntest_endpoint2::get_webhooks -  {} webhook(s) successfully retrieved...'.format(total))
    