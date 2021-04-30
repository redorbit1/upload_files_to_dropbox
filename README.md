# Upload Files to Dropbox

# Description
The purpose of this simple Python script is to automatically upload files to Dropbox.
The script will upload files and folders recursively starting from a base path.
Glob filter is supported, so you can upload main folder only, specific file extension or both

# Use Cases
- Automatic backup to Dropbox using CRON or Scheduled Task
- Sync local files to Dropbox
- Automate sharing files with others on shared folder

# Requirements
- Install Python 3.x
- Install pip3
- Install dropbox module using "pip3 install dropbox"
- Dropbox API Token

# How To Use
- Update src_dir to be the local folder you want to upload
- Update dst_dir to the dropbox destination folder. It will be created if it doesn't exist
- Update token to your Dropbox API token

