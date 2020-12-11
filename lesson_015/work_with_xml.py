import xml.etree.ElementTree as ETree

# первым делом нужно распарсить имеющийся документ
developers_cv = ETree.parse('python_snippets/external_data/demo.xml')
# Найти корень
root_of_developers_cv = developers_cv.getroot()

print(f'Название корневого тега {root_of_developers_cv.tag}, а вот текста в нем нет {root_of_developers_cv.text}')
print(f'Следующий элемент, название тега "{root_of_developers_cv[0].tag}", \n \
        текст внутри "{root_of_developers_cv[0].text}"')

# Узнаем какими языками владеее Пётр

skills = []
for lang in root_of_developers_cv[3]:
    skills.append(lang.attrib['name'])

print(f'Петр владеет следующими ЯП {skills}')

tags = sorted(list({elem.tag for elem in developers_cv.iter()}))

print(f'Все теги: {tags}')
