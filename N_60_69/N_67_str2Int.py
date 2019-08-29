# -*- coding:utf-8 -*-
'''
将字符串转化为整数，有正负号的判断（整数可以没有‘+’）
'''
class Solution:
    def convert(self, s):
        if type(s)!=str or len(s)<=0 :
            return
        flag = (-1 if(s[0]=='-') else 1)
        res = 0
        for i in range(0,len(s)):
            if i==0 and (s[i]=='+' or s[i]=='-'):
                continue
            if s[i]<'0' or s[i]>'9':
                return
            res = res*10 + (ord(s[i])-ord('0'))
        return flag * res

test = Solution()
s = '+123'
s2 = '1+23'
s3 = '-123'
print test.convert(s)
print test.convert(s2)
print test.convert(s3)