# 4. 集合（Set）
# 集合是一个无序的集合，元素唯一。
# 特点：
# 元素唯一，重复的元素会被自动去除。
# 支持集合操作，如并集、交集、差集等。
# 通过哈希表实现，查找和插入操作的时间复杂度为 O(1)。
# 常用操作：
# Python
# 复制
# 创建集合
my_set = {1, 2, 3, 4, 5}

# 添加元素
my_set.add(6)

# 删除元素
my_set.remove(3)  # 如果元素不存在会抛出 KeyError
my_set.discard(3)  # 如果元素不存在不会报错

# 集合操作
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))  # 并集：{1, 2, 3, 4, 5}
print(set1.intersection(set2))  # 交集：{3}
print(set1.difference(set2))  # 差集：{1, 2}