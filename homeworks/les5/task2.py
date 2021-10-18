"""2
Дан словарь с кодированием строк азбуки Морзе
2.1 Реализовать функцию кодирующую текст в морзе строку. на вход функции подается строка текста, в ответ возвращается 
строка закодированная азбукой морзе. В качестве разделителя морзе символов использовать пробел. 
Пробел кодируется тоже как пробел

2.2 Реализовать функцию декодирующую морзе строку обратно в читаемый текст. 

Обратите внимание что используется только символы латинского Алфавита в lower case. 
При этом строка должна всегда начинаться с заглавной буквы
"""

MORSE = {
    '.-': 'a', '-...': 'b', '-.-.': 'c',
    '-..': 'd', '.': 'e', '..-.': 'f',
    '--.': 'g', '....': 'h', '..': 'i',
    '.---': 'j', '-.-': 'k', '.-..': 'l',
    '--': 'm', '-.': 'n', '---': 'o',
    '.--.': 'p', '--.-': 'q', '.-.': 'r',
    '...': 's', '-': 't', '..-': 'u',
    '...-': 'v', '.--': 'w', '-..-': 'x',
    '-.--': 'y', '--..': 'z', '-----': '0',
    '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6',
    '--...': '7', '---..': '8', '----.': '9'
}


def morse_decode(text, code_table=MORSE):
    clear_text = text.split(" ")
    result = []
    for m_char in clear_text:
        decod_char = code_table[m_char] if m_char else " "
        result.append(decod_char)
    return "".join(result).capitalize()


def morse_encode(text, code_table=MORSE):
    convert_code_table = dict(zip(code_table.values(), code_table.keys()))
    add_separator_text = text.lower().split(" ")
    result = []
    for word in add_separator_text:
        encode_word = " ".join(map(lambda char: convert_code_table[char], word))
        result.append(encode_word)

    return "  ".join(result)


print(morse_decode("... --- -- .  - . -..- -"))
print(morse_encode('Some text'))
