class Contato():
    def __init__(self, celular: str, email: str):
        self.__celular = celular
        self.__email = email

    @property
    def celular(self):
        return self.__celular
    
    @celular.setter
    def celular(self, novo: str):
        if isinstance(novo, str):
            self.__celular = novo

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, novo: str):
        if isinstance(novo, str):
            self.__email = novo
            
        