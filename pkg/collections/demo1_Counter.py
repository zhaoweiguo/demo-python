from collections import Counter

# 使用 Counter 对象计数列表中元素的频率
my_list = ['apple', 'banana', 'apple', 'orange', 'apple', 'banana', 'apple']
my_counter = Counter(my_list)
print(my_counter)
# 输出：Counter({'apple': 4, 'banana': 2, 'orange': 1})


# 计数列表中元素的出现次数
from collections import Counter
counter = Counter([1, 2, 3, 1, 2, 1, 1, 3, 4])
print(counter)
# 输出：Counter({1: 4, 2: 2, 3: 2, 4: 1})
sorted_items = counter.most_common()
for item in sorted_items:
    print("从大到小排序输出：", item[0], ":", item[1])
# 输出
    # 从大到小排序输出： 1 : 4
    # 从大到小排序输出： 2 : 2
    # 从大到小排序输出： 3 : 2
    # 从大到小排序输出： 4 : 1
most_item = counter.most_common(1)
print("出现次数最多的元素:", most_item)
# 输出：
#   出现次数最多的元素: [(1, 4)]
for element, count in counter.items():
    if count > 1:
        print(f"输出计数大于1的元素: {element}: {count}")
# 输出：
    # 输出计数大于1的元素: 1: 4
    # 输出计数大于1的元素: 2: 2
    # 输出计数大于1的元素: 3: 2


from collections import Counter
counter = Counter("hello world")
print(counter)
# 输出：Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})


from collections import Counter
counter1 = Counter({'a': 3, 'b': 2, 'c': 1})
counter2 = Counter({'a': 1, 'b': 2, 'd': 1})
merged_counter = counter1 + counter2
print(merged_counter)
# 输出：Counter({'a': 4, 'b': 4, 'c': 1, 'd': 1})





















