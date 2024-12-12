from textBuilder.bar_textBuilder import print_full_bar, print_empty_bar, print_centered_text_bar

def build_frame_with_text(left_padding, top_padding, text):
    longest_text = 0

    for line in text:
        if len(line) > longest_text:
            longest_text = len(line)

    frame_with = (longest_text + left_padding)* 2

    print_full_bar(frame_with)
    for i in range(top_padding):
        print_empty_bar(frame_with)

    if isinstance(text, str):
        print_centered_text_bar(frame_with, text)
    else:
        for line in text:
            print_centered_text_bar(frame_with, line)

    for i in range(top_padding):
        print_empty_bar(frame_with)
    print_full_bar(frame_with)

# TODO: implement function with max_frame_with
