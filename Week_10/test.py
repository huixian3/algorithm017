class Solution:
    def numDecodings(self, s: str) -> int:
        # 回溯尝试
        n = len(s)
        self.num = 0
        self.bt(s, 0, n)
        return self.num

    def bt(self, s, index, n):
        if index == n:
            self.num += 1
            return
        elif index == n-1:
            if int(s[index]) > 0:
                self.num += 1
            return
        else:
            if int(s[index]) > 0:
                # index += 1
                self.bt(s, index+1, n)

            if index < n-1 and int(s[index]) >0 and int(s[index]) * 10 +int(s[index+1]) <= 26:
                # index += 2
                self.bt(s, index+2, n)
            else:
                return

print(Solution().numDecodings('124'))