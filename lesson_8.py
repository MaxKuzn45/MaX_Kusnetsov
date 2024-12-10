#дз 8.1
import re
a=input("")
while a!='':
    if re.fullmatch(r'[А-Я]\d{3}[А-Я]{2}\d{2,3}', a):
        print('частный автомобиль')
    elif re.fullmatch(r'[А-Я]{2}\d{4,5}', a):
        print('такси')
    else:
        print('ошибка')
    a=input("")
#дз 8.2
import re
from functools import reduce
with open('Занятие_8_Текст.txt', 'r', encoding='utf-8') as file:
    s = file.readlines()
words = reduce(lambda x, y: x.strip() + ' ' + y.strip(), s).split()
print(words)
filtered_words = list(filter(
    lambda x: re.fullmatch(r'\b[А-Яа-яёЁ]+[-]?[А-Яа-яёЁ]+\b', x) or re.fullmatch(r'\b[A-Za-z]+[-]?[A-Za-z]+\b', x),
    words
))
print(filtered_words)
#дз 8.3
import re
from functools import reduce
D='Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю.'
D=D.split()
x=list(filter(lambda x: re.search(r'\b(0[0-9]|1[0-9]|2[0-4])[:](0[0-9]|[0-9]{2})\b',x) ,D))
D= reduce(lambda x,y:  x+' '+y, D)
for i in x:
    D=D.replace(i,'(TBD)',1)
print(D)
#дз 8.4
import re
s = 'Владимир устроился на работу в одно очень важное место.'
x = re.findall((r'\b[А-Я][А-Я]*[А-Я]\b', s))
print(x)
