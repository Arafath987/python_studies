import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            y = x
            z = 0
            while y >= 1:
                last_digit = y % 10
                y = math.floor(y / 10)
                z = z * 10 + last_digit
            if x == z:
                return True
            else:
                return False


x = Solution()
y = x.isPalindrome(12)
print(y)
