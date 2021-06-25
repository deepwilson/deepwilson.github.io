import os
import shutil

dirHluPy = r"H:\0ut51d3r5.17711\Google Drive\_hlu.Projects\Mein.Platz"


def delPycacheFolders(targetFolder=dirHluPy):
    for dirpath, dirnames, _ in os.walk(targetFolder):
        for folder in dirnames:
            if folder in ["__pycache__", "__MACOSX", ".ipynb_checkpoints"]:
                folderpath = os.path.join(dirpath, folder)
                shutil.rmtree(folderpath)


delPycacheFolders()
