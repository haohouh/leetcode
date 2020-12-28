class FileSystem(object):

    def __init__(self):
        self.fileSystem = {}

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        if path == "/":
            lst = []
        else:
            path = path.lstrip("/")
            lst = path.split("/")
        cur = self.fileSystem
        for letter in lst:
            cur = cur[letter]
        if isinstance(cur,str):
            return lst[-1]
        else:
            return list(sorted(cur.keys()))
        

    def mkdir(self, path):
        """
        :type path: str
        :rtype: None
        """
        path = path.strip("/")
        lst = path.split("/")
        root = self.fileSystem
        for letter in lst:
            root = root.setdefault(letter,{})
            
            
        

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: None
        """
        filePath = filePath.lstrip("/")
        lst = filePath.split("/")
        directory = lst[:-1]
        fileName = lst[-1]
        cur = self.fileSystem
        for letter in directory:
            cur = cur[letter]
        if fileName not in cur:
            cur[fileName] = content
        else:
            cur[fileName] = cur[fileName] + content
        

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        filePath = filePath.lstrip("/")
        lst = filePath.split("/")
        directory = lst[:-1]
        fileName = lst[-1]
        cur = self.fileSystem
        for letter in directory:
            cur = cur[letter]
        return cur[fileName]    

if __name__ == "__main__":
    s = FileSystem()
    s.mkdir("/goowmfn")
    s.ls("/goowmfn")
    s.ls("/")
    s.mkdir("/z")
    s.ls("/")
    s.ls("/")
    s.addContentToFile("/goowmfn/c","shetopcy")
    s.ls("/z")
    s.ls("/goowmfn/c")
    s.ls("/goowmfn")
    """

    ["FileSystem","mkdir","ls","ls","mkdir","ls","ls","addContentToFile","ls","ls","ls"]
[[],["/goowmfn"],["/goowmfn"],["/"],["/z"],["/"],["/"],["/goowmfn/c","shetopcy"],["/z"],["/goowmfn/c"],["/goowmfn"]]
"""