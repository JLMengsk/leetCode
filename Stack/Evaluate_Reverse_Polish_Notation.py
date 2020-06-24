# -*- coding:utf-8 -*-
# @Time     : 6/24/2020 5:25 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Evaluate_Reverse_Polish_Notation.py
# @Software : PyCharm

# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.

# There is a big difference between C and python
# Python: (-1)/2=-1 是向下取整的
# C: (-1)/2=0。也就是c语言中，除法是向零取整，即舍弃小数点后的数


# slow way use eval()
class Solution1:
    def evalRPN(self, tokens):
        stack = []
        operators = ['+', '-', '*', '/']
        for token in tokens:
            if token not in operators:  # Number
                stack.append(token)  # eval must be str
            else:
                b = stack.pop()  # stack[-1]
                a = stack.pop()  # stack[-2]
                if token == '/' and int(a) * int(b) < 0:
                    res = int(eval('-' + '(' + '-' + a + '/' + b + ')'))  # -(-a/b)
                # Another way use operator.truediv()
                # if token == '/':
                #     res = int(operator.truediv(int(a),int(b)))
                else:
                    res = int(eval(a + token + b))  # type(res) => int
                stack.append(str(res))
        return stack[0]


class Solution2:
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t not in ['+', '-', '*', '/']:
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == '+':
                    stack.append(r + l)
                elif t == '-':
                    stack.append(l - r)
                elif t == '*':
                    stack.append(l * r)
                else:
                    if l * r < 0 and l % r != 0:
                        stack.append(-(-l // r))  # also could be (l//r+1)
                    else:
                        stack.append(l // r)
        return stack.pop()


s = Solution1()
print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
s = Solution2()
print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
