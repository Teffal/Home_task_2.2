import json
import xml.etree.ElementTree as ET
import string
from pprint import pprint

list_files_json = [
    ('newsafr.json', 'utf-8'),
    ('newscy.json', 'koi8-r'),
    ('newsfr.json', 'iso-8859-5'),
    ('newsit.json', 'cp1251')
]

list_files_xml = ['newsafr.xml', 'newscy.xml', 'newsfr.xml', 'newsit.xml']

def get_frequency_dictionery(list_files):
    strip = string.whitespace + string.punctuation + string.digits + "\"'" + '<br>'
    for json_file, engoding_file in list_files:
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

def get_frequency_dictionery_xml(list_files_xml):
    print(list_files_xml)
    print(list_files_xml[0])
    print(type(list_files_xml[0]))
    f = 'newsfr.xml'
    print(type(f))
    n = list_files_xml[0]
    print(type(n))

    tree = ET.parse(f)
    tree = ET.parse(n) # неработает передача названия документа, как элемента списка. Почему?
    print(tree)
    for i in tree.iter():
        print(i)
    # print(list_files_xml)
    # for xml_file in list_files_xml:
    #     print(xml_file)
    #     tree = ET.parse('newsafr.xml')
        # tree = ET.parse(xml_file) #строка выдает ошибку, так и не смог понять почему?(
        # print(tree)
        # for i in tree.iter():
        #     print(i)

def print_frequency_dictionery(json_file,words):
    i = 0
    print('----------------{}----------------------'.format(json_file))
    for word in sorted(words, key=words.get, reverse=True):
        print("'{0}' frequency {1} times".format(word, words[word]))
        i +=1
        if i == 10:
            break

if __name__ == "__main__":
    # get_frequency_dictionery(list_files_json)
    get_frequency_dictionery_xml(list_files_xml)