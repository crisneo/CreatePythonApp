import os

class FsHelper:
    def createFile(self, fileName, contents, directory):
        if not os.path.exists(fileName):
            file = open(fileName, "a")
            file.write(contents)
            file.close()

    def createDirectory(self, directoryName):
        if not os.path.exists(directoryName):
            os.mkdir(directoryName)


