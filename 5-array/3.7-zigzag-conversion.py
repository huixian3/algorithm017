class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Q: 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
        # 遍历char字符，将符合要求的所属行数 0->n->0，存储到数组；之后进行 join 即可
        if numRows <= 1: return s

        chars = list(s)
        row = 0
        next_step = -1

        res = ['' for _ in range(numRows)] # 存储结果
        for ch in chars:
            print(row)
            res[row] += ch
            if row == 0 or row == numRows-1:
                next_step = -next_step
            row += next_step
        return ''.join(res)




