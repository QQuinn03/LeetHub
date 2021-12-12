class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        index=0
        cur_gas=0
        max_gas=0
        
        for i in range(len(gas)):
            cur_gas+=gas[i]-cost[i]
            max_gas+=gas[i]-cost[i]
            if cur_gas<0:
                index=i+1
                cur_gas=0
        if max_gas<0:
            return -1
        return index