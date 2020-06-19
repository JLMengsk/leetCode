# -*- coding:utf-8 -*-
# @Time     : 6/13/2020 8:36 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Reverse_Words_in_a_String.py
# @Software : PyCharm

# Given an input string, reverse the string word by word.

class Solution1:
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])
    # return ' '.join(reversed(s.split()))


class Solution2:
    def reverseWords(self, s):
        words = s.split(" ")
        n = len(words)
        result = ''
        for i in range(n - 1, -1, -1):
            if words[i] != '':
                result += words[i].strip() + ' '
                # Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
                # 注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
        return result.strip()


s = Solution1()
print(s.reverseWords("the sky is blue"))
s = Solution2()
print(s.reverseWords("the sky is blue"))
