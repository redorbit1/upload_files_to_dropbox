import dropbox
import re
import glob

# Absolute path of source folder
src_dir = "/opt/dropbox/test"

# Glob files filter for target files including subfolders. 
# This will get all files and subfolders of /root/test
src_files_glob = "/**/*"
# src_files_glob = "/*" # work first folder only 
# src_files_glob = "/*.csv" # work with CSV files only
# src_files_glob = "/**/*.csv" # first level and subfolder but CSV files only

# Destination folder in Dropbox
dst_dir = "/backup"

# API Token - see https://www.dropbox.com/developers/apps
token = ""
# Create API object
d = dropbox.Dropbox(token)

# Get all source files
src_files = glob.glob(src_dir + src_files_glob)

# Checks if folder is empty
if len(src_files) == 0:
	exit("No files to upload from " + src_dir + " matching glob filter " + src_files_glob)

# Print list of files to be seen when running script interactively
print("Working with source files:")
print(src_files)

# Loop through each of files in src_dir and write them
for src_file in src_files:
	fp = open(src_file, "rb")
	dst_file_dropbox = dst_dir + src_file
	dst_file_dropbox = dst_file_dropbox.replace(src_dir, "")
	print("Uploading " + src_file + " to Dropbox: " + dst_file_dropbox)
	meta = d.files_upload(fp.read(), dst_file_dropbox, mode=dropbox.files.WriteMode("overwrite"))

print("Upload finished")
