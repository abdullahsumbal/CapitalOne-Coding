from tokenize import generate_tokens, untokenize, NUMBER, STRING, NAME, OP, COMMENT, NL, ENDMARKER
from io import BytesIO

f = open("data-samples/python-file2.py")
total_lines = 0
line_num_single_comments = []
total_single_comments = 0
total_block_comments = 0
total_block_comments_lines = 0
total_multi_comments = 0
total_multi_comments_lines = 0
total_TODOs = 0

previous_token_type = NUMBER
is_block_comment = False
for tok in generate_tokens(f.readline):
    print(tok)
    token_type = tok[0]
    token_string = tok[1]
    start_line, start_col = tok[2]
    end_line, end_col = tok[3]

    if token_type in [NL, ENDMARKER]:
        continue

    if previous_token_type == COMMENT and token_type != COMMENT:
        if is_block_comment:
            total_block_comments += 1
        else:
            total_single_comments += 1

        is_block_comment = False
    elif previous_token_type == COMMENT and token_type == COMMENT:
        is_block_comment = True
        total_block_comments_lines += 1

    previous_token_type = token_type


if previous_token_type == COMMENT:
    if is_block_comment:
        total_block_comments += 1
    else:
        total_single_comments += 1

print("total_lines:", total_lines)
print("total_block_comments:", total_block_comments)
print("total_block_comments_lines", total_block_comments_lines)
print("total_single_comments:", total_single_comments)
print("total_TODOs:", total_TODOs)