func twoSum(nums []int, target int) []int {
    seen:=make(map[int]int)
    
    for idx,val :=range nums{
        if seen_idx,ok:=seen[target-val];ok{
            return [] int {seen_idx,idx}
        }
        seen[val]=idx
    }
    
    return []int{0, 0}
}