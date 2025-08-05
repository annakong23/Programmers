while True:
    try:
        sentence = input()
        lower, upper, num, space = 0, 0, 0, 0
        for char in sentence:
            if char.islower():
                lower += 1
            elif char.isupper():
                upper += 1
            elif char.isdigit():
                num += 1
            elif char.isspace():
                space += 1
        print(lower, upper, num, space)
    except EOFError:
        break