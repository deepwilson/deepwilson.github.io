import os
import shutil

MEIN_PLATZ = r"H:\0ut51d3r5.17711\Google Drive\_hlu.Projects\Mein.Platz"
OUTSIDERS17711_FASTPAGES = (
    r"H:\0ut51d3r5.17711\Google Drive\_hlu.Projects\Outsiders17711.FastPages"
)


for dirpath, dirnames, dirfiles in os.walk(MEIN_PLATZ):
    for folder in dirnames:
        folderpath = os.path.join(dirpath, folder)
        if folder in ["_notebooks", "_posts", "images"]:
            mirror_folderpath = os.path.join(OUTSIDERS17711_FASTPAGES, folder)
            shutil.rmtree(mirror_folderpath, ignore_errors=True)
            shutil.copytree(folderpath, mirror_folderpath)

        if folder == "_stashedPosts":
            for _, _, stashedfiles in os.walk(folderpath):
                for file in stashedfiles:
                    if file not in [
                        "changeLog.ipynb",
                        "fastai.fastpages.master.README.md",
                    ]:
                        filepath = os.path.join(folderpath, file)
                        if os.path.splitext(filepath)[1] == ".ipynb":
                            mirror_filepath = os.path.join(
                                OUTSIDERS17711_FASTPAGES, f"_notebooks\\{file}"
                            )
                            shutil.copy2(filepath, mirror_filepath)
                        elif os.path.splitext(filepath)[1] == ".md":
                            mirror_filepath = os.path.join(
                                OUTSIDERS17711_FASTPAGES, f"_posts\\{file}"
                            )
                            shutil.copy2(filepath, mirror_filepath)

    for file in dirfiles:
        filepath = os.path.join(dirpath, file)
        if file in [".gitactions.ipynb", "changeLog.ipynb", ".syncBlogs.py"]:
            mirror_filepath = os.path.join(
                OUTSIDERS17711_FASTPAGES, f"_stashedPosts\\{file}"
            )
            shutil.copy2(filepath, mirror_filepath)
