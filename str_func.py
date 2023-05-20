def upper_str(str):
    """
    докстринг
    """
    return str.upper()

def title_str(str):
    """
    Первые буквы слов у строки в верхнем регистре
    """
    new_line = ''
    line = str.split()
    for thing in line:
        new_line += thing.capitalize()
        new_line += " "
    return new_line


