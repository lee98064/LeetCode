class Solution:
    def myAtoi(self, s: str) -> int:
            
        num = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        operate = {' ', '-', '+'}

        temp = ""
        is_negative = False
        is_start = False
        for i in s:

            if(i in num):
                temp += i
                is_start = True
            elif(i == "-" and not is_start):
                is_negative = True
                is_start = True
            elif(i == "+" and not is_start):
                is_negative = False
                is_start = True
            elif(is_start):
                break
            elif(i not in operate):
                break
                
                
        if (len(temp) == 0):
            return 0
        else:
            result = int(temp)
        
        if(is_negative):
            if(result * -1 < -2147483648):
                return -2147483648
            else:
                return result * -1
        else:
            if(result > 2147483647):
                return 2147483647
            else:
                return result