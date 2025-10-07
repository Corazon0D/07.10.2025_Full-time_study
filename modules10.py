# Дополнительные устанавливаемые модули
# Модули документов
# PIP - Python Installation Package
# pip install xlsxwriter
# Создание таблиц Excel
import xlsxwriter

workbook = xlsxwriter.Workbook('excel/list.xlsx')  # открыть лист
worksheet = workbook.add_worksheet()  # открыть

data = [
    ('Праздник', 6800),
    ('Продукты', 25600),
    ('Транспорт', 3650),
    ('Обучение', 3000)
]
# enumerate для списка возвращает пары: индекс, значение
for row, (item, price) in enumerate(data):
    worksheet.write(row, 0, item)
    worksheet.write(row, 1, price)

row += 1

worksheet.write(row, 0, 'Итого:')
worksheet.write(row, 1, f'=СУММ(B1:B{row})')

workbook.close()
