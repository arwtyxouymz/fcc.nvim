#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName:     util
# CreatedDate:  2018-12-03 20:54:48
#


def error(vim, msg):
    msg = (msg if isinstance(msg, str) else str(msg))
    vim.call('fcc#util#print_error', msg)


def echo(vim, msg):
    vim.call('fcc#util#echo', msg)
