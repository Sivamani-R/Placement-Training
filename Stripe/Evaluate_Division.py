class Solution:
  def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
      d=defaultdict(dict)
      n=len(equations)
      for ind,(x,y) in enumerate(equations):
          d[x][y]=values[ind]
          d[y][x]=1/values[ind]
      def solve(cur,target,val,visited):
          if cur not in d:
              return -1.0
          if cur==target:
              return val
          visited.add(cur)
          for x,y in d[cur].items():
              if x not in visited:
                  res=solve(x,target,val*y,visited)
                  if res!=-1:
                      return res
          return -1
      res=[]
      for x,y in queries:
            res.append(solve(x,y,1,set()))
        return res


            
            
        
