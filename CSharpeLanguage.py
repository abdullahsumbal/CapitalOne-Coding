from Language import Language


class CSharpeLanguage(Language):
    """
    Implement the algorithm using the Strategy interface.
    """

    def __init__(self, file_path):
        self._file_path = file_path
        super().__init__()

    def get_comment_info(self):
        """
        Count single line comments, block comments and TODOs
        :return: a dictionary of the comment mentioned mentioned above
        """
        return self.get_comment_info_common()