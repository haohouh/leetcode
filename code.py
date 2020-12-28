
"1234"
["4"]
"34"
"43"
"234"
"324"
"342"



class Solution(object):

    def permutation(self,word):
        index = 0
        return self.backtracking(word,0)

    def backtracking(self,word,index):
        if index == len(word) - 1:
            return [word[index]]
        
        resToAdd = self.backtracking(word,index+1)
        res = []
        for item in resToAdd:
            for i in range(len(item)):
                res.append(item[0:i] + word[index] + item[i:] )
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.permutation("123"))
        

        