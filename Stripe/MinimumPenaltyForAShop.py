class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n=len(customers)
        Y=customers.count("Y")
        N=0
        time=n-1
        res=float("inf")
        for i in range(n):
            if N+Y<res:
                res=N+Y
                time=i
            if customers[i]=="Y":
                Y-=1
            else:
                N+=1
        if N<res:
            time=n
        return time

        
        
