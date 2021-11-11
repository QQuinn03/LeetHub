class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur_max=0
        total_max=0
        res=0
        for i in range(len(gas)):
            total_max+=gas[i]-cost[i]
            cur_max+=gas[i]-cost[i]
            if cur_max<0:
                res=i+1
                cur_max=0
        if total_max>=0:
            return res
        return -1
                