"""
### 9. 回文数（简单）

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数

示例：
输入: 121
输出: true

输入: -121
输出: false

#### 我的解题思路

- 先判断整数与0的大小，小于0,则返回False
- 大于0,将整数转换成字符串，将字符串利用切片逆序，再将逆序的字符串转化成整数，判断两个数是否相等，相等则返回True,不相等返回False;

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            x_2_str = str(x)
            x_str_reverse = x_2_str[::-1]
            x_reverse = int (x_str_reverse)
            if x == x_reverse:
                return True
            else:
                return False
