

# 使用 defaultdict 构建一个字典，当键不存在时，会返回默认值
from collections import defaultdict
my_dict = defaultdict(int)
# 更新字典的值
my_dict['apple'] += 1
my_dict['banana'] += 2
print(my_dict['apple'])  # 输出：1
print(my_dict['banana']) # 输出：2
print(my_dict['orange']) # 输出：0，因为 'orange' 键不存在，返回了默认值 0


# 使用 deque 实现队列的功能
from collections import deque
my_queue = deque()
my_queue.append('apple')
my_queue.append('banana')
first_item = my_queue.popleft()
print(first_item) # 输出：'apple'
print(my_queue)   # 输出：deque(['banana'])
print(my_queue)   # 输出：deque(['banana'])



