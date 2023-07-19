f = open('test.txt')
count = 0

for i in f:
    gamers = list(map(int, i.split())) #создаем список игроков в комнате
    max_age_player = 0
    for j in range(len(gamers)): #проходимся по игрокам, чтобы понять к какой кат. относится игрок
        max_age_player = max(max_age_player, gamers[j])
        if gamers[j] <= 14:
            gamers[j] = 'st_player'
        elif gamers[j] <= 32:
            gamers[j] = 'cs_player'
        else:
            gamers[j] = 'doom_player'
    st_quantity = gamers.count('st_player')
    cs_quantity = gamers.count('cs_player')
    doom_quantity = gamers.count('doom_player')
    if doom_quantity < (st_quantity + cs_quantity) and max_age_player > 50: #проверка всех условий
        count += 1
        
print(count)
