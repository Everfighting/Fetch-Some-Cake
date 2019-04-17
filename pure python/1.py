"""
题目:写一个函数,找出不在列表中且不能够用列表中的元素相加得到的最小整数
	eg. [1,2,5,7]--->4

"""


import itertools
def func()
	mylist=[7,1,2,4,3,5]
	mylist_copy=mylist.copy()  # 对原列表备份
	result=itertools.combinations(mylist,2) # 通过combinations()列出原列表所有组合情况
	for i in result:
		mylist_copy.append(sum(i))  # 将两数相加的所有情况加入mylist_copy中
	mylist_copy=list(set(mylist_copy))  # 去重
	print(mylist_copy)
	for j in range(len(mylist_copy)-1):
		gap=mylist_copy[j+1]-mylist_copy[j] # 计算两数的间隙
		if gap>1:
			return mylist_copy[j]+1 # 如果间隙>1,只需要在其基础上+1 即可得到结果
			
	else:  # 正常结束循环则为最后一个数+1
		return mylist_copy[-1]+1 
