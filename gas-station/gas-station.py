class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_gas = 0
        cur_gas = 0
        starting_station = 0
        
        for i in range(n):
            total_gas +=gas[i]-cost[i]
            cur_gas +=gas[i]-cost[i]
            if cur_gas<0:
                starting_station =i+1
                cur_gas = 0
                
        return starting_station if total_gas>=0 else -1        
                
            
            