con=[[] for _ in range(n)]
for x,y,z in flights:
      con[x].append((y,z))
      l=deque([(src,0,0)])
      res=float("inf")
      visited=[0]*n
      while l:
          cur,steps,cost=l.popleft()
          if steps-1>k:
              continue
          if cur==dst:
              res=min(res,cost)
              continue
          visited[cur]=cost
          for x,y in con[cur]:
              if visited[x]==0 or visited[x]>cost+y:
                  l.append((x,steps+1,cost+y))
      return res if res!=float("inf") else -1 
              
