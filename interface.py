import argparse
import logging
import os
import git
from find_active_branch import find_active_branch, get_active_branch
from is_modified import is_modified
from is_last_week import is_last_week
from is_rufus import is_rufus

def is_git_repo(path):
    try:
        _ = git.Repo(path).git_dir
        return True
    except:
        return False

def driver(pv_git_dir):
    # check if git directory is valid
    if not is_git_repo(pv_git_dir):
        print(f"{pv_git_dir} Not a git repo")
        logging.error(f"git_dir is not git repo or invalid")
        return -1
    
    logging.info(f"Check status of directory: {pv_git_dir}")
    os.chdir(pv_git_dir)
    logging.info(f"Changed directory to {pv_git_dir}")

    
    # find_active_branch()
    get_active_branch()
    
    logging.info(f"Check whether repository files have been modified")
    lv_is_modified = is_modified()
    logging.info(f"local changes: {lv_is_modified}")

    is_last_week()

    logging.info(f"Check whether the current head commit was authored by Rufus")
    lv_is_rufus = is_rufus()
    logging.info(f"blame Rufus: {lv_is_rufus}")

    print(f"local changes: {lv_is_modified}")
    print(f"blame Rufus: {lv_is_rufus}")

    logging.info(f"Output on stdout successful")
    return 0

def main():
    lv_filename = os.path.basename(__file__)
    lv_log_filename = os.path.splitext(lv_filename)[0] + ".log"
    logging.basicConfig(filename = lv_log_filename,
                        format='%(asctime)s %(levelname)s:%(message)s',
                        level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument(
            "--git_dir", type=str, required=True,
            help="directory in which to assess git status"
    )
    args = parser.parse_args()

    lv_error = driver(args.git_dir)
    if lv_error == -1:
        logging.info("Exited due to error.")
        return
    logging.info("Task completed")

if __name__ == '__main__':
    main()