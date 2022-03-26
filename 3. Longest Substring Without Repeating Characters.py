class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ans = []
        dic = {}

        for i in range(0, len(s), 1):
            for j in range(i,len(s), 1):
                if(not s[j] in dic):
                    dic[s[j]] = 0
                else:
                    ans.append(len(dic.keys()))
                    dic = {}
                    break

        ans.append(len(dic.keys()))

        return max(ans)