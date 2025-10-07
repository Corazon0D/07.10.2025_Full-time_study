# Основные понятия в ООП
# 1. Класс - это описание модели будущего объекта
# 2. Экземпляр - экземпляр (объект) класс
# 3. Объект - это конкретное воплощения класса
# 4. Атрибуты - свойства и действия, присущие объекту
# 5. Метод - действия над собой и другими объектами

class Fruit:
    def __init__(self, n='Фрукт', w=0, c='Белый'):
        self.name = n
        self.washed = w
        self.color = c

    def wash(self):
        print(f'Фрукт {self.name} помыт')

    def about_me(self):
        print(f'Я фрукт {self.name}, который весит {self.washed}.')
        print(f'А цвет у меня {self.color}')


f1 = Fruit('Груша', 150, 'Зелёная')  # Был вызван конструктор
# f1.name = 'Груша'
# f1.weight = 150
f1.about_me()
f1.wash()
# print(f'Фрукт {f1.name} весит {f1.weight} грамм')
# f1.washed()

f2 = Fruit('Яблоко', 180, 'Красный')  # Был вызван конструктор
# f2.name = 'Яблоко'
# f2.weight = 130
f2.about_me()
f2.wash()
# print(f'Фрукт {f2.name} весит {f2.weight} грамм')

f3 = Fruit('Лимон', 160, 'Жёлтый')  # Был вызван конструктор
# f3.name = 'Лимон'
# f3.weight = 160
# f3.color = 'Жёлтый'
f3.about_me()
f3.wash()
# print(f'Фрукт {f3.name}, Цвет: {f3.color} весит {f3.weight} грамм')
# print(f1.color) у f1 цвет не назначался
