class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        divisors = [d for d in range(1, n + 1) if n % d == 0]
        return len(divisors) == 3
        
        