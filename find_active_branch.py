import logging
import subprocess
import sys

def find_active_branch(pv_git_dir):
    """Get current active branch name"""
    currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name

    logging.info(f"Get active branch name")
    try:
        lv_cmd = 'git -C ' + pv_git_dir + ' branch --show-current'
        lv_result = subprocess.run(lv_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, shell=True)
        lv_ref_name = lv_result.stdout.decode().strip()
        if not lv_ref_name:
            logging.info(f"HEAD is detached")
            lv_cmd = 'cat ' + pv_git_dir + '.git/HEAD'
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
