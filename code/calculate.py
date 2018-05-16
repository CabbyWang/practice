#!/usr/bin/env python3
# coding:utf-8

from math import sin, cos, tan, pi, atan, sqrt
import sys
import click
from pathlib import Path
from PyQt5.QtWidgets import *
from PyQt5 import uic


def z_iter(F, T, D, HZ):
    a = ((F - T) // D + 1) * D
    yield a
    while a < HZ:
        a = a + D
        yield a


def calculate(R, F, A1, A2, A3, L, D):
    p = 206265
    A = (A1 * 3600 + A2 * 60 + A3) / 3600
    B = L / (2 * R) * p
    m = L / 2 - pow(L, 3) / (240 * pow(R, 2))
    P = pow(L, 2) / (24 * R)
    T = (R + P) * m * tan(A / 2)
    l = pi * R * (A - 2 * B) / 180 + 2 * L
    E = (R + P) * (1 / cos(A / 2)) - R
    Q = 2 * T - L

    ## 主点里程
    li_ZH = F - T
    li_HY = li_ZH + L
    li_QZ = li_HY + (A / 2 - B) * pi * R / 180
    li_YH = li_HY + (A - 2 * B) * pi * R / 180
    li_HZ = li_ZH + 2 * L + (A - 2 * B) * pi * R / 180

    ## 主点坐标
    zb_ZH = (0, 0)
    zb_HY = (L - pow(L, 3) / (40 * pow(R, 2)), pow(L, 2) / 6 / R)
    zb_QZ = (R * sin(A) + m, R - cos(A / 2) * R + P)
    zb_YH = (sin(180 - A) + m, cos(180 - A) + R + P)
    zb_HZ = ((cos(A) + 1) * T, sin(A) * T)

    ## 桩点里程
    Z = list(z_iter(F, T, D, li_HZ))
    lis_1 = list(filter(lambda x: x < li_HY, Z))
    lis_2 = list(filter(lambda x: x > li_HY and x < li_YH, Z))
    lis_3 = list(filter(lambda x: x < li_YH and x < li_HZ, Z))

    ## 桩点坐标
    # 第一段, 对应lis_1
    zb_1_list = []
    for li1 in lis_1:
        temp = li1 - (F - T)
        x = temp - pow(temp, 5) / (40 * pow(R, 2) * pow(L, 2))
        y = pow(temp, 3) / (6 * R * L)
        zb_1_list.append((x, y))
    # 偏角
    painjiao_list1 = [atan(y / x) * 180 / pi for x, y in zb_1_list]
    # 距离
    juli1 = [sqrt(pow(x, 2) + pow(y, 2)) for x, y in zb_1_list]

    # 第二段，对应lis_2
    zb_2_list = []
    for li2 in lis_2:
        temp = 180 / (pi * R) * (li2 - F + T - L) + B
        x = R * sin(temp) + m
        y = R * (1 - cos(temp)) + P
        zb_2_list.append((x, y))
    # 偏角
    painjiao_list2 = [atan(y / x) * 180 / pi for x, y in zb_2_list]
    # 距离
    juli2 = [sqrt(pow(x, 2) + pow(y, 2)) for x, y in zb_2_list]

    # 第三段, 对应lis_3
    zb_3_list = []
    for li3 in lis_3:
        temp = li_HZ - li3
        x0 = temp - pow(temp, 5) / (40 * pow(R, 2) * pow(L, 2))
        y0 = pow(temp, 3) / (6 * R * L)
        # 转换坐标系
        x = y0 * sin(-A) - x0 * cos(-A) + zb_HZ[0]
        y = y0 * cos(-A) + x0 * sin(-A) + zb_HZ[1]
        zb_3_list.append((x, y))
    # 偏角
    painjiao_list3 = [atan(y / x) * 180 / pi for x, y in zb_3_list]
    # 距离
    juli3 = [sqrt(pow(x, 2) + pow(y, 2)) for x, y in zb_3_list]


class CacWidget(QWidget):

    def __init__(self, parent=None):
        super(CacWidget, self).__init__(parent)
        self.ui = uic.loadUi(str(Path(__file__).parent.parent / 'ui' / 'calculate.ui'), self)
        self.set_ui()

    def set_ui(self):
        self.setWindowTitle('缓和曲线计算程序')
        self.ui.btn_calc.clicked.connect(self.calculate)
        self.ui.btn_clear.clicked.connect(self.clear)

    def calculate(self):
        R = self.ui.edit_R.text()
        F = self.ui.edit_F.text()
        A1 = self.ui.edit_A1.text()
        A2 = self.ui.edit_A2.text()
        A3 = self.ui.edit_A3.text()
        L = self.ui.edit_L.text()
        D = self.ui.edit_D.text()
        calculate(R, F, A1, A2, A3, L, D)

    def clear(self):
        self.ui.edit_R.clear()
        self.ui.edit_F.clear()
        self.ui.edit_A1.clear()
        self.ui.edit_A2.clear()
        self.ui.edit_A3.clear()
        self.ui.edit_L.clear()
        self.ui.edit_D.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cw = CacWidget()
    cw.show()
    sys.exit(app.exec())