"""
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

user_input = input("введите слова через пробел\n>>>")
user_words = user_input.split(" ")

idx = 0
words_count = len(user_words)
max_word_len = 10
idx_column_len = len(str(words_count))
while idx < words_count:
    print(f"{idx + 1:>{idx_column_len}}: {user_words[idx][:max_word_len]:^{max_word_len}}")
    idx += 1
