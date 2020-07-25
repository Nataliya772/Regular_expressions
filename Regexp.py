import itertools
import csv
import re
# читаем адресную книгу в формате CSV в список contacts_list

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    #print(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
phonebook = []

def clean_text(contacts_list):
    for contact in contacts_list:
        pattern = re.compile(r"([А-Я]{1}[а-яё]+)(\s)([А-Я]{1}[а-яё]+)(\s)([А-Я]{1}[а-яё]+)")
        text_one = pattern.sub(r"\1', '\3', '\5", str(contact))
        #print(text_one)
        pattern = re.compile(r"([А-Я]{1}[а-яё]+)(\s)([А-Я]{1}[а-яё]+)")
        text_two = pattern.sub(r"\1', '\3", str(text_one))
        #print(text_two)
        pattern = re.compile(r"([А-Я][а-яёА-ЯЁ]+\S,\s)(\'',)")
        text_three = pattern.sub(r"\1", str(text_two))
        #print(text_three)
        pattern = re.compile(r"([А-Я][а-яёА-ЯЁ]+\S,\s)\s(\'',)")
        text_four = pattern.sub(r"\1", str(text_three))
        #print(text_four)
        pattern = re.compile(r"(\+7|8)?\s*\((\d+)\)\s*(\d+)(\s*|\-?)(\d+)(\s*|\-?)(\d+)")
        text_five = pattern.sub(r"+7(\2)\3-\5-\7", str(text_four))
        #print(text_five)
        pattern = re.compile(r"(\+7|8)(\s|\d)(\d+)(\-)(\d+)(\-)(\d{2})(\d{2})")
        text_six = pattern.sub(r"+7(\3)\5-\7-\8", str(text_five))
        #print(text_six)
        pattern = re.compile(r"(\+7|8)(\s|\d{3})(\d{3})(\d{2})(\d{2})")
        text_seven = pattern.sub(r"+7(\2)\3-\4-\5", str(text_six))
        #print(text_seven)
        pattern = re.compile(r"(\s|\()(доб.{1})(\s)(\d+)('|\))")
        text_eight = pattern.sub(r" \2\4", str(text_seven))
        #print(text_eight)
        pattern = re.compile(r"([а-яёА-ЯЁ]+)(',)(\s)(\s)('\+)")
        text_nine = pattern.sub(r"\1\2\3'',\4\5", str(text_eight))
        #print(text_nine)
        pattern = re.compile(r"(доб.0792',)(\s)('')")
        text_ten = pattern.sub(r"\1\2'Ivan.Laguntcov@minfin.ru'", str(text_nine))
        #print(text_ten)
        pattern = re.compile(r"('Мартиняхин', 'Виталий', 'Геннадьевич',  'ФНС',)(\s)('',)")
        text_eleven = pattern.sub(r"\1\2'cоветник отдела Интернет проектов Управления информационных технологий',", str(text_ten))
        #print(text_eleven)
        pattern = re.compile(r'(.*)')
        text_new = (re.findall(pattern, str(text_eleven)))
        phonebook.append(text_new)

    print(phonebook)

clean_text(contacts_list)



# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
#phonebook = []

def get_name(contacts_list):
    for contact in contacts_list:
        pattern = re.compile(r"([А-Я]{1}[а-яё]+)")
        text_new = (re.findall(pattern, str(contact)))
        if text_new != []:
            phonebook.append(text_new[0:3])

#get_name(contacts_list)
#print(phonebook)

def get_sort_phonebook(phonebook):
    phonebook_sort = sorted(phonebook)
    phonebook_new = (list(phonebook_sort for phonebook_sort,_ in itertools.groupby(phonebook_sort)))
    print(phonebook_new)
    return phonebook_new

get_sort_phonebook(phonebook)
#print(phonebook_new)

def get_organization():
    for contact in contacts_list:
        pattern = re.compile(r"([А-Я]{1}[а-яё]+)")
        text_new = (re.findall(pattern, str(contact)))
        contact_new = contact[0].split()
        #print(contact_new)
        phonebook_new = get_sort_phonebook(phonebook)
        for value in phonebook_new:
            if value[0:2] == value:
                phonebook_new.remove(value)
            if contact_new[0] in value:
                value.append(contact[3])
                value.append(contact[4])
                value.append(contact[5])
                value.append(contact[6])

    print(phonebook_new)


#del_duplicates()
#get_organization()


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    phonebook_new = get_sort_phonebook(phonebook)
    datawriter.writerows(phonebook_new)

