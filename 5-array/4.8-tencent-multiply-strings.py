# 输入2个数字组成的字符串，模拟乘法的方式输出他们的乘积。
import collections
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        x1, x2 = list(num1), list(num2)
        res1 = []
        t1, f = 0, 1
        for i in range(len(x1) - 1, -1, -1):
            t1 += int(x1[i]) * f
            f *= 10
        for j in range(len(x2)-1, -1, -1):
            res1.append(int(x2[j]) * t1)

        res = collections.deque()
        # 数组多个元素相加，乘以10^n，n为数据索引
        tmp, k = 0, 0
        while sum(res1) > 0:
            i = 0
            while i <= k and i < len(res1):
                tmp += res1[i] % 10
                res1[i] //= 10
                i += 1
            k += 1
            res.appendleft(str(tmp % 10))
            tmp //= 10

        # print('res', res)
        if tmp != 0: res.appendleft(str(tmp))
        return ''.join(res) if res else '0'



print(Solution().func(['123','201']))


'''
class Solution {
    public String multiply(String num1, String num2) {
        if (num1.equals("0") || num2.equals("0")) {
            return "0";
        }
        int[] res = new int[num1.length() + num2.length()];
        for (int i = num1.length() - 1; i >= 0; i--) {
            int n1 = num1.charAt(i) - '0';
            for (int j = num2.length() - 1; j >= 0; j--) {
                int n2 = num2.charAt(j) - '0';
                int sum = (res[i + j + 1] + n1 * n2);
                res[i + j + 1] = sum % 10;
                res[i + j] += sum / 10;
            }
        }

        StringBuilder result = new StringBuilder();
        for (int i = 0; i < res.length; i++) {
            if (i == 0 && res[i] == 0) continue;
            result.append(res[i]);
        }
        return result.toString();
    }
}

'''







