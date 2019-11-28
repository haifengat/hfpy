#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = '策略报告'
__author__ = 'HaiFeng'
__mtime__ = '20180831'

from .strategy import Strategy
from .data import Data
from .bar import Bar
import os
from .order import OrderItem
import pandas as pd
from pandas import DataFrame, Grouper
import webbrowser
import json
from py_ctp.enums import DirectType, OffsetType
import numpy as np


class Report(object):
    """"""

    def __init__(self, stra: Strategy, base_fund: float = 1000.0):
        """初始化"""
        # self.yi_、_an_Bar_ji_suan = .0 # 一、按Bar计算
        self.chu_shi_zi_jin = base_fund  # 初始资金
        self.zui_da_hui_che_bi_lv = .0  # 最大回撤比率
        self.zui_da_hui_che_qu_jian = .0  # 最大回撤区间
        # self.er_、_an_jiao_yi_bi_shu_ji_suan = .0 # 二、按交易笔数计算
        self.jiao_yi_ci_shu = .0  # 交易次数
        self.ying_li_ci_shu = .0  # 盈利次数
        self.kui_sun_ci_shu = .0  # 亏损次数

        self.zong_ying_li = .0  # 总盈利
        self.zong_kui_sun = .0  # 总亏损
        self.ying_li_yin_zi = .0  # 盈利因子

        self.ping_jun_ying_li = .0  # 平均盈利
        self.ping_jun_kui_sun = .0  # 平均亏损
        self.ping_jun_ying_kui_bi = .0  # 平均盈亏比

        self.jing_li_run = .0  # 净利润
        self.zui_da_ying_li = .0  # 最大盈利
        self.zui_da_kui_sun = .0  # 最大亏损

        self.sheng_lv = .0  # 胜率
        self.zui_da_ying_li_zhan_bi = .0  # 最大盈利占比
        self.zui_da_kui_sun_zhan_bi = .0  # 最大亏损占比

        # self.san_、_an_ri_ji_suan = .0 # 三、按日计算
        self.zong_jiao_yi_tian_shu = .0  # 总交易天数
        self.ying_li_tian_shu = .0  # 盈利天数
        self.kui_sun_tian_shu = .0  # 亏损天数

        self.ping_jun_mei_tian_kui_sun = .0  # 平均每天亏损
        self.ping_jun_mei_tian_ying_li = .0  # 平均每天盈利
        self.ri_jun_ying_kui_bi_bi_lv = .0  # 日均盈亏比比率

        self.zui_da_lian_xu_ying_li_ci_shu = .0  # 最大连续盈利次数
        self.zui_da_lian_xu_kui_sun_ci_shu = .0  # 最大连续亏损次数
        # self.zui_da_lian_xu_ying_li_tian_shu = .0  # 最大连续盈利天数

        self.zui_da_lian_xu_ying_li_jin_e = .0  # 最大连续盈利金额
        self.zui_da_lian_xu_kui_sun_jin_e = .0  # 最大连续亏损金额
        # self.zui_da_lian_xu_kui_sun_tian_shu = .0  # 最大连续亏损天数

        self.zong_shou_yi_lv = .0  # 总收益率
        self.ping_jun_ri_shou_yi = .0  # 平均日收益
        self.nian_hua_shou_yi_lv = .0  # 年化收益率

        self.bo_dong_lv = .0  # 波动率
        self.xia_pu_bi_lv = .0  # 夏普比率
        self.MAR_bi_lv = .0  # MAR比率

        self.zui_da_jing_zhi_bu_chuang_xin_gao_tian_shu = .0  # 最大净值不创新高天数
        # self.zui_da_jing_zhi_bu_chuang_xin_gao_qu_jian = .0  # 最大净值不创新高区间

        # self.wu_、_an_yue_ji_suan = .0 # 五、按月计算
        # self.zong_jiao_yi_yue_shu = .0  # 总交易月数
        # self.ying_li_yue_shu = .0  # 盈利月数
        # self.kui_sun_yue_shu = .0  # 亏损月数
        # self.chi_ping_yue_shu = .0  # 持平月数
        # self.zui_da_lian_xu_ying_li_yue_shu = .0  # 最大连续盈利月数
        # self.zui_da_lian_xu_kui_sun_yue_shu = .0  # 最大连续亏损月数
        # self.ping_jun_mei_yue_ying_li = .0  # 平均每月盈利
        # self.ping_jun_mei_yue_kui_sun = .0  # 平均每月亏损

        self.longwinnlist = []
        self.shortwinnlist = []
        self.winnlist = []

        self.index_description = {'chu_shi_zi_jin': '初始资金',
                                  'zui_da_hui_che_bi_lv': '最大回撤比率',
                                  'zui_da_hui_che_qu_jian': '最大回撤区间',

                                  'jing_li_run': '净利润',
                                  'jiao_yi_ci_shu': '交易次数',
                                  'ying_li_ci_shu': '盈利次数',
                                  'kui_sun_ci_shu': '亏损次数',
                                  'chi_ping_ci_shu': '持平次数',
                                  'zong_ying_li': '总盈利',
                                  'zong_kui_sun': '总亏损',
                                  'ying_li_yin_zi': '盈利因子',
                                  'sheng_lv': '胜率',
                                  'ping_jun_ying_li': '平均盈利',
                                  'ping_jun_kui_sun': '平均亏损',
                                  'ping_jun_ying_kui_bi': '平均盈亏比',
                                  'zui_da_ying_li': '最大单次盈利',
                                  'zui_da_kui_sun': '最大单次亏损',
                                  'zui_da_ying_li_zhan_bi': '最大盈利占比',
                                  'zui_da_kui_sun_zhan_bi': '最大亏损占比',
                                  'zui_da_lian_xu_ying_li_ci_shu': '最大连续盈利次数',
                                  'zui_da_lian_xu_kui_sun_ci_shu': '最大连续亏损次数',
                                  'zui_da_lian_xu_ying_li_jin_e': '最大连续盈利金额',
                                  'zui_da_lian_xu_kui_sun_jin_e': '最大连续亏损金额',

                                  'zong_jiao_yi_tian_shu': '总交易天数',
                                  'ying_li_tian_shu': '盈利天数',
                                  'kui_sun_tian_shu': '亏损天数',
                                  'chi_ping_tian_shu': '持平天数',
                                  'ping_jun_ri_shou_yi': '平均日收益',
                                  'ping_jun_mei_tian_kui_sun': '平均每天亏损',
                                  'ping_jun_mei_tian_ying_li': '平均每天盈利',
                                  'ri_jun_ying_kui_bi_bi_lv': '日均盈亏比比率',
                                  #   'zui_da_lian_xu_ying_li_tian_shu': '最大连续盈利天数',
                                  #   'zui_da_lian_xu_kui_sun_tian_shu': '最大连续亏损天数',
                                  'zui_da_jing_zhi_bu_chuang_xin_gao_tian_shu': '最大净值不创新高天数',
                                  #   'zui_da_jing_zhi_bu_chuang_xin_gao_qu_jian': '最大净值不创新高区间',
                                  'zong_shou_yi_lv': '总收益率',
                                  'nian_hua_shou_yi_lv': '年化收益率',
                                  'bo_dong_lv': '波动率',
                                  'xia_pu_bi_lv': '夏普比率',
                                  'MAR_bi_lv': 'ＭＡＲ比率',

                                  #   'zong_jiao_yi_zhou_shu': '总交易周数',
                                  #   'ying_li_zhou_shu': '盈利周数',
                                  #   'kui_sun_zhou_shu': '亏损周数',
                                  #   'chi_ping_zhou_shu': '持平周数',
                                  #   'zhou_sheng_lv': '周胜率',
                                  #   'ping_jun_mei_zhou_kui_sun': '平均每周亏损',
                                  #   'ping_jun_mei_zhou_ying_li': '平均每周盈利',
                                  #   'zui_da_lian_xu_ying_li_zhou_shu': '最大连续盈利周数',
                                  #   'zui_da_lian_xu_kui_sun_zhou_shu': '最大连续亏损周数',

                                  #   'zong_jiao_yi_yue_shu': '总交易月数',
                                  #   'ying_li_yue_shu': '盈利月数',
                                  #   'kui_sun_yue_shu': '亏损月数',
                                  #   'chi_ping_yue_shu': '持平月数',
                                  #   'zui_da_lian_xu_ying_li_yue_shu': '最大连续盈利月数',
                                  #   'zui_da_lian_xu_kui_sun_yue_shu': '最大连续亏损月数',
                                  #   'ping_jun_mei_yue_kui_sun': '平均每月亏损',
                                  #   'ping_jun_mei_yue_ying_li': '平均每月盈利',

                                  #   'zong_jiao_yi_nian_shu': '总交易年数',
                                  #   'ying_li_nian_shu': '盈利年数',
                                  #   'kui_sun_nian_shu': '亏损年数',
                                  #   'chi_ping_nian_shu': '持平年数',
                                  #   'zui_da_lian_xu_ying_li_nian_shu': '最大连续盈利年数',
                                  #   'zui_da_lian_xu_kui_sun_nian_shu': '最大连续亏损年数',
                                  #   'ping_jun_mei_nian_kui_sun': '平均每年亏损',
                                  #   'ping_jun_mei_nian_ying_li': '平均每年盈利'

                                  }

        data: Data = stra.Datas[0]
        if len(data.Orders) == 0:
            return
        j = ''
        bar: Bar = None
        for bar in data.Bars:
            js = '"D":"{}",'.format(bar.D)
            js += '"TD":{},'.format(bar.Tradingday)
            js += '"O":{},'.format(bar.O)
            js += '"H":{},'.format(bar.H)
            js += '"L":{},'.format(bar.L)
            js += '"C":{},'.format(bar.C)
            js += '"V":{},'.format(bar.V)
            js += '"I":{}'.format(bar.I)
            j += '{{{}}},'.format(js)
        j = '[{}]'.format(j[:-1])
        df_data: DataFrame = pd.read_json(j)
        df_data['D'] = pd.to_datetime(df_data['D'], format='%Y%m%d %H:%M:%S')
        df_data = df_data.set_index('D', drop=True)
        df_data = df_data[['O', 'H', 'L', 'C', 'V', 'I', 'TD']]
        # print(df_data)
        j = ''
        o: OrderItem = None
        for o in data.Orders:
            js = '"D":"{}",'.format(o.DateTime)
            # js += '"OP":"{}",'.format(o.Direction.name[0] + ('K' if o.Offset.name[0] == 'O' else 'P'))
            # js += '"Price":{},'.format(o.Price)
            # js += '"Volume":{}'.format(o.Volume)
            js += '"AvgEntryPriceLong":{},'.format(o.AvgEntryPriceLong)
            js += '"AvgEntryPriceShort":{},'.format(o.AvgEntryPriceShort)
            js += '"PositionLong":{},'.format(o.PositionLong)
            js += '"PositionShort":{},'.format(o.PositionShort)
            # AvgEntryPriceLong 无仓时为0
            js += '"CloseProfit":{},'.format((o.Price - o.AvgEntryPriceLong if o.Direction.name[0] + o.Offset.name[0] == 'SC' else o.AvgEntryPriceShort - o.Price if o.Direction.name[0] + o.Offset.name[0] == 'BC' else 0) * o.Volume)
            j += '{{{}}},'.format(js)
        j = '[{}]'.format(j[:-1])
        df_order: DataFrame = pd.read_json(j)
        df_order['D'] = pd.to_datetime(df_order['D'], format='%Y%m%d %H:%M:%S')
        df_order = df_order.set_index('D', drop=True)
        # df_order = df_order.ix[:, ['AvgEntryPriceLong', 'AvgEntryPriceShort', 'PositionLong', 'PositionShort']]
        # 把交易日和交易合并
        df_data = df_data.join(df_order, on='D', how='left')
        # df_data = df_data.fillna(method='ffill')
        # df_data = df_data.fillna(value=0)
        self.df_data = df_data
        self.stra = stra
        self.get_report(stra)
        self.show(stra)

    def get_report(self, stra: Strategy):
        """按日统计"""
        # 插入一行序号
        nr = {'nr': range(self.df_data.shape[0])}
        self.df_data.insert(12, 'nr', nr['nr'])
        self.df_data['profit10'] = self.df_data['CloseProfit'].notnull()
        self.df_data.insert(13, 'Profit', nr['nr'])

        self.daywinnlist = []
        daysumm = 0
        longpos = 0
        shortpos = 0
        profit = 0.0
        longprice = 0.0
        shortprice = 0.0

        # df_data的循环
        for index, row in self.df_data.iterrows():

            # 没有交易的日子进行填补
            if not row['profit10']:
                self.df_data.at[index, 'PositionShort'] = shortpos
                self.df_data.at[index, 'PositionLong'] = longpos
                self.df_data.at[index, 'CloseProfit'] = profit
                self.df_data.at[index, 'AvgEntryPriceLong'] = longprice
                self.df_data.at[index, 'AvgEntryPriceShort'] = shortprice
                # 多空及无持仓时，profit 的填补
                if self.df_data.at[index, 'PositionLong'] > 0 and self.df_data.at[index, 'PositionShort'] == 0:
                    self.df_data.at[index, 'Profit'] = daysumm + (self.df_data.at[index, 'C'] - self.df_data.at[index, 'AvgEntryPriceLong']) * self.df_data.at[index, 'PositionLong']
                elif self.df_data.at[index, 'PositionShort'] > 0 and self.df_data.at[index, 'PositionLong'] == 0:
                    self.df_data.at[index, 'Profit'] = daysumm + (self.df_data.at[index, 'AvgEntryPriceShort'] - self.df_data.at[index, 'C']) * self.df_data.at[index, 'PositionShort']
                else:
                    self.df_data.at[index, 'Profit'] = daysumm

            # 有交易的日子进行赋值
            if row['profit10'] and row['PositionShort'] == 0 and row['PositionLong'] == 0:
                daysumm = daysumm + row['CloseProfit']
                self.df_data.at[index, 'Profit'] = daysumm
                longpos = 0
                shortpos = 0
                longprice = 0.0
                shortprice = 0.0
                profit = 0.0
            elif row['profit10'] and row['PositionShort'] == 1 and row['PositionLong'] == 0:
                daysumm = daysumm + row['CloseProfit']
                self.df_data.at[index, 'Profit'] = daysumm
                longpos = 0
                shortpos = row['PositionShort']
                longprice = 0
                shortprice = row['AvgEntryPriceShort']
                profit = row['CloseProfit']
            elif row['profit10'] and row['PositionShort'] == 0 and row['PositionLong'] == 1:
                daysumm = daysumm + row['CloseProfit']
                self.df_data.at[index, 'Profit'] = daysumm
                longpos = row['PositionLong']
                shortpos = 0
                longprice = row['AvgEntryPriceLong']
                shortprice = 0
                profit = row['CloseProfit']

            elif row['profit10'] and row['PositionShort'] == 1 and row['PositionLong'] == 1:
                daysumm = daysumm + row['CloseProfit']
                self.df_data.at[index, 'Profit'] = daysumm
                longpos = row['PositionLong']
                shortpos = row['PositionShort']
                longprice = row['AvgEntryPriceLong']
                shortprice = row['AvgEntryPriceLong']
                profit = row['CloseProfit']

        # # self.san_、_an_ri_ji_suan = .0 # 三、按日计算
        self.df_data['post_net'] = self.df_data['PositionLong'] + self.df_data['PositionShort']
        # self.df_data['ProfitLong'] = (self.df_data['C'] - self.df_data['AvgEntryPriceLong']) * self.df_data['PositionLong']
        # self.df_data['ProfitShort'] = (self.df_data['AvgEntryPriceShort'] - self.df_data['C']) * self.df_data['PositionShort']
        # self.df_data['Profit'] = self.df_data['ProfitLong'] + self.df_data['ProfitShort']
        # # self.df_data['Profit_'] = 1 if self.df_data['Profit'] > 0 else -1 if self.df_data['Profit'] < 0 else 0
        # self.df_data['Profit'] = self.df_data['profit2']

        g = self.df_data.groupby('TD', axis=0, sort=True)  # Grouper(freq='1B', axis=0, sort=True))
        df_day: DataFrame = DataFrame()
        df_day['D'] = g.indices

        # 收益累加 按日计算，累计的盈亏
        df_day['Profit'] = g['Profit'].last()
        # 平仓收益按，当日无平仓为零,每日得盈亏
        df_day['CloseProfit'] = g['CloseProfit'].sum()

        # ===================================== 笔统计 ===================

        # 计算单笔收益

        longinprice = 0
        shortinprice = 0
        for o in stra.Datas[0].Orders:
            if o.Offset == OffsetType.Open and o.Direction == DirectType.Buy:
                longinprice = o.Price
            elif o.Offset == OffsetType.Open and o.Direction == DirectType.Sell:
                shortinprice = o.Price
            elif o.Offset == OffsetType.Close and o.Direction == DirectType.Sell:
                winn = o.Price - longinprice
                self.longwinnlist.append(winn)
                self.winnlist.append(winn)
            elif o.Offset == OffsetType.Close and o.Direction == DirectType.Buy:
                winn = shortinprice - o.Price
                self.shortwinnlist.append(winn)
                self.winnlist.append(winn)

        # self.jing_li_run = .0  # 净利润
        self.jing_li_run = self.df_data['Profit'][-1]
        # self.jiao_yi_ci_shu = .0  # 交易次数::当前持仓比下一持仓大,则表示有平仓,即视为一次交易
        self.jiao_yi_ci_shu = len(self.df_data[self.df_data['CloseProfit'] != 0])
        if self.jiao_yi_ci_shu == 0:
            print("没有成交")
            return
        # self.ying_li_ci_shu = .0  # 盈利次数
        self.ying_li_ci_shu = len(self.df_data[self.df_data['CloseProfit'] > 0])
        # self.kui_sun_ci_shu = .0  # 亏损次数
        self.kui_sun_ci_shu = len(self.df_data[self.df_data['CloseProfit'] < 0])
        # self.zong_ying_li = .0  # 总盈利
        self.zong_ying_li = self.df_data[self.df_data['CloseProfit'] > 0]['CloseProfit'].sum()
        # self.zong_kui_sun = .0  # 总亏损
        self.zong_kui_sun = self.df_data[self.df_data['CloseProfit'] < 0]['CloseProfit'].sum()
        # self.sheng_lv = .0  # 胜率
        self.sheng_lv = round(self.ying_li_ci_shu / self.jiao_yi_ci_shu, 4)

        # 计算最大回撤区间和比例  最大不创新高天数
        maxprofit = 0
        nowback = 0
        nowbacklist = []
        nowbackperc = 0
        nowbackperclist = []

        maxmany = 0  # 最大净值
        notmaxmanyday = 0
        maxnotmaxmanyday = 0
        for index, row in df_day.iterrows():
            maxprofit = max(row["Profit"], maxprofit)
            nowback = - (row["Profit"] - maxprofit)
            if nowback != 0 and maxprofit != 0:
                nowbackperc = nowback / (maxprofit + self.chu_shi_zi_jin)
            else:
                nowbackperc = 0
            nowbacklist.append(nowback)
            nowbackperclist.append(nowbackperc)

            maxmany = max(row["Profit"], maxmany)
            if row["Profit"] == maxmany:
                notmaxmanyday = 0
            else:
                notmaxmanyday = notmaxmanyday + 1
                maxnotmaxmanyday = max(maxnotmaxmanyday, notmaxmanyday)

        # 最大净值不创新高天数
        self.zui_da_jing_zhi_bu_chuang_xin_gao_tian_shu = maxnotmaxmanyday
        # 最大回撤比率
        self.zui_da_hui_che_bi_lv = round(max(nowbackperclist), 4)

        # 最大回撤区间
        self.zui_da_hui_che_qu_jian = max(nowbacklist)

        if self.zong_ying_li > 0:
            # self.ping_jun_ying_li = .0  # 平均盈利
            self.ping_jun_ying_li = round(self.zong_ying_li / self.ying_li_ci_shu, 2)
        else:
            # self.ping_jun_ying_li = .0  # 平均盈利
            self.ping_jun_ying_li = 0

        if self.zong_kui_sun < 0:
            # self.ping_jun_kui_sun = .0  # 平均亏损
            self.ping_jun_kui_sun = round(self.zong_kui_sun / self.kui_sun_ci_shu, 2)
            # self.ping_jun_ying_kui_bi = .0  # 平均盈亏比
            self.ping_jun_ying_kui_bi = - round(self.ping_jun_ying_li / self.ping_jun_kui_sun, 2)

        else:
            # self.ping_jun_kui_sun = .0  # 平均亏损
            self.ping_jun_kui_sun = 0
            # self.ping_jun_ying_kui_bi = .0  # 平均盈亏比
            self.ping_jun_ying_kui_bi = 0

        # self.zui_da_ying_li = .0  # 最大盈利
        self.zui_da_ying_li = self.df_data[self.df_data['CloseProfit'] > 0]['CloseProfit'].max()
        # self.zui_da_kui_sun = .0  # 最大亏损
        self.zui_da_kui_sun = self.df_data[self.df_data['CloseProfit'] < 0]['CloseProfit'].min()
        # self.zui_da_ying_li_zhan_bi = .0  # 最大盈利占比
        if self.zong_ying_li > 0:
            self.zui_da_ying_li_zhan_bi = round(self.zui_da_ying_li / self.zong_ying_li, 2)
        else:
            self.zui_da_ying_li_zhan_bi = 0
        # self.zui_da_kui_sun_zhan_bi = .0  # 最大亏损占比
        if self.zong_kui_sun < 0:
            self.zui_da_kui_sun_zhan_bi = round(self.zui_da_kui_sun / self.zong_kui_sun, 2)
        else:
            self.zui_da_kui_sun_zhan_bi = 0
        # # self.zui_da_lian_xu_ying_li_ci_shu = .0  # 最大连续盈利次数
        # self.df_data['CloseProfit_cnt'] = (self.df_data['CloseProfit'] > 0).astype(int)
        # self.df_data['CloseProfit_times'] = self.df_data.groupby((self.df_data['CloseProfit_cnt'] != self.df_data['CloseProfit_cnt'].shift(1)).cumsum()).cumcount() + 1
        # self.zui_da_lian_xu_ying_li_ci_shu = self.df_data['CloseProfit_times'].max()
        # # self.zui_da_lian_xu_kui_sun_ci_shu = .0  # 最大连续亏损次数
        # self.df_data['CloseLoss_cnt'] = (self.df_data['CloseProfit'] < 0).astype(int)
        # self.df_data['CloseLoss_times'] = self.df_data.groupby((self.df_data['CloseLoss_cnt'] != self.df_data['CloseLoss_cnt'].shift(1)).cumsum()).cumcount() + 1
        # self.zui_da_lian_xu_kui_sun_ci_shu = self.df_data['CloseLoss_times'].max()
        # self.ying_li_yin_zi = .0  # 盈利因子
        self.ying_li_yin_zi = round(self.zong_ying_li / self.zong_kui_sun, 2)
        # # self.zui_da_lian_xu_ying_li_jin_e = .0  # 最大连续盈利金额
        # self.df_data['CloseProfit_money'] = self.df_data.groupby((self.df_data['CloseProfit_cnt'] != self.df_data['CloseProfit_cnt'].shift(1)).cumsum()).cumsum()
        # self.zui_da_lian_xu_ying_li_jin_e = self.df_data['CloseProfit_money'].max()
        # # self.zui_da_lian_xu_kui_sun_jin_e = .0  # 最大连续亏损金额
        # self.df_data['CloseLoss_money'] = self.df_data.groupby((self.df_data['CloseLoss_cnt'] != self.df_data['CloseLoss_cnt'].shift(1)).cumsum()).cumsum()
        # self.zui_da_lian_xu_kui_sun_jin_e = self.df_data['CloseLoss_money'].max()

        # =============================== 日统计 =====================
        # self.zui_da_jing_zhi_bu_chuang_xin_gao_tian_shu = .0  # 最大净值不创新高天数
        # self.zui_da_jing_zhi_bu_chuang_xin_gao_qu_jian = .0  # 最大净值不创新高区间
        # self.bo_dong_lv = .0  # 波动率
        self.bo_dong_lv = round((self.df_data['Profit'] / 1000).std(), 2)  # mean收益率

        # self.zong_jiao_yi_tian_shu = .0  # 总交易天数
        self.zong_jiao_yi_tian_shu = len(df_day['Profit'])

        # self.ying_li_tian_shu = .0  # 盈利天数
        self.ying_li_tian_shu = len([p for p in df_day['Profit'] if p > 0])

        # self.kui_sun_tian_shu = .0  # 亏损天数
        self.kui_sun_tian_shu = len([p for p in df_day['Profit'] if p < 0])

        # self.ping_jun_ri_shou_yi = .0  # 平均日收益
        self.ping_jun_ri_shou_yi = round(df_day['Profit'] / self.zong_jiao_yi_tian_shu, 2)

        # self.ping_jun_mei_tian_kui_sun = .0  # 平均每天亏损
        self.ping_jun_mei_tian_kui_sun = round(sum([p for p in df_day['Profit'] if p < 0]) / self.zong_jiao_yi_tian_shu, 2)

        # self.ping_jun_mei_tian_ying_li = .0  # 平均每天盈利
        self.ping_jun_mei_tian_ying_li = round(sum([p for p in df_day['Profit'] if p > 0]) / self.zong_jiao_yi_tian_shu, 2)

        # self.ri_jun_ying_kui_bi_bi_lv = .0  # 日均盈亏比比率
        self.ri_jun_ying_kui_bi_bi_lv = 0 if self.ping_jun_mei_tian_kui_sun == 0 else round(self.ping_jun_mei_tian_ying_li / self.ping_jun_mei_tian_kui_sun, 4)

        # self.zui_da_lian_xu_ying_li_tian_shu = .0  # 最大连续盈利天数

        # self.zui_da_lian_xu_kui_sun_tian_shu = .0  # 最大连续亏损天数
        # 计算最大盈利和亏损次数 金额
        winntime = 0
        losstime = 0
        winnmany = 0
        lossmany = 0

        maxwinntime = 0
        maxlosstime = 0
        maxwinnmany = 0
        maxlossmany = 0

        for winns in self.winnlist:
            if winns > 0:
                maxlosstime = max(maxlosstime, losstime)
                losstime = 0
                winntime = winntime + 1
                maxlossmany = min(maxlossmany, lossmany)
                lossmany = 0
                winnmany = winnmany + winns
            elif winns < 0:
                maxwinntime = max(winntime, maxwinntime)
                winntime = 0
                losstime = losstime + 1
                maxwinnmany = max(winnmany, maxwinnmany)
                winnmany = 0
                lossmany = lossmany + winns

        self.zui_da_lian_xu_ying_li_ci_shu = maxwinntime
        self.zui_da_lian_xu_kui_sun_ci_shu = maxlosstime
        self.zui_da_lian_xu_ying_li_jin_e = maxwinnmany
        self.zui_da_lian_xu_kui_sun_jin_e = maxlossmany

        '''
        # self.zui_da_lian_xu_ying_li_tian_shu = .0  # 最大连续盈利天数
        df_day['Profit_cnt'] = (df_day['Profit'] > 0).astype(int)
        df_day['Profit_days'] = df_day.groupby((df_day['Profit_cnt'] != df_day['Profit_cnt'].shift(1)).cumsum()).cumcount() + 1
        self.zui_da_lian_xu_ying_li_tian_shu = df_day['Profit_days'].max()

        # self.zui_da_lian_xu_kui_sun_tian_shu = .0  # 最大连续亏损天数
        df_day['Loss_cnt'] = (df_day['Profit'] < 0).astype(int)
        df_day['Loss_days'] = df_day.groupby((df_day['Loss_cnt'] != df_day['Loss_cnt'].shift(1)).cumsum()).cumcount() + 1
        self.zui_da_lian_xu_kui_sun_tian_shu = df_day['Loss_days'].max()
        '''
        # self.zong_shou_yi_lv = .0  # 总收益率
        self.zong_shou_yi_lv = round(self.df_data['Profit'][-1] / self.chu_shi_zi_jin, 2)

        # self.xia_pu_bi_lv = .0  # 夏普比率
        self.xia_pu_bi_lv = round((self.zong_shou_yi_lv - 0.04) / self.bo_dong_lv, 4)

        # self.MAR_bi_lv = .0  # MAR比率
        self.MAR_bi_lv = round(self.zong_shou_yi_lv / self.zui_da_hui_che_bi_lv, 4)

        # self.nian_hua_shou_yi_lv = .0  # 年化收益率
        g_year = self.df_data.groupby(Grouper(freq='12M', axis=0, sort=True))
        self.nian_hua_shou_yi_lv = round(self.df_data['Profit'].sum() / len(g_year) / self.chu_shi_zi_jin, 2)

    def show(self, stra: Strategy):
        report = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'template.html'), 'r', encoding='utf-8').read()
        tempData = []
        reportData = []
        for k, v in vars(self).items():
            if type(v) == float or type(v) == int or type(v) == np.float64:
                tempData.append({
                    'item': self.index_description[k],
                    'value': v
                })

        if len(tempData) % 3 == 0:
            rownum = int(len(tempData) / 3)
        else:
            rownum = int(len(tempData) / 3) + 1
            tempData.append({
                'item': '',
                'value': ''
            })
            if len(tempData) % 3 == 2:
                tempData.append({
                    'item': '',
                    'value': ''
                })

        for i in range(rownum):
            reportData.append({
                'item_1': tempData[i]['item'],
                'value_1': tempData[i]['value'],
                'item_2': tempData[rownum * 1 + i]['item'],
                'value_2': tempData[rownum * 1 + i]['value'],
                'item_3': tempData[rownum * 2 + i]['item'],
                'value_3': tempData[rownum * 2 + i]['value']
            })

        # items_per_row = 3
        # table = '<tr>'
        # for i in range(items_per_row):
        #     table += '<td>项目</td><td>值</td>'
        # table += '</tr><tr>'
        # idx = 0
        # for k, v in vars(self).items():
        #     print(self.index_description[k], v)
        #     if str(type(v)).find('int') > 0:
        #         table += '<td>{}</td><td>{}</td>'.format(self.index_description[k], v)
        #         # print('{0:{2}<12}:{1:>9d}.   |'.format(self.index_description[k], v, chr(12288)), end='\t')
        #     elif str(type(v)).find('float') > 0:
        #         table += '<td>{}</td><td>{}</td>'.format(self.index_description[k], v)
        #         # print('{0:{2}<12}:{1:>13.3f}|'.format(self.index_description[k], v, chr(12288)), end='\t')
        #     else:
        #         continue
        #     idx += 1
        #     if idx % items_per_row == 0:
        #         table += '</tr><tr>'
        #         # print('')
        # table += '</tr>'
        report = report.replace('$report_table$', str(json.dumps(reportData)))

        bars_json = []
        for bar in self.stra.Bars:
            bars_json.append([bar.D, bar.O, bar.C, bar.L, bar.H])
        report = report.replace('$bars$', str(bars_json))

        orders_json = []
        for ord in self.stra.Orders:
            # 遇到diction=Diction.Buy转换后:diction:<Diction.Buy:1> 后面报错
            # orders_str.append(ord.__dict__)
            orders_json.append([ord.DateTime, (0 if ord.Direction == DirectType.Buy else 1), (0 if ord.Offset == OffsetType.Open else 1), ord.Price, ord.Volume])
        report = report.replace('$orders$', json.dumps(orders_json))

        g = self.df_data.groupby('TD', axis=0, sort=True)  # Grouper(freq='1B', axis=0, sort=True))
        df_day: DataFrame = DataFrame()
        df_day['D'] = g.indices

        # 收益累加 按日计算，累计的盈亏
        df_day['Profit'] = g['Profit'].last()
        # 平仓收益按，当日无平仓为零,每日得盈亏
        df_day['CloseProfit'] = g['CloseProfit'].sum()

        lei_ji_shou_yi = df_day['Profit']
        quanyi = lei_ji_shou_yi.to_dict().items()
        quanyi = [[k, v] for k, v in quanyi]
        report = report.replace('$quanyi$', str(quanyi))

        # 计算累计收益率 做多和做空的

        winnsumlist = np.array(self.winnlist, dtype=float).cumsum()
        longwinnsumlist = np.array(self.longwinnlist, dtype=float).cumsum()
        shortwinnsumlist = np.array(self.shortwinnlist, dtype=float).cumsum()

        leijishouyi = []
        longleijishouyi = []
        shortleijishouyi = []
        for x in range(len(winnsumlist)):
            leijishouyi.append([x, winnsumlist[x]])

        for x in range(len(longwinnsumlist)):
            longleijishouyi.append([x, longwinnsumlist[x]])

        for x in range(len(shortwinnsumlist)):
            shortleijishouyi.append([x, shortwinnsumlist[x]])

        report = report.replace('$leijishouyi$', str(leijishouyi))
        report = report.replace('$longleijishouyi$', str(longleijishouyi))
        report = report.replace('$shortleijishouyi$', str(shortleijishouyi))

        with open('r.html', 'w', encoding='utf-8') as w:
            w.write(report)
        webbrowser.open("r.html")
