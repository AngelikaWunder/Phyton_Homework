# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R  – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# Ввод:
# ноутбук
# Вывод:12

alphabet_en={1:'AEIOULNSTR',
             2:'D,G', 
             3:'BCMP',
             4: 'F, H, V, W, Y',
             5: 'K',
             8:'J, X',
             10:'Q, Z'}
alphabet_rus={1:'А, В, Е, И, Н, О, Р, С, Т',
              2:'Д, К, Л, М, П, У',
              3:'Б, Г, Ё, Ь, Я',
              4:'Й, Ы',
              5:'Ж, З, Х, Ц, Ч',
              8:'Ш, Э, Ю',
              10:'Ф, Щ, Ъ'}

word = input('Введите слово: ').upper()
value = 0
for item in word:
    for k, v in alphabet_en.items():
        if item in v:
            value = value + k
    for i, j in alphabet_rus.items():
                if item in j:
                    value = value + i
                
print(f'Стоимость слова составляет {value}.')    
