class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        hashmap = {}
        for s in strings:
            key = ()
            for i in range(len(s) - 1):
                circular_difference =ord(s[i+1]) - ord(s[i])
                key+=(circular_difference % 26,)
                
            hashmap[key] = hashmap.get(key, []) + [s]
            # print(hashmap)
        return list(hashmap.values())
        