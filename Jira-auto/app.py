from flask import Flask, request # to read the json payload from github
import os # for environment variables to store the jira token.
import requests   # importing requests library to make api calls to jira api. 
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)
@app.route("/createJira" , methods=["POST"]) # using post coz we are creating new ticket in jira.

def create_jira_ticket():  # using tab to put the code inside the function.
    # Get GitHub webhook JSON
    github_payload = request.get_json()
    print("Webhook received")
    # Get the comment text
    comment = github_payload["comment"]["body"]

    # Only continue if comment starts with /jira
    if comment.startswith("/jira"):

        print("Creating Jira ticket...")


        url = "https://saiffarooqui169.atlassian.net/rest/api/3/issue"

        TOKEN = os.environ.get("JIRA_TOKEN")
        EMAIL = os.environ.get("JIRA_EMAIL")

        auth = HTTPBasicAuth(EMAIL, TOKEN)

        headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
        }

        payload = json.dumps( {
        "fields": {
            
            "description": {
            "content": [
                {
                "content": [
                    {
                    "text": "from github to jira",
                    "type": "text"
                    }
                ],
                "type": "paragraph"
                }
            ],
            "type": "doc",
            "version": 1
            },

            "issuetype": {
            "id": "10002"
            },
            
            "project": {
            "key": "SAIF"
            },
            
            "summary": "new jira ticket from github",
            "timetracking": {
            "originalEstimate": "10",
            "remainingEstimate": "5"
            },
            
        },
        "update": {}
        } )

        response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
        )

        print("Jira ticket created")

        return(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))) # instead of print we used return

    else:
        return "Ignored", 200

if __name__ == "__main__":
    app.run('0.0.0.0', port=6767) # this will run the flask app on port 6767. we can access the api at http://localhost:6767/createJira

