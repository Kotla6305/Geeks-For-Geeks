#User function Template for python3

class Solution:
    def gameOfXor(self, N , A):
        # code here 
        ans=0
        for i,v in enumerate(A):
            x=(i+1)*(N-i)%2    
            if x==1:
                ans^=v
        return ans    


