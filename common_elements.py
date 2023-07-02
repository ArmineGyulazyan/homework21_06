def find_common_elements(ls1,ls2):
	new_ls = []
	for i in ls1:
		for j in ls2:
			if i==j:
				new_ls.append(i)
	print(new_ls)

list1 = [1,2,3,44,6,5,7,8]
list2 = [1,3,5,44,15,9,10,7]
find_common_elements(list1,list2)	
