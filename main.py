import extractor, os, shutil
from traceback import format_exc
from glob import glob

def getAssetFolders(folder):
    folders = []
    for child_folder in os.listdir(folder):
        folders.append("{}\\".format(os.path.join(folder, child_folder)))
    return folders

def start(file_name):
    extractor.extract(file_name)
    folder = extractor.getFolder(file_name)
    for asset in getAssetFolders("_{}".format(folder)):
        pathname = ""
        with open(asset + "pathname", encoding = "UTF-8") as f:
            pathname = "{}/{}".format(folder, f.read())
        pathname = pathname.split("/")
        file_name = pathname[-1]
        print('Unpacking "{}"'.format(file_name))
        del pathname[-1]
        folder_path = "/".join(pathname)
        try:
            os.makedirs(folder_path)
        except:pass
        try:
            os.rename(asset + "asset", "{}/{}".format(folder_path, file_name))
        except:pass
        try:
            os.rename(asset + "asset.meta", "{}/{}.meta".format(folder_path, file_name))
        except:pass
    shutil.rmtree("_{}".format(folder))

def main():
    file_name = input("Enter file name: ")
    if file_name.lower() == "all":
        for file in glob("*.unitypackage"):
            start(file)
    else:
        start(file_name)


if __name__ == "__main__":
    try:
        main()
    except:
        print(format_exc())
    input("done")