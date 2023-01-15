import logging
import subprocess
import os
import sys

def get_head_commit_author(pv_git_dir):
    """Get author name of HEAD commit in UNIX timestamp"""
    currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name

    logging.info(f"Current working directory: {os.getcwd()}")
    lv_name = None
    try:
        # %an gets author name
        lv_cmd = 'git -C ' + pv_git_dir + ' log -1 --pretty=format:%an HEAD'
        lv_result = subprocess.run(lv_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        lv_name = lv_result.stdout.decode('utf-8')
        logging.info(f"Author name is: {lv_name}")
    except subprocess.CalledProcessError as e:
        logging.error(f"{currentFuncName()}, Error: {e}")
    except FileNotFoundError:
        logging.error(f"{currentFuncName()}, Error: git command not found.")
    return lv_name

def is_rufus(pv_git_dir):
    """Check is given name is Rufus"""
    logging.info(f"Check whether the current head commit was authored by Rufus")
    lv_name = get_head_commit_author(pv_git_dir)
    lv_is_rufus = lv_name == "Rufus"
    print(f"blame Rufus: {lv_is_rufus}")
    logging.info(f"blame Rufus: {lv_is_rufus}")
