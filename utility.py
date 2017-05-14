def replace_characters(*args, string, replacement):
    string2 = string
    for arg in args:
        string2 = string2.replace(arg, replacement)

    return string2.strip()
