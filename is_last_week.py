import logging
import subprocess
import os
import sys
from datetime import datetime, timedelta, date

def get_head_commit_time(pv_git_dir):
    """Get authorized datetime of HEAD commit in UNIX timestamp"""
    currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name
    logging.info(f"Current working directory: {os.getcwd()}")
    
    lv_epoch_time = None
    try:
        # %at gets author date, UNIX timestamp
        lv_cmd = 'git -C ' + pv_git_dir + ' log -1 --pretty=format:%at HEAD'
        lv_result = subprocess.run(lv_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        lv_epoch_time = float(lv_result.stdout.decode('utf-8'))
        
        lv_datetime = datetime.fromtimestamp(float(lv_epoch_time)) 
        logging.info(f"Authorized datetime: {lv_datetime}") 
    except subprocess.CalledProcessError as e:
        logging.error(f"{currentFuncName()}, Error: {e}")
    except FileNotFoundError:
        logging.error(f"{currentFuncName()}, Error: git command not found.")
    return lv_epoch_time

def is_last_week(pv_git_dir):
    """Check if the given datetime is in the last week."""
    logging.info(f"Check whether repository files have been modified")

    lv_datetime = get_head_commit_time(pv_git_dir)
    lv_is_lastweek = False
    if lv_datetime:
        lv_today = date.today()

        lv_week_ago = lv_today - timedelta(days=7)
        lv_start = lv_week_ago - timedelta(days=lv_week_ago.weekday())
        lv_end = lv_start + timedelta(days=6)

        logging.info(f"Start day of last week is : {lv_start}")
        logging.info(f"End day of last week is : {lv_end} (inclusive)")

        lv_start_time = datetime(lv_start.year, lv_start.month, lv_start.day).timestamp()
        lv_end_time = datetime(lv_end.year, lv_end.month, lv_end.day, 23, 59, 59).timestamp()
        lv_is_lastweek = lv_start_time <= lv_datetime <= lv_end_time
    logging.info(f"recent commit: {lv_is_lastweek}")
    print(f"recent commit: {lv_is_lastweek}")