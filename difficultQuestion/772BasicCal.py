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
        opStack = []
        numStack = []
        for letter in expList:
            if letter.lstrip("-").isdigit():
                numStack.append(int(letter))
            else:
                if len(opStack) == 0 or letter == "(":
                    opStack.append(letter)
                elif letter != ")" and opStack[-1] == "(":
                    opStack.append(letter)
                elif letter == ")":
                    while opStack[-1] != "(":
                        b = numStack.pop()
                        a = numStack.pop()
                        numStack.append(op[opStack.pop()](a,b))
                    opStack.pop()
                elif letter in "*/":
                    if opStack[-1] in "+-(":
                        opStack.append(letter)
                    else:
                        while opStack and opStack[-1] not in "(+-":
                            b = numStack.pop()
                            a = numStack.pop()
                            numStack.append(op[opStack.pop()](a,b))
                        opStack.append(letter)
                elif letter in "+-":
                    while opStack and opStack[-1] not in "(":
                            b = numStack.pop()
                            a = numStack.pop()
                            numStack.append(op[opStack.pop()](a,b))
                    opStack.append(letter)
        while opStack:
            b = numStack.pop()
            a = numStack.pop()
            numStack.append(op[opStack.pop()](a,b))
        return numStack[-1]