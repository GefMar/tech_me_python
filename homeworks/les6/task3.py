""" 3
На вход функции подается строка, вернуть булевое является эта строка полиндромом или нет
проверочная строка "Пал, а норов худ и дух ворона лап."
Полиндром это строка которая читается в обе стороны одинаково, при этом знаки препинания числа и непечатные символы 
игнорируются
"""


def alpha_lower_char(word, reverse=False):
    word_len = len(word)
    inxs = range(word_len - 1, -1, -1) if reverse else range(0, int(word_len / 2))

    for idx in inxs:
        char = word[idx]
        if char.isalpha():
            yield char.lower()


def is_palindrome(word: str):
    return all(
        map(
            lambda args: args[0] == args[1],
            zip(alpha_lower_char(word), alpha_lower_char(word, reverse=True))
        )
    )


tests = (
    ("Кони, топот, инок, ", True),
    ("Но не реч, а черен он.", True),
    ("Пал, а норов худ и дух ворона лап.", True),
    ("jfhgsjgeieiodnnff", False)
)


for test in tests:
    assert is_palindrome(test[0]) is test[1], test[0]


