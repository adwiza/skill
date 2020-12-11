import yaml

with open('python_snippets/external_data/yaml_example.yaml') as yaml_file:
    martins_resume_in = yaml.load(yaml_file, Loader=yaml.FullLoader)
    print(f'Полученное резюме в формате YAML мы превратили в словарь Пайтона {martins_resume_in}')

martins_resume_out = yaml.dump(martins_resume_in)
# Обратная операция восстановила структуру, превратив словарь в строку, соответствующую формату YAML:
print(martins_resume_out)
