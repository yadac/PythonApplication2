import shutil

# escape seaquence \\
shutil.copy("a\\aaa.txt", "b\\ccc.txt")

shutil.move("b\\ccc.txt", "b\\ddd.txt")

shutil.copytree("C:\\temp\\csharp", "temp\\qsharp")