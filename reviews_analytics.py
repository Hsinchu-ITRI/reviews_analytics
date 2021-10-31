# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 16:52:24 2021

@author: Win10
"""

data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line.strip())
        count += 1
        if (count % 1000) == 0:
            print(len(data))
print('檔案讀取完了, 總共有', count, '筆資料')

total_length = 0
for d in data:
    total_length += len(d)
print('平均每筆長度為', total_length/len(data))