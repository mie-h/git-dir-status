## 🌟 About The Project

This program prints specific facts about a local git repository.
This program takes in one argument `git_dir` -- directory in which to assess git status.
This program prints the following things:

- active branch (string)
- whether repository files have been modified (boolean)
- whether the current head commit was authored in the last week (boolean)
- whether the current head commit was authored by Rufus (boolean)

## ⚙️ Getting Started

### Installation

1.  Clone the repo

```sh
git clone https://github.com/mie-h/git-dir-status.git
```

2. Install packages
   ```sh
   pip3 install -r requirements.txt
   ```

## 🏃 Usage

Run the program using following command.

```sh
   python3 interface.py --git_dir <path to git repo>
```

This will create `interface.log` file and output the following:

```
active branch: master
local changes: False
recent commit: True
blame Rufus: True
```

For more detailed logs, please check `interface.log` file.

## 🚩 Note

- When HEAD is detached, `active branch` will show commit ID
- `recent commit` is defined as start time of previsous week's Monday 00:00:00 and end time of previous week's Sunday 23:59:59. For example, if today is January 14, then any commit between January 2, 00:00:00 and January 8, 23:59:59 will be considered as `recent commit`
