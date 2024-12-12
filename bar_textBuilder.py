# Methods for printing bars
def print_full_bar(length_of_bar):
    bar = "+"

    for i in range(length_of_bar):
        bar += "-"
    bar += "+"
    print(bar)

def print_empty_bar(length_of_bar):
    bar = "|"

    for i in range(length_of_bar):
        bar += " "
    bar += "|"
    print(bar)

def print_centered_text_bar(legth_of_bar, text):
    len_of_text = len(text)
    left_padding = int((legth_of_bar - len_of_text) / 2)
    right_padding = legth_of_bar - left_padding - len_of_text

    if left_padding < 0:
        raise ValueError
    bar = "|"

    for i in range(left_padding):
        bar += " "
    bar += text

    for i in range(right_padding):
        bar += " "
    bar += "|"
    print(bar)

def print_left_text_bar(lenght_of_bar, text):
    len_of_text = len(text)
    right_padding = lenght_of_bar - len_of_text

    bar = "|" + text
    for i in range(right_padding):
        bar += " "
    bar += "|"
    print(bar)

