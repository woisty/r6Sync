import os
import shutil
import sys

def sync_settings_file(base_dir):
    # Path to the GameSettings.ini file in the root of the selected directory
    settings_file = os.path.join(base_dir, "GameSettings.ini")

    # Print the base directory and settings file for debugging
    print(f"Base directory: {base_dir}")
    print(f"Settings file path: {settings_file}")

    # Ensure the original GameSettings.ini file exists
    if not os.path.isfile(settings_file):
        print("GameSettings.ini not found in the base directory.")
        return

    # echos through all subdirectories in the base directory
    for subdir_name in os.listdir(base_dir):
        subdir_path = os.path.join(base_dir, subdir_name)
        # Check if it's a directory and skip 'sync_settings.exe'
        if os.path.isdir(subdir_path) and subdir_name != "Sync.exe":
            dest_file = os.path.join(subdir_path, "GameSettings.ini")
            # Replace the GameSettings.ini file in each profile directory
            if os.path.isfile(dest_file):
                shutil.copy2(settings_file, dest_file)
                print(f"Replaced {dest_file}")

if __name__ == "__main__":
    if getattr(sys, 'frozen', False):
        base_directory = os.path.dirname(sys.executable)
    else:
        base_directory = os.path.dirname(os.path.abspath(__file__))

    # Debugging: Print the directory where the script is running from
    print(f"Script is running from: {base_directory}")

    if os.path.isdir(base_directory):
        sync_settings_file(base_directory)
    else:
        print("Invalid directory path.")
