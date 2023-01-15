import logging
import subprocess
import os

def find_active_branch():
    """Get current active branch name"""
    logging.info(f"Get active branch name")
    logging.info(f"Current working directory: {os.getcwd()}")
    try:
        lv_cmd = 'git rev-parse --abbrev-ref HEAD'
        # git branch --show-current
        lv_result = subprocess.run(lv_cmd, stdout=subprocess.PIPE, shell=True)
        lv_ref_name = lv_result.stdout.decode('utf-8').strip()
    
        if lv_ref_name == "HEAD":
            logging.info(f"HEAD is detached")
            lv_cmd = 'cat .git/HEAD'
            lv_result = subprocess.run(lv_cmd, stdout=subprocess.PIPE)
            lv_ref_name = lv_result.stdout.decode('utf-8').strip()
            logging.info(f"Detached HEAD is at {lv_ref_name}")
            
        logging.info(f"active branch: {lv_ref_name}")
        print(f"active branch: {lv_ref_name}")
    except:
        print(f"No active branch found")


def get_active_branch():
    try:
        git_cmd = ["git", "rev-parse", "--abbrev-ref", "HEAD"]
        lv_ref_name = subprocess.run(git_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True).stdout.strip().decode()
        print(f"active branch: {lv_ref_name}")
    except subprocess.CalledProcessError as e:
        if e.returncode == 128:
            print(f"No active branch found")
        else:
            print(f"Error: {e}")
    except FileNotFoundError:
        print("Error: git command not found.")
