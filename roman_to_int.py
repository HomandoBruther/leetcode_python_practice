class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        '''
        no need to convert s to int with use of dictionary, int value already assigned to numeral
        need result to add to the result that we may need to subtract from after new numeral iteration
        give the string of numerals in reverse to check if new value is smaller than the value before it
        if so subtract the new lower value with result
        previous value variable ensures we store what previous value was to keep operations going
        '''

        result = 0
        previous_value = 0

        for numeral in reversed(s):
            value = roman[numeral]

            if value < previous_value:
                result -= value

            else:
                result += value

            previous_value = value

        return result
        #print(result)


solution = Solution()

case1 = "III"
case2 = "LVIII"
case3 = "MCMXCIV"


solution.romanToInt(case1)
solution.romanToInt(case2)
solution.romanToInt(case3)
