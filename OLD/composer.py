import filesystem as fs
from filesystem import file
from filesystem import directory
from writter import folders

APPLICATION_FOLDER = f'{fs.documents}/NannoKitComposer/'
folders_list = ["examples/", "nannokit/", "tests/"]
files_list = ["setup.py", "LICENSE", "pyproject.toml", "README.md", "requirements.txt", "CHANGELOG.md"]
print()

def new_extension(ext_name):
    __ext_path__ = f'{APPLICATION_FOLDER}{ext_name}'
    directory.create(__ext_path__)
    ext_path = __ext_path__.replace("_", ".")
    directory.rename(__ext_path__, ext_path)

    folders.create_folders(ext_path)
    
    for f in folders_list:
        path_name = f'{ext_path}/{f}'
        directory.create(path_name)
        print(f"Created {path_name}")
    
    # file.create(f'{ext_path}/')
    print(ext_name)
    print(ext_path)