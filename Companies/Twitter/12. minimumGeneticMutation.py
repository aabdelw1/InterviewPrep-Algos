from collections import deque

class Solution:
	def minMutation(self, start: str, end: str, bank: List[str]) -> int:
		
		# convert bank to set for faster retrieval
		bank = set(bank)
		
		# track the genes already processed in the BFS
		genes_done = set()
		
		# initialize the queue with the "end" string, as we make incremental changes backwards
		queue = deque([(end, 0)])
		
		chromosomes = ['A', 'C', 'G', 'T']
		min_steps = float("inf")
		
		# iterate till there are no genes to be processed
		while queue:
			curr = queue.popleft()
			curr_gene = curr[0]
			curr_steps = curr[1]
			
			# if our current gene is same as the one we begin with, then record the number of steps taken
			if curr_gene == start:
				min_steps = min(min_steps, curr_steps)

			elif curr_gene in bank and curr_gene not in genes_done:
				genes_done.add(curr_gene)
				
				# iterate through different changes we can make to get a new gene
				for i in range(8):
					for chromosome in chromosomes:
						if chromosome != curr_gene[i]:
							new_gene = curr_gene[:i] + chromosome + curr_gene[i + 1:]
							new_steps = curr_steps + 1
							queue.append((new_gene, new_steps))
		
		# if no minimum recorded, it means there is no valid path between "start" and "end"
		return min_steps if min_steps != float("inf") else -1