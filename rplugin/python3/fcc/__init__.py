#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName:     __init__
# CreatedDate:  2018-12-03 20:24:31
#

import os
import shutil
from importlib import find_loader
from fcc import util

if find_loader('pynvim'):
    import pynvim
    vim = pynvim
else:
    import neovim
    vim = neovim


@vim.plugin
class FCC(object):
    def __init__(self, vim):
        self._vim = vim

    @vim.command('FindCompileCommands', nargs='*', range='')
    def find_compile_commands_json(self, args, range):
        self._vim.call("fcc#initialize")
        current = self._vim.funcs.getcwd()
        pacakge_path = self.get_package_path(current)
        pacakge_name = os.path.basename(pacakge_path)
        if not pacakge_name:
            util.error(self._vim, "Cannot detect package name!")
            return
        catkin_ws = self._vim.vars['fcc#catkin_ws']
        # copy
        json_path = os.path.join(catkin_ws, "build", pacakge_name)
        if "compile_commands.json" in os.listdir(json_path):
            util.echo(self._vim, "Correctly copied!")
            shutil.copy(os.path.join(json_path, "compile_commands.json"), pacakge_path)
        else:
            util.error(self._vim, "compile_commands.json was not found!")

    def get_package_path(self, current):
        nest = int(self._vim.vars['fcc#nest_num'])
        for _ in range(nest):
            flag = self.check_exist(current)
            if flag:
                break
            current = os.path.abspath(os.path.join(current, os.path.pardir))
        return current if flag else None

    def check_exist(self, path):
        return 'package.xml' in os.listdir(path)
