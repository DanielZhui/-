# 实现快排
# 方式一递归实现快速排序
# def qsort(l):
# 	if len(l) <= 1:return l
# 	return qsort([lt for lt in l[1:] if lt < l[0]]) + l[0:1] + qsort([ll for ll in l[1:] if ll >= l[0]])

# lis = [3,6,7,5,11,100,95,66]
# print(lis[0:1])
# print(qsort(lis))

# 列表嵌套实现一个列表
lst = [1,2,[3,4],5,[6,7],[8,[9,10]],[11]]
lst2 = [1]
lst3 = []

lst1 = []
def func(lst):
	if len(lst) < 1:
		return lst
	for l in lst:
		if type(l) == list:
			func(l)
		else:
			lst1.append(l)
	return lst1

print(func(lst3))
