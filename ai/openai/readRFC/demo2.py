import re

with open('resources/rfc/rfc7230.txt') as f:
    content = f.read()

chapters = re.split('\n\d+. ', content)

for i, chapter in enumerate(chapters):
    if len(chapter) > 200:
        small_chapters = re.split('\n\d+\.\d+. ', chapter)
        for j, small_chapter in enumerate(small_chapters):
            with open(f'b{i+1}_{j+1}.txt', 'w') as f:
                f.write(small_chapter)
    else:
        with open(f'b{i+1}.txt', 'w') as f:
            f.write(chapter)



