# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.

my_file = open('text_1.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле: {len(content)}')
my_file = open('text_1.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Количество символов в строке № {i+1}: {int(len(content[i])-1)}')
# if count(' ') in content
my_file = open('text_1.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов: {len(content)}')
my_file = open('text_1.txt', 'r')
content = my_file.readlines()
for line in my_file:


        range(len(content.split(' '))):
    print(f'Количество символов в строке № {i+1}: {int(len(content[i]))}')


my_file.close()


# with open("text_1.txt") as file_obj:
#     lines = 0
#     letters = 0
#     for line in file_obj:
#         lines += line.count("\n")
#         letters = len(line)-1
#         print(f"{letters} слов в линии № }")
#     for line in file_obj:
#         words
#     print(f"Всего строк: {lines}")