import os
import shutil

def organize_files(folder_path):
    # Get a list of all files in the specified folder
    files = os.listdir(folder_path)

    for file in files:
        # Get the full path of the file
        file_path = os.path.join(folder_path, file)

        # Check if the item is a file
        if os.path.isfile(file_path):
            # Get the file extension
            _, file_extension = os.path.splitext(file)

            # Create a destination folder based on the file extension
            destination_folder = os.path.join(folder_path, file_extension[1:].lower())

            # Create the destination folder if it doesn't exist
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            # Move the file to the destination folder
            shutil.move(file_path, destination_folder)

if __name__ == '__main__':
    desktop_path = os.path.expanduser("~/Desktop")  # Path to the desktop folder
    organize_files(desktop_path)