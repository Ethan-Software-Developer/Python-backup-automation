import os
import shutil
from datetime import datetime

def backup_files(source_dir, backup_dir):
    # Get the current date to create a timestamped backup folder
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_folder = os.path.join(backup_dir, f"backup_{timestamp}")

    # Create the backup directory if it doesn't exist
    os.makedirs(backup_folder, exist_ok=True)

    # Iterate through all files and directories in the source directory
    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        backup_path = os.path.join(backup_folder, item)

        try:
            # If it's a file, copy it
            if os.path.isfile(source_path):
                shutil.copy2(source_path, backup_path)
                print(f"Copied file: {source_path} to {backup_path}")
            # If it's a directory, copy it recursively
            elif os.path.isdir(source_path):
                shutil.copytree(source_path, backup_path)
                print(f"Copied directory: {source_path} to {backup_path}")
        except Exception as e:
            print(f"Error copying {source_path}: {e}")

if __name__ == "__main__":
    source_directory = r"C:\Users\Ethan\Downloads"  # Replace with your source directory
    backup_directory = r"E:\Archives"  # Replace with your backup directory

    backup_files(source_directory, backup_directory)
