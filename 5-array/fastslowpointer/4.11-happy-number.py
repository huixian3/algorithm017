# 快慢指针，判断是否有循环出现

# 编写一个算法来判断一个数 n 是不是快乐数。
#
# 「快乐数」定义为：
#
# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果 可以变为  1，那么这个数就是快乐数。
# 如果 n 是快乐数就返回 true ；不是，则返回 false 。


'''
class Solution {
public:
    int bitSquareSum(int n) {
        int sum = 0;
        while(n > 0)
        {
            int bit = n % 10;
            sum += bit * bit;
            n = n / 10;
        }
        return sum;
    }

    bool isHappy(int n) {
        int slow = n, fast = n;
        do{
            slow = bitSquareSum(slow);
            fast = bitSquareSum(fast);
            fast = bitSquareSum(fast);
        }while(slow != fast);

        return slow == 1;
    }
};
'''