#!/usr/bin/env bash

#Запуск тестов в консоли:
python -m unittest

# coverage
coverage run --source=vk_bot,handlers,settrings -m unittest
coverage report -m

# create PostgreSQL database
psql -c "create database vk_bot"
psql -d vk_bot