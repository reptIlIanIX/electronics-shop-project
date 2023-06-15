from src.item import Item


class MixinLanguage:
    def __init__(self):
        self.language = "EN"

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        else:
            self.language = "EN"
        return self


class KeyBoard(Item, MixinLanguage):
    pass
