#!/usr/bin/python3
# coding=utf-8
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = list()
    if len(s) % 2  == 1:
        return False
    # 栈2
    dic = {'{':'}', '[':']', '(':')'}
    for ch in s:
        if ch in dic.keys():
            stack.append(dic[ch])
        elif ch in dic.values():
            if not stack or stack.pop() != ch:
                return False
        else:
            return False
    return not stack
    # 栈1
    # for ch in s:
    #     if ch == '{':
    #         stack.append('}')
    #     elif ch == '[':
    #         stack.append(']')
    #     elif ch == '(':
    #         stack.append(')')
    #     else:
    #         if stack.pop() != ch:
    #             return False
    # return len(stack) == 0


print(isValid("((())){}{}{}{"))