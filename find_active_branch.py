import logging
import subprocess
import os
import sys

def find_active_branch():
    """Get current active branch name"""
    currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name

    logging.info(f"Get active branch name")
    logging.info(f"Current working directory: {os.getcwd()}")
    try:
        # lv_cmd = 'git rev-parse --abbrev-ref HEAD'
        lv_cmd = 'git branch --show-current'
        lv_result = subprocess.run(lv_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        lv_ref_name = lv_result.stdout.decode().strip()
        if not lv_ref_name:
            logging.info(f"HEAD is detached")
            lv_cmd = 'cat .git/HEAD'
            lv_result = subprocess.run(lv_cmd, stdout=subprocess.PIPE)
            lv_ref_name = lv_result.stdout.decode('utf-8').strip()
            logging.info(f"Detached HEAD is at {lv_ref_name}")
            
        logging.info(f"active branch: {lv_ref_name}")
        print(f"active branch: {lv_ref_name}")
    except subprocess.CalledProcessError as e:
        logging.error(f"{currentFuncName()}, Error: {e}")
        print(f"No active branch found")
    except FileNotFoundError:
        logging.error(f"{currentFuncName()}, Error: git command not found.")
        print(f"No active branch found")
