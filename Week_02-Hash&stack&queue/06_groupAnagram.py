#!/usr/bin/python3
# coding=utf-8
import collections

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    # key v 串：value 是List
    #
    def anagram(st):
        return "".join(sorted(st))

    res = collections.defaultdict(list)
    for s in strs:
        key = anagram(s)
        res[key].append(s)
    return res.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))