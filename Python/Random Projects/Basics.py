def bobs(s):
	"""
	We assume all lowercase letters in s
	"""
	b_count = 0
	s_len = len(s)
	for i in range(s_len-2):
		if s[i]=='b' and s[i+1] == "o" and s[i+2]=='b':
			b_count += 1
	return b_count




def bsearch(e, lis):
	if len(lis)==0:return False
	return bs(e,lis,0,len(lis))



def bs(e,lis, start, end):
	mid = int((start+end)/2.0)
	print(mid)
	if start==end:return False
	if lis[mid]==e:
		return mid
	elif lis[mid]>e:
		return bs(e,lis, start,mid)

	else:
		return bs(e,lis, mid+1, end)














