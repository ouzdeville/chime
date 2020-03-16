import yaml


class I18n:
    def __init__(self, file_name: str):
        with open(f"locales/{file_name}.yaml", 'r') as file_stream:
            self.locale_file = yaml.safe_load(file_stream)

    def set_locale(self, locale: str):
        self.locale = locale

    def t(self, word: str):
        '''Method for transrate'''
        locale_dic = self.locale_file[self.locale] if self.locale in self.locale_file else self.locale_file["en"]
        return locale_dic[word] if word in locale_dic else word