import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError
        return self.quantity + other.quantity

    @classmethod
    def instantiate_from_csv(cls):
        items = []
        with open('../src/items.csv', 'r', encoding='windows-1251') as csv_file:
            reader = csv.reader(csv_file)
            for item in reader:
                items.append(item)
            items.pop(0)
            for item in items:
                join_items = ','.join(item)
                name, price, quantity = join_items.split(',')
                make_classes = (cls(name, float(price), int(quantity)))
                Item.all.append(make_classes)
            return Item.all

    @staticmethod
    def string_to_number(value: str):
        float_value = float(value)
        return int(float_value)

    @property
    def name(self):
        name = self.__name
        return f'{name}'

    @name.setter
    def name(self, name):
        if len(name) >= 10:
            return Exception('Длина наименования товара превышает 10 символов')
        else:
            self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return self.price
