"""
Задача №27. Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
Output: 13
"""
# twister = """ She sells sea shells on the sea shore The shells 
# that she sells are sea shells I'm sure.So if she sells sea 
# shells on the sea shore I'm sure that the shells are sea 
# shore shells """.lower().split()

# print(len(set(twister)))

# # twister = """ She sells sea shells on the sea shore The shells 
# that she sells are sea shells I'm sure.So if she sells sea 
# shells on the sea shore I'm sure that the shells are sea 
# shore shells """
# print(sorted(list(set(twister.upper().split()))))
# print(len(set(twister.upper().split())))

twister = """ She sells sea shells on the sea shore The shells 
that she sells are sea shells I'm sure.So if she sells sea 
shells on the sea shore I'm sure that the shells are sea 
shore shells """
twister_list=twister.lower().split()
twister_set=set(twister_list)
print(twister_list)
print(len(set(twister_set)))

#через регулярные выражения ?
# import re
# s=""" She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure . 
# So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells """
# delimiters=r"[;,:.\`]+"
# s=re.split(delimiters, s)
# print(len(set(s)))