f = open('test.txt')
count = 0

def check_podryad(logs): #проверка одного из условий сделана в виде функц. для лучшего понимания
    for i in range(len(logs)-1):
        if logs[i] == logs[i+1]:
            return True
    else:
        return False

for i in f:
    dop_list = []
    logs = list(map(int, i.split()))
    for j in range(len(logs)):
        if logs[j] <= 20:
            logs[j] = 'apple'
        elif logs[j] <= 50:
            dop_list.append(logs[j]) #добавляем в новый список, чтобы далее проверить отсутствие повторений
            logs[j] = 'green_zone'
        elif logs[j] <= 100:
            dop_list.append(logs[j])  #добавляем в новый список, чтобы далее проверить отсутствие повторений
            logs[j] = 'grey_zone'
    if not (any(x == 'apple' for x in logs)): #проверяем, что Саша не попал по яблочку
        if len(dop_list) == len(set(dop_list)): #проверяем отсутствие повторений с помощью множества
            if check_podryad(logs):
                count += 1
print(count)
