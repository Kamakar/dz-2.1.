word = input('Введите слово')
if len(word) % 2 == 0:
    word_index_1 = int((len(word)/2-1))
    middle_lets = word[word_index_1]+word[word_index_1+1]
    print(middle_lets)
elif len(word) % 2 != 0:
    word_index_2 = int(len(word)//2)
    print(word[word_index_2])
else: print('Ошибка')
