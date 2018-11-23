#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 2:14 PM
# @Author  : Motao
# @Site    : 
# @File    : view.py
# @Software: PyCharm
from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    # 使用一个字典context作为参数
    context = {}
    # context 字典中元素的键值 "hello" 对应了模板中的变量 "{{ hello }}"
    context['hello'] = "HELLO WORLD"
    # 使用render来替代之前使用的HttpResponse
    return render(request, "hello.html", context)

def base(request):
    return render(request, 'base.html')
