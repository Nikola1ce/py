#  列表,数组（List）
# 列表是一种动态数组，可以存储任意类型的对象，并且支持动态扩展和删除。
# 特点：
# 可变：可以修改列表中的元素。
# 元素可以是任意类型。
# 支持索引和切片操作。
# 创建列表
my_list = [1, 2, 3, 4, 5]

# 访问元素
print(my_list[0])  # 输出 1

# 切片
print(my_list[1:3])  # 输出 [2, 3]

# 添加元素
my_list.append(6)  # 在末尾添加元素
my_list.insert(2, 10)  # 在指定位置插入元素

# 删除元素
del my_list[0]  # 删除指定索引的元素
my_list.remove(3)  # 删除第一个值为3的元素
print(my_list.pop())  # 删除并返回最后一个元素


# 遍历列表
for item in my_list:
    print(item)