class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if(numRows == 1):
            return s

        ans = [""] * numRows
        now = 0
        reverse = False
        for i in s:
            ans[now] += i

            if(reverse):
                now -= 1
            else:
                now += 1

            if(now > numRows - 1):
                reverse = True
                now = numRows - 2
            elif(now < 0):
                reverse = False
                now = 1

        return ''.join(ans)