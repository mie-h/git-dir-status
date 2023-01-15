import logging
import subprocess
import os

def is_modified():
    """Check if any files are modified"""

    logging.info(f"Check whether repository files have been modified")
    logging.info(f"Current working directory: {os.getcwd()}")

    try:
        lv_cmd = 'git diff-index --quiet HEAD'
        lv_result = subprocess.run(lv_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        lv_result.stdout.strip().decode()
        lv_return_code = lv_result.returncode
        lv_is_modified = lv_return_code != 0
    except Exception as e:
        logging.error(f"Error {e}")
        return 
    
    print(f"local changes: {lv_is_modified}")
    logging.info(f"local changes: {lv_is_modified}")
