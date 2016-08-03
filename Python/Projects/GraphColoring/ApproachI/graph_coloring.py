



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



	

