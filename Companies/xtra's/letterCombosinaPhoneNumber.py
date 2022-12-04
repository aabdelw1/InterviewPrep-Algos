def letterCombinations(digits: str) -> List[str]:
      
      letters = {'2':'abc', '3':'def','4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs','8':'tuv', '9':'wxyz'}
      if digits == "":
          return []

      def backtrack(digits, path, res):
          if digits == '':
              res.append(path)
              return
          for letter in letters[digits[0]]:

              path += letter
              backtrack(digits[1:], path, res)
              path = path[:-1]


      res = []
      backtrack(digits, '', res)
      return res


      d = { "2":"abc" , "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
      if not digits:
          return []
      output=[""]

      for c in digits:
          tmp=[]
          for v in d[c]:
              for o in output:
                  tmp.append(o+v)
          output=tmp
      return output