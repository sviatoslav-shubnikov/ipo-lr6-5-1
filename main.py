### Задание 1

# Написать программу, которая:

# - Создаёт список из 6 строк (*строки определяются в коде, на ваш вкус*).
# - Подсчитывает количество строк, содержащих букву `д`.
# - Использует циклы для подсчета.


list = ["Почему", "Леончик Никита", "Захотел Переделать", "Сайт колледжа", "При этом", "Вписывая в это меня :)"] # Создаем список строк
count = 0 # Инициализируем переменную count, для подсчета содержащейся буквы д в строках


for i in list: # Перебираем значение списка
	
	letter = 'д' # Инициализируем переменную letter

	if letter in i: # Проверка на содержание в строке буквы 

		count+=1 # Если есть буква д, тогда увеличиваем счетчик на 1.


print(f"количество строк в которых содержится буква д: {count}") # Выводим на экран