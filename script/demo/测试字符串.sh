#!/usr/bin/env bash


########## 拼接字符串 ##########
your_name="runoob"
# 使用双引号拼接
echo -e "\n双引号"
greeting="hello, "$your_name" !"
greeting_1="hello, ${your_name} !"
echo -e $greeting "\n" $greeting_1
# 使用单引号拼接
echo -e "\n单引号"
greeting_2='hello, '$your_name' !'
greeting_3='hello, ${your_name} !'
echo -e $greeting_2 "\n" $greeting_3

########## 获取字符串长度 ##########
echo -e "\n"
string="abcd"
echo ${#string} #输出 4

########## 提取子字符串 ##########

echo -e "\n"
string="runoob is a great site"
echo ${string:1:4} # 输出 unoo

########## 查找子字符串 ##########

echo -e "\n"
string="runoob is a great site"
echo `expr index "$string" io`  # 输出 4