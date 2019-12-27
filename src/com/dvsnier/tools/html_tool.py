# -*- coding:utf-8 -*-


def html_linkify(text):
    return text.lower().replace(' ', '_')


def html_header(level, text):
    name = html_linkify(text)
    return '\n<h%d id="%s"><a href="#%s">%s</a></h%d>\n\n' % (
        level, name, name, text, level)
