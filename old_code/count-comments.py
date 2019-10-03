"""
Author: Muhammad Abdullah Sumbal

count comments.
"""
import re
from old_code.helper import read_file

file_path = "data-samples/python-file2.py"
total_lines = 0
total_single_comments = 0
total_multi_comments = 0
total_multi_comments_lines = 0
total_TODOs = 0


file_lines = read_file(file_path, lines=True)
file_content = read_file(file_path, lines=False)

# total lines - When a file is checked in, scan the file to count the total number of lines.
total_lines = len(file_lines)

# total multiple line comments
# multi_comments_list = re.findall("""("{3}[\s\S]*?"{3}|'{3}[\s\S]*?'{3})""", file_content)
# total_multi_comments = len(multi_comments_list)

quotes_found = False
between_round_brackets = False
is_previous_single_line_comment = False
for index, line in enumerate(file_lines):

    line, block_comments_inline = re.subn("""(?<!\(\s*)("{3}[\s\S]*?"{3}|'{3}[\s\S]*?'{3})(?![\s\S]*?\))""", "", line)
    if not between_round_brackets:
        total_multi_comments += block_comments_inline


    line, block_comments_inline = re.subn("""(?<!\()[\s\S]*?("{3}[\s\S]*?|'{3}[\s\S]*?)(?![\s\S]*?\))""", "", line)
    if "(" in line:
        between_round_brackets = True
    elif ")" in line:
        between_round_brackets = False

    if block_comments_inline > 0 and not between_round_brackets:
        if quotes_found:
            quotes_found = False
            total_multi_comments += block_comments_inline
        else:
            quotes_found = True

    # if "#" in line and not is_previous_single_line_comment:
    #     total_single_comments += 1
    #     is_previous_single_line_comment = True
    # elif "#" not in line and is_previous_single_line_comment:
    #     is_previous_single_line_comment = False
    #     total_multi_comments += 1



    print(between_round_brackets, line.strip(), total_multi_comments)




    file_lines[index] = line
        # if block_comment:
        #     total_multi_comments+=1
        #     block_comment = False
        # else:
        #     block_comment = True



# for line in file_lines:
#     print(line)
print("total_lines:", total_lines)
print("total_multi_comments:", total_multi_comments)
print("total_single_comments:", total_single_comments)

