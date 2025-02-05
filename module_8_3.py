class IncorrectVinNumber(Exception):
    """Исключение для некорректного VIN-номера."""
    def __init__(self, message="Некорректный VIN-номер"):
        super().__init__(message)
        self.message = message  # Добавьте эту строку

class IncorrectCarNumbers(Exception):
    """Исключение для некорректных номеров автомобиля."""
    def __init__(self, message="Некорректные номера автомобиля"):
        super().__init__(message)
        self.message = message  # Добавьте эту строку

class Car:
    """Класс, представляющий автомобиль."""

    def __init__(self, model, vin, numbers):
        """Инициализирует объект автомобиля."""
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        self.__is_valid_vin(self.__vin)
        self.__is_valid_numbers(self.__numbers)

    def __is_valid_vin(self, vin_number):
        """Проверяет корректность VIN-номера."""
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Некорректный тип VIN-номера")
        if not 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber("Неверный диапазон для VIN-номера")  # Передаем сообщение в raise
        return True

    def __is_valid_numbers(self, numbers):
        """Проверяет корректность номеров автомобиля."""
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        if len(numbers) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")  # Передаем сообщение в raise
        return True

# Пример использования:
try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
