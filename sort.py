from pathlib import Path
import os
import shutil

# getting the possible extensions
file_extensions = [
    '.jpg', '.jpeg', '.png', '.gif', '.bmp',  # Image formats
    '.pdf', '.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx',  # Document formats
    '.mp3', '.wav',  # Audio formats
    '.mp4', '.avi', '.mkv', '.mov',  # Video formats
    '.txt', '.csv', '.json', '.xml',  # Text and data formats
    '.zip', '.rar', '.tar', '.gz', '.7z',  # Archive formats
    '.html', '.css', '.js', '.php',  # Web-related formats
    '.exe', '.sh',  # Executable and script formats
    '.svg', '.psd', '.ai',  # Design and graphics formats
    '.dat', '.db', '.sqlite',  # Database formats
    '.log', '.ini', '.cfg',  # Configuration and log formats
    '.iso', '.img', '.vhd',  # Disk image formats
]


# accessing the downloads folder
downloads_folder = Path.home() / 'Downloads'


# list of files in a folder
for file_name in os.listdir(downloads_folder):

    for extension in file_extensions:

        if extension in file_name:

            for extent in extension:
                if os.path.exists(f'{downloads_folder}\\{extent}s'):
                    print("Folder already exists")
                else:
                    os.makedirs(f'{downloads_folder}\\{extent}s')

            source_path = downloads_folder / file_name
            destination_folder = downloads_folder / f"{extension}s"

            try:
                shutil.move(source_path, destination_folder)
                print(f"Item {file_name} already moved to the folder")
            except FileNotFoundError:
                print(f"File {file_name} doesn't exists")
