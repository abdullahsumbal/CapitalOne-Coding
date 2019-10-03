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

    def count_TODOs(self, line):
        """
        find TODOs in the line
        :param line: a source code line
        :return: number of TODOs found
        """
        return len(re.findall("TODO:", line))
