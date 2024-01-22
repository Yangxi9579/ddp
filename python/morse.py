"""
Write a Python function named morse_translator that translates a given string into Morse code.

Each alphabetic character in the string should be translated to its corresponding Morse code equivalent.
The Morse code for each character should be separated by a space.
Each word in the string should be separated by a forward slash (/).
The function should handle both uppercase and lowercase alphabetic characters.
The function should be case-insensitive, meaning it treats uppercase and lowercase letters the same.
Non-alphabetic characters (like numbers or symbols) should not be translated.

https://en.wikipedia.org/wiki/Morse_code
"""


def morse_translator(input_string):
      # Morse code mapping
    morse_code_dict = {
         "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }


    # Your code goes here
    translated_string = ''
    for char in input_string:
        if char.isalpha():
            char_upper = char.upper()
            translated_string += morse_code_dict[char_upper] + ' '

    translated_string = translated_string.strip().replace(' ', '/ ')

    return translated_string

input_text = "Love"
result = morse_translator(input_text)
print(result)
