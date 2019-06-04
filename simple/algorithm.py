"""
### 7. 整数反转（简单）

给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:      
输入: 123   
输出: 321  

示例 2:

输入: -123
输出: -321
 
示例 3:  
输入: 120 
输出: 21 

#### 我的解题思路
- 将整数转化成字符串处理，然后将字符串通过切片反转，再转化成整数，对于负数，可以先将其对应的字符串的首位取下，反转之后再加上即可
- 注意：
    - 负整数的反转
    - 应当考虑反转之后的数字是否会溢出

"""

class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        if x_str[0] != '-':
            x_str_reverse = x_str[::-1]
            x_reverse = int(x_str_reverse)
        else:
            x_str = x_str[1::]
            x_str_reverse = '-' + x_str[::-1]
            x_reverse = int(x_str_reverse)
        if -2**31 < x_reverse < 2**31-1:
            return x_reverse
        return 0
