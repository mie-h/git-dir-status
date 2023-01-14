import logging
import subprocess
import os

def get_active_branch():
    """Get current active branch name"""
    logging.info(f"Current working directory: {os.getcwd()}")

    lv_cmd = 'git rev-parse --abbrev-ref HEAD'
    lv_result = subprocess.run(lv_cmd, stdout=subprocess.PIPE, shell=True)
    lv_ref_name = lv_result.stdout.decode('utf-8').strip()
    if lv_ref_name == "HEAD":
        logging.info(f"HEAD is detached")
        lv_cmd = 'cat .git/HEAD'
        lv_result = subprocess.run(lv_cmd, stdout=subprocess.PIPE)
        lv_ref_name = lv_result.stdout.decode('utf-8').strip()
        logging.info(f"Detached HEAD is at {lv_ref_name}")
    return lv_ref_name