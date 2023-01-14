import logging
import subprocess
import os
from datetime import datetime, timedelta, date

def get_head_commit_time():
    """Get authorized datetime of HEAD commit in UNIX timestamp"""
    logging.info(f"Current working directory: {os.getcwd()}")

    # %at gets author date, UNIX timestamp
    lv_cmd = 'git log -1 --pretty=format:%at HEAD'
    lv_result = subprocess.run(lv_cmd, stdout=subprocess.PIPE, shell=True)
    lv_epoch_time = float(lv_result.stdout.decode('utf-8'))
    lv_datetime = datetime.fromtimestamp(float(lv_epoch_time)) 
    logging.info(f"Authorized datetime: {lv_datetime}") 
    return lv_epoch_time

def is_last_week():
    """Check if the given datetime is in the last week."""
    lv_datetime = get_head_commit_time()

    lv_today = date.today()

    lv_week_ago = lv_today - timedelta(days=7)
    lv_start = lv_week_ago - timedelta(days=lv_week_ago.weekday())
    lv_end = lv_start + timedelta(days=6)

    logging.info(f"Start day of last week is : {lv_start}")
    logging.info(f"End day of last week is : {lv_end} (inclusive)")

    lv_start_time = datetime(lv_start.year, lv_start.month, lv_start.day).timestamp()
    lv_end_time = datetime(lv_end.year, lv_end.month, lv_end.day, 23, 59, 59).timestamp()
    return lv_start_time <= lv_datetime <= lv_end_time