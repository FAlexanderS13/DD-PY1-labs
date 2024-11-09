# TODO Найдите количество книг, которое можно разместить на дискете
information_volume = 1.44 # Информационный объем дискеты в Мб
number_of_pages = 100 # Количество страниц в книге
number_of_lines = 50 # Число строк на странице
number_of_characters = 25 # Количество символов в строке
symbol_weight = 4 # Размер одного символа для хранения
size_book = ((number_of_characters * number_of_lines * number_of_pages * symbol_weight) / 1024) / 1024 # Размер одной книги
quantity = round(information_volume // size_book) # Количесвто книг помещающих на дискетку
print("Количество книг, помещающихся на дискету:", quantity)
