
# Uses requests library: http://docs.python-requests.org/en/latest/
import requests

BASE_URL = "https://api.surveymonkey.net/v3"

# Currently provides the following SurveyMonkey
# API v3 methods:
#   /surveys
#   /webhooks
# . /webhooks/(id}
# Handles http using the requests module

class ApiService (object):
    def __init__(self, access_token):
        self.client = requests.session()
        self.client.headers = {
            "Authorization": "bearer %s" % access_token,
            "Content-Type": "application/json"
        }
    
    ############################################
    ######### SurveyMonkey API Methods #########
    ############################################
    
    def check_head(self, uri):
        r = self._do_head(BASE_URL + uri)
        return r
    
    def check_options(self, uri):
        r = self._do_options(BASE_URL + uri)
        return r

    #v3.surveys

    def create_survey(self, uri, data=None):
        data = data if data is not None else {} 
        r = self._post_request(BASE_URL + uri, data)
        return r
     
    # v3.webhooks
    def create_webhook(self , uri, data=None):
        data = data if data is not None else {} 
        r = self._post_request(BASE_URL + uri, data)
        return r


    def get_webhook(self, uri):
        r = self._get_request(BASE_URL+uri)
        return r


    def modify_webhook(self, uri, data=None):
        data = data if data is not None else {} 
        r = self._patch_request(BASE_URL + uri, data)
        return r


    def replace_webhook(self, uri, data=None):
        data = data if data is not None else {} 
        r = self._put_request(BASE_URL + uri, data)
        return r


    def delete_webhook(self, uri):
        r = self._delete_request(BASE_URL + uri)
        return r
        

    def get_webhooks(self, uri, data=None):
        data = data if data is not None else {}
        r = self._get_request(BASE_URL + uri)
        return r   
  
    #############################################
    ######## API Service Private Methods ########
    #############################################

    def _do_head(self, url):
        response = self.client.head(url)
        return response
    
    def _do_options(self, url):
        response = self.client.options(url)
        return response

    def _get_request(self, url):
        response = self.client.get(url)
        return response

    def _post_request(self, url, payload):
        response = self.client.post(url,json=payload)
        return response

    def _patch_request(self, url, payload):
        response = self.client.patch(url,json=payload)
        return response

    def _put_request(self, url, payload):
        response = self.client.put(url,json=payload)
        return response

    def _delete_request(self, url):
        response = self.client.delete(url)
        return response