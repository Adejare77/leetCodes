#!/usr/bin/env python3

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower()
#         left, right = 0, len(s) - 1

#         while left < right:
#             if not s[left].isalnum():
#                 left += 1
#                 continue
#             elif not s[right].isalnum():
#                 right -= 1
#                 continue

#             if s[left] != s[right]:
#                 return False

#             left += 1
#             right -= 1

#         return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            elif not s[right].isalnum():
                right -= 1
                continue
            if not s[left].isalpha() or not s[right].isalpha():
                if not ord(s[left]) == ord(s[right]):
                    return False
            else:
                if not (ord(s[left]) + 32 == ord(s[right]) or ord(s[left]) - 32 == ord(s[right]) or ord(s[left]) == ord(s[right])):
                    return False

            left += 1
            right -= 1

        return True


s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))

s = ""
print(Solution().isPalindrome(s))

s = "race a car"
print(Solution().isPalindrome(s))

s = "0P"
print(Solution().isPalindrome(s))
