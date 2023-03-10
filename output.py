

import os
import shutil
from datetime import datetime, timedelta

# Get current directory
cur_dir = os.getcwd() 

# Get the path of downloads folder
downloads_dir = os.path.join(cur_dir, 'Downloads')

# Get the path of deleted folder
deleted_dir = os.path.join(cur_dir, 'Deleted')

# Create the folder Deleted if not exists
if not os.path.exists(deleted_dir):
    os.mkdir(deleted_dir)

# Get the current date
today = datetime.now()

# Get files from Downloads folder
files = os.listdir(downloads_dir)

# Iterate through files
for file in files:
    # Get the file path
    file_path = os.path.join(downloads_dir, file)
    # Get the modified date
    modified_date = datetime.fromtimestamp(os.path.getmtime(file_path))
    # Check if the modified date is more than 30 days
    if today - modified_date > timedelta(days=30):
        # Move the file to Deleted folder
        shutil.move(file_path, deleted_dir)