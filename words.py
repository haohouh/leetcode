"""
Input: ["abch", "ell", "out"], "hello"

output: [0, 3]

["abhel","lalo","bcd"],"hello" : -1
["hello","abc","bcd"],"hello" :[0,0]
["adfs","abc","hello"],"hello" :[2,0]
["abch", "ell", "out"],"hello": [0,3]
["", "abc",""], "" : [0,0]
["abhel","lalo","bcd","hello"], hello :[0,3]
["","hello", "abc"],hello : [1,0]
["hello","", "abc"],hello :[]
Input: ["abchh", "hhell", "out"], "hhhello", output: [0, 4]
"""

class Solution(object):

    def getWordPosition(self,wordList,word):
        if len(word) == 0:
            if "" in wordList:
                return [wordList.index(""),0]
            else:
                return -1
        i = 0 # to track the current index of the word
        j = 0 # iterate the wordList array
        startWord = 0
        startIndex = 0
        nextIndex = 0
        while j < len(wordList):
            if i == 0:
                idx = wordList[j][next] = find(word[i])
                if idx == -1:
                    j = j + 1
                else:
                    startWord = j
                    startIndex = idx
                    nextIndex = idx + 1
                    if nextIndex == len( wordList[j])
                        j = j + 1
                        nextIndex = 0
                    i = i + 1
                    if i == len(word):
                        return [startWord,startIndex]
                    continue
            else:
                if wordList[j][nextIndex] == word[i]:
                    if nextIndex == len(wordList[j]) -1:
                        nextIndex = 0
                        j = j + 1
                        i = i + 1
                        if i == len(word):
                            return [startWord,startIndex]
                    else:
                        nextIndex += 1
                        i  = i + 1
                        if i == len(word):
                            return [startWord,startIndex]
                else:
                    j = j + 1
                    i = 0
                    nextIndex = 0
        return -1


