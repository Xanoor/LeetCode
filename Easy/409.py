class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters_set = set()
        result = 0

        for i in s:
            if i in letters_set:
                result+=2
                letters_set.remove(i)
            else:
                letters_set.add(i)

        if letters_set:
            result+=1

        return result
        
# print(Solution.longestPalindrome(Solution, "abcbc"))
# 4ms 12.56Mb