# -*- coding: utf-8 -*-
"""
calc_irradiance.py
放射照度値の海面への投射
Written by Kosuke Takahashi on 2018-09-14
日本語入力できるぜ！
ただし，emacsキーバインドではない
"""

import numpy as np
import scipy as sp
import pandas
import math

# ファイルからのデータ入力
#with open("Haku.csv", "r", encoding="utf_8") as f:
#    data = f.read(2)
#    print(data)
#    data = f.read(2)
#    print(data)
#f.close()

# numpyを使わんとならんらしい？
# encoding='utf_8'を書き込まないとcp932だめよエラーがでる。
data = np.loadtxt('H28_H30.csv', skiprows = 1, delimiter = ',', dtype='float', encoding='utf_8')
print(data[0])

# for i in を入れて52点のデータを加工，別ファイルに格納させる(Under Constracting) これ作ったら描画までさせちゃお

""" 変数定義 
1行目1列は[0][0]＝Mo, [0][1]:海面から物標までの高さ（計算値）， [2]:海面から地面までの高さ， [3]:地面から測器までの高さ
[4]:x, [5]:y, [6]:irrandiance
"""

row = 3

h0 = data[row][1]
hg = data[row][2]
hs = data[row][3]
xi = data[row][4]
yi = data[row][5]
Ii = data[row][6]

# 
# Theta の算出
Theta = math.atan((h0 - (hg + hs)) / (math.sqrt(pow(xi,2) + pow(yi,2))))

# 放射照度減衰率の計算
di = pow((math.sin(Theta) / (h0 - (hg + hs))), 2)

# 海面での減衰率計算
d0 = pow((math.sin(Theta) / h0),2)

# 海面の放射照度
I0 = Ii * (d0/di)

# 海面座標の算出
Alpha = math.atan(data[row][4])
if xi == 0:
    x0 = 0
else:
    x0 = ((h0 / math.tan(Theta)) - math.sqrt(pow(xi,2) + pow(yi,2))) * math.cos(Alpha) + xi
y0 = h0 / math.tan(Theta)

# 海面の放射照度，海面座標の表示
print(I0)
print("x=",x0)
print("y=",y0)
print("Θ=",Theta)
 


