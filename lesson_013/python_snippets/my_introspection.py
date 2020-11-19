import inspect
import sys
# import requests
from pprint import pprint

some_string = 'i am a string'
some_number = 42
some_list = [some_string, some_number]


def some_functions(param, param_2='n/a'):
    print('my param is', param, param_2)


class SomeClass:

    def __init__(self):
        self.attribute_1 = 27

    def some_class_method(self, value):
        self.attribute_1 = value
        print(self.attribute_1)


some_object = SomeClass()

# print(type(some_number))
# print(type(some_number) is int)
# print(type(some_number) is list)

# print(some_functions.__name__)
# print(SomeClass.__name__)
# print(requests.__name__)
# print(__name__)


def check_params(value):
    if type(value) is str:
        print('Обрабатываем строку', value)
    else:
        print('Это не строка')


# check_params(some_string)
# check_params(some_list)

# print(type(requests))

# pprint(dir(some_number))
# pprint(dir(some_list))
# pprint(dir(some_functions))
# pprint(dir(SomeClass))
# pprint(dir(some_object))
#
#
# # Без указания аргумента dir() возвращает имена в текущей области видимости
# pprint(dir())

# pprint(dir(requests))

# print(hasattr(some_object, 'attribute_1'))
# print(hasattr(some_object, 'attribute_2'))
# print(getattr(some_object, 'attribute_1'))
# print(some_object.attribute_1)
# print(getattr(some_object, 'attribute_2', 'Значение если атрибута нет'))

# print(hasattr(requests, 'get'))
# http_get = getattr(requests, 'get')
# print(type(http_get))
# print(callable(http_get))

# for attr_name in dir(requests):
#     attr = (getattr(requests, attr_name))
#     print(attr_name, type(attr), callable(attr))

# print(callable(some_string))
# print(callable(some_functions))
# print(callable(some_object.attribute_1))
# print(callable(some_object.some_class_method))

# response = requests.get(url='https://skillbox.ru')
# print(response, type(response), callable(response))
# print(isinstance(response, requests.Response))
# print(isinstance(response, requests.NullHandler))

class DerivedClass(SomeClass):
    pass


some_object_2 = DerivedClass()

# print(issubclass(SomeClass, DerivedClass))
# print(issubclass(DerivedClass, SomeClass))
# print(isinstance(some_object_2, SomeClass))
# print(isinstance(some_object_2, DerivedClass))

some_function_module = inspect.getmodule(some_functions)
# print(type(some_function_module), some_function_module)

signature = inspect.signature(some_functions)
# get_signature = inspect.signature(requests.get)
# print(type(signature), signature)
# pprint(dir(signature))
# print(type(signature.parameters), signature.parameters)

# for param_name, param in get_signature.parameters.items():
#     print(param, param.name, param.default)

# pprint(dir(sys))

# print(sys.executable)
#
# print(sys.platform)
# print(sys.version)
# print(sys.path)
# print(sys.modules)

# print(type(sys.modules), sys.modules)
# for k, v in sys.modules.items():
#     print(k, type(v), v)
print(__builtins__)
pprint(__builtins__)