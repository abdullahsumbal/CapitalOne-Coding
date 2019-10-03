import abc
import re

class Language(metaclass=abc.ABCMeta):
    """
    Declare an interface common to all supported algorithms. Context
    uses this interface to call the algorithm defined by a
    Concrete Strategy e.g PythonLanguage.
    """

    @abc.abstractmethod
    def get_comment_info(self):
        pass

    def load_file(self):
        """
        load file
        :return: file pointer
        """
        return open(self._file_path, 'r')

    def count_TODOs(self, line):
        """
        find TODOs in the line
        :param line: a source code line
        :return: number of TODOs found
        """
        return len(re.findall("TODO:", line))

    def get_comment_info_generic(self):
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

        # this pattern will give any /**/ and // strings.
        # also it give me /* and // which are inside string including string quotations.
        pattern = '//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"'
        regex = re.compile(pattern, re.VERBOSE | re.MULTILINE | re.DOTALL)

        for matching in regex.findall(file_pointer.read()):
            # print(matching)
            # block comments
            if matching[:2] == "/*":
                comment_info["total_block_comments_lines"] += len(matching.split('\n'))
                comment_info["total_block_comments"] += 1
                comment_info["total_TODOs"] += self.count_TODOs(matching)
            # single line comments
            elif matching[:2] == "//":
                comment_info["total_single_comments"] += 1
                comment_info["total_TODOs"] += self.count_TODOs(matching)
        return comment_info
