# -*- coding:utf-8 -*-
class Solution:

    # 整体和部分分别旋转
    def leftReverse(self, s, k):
        if not isinstance(s, str) or len(s) == 0 or s == None or k <= 0:
            return ''
        strList = list(s)
        self.reverse(strList, 0, k-1)
        self.reverse(strList, k, len(strList)-1)
        self.reverse(strList, 0, len(strList)-1)

        return ''.join(strList)

    def reverse(self, s, i, j):
        if i > j:
            return ''
        while i <= j:
            c = s[i]
            s[i] = s[j]
            s[j] = c
            i += 1
            j -= 1

    # 直接使用python字符串拼接
    def leftReverse2(self, s, k):
        if not isinstance(s,str) or len(s)<=0 or s==None or k<0:
            return ''
        return s[k:] + s[:k]
test = Solution()
s = "123456789"
print test.leftReverse(s,4)
print test.leftReverse2(s,4)