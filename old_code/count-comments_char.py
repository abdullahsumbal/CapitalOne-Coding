"""
Author: Muhammad Abdullah Sumbal

count comments.
"""
from old_code.helper import *



file_path = "data-samples/python-file2.py"
total_lines = 0
line_num_single_comments = []
total_single_comments = 0
total_multi_comments = 0
total_multi_comments_lines = 0
total_TODOs = 0


file_lines = read_file(file_path, lines=True)
file_content = read_file(file_path, lines=False)

# total lines - When a file is checked in, scan the file to count the total number of lines.
total_lines = len(file_lines)


code_mode = True
between_brackets = False
stack = []

# Iter every line
for line_index, line in enumerate(file_lines):

    char_index = 0
    # iter every char
    while char_index < len(line):
        char = line[char_index]

        if char == hashtag:
            # If there is no quotation before #, # is used as a comment.
            if stack:
                if not is_part_of_comment_or_string(stack):
                    total_single_comments += 1
                    # keep track of the line number, later used to find block comments
                    line_num_single_comments.append(line_index)
                    # No need to check other char in line because anything after # is part of the comment
                    stack.append(hashtag)
                    # break
            # no, quotation found before #, so it is used as a comment.
            else:
                # keep track of the line number, later used to find block comments
                line_num_single_comments.append(line_index)
                total_single_comments += 1
                stack.append(hashtag)
                # break
        elif char == double_quote or char == single_quote:
            quote = char
            # it could be a block comment so check if next two char are '""' in the line
            if is_triple_quotes(line, char_index, quote):
                if stack:
                    if not is_part_of_comment_or_string(stack, quote=quote):
                        # closing of block comment
                        if stack[-1] == get_triple_quotes(quote):
                            stack.pop()
                            char_index += 2
                            total_multi_comments += 1
                            total_multi_comments_lines += 1
                        # if round bracket are open then it could be used as an string argument.
                        elif stack[-1] != "(":
                            stack.append(get_triple_quotes(quote))
                            char_index += 2
                # start of block comment
                else:
                    stack.append(get_triple_quotes(quote))
                    char_index += 2
            # just a simple quotation.
            else:
                if stack:
                    if stack[-1] == quote:
                        stack.pop()
                else:
                    stack.append(char)
        elif char == '(':
            if stack:
                # This should not be a part of a comment or string
                if not is_part_of_comment_or_string(stack):
                    stack.append(char)
            else:
                stack.append(char)
        elif char == ")":
            if stack:
                if stack[-1] == '(':
                    stack.pop()
        elif char == "T":
            if stack:
                if is_part_of_comment_or_string(stack):
                    total_TODOs += is_TODO_in_comment(line, char_index)

        char_index += 1

    # this check if we are in comment mode or code mode
    if stack:
        if is_part_of_comment_or_string(stack):
            total_multi_comments_lines += 1
        if stack[-1] == hashtag:
            stack.pop()

extra_block_comments, total_single_comments = count_block_comment_from_single_comments(line_num_single_comments)

total_multi_comments += extra_block_comments

print("total_lines:", total_lines)
print("total_multi_comments:", total_multi_comments)
print("total_multi_comments_lines", total_multi_comments_lines)
print("total_single_comments:", total_single_comments)
print("total_TODOs:", total_TODOs)


