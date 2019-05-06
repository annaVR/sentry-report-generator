import requests
from sentry_report_generator.timestamps_list import get_epoch_list
API_ENDPOINT_URL = None

def get_json_list():
    """
    Prompts user for auth token (Bearer format only).
    Makes GET calls to stats endpoint for the previous seven days and today.
    For each day returns json: timestamp, issue count pair for every hour.
    :return: jsons from sentry-report-generator stats endpoint
    """
    authorization_token = input("Enter a Bearer token:")
    headers = {'Authorization': authorization_token}
    json_list = []
    for date in get_epoch_list():
        url = API_ENDPOINT_URL
        r = requests.get(url, headers=headers)
        response = r.json()
        if r.status_code == 200:
            json_list.append(response)
        else:
            print("Response: {}: {}".format(r.status_code, response))
            break
    return json_list
