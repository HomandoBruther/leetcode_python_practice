
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_as_string = str(x)    # convert x to string

        if str(x) == x_as_string[::-1]: #compare converted string to itself backwards
            return True
        else:
            return False


solution = Solution()

case1 = 121
case2 = -121
case3 = 10


solution.isPalindrome(case1)
solution.isPalindrome(case2)
solution.isPalindrome(case3)


# should and gives: true, false, false