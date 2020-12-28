class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        op = {"+":lambda x,y: x+y, "-":lambda x,y: x-y, "*":lambda x,y: x*y, "/":lambda x,y: int(float(x)/y)}
        expList = []
        newStr = ""
        for letter in s:
            if letter == " ":
                continue
            else:
                newStr += letter
        lowerBound = 0
        for i,letter in enumerate(newStr):
            if letter in "()+-*/":
                if lowerBound != i:
                    expList.append(newStr[lowerBound:i])
                expList.append(letter)
                lowerBound = i + 1
        if lowerBound != len(newStr):
            expList.append(newStr[lowerBound:len(newStr)])
        suffixExpress = []
        opStack = []
        for letter in expList:
            if letter.isdigit():
                suffixExpress.append(letter)
            elif letter == ")":
                while opStack and opStack[-1] != "(":
                    suffixExpress.append(opStack.pop())
                opStack.pop()
            elif letter == "(":
                opStack.append(letter)
            elif letter in "+-":
                while opStack and opStack[-1] != "(":
                    suffixExpress.append(opStack.pop())
                opStack.append(letter)
            elif letter in "*/":
                while opStack and opStack[-1] not in "(+-":
                    suffixExpress.append(opStack.pop())
                opStack.append(letter)
        while opStack:
            suffixExpress.append(opStack.pop())
        resStack = []
        for item in suffixExpress:
            if item.isdigit():
                resStack.append(int(item))
            else:
                b = resStack.pop()
                a = resStack.pop()
                resStack.append(op[item](a,b))
        return resStack[-1]
                                      