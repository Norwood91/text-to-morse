
# -------------------------------------------------- MORSE LOGIC ---------------------------------------------------
morse_library = {
    'A': '._', 'B': '_...', 'C': '_._.', 'D': '_..', 'E': '.', 'F': '.._.',
    'G': '__.', 'H': '....', 'I': '..', 'J': '.___', 'K': '_._', 'L': '._..',
    'M': '__', 'N': '_.', 'O': '___', 'P': '.__.', 'Q': '__._', 'R': '._.',
    'S': '...', 'T': '_', 'U': '.._', 'V': '..._', 'W': '.__', 'X': '_.._',
    'Y': '_.__', 'Z': '__..', '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ',':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'
}

def encode_message(message):
    encoded_message = ''
    for char in message:
        if char != ' ':
            encoded_message += morse_library[char] + ' '
        else:
            encoded_message += ' '
    return encoded_message


def decode_message(message):
    message += ' '
    decoded_message = ''
    citext = ''
    for char in message:
        if char != ' ':
            space = 0
            citext += char
        else:
            space += 1
            if space == 2:
                decoded_message += ' '
            else:
                decoded_message += list(morse_library.keys())[list(morse_library.values()).index(citext)]
                citext = ''

    return decoded_message

def get_user_input():
    user_options = input('Would you like to encode or decode a message?: ').lower()
    secret_message = input(f'What message would you like to {user_options}: ').upper()

    if user_options == 'encode':
        print(encode_message(secret_message))
    elif user_options == 'decode':
        print(decode_message(secret_message))

get_user_input()


