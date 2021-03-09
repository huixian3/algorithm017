class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # Q:给你一个 无重叠的 ，按照区间起始端点排序的区间列表。
        #
        # 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
        # 插入 and 合并; 时间复杂福O(N)

        res = []
        is_insert = 0
        left, right = newInterval
        for interval in intervals:
            # 在插入区间右侧，且无交集
            if interval[0] > right:
                if not is_insert:
                    res.append([left, right])
                    is_insert = 1
                res.append(interval)
            # 在插入区间左侧，且无交集
            elif interval[1] < left:
                res.append(interval)
            # 与插入区间有交集，计算它们的并集
            else:
                left = min(interval[0], left)
                right = max(interval[1], right)
        if not is_insert: res.append([left, right])

        return res

        # 与插入区间有交集，计算它们的并集
        #     if is_insert == 0 and interval[0] < newInterval[0]:
        #         res.append(interval)
        #         if interval[1] >= newInterval[0]:
        #             res[-1][1] = max(res[-1][1], newInterval[1])
        #             is_insert = 1

        #     else:
        #         if is_insert == 0:
        #             res.append(newInterval)
        #             is_insert = 1
        #         # 合并区间
        #         if res[-1][1] < interval[0]:
        #             res.append(interval)
        #         else:
        #             res[-1][1] = max(res[-1][1], interval[1])
        # if not is_insert: res.append(newInterval)
        # return res

