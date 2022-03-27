class Solution:
    def reverse(self, x: int) -> int:
        if(x < 0):
            x *= -1
            temp = int("-" + str(x)[::-1])
        else:
            temp = int(str(x)[::-1])
        
        if(temp > 2147483647 or temp < -2147483647):
            return 0
        else:
            return temp
        