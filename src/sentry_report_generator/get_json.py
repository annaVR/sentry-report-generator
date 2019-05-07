import requests
from sentry_report_generator.timestamps_list import get_epoch_list
API_ENDPOINT_URL = None # TODO Add --setup to store endpoint in the configuration file

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
    main_url = input("Enter URL:")
    for date in get_epoch_list():
        url_for_day = "https://" + main_url + str(date)
        r = requests.get(url_for_day, headers=headers)
        response = r.json()
        if r.status_code == 200:
            json_list.append(response)
        else:
            print("Response: {}: {}".format(r.status_code, response))
            break
    return json_list
