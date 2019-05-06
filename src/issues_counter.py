import time
from sentry_report_generator.get_json import get_json_list


def main():
    """
    Parses json and calculates issues count per day.
    :return: timestamp and issue count per day.
    """
    json_list = get_json_list()
    if setup
    if json_list:
        for json_day in json_list:
            issues_counter = 0
            date = time.strftime("%Y-%m-%d", time.gmtime(json_day[-1][0]))
            print("Date: {}".format(date))
            for pair in json_day:
                issues_counter += pair[1]
            print("Total issues per day: {}".format(issues_counter))
    else:
        pass

main()

