import logging
import subprocess
import os

def is_modified():
    """Check if any files are modified"""
    logging.info(f"Current working directory: {os.getcwd()}")

    lv_cmd = 'git diff-index --quiet HEAD'
    lv_result = subprocess.run(lv_cmd, stdout=subprocess.PIPE, shell=True)
    lv_return_code = lv_result.returncode
    return lv_return_code != 0