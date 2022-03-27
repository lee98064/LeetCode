class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        total = 0
        for i in s[::-1]:
            if(i != " "):
                total +=1
            else:
                break
        return total