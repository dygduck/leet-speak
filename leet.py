# def translate_leet(message):
#     characters = list(message)
#     for i in range(len(characters)):
#         if characters[i] == 'a' or characters[i] == 'A':
#             characters[i] = '@'
#         elif characters[i] == 'o' or characters[i] == 'O':
#             characters[i] = '0'
#         elif characters[i] == 'e' or characters[i] == 'E':
#             characters[i] = '3'
#         elif characters[i] == 'l' or characters[i] == 'L':
#             characters[i] = '1'
#         elif characters[i] == 's' or characters[i] == 'S':
#             characters[i] = '5'
#         elif characters[i] == 't' or characters[i] == 'T':
#             characters[i] = '7'
#     return "".join(characters)


# def translate_leet(message):
#     leet = {
#         'a': '@',
#         'o': '0',
#         'e': '3',
#         'l': '1',
#         's': '5',
#         't': '7'
#     }
#     letters = list(message)
#     for i in range(len(letters)):
#         if letters[i].lower() in leet:
#             letters[i] = leet[letters[i].lower()]
#     return "".join(letters)


def translate_leet(message):
    leet = {'a': '@', 'o': '0', 'e': '3',
            'l': '1', 's': '5', 't': '7'}

    letters = [leet.get(letter.lower(), letter) for letter in message]
    return "".join(letters)

print translate_leet("Estrella")
