from pathlib import Path
import os
import shutil

# getting the possible extensions
file_extensions = ['.svg', '.png']

# accessing the downloads folder
downloads_folder = Path.home() / 'Downloads'

# creating a folder
# iterate through a list
for extent in file_extensions:
    if os.path.exists(f'{downloads_folder}\\{extent}s'):
        print("Folder already exists")
    else:
        os.makedirs(f'{downloads_folder}\\{extent}s')


# list of files in a folder
for file_name in os.listdir(downloads_folder):
    for extension in file_extensions:
        if extension in file_name:
            source_path = downloads_folder / file_name
            destination_folder = downloads_folder / f"{extension}s"

            try:
                shutil.move(source_path, destination_folder)
                print(f"Item {file_name} already moved to the folder")
            except FileNotFoundError:
                print(f"File {file_name} doesn't exists")
