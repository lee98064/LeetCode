class Solution:
    def longestPalindrome(self, s: str) -> str:
        dic = {}
        ans = s[0]

        for index,i in enumerate(s):
            if(i not in dic):
                dic[i] = [index]
            else:
                for j in dic[i]:
                    temp = s[j:index + 1]
                    if(temp == temp[::-1]):
                        if len(temp) > len(ans): ans = temp
                        break
                dic[i].append(index)
        return ans