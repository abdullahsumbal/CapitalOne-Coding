from Language import Language
import re
from tokenize import generate_tokens, COMMENT, NL, ENDMARKER

class PythonLanguage(Language):
    """
    Implement the algorithm using the Strategy interface.
    """

    def __init__(self, file_path):
        self._file_path = file_path

    def get_comment_info(self):
        """
        Count single line comments, block comments and TODOs
        :return: a dictionary of the comment mentioned mentioned above
        """
        # dictionary to keep track of the single, multi line comments
        # and also TODOs in the comments
        comment_info = {
                        "total_lines": 0,
                        "total_single_comments": 0,
                        "total_block_comments": 0,
                        "total_block_comments_lines": 0,
                        "total_TODOs": 0
                        }

        # get total_lines
        file_pointer = self.load_file()
        comment_info["total_lines"] = len(file_pointer.readlines())
        file_pointer.seek(0)

        # default values
        previous_token_type = NL
        is_block_comment = False

        # loop over each token
        for tok in generate_tokens(file_pointer.readline):
            token_type = tok[0]
            token_str = tok[1]

            # ignore new line and end of file token
            if token_type in [NL, ENDMARKER]:
                continue

            # if the current token is a comment, lok for TODOs and add them
            if token_type == COMMENT:
                comment_info["total_TODOs"] += self.count_TODOs(token_str)

            # if previous token is a comment and current token is not a comment
            # then either the previous comment is single line comment or
            # a part of a multi-line comment
            if previous_token_type == COMMENT and token_type != COMMENT:
                if is_block_comment:
                    comment_info["total_block_comments"] += 1
                else:
                    comment_info["total_single_comments"] += 1

                # reset block comment checker
                is_block_comment = False

            # if the previous and current token is a comment, then for sure it is
            # block comment
            elif previous_token_type == COMMENT and token_type == COMMENT:
                # add 2 to include the previous comment line
                comment_info["total_block_comments_lines"] += 2 if not is_block_comment else 1
                is_block_comment = True


            previous_token_type = token_type

        # check for the last token is it a comment
        if previous_token_type == COMMENT:
            if is_block_comment:
                comment_info["total_block_comments"] += 1
            else:
                comment_info["total_single_comments"] += 1

        return comment_info


