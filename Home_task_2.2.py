import json
# import cchardet as chardet      #cchardet=chardet, but cchardet work faster than chardet
import os
import string
from pprint import pprint

list_files = [
    ('newsafr.json', 'utf-8'),
    ('newscy.json', 'koi8-r'),
    ('newsfr.json', 'iso-8859-5'),
    ('newsit.json', 'cp1251')
]

# def check_encoding(fname):
#     rawdata = open(fname, "rb").read()
#     result = chardet.detect(rawdata)['encoding']
#     return result.lower()
#
# def get_file_list(our_directory, file_extension):
#     list_files = []
#     json_files = []
#     xml_files = []
#     for file in os.listdir(our_directory):
#         file_name = file #os.path.join(our_directory, file)
#         if file.endswith(file_extension):
#             list_files.append((file_name, check_encoding(file_name)))
#         # elif file.endswith(".xml"):
#         #     xml_files.append((file_name, check_encoding(file_name)))
#     pprint(list_files)
#     print(list_files)
#     return list_files

def get_frequency_dictionery(list_files, our_directory):
    for json_file, engoding_file in list_files:
        strip = string.whitespace + string.punctuation + string.digits + "\"'" + '<br>'
        with open(json_file, 'r', encoding=engoding_file) as f:
            data = json.load(f)
            words = {}
            for cdata in data['rss']['channel']['item']:
                if len(cdata['description']) > 1:
                    string_from_description = cdata['description']
                else:
                    string_from_description =  cdata['description']['__cdata']

                for word in string_from_description.lower().split():
                    word = word.strip(strip)
                    if len(word) > 5:
                        words[word] = words.get(word, 0) + 1
        print_frequency_dictionery(json_file,words)

def print_frequency_dictionery(json_file,words):
    i = 0
    print('----------------{}----------------------'.format(json_file))
    for word in sorted(words, key=words.get, reverse=True):
        print("'{0}' frequency {1} times".format(word, words[word]))
        i +=1
        if i == 10:
            break

if __name__ == "__main__":
    our_directory = input("Enter directory's name(if directory's name is empty,"
                          "the current working directory will be assigned):")
    if not our_directory:
        our_directory = os.getcwd()  # the current working directory: "...Home_task_2.2"
    get_frequency_dictionery(list_files, our_directory)