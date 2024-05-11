import datetime
class Account: #Содержит в себе баланс, а также методы для работы с учетом 
  #Просто заправшиваем данные
  def getData(self):
    date = input("Пожалуйста, введите 0 или дату записи (в формате YYYY-MM-DD): ")
    category = input("Пожалуйста, введите 0 или категорию записи (Доход или Расход): ")
    sum = float(input("Пожалуйста, введите 0 или сумму записи: "))
    return date, category, sum

  
  def __init__(self, name):
    self.name = name
    balance = 0
    with open(f"{self.name}_records.txt", "r") as f:
      content = f.readlines()

    for i in range(1, len(content) - 2, 4):
      if(content[i][12:].lower()[0] == "д"):
        balance += float(content[i + 1].strip("Сумма: "))
      else:
        balance -= float(content[i + 1].strip("Сумма: "))
    self.balance = balance

  #Ничего не возвращает, создает запись в файле Имя_records.txt или сам файл а потом записывает в него
  def add_record(self):
    date = datetime.date.today()
    
    category = input("Пожалуйста, введите категорию записи (Доход или Расход): ")
    
    sum = float(input("Пожалуйста, введите сумму записи: "))
    
    description = input("Пожалуйста, введите описание записи: ")
    
    with open(f"{self.name}_records.txt", "a") as f:
        f.write(f" Дата: {date.year}-{date.month}-{date.day}\n Категория: {category}\n Сумма: {sum}\n Описание {description}\n")
    print("Запись успешно добавлена!")

    if(category.lower()[0] == "д"): 
      self.balance += sum
    else:
      self.balance -= sum
  #Выводит строку на которой находится первое совпадение с поиском и возвращает ее, либо выводит что строка не найдена и возвращает 0
  def find_record(self, date, category, sum):

    with open(f"{self.name}_records.txt", "r") as f:
      content = f.readlines()
  
    for i in range(0, len(content), 4):
      if date == content[i].strip("Дата: \n") or date == "0":
        if category.lower()[0] == content[i+1][12:].lower()[0] or category == "0":
          if sum == float(content[i+2].strip("Сумма: ")) or sum == 0:
            print(f"Эта запись находится на строке {i + 1}")
            return i + 1
    print("Запись не найдена")
    return 0
  #Ничего не возвращает, выводит что запись изменена успешно при успешном изменении либо выводит что запись не найдена
  def edit_record(self):
    date,category, sum = self.getData()
    with open(f"{self.name}_records.txt", "r") as f:
      content = f.readlines()
    line = self.find_record(date, category, sum)
    if(line == 0):
      print("Запись не найдена")
    change = input("Хотите изменить дату(1), категорию(2), сумму(3) или описание(4)? Введите цифру")
    if change == "1":
      date = input("Введите новую дату: ")
      content[line - 1] = f"Дата: {date}\n"
    elif change == "2":
      category = input("Введите новую категорию: ")
      content[line] = f"Категория: {category}\n"
    elif change == "3":
      sum = float(input("Введите новую сумму: "))
      content[line+1] = f"Сумма: {sum}\n"
    elif change =="4":
      description = input("Введите новое описание: ")
      content[line+2] = f"Описание: {description}\n"
    else:
      return
      
    with open(f"{self.name}_records.txt", "w") as f:
      f.writelines(content)

    print("Запись успешно изменена!")



#начало тестового кода
name = input("Пожалуйста, введите имя вашего счета: ")
account = Account(name)

while True:
    print("Выберите действие:")
    print("1. Добавить запись")
    print("2. Найти запись")
    print("3. Выйти")
    print("4, Редактировать запись")

    choice = input("Введите номер действия: ")

    if choice == "1":
      account.add_record()
    elif choice == "2":
      date, category, sum = account.getData()
      account.find_record(date,category,sum)
    elif choice == "3":
      break
    elif choice == "4":
      account.edit_record()
    else:
      print("Неверный выбор. Пожалуйста, попробуйте еще раз.")
