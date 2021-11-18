class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur_gas=0
        max_gas=0
        res=0
        
        for i in range(len(gas)):
            cur_gas+=gas[i]-cost[i]
            max_gas+=gas[i]-cost[i]
            if cur_gas<0:
                cur_gas=0
                res=i+1
        if max_gas<0:
            return -1
        return res