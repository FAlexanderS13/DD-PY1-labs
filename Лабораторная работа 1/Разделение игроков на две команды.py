list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"] # Список имен игроков
# индекс середины
middle_index = len(list_players) // 2 # Разделение игроков на команды
first_team = list_players[:middle_index] # Первая команда
second_team = list_players[middle_index:] # Вторая команда
print(first_team)
print(second_team)
