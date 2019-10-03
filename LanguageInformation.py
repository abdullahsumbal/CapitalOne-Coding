class LanguageInformation:
    """
    Define the interface of interest to clients.
    Maintain a reference to a different language objects
    """
    def __init__(self):
        self._language = None

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, language):
        self._language = language

    def get_comment_info(self):
        return self._language.get_comment_info()
