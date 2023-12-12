import re

with open('resources/rfc/rfc7230.txt') as f:
    content = f.read()

chapters = re.split('\n\d+\.  ', content)

for i, chapter in enumerate(chapters):
    print(f'第{i+1}章')
    with open(f'a{i+1}.txt', 'w') as f:
        f.write(chapter)


