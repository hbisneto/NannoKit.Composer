import filesystem as fs
from filesystem import directory

folders_list = ["examples/", "nannokit/", "tests/"]

def create_folders(default_directory):
    print(default_directory)
    for f in folders_list:
        folder_path = f'{default_directory}/{f}'
        directory.create(folder_path)
