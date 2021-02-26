import collections
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        # 思路1：从前往后，贪心算法，每次找零，尽量给大额钞票
        # save = collections.defaultdict(int)
        #
        # for change in bills:
        #     if change == 5:
        #         save[5] += 1
        #     elif change == 10:
        #         save[5] -= 1
        #         save[10] += 1
        #     elif change == 20:
        #         if save[10] > 0:
        #             save[10] -= 1
        #             save[5] -= 1
        #         else:
        #             save[5] -= 3
        #     if save[10] < 0 or save[5] < 0:
        #         return False
        # return True
        # 思路2：
        five = ten = 0
        for change in bills:
            if change == 5:
                five += 1
            elif change == 10:
                five -= 1
                ten += 1
            elif change == 20:
                if ten > 0:
                    ten -= 1
                    five -= 1
                else:
                    five -= 3
            if ten < 0 or five < 0:
                return False
        return True
print(Solution.lemonadeChange(Solution, [5,5,5,10,20]))