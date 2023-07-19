f = open('9.txt')
count = 0

for i in f:
    flat = list(map(int, i.split())) #создание списка всех комнат
    flat.sort(reverse = True) #сортировка по невозрастанию
    if (sum(flat) >= 280) and (flat[-1] < 30) and\
       (30 <= flat[-2] <= 60) and (flat[-3] > 60):
        count += 1

print(count)
