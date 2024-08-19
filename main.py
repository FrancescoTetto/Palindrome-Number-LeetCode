class Solution(object):
    def isPalindrome(self, x):
        str_x = str(x)
        if str_x == str_x[::-1]:
            return True
        else:
            return False

solution = Solution()

print(solution.isPalindrome(121))
print(solution.isPalindrome(-121))
print(solution.isPalindrome(10))
