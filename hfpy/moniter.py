#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = '监控所有策略'
__author__ = '海风'
__mtime__ = '20181106'

from .hfpy import HFPY


class Moniter(object):
    """监控所有策略持仓"""
    def __init__(self, atp: HFPY):
        self.posi = [{'Strategy': type(stra), 'Params': stra.Params, 'Position': stra.Position, 'PositionLong': stra.PositionLong, 'PositionShort': stra.PositionShort} for stra in atp.stra_instances]
