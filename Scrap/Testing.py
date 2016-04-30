def heman(f_l,args):
	ret = f_l[0](args*)
	for i in f_l[1:]:
		ret = i(ret)
	return ret

	
		