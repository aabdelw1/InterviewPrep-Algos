class Solution:
  def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
      output = []
      i = 0
      products.sort()
      while(i < len(searchWord)):
          
          temp = []
          count = 0
          for product in products:
              if count == 3:
                  break
              elif i < len(product) and searchWord[:i+1] == product[:i+1]:
                  temp.append(product)
                  count += 1
          output.append(temp)
          i+=1
      return output

  def suggestedProducts2(self, products: List[str], searchWord: str) -> List[List[str]]:
		sol = []
		products.sort()
		for i in range(len(searchWord)): # checking letter is correct at each index i
			temp = []
			for p in products:
				if i >= len(p): # skip if the word is shorter than searchword
					continue
				if p[i] == searchWord[i]:
					temp.append(p)
			products = temp # setting the searchlist to the words we just found
			sol.append(temp[:3]) # add the first 3. This works b/c we sort in the beginning
		return sol

class Trie:
    def __init__(self):
        
        self.root ={"*":"*"}
        
    def insert(self, word):
        
        cur_node =self.root
        for c in word:
            if c not in cur_node:
                cur_node[c] = {}
                
            cur_node = cur_node[c]
            
        cur_node['*'] = {'*'} # a dic so that subsequent ones could continue
       
    def dfs(self, cur_node, cur_word):
        ans =[]
        for key  in sorted(cur_node.keys()):
            if key=='*': 
                ans += [cur_word]
                continue
            
            temp= self.dfs(cur_node[key], cur_word+key)
            if temp: 
                ans+= temp
                     
        return ans
            
    def get_all_words(self, prefix):
        cur_node = self.root
        
        for i,c in enumerate(prefix):
            if c not in cur_node: return []
            cur_node = cur_node[c]
        
        #from here we start accumulating answers
        ans = self.dfs(cur_node, prefix)
        
        return ans
            
            
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        trie = Trie()
        
        for p in products: trie.insert(p)
         
        ans  =[]
        
        for j in range(len(searchWord)):
            temp = trie.get_all_words(searchWord[:j+1])
            temp = temp[:3]
            ans.append(temp)
            
        return ans