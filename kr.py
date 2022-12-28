#!/usr/bin/python3

# -*- coding: utf-8 -*-

numstr = ["hello", "2", "world", "qwerty", "aq"]
rev_numstr = []

print(f"Исходный массив: {numstr}")

for i in range(len(numstr)):
    st = len(numstr[i])
    if st <= 3:
        rev_numstr.append(numstr[i])

print()

print(f"Массив с элементами исходного массива, длина которых <= 3: {rev_numstr}")
