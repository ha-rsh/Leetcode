from collections import Counter

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if not stack:
                    return False
                c = stack.pop()
                if c == "(":
                    if i != ")":
                        return False
                if c == "{":
                    if i != "}":
                        return False
                if c == "[":
                    if i != "]":
                        return False

        if stack:
            return False
        return True
