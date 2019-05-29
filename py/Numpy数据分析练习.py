# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:57:00 2019

@author: admin
"""
#导入numpy
import numpy as np
# 打印当前numpy版本号
print(np.__version__)

# 创建从0到9的一维数字数组
arr = np.arange(0,10)
print(arr)

#创建一个numpy数组元素值全为True（真）的数组
arr = np.full((3,3),False,dtype=bool)
print(arr)

#结果同上
arr = np.ones((3,3),dtype=bool)
print(arr)

# 从 arr 中提取所有的奇数
arr = np.arange(0,10)
arr = arr[arr%2 == 1] 
print(arr)

#将arr中的所有奇数替换为-1。
arr = np.arange(0,10)
arr[arr%2 == 1] =-1
print(arr)

#将arr中的所有奇数替换为-1，而不改变arr。
arr = np.arange(0,10)
out = np.where(arr%2 == 1,-1,arr)
print(arr)
print(out)

# 将一维数组转换为2行的2维数组
arr = np.arange(10)
arr = arr.reshape(2,-1)
print(arr)

# 垂直堆叠数组a和数组b
a = np.arange(10).reshape(2,-1)
b = np.repeat(1,10).reshape(2,-1)

c = np.concatenate([a,b],axis = 0)
print(c)
print("---------------L2---------------------------")

#将数组a和数组b水平堆叠。
a = np.arange(10).reshape(2,-1)
b = np.repeat(1,10).reshape(2,-1)
c = np.concatenate([a,b],axis=1)
print(c)
#method 2
c = np.hstack([a,b])
print(c)
# method 3
c = np.c_[a,b]
print(c)

# 创建以下模式而不使用硬编码。只使用numpy函数和下面的输入数组a。
#a = np.array([1,2,3])` -> array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])

a = np.array([1,2,3])
b = np.r_[np.repeat(a,3),np.tile(a,3)]
print(b)

# 获取数组a和数组b之间的公共项。
a = np.arange(0,8)
b = np.arange(5,20)
c = np.intersect1d(a,b)
print(c)

# 从数组a中删除数组b中的所有项。
a = np.arange(0,8)
b = np.arange(5,20)
c = np.setdiff1d(a,b)
print(c)

#获取a和b元素匹配的位置。
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
c = np.where(a == b)
print(c)

#获取5到10之间的所有项目。
a = np.arange(15)
#method 1
index = np.where((a >= 5) & (a <=10))
b = a[index]
print(b)
#method 2
index = np.where(np.logical_and(a>=5,a<=10))
b = a[index]
print(b)
#method 3
b = a[(a>=5)&(a<=10)]
print(b)

#转换适用于两个标量的函数maxx，以处理两个数组。
def maxx(x,y):
    if x>=y:
        return x
    else:
        return y

a = np.array([5,7,9,8,6,4,5])
b = np.array([6,3,4,8,9,7,1])
pair_max = np.vectorize(maxx,otypes=[float])
c = pair_max(a,b)
print(c)
