// 20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            match ch:
                case '(' | '{' | '[':
                    stack.append(ch)
                case ')':
                    if not stack or stack.pop() != '(':
                        return False
                case '}':
                    if not stack or stack.pop() != '{':
                        return False
                case ']':
                    if not stack or stack.pop() != '[':
                        return False

        return not stack
