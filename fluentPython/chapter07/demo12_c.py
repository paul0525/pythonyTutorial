#coding=utf-8
"""
单分派函数
"""
import html


def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

htmlize({1,2,3})