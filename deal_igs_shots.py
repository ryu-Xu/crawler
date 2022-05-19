# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# Project    :crawler
# File       :deal_igs_shots.py
# Time       :2022/5/19 16:04
# Author     :Felix
# version    :python 3.x
# Description：
    处理igs文件
    转换成新迪psm文件
    调整角度和取消坐标系
    截图保存为bmp文件
    关闭并保存psm文件

    基本思路是：一个个来处理
    打开
    处理
    关闭
"""

import os
import pyautogui as pag
import time


def auto_deal_igs(igs_file, out_psm_path, out_bmp_path):
    # 点击浏览按钮
    button_open = pag.locateCenterOnScreen(r'icon_open.png', region=(0, 0, 360, 240), confidence=0.7)
    pag.moveTo(*button_open, duration=0.5)
    pag.click(button='left')

    # 输入文件名
    pag.typewrite(message=igs_file, interval=0.1)
    pag.press('enter')

    # 转换成psm文件
    time.sleep(1)
    button_psm = pag.locateCenterOnScreen(r'icon_psm.png', region=(800, 240, 1000, 400), confidence=0.5)
    pag.moveTo(*button_psm, duration=0.5)
    pag.doubleClick(button='left')

    # 等待进入
    time.sleep(5)
    while pag.pixel(1000, 530) == (240, 240, 240):
        time.sleep(5)
    time.sleep(5)

    # 取消掉坐标系的勾
    button_base = pag.locateCenterOnScreen(r'icon_base.png', region=(230, 145, 450, 230), confidence=0.7)
    pag.moveTo(*button_base, duration=0.5)
    pag.moveRel(-35, 0)
    pag.click(button='left')

    # 旋转到正面
    pag.hotkey('ctrl', 't')

    # 点击另存为图片
    pag.click(215, 13)  # 下拉框
    pag.click(226, 56)  # 另存为图片
    button_save = pag.locateCenterOnScreen(r'icon_save.png', region=(1000, 700, 1300, 800), confidence=0.7)
    pag.moveTo(*button_save, duration=0.5)
    pag.click(button='left')

    # 点击x 关闭并保存
    pag.click(302, 156)  # 点击x
    button_yes = pag.locateCenterOnScreen(r'icon_yes.png', region=(850, 580, 950, 650), confidence=0.7)
    pag.moveTo(*button_yes, duration=0.5)
    pag.click(button='left')  # 点击是

    time.sleep(1)
    button_save = pag.locateCenterOnScreen(r'icon_save.png', region=(1000, 700, 1300, 800), confidence=0.7)
    pag.moveTo(*button_save, duration=0.5)
    pag.click(button='left')  # 点击保存


def file_match(path_folder, suffix):
    list_files = os.listdir(path_folder)

    list_needed = []

    for FILE in list_files:
        if FILE[-4:] == suffix:
            list_needed.append(FILE)

    return list_needed


if __name__ == "__main__":

    path_igs_files = r'F:\python_learning\test'
    files_list = file_match(path_igs_files, r'.igs')

    pag.PAUSE = 0.5

    for file in files_list:
        auto_deal_igs(igs_file=file, out_bmp_path=None, out_psm_path=None)
        time.sleep(5)
