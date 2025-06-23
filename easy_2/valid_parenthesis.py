#!/usr/bin/env python3

class Solution:
    def isValid(self, s: str) -> bool:
        opening_parenthesis = {'{', '(', '['}
        corresponding_parenthesis = {
            '}': '{',
            ')': '(',
            ']': '['
        }

        parenthesis = []
        for b in s:
            if b in opening_parenthesis:
                parenthesis.append(b)
            else:
                if not parenthesis: ## if it's empty
                    return False

                last_element = parenthesis.pop()
                if last_element != corresponding_parenthesis[b]:
                    return False

        return not parenthesis # True if parenthesis is empty


s = "()"
print(Solution().isValid(s))

s = "()[]{}"
print(Solution().isValid(s))

s = "(]"
print(Solution().isValid(s))

s = "([])"
print(Solution().isValid(s))

s = "["
print(Solution().isValid(s))

s = "]"
print(Solution().isValid(s))
