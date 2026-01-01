class Solution:
  def expand(self, s: str) -> List[str]:
      res = ['']
      i = 0
      n = len(s)
      while i < n:
          if s[i] == '{':
              j = i
              while s[j] != '}':
                  j += 1
              options = s[i+1:j].split(',')
              res = [p + o for p in res for o in options]
              i = j + 1
          else:
              res = [p + s[i] for p in res]
              i += 1
      return sorted(res)
