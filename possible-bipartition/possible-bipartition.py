class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        not_colored=0
        blue=1
        green=-1
        
        def helper(person,color):
            color_table[person]=color
            
            for dislike_ppl in dislike_table[person]:
                if color_table[dislike_ppl]==color:
                    return False
                if color_table[dislike_ppl]==not_colored and not(helper(dislike_ppl,-color)):
                    return False
            return True
        
        if n==1 or not dislikes:
            return True
        dislike_table=defaultdict(list)
        for i in dislikes:
            dislike_table[i[0]].append(i[1])
            dislike_table[i[1]].append(i[0])
        color_table=[not_colored for i in range(n+1)]
        
        for person in range(1,n+1):
            if color_table[person]==not_colored and (not helper(person,blue)):
                return False
        return True