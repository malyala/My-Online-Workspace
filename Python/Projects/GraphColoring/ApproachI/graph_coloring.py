"""
The complexity of this is O(n*k + d) where we have a set of k distinct colors
and a graph with n nodes and total degree d. We can reason as follows. In the 


"""



def FindColors(graph, ColorSet):
	"""
	Graph is a dict to a set of nodes 
	as keys with values as a list of nodes 
	pointed to by the key. ColorSet is a set
	of distinct colors.
	"""
	soln = dict();
	for node in graph.keys():
		UsedColors = set();
		for neighbor in graph[node]:
			try:
				UsedColors.add(soln[neighbor]);
			except:
				continue;
		PotentialColors = ColorSet - UsedColors;
		if len(PotentialColors) == 0:
			return False;
		else:
			soln[node] = PotentialColors.pop()
	return soln;


##Testing
graph = {'A':['B','C'], 'B':['A'], 'C':['A']}
colors = set(["red", "blue"])
test1 = FindColors(graph, colors)
print(str(test1) +
"\n-> Should be A is diff from B and C (which are the same)")

	

