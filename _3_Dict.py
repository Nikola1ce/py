# 字典（Dictionary）
# 字典是一种键值对的集合，类似于哈希表或映射。
# 特点：
# 键必须是不可变类型（如字符串、数字、元组）。
# 值可以是任意类型。
# 通过键快速访问值，时间复杂度为 O(1)。
# 常用操作：
# Python
# 复制
# 创建字典
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# 访问值
print(my_dict["name"])  # 输出 Alice

# 添加键值对
my_dict["gender"] = "Female"

# 删除键值对
del my_dict["city"]

# 遍历字典
for key, value in my_dict.items():
    print(key, value)

# 检查键是否存在
if "age" in my_dict:
    print("Age exists")