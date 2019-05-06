import time
import datetime


def get_epoch_list():
    """
    Determines where it's daylight saving time or not and creates
    a timestamp in epoch format for each day of previous week and for today.
    :return: list of timestamps in epoch format.
    """
    dst = time.localtime().tm_isdst
    # "15:00:00.000" or "16:00:00.000" depends on DST and equals to "23:00:00.000" in gmt
    if dst == 0:
        hours_part = "15:00:00.000"
    elif dst == 1:
        hours_part = "16:00:00.000"
    epoch_list = []
    for day in range(-7, 1):
        date = datetime.datetime.today()+datetime.timedelta(days=day)
        date_time_str = "{}-{}-{} {}".format(date.year, date.month, date.day, hours_part)
        utc_timestamp = time.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
        epoch_date = int(time.mktime(utc_timestamp))
        epoch_list.append(epoch_date)
    return epoch_list
