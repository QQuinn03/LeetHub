class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        no_color=0
        blue=1
        green=-1
        
        dislike_table=defaultdict(list)
        color_table=[no_color for i in range(n+1)]
        for i in dislikes:
            dislike_table[i[0]].append(i[1])
            dislike_table[i[1]].append(i[0])
        
        for i in range(1,n+1):
            if color_table[i]==no_color and self.group(i,blue,no_color,color_table,dislike_table)==False:
                return False
        print(color_table)     
        return True
    
    def group(self,i,color,no_color,color_table,dislike_table):
        color_table[i]=color
        for dislike_people in dislike_table[i]:
            #print(color,dislike_people)
            if color_table[dislike_people]==color:
                return False
            if color_table[dislike_people]==no_color and self.group(dislike_people,color*-1,no_color,color_table,dislike_table)==False:
                return False
            
        return True      
        
            