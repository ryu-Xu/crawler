# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# Project    :crawler
# File       :auto_fileIn.py
# Time       :2022/5/17 14:44
# Author     :Felix
# version    :python 3.x
# Description：
    自动导入文件
    并保存图片
"""
import time

import pyautogui as gui


def file_in():

    gui.click(1044, 391, button='left')
    time.sleep(1)
    gui.click(1296, 772, button='left')
    time.sleep(60)


def shot(click_file_x):
    gui.click(click_file_x, 160, button='left')  # 选择文件
    gui.PAUSE = 1
    gui.click(280, 206, button='left')  # 取消坐标系
    gui.PAUSE = 0.5
    gui.click(270, 206, button='left')  # 取消坐标系
    gui.PAUSE = 1
    gui.click(1859, 932, button='left')  # 正向
    gui.PAUSE = 1
    gui.click(217, 10, button='left')  # 另存为
    gui.PAUSE = 1
    gui.click(245, 60, button='left')  # 另存为图片
    gui.PAUSE = 1
    gui.click(1276, 656, button='left')  # 保存
    gui.PAUSE = 1


def save_file():
    gui.click(297, 158, button='left')  # 点击关闭
    gui.PAUSE = 1
    gui.click(909, 610, button='left')  # 点击保存
    gui.PAUSE = 1
    gui.click(1284, 649, button='left')  # 点击保存
    time.sleep(5)


if __name__ == '__main__':
    gui.FAILSAFE = True

    start_x = 270
    interval = 80
    for i in range(5):
        # file_in()
        # shot(start_x + interval * (i+0))
        save_file()
