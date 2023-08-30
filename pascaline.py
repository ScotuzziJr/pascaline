from interpreter_pascaline import Interpreter

while True:
    try:
        source = input('pascaline> ')
    except EOFError:
        break

    if not source:
        continue
    elif source == 'q':
        break

    interpreter = Interpreter(source)
    result = interpreter.run()
    print(result)
