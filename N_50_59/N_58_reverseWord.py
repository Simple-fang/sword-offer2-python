# -*- coding:utf-8 -*-
'''
翻转单词顺序：
hello world -> world hello
'''
class Solution:
    def reverse(self, s):
        if not isinstance(s, str) or len(s)<=0 or s==None:
            return
        i , j = 0, 0
        strlist = list(s)
        while j <= len(strlist):
            if j==len(strlist) or strlist[j]==' ':
                self.trans(strlist, i ,j-1)
                i = j+1
            j += 1
        self.trans(strlist, 0, len(strlist)-1)
        return ''.join(strlist)

    def trans(self, strlist, i, j):
        while i <= j:
            c = strlist[i]
            strlist[i] = strlist[j]
            strlist[j] = c
            i += 1
            j -= 1

    # 直接使用python语法进行字符串翻转
    def reverse2(self, s):
        ll = s.split(' ')
        return ' '.join(ll[::-1])
test = Solution()
s = 'hello world'
print test.reverse(s)
print test.reverse2(s)