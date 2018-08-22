#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/11/2'
"""

import zmq
import gzip
import json
import os
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import copy
from py_ctp.enums import OffsetType, DirectType
from .structs import IntervalType, ReqPackage
from .switch import switch


class Statistics(object):
    """"""

    def __init__(self, stra):
        """"""

        self.__path = os.getcwd() + '/report/'

        if not os.path.exists(self.__path):
            os.makedirs(self.__path)
        self.__interest = 'simple'
        # 基本变量定义
        self.__stra = stra
        self.__DictInstrument = {}
        self.__Report = []
        # 更新品种数据
        products = self.__get_product_zmq()
        for prod in products:
            for data in stra.Datas:
                if prod['_id'] == data.Instrument[0:len(prod['_id'])]:
                    self.__DictInstrument[data.Instrument] = prod
                break
        # 定义equity
        self.minEquity = []
        self.dayEquity = []
        self.weekEquity = []
        self.monthEquity = []
        self.yearEquity = []
        # 定义按笔计算指标
        self.listAccumuProfit = []  # 累计利润列表
        self.tListSingleProfit = []  # 单笔利润列表
        self.tTotalCount = .0  # 交易次数
        self.tGainCount = .0  # 盈利次数
        self.tLossCount = .0  # 亏损次数
        self.tHoldCount = .0  # 持平次数
        self.tGainAmount = .0  # 总盈利
        self.tLossAmount = .0  # 总亏损
        self.tProfitFactor = .0  # 盈利因子
        self.tTotalNetProfit = .0  # 净利润
        self.tWinRate = .0  # 每笔交易胜率
        self.tAvgGain = .0  # 平均每笔盈利
        self.tAvgLoss = .0  # 平均每笔亏损
        self.tAvgGLRate = .0  # 平均盈亏比
        self.tMaxGain = .0  # 最大盈利
        self.tMaxLoss = .0  # 最大亏损
        self.tMaxGainRatio = .0  # 最大盈利/总盈利
        self.tMaxLossRatio = .0  # 最大亏损/总亏损
        self.tMaxContGainCount = .0  # 最大连续盈利次数
        self.tMaxContLossCount = .0  # 最大连续亏损次数
        self.tMaxContGainAmount = .0  # 最大连续盈利金额
        self.tMaxContLossAmount = .0  # 最大连续亏损金额
        # 定义按1分钟bar计算指标
        self.bListRddrate = []
        self.bMddRate = .0
        self.dDropDownPeriod = ''
        self.bInitFund = 0
        # 定义按日线计算指标
        self.dListDayYield = []
        self.dListDayNetValue = []
        self.dTotalCount = 0  # 总交易天数
        self.dGainCount = 0  # 盈利天数
        self.dLossCount = 0  # 亏损天数
        self.dHoldCount = 0  # 持平天数
        self.dWinRate = .0  # 胜率
        self.dAvgYield = .0  # 平均日收益
        self.dAvgLoss = .0  # 平均每天亏损
        self.dAvgGain = .0  # 平均每天盈利
        self.dAvgGLRate = .0  # 日均盈亏比比率
        self.dMaxContGainCount = .0  # 最大连续盈利天数
        self.dMaxContLossCount = .0  # 最大连续亏损天数
        self.dTotalyield = .0  # 总收益率
        self.dYearYield = .0  # 年化收益率
        self.dVolatility = .0  # 波动率
        self.dSharpRitio = .0  # 夏普比率
        self.dMarRate = .0  # MAR比率
        self.dNoNewHighDays = .0
        self.dNoNewHighPeriod = ''
        # 定义按周线计算指标
        self.wListWeekNetValue = []  # 周净值
        self.wListWeekYield = []  # 周收益率
        self.wTotalCount = .0  # 总交易周数
        self.wGainCount = .0  # 盈利周数
        self.wLossCount = .0  # 亏损周数
        self.wHoldCount = .0  # 持平周数
        self.wWinRate = .0  # 周胜率
        self.wAvgLoss = .0  # 平均每周亏损
        self.wwvgGain = .0  # 平均每周盈利
        self.wMaxContGainCount = .0  # 最大连续盈利周数
        self.wMaxContLossCount = .0  # 最大连续亏损周数
        # 定义按月线计算指标
        self.mListMonthNetValue = []  # 月收益净值
        self.mListMonthYield = []  # 月收益率
        self.mTotalCount = .0  # 总交易月数
        self.mGainCount = .0  # 盈利月数
        self.mLossCount = .0  # 亏损月数
        self.mHoldCount = .0  # 持平月数
        self.mMaxContGainCount = .0  # 最大连续盈利月数
        self.mMaxContLossCount = .0  # 最大连续亏损月数
        self.mAvgLoss = .0  # 平均每月亏损
        self.mAvgGain = .0  # 平均每月盈利
        # 定义按年线计算指标
        self.yListYearNetValue = []  # 年收益净值
        self.yListYearYield = []  # 年收益率
        self.yTotalCount = .0  # 交易年数
        self.yGainCount = .0  # 盈利年数
        self.yLossCount = .0  # 亏损年数
        self.yHoldCount = .0  # 持平年数
        self.yMAxContGainCount = .0  # 最大连续盈利年数
        self.yMaxContLossCount = .0  # 最大连续亏损年数
        self.yAvgLoss = .0  # 平均每年可亏损
        self.yAvgGain = .0  # 平均每年盈

        self.__countFromTradeRecord(stra)
        self.minEquity = self.__getMinBarEquity(stra)
        self.__getOtherEquitys()
        self.__countBarPerfermence()
        self.__countDayPerfermence()
        self.__countWeekPerfermence()
        self.__countMonthPerfermence()
        self.__countYearPerfermence()
        self.__printf()
        # self.showSignalPoint()
        # self.__plotf()
        self.__ShowWeb()

        # self.CalculateProfit()

    def __getMinBarEquity(self, stra):
        # 获取交易记录
        # tradeRecords=stra.Orders
        # dfTrade=pd.DataFrame(index=['datet','instrument','direction','offset','volume','price'])
        # for j in range(len(tradeRecords)):
        #     dfTrade[j]=[tradeRecords[j].DateTime,tradeRecords[j].Instrument,tradeRecords[j].Direction,tradeRecords[j].Offset,tradeRecords[j].Volume,tradeRecords[j].Price]

        # dfTrade=dfTrade.T

        # #获取历史数据
        # minBars=self.read_from_mq(stra.Datas[0])
        # dfMin=pd.DataFrame(index=['D','O','H','L','C','V','I'])
        # for i in range(len(minBars)):
        #     dfMin[i]=[minBars[i]['_id'],minBars[i]['Open'],minBars[i]['High'],minBars[i]['Low'],minBars[i]['Close'],minBars[i]['Volume'],minBars[i]['OpenInterest']]
        # dfMin=dfMin.T
        # dfLog=pd.merge(dfMin,dfTrade,how='left',left_on='D',right_on='datet')
        # # print(dfLog)
        # #计算权益
        # Multiplier=self.__DictInstrument[stra.Instrument]['VolumeTuple']
        # position=0
        # entryprice=0
        # floatprofit=0
        # closeprofit=0
        # lstMinEquity=[]
        # initfund=10000
        # equity=0
        # for index,row in dfLog.iterrows():

        #     if not pd.isnull(row.datet):
        #         if row.direction==DirectType.Buy and row.offset==OffsetType.Open:
        #             position=position+row.volume
        #             entryprice=row.price
        #         if row.direction==DirectType.Buy and row.offset==OffsetType.Close:
        #             closeprofit += (entryprice-row.price) * row.volume * Multiplier
        #             position=position+row.volume
        #         if row.direction==DirectType.Sell and row.offset==OffsetType.Open:
        #             position=position-row.volume
        #             entryprice=row.price
        #         if row.direction==DirectType.Sell and row.offset==OffsetType.Close:
        #             closeprofit += (row.price-entryprice) * row.volume * Multiplier
        #             position=position-row.volume
        #     #计算浮动盈亏
        #     if position > 0:
        #         floatprofit =  Multiplier* (row.C - entryprice)*position
        #     elif position<0:
        #         floatprofit = Multiplier * (entryprice - row.C)*(-position)
        #     else:
        #         floatprofit=0
        #     print('{0}  {1}  {2}'.format(equity,floatprofit,closeprofit));
        #     equity=initfund+floatprofit+closeprofit
        #     # print([row.D,equity])
        #     lstMinEquity.append([row.D,equity])
        fmin = open(self.__path + 'MinEquity.csv', 'w')
        for item6 in stra.listEquity:
            fmin.write('%s,%.2f\n' % (item6[0], item6[1]))
        fmin.flush()
        fmin.close()
        # for item in stra.listEquity:
        #     print(item)
        return stra.listEquity
        # print(lstMinEquity)

    def __getOtherEquitys(self):

        ################计算日动态权益##########################################
        firstmin = True
        lastdthour = 0
        lastdt = 0
        lastequity = 0
        # for  minindex,minitem in eq.iteritems():
        for mitem in self.minEquity:
            if firstmin:
                firstmin = False
                dt = datetime.datetime.strptime(mitem[0], '%Y%m%d %H:%M:%S')
                lastdt = dt
                dt = dt+datetime.timedelta(days=-1)
                dtday = datetime.datetime.strftime(dt, '%Y-%m-%d')
            else:
                dt = datetime.datetime.strptime(mitem[0], '%Y%m%d %H:%M:%S')
                equity = mitem[1]

                if 12 < lastdt.hour < 16 and (dt.hour > 16 or dt.hour < 12):
                    dtday = datetime.datetime.strftime(lastdt, '%Y-%m-%d')
                    self.dayEquity.append([dtday, lastequity])
                lastdthour = dt.hour
                lastequity = equity
                lastdt = dt
        dtday = datetime.datetime.strftime(lastdt, '%Y-%m-%d')
        self.dayEquity.append([dtday, lastequity])
        fday = open(self.__path + 'DayEquity.csv', 'w')
        for item in self.dayEquity:
            fday.write('%s,%.2f\n' % (item[0], item[1]))
        fday.flush()
        fday.close()

        #########################周############################################

        # 计算周动态权益

        last = ()
        first = True
        second = True
        lastrow = 0
        lastindex = 0
        for witem in self.dayEquity:

            day = datetime.datetime.strptime(witem[0], '%Y-%m-%d')
            nowday = day.isocalendar()
            if first:
                self.weekEquity.append([witem[0], witem[1]])
                first = False
            elif second:
                second = False
            else:
                if nowday[2] < last[2]:
                    self.weekEquity.append([lastindex, lastrow])
                elif nowday[2] == last[2]:
                    self.weekEquity.append([lastindex, lastrow])
                elif nowday[2] > last[2]:
                    if nowday[1] != last[1]:
                        self.weekEquity.append([lastindex, lastrow])
            last = nowday
            lastindex = witem[0]
            lastrow = witem[1]
        self.weekEquity.append([lastindex, lastrow])
        fweek = open(self.__path + 'WeekEquity.csv', 'w')
        for fwitem in self.weekEquity:
            fweek.write('%s,%.2f\n' % (fwitem[0], fwitem[1]))
        fweek.flush()
        fweek.close()
       # 3
        # 计算月动态权益

        first = 0
        lastrow = 0

        for item2 in self.dayEquity:
            day = datetime.datetime.strptime(item2[0], '%Y-%m-%d')

            a = day.day
            if not first:
                self.monthEquity.append([item2[0], item2[1]])
                lastindex = item2[0]
                lastrow = item2[1]
                first = a
                continue
            elif a > first:
                lastindex = item2[0]
                lastrow = item2[1]
                first = a
            else:
                self.monthEquity.append([lastindex, lastrow])
                lastindex = item2[0]
                lastrow = item2[1]
                first = a
        self.monthEquity.append([lastindex, lastrow])
        fmonth = open(self.__path + '/MonthEquity.csv', 'w')
        for item in self.monthEquity:
            fmonth.write('%s,%.2f\n' % (item[0], item[1]))
        fmonth.flush()
        fmonth.close()
        # 3
        # 计算年动态权益
        first = 0
        lastrow = 0
        lastindex = 0
        for row in self.monthEquity:
            day = datetime.datetime.strptime(row[0], '%Y-%m-%d')
            if not first:
                self.yearEquity.append(row)
                lastrow = row
                lastindex = row[0]
                first = day.year
            elif day.year > first:
                self.yearEquity.append(lastrow)
                lastrow = row
                lastindex = row[0]
                first = day.year
            elif day.year == first:
                lastrow = row
                lastindex = row[0]
                first = day.year
        self.yearEquity.append(lastrow)
        fyear = open(self.__path + '/YearEquity.csv', 'w')
        for item in self.yearEquity:
            fyear.write('%s,%.2f\n' % (item[0], item[1]))
        fyear.flush()
        fyear.close()

    def __countBarPerfermence(self):
        # equity = pd.read_csv(self.__path+'Equity.csv',names=['dtime','captical'])

        mrdd = 0
        isfirst = True
        frontpoint = 1
        bListrdd = []
        ddperiod = ''

        # eq = equity['captical']
        # eqNetValue = eq / eq[0] if eq[0] != 0 else float('inf')
        #
        # for item in eqNetValue:
        #     frontpoint = item if item > frontpoint else frontpoint
        #
        #     drowdown = frontpoint - item if item < frontpoint else 0
        #     rdd = drowdown / frontpoint
        #     bListrdd.append(-rdd)
        #     # mdd = drowdown if drowdown > mdd else mdd
        #     mrdd = rdd if rdd > mrdd else mrdd
        #
        # self.bListRddrate = bListrdd
        # self.bMddRate = mrdd  # 最大回撤比率
        mrddbegin = ''
        # equity.captical = equity.captical / equity.captical[0] if equity.captical[0] != 0 else float('inf')
        # for key, value in equity.iterrows():
        for dayitem1 in self.minEquity:
            if isfirst:
                frontpoint = dayitem1[1]
                isfirst = False
                continue
            if dayitem1[1] > frontpoint:
                frontpoint = dayitem1[1]
                mrddbegin = (dayitem1[0], round(dayitem1[1], 5))

            # frontpoint = value[1] if value[1] > frontpoint else frontpoint

            drowdown = frontpoint - dayitem1[1] if dayitem1[1] < frontpoint else 0
            rdd = drowdown / frontpoint
            bListrdd.append(-rdd)
            # mdd = drowdown if drowdown > mdd else mdd
            if rdd > mrdd:
                mrdd = rdd
                mrddend = (dayitem1[0], round(dayitem1[1], 5))
                ddperiod = str(mrddbegin)+'-'+str(mrddend)
        self.bListRddrate = bListrdd
        self.bMddRate = np.round(mrdd, 4)
        self.dDropDownPeriod = ddperiod
        self.bInitFund = self.minEquity[0][1]

    def __plottest(self, eq):

        fig1 = plt.figure('日级别动态权益图')
        ax1 = plt.subplot(311)
        ax1.xaxis_date()
        # ax1.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))#设置时间标签显示格式
        # plt.xticks(pd.date_range(demo0719.index[0],demo0719.index[-1],freq='1day'))
        plt.ylabel('Equity')

        plt.title('Equity of Day')

        plt.plot(eq, color='red')

        # plt.savefig(self.__path + 'Day2.png')

    def __countDayPerfermence(self):
        dfday = pd.read_csv(self.__path + 'DayEquity.csv', header=None, index_col=0,
                            names=['captical'])
        # self.plottest(dfday)
        eq = np.array(dfday['captical'])

        eqtemp = np.zeros(len(eq))
        eqYield = np.zeros(len(eq))
        eqtemp[0] = np.array(eq[0])
        eqtemp[1:] = eq[0:len(eq) - 1]
        # eqYield = (eq - eqtemp) / eqtemp
        eqYield = (eq - eqtemp)
        eqNetValue = eq
        maxContGainDayCount = 0
        maxContLossDayCount = 0

        noNewBegin = False
        maxNoNewHighBegin = 0
        maxNoNewHighEnd = 0
        noNewHighBegin = 0
        noNewHighEnd = 0
        maxNoNewHighDays = 0
        isfirst = True

        gaincount = 0
        losscount = 0
        fronthigh = 0

        # 计算未创新高天数
        for index, value in dfday.iterrows():
            if isfirst:
                fronthigh = value[0]
                isfirst = False
            if value[0] > fronthigh:
                fronthigh = value[0]
                noNewHighBegin = index
                noNewHighEnd = index
                noNewBegin = True
            else:
                noNewHighEnd = index
            if noNewBegin:
                noNewHighDays = (datetime.datetime.strptime(noNewHighEnd, '%Y-%m-%d') -
                                 datetime.datetime.strptime(noNewHighBegin, '%Y-%m-%d')).days
                if noNewHighDays > maxNoNewHighDays:
                    maxNoNewHighDays = noNewHighDays
                    maxNoNewHighBegin = noNewHighBegin
                    maxNoNewHighEnd = noNewHighEnd

        for item in eqYield:
            if item > 0:
                losscount = 0
                gaincount += 1
                maxContGainDayCount = gaincount if gaincount > maxContGainDayCount else maxContGainDayCount

            elif item < 0:
                gaincount = 0
                losscount += 1
                maxContLossDayCount = losscount if losscount > maxContLossDayCount else maxContLossDayCount
            else:
                gaincount = 0
                gaincount = 0

        totalcount = eqYield.size-1
        gaincount = (eqYield[eqYield > 0]).size
        losscount = (eqYield[eqYield < 0]).size
        holdcount = (eqYield[eqYield == 0]).size - 1
        winrate = gaincount / (gaincount + losscount) if (gaincount + losscount) != 0 else 0
        avgyield = np.average(eqYield)
        avgloss = np.average(eqYield[eqYield < 0]) if len(eqYield[eqYield < 0]) > 0 else 0
        avggain = np.average(eqYield[eqYield > 0]) if len(eqYield[eqYield > 0]) > 0 else 0
        avgPLRate = -avggain / avgloss if avgloss != 0 else 0

        totalYield = (eqNetValue[-1] - eqNetValue[0]) / eqNetValue[0] if eqNetValue[0] != 0 else 0

        # 按复利计算
        if self.__interest == 'compound':
            print('年化收益按复利计算')
            dayYield = np.power(totalYield + 1, 1.0 / float(eq.size)) - 1
            yearYield = (1 + float(dayYield)) ** 242.0 - 1
        # 按单利计算
        else:
            print('年化收益按单利计算')
            # print  totalYield
            dayYield = totalYield/float(eq.size)
            yearYield = dayYield*242
            print(yearYield)
        # yearYield=np.power(3.87+1,242.0/1830)-1
        volatility = np.std(eqYield)

        sharpRitio = np.sqrt(242) * eqYield.mean() / np.std(eqYield) if len(eqYield) > 0 else 0
        marrate = yearYield / self.bMddRate if self.bMddRate != 0 else 0

        self.dListDayYield = list(eqYield)
        self.dListDayNetValue = list(eqNetValue)

        self.dTotalCount = totalcount  # 总交易天数
        self.dGainCount = gaincount  # 盈利天数
        self.dLossCount = losscount  # 亏损天数
        self.dHoldCount = holdcount  # 持平天数
        self.dWinRate = np.round(winrate, 4)  # 胜率
        self.dAvgYield = np.round(avgyield, 4)  # 平均日收益
        self.dAvgLoss = np.round(avgloss, 4)  # 平均每天亏损
        self.dAvgGain = np.round(avggain, 4)  # 平均每天盈利
        self.dAvgGLRate = np.round(avgPLRate, 4)  # 日均盈亏比比率
        self.dMaxContGainCount = maxContGainDayCount  # 最大连续盈利天数
        self.dMaxContLossCount = maxContLossDayCount  # 最大连续亏损天数

        self.dTotalyield = np.round(totalYield, 4)  # 总收益率
        self.dYearYield = np.round(yearYield, 4)  # 年化收益率
        self.dVolatility = np.round(volatility, 4)  # 波动率
        self.dSharpRitio = np.round(sharpRitio, 4)  # 夏普比率
        self.dMarRate = np.round(marrate, 4)  # MAR比率

        self.dNoNewHighDays = maxNoNewHighDays
        self.dNoNewHighPeriod = str(maxNoNewHighBegin)+'----'+str(maxNoNewHighEnd)

    def __countWeekPerfermence(self):
        losscount = 0
        gaincount = 0
        holdcount = 0
        maxContGainDayCount = 0
        maxContLossDayCount = 0

        dfweek = pd.read_csv(self.__path + 'WeekEquity.csv', header=None, index_col=0,
                             names=['captical'])
        initfund = dfweek['captical'][0]
        isbegin = True
        eq = np.array(dfweek['captical'])
        eq2 = np.zeros(len(dfweek))
        eq2[0] = eq[0]
        eq2[1:] = eq[0:len(eq) - 1]
        eqYield = (eq - eq2) / eq2
        eqNetValue = eq

        for item in eqYield:
            if item > 0:
                losscount = 0
                gaincount += 1
                maxContGainDayCount = gaincount if gaincount > maxContGainDayCount else maxContGainDayCount

            elif item < 0:
                gaincount = 0
                losscount += 1
                maxContLossDayCount = losscount if losscount > maxContLossDayCount else maxContLossDayCount
            else:
                gaincount = 0
                gaincount = 0

        losscount = eqYield[eqYield < 0].size
        gaincount = eqYield[eqYield > 0].size
        holdcount = eqYield[eqYield == 0].size - 1
        totalcount = eqYield.size - 1
        avgloss = np.average(eqYield[eqYield < 0]) if len(eqYield[eqYield < 0]) > 0 else 0
        avggain = np.average(eqYield[eqYield > 0]) if len(eqYield[eqYield > 0]) > 0 else 0

        avgPLRate = avggain / avgloss if avgloss != 0 else 0
        winRate = gaincount / (gaincount + losscount) if gaincount + losscount > 0 else 0

        self.wListWeekNetValue = eqNetValue  # 周净值
        self.wListWeekYield = eqYield  # 周收益率

        self.wTotalCount = totalcount  # 总交易周数
        self.wGainCount = gaincount  # 盈利周数
        self.wLossCount = losscount  # 亏损周数
        self.wHoldCount = holdcount  # 持平周数
        self.wWinRate = np.round(winRate, 4)  # 周胜率
        self.wAvgLoss = np.round(avgloss, 4)  # 平均每周亏损
        self.wwvgGain = np.round(avggain, 4)  # 平均每周盈利
        self.wMaxContGainCount = maxContGainDayCount  # 最大连续盈利周数
        self.wMaxContLossCount = maxContLossDayCount  # 最大连续亏损周数

    def __countMonthPerfermence(self):

        listMonthYield = []
        listMonthNetValue = []
        losscount = 0
        gaincount = 0

        maxContLossMonthCount = 0
        maxContGainMonthCount = 0

        dfmonth = pd.read_csv(self.__path + 'MonthEquity.csv', header=None, index_col=0,
                              names=['captical'])
        eq = np.array(dfmonth['captical'])
        eq2 = np.zeros(len(eq))
        eq3 = np.zeros(len(eq))
        eq2[0] = eq[0]
        eq2[1:] = eq[0:len(eq) - 1]
        eq3 = (eq - eq2) / eq2
        eq4 = eq

        for item in eq3:
            if item > 0:
                losscount = 0
                gaincount += 1
                maxContGainMonthCount = gaincount if gaincount > maxContGainMonthCount else maxContGainMonthCount

            elif item < 0:
                gaincount = 0
                losscount += 1
                maxContLossMonthCount = losscount if losscount > maxContLossMonthCount else maxContLossMonthCount
            else:
                gaincount = 0
                gaincount = 0
        losscount = eq3[eq3 < 0].size
        gaincount = eq3[eq3 > 0].size
        holdcount = eq3[eq3 == 0].size - 1
        totalcount = eq3.size - 1
        avgloss = np.average(eq3[eq3 < 0]) if len(eq3[eq3 < 0]) > 0 else 0
        avggain = np.average(eq3[eq3 > 0]) if len(eq3[eq3 > 0]) > 0 else 0

        self.mListMonthNetValue = list(eq4)  # 月收益净值
        self.mListMonthYield = list(eq3)  # 月收益率

        self.mTotalCount = totalcount  # 总交易月数
        self.mGainCount = gaincount  # 盈利月数
        self.mLossCount = losscount  # 亏损月数
        self.mHoldCount = holdcount  # 持平月数
        self.mMaxContGainCount = maxContGainMonthCount  # 最大连续盈利月数
        self.mMaxContLossCount = maxContLossMonthCount  # 最大连续亏损月数
        self.mAvgLoss = np.round(avgloss, 4)  # 平均每月亏损
        self.mAvgGain = np.round(avggain, 4)  # 平均每月盈利

    def __countYearPerfermence(self):
        listYearNetValue = []
        listYearYield = []
        maxContGainCount = 0
        maxContLossCount = 0
        dfyear = pd.read_csv(self.__path + 'YearEquity.csv', header=None, index_col=0,
                             names=['captical'])
        eq = np.array(dfyear['captical'])

        eq2 = np.zeros(len(eq))
        eq2[0] = eq[0]
        eq2[1:] = eq[0:len(eq) - 1]
        eqYield = (eq - eq2) / eq2
        eqNetValue = eq
        losscount = 0
        gaincount = 0
        holdcount = 0
        for item in eqYield:
            if item > 0:
                losscount = 0
                gaincount += 1
                maxContGainCount = gaincount if gaincount > maxContGainCount else maxContGainCount

            elif item < 0:
                gaincount = 0
                losscount += 1
                maxContLossCount = losscount if losscount > maxContLossCount else maxContLossCount
            else:
                gaincount = 0
                gaincount = 0
        losscount = eqYield[eqYield < 0].size
        gaincount = eqYield[eqYield > 0].size
        holdcount = eqYield[eqYield == 0].size - 1
        totalcount = eqYield.size - 1
        avgloss = np.average(eqYield[eqYield < 0]) if len(eqYield[eqYield < 0]) > 0 else 0
        avggain = np.average(eqYield[eqYield > 0]) if len(eqYield[eqYield > 0]) > 0 else 0

        self.yListYearNetValue = list(eqNetValue)  # 年收益净值
        self.yListYearYield = list(eqYield)  # 年收益率
        self.yTotalCount = totalcount  # 交易年数
        self.yGainCount = gaincount  # 盈利年数
        self.yLossCount = losscount  # 亏损年数
        self.yHoldCount = holdcount  # 持平年数
        self.yMAxContGainCount = maxContGainCount  # 最大连续盈利年数
        self.yMaxContLossCount = maxContLossCount  # 最大连续亏损年数
        self.yAvgLoss = np.round(avgloss, 4)  # 平均每年可亏损
        self.yAvgGain = np.round(avggain, 4)  # 平均每年盈

    def __read_from_mq(self, data):
        """netMQ"""
        # _stra = Strategy()  # 为了下面的提示信息创建
        # _stra = stra
        # pip install pyzmq即可安装
        context = zmq.Context()
        socket = context.socket(zmq.REQ)  # REQ模式,即REQ-RSP  CS结构
        # socket.connect('tcp://localhost:8888')	# 连接本地测试
        socket.connect('tcp://58.247.171.146:5055')  # 实际netMQ数据服务器地址
        bars = []

        # 请求数据格式
        req = ReqPackage()
        req.Type = 0  # BarType.Min
        req.Instrument = data.Instrument
        req.Begin = data.BeginDate
        req.End = data.EndDate
        # __dict__返回diction格式,即{key,value}格式
        p = req.__dict__
        socket.send_json(p)  # 直接发送__dict__转换的{}即可,不需要再转换成str

        # msg = socket.recv_unicode()	# 服务器此处查询出现异常, 排除中->C# 正常
        # 用recv接收,但是默认的socket中并没有此提示函数(可能是向下兼容的函数),不知能否转换为其他格式
        bs = socket.recv()  # 此处得到的是bytes

        # gzip解压:decompress(bytes)解压,会得到解压后的bytes,再用decode转成string
        gzipper = gzip.decompress(bs).decode()  # decode转换为string

        # json解析:与dumps对应,将str转换为{}
        bs = json.loads(gzipper)  # json解析
        for bar in bs:
            bar['Instrument'] = data.Instrument
            bars.append(bar)

        bars.sort(key=lambda bar: bar['_id'])  # 按时间升序
        return bars

    def __get_product_zmq(self):
        """从zmq读取合约信息"""
        context = zmq.Context()
        socket = context.socket(zmq.REQ)  # REQ模式,即REQ-RSP  CS结构
        socket.connect('tcp://58.247.171.146:5055')  # 实际netMQ数据服务器地址

        socket.send_json({"Type": 4})  # 直接发送__dict__转换的{}即可,不需要再转换成str

        # msg = socket.recv_unicode()    # 服务器此处查询出现异常, 排除中->C# 正常
        # 用recv接收,但是默认的socket中并没有此提示函数(可能是向下兼容的函数),不知能否转换为其他格式
        bs = socket.recv()  # 此处得到的是bytes

        # gzip解压:decompress(bytes)解压,会得到解压后的bytes,再用decode转成string
        str_json = gzip.decompress(bs).decode()  # decode转换为string
        return json.loads(str_json)

    def __countFromTradeRecord(self, stra):
        tradeRecords = stra.Orders

        dictpos = {}
        listoneorder = []
        totalfee = 0

        listContract = []
        listFee = []

        totalCount = 0  # 交易次数
        gainCount = 0  # 盈利次数
        lossCount = 0  # 亏损次数
        holdCount = 0  # 持平次数
        gainAmount = 0  # 盈利总额
        lossAmount = 0  # 亏损总额
        avgGain = 0  # 平均盈利
        avgLoss = 0  # 平均亏损
        maxGain = .0  # 最大盈利
        maxLoss = .0  # 最大亏损

        pyield = .0
        profit = .0
        totalProfit = .0

        listSingleProfit = []  # 单笔净值列表
        listAccumuProfit = []  # 单笔收益率列表

        contiGainCount = 0  # 连续盈利次数
        contiLossCount = 0  # 连续亏损次数
        contiGainAmount = 0  # 连续盈利金额
        contiLossAmount = 0  # 连续亏损金额

        maxContiGainCount = 0  # 最大连续盈利次数
        maxContiLossCount = 0  # 最大连续亏损次数
        maxContiGainAmount = .0  # 最大连续盈利金额
        maxContiLossAmount = .0  # 最大连续亏损金额

        ftrade = open(self.__path+'/trade.csv', 'w')
        str2 = ''
        for trade in tradeRecords:
            dire = 'buy' if trade.Direction == DirectType.Buy else 'sell'
            off = 'open' if trade.Offset == OffsetType.Open else 'close'

            ftrade.write('%s,%s,%s,%.2f,%d,%s\n' % (trade.Instrument, dire, off, trade.Price, trade.Volume, trade.DateTime))
        ftrade.flush()
        ftrade.close()
        # 获取每笔利润
        for trade in tradeRecords:
            # print(trade.Instrument,trade.Direction,trade.Offset,trade.Price,trade.Volume,trade.DateTime)
            # listFee = queryFeeFromSymbol(trade[1])
            # contract = queryContractFromSymbol(trade[1])

            fee = 0
            if trade.Offset == OffsetType.Open:
                if (trade.Instrument, trade.Direction) in dictpos:
                    dictpos[(trade.Instrument, trade.Direction)].append([trade.Volume, trade.Price, trade.DateTime])
                else:
                    dictpos[(trade.Instrument, trade.Direction)] = [[trade.Volume, trade.Price, trade.DateTime]]
            else:
                pos = []
                profit = 0
                # totalCount += 1
                volume = trade.Volume

                # 计算手续费
                # openfee = float(listFee['OpenFee']) * float(trade[5]) * float(contract['Multiplier']) * f(
                #     trade[4]) / 10000 if listFee['FeeType'] == 'percent' else  float(
                #     listFee['OpenFee']) * f(trade[4])
                # closefee = float(listFee['CloseTodayFee']) * float(trade[5]) * float(
                #     contract['Multiplier']) * f(
                #     trade[4]) / 10000.0 if listFee['FeeType'] == 'percent' else   float(
                #     listFee['CloseTodayFee']) * f(trade[4])
                # totalfee += closefee + openfee
                if trade.Direction == DirectType.Buy:

                    pos = dictpos[(trade.Instrument, DirectType.Sell)]
                    for p in pos:
                        # for i in range(len(pos)):
                        if p[0] == volume:
                            # profit = (p[1] - float(trade.Price)) * volume * self.__DictInstrument[trade.Instrument] - closefee - openfee
                            profit += (p[1] - trade.Price) * volume * self.__DictInstrument[trade.Instrument]['VolumeTuple']
                            # pyield = profit / p[1]
                            pos.remove(p)
                            break
                        elif p[0] > volume:
                            # profit = (p[1] - float(.Price)) * volume * self.__DictInstrument[trade.Instrument] - closefee - openfee
                            profit += (p[1] - trade.Price) * volume * self.__DictInstrument[trade.Instrument]['VolumeTuple']
                            # pyield = profit / p[1]
                            p[0] -= volume
                            break
                        else:
                            # profit += (p[1] - trade.Price * p[0] * self.__DictInstrument[trade.Instrument]  - closefee - openfee
                            profit += (p[1] - trade.Price) * p[0] * self.__DictInstrument[trade.Instrument]['VolumeTuple']
                            # pyield = profit / p[1]
                            volume -= p[0]
                            pos.remove(p)

                else:
                    pos = dictpos[trade.Instrument, DirectType.Buy]
                    for p in pos:
                        # for i in range(len(pos)):
                        if p[0] == volume:
                            # profit += (trade.Price - p[1]) * volume * self.__DictInstrument[trade.Instrument] - closefee - openfee
                            profit += (trade.Price - p[1]) * volume * self.__DictInstrument[trade.Instrument]['VolumeTuple']
                            # pyield = profit / p[1]
                            pos.remove(p)
                            break
                        elif p[0] > volume:
                            profit += (trade.Price - p[1]) * volume * self.__DictInstrument[trade.Instrument]['VolumeTuple']
                            # pyield = profit / p[1]
                            p[0] -= volume
                            break
                        else:
                            # profit += (float(trade[5]) - p[1]) * p[0] * self.__DictInstrument[trade.Instrument]  - closefee - openfee
                            profit += (trade.Price - p[1]) * p[0] * self.__DictInstrument[trade.Instrument]['VolumeTuple']
                            # pyield = profit / p[1]
                            volume -= p[0]
                            pos.remove(p)

                # netValue = netValue + pyield
                listSingleProfit.append(profit)
                # listSingleYield.append(pyield)

                if profit > 0:
                    contiGainCount = (contiGainCount + 1) if contiGainCount > 0 else 1
                    contiGainAmount = contiGainAmount + profit if contiGainAmount > 0 else profit
                    contiLossCount = 0
                    contiLossAmount = 0
                    if contiGainCount > maxContiGainCount:
                        maxContiGainCount = contiGainCount
                    if contiGainAmount > maxContiGainAmount:
                        maxContiGainAmount = contiGainAmount
                elif profit == 0:
                    contiLossCount = 0
                    contiLossSum = 0
                    contiGainCount = 0
                    contiGainSum = 0
                else:
                    contiLossCount = (contiLossCount + 1) if contiLossCount > 0 else 1
                    contiLossAmount = contiLossAmount + profit if contiLossAmount < 0 else profit
                    contiGainCount = 0
                    contiGainSum = 0
                    if contiLossCount > maxContiLossCount:
                        maxContiLossCount = contiLossCount
                    if contiLossAmount < maxContiLossAmount:
                        maxContiLossAmount = contiLossAmount
        # winRate = gainCount / (gainCount + lossCount) if gainCount + lossCount > 0 else float('inf')
        # gainSum=np.sum(listSingleYield[listSingleYield>0])
        # lossSum=np.sum(listSingleYield[listSingleYield<0])

        arraySingleProfit = np.array(listSingleProfit)
        avgGain = np.average(arraySingleProfit[arraySingleProfit > 0]) if len(arraySingleProfit[arraySingleProfit > 0]) > 0 else 0
        avgLoss = np.average(arraySingleProfit[arraySingleProfit < 0]) if len(arraySingleProfit[arraySingleProfit < 0]) > 0 else 0
        totalCount = arraySingleProfit.size

        gainAmount = np.sum(arraySingleProfit[arraySingleProfit > 0]) if len(arraySingleProfit[arraySingleProfit > 0]) > 0 else 0
        lossAmount = np.sum(arraySingleProfit[arraySingleProfit < 0]) if len(arraySingleProfit[arraySingleProfit < 0]) > 0 else 0

        maxGain = np.max(arraySingleProfit[arraySingleProfit > 0]) if len(arraySingleProfit[arraySingleProfit > 0]) > 0 else 0
        maxLoss = np.min(arraySingleProfit[arraySingleProfit < 0]) if len(arraySingleProfit[arraySingleProfit < 0]) > 0 else 0

        lossCount = np.sum(arraySingleProfit < 0) if len(arraySingleProfit[arraySingleProfit < 0]) > 0 else 0
        holdCount = np.sum(arraySingleProfit == 0) if len(arraySingleProfit[arraySingleProfit == 0]) > 0 else 0
        gainCount = np.sum(arraySingleProfit > 0) if len(arraySingleProfit[arraySingleProfit > 0]) > 0 else 0

        winRate = gainCount / (totalCount) if totalCount > 0 else 0
        plRatio = -avgGain / avgLoss if avgLoss != 0 else 0

        arrAccup = np.array(listSingleProfit)
        listAccumuProfit = list(arrAccup.cumsum())
        # 按笔计算
        self.listAccumuProfit = listAccumuProfit  # 单笔收益率列表
        self.tListSingleProfit = listSingleProfit  # 单笔利润列表
        self.tTotalCount = totalCount  # 交易次数
        self.tGainCount = gainCount  # 盈利次数
        self.tLossCount = lossCount  # 亏损次数
        self.tHoldCount = holdCount  # 持平次数
        self.tGainAmount = gainAmount  # 总盈利
        self.tLossAmount = lossAmount  # 总亏损
        self.tProfitFactor = np.round(-gainAmount/lossAmount if lossAmount != 0 else 0, 4)  # 盈利因子
        self.tTotalNetProfit = gainAmount+lossAmount  # 净利润
        self.tWinRate = np.round(winRate, 4)  # 每笔交易胜率
        self.tAvgGain = np.round(avgGain, 4)  # 平均每笔盈利
        self.tAvgLoss = np.round(avgLoss, 4)  # 平均每笔亏损
        self.tAvgGLRate = np.round(plRatio, 4)  # 平均盈亏比
        self.tMaxGain = maxGain  # 最大盈利
        self.tMaxLoss = maxLoss  # 最大亏损
        self.tMaxGainRatio = np.round(maxGain/gainAmount if gainAmount != 0 else 0, 4)  # 最大盈利/总盈利
        self.tMaxLossRatio = np.round(maxLoss/lossAmount if lossAmount != 0 else 0, 4)  # 最大亏损/总亏损
        self.tMaxContGainCount = maxContiGainCount  # 最大连续盈利次数
        self.tMaxContLossCount = maxContiLossCount  # 最大连续亏损次数
        self.tMaxContGainAmount = maxContiGainAmount  # 最大连续盈利金额
        self.tMaxContLossAmount = maxContiLossAmount  # 最大连续亏损金额

    def __showSignalPoint(self):
        dfSignal = pd.read_csv(self.__path + 'MinEquity.csv')
        dfSignal.columns = ['dt', 'equity', 'open', 'high', 'low', 'close', 'volume', 'openInt', 'dire', 'sprice', 'svolume']
        temcolum = np.arange(dfSignal.index.size)
        dfSignal['num'] = temcolum

        longsignal = dfSignal[dfSignal.loc[:, 'dire'] > 0]
        longx = longsignal['num']
        longy = longsignal.loc[:, 'sprice']

        shortsignal = dfSignal[dfSignal.loc[:, 'dire'] < 0]
        shortx = shortsignal['num']
        shorty = shortsignal.loc[:, 'sprice']
        #
        fig1 = plt.figure('signal draw')
        ax1 = plt.subplot(111)

        # plt.xaxis_date()
        plt.xticks(rotation=45)
        mf.candlestick2_ohlc(plt.axes(), dfSignal.loc[:, 'open'], dfSignal.loc[:, 'high'], dfSignal.loc[:, 'low'],
                             dfSignal.loc[:, 'close'], width=0.75, colorup=u'r', colordown=u'g', alpha=1)
        for i in range(dfSignal.shape[1] - 12):

            plt.plot(dfSignal.index, dfSignal.iloc[:, i + 9], '.-', label=dfSignal.columns[i+9])
        plt.scatter(longx, longy, s=160, c='m', marker='^', label='long')

        plt.scatter(shortx, shorty, s=160, c='k', marker='v', label='short')
        ax2 = ax1.twinx()
        ax2.plot(dfSignal.loc[:, 'equity'], c='r')

        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.savefig(self.__path + 'Signal.png')

        plt.show()
        fig1.clear()
        plt.close()

    def __plotf(self, isshow=False):

        fig1 = plt.figure('日级别动态权益图')
        plt.subplot(311)
        plt.ylabel('Equity')
        plt.title('Equity of Day')

        plt.plot(list(self.dListDayNetValue), color='red')
        plt.subplot(312)
        plt.ylabel('DropDownRate')
        plt.bar(range(len(self.bListRddrate)), self.bListRddrate, width=0.5, color='red')
        plt.subplot(313)
        plt.ylabel('Absolute Each Day Profit')
        # plt.hist(self.dListDayYield, bins=30)
        plt.bar(np.arange(len(self.dListDayYield)), self.dListDayYield)
        plt.savefig(self.__path + 'Day.png')
        # fig2 = plt.figure('周级别动态权益图')
        # plt.subplot(311)
        # plt.ylabel('NetValue')
        # plt.plot(list(self.wListWeekNetValue))
        # plt.subplot(312)
        # plt.ylabel('Yield')
        # plt.bar(np.arange(len(self.wListWeekYield)), self.wListWeekYield)
        # plt.subplot(313)
        # plt.ylabel('Yield static')
        # plt.hist(self.wListWeekYield)

        # plt.savefig(self.__path + 'Week.png')
        # fig3 = plt.figure('NetValue For Each Month')
        # plt.subplot(311)
        # plt.ylabel('NetValue')
        # plt.plot(list(self.mListMonthNetValue))
        # plt.subplot(312)
        # plt.ylabel('NetValue')
        # plt.bar(np.arange(len(self.mListMonthYield)), self.mListMonthYield)
        # plt.subplot(313)
        # plt.ylabel('DayNum')
        # plt.hist(self.mListMonthYield)

        # plt.savefig(self.__path + 'Month.png')
        # fig4 = plt.figure('NetValue for Each Year')
        # plt.subplot(311)
        # plt.ylabel('NetValue')
        # plt.plot(list(self.yListYearNetValue))
        # plt.subplot(312)
        # plt.ylabel('Yield')
        # plt.bar(np.arange(len(self.yListYearYield)), self.yListYearYield)
        # plt.subplot(313)
        # plt.ylabel('YearNum')
        # plt.hist(self.yListYearYield)

        fig4 = plt.figure('单笔收益图')
        plt.subplot(311)
        plt.plot(self.listAccumuProfit)
        plt.subplot(312)
        plt.bar(np.arange(len(self.tListSingleProfit)), self.tListSingleProfit)
        plt.subplot(313)
        plt.hist(self.tListSingleProfit)

        plt.show()

        fig1.clear()
        # fig2.clear()
        # fig3.clear()
        fig4.clear()
        plt.close()

    def __printf(self):

        print('显示回测结果：')
        print('###################################################################################################')
        print('###################################################################################################')
        print('###################################################################################################')

        print('一、按Bar计算')
        print('初始资金:%.4f' % (self.bInitFund))
        print('最大回撤比率:%.4f' % (self.bMddRate))   # 最大回撤比率
        print('最大回撤区间:%s' % (self.dDropDownPeriod))  # 最大回撤区间
        print('二、按交易笔数计算')
        print('净利润:%.4f' % (self.tTotalNetProfit))
        print('交易次数:%.4f' % (self.tTotalCount))
        print('盈利次数:%.4f' % (self.tGainCount))
        print('亏损次数:%.4f' % (self.tLossCount))
        print('持平次数:%.4f' % (self.tHoldCount))
        print('总盈利:%.4f' % (self.tGainAmount))
        print('总亏损:%.4f' % (self.tLossAmount))
        print('盈利因子:%.4f' % (self.tProfitFactor))
        print('胜率:%.4f' % (self.tWinRate))
        print('平均盈利:%.4f' % (self.tAvgGain))
        print('平均亏损:%.4f' % (self.tAvgLoss))
        print('平均盈亏比:%.4f' % (self.tAvgGLRate))
        print('最大盈利:%.4f' % (self.tMaxGain))
        print('最大亏损:%.4f' % (self.tMaxLoss))
        print('最大盈利占比:%.4f' % (self.tMaxGainRatio))
        print('最大亏损占比:%.4f' % (self.tMaxLossRatio))
        print('最大连续盈利次数:%.4f' % (self.tMaxContGainCount))
        print('最大连续亏损次数:%.4f' % (self.tMaxContLossCount))
        print('最大连续盈利金额:%.4f' % (self.tMaxContGainAmount))
        print('最大连续亏损金额:%.4f' % (self.tMaxContLossAmount))
        print('###################################################################################################')

        print('三、按日计算')
        print('总交易天数:%.4f' % self.dTotalCount)   # 总交易天数
        print('盈利天数:%.4f' % self.dGainCount)   # 盈利天数
        print('亏损天数:%.4f' % self.dLossCount)  # 亏损天数
        print('持平天数:%.4f' % self.dHoldCount)  # 持平天数
        print('胜率:%.4f' % self.dWinRate)   # 胜率
        print('平均日收益:%.4f' % self.dAvgYield)  # 平均日收益
        print('平均每天亏损:%.4f' % self.dAvgLoss)  # 平均每天亏损
        print('平均每天盈利:%.4f' % self.dAvgGain)  # 平均每天盈利
        print('日均盈亏比比率:%.4f' % self.dAvgGLRate)   # 日均盈亏比比率
        print('最大连续盈利天数:%.4f' % self.dMaxContGainCount)   # 最大连续盈利天数
        print('最大连续亏损天数:%.4f' % self.dMaxContLossCount)   # 最大连续亏损天数
        print('最大净值不创新高天数:%d' % self.dNoNewHighDays)  # 净值不创新高天数
        print('最大净值不创新高区间:%s' % self.dNoNewHighPeriod)  # 净值不创新高区间
        print('总收益率:%.4f' % self.dTotalyield)  # 总收益率
        print('年化收益率:%.4f' % self.dYearYield)  # 年化收益率
        print('波动率:%.4f' % self.dVolatility)  # 波动率
        print('夏普比率:%.4f' % self.dSharpRitio)  # 夏普比率
        print('MAR比率:%.4f' % self.dMarRate)  # MAR比率
        print('###################################################################################################')
        print('四、按周计算')

        print('总交易周数:%.4f' % self.wTotalCount)   # 总交易周数
        print('盈利周数:%.4f' % self.wGainCount)   # 盈利周数
        print('亏损周数:%.4f' % self.wLossCount)  # 亏损周数
        print('持平周数:%.4f' % self.wHoldCount)  # 持平周数
        print('周胜率:%.4f' % self.wWinRate)  # 周胜率
        print('平均每周亏损:%.4f' % self.wAvgLoss)  # 平均每周亏损
        print('平均每周盈利:%.4f' % self.wwvgGain)   # 平均每周盈利
        print('最大连续盈利周数:%.4f' % self.wMaxContGainCount)  # 最大连续盈利周数
        print('最大连续亏损周数:%.4f' % self.wMaxContLossCount)  # 最大连续亏损周数
        print('###################################################################################################')
        print('五、按月计算')

        print('总交易月数:%.4f' % self.mTotalCount)   # 总交易月数
        print('盈利月数:%.4f' % self.mGainCount)   # 盈利月数
        print('亏损月数:%.4f' % self.mLossCount)  # 亏损月数
        print('持平月数:%.4f' % self.mHoldCount)   # 持平月数
        print('最大连续盈利月数:%.4f' % self.mMaxContGainCount)   # 最大连续盈利月数
        print('最大连续亏损月数:%.4f' % self.mMaxContLossCount)  # 最大连续亏损月数
        print('平均每月亏损:%.4f' % self.mAvgLoss)   # 平均每月亏损
        print('平均每月盈利:%.4f' % self.mAvgGain)   # 平均每月盈利
        print('###################################################################################################')
        print('六、按年统计')

        print('总交易年数:%.4f' % self.yTotalCount)  # 总交易月数
        print('盈利年数:%.4f' % self.yGainCount)  # 盈利月数
        print('亏损年数:%.4f' % self.yLossCount)  # 亏损月数
        print('持平年数:%.4f' % self.yHoldCount)  # 持平月数
        print('最大连续盈利年数:%.4f' % self.yMAxContGainCount)  # 最大连续盈利月数
        print('最大连续亏损年数:%.4f' % self.yMaxContLossCount)  # 最大连续亏损月数
        print('平均每年亏损:%.4f' % self.yAvgLoss)  # 平均每月亏损
        print('平均每年盈利:%.4f' % self.yAvgGain)  # 平均每月盈利

        print('###################################################################################################')
        print('###################################################################################################')
        print('###################################################################################################')

    def __GetDataAndBars(self):
        """处理数据"""
        stra = copy.copy(self.__stra)
        self.__stra = 0
        orders = stra.Orders
        # orders = [{"Direction": 0, "DateTime": "20161019 14:00:00", "Price": 2300},
        # #         {"Direction":1,"DateTime":"20161019 09:00:00","Price":2400}]
        orders_json = []
        for i in range(0, len(orders)):
            # 遇到diction=Diction.Buy转换后:diction:<Diction.Buy:1> 后面报错
            # orders_str.append(ord.__dict__)
            ord = orders[i]
            d = datetime.datetime.strptime(ord.DateTime, '%Y%m%d %H:%M:%S').strftime('%Y/%m/%d %H:%M:%S')
            orders_json.append([d, (0 if ord.Direction == DirectType.Buy else 1), (0 if ord.Offset == OffsetType.Open else 1), ord.Price, ord.Volume])

        it = 'year'
        for case in switch(stra.IntervalType):
            if case(IntervalType.Minute):
                it = 'min'
                break
            if case(IntervalType.Hour):
                it = 'hour'
                break
            if case(IntervalType.Day):
                it = 'day'
                break
            if case(IntervalType.Month):
                it = 'month'
                break

        data_req = {
            'id': stra.ID,
            'instrument': stra.Instrument,
            'begin': stra.BeginDate,
            # 'end': str a.EndDate,
            'interval': stra.Interval,
            'intervalType': str(stra.IntervalType),
            'params': str(stra.Params),
        }

        indexes_json = []
        # for key, values in stra.IndexDict.items():
        #     array = []
        #     for value in values:
        #         array.append(value)
        #     indexes_json.append({'name': key, 'array': array})

        bars_json = []
        for bar in stra.Bars:
            d = datetime.datetime.strptime(bar.D, '%Y%m%d %H:%M:%S').strftime('%Y/%m/%d %H:%M:%S')
            bars_json.append([d, bar.O, bar.C, bar.L, bar.H])

        report_json = {
            'bInitFund': self.bInitFund,
            'bMddRate': self.bMddRate,   # 最大回撤比率
            'dDropDownPeriod': self.dDropDownPeriod,  # 最大回撤区间
            'listAccumuProfit': self.listAccumuProfit,
            'tTotalNetProfit': self.tTotalNetProfit,
            'tTotalCount': self.tTotalCount,
            'tGainCount': self.tGainCount,
            'tLossCount': self.tLossCount,
            'tHoldCount': self.tHoldCount,
            'tGainAmount': self.tGainAmount,
            'tLossAmount': self.tLossAmount,
            'tProfitFactor': self.tProfitFactor,
            'tWinRate': self.tWinRate,
            'tAvgGain': self.tAvgGain,
            'tAvgLoss': self.tAvgLoss,
            'tAvgGLRate': self.tAvgGLRate,
            'tMaxGain': self.tMaxGain,
            'tMaxLoss': self.tMaxLoss,
            'tMaxGainRatio': self.tMaxGainRatio,
            'tMaxLossRatio': self.tMaxLossRatio,
            'tMaxContGainCount': self.tMaxContGainCount,
            'tMaxContLossCount': self.tMaxContLossCount,
            'tMaxContGainAmount': self.tMaxContGainAmount,
            'tMaxContLossAmount': self.tMaxContLossAmount,
            'dListDayYield': self.dListDayYield,
            'dTotalCount': self.dTotalCount,  # 总交易天数
            'dGainCount': self.dGainCount,  # 盈利天数
            'dLossCount': self.dLossCount,  # 亏损天数
            'dHoldCount': self.dHoldCount,  # 持平天数
            'dWinRate': self.dWinRate,  # 胜率
            'dAvgYield': self.dAvgYield,  # 平均日收益
            'dAvgLoss': self.dAvgLoss,  # 平均每天亏损
            'dAvgGain': self.dAvgGain,  # 平均每天盈利
            'dAvgGLRate': self.dAvgGLRate,  # 日均盈亏比比率
            'dMaxContGainCount': self.dMaxContGainCount,  # 最大连续盈利天数
            'dMaxContLossCount': self.dMaxContLossCount,  # 最大连续亏损天数
            'dNoNewHighDays': self.dNoNewHighDays,  # 净值不创新高天数
            'dNoNewHighPeriod': self.dNoNewHighPeriod,  # 净值不创新高区间
            'dTotalyield': self.dTotalyield,  # 总收益率
            'dYearYield': self.dYearYield,  # 年化收益率
            'dVolatility': self.dVolatility,  # 波动率
            'dSharpRitio': self.dSharpRitio,  # 夏普比率
            'dMarRate': self.dMarRate,  # MAR比率


            'wTotalCount': self.wTotalCount,  # 总交易周数
            'wGainCount': self.wGainCount,  # 盈利周数
            'wLossCount': self.wLossCount,  # 亏损周数
            'wHoldCount': self.wHoldCount,  # 持平周数
            'wWinRate': self.wWinRate,  # 周胜率
            'wAvgLoss': self.wAvgLoss,  # 平均每周亏损
            'wwvgGain': self.wwvgGain,  # 平均每周盈利
            'wMaxContGainCount': self.wMaxContGainCount,  # 最大连续盈利周数
            'wMaxContLossCount': self.wMaxContLossCount,  # 最大连续亏损周数

            'mTotalCount': self.mTotalCount,  # 总交易月数
            'mGainCount': self.mGainCount,  # 盈利月数
            'mLossCount': self.mLossCount,  # 亏损月数
            'mHoldCount': self.mHoldCount,  # 持平月数
            'mMaxContGainCount': self.mMaxContGainCount,  # 最大连续盈利月数
            'mMaxContLossCount': self.mMaxContLossCount,  # 最大连续亏损月数
            'mAvgLoss': self.mAvgLoss,  # 平均每月亏损
            'mAvgGain': self.mAvgGain,  # 平均每月盈利


            'yTotalCount': self.yTotalCount,  # 总交易月数
            'yGainCount': self.yGainCount,  # 盈利月数
            'yLossCount': self.yLossCount,  # 亏损月数
            'yHoldCount': self.yHoldCount,  # 持平月数
            'yMAxContGainCount': self.yMAxContGainCount,  # 最大连续盈利月数
            'yMaxContLossCount': self.yMaxContLossCount,  # 最大连续亏损月数
            'mAvgLoss': self.mAvgLoss,  # 平均每月亏损
            'mAvgGain': self.mAvgGain,

            'yTotalCount': self.yTotalCount,  # 总交易月数
            'yGainCount': self.yGainCount,  # 盈利月数
            'yLossCount': self.yLossCount,  # 亏损月数
            'yHoldCount': self.yHoldCount,  # 持平月数
            'yMAxContGainCount': self.yMAxContGainCount,  # 最大连续盈利月数
            'yMaxContLossCount': self.yMaxContLossCount,  # 最大连续亏损月数
            'yAvgLoss': self.yAvgLoss,  # 平均每月亏损
            'yAvgGain': self.yAvgGain,  # 平
            'dayEquity': self.dayEquity,
        }
        # report_json.pop('_Statistics_stra')

        # data_req = json.dumps(data_req)
        # orders_json = json.dumps(orders_json)
        # indexes_json = json.dumps(indexes_json)
        # report_json = json.dumps(report_json, ensure_ascii=False)

        data = {'orders': orders_json, 'indexes': indexes_json, 'report': report_json, 'req': data_req}
        return data, bars_json

    def __ShowWeb(self):
        '''输出网页'''
        data, bars_json = self.__GetDataAndBars()

        print('#################################################################################################')

        # data = json.dumps(data)
        # bars_json = json.dumps(bars_json)
        from py_at.report import show
        show(data, bars_json)


if __name__ == '__main__':
    stat = Statistics(None)
