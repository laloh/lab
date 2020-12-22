def greeting(name: str, excited: bool = False) -> str:
    message = 'Hello, {}'.format(name)
    if excited:
        message += '!!!!'
    return message

def p() -> None:
    print("Hello")

greeting('Lalloooo')


