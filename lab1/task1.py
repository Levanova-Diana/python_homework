k = int(input())  #сколько клавиш нажимает один игрок

#счётчики для цифр 1-9
counts = [0] * 10  #индекс 0 не используем

#читаем 4 строки поля
for i in range(4):
    row = input()
    for ch in row:
        if ch != '.':          #если не точка, значит цифра
            digit = int(ch)    #превращаем символ в число
            counts[digit] = counts[digit] + 1 #увеличиваем счетчик на 1

#сколько клавиш могут нажать оба игрока вместе
max_press = 2 * k

#считаем баллы
score = 0
for t in range(1, 10):         #t от 1 до 9
    if counts[t] > 0 and counts[t] <= max_press:
        score = score + 1

print(score)