import logging
import subprocess
import os
import sys

def is_modified(pv_git_dir):
    """Check if any files are modified"""
    currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name

    logging.info(f"Check whether repository files have been modified")
    logging.info(f"Current working directory: {os.getcwd()}")

    lv_is_modified = False
    try:
        lv_cmd = 'git -C ' + pv_git_dir + ' diff'
        lv_result = subprocess.run(lv_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        lv_diff = lv_result.stdout.decode().strip()
        lv_is_modified = lv_diff != ""
    except subprocess.CalledProcessError as e:
        logging.error(f"{currentFuncName()}, Error: {e}")
    except FileNotFoundError:
        logging.error(f"{currentFuncName()}, Error: git command not found.")

    print(f"local changes: {lv_is_modified}")
    logging.info(f"local changes: {lv_is_modified}")
