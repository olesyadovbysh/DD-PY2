import doctest
from typing import Union

class Garland:
    """
    Класс описывает характеристики гирлянды
    """
    def __init__(self, lenght_m: Union[int,float], number_of_leds: int):
        self.length_m = lenght_m #длина гирлянды
        self.number_of_leds = number_of_leds #количество светодиодов
        self.color = 'теплый белый'
        self.number_of_operation_mode = 8 #количество режимов работы
        self.current_operation_mode = 1
        self.ip44 = False #наличие защиты гирлянды для использования на улице

        if not isinstance(lenght_m, (int, float)):
            raise TypeError('Длина гирлянды должна иметь тип int или float')
        if not isinstance(number_of_leds, int):
            raise TypeError('Количество светодиодов должно быть целым числом')
        if lenght_m < 0:
            raise ValueError('Длина гирлянды должна быть положительным числом')
        if number_of_leds < 0:
            raise ValueError('Количество светодиодов должно быть положительным числом')

    def turn_on(self, on: bool) -> None:
        """
        Метод включает или выключает гирлянду
        :param on: включает гирлянду, если True

        Пример:
        >>> garland = Garland(20, 200)
        >>> garland.turn_on(True)
        """
        if not isinstance(on, bool):
            raise TypeError ('Переменная должна быть типа bool')
        ...

    def change_operation_mode(self, new_operation_mode: int) -> None:
        """
        Метод изменяет режим работы гирлянды
        :param new_operation_mode: выбор нового режима работы

        Пример:
        >>> garland = Garland(20, 200)
        >>> garland.change_operation_mode(2)
        """
        if not isinstance(new_operation_mode, int):
            raise TypeError ('Номер режима работы должен быть целым числом')
        if new_operation_mode > self.number_of_operation_mode:
            raise ValueError ('Номер режима работы не должен быть больше количества режимов работы')
        if new_operation_mode < 0:
            raise ValueError ('Номер режима работы не должен быть отрицательным')



class OlivierSalad:
    """
    Класс описывает салат оливье
    """
    def __init__(self):
        self.cucumbers_num = 5
        self.potato_num = 3
        self.carrot_num = 3
        self.pea_g = 400
        self.eggs_num = 4
        self.sausage_g = 350
        self.mayonnaise_ml = 250

    def add_crawfish_necks(self, crawfish: int) -> None:
        """
        Метод добавляет в салат раковые шейки
        :param crawfish: Количество доавляемых раков

        Пример:
        >>> salad = OlivierSalad()
        >>> salad.add_crawfish_necks(8)
        """
        if not isinstance(crawfish, int):
            raise TypeError('Количество доступных вам раков должно быть целым')
        ...

    def eating_from_bowl(self, from_bowl: bool) -> None:
        """
        Метод позволяет есть салат прямо из общей тарелки
        :param from_bowl: Можно есть из общей тарелки, если True

        Пример:
        >>> salad = OlivierSalad()
        >>> salad.eating_from_bowl(True)
        """
        if not isinstance(from_bowl, bool):
            raise TypeError ('Переменная должна быть типа bool')
        ...

    def is_there_salad(self) -> bool:
        """
        Метод проверяет остался ли еще салат
        :return: Остался ли салат

        Пример:
        >>> salad = OlivierSalad()
        >>> salad.is_there_salad()
        """
        ...



class AddressByPutin:
    """
    Класс описывает обращение презедента
    """
    def __init__(self, time_min: Union[int, float]):
        self.citation = 'Это был тяжелый год'
        self.background = 'Кремль'
        self.tie_color = 'Красный'
        self.time = time_min #длительность обращения в минутах

        if not isinstance(time_min, (int, float)):
            raise TypeError ('Длительность обращения должна быть типа int или float')
        if time_min > 7:
            raise ValueError ('Слишком долгое обращение')
        if time_min < 0:
            raise ValueError ('Длительность обращения должна быть положительной')

    def add_citation(self, new_citation: str) -> None:
        """
        Метод позволяет добавить цитату в обращение президента
        :param new_citation: Цитата

        Пример:
        >>> putin = AddressByPutin(6)
        >>> putin.add_citation('C Новым 2023 годом!')
        """
        if not isinstance(new_citation, str):
            raise TypeError ('Цитата должна быть типа str')

    def change_background(self, new_background: str) -> None:
        """
        Метод позволяет сменить фон обращения президента
        :param new_background: Новый фон

        Пример:
        >>> putin = AddressByPutin(6)
        >>> putin.change_background('Не кремль')
        """
        if not isinstance(new_background, str):
            raise TypeError('Переменная должна быть типа str')
        ...

if __name__ == "__main__":
    doctest.testmod()
    pass
