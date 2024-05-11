RU
Учет доходов и расходов:
Простое приложение для учета доходов и расходов на Python с использованием текстового файла для хранения данных.

Использование:
Для начала работы введите имя вашего счета. Программа автоматически загрузит данные из файла {имя счета}_records.txt, если он существует.

Вам будет предложено выбрать одно из следующих действий:

Добавить запись: Добавляет новую запись о доходе или расходе.
Найти запись: Позволяет искать запись по дате, категории и/или сумме.
Выйти: Завершает работу программы.


Функции класса Account:
add_record(): Добавляет новую запись о доходе или расходе.
find_record(date, category, sum): Ищет запись по указанным параметрам.
edit_record(): Редактирует существующую запись.

Примечание:

Для каждого счета создается отдельный файл для хранения записей. Имя файла формируется как {имя счета}_records.txt.
Для изменения данных о записи используйте функцию edit_record().
Зависимости
Для работы приложения требуется Python 3.x.

Автор
[Timondrius]

Лицензия
Этот проект лицензирован по лицензии MIT License.



EN

Income and Expense Tracker
A simple Python application for tracking income and expenses using a text file to store data.

Usage:
To get started, enter the name of your account. The program will automatically load data from the {account name}_records.txt file if it exists.

You will be prompted to choose one of the following actions:

Add Record: Add a new record of income or expense.
Find Record: Allows you to search for a record by date, category, and/or amount.
Exit: Quit the program.


Account Class Functions:
add_record(): Add a new record of income or expense.
find_record(date, category, sum): Find a record based on the specified parameters.
edit_record(): Edit an existing record.

Note:
Each account has its own file to store records. The file name is formed as {account name}_records.txt.
Use the edit_record() function to modify record data.
Dependencies
This application requires Python 3.x to run.

Author
[Timondrius]

License
This project is licensed under the MIT License.
