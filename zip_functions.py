import zipfile as zf
import pathlib as pl

def create_archive(filepaths, destination):
    folder_destination = pl.Path(destination, "compressed.zip")
    with zf.ZipFile(folder_destination, 'w') as archive:
        for filepath in filepaths:
            filepath = pl.Path(filepath)
            archive.write(filepath, arcname=filepath.name)