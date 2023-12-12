import re
import tiktoken

def get_token(content):
    embedding_encoding = "cl100k_base"
    encoding = tiktoken.get_encoding(embedding_encoding)
    return len(encoding.encode(content))

def do_action(file, content):
    with open(file, 'w') as f:
        reply = content
        f.write(reply)


with open('resources/rfc/rfc7230.txt') as f:
    content = f.read()

chapters = re.split('\n\d+. ', content)

for i, chapter in enumerate(chapters):
    tokens = get_token(chapter)
    print("=====> ",i, tokens)
    if tokens > 500:
        small_chapters = re.split('\n\d+\.\d+. ', chapter)
        for j, small_chapter in enumerate(small_chapters):
            do_action(f'b{i+1}_{j+1}.txt', chapter)
    else:
        do_action(f'b{i+1}.txt', chapter)






