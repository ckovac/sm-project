# content of test_endpoint1.py

import pytest
import requests
from api_service import ApiService 

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
SUBSCRIPTION_URL = "YOUR SUBSCRIPTION_URL"
SURVEY_TITLE = "Test Survey"
SURVEY_TITLE2 = "Test Webhook Firing"


def test_happy_path_scenario():   
    api_svc = ApiService(ACCESS_TOKEN)
    
    # Check HEAD
    result = api_svc.check_head("/webhooks")
    assert result.status_code == 204
    
    # Check OPTIONS
    result = api_svc.check_options("/webhooks")
    # No options returned (?) 
    assert result.status_code == 204
    
    survey_id = create_survey(api_svc, SURVEY_TITLE, "/surveys")
    webhook_id = create_webhook(api_svc, survey_id, "webhook_one", "/webhooks")
    modify_webhook(api_svc, "My Modified Webhook", "/webhooks/" + webhook_id)
    replace_webhook(api_svc, survey_id, "/webhooks/" + webhook_id)    
    get_webhook(api_svc,"/webhooks/"+ webhook_id)
    delete_webhook(api_svc,"/webhooks/" + webhook_id)

def test_webhook_fires_scenario():   
    api_svc = ApiService(ACCESS_TOKEN)
    
    survey_id = create_survey(api_svc, "test webhook fires", "/surveys")
    webhook_id = create_webhook(api_svc, survey_id,  "webhook_two", "/webhooks")
    # manually complete the "test webhook fires" survey and confirm that the webhook fires by checking requestbin

    # IMPORTANT: manually clear out the webhooks between runs. 
    #            There appears to be a bug when creating a webhook. If there are multiple surveys with the same name
    #            then creating a webhook returns an error (because the survey names are not unique?) 
    #            Also, deleting a survey does not clear the associated webhooks (by design?).
    
    # TODO: automate survey response and compare the webhook data with the event data

def create_survey(api_svc, title, uri):
    global survey_id 
   
    payload = {
        "title": title
    }
    result = api_svc.create_survey(uri, payload) 
    assert result.status_code == 201
    result = result.json()
    survey_id = result["id"]
    print ('\ntest_endpoint1::create_survey - survey {} with title {} successfully created...'.format(survey_id, title))
    return survey_id


def create_webhook(api_svc, survey_id, webhook_name, uri):
    global webhook_id 
    payload = {
        "event_type": "response_completed",
        "subscription_url": SUBSCRIPTION_URL,
        "object_type": "survey",
        "object_ids": [survey_id],
        "name": webhook_name     
    }
    result = api_svc.create_webhook(uri, payload)
    assert result.status_code == 201
    result = result.json()
    webhook_id = result["id"]
    print ('\ntest_endpoint1::create_webhook - webhook with id {} successfully created...'.format(webhook_id))
    return webhook_id


def modify_webhook(api_svc, name, uri):
    payload = {
        "name": name 
    }
    result = api_svc.modify_webhook(uri,payload)
    assert result.status_code == 200
    result = result.json()
    id = result["id"]
    print ('\ntest_endpoint1::modify_webhook - webhook with id {} successfully modified...'.format(id))
  

def replace_webhook(api_svc, survey_id, uri):
    payload = {
        "event_type": "response_completed",
        "subscription_url": SUBSCRIPTION_URL,
        "object_type": "survey",
        "object_ids": [survey_id],
        "name": "My Replaced Webhook" 
    }
    result = api_svc.replace_webhook(uri,payload)
    assert result.status_code == 200
    result = result.json()
    id = result["id"]
    print ('\ntest_endpoint1::replace_webhook - webhook with id {} successfully replaced...'.format(id))
  

def get_webhook(api_svc, uri):  
    result = api_svc.get_webhook(uri) 
    assert result.status_code == 200
    result = result.json()
    id = result["id"]
    print ('\ntest_endpoint1::get_webhook - webhook with id {} successfully retrieved...'.format(id))


def delete_webhook(api_svc, uri):
    result = api_svc.delete_webhook(uri)
    assert result.status_code == 200
    result = result.json()
    id = result["id"]
    print ('\ntest_endpoint1::delete_webhook - webhook with id {} successfully deleted...'.format(id))