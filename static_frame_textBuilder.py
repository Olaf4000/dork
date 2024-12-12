from textBuilder.bar_textBuilder import print_full_bar, print_empty_bar, print_centered_text_bar


def build_frame_with_single_line_text(frame_with, text):
    print_full_bar(frame_with)
    print_empty_bar(frame_with)

    print_centered_text_bar(frame_with, text)

    print_empty_bar(frame_with)
    print_full_bar(frame_with)

def build_frame_with_multi_line_text(frame_with, text):    
    print_full_bar(frame_with)
    print_empty_bar(frame_with)
    for line in text:
        print_centered_text_bar(frame_with, line)
    print_empty_bar(frame_with)
    print_full_bar(frame_with)