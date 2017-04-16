# smproject
Test Survey Monkey Webhooks API

# Setup Instructions

## Minimum Requirements

macOS 10.12.3 Sierra with Python 3.6.0 installed


## Environment Setup

Please run the following commands at the root of the project to create your test virtual environment:

 	virtualenv -p python3 venv
	source venv/bin/activate
	pip install -r requirements.txt
    
    
## Running the Tests

* update ACCESS_TOKEN with your access token in test_endpoint1.py and test_enpoint2.py
* update SUBSCRIPTION_URL with your subscription url where callback events are sent to (e.g., https://requestb.in/)
* ensure the Create/Modify Surveys, View Webhooks and Create/Modify Webhooks scopes are available for your app
* manually complete the "test webhook fires" survey and confirm that the webhook fires by checking requestb.in
   
IMPORTANT: manually clear out the webhooks between runs.
           There appears to be a bug when creating a webhook. If there are multiple surveys with the same name
           then creating a webhook returns an error (because the survey names are not unique?) 
           Also, deleting a survey does not clear the associated webhooks (by design?).
    
TODO: automate survey response and compare the webhook data with the event data

Please run the following command from the project root folder to run the tests:

    pytest
