# -*- coding:utf-8 -*-
'''
    替换字符串中的空格为“20%”
'''

class Solution:
    # s 源字符串

    # 使用list的append
    def replaceByAppend(self,s):
        if not isinstance(s,str) or len(s)<=0 or s==None:
            return ''
        strReplace = []
        for item in s:
            if(item==' '):
                strReplace.append('%')
                strReplace.append('2')
                strReplace.append('0')
            else:
                strReplace.append(item)
        return  ''.join(strReplace)

    # 新建字符串
    def replaceByStr(self,s):
        if type(s) != str:
            return ''
        tmpStr = ''

        for c in s:
            if c == ' ':
                tmpStr += "%20"
            else:
                tmpStr += c
        return tmpStr

    # 简单替换
    def replaceBysimple(self, s):
        if not isinstance(s, str) or len(s) <= 0 or s == None:
            return
        return s.replace(" ", "%20")

    # 使用下标移动
    def replaceByindex(self, s):
        if not isinstance(s,str) or len(s) <= 0 or s==None:
            return ''
        blankNum = 0
        for c in s:
            if c==' ':
                blankNum += 1
        newStrLen = len(s) + blankNum*2
        newStr = newStrLen * [None]
        indexOfOld, indexOfNew = len(s)-1 , newStrLen-1
        while indexOfNew >= 0 and indexOfNew >= indexOfOld:
            if s[indexOfOld] == ' ':
                newStr[indexOfNew-2 : indexOfNew+1] = ['%','2','0']
                indexOfNew -= 3
                indexOfOld -= 1
            else:
                newStr[indexOfNew] = s[indexOfOld]
                indexOfNew -= 1
                indexOfOld -= 1
        return "".join(newStr)


s = 'I am a programmer'
test = Solution()
print test.replaceByAppend(s)
print test.replaceByStr(s)
print test.replaceBysimple(s)
print test.replaceByindex(s)