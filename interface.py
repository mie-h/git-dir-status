import argparse
import logging
import os
import git
from find_active_branch import find_active_branch
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

    find_active_branch(pv_git_dir)
    is_modified(pv_git_dir)
    is_last_week(pv_git_dir)
    is_rufus(pv_git_dir)

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