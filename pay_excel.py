#!/usr/bin/python
#encoding: utf-8
import xlwt
"""
aqua 0x31
black 0x08
blue 0x0C
blue_gray 0x36
bright_green 0x0B
brown 0x3C
coral 0x1D
cyan_ega 0x0F
dark_blue 0x12
dark_blue_ega 0x12
dark_green 0x3A
dark_green_ega 0x11
dark_purple 0x1C
dark_red 0x10
dark_red_ega 0x10
dark_teal 0x38
dark_yellow 0x13
gold 0x33
gray_ega 0x17
gray25 0x16
gray40 0x37
gray50 0x17
gray80 0x3F
green 0x11
ice_blue 0x1F
indigo 0x3E
ivory 0x1A
lavender 0x2E
light_blue 0x30
light_green 0x2A
light_orange 0x34
light_turquoise 0x29
light_yellow 0x2B
lime 0x32
magenta_ega 0x0E
ocean_blue 0x1E
olive_ega 0x13
olive_green 0x3B
orange 0x35
pale_blue 0x2C
periwinkle 0x18
pink 0x0E
plum 0x3D
purple_ega 0x14
red 0x0A
rose 0x2D
sea_green 0x39
silver_ega 0x16
sky_blue 0x28
tan 0x2F
teal 0x15
teal_ega 0x15
turquoise 0x0F
violet 0x14
white 0x09
yellow 0x0D"""
#设置底色为黄色
def back_yellow ():
    style = xlwt.easyxf('pattern: pattern solid, fore_color yellow;') 
    return style

#设置底色为亮绿色
def back_bright_green ():
    style = xlwt.easyxf('pattern: pattern solid, fore_color bright_green;') 
    return style

#设置底色为红色
def back_red ():
    style = xlwt.easyxf('pattern: pattern solid, fore_color red;') 
    return style
 
#xlwt.easyxf('font: height 400, name Arial, colour_index red, bold on, italic on, underline on; align: wrap on, vert centre, horiz center;'))
#easyxf（'hanggao：身高400，名字colour_index宋体，红色，加粗，斜体，下划线；对齐：裹在中心，垂直，水平中心；'））
#设置字体为红色，加粗
def word_red ():
    style = xlwt.easyxf('Font:colour_index red,bold on;') 
    return style
