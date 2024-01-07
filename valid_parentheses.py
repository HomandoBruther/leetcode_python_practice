class Solution:
    def isValid(self, s: str) -> bool:

        '''
        takes parentheses from s
        checks if theyre from open list first, if so append to balanced
        if it finds a parenthese from the closed list, check if parenthese is the same as the one from open list
        therefore checks if lenght of balanced is not empty, and uses positional brackets to position of closed is same
        to the paranthese stored in balanced. If conditions met, pop them since we no longer need them. comming out to
        balanced being 0

        from: https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/
        so cant take credit
        '''


        open_list = ["(", "{", "["]
        closed_list = [")", "}", "]"]


        balanced = []
        for parentheses in s:
            if parentheses in open_list:
                balanced.append(parentheses)

            elif parentheses in closed_list:
                position = closed_list.index(parentheses)
                if (len(balanced) > 0) and (open_list[position] == balanced[len(balanced)-1]):
                    balanced.pop()
                else:
                    return False

        if len(balanced) == 0:
            return True
        else:
            return False




sul = Solution()

case1 = "()"
case2 = "()[]{}"
case3 = "(]"


sul.isValid(case1)
sul.isValid(case2)
sul.isValid(case3)