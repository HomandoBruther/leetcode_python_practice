from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        '''
        empty string to add letter to
        need to take into account the position of letters as well
        used index brackets to check if letters in all words are equal. if so append into common_letters
        if no more simular letters, break and return common_letters
        '''

        common_letters = ""

        if strs:
            shortest_word = min(len(letters) for letters in strs)
            for letter_to_check in range(shortest_word):
                if all(letters[letter_to_check] == strs[0][letter_to_check] for letters in strs):
                    common_letters += strs[0][letter_to_check]
                else:
                    break

        return common_letters


solution = Solution()


strs1 = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]


solution.longestCommonPrefix(strs1)
solution.longestCommonPrefix(strs2)