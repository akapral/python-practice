'''
Недавно мы считали для каждого слова количество его вхождений в строку.
Но на все слова может быть не так интересно смотреть, как, например, на
наиболее часто используемые.

Напишите программу, которая считывает текст из файла (в файле может быть
больше одной строки) и выводит самое частое слово в этом тексте и через пробел то,
сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически
первое (можно использовать оператор < для строк).

Слова, написанные в разных регистрах, считаются одинаковыми.
'''

with open('/home/skapral/Downloads/dataset_3363_3.txt') as input:
    line=input.readline().strip().lower().split()

result={}
length=len(line)
for w in line:
    result.setdefault(w, )
    for w1 in result:
        count=0
        for w2 in range(length):
            if w1==line[w2]:
                count+=1
                result.update({w1: count})

for w,count in result.items():
    print(w, count)

'''output=open('/home/skapral/Downloads/dataset3.txt', 'w')
for w in result:
    output.write(w)'''
