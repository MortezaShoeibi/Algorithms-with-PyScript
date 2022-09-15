from js import console
from .morse_dict import morse

def changeToMorse(human_readable_string):
    result = []
    for i in human_readable_string:
        for key, value in morse.items():
            if i == key:
                result.append(value)
    return result


def getUserInput(*args, **kwargs):

    user_input = str(Element('input').element.value).upper()

    console.log(f'the entered string: {user_input}')

    Element('output').element.innerText = changeToMorse(user_input)