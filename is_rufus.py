import logging
import subprocess
import os

def get_head_commit_author():
    """Get author name of HEAD commit in UNIX timestamp"""
    logging.info(f"Current working directory: {os.getcwd()}")

    try:
        # %an gets author name
        lv_cmd = 'git log -1 --pretty=format:%an HEAD'
        lv_result = subprocess.run(lv_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        lv_name = lv_result.stdout.decode('utf-8')
        logging.info(f"Author name is: {lv_name}")
        return lv_name
    except:
        return

def is_rufus():
    """Check is given name is Rufus"""
    lv_name = get_head_commit_author()
    return lv_name == "Rufus"