from src.item import Item


class MixinLanguage:

    def __init__(self):
        self.__language = "EN"

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self

    @property
    def language(self):
        language = self.__language
        return language


class KeyBoard(Item, MixinLanguage):
    pass


