# First solution (recursive): Combines the words character by character using recursion, but less efficient for long inputs due to memory overhead.
#21ms 12.58Mb

class Solution(object):
    def mergeAlternately(self, word1, word2, s=0):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        if len(str(word1))==0 or len(str(word2))==0:
            return word1+word2
        return (word1[0]+word2[0])+self.mergeAlternately(word1[1:], word2[1:], s+1)
        


# Second solution (iterative): Uses a while loop, making it faster and better suited for long inputs as it avoids recursion limits.
#15ms 12.41Mb

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        str = ""
        l1 = len(word1)
        l2 = len(word2)
        s1 = 0
        s2 =0
        while s1 < l1 or s2 < l2:
            if s1 < l1:
                str+=word1[s1]
                s1+=1
            if s2 < l2:
                str+=word2[s2]
                s2+=1
        return str
    
#print(Solution.mergeAlternately(Solution, "abc", "ferf"))


