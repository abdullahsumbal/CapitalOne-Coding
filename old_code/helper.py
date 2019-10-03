"""
Author: Muhammad Abdullah Sumbal

This file contains helper functions

"""
hashtag = "#"
triple_single_quotes = """'''"""
triple_double_quotes = '''"""'''
single_quote = "'"
double_quote = '"'

comments_string_quotes = [triple_single_quotes, triple_double_quotes, double_quote, single_quote, hashtag]

def read_file(file_path, lines=True):
    """
    Read file
    :param file_path: file_path: Path to file
    :param lines: if true then read file by lines else read the whole file as a string.
    :return:
    """
    with open(file_path, "r") as file:
        if lines:
            return file.readlines()
        else:
            return file.read()


def is_triple_quotes(line, char_index, quote):
    """

    :param line:
    :param char_index:
    :return:
    """
    if char_index + 2 < len(line):
        if quote == single_quote:
            return line[char_index:char_index + 3] == triple_single_quotes
        else:
            return line[char_index:char_index + 3] == triple_double_quotes


def get_triple_quotes(quote):
    if quote == single_quote:
        return triple_single_quotes
    else:
        return triple_double_quotes


def is_part_of_comment_or_string(stack, quote=None):
    if quote is None:
        return stack[-1] in comments_string_quotes
    elif quote == single_quote:
        return stack[-1] == triple_double_quotes
    elif quote == double_quote:
        return stack[-1] == triple_single_quotes
    else:
        return False

def count_block_comment_from_single_comments(line_num_single_comments):

    if len(line_num_single_comments) > 0:
        previous_number = line_num_single_comments[0]
    consecutive_comments = 1

    block_comments = 0
    single_comments = 0
    for num in line_num_single_comments[1:]:
        if num - previous_number == 1:
            consecutive_comments += 1

        # reset consecutive comment counter
        elif consecutive_comments > 1:
            consecutive_comments = 1
            block_comments += 1
        else:
            single_comments += 1
        previous_number = num

    if consecutive_comments > 1:
        block_comments += 1
    else:
        single_comments += 1

    return block_comments, single_comments


def is_TODO_in_comment(line, char_index):
    if len(line) > char_index + 4:
        return line[char_index:char_index+4] == "TODO"








