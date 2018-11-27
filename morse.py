# morse.py
# pylint: disable=missing-docstring

class Morse:
    ALPHABET = {
        '.-':   'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..':  'D',
        '.':    'E',
        '..-.': 'F',
        '--.':  'G',
        '....': 'H',
        '..':   'I',
        '.---': 'J',
        '-.-':  'K',
        '.-..': 'L',
        '--':   'M',
        '-.':   'N',
        '---':  'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.':  'R',
        '...':  'S',
        '-':    'T',
        '..-':  'U',
        '...-': 'V',
        '.--':  'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z'
    }

    def decode(self, message):
        if message == '':
            return ""
        code = ""
        letters = message.split(' ')
        for letter in letters:
            code = code + (self.ALPHABET[letter])
        return code
