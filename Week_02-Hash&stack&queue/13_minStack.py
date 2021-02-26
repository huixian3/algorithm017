#!/usr/bin/python3
# coding=utf-8

import sys
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.minstack = [sys.maxsize] # 最大值，否则最小值会被替代

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        self.minstack.append(min(x, self.minstack[-1]))

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minstack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]
