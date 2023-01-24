from string import ascii_letters        # импорт латинских букв


class Employee:

    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'        # набор русских букв
    S_RUS_UPPER = S_RUS.upper()        # набор заглавных русских букв

    def __init__(self, fio, age, passport, weight, experience):

        self.__fio = fio
        self.age = age
        self.passport = passport
        self.weight = weight
        self.experience = experience

    @classmethod
    def verify_fio(cls, fio):
        """Проверка корректности ФИО"""
        if type(fio) != str:
            raise TypeError('ФИО должно быть строкой')

        f = fio.split()
        if len(f) != 3:
            raise TypeError('Неверный формат ФИО')

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER       # коллекция допустимых символов

        for s in f:
            if len(s) < 1:
                raise TypeError('В ФИО должен быть хотя бы один символ')
            if len(s.strip(letters)) != 0:
                raise TypeError('В ФИО нужно использовать только буквенные символы и дефис')

    @classmethod
    def verify_age(cls, age):
        """Проверка корректности возраста"""
        if type(age) != int or age < 14 or age > 55:
            raise TypeError('Возраст должен быть целым числом')

    @classmethod
    def verify_weight(cls, weight):
        """Проверка корректности веса"""
        if type(weight) != float or weight < 40 or weight > 130:
            raise TypeError('Вес должен быть вещественным числом')

    @classmethod
    def verify_passport(cls, passport):
        """Проверка корректности серии и номера паспорта"""
        if type(passport) != str:
            raise TypeError('Паспорт должен быть строкой')

        s = passport.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError('Неверный формат паспорта')
        for P in s:
            if not P.isdigit():
                raise TypeError('Серия и номер паспорта должны быть числами')

    @classmethod
    def varify_experience(cls, experience):
        """Проверка корректности опыта работы"""
        if type(experience) != float or experience < 1.5:
            raise TypeError('Опыт работы должен быть записан вещественным числом и составлять не менее полутора лет')

    @property
    def fio(self):
        """Геттер для ФИО"""
        return self.__fio

    @fio.setter
    def fio(self, fio):
        """Сеттер для ФИО"""
        self.verify_fio(fio)
        self.__fio = fio

    @property
    def age(self):
        """Геттер для возраста"""
        return self.__age

    @age.setter
    def age(self, age):
        """Сеттер для возраста"""
        self.verify_age(age)
        self.__age = age

    @property
    def weight(self):
        """Геттер для веса"""
        return self.__weight

    @weight.setter
    def weight(self, weight):
        """Сеттер для возраста"""
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def passport(self):
        """Геттер для серии и номера паспорта"""
        return self.__passport

    @passport.setter
    def passport(self, passport):
        """Сеттер для серии и номера паспорта"""
        self.verify_passport(passport)
        self.__passport = passport

    @property
    def experience(self):
        """Геттер для опыта работы"""
        return self.__experience

    @experience.setter
    def experience(self, experience):
        """Сеттер для опыта работы"""
        self.varify_experience(experience)
        self.__experience = experience


employee1 = Employee('Пушкин Александр Сергеевич', 26, '1234 567890', 73.5, 1.7)
print(employee1.__dict__)
employee2 = Employee('Галкин Иннокентий Афанасьевич', 25, '2112 222333', 70.0, 1.5)
employee2.fio = input("Укажите ФИО сотрудника через пробел: ")
employee2.age = int(input("Укажите возраст сотрудника: "))
employee2.weight = float(input("Укажите вес сотрудника: "))
employee2.passport = input("Укажите серию и номер паспорта сотрудника через пробел: ")
employee2.experience = float(input("Укажите опыт работы сотрудника: "))
print(employee2.__dict__)
