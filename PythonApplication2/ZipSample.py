import zipfile

# read ziped file
files = zipfile.ZipFile("c:\\temp\\csharp.zip")

# confirm
print(files.namelist())

# unzip
files.extractall("extract-here")

# dispose
files.close()

# create zip file
zf = zipfile.ZipFile("zipedFile.zip", mode = "w")

# add file to zip
zf.write("a")
zf.write("b")

# dispose
zf.close()

