#дз 7.1
def read_last(lines, file):
    file = open(r'C:\file\article.txt', 'r')
    if lines <= 0:
        print('The number will > 0')
        return
    with open(r'C:\file\article.txt', 'r') as file:
        X = file.readlines()
        for line in X[-lines]:
            print(line.strip())
read_last(3, 'article.txt')
#дз 7.2
import os
def print_docs(directory):
    if not os.path.exists(directory):
        print(f'directory {directory} was not found')
        return
    for i in os.listdir(directory):
        p = os.path.join(directory, i)
        print(p)
        if os.path.isdir(p:
            print_docs(p)
print_docs(r'C:\file2.txt')
#дз 7.3
def longest_words(file):
    with open(file, 'r') as f:
        content = f.read()
    words = content.split()
    if not words:
        return []
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]
    return longest_words
print(longest_words('article.txt'))
#дз 7.4
def text_editor():
    file_name = input()
    file_name += '.txt'
    with open(file_name, 'w') as f :
        while True:
            line = input()
            if line.strip() == '' or not line.isprintable():
                break
            f.write(line + '\n')
text_editor()
