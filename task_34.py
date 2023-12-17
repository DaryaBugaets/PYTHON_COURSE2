# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод: пара-ра-рам рам-пам-папам па-ра-па-дам Вывод: Парам пам-пам

# stroka = "пара-ра-рам рам-пам-папам па-ра-па-дам"
# stroks = stroka.split()
# print(stroks)
# lst = [sum(x in 'уеыаоэяию' for x in lin)
#  for lin in stroks]
# if len(set(lst)) == 1 :
#     res = "Парам пам-пам"  
# else: 
#     res = "Пам парам"
# print(res)


# stroka = 'пара-ра-рам рам-пам-папам па-ра-па'
# def rhythm(str):
#     str = str.split()
#     list_1 = []
#     for word in str:
#         sum_w = 0
#         for i in word:
#             if i in 'аеёиоуыэюя':
#                 sum_w += 1
#                 list_1.append(sum_w)
#                 return len(list_1) == list_1.count(list_1[0])
# # stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# if rhythm(stroka):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')


# def count_vowels(word):
#     vowels = 'aeiouy'
#     count = 0
#     for letter in word:
#         if letter.lower() in vowels:
#             count += 1
#     return count
# def check_rhythm(stroka):
#     phrases = stroka.split(" ")
#     syllables = []
#     for phrase in phrases:
#         words = phrase.split("-")
#         phrase_syllables = []
#         for word in words:
#             syllable_count = count_vowels(word)
#             phrase_syllables.append(syllable_count)
#         syllables.append(phrase_syllables)
#     for i in range(1, len(syllables)):
#         if syllables[i] != syllables[i-1]:
#             return "Пам парам"
#     return "Парам пам-пам"
# # Ввод стихотворения
# stroka = 'пара-ра-рам рам-пам-папам па-ра-па'
# # poem = input("Введите стихотворение: ")
# # Проверка ритма
# result = check_rhythm(stroka)
# print(result)

stroka = 'пара-ра-рам рам-пам-папам па-ра-па'
vowels = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
phrases = stroka.split()
if len(phrases) < 2:
 print('Количество фраз должно быть больше одной!')
else:
 countVowels = []

 for i in phrases:
  countVowels.append(len([x for x in i if x.lower() in vowels]))

 if countVowels.count(countVowels[0]) == len(countVowels):
  print('Парам пам-пам')
 else:
  print('Пам парам')