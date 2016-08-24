#!/usr/bin/env python
#coding:utf-8
from ctypes import *
from ctp_enum import *

class CThostFtdcDisseminationField(Structure):
	"""信息分发"""
	_fields_ = [
		#序列系列号
		("SequenceSeries",c_int32),
		#序列号
		("SequenceNo",c_int32),
		]

	def getSequenceSeries(self):
		return self.SequenceSeries
	def getSequenceNo(self):
		return self.SequenceNo

class CThostFtdcReqUserLoginField(Structure):
	"""用户登录请求"""
	_fields_ = [
		#交易日
		("TradingDay",c_char*9),
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#密码
		("Password",c_char*41),
		#用户端产品信息
		("UserProductInfo",c_char*11),
		#接口端产品信息
		("InterfaceProductInfo",c_char*11),
		#协议信息
		("ProtocolInfo",c_char*11),
		#Mac地址
		("MacAddress",c_char*21),
		#动态密码
		("OneTimePassword",c_char*41),
		#终端IP地址
		("ClientIPAddress",c_char*16),
		]

	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getPassword(self):
		return self.Password.decode('ascii')
	def getUserProductInfo(self):
		return self.UserProductInfo.decode('ascii')
	def getInterfaceProductInfo(self):
		return self.InterfaceProductInfo.decode('ascii')
	def getProtocolInfo(self):
		return self.ProtocolInfo.decode('ascii')
	def getMacAddress(self):
		return self.MacAddress.decode('ascii')
	def getOneTimePassword(self):
		return self.OneTimePassword.decode('ascii')
	def getClientIPAddress(self):
		return self.ClientIPAddress.decode('ascii')

class CThostFtdcRspUserLoginField(Structure):
	"""用户登录应答"""
	_fields_ = [
		#交易日
		("TradingDay",c_char*9),
		#登录成功时间
		("LoginTime",c_char*9),
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#交易系统名称
		("SystemName",c_char*41),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#最大报单引用
		("MaxOrderRef",c_char*13),
		#上期所时间
		("SHFETime",c_char*9),
		#大商所时间
		("DCETime",c_char*9),
		#郑商所时间
		("CZCETime",c_char*9),
		#中金所时间
		("FFEXTime",c_char*9),
		#能源中心时间
		("INETime",c_char*9),
		]

	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getLoginTime(self):
		return self.LoginTime.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getSystemName(self):
		return self.SystemName.decode('ascii')
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getMaxOrderRef(self):
		return self.MaxOrderRef.decode('ascii')
	def getSHFETime(self):
		return self.SHFETime.decode('ascii')
	def getDCETime(self):
		return self.DCETime.decode('ascii')
	def getCZCETime(self):
		return self.CZCETime.decode('ascii')
	def getFFEXTime(self):
		return self.FFEXTime.decode('ascii')
	def getINETime(self):
		return self.INETime.decode('ascii')

class CThostFtdcUserLogoutField(Structure):
	"""用户登出请求"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')

class CThostFtdcForceUserLogoutField(Structure):
	"""强制交易员退出"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')

class CThostFtdcReqAuthenticateField(Structure):
	"""客户端认证请求"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#用户端产品信息
		("UserProductInfo",c_char*11),
		#认证码
		("AuthCode",c_char*17),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getUserProductInfo(self):
		return self.UserProductInfo.decode('ascii')
	def getAuthCode(self):
		return self.AuthCode.decode('ascii')

class CThostFtdcRspAuthenticateField(Structure):
	"""客户端认证响应"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#用户端产品信息
		("UserProductInfo",c_char*11),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getUserProductInfo(self):
		return self.UserProductInfo.decode('ascii')

class CThostFtdcAuthenticationInfoField(Structure):
	"""客户端认证信息"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#用户端产品信息
		("UserProductInfo",c_char*11),
		#认证信息
		("AuthInfo",c_char*129),
		#是否为认证结果
		("IsResult",c_int32),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getUserProductInfo(self):
		return self.UserProductInfo.decode('ascii')
	def getAuthInfo(self):
		return self.AuthInfo.decode('ascii')
	def getIsResult(self):
		return self.IsResult

class CThostFtdcTransferHeaderField(Structure):
	"""银期转帐报文头"""
	_fields_ = [
		#版本号，常量，1.0
		("Version",c_char*4),
		#交易代码，必填
		("TradeCode",c_char*7),
		#交易日期，必填，格式：yyyymmdd
		("TradeDate",c_char*9),
		#交易时间，必填，格式：hhmmss
		("TradeTime",c_char*9),
		#发起方流水号，N/A
		("TradeSerial",c_char*9),
		#期货公司代码，必填
		("FutureID",c_char*11),
		#银行代码，根据查询银行得到，必填
		("BankID",c_char*4),
		#银行分中心代码，根据查询银行得到，必填
		("BankBrchID",c_char*5),
		#操作员，N/A
		("OperNo",c_char*17),
		#交易设备类型，N/A
		("DeviceID",c_char*3),
		#记录数，N/A
		("RecordNum",c_char*7),
		#会话编号，N/A
		("SessionID",c_int32),
		#请求编号，N/A
		("RequestID",c_int32),
		]

	def getVersion(self):
		return self.Version.decode('ascii')
	def getTradeCode(self):
		return self.TradeCode.decode('ascii')
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getTradeSerial(self):
		return self.TradeSerial.decode('ascii')
	def getFutureID(self):
		return self.FutureID.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBrchID(self):
		return self.BankBrchID.decode('ascii')
	def getOperNo(self):
		return self.OperNo.decode('ascii')
	def getDeviceID(self):
		return self.DeviceID.decode('ascii')
	def getRecordNum(self):
		return self.RecordNum.decode('ascii')
	def getSessionID(self):
		return self.SessionID
	def getRequestID(self):
		return self.RequestID

class CThostFtdcTransferBankToFutureReqField(Structure):
	"""银行资金转期货请求，TradeCode=202001"""
	_fields_ = [
		#期货资金账户
		("FutureAccount",c_char*13),
		#密码标志
		("FuturePwdFlag",c_char),
		#密码
		("FutureAccPwd",c_char*17),
		#转账金额
		("TradeAmt",c_double),
		#客户手续费
		("CustFee",c_double),
		#币种：RMB-人民币 USD-美圆 HKD-港元
		("CurrencyCode",c_char*4),
		]

	def getFutureAccount(self):
		return self.FutureAccount.decode('ascii')
	def getFuturePwdFlag(self):
		return FuturePwdFlagType(ord(self.FuturePwdFlag))
	def getFutureAccPwd(self):
		return self.FutureAccPwd.decode('ascii')
	def getTradeAmt(self):
		return self.TradeAmt
	def getCustFee(self):
		return self.CustFee
	def getCurrencyCode(self):
		return self.CurrencyCode.decode('ascii')

class CThostFtdcTransferBankToFutureRspField(Structure):
	"""银行资金转期货请求响应"""
	_fields_ = [
		#响应代码
		("RetCode",c_char*5),
		#响应信息
		("RetInfo",c_char*129),
		#资金账户
		("FutureAccount",c_char*13),
		#转帐金额
		("TradeAmt",c_double),
		#应收客户手续费
		("CustFee",c_double),
		#币种
		("CurrencyCode",c_char*4),
		]

	def getRetCode(self):
		return self.RetCode.decode('ascii')
	def getRetInfo(self):
		return self.RetInfo.decode('ascii')
	def getFutureAccount(self):
		return self.FutureAccount.decode('ascii')
	def getTradeAmt(self):
		return self.TradeAmt
	def getCustFee(self):
		return self.CustFee
	def getCurrencyCode(self):
		return self.CurrencyCode.decode('ascii')

class CThostFtdcTransferFutureToBankReqField(Structure):
	"""期货资金转银行请求，TradeCode=202002"""
	_fields_ = [
		#期货资金账户
		("FutureAccount",c_char*13),
		#密码标志
		("FuturePwdFlag",c_char),
		#密码
		("FutureAccPwd",c_char*17),
		#转账金额
		("TradeAmt",c_double),
		#客户手续费
		("CustFee",c_double),
		#币种：RMB-人民币 USD-美圆 HKD-港元
		("CurrencyCode",c_char*4),
		]

	def getFutureAccount(self):
		return self.FutureAccount.decode('ascii')
	def getFuturePwdFlag(self):
		return FuturePwdFlagType(ord(self.FuturePwdFlag))
	def getFutureAccPwd(self):
		return self.FutureAccPwd.decode('ascii')
	def getTradeAmt(self):
		return self.TradeAmt
	def getCustFee(self):
		return self.CustFee
	def getCurrencyCode(self):
		return self.CurrencyCode.decode('ascii')

class CThostFtdcTransferFutureToBankRspField(Structure):
	"""期货资金转银行请求响应"""
	_fields_ = [
		#响应代码
		("RetCode",c_char*5),
		#响应信息
		("RetInfo",c_char*129),
		#资金账户
		("FutureAccount",c_char*13),
		#转帐金额
		("TradeAmt",c_double),
		#应收客户手续费
		("CustFee",c_double),
		#币种
		("CurrencyCode",c_char*4),
		]

	def getRetCode(self):
		return self.RetCode.decode('ascii')
	def getRetInfo(self):
		return self.RetInfo.decode('ascii')
	def getFutureAccount(self):
		return self.FutureAccount.decode('ascii')
	def getTradeAmt(self):
		return self.TradeAmt
	def getCustFee(self):
		return self.CustFee
	def getCurrencyCode(self):
		return self.CurrencyCode.decode('ascii')

class CThostFtdcTransferQryBankReqField(Structure):
	"""查询银行资金请求，TradeCode=204002"""
	_fields_ = [
		#期货资金账户
		("FutureAccount",c_char*13),
		#密码标志
		("FuturePwdFlag",c_char),
		#密码
		("FutureAccPwd",c_char*17),
		#币种：RMB-人民币 USD-美圆 HKD-港元
		("CurrencyCode",c_char*4),
		]

	def getFutureAccount(self):
		return self.FutureAccount.decode('ascii')
	def getFuturePwdFlag(self):
		return FuturePwdFlagType(ord(self.FuturePwdFlag))
	def getFutureAccPwd(self):
		return self.FutureAccPwd.decode('ascii')
	def getCurrencyCode(self):
		return self.CurrencyCode.decode('ascii')

class CThostFtdcTransferQryBankRspField(Structure):
	"""查询银行资金请求响应"""
	_fields_ = [
		#响应代码
		("RetCode",c_char*5),
		#响应信息
		("RetInfo",c_char*129),
		#资金账户
		("FutureAccount",c_char*13),
		#银行余额
		("TradeAmt",c_double),
		#银行可用余额
		("UseAmt",c_double),
		#银行可取余额
		("FetchAmt",c_double),
		#币种
		("CurrencyCode",c_char*4),
		]

	def getRetCode(self):
		return self.RetCode.decode('ascii')
	def getRetInfo(self):
		return self.RetInfo.decode('ascii')
	def getFutureAccount(self):
		return self.FutureAccount.decode('ascii')
	def getTradeAmt(self):
		return self.TradeAmt
	def getUseAmt(self):
		return self.UseAmt
	def getFetchAmt(self):
		return self.FetchAmt
	def getCurrencyCode(self):
		return self.CurrencyCode.decode('ascii')

class CThostFtdcTransferQryDetailReqField(Structure):
	"""查询银行交易明细请求，TradeCode=204999"""
	_fields_ = [
		#期货资金账户
		("FutureAccount",c_char*13),
		]

	def getFutureAccount(self):
		return self.FutureAccount.decode('ascii')

class CThostFtdcTransferQryDetailRspField(Structure):
	"""查询银行交易明细请求响应"""
	_fields_ = [
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#交易代码
		("TradeCode",c_char*7),
		#期货流水号
		("FutureSerial",c_int32),
		#期货公司代码
		("FutureID",c_char*11),
		#资金帐号
		("FutureAccount",c_char*22),
		#银行流水号
		("BankSerial",c_int32),
		#银行代码
		("BankID",c_char*4),
		#银行分中心代码
		("BankBrchID",c_char*5),
		#银行账号
		("BankAccount",c_char*41),
		#证件号码
		("CertCode",c_char*21),
		#货币代码
		("CurrencyCode",c_char*4),
		#发生金额
		("TxAmount",c_double),
		#有效标志
		("Flag",c_char),
		]

	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getTradeCode(self):
		return self.TradeCode.decode('ascii')
	def getFutureSerial(self):
		return self.FutureSerial
	def getFutureID(self):
		return self.FutureID.decode('ascii')
	def getFutureAccount(self):
		return self.FutureAccount.decode('ascii')
	def getBankSerial(self):
		return self.BankSerial
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBrchID(self):
		return self.BankBrchID.decode('ascii')
	def getBankAccount(self):
		return self.BankAccount.decode('ascii')
	def getCertCode(self):
		return self.CertCode.decode('ascii')
	def getCurrencyCode(self):
		return self.CurrencyCode.decode('ascii')
	def getTxAmount(self):
		return self.TxAmount
	def getFlag(self):
		return TransferValidFlagType(ord(self.Flag))

class CThostFtdcRspInfoField(Structure):
	"""响应信息"""
	_fields_ = [
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return self.ErrorMsg.decode('GB2312')

class CThostFtdcExchangeField(Structure):
	"""交易所"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#交易所名称
		("ExchangeName",c_char*61),
		#交易所属性
		("ExchangeProperty",c_char),
		]

	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getExchangeName(self):
		return self.ExchangeName.decode('ascii')
	def getExchangeProperty(self):
		return ExchangePropertyType(ord(self.ExchangeProperty))

class CThostFtdcProductField(Structure):
	"""产品"""
	_fields_ = [
		#产品代码
		("ProductID",c_char*31),
		#产品名称
		("ProductName",c_char*21),
		#交易所代码
		("ExchangeID",c_char*9),
		#产品类型
		("ProductClass",c_char),
		#合约数量乘数
		("VolumeMultiple",c_int32),
		#最小变动价位
		("PriceTick",c_double),
		#市价单最大下单量
		("MaxMarketOrderVolume",c_int32),
		#市价单最小下单量
		("MinMarketOrderVolume",c_int32),
		#限价单最大下单量
		("MaxLimitOrderVolume",c_int32),
		#限价单最小下单量
		("MinLimitOrderVolume",c_int32),
		#持仓类型
		("PositionType",c_char),
		#持仓日期类型
		("PositionDateType",c_char),
		#平仓处理类型
		("CloseDealType",c_char),
		#交易币种类型
		("TradeCurrencyID",c_char*4),
		#质押资金可用范围
		("MortgageFundUseRange",c_char),
		#交易所产品代码
		("ExchangeProductID",c_char*31),
		#合约基础商品乘数
		("UnderlyingMultiple",c_double),
		]

	def getProductID(self):
		return self.ProductID.decode('ascii')
	def getProductName(self):
		return self.ProductName.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getProductClass(self):
		return ProductClassType(ord(self.ProductClass))
	def getVolumeMultiple(self):
		return self.VolumeMultiple
	def getPriceTick(self):
		return self.PriceTick
	def getMaxMarketOrderVolume(self):
		return self.MaxMarketOrderVolume
	def getMinMarketOrderVolume(self):
		return self.MinMarketOrderVolume
	def getMaxLimitOrderVolume(self):
		return self.MaxLimitOrderVolume
	def getMinLimitOrderVolume(self):
		return self.MinLimitOrderVolume
	def getPositionType(self):
		return PositionTypeType(ord(self.PositionType))
	def getPositionDateType(self):
		return PositionDateTypeType(ord(self.PositionDateType))
	def getCloseDealType(self):
		return CloseDealTypeType(ord(self.CloseDealType))
	def getTradeCurrencyID(self):
		return self.TradeCurrencyID.decode('ascii')
	def getMortgageFundUseRange(self):
		return MortgageFundUseRangeType(ord(self.MortgageFundUseRange))
	def getExchangeProductID(self):
		return self.ExchangeProductID.decode('ascii')
	def getUnderlyingMultiple(self):
		return self.UnderlyingMultiple

class CThostFtdcInstrumentField(Structure):
	"""合约"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#合约名称
		("InstrumentName",c_char*21),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#产品代码
		("ProductID",c_char*31),
		#产品类型
		("ProductClass",c_char),
		#交割年份
		("DeliveryYear",c_int32),
		#交割月
		("DeliveryMonth",c_int32),
		#市价单最大下单量
		("MaxMarketOrderVolume",c_int32),
		#市价单最小下单量
		("MinMarketOrderVolume",c_int32),
		#限价单最大下单量
		("MaxLimitOrderVolume",c_int32),
		#限价单最小下单量
		("MinLimitOrderVolume",c_int32),
		#合约数量乘数
		("VolumeMultiple",c_int32),
		#最小变动价位
		("PriceTick",c_double),
		#创建日
		("CreateDate",c_char*9),
		#上市日
		("OpenDate",c_char*9),
		#到期日
		("ExpireDate",c_char*9),
		#开始交割日
		("StartDelivDate",c_char*9),
		#结束交割日
		("EndDelivDate",c_char*9),
		#合约生命周期状态
		("InstLifePhase",c_char),
		#当前是否交易
		("IsTrading",c_int32),
		#持仓类型
		("PositionType",c_char),
		#持仓日期类型
		("PositionDateType",c_char),
		#多头保证金率
		("LongMarginRatio",c_double),
		#空头保证金率
		("ShortMarginRatio",c_double),
		#是否使用大额单边保证金算法
		("MaxMarginSideAlgorithm",c_char),
		#基础商品代码
		("UnderlyingInstrID",c_char*31),
		#执行价
		("StrikePrice",c_double),
		#期权类型
		("OptionsType",c_char),
		#合约基础商品乘数
		("UnderlyingMultiple",c_double),
		#组合类型
		("CombinationType",c_char),
		]

	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getInstrumentName(self):
		return self.InstrumentName.decode('ascii')
	def getExchangeInstID(self):
		return self.ExchangeInstID.decode('ascii')
	def getProductID(self):
		return self.ProductID.decode('ascii')
	def getProductClass(self):
		return ProductClassType(ord(self.ProductClass))
	def getDeliveryYear(self):
		return self.DeliveryYear
	def getDeliveryMonth(self):
		return self.DeliveryMonth
	def getMaxMarketOrderVolume(self):
		return self.MaxMarketOrderVolume
	def getMinMarketOrderVolume(self):
		return self.MinMarketOrderVolume
	def getMaxLimitOrderVolume(self):
		return self.MaxLimitOrderVolume
	def getMinLimitOrderVolume(self):
		return self.MinLimitOrderVolume
	def getVolumeMultiple(self):
		return self.VolumeMultiple
	def getPriceTick(self):
		return self.PriceTick
	def getCreateDate(self):
		return self.CreateDate.decode('ascii')
	def getOpenDate(self):
		return self.OpenDate.decode('ascii')
	def getExpireDate(self):
		return self.ExpireDate.decode('ascii')
	def getStartDelivDate(self):
		return self.StartDelivDate.decode('ascii')
	def getEndDelivDate(self):
		return self.EndDelivDate.decode('ascii')
	def getInstLifePhase(self):
		return InstLifePhaseType(ord(self.InstLifePhase))
	def getIsTrading(self):
		return self.IsTrading
	def getPositionType(self):
		return PositionTypeType(ord(self.PositionType))
	def getPositionDateType(self):
		return PositionDateTypeType(ord(self.PositionDateType))
	def getLongMarginRatio(self):
		return self.LongMarginRatio
	def getShortMarginRatio(self):
		return self.ShortMarginRatio
	def getMaxMarginSideAlgorithm(self):
		return MaxMarginSideAlgorithmType(ord(self.MaxMarginSideAlgorithm))
	def getUnderlyingInstrID(self):
		return self.UnderlyingInstrID.decode('ascii')
	def getStrikePrice(self):
		return self.StrikePrice
	def getOptionsType(self):
		return OptionsTypeType(ord(self.OptionsType))
	def getUnderlyingMultiple(self):
		return self.UnderlyingMultiple
	def getCombinationType(self):
		return CombinationTypeType(ord(self.CombinationType))

class CThostFtdcBrokerField(Structure):
	"""经纪公司"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#经纪公司简称
		("BrokerAbbr",c_char*9),
		#经纪公司名称
		("BrokerName",c_char*81),
		#是否活跃
		("IsActive",c_int32),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBrokerAbbr(self):
		return self.BrokerAbbr.decode('ascii')
	def getBrokerName(self):
		return self.BrokerName.decode('ascii')
	def getIsActive(self):
		return self.IsActive

class CThostFtdcTraderField(Structure):
	"""交易所交易员"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		#会员代码
		("ParticipantID",c_char*11),
		#密码
		("Password",c_char*41),
		#安装数量
		("InstallCount",c_int32),
		#经纪公司代码
		("BrokerID",c_char*11),
		]

	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getPassword(self):
		return self.Password.decode('ascii')
	def getInstallCount(self):
		return self.InstallCount
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')

class CThostFtdcInvestorField(Structure):
	"""投资者"""
	_fields_ = [
		#投资者代码
		("InvestorID",c_char*13),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者分组代码
		("InvestorGroupID",c_char*13),
		#投资者名称
		("InvestorName",c_char*81),
		#证件类型
		("IdentifiedCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#是否活跃
		("IsActive",c_int32),
		#联系电话
		("Telephone",c_char*41),
		#通讯地址
		("Address",c_char*101),
		#开户日期
		("OpenDate",c_char*9),
		#手机
		("Mobile",c_char*41),
		#手续费率模板代码
		("CommModelID",c_char*13),
		#保证金率模板代码
		("MarginModelID",c_char*13),
		]

	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorGroupID(self):
		return self.InvestorGroupID.decode('ascii')
	def getInvestorName(self):
		return self.InvestorName.decode('ascii')
	def getIdentifiedCardType(self):
		return IdCardTypeType(ord(self.IdentifiedCardType))
	def getIdentifiedCardNo(self):
		return self.IdentifiedCardNo.decode('ascii')
	def getIsActive(self):
		return self.IsActive
	def getTelephone(self):
		return self.Telephone.decode('ascii')
	def getAddress(self):
		return self.Address.decode('ascii')
	def getOpenDate(self):
		return self.OpenDate.decode('ascii')
	def getMobile(self):
		return self.Mobile.decode('ascii')
	def getCommModelID(self):
		return self.CommModelID.decode('ascii')
	def getMarginModelID(self):
		return self.MarginModelID.decode('ascii')

class CThostFtdcTradingCodeField(Structure):
	"""交易编码"""
	_fields_ = [
		#投资者代码
		("InvestorID",c_char*13),
		#经纪公司代码
		("BrokerID",c_char*11),
		#交易所代码
		("ExchangeID",c_char*9),
		#客户代码
		("ClientID",c_char*11),
		#是否活跃
		("IsActive",c_int32),
		#交易编码类型
		("ClientIDType",c_char),
		]

	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getClientID(self):
		return self.ClientID.decode('ascii')
	def getIsActive(self):
		return self.IsActive
	def getClientIDType(self):
		return ClientIDTypeType(ord(self.ClientIDType))

class CThostFtdcPartBrokerField(Structure):
	"""会员编码和经纪公司编码对照表"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#是否活跃
		("IsActive",c_int32),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getIsActive(self):
		return self.IsActive

class CThostFtdcSuperUserField(Structure):
	"""管理用户"""
	_fields_ = [
		#用户代码
		("UserID",c_char*16),
		#用户名称
		("UserName",c_char*81),
		#密码
		("Password",c_char*41),
		#是否活跃
		("IsActive",c_int32),
		]

	def getUserID(self):
		return self.UserID.decode('ascii')
	def getUserName(self):
		return self.UserName.decode('ascii')
	def getPassword(self):
		return self.Password.decode('ascii')
	def getIsActive(self):
		return self.IsActive

class CThostFtdcSuperUserFunctionField(Structure):
	"""管理用户功能权限"""
	_fields_ = [
		#用户代码
		("UserID",c_char*16),
		#功能代码
		("FunctionCode",c_char),
		]

	def getUserID(self):
		return self.UserID.decode('ascii')
	def getFunctionCode(self):
		return FunctionCodeType(ord(self.FunctionCode))

class CThostFtdcInvestorGroupField(Structure):
	"""投资者组"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者分组代码
		("InvestorGroupID",c_char*13),
		#投资者分组名称
		("InvestorGroupName",c_char*41),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorGroupID(self):
		return self.InvestorGroupID.decode('ascii')
	def getInvestorGroupName(self):
		return self.InvestorGroupName.decode('ascii')

class CThostFtdcTradingAccountField(Structure):
	"""资金账户"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者帐号
		("AccountID",c_char*13),
		#上次质押金额
		("PreMortgage",c_double),
		#上次信用额度
		("PreCredit",c_double),
		#上次存款额
		("PreDeposit",c_double),
		#上次结算准备金
		("PreBalance",c_double),
		#上次占用的保证金
		("PreMargin",c_double),
		#利息基数
		("InterestBase",c_double),
		#利息收入
		("Interest",c_double),
		#入金金额
		("Deposit",c_double),
		#出金金额
		("Withdraw",c_double),
		#冻结的保证金
		("FrozenMargin",c_double),
		#冻结的资金
		("FrozenCash",c_double),
		#冻结的手续费
		("FrozenCommission",c_double),
		#当前保证金总额
		("CurrMargin",c_double),
		#资金差额
		("CashIn",c_double),
		#手续费
		("Commission",c_double),
		#平仓盈亏
		("CloseProfit",c_double),
		#持仓盈亏
		("PositionProfit",c_double),
		#期货结算准备金
		("Balance",c_double),
		#可用资金
		("Available",c_double),
		#可取资金
		("WithdrawQuota",c_double),
		#基本准备金
		("Reserve",c_double),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#信用额度
		("Credit",c_double),
		#质押金额
		("Mortgage",c_double),
		#交易所保证金
		("ExchangeMargin",c_double),
		#投资者交割保证金
		("DeliveryMargin",c_double),
		#交易所交割保证金
		("ExchangeDeliveryMargin",c_double),
		#保底期货结算准备金
		("ReserveBalance",c_double),
		#币种代码
		("CurrencyID",c_char*4),
		#上次货币质入金额
		("PreFundMortgageIn",c_double),
		#上次货币质出金额
		("PreFundMortgageOut",c_double),
		#货币质入金额
		("FundMortgageIn",c_double),
		#货币质出金额
		("FundMortgageOut",c_double),
		#货币质押余额
		("FundMortgageAvailable",c_double),
		#可质押货币金额
		("MortgageableFund",c_double),
		#特殊产品占用保证金
		("SpecProductMargin",c_double),
		#特殊产品冻结保证金
		("SpecProductFrozenMargin",c_double),
		#特殊产品手续费
		("SpecProductCommission",c_double),
		#特殊产品冻结手续费
		("SpecProductFrozenCommission",c_double),
		#特殊产品持仓盈亏
		("SpecProductPositionProfit",c_double),
		#特殊产品平仓盈亏
		("SpecProductCloseProfit",c_double),
		#根据持仓盈亏算法计算的特殊产品持仓盈亏
		("SpecProductPositionProfitByAlg",c_double),
		#特殊产品交易所保证金
		("SpecProductExchangeMargin",c_double),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getPreMortgage(self):
		return self.PreMortgage
	def getPreCredit(self):
		return self.PreCredit
	def getPreDeposit(self):
		return self.PreDeposit
	def getPreBalance(self):
		return self.PreBalance
	def getPreMargin(self):
		return self.PreMargin
	def getInterestBase(self):
		return self.InterestBase
	def getInterest(self):
		return self.Interest
	def getDeposit(self):
		return self.Deposit
	def getWithdraw(self):
		return self.Withdraw
	def getFrozenMargin(self):
		return self.FrozenMargin
	def getFrozenCash(self):
		return self.FrozenCash
	def getFrozenCommission(self):
		return self.FrozenCommission
	def getCurrMargin(self):
		return self.CurrMargin
	def getCashIn(self):
		return self.CashIn
	def getCommission(self):
		return self.Commission
	def getCloseProfit(self):
		return self.CloseProfit
	def getPositionProfit(self):
		return self.PositionProfit
	def getBalance(self):
		return self.Balance
	def getAvailable(self):
		return self.Available
	def getWithdrawQuota(self):
		return self.WithdrawQuota
	def getReserve(self):
		return self.Reserve
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getSettlementID(self):
		return self.SettlementID
	def getCredit(self):
		return self.Credit
	def getMortgage(self):
		return self.Mortgage
	def getExchangeMargin(self):
		return self.ExchangeMargin
	def getDeliveryMargin(self):
		return self.DeliveryMargin
	def getExchangeDeliveryMargin(self):
		return self.ExchangeDeliveryMargin
	def getReserveBalance(self):
		return self.ReserveBalance
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')
	def getPreFundMortgageIn(self):
		return self.PreFundMortgageIn
	def getPreFundMortgageOut(self):
		return self.PreFundMortgageOut
	def getFundMortgageIn(self):
		return self.FundMortgageIn
	def getFundMortgageOut(self):
		return self.FundMortgageOut
	def getFundMortgageAvailable(self):
		return self.FundMortgageAvailable
	def getMortgageableFund(self):
		return self.MortgageableFund
	def getSpecProductMargin(self):
		return self.SpecProductMargin
	def getSpecProductFrozenMargin(self):
		return self.SpecProductFrozenMargin
	def getSpecProductCommission(self):
		return self.SpecProductCommission
	def getSpecProductFrozenCommission(self):
		return self.SpecProductFrozenCommission
	def getSpecProductPositionProfit(self):
		return self.SpecProductPositionProfit
	def getSpecProductCloseProfit(self):
		return self.SpecProductCloseProfit
	def getSpecProductPositionProfitByAlg(self):
		return self.SpecProductPositionProfitByAlg
	def getSpecProductExchangeMargin(self):
		return self.SpecProductExchangeMargin

class CThostFtdcInvestorPositionField(Structure):
	"""投资者持仓"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#持仓多空方向
		("PosiDirection",c_char),
		#投机套保标志
		("HedgeFlag",c_char),
		#持仓日期
		("PositionDate",c_char),
		#上日持仓
		("YdPosition",c_int32),
		#今日持仓
		("Position",c_int32),
		#多头冻结
		("LongFrozen",c_int32),
		#空头冻结
		("ShortFrozen",c_int32),
		#开仓冻结金额
		("LongFrozenAmount",c_double),
		#开仓冻结金额
		("ShortFrozenAmount",c_double),
		#开仓量
		("OpenVolume",c_int32),
		#平仓量
		("CloseVolume",c_int32),
		#开仓金额
		("OpenAmount",c_double),
		#平仓金额
		("CloseAmount",c_double),
		#持仓成本
		("PositionCost",c_double),
		#上次占用的保证金
		("PreMargin",c_double),
		#占用的保证金
		("UseMargin",c_double),
		#冻结的保证金
		("FrozenMargin",c_double),
		#冻结的资金
		("FrozenCash",c_double),
		#冻结的手续费
		("FrozenCommission",c_double),
		#资金差额
		("CashIn",c_double),
		#手续费
		("Commission",c_double),
		#平仓盈亏
		("CloseProfit",c_double),
		#持仓盈亏
		("PositionProfit",c_double),
		#上次结算价
		("PreSettlementPrice",c_double),
		#本次结算价
		("SettlementPrice",c_double),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#开仓成本
		("OpenCost",c_double),
		#交易所保证金
		("ExchangeMargin",c_double),
		#组合成交形成的持仓
		("CombPosition",c_int32),
		#组合多头冻结
		("CombLongFrozen",c_int32),
		#组合空头冻结
		("CombShortFrozen",c_int32),
		#逐日盯市平仓盈亏
		("CloseProfitByDate",c_double),
		#逐笔对冲平仓盈亏
		("CloseProfitByTrade",c_double),
		#今日持仓
		("TodayPosition",c_int32),
		#保证金率
		("MarginRateByMoney",c_double),
		#保证金率(按手数)
		("MarginRateByVolume",c_double),
		#执行冻结
		("StrikeFrozen",c_int32),
		#执行冻结金额
		("StrikeFrozenAmount",c_double),
		#放弃执行冻结
		("AbandonFrozen",c_int32),
		]

	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getPosiDirection(self):
		return PosiDirectionType(ord(self.PosiDirection))
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getPositionDate(self):
		return PositionDateType(ord(self.PositionDate))
	def getYdPosition(self):
		return self.YdPosition
	def getPosition(self):
		return self.Position
	def getLongFrozen(self):
		return self.LongFrozen
	def getShortFrozen(self):
		return self.ShortFrozen
	def getLongFrozenAmount(self):
		return self.LongFrozenAmount
	def getShortFrozenAmount(self):
		return self.ShortFrozenAmount
	def getOpenVolume(self):
		return self.OpenVolume
	def getCloseVolume(self):
		return self.CloseVolume
	def getOpenAmount(self):
		return self.OpenAmount
	def getCloseAmount(self):
		return self.CloseAmount
	def getPositionCost(self):
		return self.PositionCost
	def getPreMargin(self):
		return self.PreMargin
	def getUseMargin(self):
		return self.UseMargin
	def getFrozenMargin(self):
		return self.FrozenMargin
	def getFrozenCash(self):
		return self.FrozenCash
	def getFrozenCommission(self):
		return self.FrozenCommission
	def getCashIn(self):
		return self.CashIn
	def getCommission(self):
		return self.Commission
	def getCloseProfit(self):
		return self.CloseProfit
	def getPositionProfit(self):
		return self.PositionProfit
	def getPreSettlementPrice(self):
		return self.PreSettlementPrice
	def getSettlementPrice(self):
		return self.SettlementPrice
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getSettlementID(self):
		return self.SettlementID
	def getOpenCost(self):
		return self.OpenCost
	def getExchangeMargin(self):
		return self.ExchangeMargin
	def getCombPosition(self):
		return self.CombPosition
	def getCombLongFrozen(self):
		return self.CombLongFrozen
	def getCombShortFrozen(self):
		return self.CombShortFrozen
	def getCloseProfitByDate(self):
		return self.CloseProfitByDate
	def getCloseProfitByTrade(self):
		return self.CloseProfitByTrade
	def getTodayPosition(self):
		return self.TodayPosition
	def getMarginRateByMoney(self):
		return self.MarginRateByMoney
	def getMarginRateByVolume(self):
		return self.MarginRateByVolume
	def getStrikeFrozen(self):
		return self.StrikeFrozen
	def getStrikeFrozenAmount(self):
		return self.StrikeFrozenAmount
	def getAbandonFrozen(self):
		return self.AbandonFrozen

class CThostFtdcInstrumentMarginRateField(Structure):
	"""合约保证金率"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#投资者范围
		("InvestorRange",c_char),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#投机套保标志
		("HedgeFlag",c_char),
		#多头保证金率
		("LongMarginRatioByMoney",c_double),
		#多头保证金费
		("LongMarginRatioByVolume",c_double),
		#空头保证金率
		("ShortMarginRatioByMoney",c_double),
		#空头保证金费
		("ShortMarginRatioByVolume",c_double),
		#是否相对交易所收取
		("IsRelative",c_int32),
		]

	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getLongMarginRatioByMoney(self):
		return self.LongMarginRatioByMoney
	def getLongMarginRatioByVolume(self):
		return self.LongMarginRatioByVolume
	def getShortMarginRatioByMoney(self):
		return self.ShortMarginRatioByMoney
	def getShortMarginRatioByVolume(self):
		return self.ShortMarginRatioByVolume
	def getIsRelative(self):
		return self.IsRelative

class CThostFtdcInstrumentCommissionRateField(Structure):
	"""合约手续费率"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#投资者范围
		("InvestorRange",c_char),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#开仓手续费率
		("OpenRatioByMoney",c_double),
		#开仓手续费
		("OpenRatioByVolume",c_double),
		#平仓手续费率
		("CloseRatioByMoney",c_double),
		#平仓手续费
		("CloseRatioByVolume",c_double),
		#平今手续费率
		("CloseTodayRatioByMoney",c_double),
		#平今手续费
		("CloseTodayRatioByVolume",c_double),
		]

	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getOpenRatioByMoney(self):
		return self.OpenRatioByMoney
	def getOpenRatioByVolume(self):
		return self.OpenRatioByVolume
	def getCloseRatioByMoney(self):
		return self.CloseRatioByMoney
	def getCloseRatioByVolume(self):
		return self.CloseRatioByVolume
	def getCloseTodayRatioByMoney(self):
		return self.CloseTodayRatioByMoney
	def getCloseTodayRatioByVolume(self):
		return self.CloseTodayRatioByVolume

class CThostFtdcDepthMarketDataField(Structure):
	"""深度行情"""
	_fields_ = [
		#交易日
		("TradingDay",c_char*9),
		#合约代码
		("InstrumentID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#最新价
		("LastPrice",c_double),
		#上次结算价
		("PreSettlementPrice",c_double),
		#昨收盘
		("PreClosePrice",c_double),
		#昨持仓量
		("PreOpenInterest",c_double),
		#今开盘
		("OpenPrice",c_double),
		#最高价
		("HighestPrice",c_double),
		#最低价
		("LowestPrice",c_double),
		#数量
		("Volume",c_int32),
		#成交金额
		("Turnover",c_double),
		#持仓量
		("OpenInterest",c_double),
		#今收盘
		("ClosePrice",c_double),
		#本次结算价
		("SettlementPrice",c_double),
		#涨停板价
		("UpperLimitPrice",c_double),
		#跌停板价
		("LowerLimitPrice",c_double),
		#昨虚实度
		("PreDelta",c_double),
		#今虚实度
		("CurrDelta",c_double),
		#最后修改时间
		("UpdateTime",c_char*9),
		#最后修改毫秒
		("UpdateMillisec",c_int32),
		#申买价一
		("BidPrice1",c_double),
		#申买量一
		("BidVolume1",c_int32),
		#申卖价一
		("AskPrice1",c_double),
		#申卖量一
		("AskVolume1",c_int32),
		#申买价二
		("BidPrice2",c_double),
		#申买量二
		("BidVolume2",c_int32),
		#申卖价二
		("AskPrice2",c_double),
		#申卖量二
		("AskVolume2",c_int32),
		#申买价三
		("BidPrice3",c_double),
		#申买量三
		("BidVolume3",c_int32),
		#申卖价三
		("AskPrice3",c_double),
		#申卖量三
		("AskVolume3",c_int32),
		#申买价四
		("BidPrice4",c_double),
		#申买量四
		("BidVolume4",c_int32),
		#申卖价四
		("AskPrice4",c_double),
		#申卖量四
		("AskVolume4",c_int32),
		#申买价五
		("BidPrice5",c_double),
		#申买量五
		("BidVolume5",c_int32),
		#申卖价五
		("AskPrice5",c_double),
		#申卖量五
		("AskVolume5",c_int32),
		#当日均价
		("AveragePrice",c_double),
		#业务日期
		("ActionDay",c_char*9),
		]

	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getExchangeInstID(self):
		return self.ExchangeInstID.decode('ascii')
	def getLastPrice(self):
		return self.LastPrice
	def getPreSettlementPrice(self):
		return self.PreSettlementPrice
	def getPreClosePrice(self):
		return self.PreClosePrice
	def getPreOpenInterest(self):
		return self.PreOpenInterest
	def getOpenPrice(self):
		return self.OpenPrice
	def getHighestPrice(self):
		return self.HighestPrice
	def getLowestPrice(self):
		return self.LowestPrice
	def getVolume(self):
		return self.Volume
	def getTurnover(self):
		return self.Turnover
	def getOpenInterest(self):
		return self.OpenInterest
	def getClosePrice(self):
		return self.ClosePrice
	def getSettlementPrice(self):
		return self.SettlementPrice
	def getUpperLimitPrice(self):
		return self.UpperLimitPrice
	def getLowerLimitPrice(self):
		return self.LowerLimitPrice
	def getPreDelta(self):
		return self.PreDelta
	def getCurrDelta(self):
		return self.CurrDelta
	def getUpdateTime(self):
		return self.UpdateTime.decode('ascii')
	def getUpdateMillisec(self):
		return self.UpdateMillisec
	def getBidPrice1(self):
		return self.BidPrice1
	def getBidVolume1(self):
		return self.BidVolume1
	def getAskPrice1(self):
		return self.AskPrice1
	def getAskVolume1(self):
		return self.AskVolume1
	def getBidPrice2(self):
		return self.BidPrice2
	def getBidVolume2(self):
		return self.BidVolume2
	def getAskPrice2(self):
		return self.AskPrice2
	def getAskVolume2(self):
		return self.AskVolume2
	def getBidPrice3(self):
		return self.BidPrice3
	def getBidVolume3(self):
		return self.BidVolume3
	def getAskPrice3(self):
		return self.AskPrice3
	def getAskVolume3(self):
		return self.AskVolume3
	def getBidPrice4(self):
		return self.BidPrice4
	def getBidVolume4(self):
		return self.BidVolume4
	def getAskPrice4(self):
		return self.AskPrice4
	def getAskVolume4(self):
		return self.AskVolume4
	def getBidPrice5(self):
		return self.BidPrice5
	def getBidVolume5(self):
		return self.BidVolume5
	def getAskPrice5(self):
		return self.AskPrice5
	def getAskVolume5(self):
		return self.AskVolume5
	def getAveragePrice(self):
		return self.AveragePrice
	def getActionDay(self):
		return self.ActionDay.decode('ascii')

class CThostFtdcInstrumentTradingRightField(Structure):
	"""投资者合约交易权限"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#投资者范围
		("InvestorRange",c_char),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#交易权限
		("TradingRight",c_char),
		]

	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getTradingRight(self):
		return TradingRightType(ord(self.TradingRight))

class CThostFtdcBrokerUserField(Structure):
	"""经纪公司用户"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#用户名称
		("UserName",c_char*81),
		#用户类型
		("UserType",c_char),
		#是否活跃
		("IsActive",c_int32),
		#是否使用令牌
		("IsUsingOTP",c_int32),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getUserName(self):
		return self.UserName.decode('ascii')
	def getUserType(self):
		return UserTypeType(ord(self.UserType))
	def getIsActive(self):
		return self.IsActive
	def getIsUsingOTP(self):
		return self.IsUsingOTP

class CThostFtdcBrokerUserPasswordField(Structure):
	"""经纪公司用户口令"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#密码
		("Password",c_char*41),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getPassword(self):
		return self.Password.decode('ascii')

class CThostFtdcBrokerUserFunctionField(Structure):
	"""经纪公司用户功能权限"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#经纪公司功能代码
		("BrokerFunctionCode",c_char),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getBrokerFunctionCode(self):
		return BrokerFunctionCodeType(ord(self.BrokerFunctionCode))

class CThostFtdcTraderOfferField(Structure):
	"""交易所交易员报盘机"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		#会员代码
		("ParticipantID",c_char*11),
		#密码
		("Password",c_char*41),
		#安装编号
		("InstallID",c_int32),
		#本地报单编号
		("OrderLocalID",c_char*13),
		#交易所交易员连接状态
		("TraderConnectStatus",c_char),
		#发出连接请求的日期
		("ConnectRequestDate",c_char*9),
		#发出连接请求的时间
		("ConnectRequestTime",c_char*9),
		#上次报告日期
		("LastReportDate",c_char*9),
		#上次报告时间
		("LastReportTime",c_char*9),
		#完成连接日期
		("ConnectDate",c_char*9),
		#完成连接时间
		("ConnectTime",c_char*9),
		#启动日期
		("StartDate",c_char*9),
		#启动时间
		("StartTime",c_char*9),
		#交易日
		("TradingDay",c_char*9),
		#经纪公司代码
		("BrokerID",c_char*11),
		#本席位最大成交编号
		("MaxTradeID",c_char*21),
		#本席位最大报单备拷
		("MaxOrderMessageReference",c_char*7),
		]

	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getPassword(self):
		return self.Password.decode('ascii')
	def getInstallID(self):
		return self.InstallID
	def getOrderLocalID(self):
		return self.OrderLocalID.decode('ascii')
	def getTraderConnectStatus(self):
		return TraderConnectStatusType(ord(self.TraderConnectStatus))
	def getConnectRequestDate(self):
		return self.ConnectRequestDate.decode('ascii')
	def getConnectRequestTime(self):
		return self.ConnectRequestTime.decode('ascii')
	def getLastReportDate(self):
		return self.LastReportDate.decode('ascii')
	def getLastReportTime(self):
		return self.LastReportTime.decode('ascii')
	def getConnectDate(self):
		return self.ConnectDate.decode('ascii')
	def getConnectTime(self):
		return self.ConnectTime.decode('ascii')
	def getStartDate(self):
		return self.StartDate.decode('ascii')
	def getStartTime(self):
		return self.StartTime.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getMaxTradeID(self):
		return self.MaxTradeID.decode('ascii')
	def getMaxOrderMessageReference(self):
		return self.MaxOrderMessageReference.decode('ascii')

class CThostFtdcSettlementInfoField(Structure):
	"""投资者结算结果"""
	_fields_ = [
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#序号
		("SequenceNo",c_int32),
		#消息正文
		("Content",c_char*501),
		]

	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getSettlementID(self):
		return self.SettlementID
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getSequenceNo(self):
		return self.SequenceNo
	def getContent(self):
		return self.Content.decode('ascii')

class CThostFtdcInstrumentMarginRateAdjustField(Structure):
	"""合约保证金率调整"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#投资者范围
		("InvestorRange",c_char),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#投机套保标志
		("HedgeFlag",c_char),
		#多头保证金率
		("LongMarginRatioByMoney",c_double),
		#多头保证金费
		("LongMarginRatioByVolume",c_double),
		#空头保证金率
		("ShortMarginRatioByMoney",c_double),
		#空头保证金费
		("ShortMarginRatioByVolume",c_double),
		#是否相对交易所收取
		("IsRelative",c_int32),
		]

	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getLongMarginRatioByMoney(self):
		return self.LongMarginRatioByMoney
	def getLongMarginRatioByVolume(self):
		return self.LongMarginRatioByVolume
	def getShortMarginRatioByMoney(self):
		return self.ShortMarginRatioByMoney
	def getShortMarginRatioByVolume(self):
		return self.ShortMarginRatioByVolume
	def getIsRelative(self):
		return self.IsRelative

class CThostFtdcExchangeMarginRateField(Structure):
	"""交易所保证金率"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#合约代码
		("InstrumentID",c_char*31),
		#投机套保标志
		("HedgeFlag",c_char),
		#多头保证金率
		("LongMarginRatioByMoney",c_double),
		#多头保证金费
		("LongMarginRatioByVolume",c_double),
		#空头保证金率
		("ShortMarginRatioByMoney",c_double),
		#空头保证金费
		("ShortMarginRatioByVolume",c_double),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getLongMarginRatioByMoney(self):
		return self.LongMarginRatioByMoney
	def getLongMarginRatioByVolume(self):
		return self.LongMarginRatioByVolume
	def getShortMarginRatioByMoney(self):
		return self.ShortMarginRatioByMoney
	def getShortMarginRatioByVolume(self):
		return self.ShortMarginRatioByVolume

class CThostFtdcExchangeMarginRateAdjustField(Structure):
	"""交易所保证金率调整"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#合约代码
		("InstrumentID",c_char*31),
		#投机套保标志
		("HedgeFlag",c_char),
		#跟随交易所投资者多头保证金率
		("LongMarginRatioByMoney",c_double),
		#跟随交易所投资者多头保证金费
		("LongMarginRatioByVolume",c_double),
		#跟随交易所投资者空头保证金率
		("ShortMarginRatioByMoney",c_double),
		#跟随交易所投资者空头保证金费
		("ShortMarginRatioByVolume",c_double),
		#交易所多头保证金率
		("ExchLongMarginRatioByMoney",c_double),
		#交易所多头保证金费
		("ExchLongMarginRatioByVolume",c_double),
		#交易所空头保证金率
		("ExchShortMarginRatioByMoney",c_double),
		#交易所空头保证金费
		("ExchShortMarginRatioByVolume",c_double),
		#不跟随交易所投资者多头保证金率
		("NoLongMarginRatioByMoney",c_double),
		#不跟随交易所投资者多头保证金费
		("NoLongMarginRatioByVolume",c_double),
		#不跟随交易所投资者空头保证金率
		("NoShortMarginRatioByMoney",c_double),
		#不跟随交易所投资者空头保证金费
		("NoShortMarginRatioByVolume",c_double),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getLongMarginRatioByMoney(self):
		return self.LongMarginRatioByMoney
	def getLongMarginRatioByVolume(self):
		return self.LongMarginRatioByVolume
	def getShortMarginRatioByMoney(self):
		return self.ShortMarginRatioByMoney
	def getShortMarginRatioByVolume(self):
		return self.ShortMarginRatioByVolume
	def getExchLongMarginRatioByMoney(self):
		return self.ExchLongMarginRatioByMoney
	def getExchLongMarginRatioByVolume(self):
		return self.ExchLongMarginRatioByVolume
	def getExchShortMarginRatioByMoney(self):
		return self.ExchShortMarginRatioByMoney
	def getExchShortMarginRatioByVolume(self):
		return self.ExchShortMarginRatioByVolume
	def getNoLongMarginRatioByMoney(self):
		return self.NoLongMarginRatioByMoney
	def getNoLongMarginRatioByVolume(self):
		return self.NoLongMarginRatioByVolume
	def getNoShortMarginRatioByMoney(self):
		return self.NoShortMarginRatioByMoney
	def getNoShortMarginRatioByVolume(self):
		return self.NoShortMarginRatioByVolume

class CThostFtdcExchangeRateField(Structure):
	"""汇率"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#源币种
		("FromCurrencyID",c_char*4),
		#源币种单位数量
		("FromCurrencyUnit",c_double),
		#目标币种
		("ToCurrencyID",c_char*4),
		#汇率
		("ExchangeRate",c_double),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getFromCurrencyID(self):
		return self.FromCurrencyID.decode('ascii')
	def getFromCurrencyUnit(self):
		return self.FromCurrencyUnit
	def getToCurrencyID(self):
		return self.ToCurrencyID.decode('ascii')
	def getExchangeRate(self):
		return self.ExchangeRate

class CThostFtdcSettlementRefField(Structure):
	"""结算引用"""
	_fields_ = [
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		]

	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getSettlementID(self):
		return self.SettlementID

class CThostFtdcCurrentTimeField(Structure):
	"""当前时间"""
	_fields_ = [
		#当前日期
		("CurrDate",c_char*9),
		#当前时间
		("CurrTime",c_char*9),
		#当前时间（毫秒）
		("CurrMillisec",c_int32),
		#业务日期
		("ActionDay",c_char*9),
		]

	def getCurrDate(self):
		return self.CurrDate.decode('ascii')
	def getCurrTime(self):
		return self.CurrTime.decode('ascii')
	def getCurrMillisec(self):
		return self.CurrMillisec
	def getActionDay(self):
		return self.ActionDay.decode('ascii')

class CThostFtdcCommPhaseField(Structure):
	"""通讯阶段"""
	_fields_ = [
		#交易日
		("TradingDay",c_char*9),
		#通讯时段编号
		("CommPhaseNo",c_int32),
		#系统编号
		("SystemID",c_char*21),
		]

	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getCommPhaseNo(self):
		return self.CommPhaseNo
	def getSystemID(self):
		return self.SystemID.decode('ascii')

class CThostFtdcLoginInfoField(Structure):
	"""登录信息"""
	_fields_ = [
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#登录日期
		("LoginDate",c_char*9),
		#登录时间
		("LoginTime",c_char*9),
		#IP地址
		("IPAddress",c_char*16),
		#用户端产品信息
		("UserProductInfo",c_char*11),
		#接口端产品信息
		("InterfaceProductInfo",c_char*11),
		#协议信息
		("ProtocolInfo",c_char*11),
		#系统名称
		("SystemName",c_char*41),
		#密码
		("Password",c_char*41),
		#最大报单引用
		("MaxOrderRef",c_char*13),
		#上期所时间
		("SHFETime",c_char*9),
		#大商所时间
		("DCETime",c_char*9),
		#郑商所时间
		("CZCETime",c_char*9),
		#中金所时间
		("FFEXTime",c_char*9),
		#Mac地址
		("MacAddress",c_char*21),
		#动态密码
		("OneTimePassword",c_char*41),
		#能源中心时间
		("INETime",c_char*9),
		]

	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getLoginDate(self):
		return self.LoginDate.decode('ascii')
	def getLoginTime(self):
		return self.LoginTime.decode('ascii')
	def getIPAddress(self):
		return self.IPAddress.decode('ascii')
	def getUserProductInfo(self):
		return self.UserProductInfo.decode('ascii')
	def getInterfaceProductInfo(self):
		return self.InterfaceProductInfo.decode('ascii')
	def getProtocolInfo(self):
		return self.ProtocolInfo.decode('ascii')
	def getSystemName(self):
		return self.SystemName.decode('ascii')
	def getPassword(self):
		return self.Password.decode('ascii')
	def getMaxOrderRef(self):
		return self.MaxOrderRef.decode('ascii')
	def getSHFETime(self):
		return self.SHFETime.decode('ascii')
	def getDCETime(self):
		return self.DCETime.decode('ascii')
	def getCZCETime(self):
		return self.CZCETime.decode('ascii')
	def getFFEXTime(self):
		return self.FFEXTime.decode('ascii')
	def getMacAddress(self):
		return self.MacAddress.decode('ascii')
	def getOneTimePassword(self):
		return self.OneTimePassword.decode('ascii')
	def getINETime(self):
		return self.INETime.decode('ascii')

class CThostFtdcLogoutAllField(Structure):
	"""登录信息"""
	_fields_ = [
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#系统名称
		("SystemName",c_char*41),
		]

	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getSystemName(self):
		return self.SystemName.decode('ascii')

class CThostFtdcFrontStatusField(Structure):
	"""前置状态"""
	_fields_ = [
		#前置编号
		("FrontID",c_int32),
		#上次报告日期
		("LastReportDate",c_char*9),
		#上次报告时间
		("LastReportTime",c_char*9),
		#是否活跃
		("IsActive",c_int32),
		]

	def getFrontID(self):
		return self.FrontID
	def getLastReportDate(self):
		return self.LastReportDate.decode('ascii')
	def getLastReportTime(self):
		return self.LastReportTime.decode('ascii')
	def getIsActive(self):
		return self.IsActive

class CThostFtdcUserPasswordUpdateField(Structure):
	"""用户口令变更"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#原来的口令
		("OldPassword",c_char*41),
		#新的口令
		("NewPassword",c_char*41),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getOldPassword(self):
		return self.OldPassword.decode('ascii')
	def getNewPassword(self):
		return self.NewPassword.decode('ascii')

class CThostFtdcInputOrderField(Structure):
	"""输入报单"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#报单引用
		("OrderRef",c_char*13),
		#用户代码
		("UserID",c_char*16),
		#报单价格条件
		("OrderPriceType",c_char),
		#买卖方向
		("Direction",c_char),
		#组合开平标志
		("CombOffsetFlag",c_char*5),
		#组合投机套保标志
		("CombHedgeFlag",c_char*5),
		#价格
		("LimitPrice",c_double),
		#数量
		("VolumeTotalOriginal",c_int32),
		#有效期类型
		("TimeCondition",c_char),
		#GTD日期
		("GTDDate",c_char*9),
		#成交量类型
		("VolumeCondition",c_char),
		#最小成交量
		("MinVolume",c_int32),
		#触发条件
		("ContingentCondition",c_char),
		#止损价
		("StopPrice",c_double),
		#强平原因
		("ForceCloseReason",c_char),
		#自动挂起标志
		("IsAutoSuspend",c_int32),
		#业务单元
		("BusinessUnit",c_char*21),
		#请求编号
		("RequestID",c_int32),
		#用户强评标志
		("UserForceClose",c_int32),
		#互换单标志
		("IsSwapOrder",c_int32),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getOrderRef(self):
		return self.OrderRef.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getOrderPriceType(self):
		return OrderPriceTypeType(ord(self.OrderPriceType))
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getCombOffsetFlag(self):
		return self.CombOffsetFlag.decode('ascii')
	def getCombHedgeFlag(self):
		return self.CombHedgeFlag.decode('ascii')
	def getLimitPrice(self):
		return self.LimitPrice
	def getVolumeTotalOriginal(self):
		return self.VolumeTotalOriginal
	def getTimeCondition(self):
		return TimeConditionType(ord(self.TimeCondition))
	def getGTDDate(self):
		return self.GTDDate.decode('ascii')
	def getVolumeCondition(self):
		return VolumeConditionType(ord(self.VolumeCondition))
	def getMinVolume(self):
		return self.MinVolume
	def getContingentCondition(self):
		return ContingentConditionType(ord(self.ContingentCondition))
	def getStopPrice(self):
		return self.StopPrice
	def getForceCloseReason(self):
		return ForceCloseReasonType(ord(self.ForceCloseReason))
	def getIsAutoSuspend(self):
		return self.IsAutoSuspend
	def getBusinessUnit(self):
		return self.BusinessUnit.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getUserForceClose(self):
		return self.UserForceClose
	def getIsSwapOrder(self):
		return self.IsSwapOrder

class CThostFtdcOrderField(Structure):
	"""报单"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#报单引用
		("OrderRef",c_char*13),
		#用户代码
		("UserID",c_char*16),
		#报单价格条件
		("OrderPriceType",c_char),
		#买卖方向
		("Direction",c_char),
		#组合开平标志
		("CombOffsetFlag",c_char*5),
		#组合投机套保标志
		("CombHedgeFlag",c_char*5),
		#价格
		("LimitPrice",c_double),
		#数量
		("VolumeTotalOriginal",c_int32),
		#有效期类型
		("TimeCondition",c_char),
		#GTD日期
		("GTDDate",c_char*9),
		#成交量类型
		("VolumeCondition",c_char),
		#最小成交量
		("MinVolume",c_int32),
		#触发条件
		("ContingentCondition",c_char),
		#止损价
		("StopPrice",c_double),
		#强平原因
		("ForceCloseReason",c_char),
		#自动挂起标志
		("IsAutoSuspend",c_int32),
		#业务单元
		("BusinessUnit",c_char*21),
		#请求编号
		("RequestID",c_int32),
		#本地报单编号
		("OrderLocalID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#报单提交状态
		("OrderSubmitStatus",c_char),
		#报单提示序号
		("NotifySequence",c_int32),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#报单编号
		("OrderSysID",c_char*21),
		#报单来源
		("OrderSource",c_char),
		#报单状态
		("OrderStatus",c_char),
		#报单类型
		("OrderType",c_char),
		#今成交数量
		("VolumeTraded",c_int32),
		#剩余数量
		("VolumeTotal",c_int32),
		#报单日期
		("InsertDate",c_char*9),
		#委托时间
		("InsertTime",c_char*9),
		#激活时间
		("ActiveTime",c_char*9),
		#挂起时间
		("SuspendTime",c_char*9),
		#最后修改时间
		("UpdateTime",c_char*9),
		#撤销时间
		("CancelTime",c_char*9),
		#最后修改交易所交易员代码
		("ActiveTraderID",c_char*21),
		#结算会员编号
		("ClearingPartID",c_char*11),
		#序号
		("SequenceNo",c_int32),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#用户端产品信息
		("UserProductInfo",c_char*11),
		#状态信息
		("StatusMsg",c_char*81),
		#用户强评标志
		("UserForceClose",c_int32),
		#操作用户代码
		("ActiveUserID",c_char*16),
		#经纪公司报单编号
		("BrokerOrderSeq",c_int32),
		#相关报单
		("RelativeOrderSysID",c_char*21),
		#郑商所成交数量
		("ZCETotalTradedVolume",c_int32),
		#互换单标志
		("IsSwapOrder",c_int32),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getOrderRef(self):
		return self.OrderRef.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getOrderPriceType(self):
		return OrderPriceTypeType(ord(self.OrderPriceType))
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getCombOffsetFlag(self):
		return self.CombOffsetFlag.decode('ascii')
	def getCombHedgeFlag(self):
		return self.CombHedgeFlag.decode('ascii')
	def getLimitPrice(self):
		return self.LimitPrice
	def getVolumeTotalOriginal(self):
		return self.VolumeTotalOriginal
	def getTimeCondition(self):
		return TimeConditionType(ord(self.TimeCondition))
	def getGTDDate(self):
		return self.GTDDate.decode('ascii')
	def getVolumeCondition(self):
		return VolumeConditionType(ord(self.VolumeCondition))
	def getMinVolume(self):
		return self.MinVolume
	def getContingentCondition(self):
		return ContingentConditionType(ord(self.ContingentCondition))
	def getStopPrice(self):
		return self.StopPrice
	def getForceCloseReason(self):
		return ForceCloseReasonType(ord(self.ForceCloseReason))
	def getIsAutoSuspend(self):
		return self.IsAutoSuspend
	def getBusinessUnit(self):
		return self.BusinessUnit.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getOrderLocalID(self):
		return self.OrderLocalID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getClientID(self):
		return self.ClientID.decode('ascii')
	def getExchangeInstID(self):
		return self.ExchangeInstID.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')
	def getInstallID(self):
		return self.InstallID
	def getOrderSubmitStatus(self):
		return OrderSubmitStatusType(ord(self.OrderSubmitStatus))
	def getNotifySequence(self):
		return self.NotifySequence
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getSettlementID(self):
		return self.SettlementID
	def getOrderSysID(self):
		return self.OrderSysID.decode('ascii')
	def getOrderSource(self):
		return OrderSourceType(ord(self.OrderSource))
	def getOrderStatus(self):
		return OrderStatusType(ord(self.OrderStatus))
	def getOrderType(self):
		return OrderTypeType(ord(self.OrderType))
	def getVolumeTraded(self):
		return self.VolumeTraded
	def getVolumeTotal(self):
		return self.VolumeTotal
	def getInsertDate(self):
		return self.InsertDate.decode('ascii')
	def getInsertTime(self):
		return self.InsertTime.decode('ascii')
	def getActiveTime(self):
		return self.ActiveTime.decode('ascii')
	def getSuspendTime(self):
		return self.SuspendTime.decode('ascii')
	def getUpdateTime(self):
		return self.UpdateTime.decode('ascii')
	def getCancelTime(self):
		return self.CancelTime.decode('ascii')
	def getActiveTraderID(self):
		return self.ActiveTraderID.decode('ascii')
	def getClearingPartID(self):
		return self.ClearingPartID.decode('ascii')
	def getSequenceNo(self):
		return self.SequenceNo
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getUserProductInfo(self):
		return self.UserProductInfo.decode('ascii')
	def getStatusMsg(self):
		return self.StatusMsg.decode('GB2312')
	def getUserForceClose(self):
		return self.UserForceClose
	def getActiveUserID(self):
		return self.ActiveUserID.decode('ascii')
	def getBrokerOrderSeq(self):
		return self.BrokerOrderSeq
	def getRelativeOrderSysID(self):
		return self.RelativeOrderSysID.decode('ascii')
	def getZCETotalTradedVolume(self):
		return self.ZCETotalTradedVolume
	def getIsSwapOrder(self):
		return self.IsSwapOrder

class CThostFtdcExchangeOrderField(Structure):
	"""交易所报单"""
	_fields_ = [
		#报单价格条件
		("OrderPriceType",c_char),
		#买卖方向
		("Direction",c_char),
		#组合开平标志
		("CombOffsetFlag",c_char*5),
		#组合投机套保标志
		("CombHedgeFlag",c_char*5),
		#价格
		("LimitPrice",c_double),
		#数量
		("VolumeTotalOriginal",c_int32),
		#有效期类型
		("TimeCondition",c_char),
		#GTD日期
		("GTDDate",c_char*9),
		#成交量类型
		("VolumeCondition",c_char),
		#最小成交量
		("MinVolume",c_int32),
		#触发条件
		("ContingentCondition",c_char),
		#止损价
		("StopPrice",c_double),
		#强平原因
		("ForceCloseReason",c_char),
		#自动挂起标志
		("IsAutoSuspend",c_int32),
		#业务单元
		("BusinessUnit",c_char*21),
		#请求编号
		("RequestID",c_int32),
		#本地报单编号
		("OrderLocalID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#报单提交状态
		("OrderSubmitStatus",c_char),
		#报单提示序号
		("NotifySequence",c_int32),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#报单编号
		("OrderSysID",c_char*21),
		#报单来源
		("OrderSource",c_char),
		#报单状态
		("OrderStatus",c_char),
		#报单类型
		("OrderType",c_char),
		#今成交数量
		("VolumeTraded",c_int32),
		#剩余数量
		("VolumeTotal",c_int32),
		#报单日期
		("InsertDate",c_char*9),
		#委托时间
		("InsertTime",c_char*9),
		#激活时间
		("ActiveTime",c_char*9),
		#挂起时间
		("SuspendTime",c_char*9),
		#最后修改时间
		("UpdateTime",c_char*9),
		#撤销时间
		("CancelTime",c_char*9),
		#最后修改交易所交易员代码
		("ActiveTraderID",c_char*21),
		#结算会员编号
		("ClearingPartID",c_char*11),
		#序号
		("SequenceNo",c_int32),
		]

	def getOrderPriceType(self):
		return OrderPriceTypeType(ord(self.OrderPriceType))
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getCombOffsetFlag(self):
		return self.CombOffsetFlag.decode('ascii')
	def getCombHedgeFlag(self):
		return self.CombHedgeFlag.decode('ascii')
	def getLimitPrice(self):
		return self.LimitPrice
	def getVolumeTotalOriginal(self):
		return self.VolumeTotalOriginal
	def getTimeCondition(self):
		return TimeConditionType(ord(self.TimeCondition))
	def getGTDDate(self):
		return self.GTDDate.decode('ascii')
	def getVolumeCondition(self):
		return VolumeConditionType(ord(self.VolumeCondition))
	def getMinVolume(self):
		return self.MinVolume
	def getContingentCondition(self):
		return ContingentConditionType(ord(self.ContingentCondition))
	def getStopPrice(self):
		return self.StopPrice
	def getForceCloseReason(self):
		return ForceCloseReasonType(ord(self.ForceCloseReason))
	def getIsAutoSuspend(self):
		return self.IsAutoSuspend
	def getBusinessUnit(self):
		return self.BusinessUnit.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getOrderLocalID(self):
		return self.OrderLocalID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getClientID(self):
		return self.ClientID.decode('ascii')
	def getExchangeInstID(self):
		return self.ExchangeInstID.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')
	def getInstallID(self):
		return self.InstallID
	def getOrderSubmitStatus(self):
		return OrderSubmitStatusType(ord(self.OrderSubmitStatus))
	def getNotifySequence(self):
		return self.NotifySequence
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getSettlementID(self):
		return self.SettlementID
	def getOrderSysID(self):
		return self.OrderSysID.decode('ascii')
	def getOrderSource(self):
		return OrderSourceType(ord(self.OrderSource))
	def getOrderStatus(self):
		return OrderStatusType(ord(self.OrderStatus))
	def getOrderType(self):
		return OrderTypeType(ord(self.OrderType))
	def getVolumeTraded(self):
		return self.VolumeTraded
	def getVolumeTotal(self):
		return self.VolumeTotal
	def getInsertDate(self):
		return self.InsertDate.decode('ascii')
	def getInsertTime(self):
		return self.InsertTime.decode('ascii')
	def getActiveTime(self):
		return self.ActiveTime.decode('ascii')
	def getSuspendTime(self):
		return self.SuspendTime.decode('ascii')
	def getUpdateTime(self):
		return self.UpdateTime.decode('ascii')
	def getCancelTime(self):
		return self.CancelTime.decode('ascii')
	def getActiveTraderID(self):
		return self.ActiveTraderID.decode('ascii')
	def getClearingPartID(self):
		return self.ClearingPartID.decode('ascii')
	def getSequenceNo(self):
		return self.SequenceNo

class CThostFtdcExchangeOrderInsertErrorField(Structure):
	"""交易所报单插入失败"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#本地报单编号
		("OrderLocalID",c_char*13),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')
	def getInstallID(self):
		return self.InstallID
	def getOrderLocalID(self):
		return self.OrderLocalID.decode('ascii')
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return self.ErrorMsg.decode('GB2312')

class CThostFtdcInputOrderActionField(Structure):
	"""输入报单操作"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#报单操作引用
		("OrderActionRef",c_int32),
		#报单引用
		("OrderRef",c_char*13),
		#请求编号
		("RequestID",c_int32),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#交易所代码
		("ExchangeID",c_char*9),
		#报单编号
		("OrderSysID",c_char*21),
		#操作标志
		("ActionFlag",c_char),
		#价格
		("LimitPrice",c_double),
		#数量变化
		("VolumeChange",c_int32),
		#用户代码
		("UserID",c_char*16),
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getOrderActionRef(self):
		return self.OrderActionRef
	def getOrderRef(self):
		return self.OrderRef.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getOrderSysID(self):
		return self.OrderSysID.decode('ascii')
	def getActionFlag(self):
		return ActionFlagType(ord(self.ActionFlag))
	def getLimitPrice(self):
		return self.LimitPrice
	def getVolumeChange(self):
		return self.VolumeChange
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')

class CThostFtdcOrderActionField(Structure):
	"""报单操作"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#报单操作引用
		("OrderActionRef",c_int32),
		#报单引用
		("OrderRef",c_char*13),
		#请求编号
		("RequestID",c_int32),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#交易所代码
		("ExchangeID",c_char*9),
		#报单编号
		("OrderSysID",c_char*21),
		#操作标志
		("ActionFlag",c_char),
		#价格
		("LimitPrice",c_double),
		#数量变化
		("VolumeChange",c_int32),
		#操作日期
		("ActionDate",c_char*9),
		#操作时间
		("ActionTime",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#本地报单编号
		("OrderLocalID",c_char*13),
		#操作本地编号
		("ActionLocalID",c_char*13),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#业务单元
		("BusinessUnit",c_char*21),
		#报单操作状态
		("OrderActionStatus",c_char),
		#用户代码
		("UserID",c_char*16),
		#状态信息
		("StatusMsg",c_char*81),
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getOrderActionRef(self):
		return self.OrderActionRef
	def getOrderRef(self):
		return self.OrderRef.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getOrderSysID(self):
		return self.OrderSysID.decode('ascii')
	def getActionFlag(self):
		return ActionFlagType(ord(self.ActionFlag))
	def getLimitPrice(self):
		return self.LimitPrice
	def getVolumeChange(self):
		return self.VolumeChange
	def getActionDate(self):
		return self.ActionDate.decode('ascii')
	def getActionTime(self):
		return self.ActionTime.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')
	def getInstallID(self):
		return self.InstallID
	def getOrderLocalID(self):
		return self.OrderLocalID.decode('ascii')
	def getActionLocalID(self):
		return self.ActionLocalID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getClientID(self):
		return self.ClientID.decode('ascii')
	def getBusinessUnit(self):
		return self.BusinessUnit.decode('ascii')
	def getOrderActionStatus(self):
		return OrderActionStatusType(ord(self.OrderActionStatus))
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getStatusMsg(self):
		return self.StatusMsg.decode('GB2312')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')

class CThostFtdcExchangeOrderActionField(Structure):
	"""交易所报单操作"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#报单编号
		("OrderSysID",c_char*21),
		#操作标志
		("ActionFlag",c_char),
		#价格
		("LimitPrice",c_double),
		#数量变化
		("VolumeChange",c_int32),
		#操作日期
		("ActionDate",c_char*9),
		#操作时间
		("ActionTime",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#本地报单编号
		("OrderLocalID",c_char*13),
		#操作本地编号
		("ActionLocalID",c_char*13),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#业务单元
		("BusinessUnit",c_char*21),
		#报单操作状态
		("OrderActionStatus",c_char),
		#用户代码
		("UserID",c_char*16),
		]

	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getOrderSysID(self):
		return self.OrderSysID.decode('ascii')
	def getActionFlag(self):
		return ActionFlagType(ord(self.ActionFlag))
	def getLimitPrice(self):
		return self.LimitPrice
	def getVolumeChange(self):
		return self.VolumeChange
	def getActionDate(self):
		return self.ActionDate.decode('ascii')
	def getActionTime(self):
		return self.ActionTime.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')
	def getInstallID(self):
		return self.InstallID
	def getOrderLocalID(self):
		return self.OrderLocalID.decode('ascii')
	def getActionLocalID(self):
		return self.ActionLocalID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getClientID(self):
		return self.ClientID.decode('ascii')
	def getBusinessUnit(self):
		return self.BusinessUnit.decode('ascii')
	def getOrderActionStatus(self):
		return OrderActionStatusType(ord(self.OrderActionStatus))
	def getUserID(self):
		return self.UserID.decode('ascii')

class CThostFtdcExchangeOrderActionErrorField(Structure):
	"""交易所报单操作失败"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#报单编号
		("OrderSysID",c_char*21),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#本地报单编号
		("OrderLocalID",c_char*13),
		#操作本地编号
		("ActionLocalID",c_char*13),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getOrderSysID(self):
		return self.OrderSysID.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')
	def getInstallID(self):
		return self.InstallID
	def getOrderLocalID(self):
		return self.OrderLocalID.decode('ascii')
	def getActionLocalID(self):
		return self.ActionLocalID.decode('ascii')
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return self.ErrorMsg.decode('GB2312')

class CThostFtdcExchangeTradeField(Structure):
	"""交易所成交"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#成交编号
		("TradeID",c_char*21),
		#买卖方向
		("Direction",c_char),
		#报单编号
		("OrderSysID",c_char*21),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#交易角色
		("TradingRole",c_char),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#开平标志
		("OffsetFlag",c_char),
		#投机套保标志
		("HedgeFlag",c_char),
		#价格
		("Price",c_double),
		#数量
		("Volume",c_int32),
		#成交时期
		("TradeDate",c_char*9),
		#成交时间
		("TradeTime",c_char*9),
		#成交类型
		("TradeType",c_char),
		#成交价来源
		("PriceSource",c_char),
		#交易所交易员代码
		("TraderID",c_char*21),
		#本地报单编号
		("OrderLocalID",c_char*13),
		#结算会员编号
		("ClearingPartID",c_char*11),
		#业务单元
		("BusinessUnit",c_char*21),
		#序号
		("SequenceNo",c_int32),
		#成交来源
		("TradeSource",c_char),
		]

	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getTradeID(self):
		return self.TradeID.decode('ascii')
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getOrderSysID(self):
		return self.OrderSysID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getClientID(self):
		return self.ClientID.decode('ascii')
	def getTradingRole(self):
		return TradingRoleType(ord(self.TradingRole))
	def getExchangeInstID(self):
		return self.ExchangeInstID.decode('ascii')
	def getOffsetFlag(self):
		return OffsetFlagType(ord(self.OffsetFlag))
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getPrice(self):
		return self.Price
	def getVolume(self):
		return self.Volume
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getTradeType(self):
		return TradeTypeType(ord(self.TradeType))
	def getPriceSource(self):
		return PriceSourceType(ord(self.PriceSource))
	def getTraderID(self):
		return self.TraderID.decode('ascii')
	def getOrderLocalID(self):
		return self.OrderLocalID.decode('ascii')
	def getClearingPartID(self):
		return self.ClearingPartID.decode('ascii')
	def getBusinessUnit(self):
		return self.BusinessUnit.decode('ascii')
	def getSequenceNo(self):
		return self.SequenceNo
	def getTradeSource(self):
		return TradeSourceType(ord(self.TradeSource))

class CThostFtdcTradeField(Structure):
	"""成交"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#报单引用
		("OrderRef",c_char*13),
		#用户代码
		("UserID",c_char*16),
		#交易所代码
		("ExchangeID",c_char*9),
		#成交编号
		("TradeID",c_char*21),
		#买卖方向
		("Direction",c_char),
		#报单编号
		("OrderSysID",c_char*21),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#交易角色
		("TradingRole",c_char),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#开平标志
		("OffsetFlag",c_char),
		#投机套保标志
		("HedgeFlag",c_char),
		#价格
		("Price",c_double),
		#数量
		("Volume",c_int32),
		#成交时期
		("TradeDate",c_char*9),
		#成交时间
		("TradeTime",c_char*9),
		#成交类型
		("TradeType",c_char),
		#成交价来源
		("PriceSource",c_char),
		#交易所交易员代码
		("TraderID",c_char*21),
		#本地报单编号
		("OrderLocalID",c_char*13),
		#结算会员编号
		("ClearingPartID",c_char*11),
		#业务单元
		("BusinessUnit",c_char*21),
		#序号
		("SequenceNo",c_int32),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#经纪公司报单编号
		("BrokerOrderSeq",c_int32),
		#成交来源
		("TradeSource",c_char),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getOrderRef(self):
		return self.OrderRef.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getTradeID(self):
		return self.TradeID.decode('ascii')
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getOrderSysID(self):
		return self.OrderSysID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getClientID(self):
		return self.ClientID.decode('ascii')
	def getTradingRole(self):
		return TradingRoleType(ord(self.TradingRole))
	def getExchangeInstID(self):
		return self.ExchangeInstID.decode('ascii')
	def getOffsetFlag(self):
		return OffsetFlagType(ord(self.OffsetFlag))
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getPrice(self):
		return self.Price
	def getVolume(self):
		return self.Volume
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getTradeType(self):
		return TradeTypeType(ord(self.TradeType))
	def getPriceSource(self):
		return PriceSourceType(ord(self.PriceSource))
	def getTraderID(self):
		return self.TraderID.decode('ascii')
	def getOrderLocalID(self):
		return self.OrderLocalID.decode('ascii')
	def getClearingPartID(self):
		return self.ClearingPartID.decode('ascii')
	def getBusinessUnit(self):
		return self.BusinessUnit.decode('ascii')
	def getSequenceNo(self):
		return self.SequenceNo
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getSettlementID(self):
		return self.SettlementID
	def getBrokerOrderSeq(self):
		return self.BrokerOrderSeq
	def getTradeSource(self):
		return TradeSourceType(ord(self.TradeSource))

class CThostFtdcUserSessionField(Structure):
	"""用户会话"""
	_fields_ = [
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#登录日期
		("LoginDate",c_char*9),
		#登录时间
		("LoginTime",c_char*9),
		#IP地址
		("IPAddress",c_char*16),
		#用户端产品信息
		("UserProductInfo",c_char*11),
		#接口端产品信息
		("InterfaceProductInfo",c_char*11),
		#协议信息
		("ProtocolInfo",c_char*11),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getLoginDate(self):
		return self.LoginDate.decode('ascii')
	def getLoginTime(self):
		return self.LoginTime.decode('ascii')
	def getIPAddress(self):
		return self.IPAddress.decode('ascii')
	def getUserProductInfo(self):
		return self.UserProductInfo.decode('ascii')
	def getInterfaceProductInfo(self):
		return self.InterfaceProductInfo.decode('ascii')
	def getProtocolInfo(self):
		return self.ProtocolInfo.decode('ascii')
	def getMacAddress(self):
		return self.MacAddress.decode('ascii')

class CThostFtdcQueryMaxOrderVolumeField(Structure):
	"""查询最大报单数量"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#买卖方向
		("Direction",c_char),
		#开平标志
		("OffsetFlag",c_char),
		#投机套保标志
		("HedgeFlag",c_char),
		#最大允许报单数量
		("MaxVolume",c_int32),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getOffsetFlag(self):
		return OffsetFlagType(ord(self.OffsetFlag))
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getMaxVolume(self):
		return self.MaxVolume

class CThostFtdcSettlementInfoConfirmField(Structure):
	"""投资者结算结果确认信息"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#确认日期
		("ConfirmDate",c_char*9),
		#确认时间
		("ConfirmTime",c_char*9),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getConfirmDate(self):
		return self.ConfirmDate.decode('ascii')
	def getConfirmTime(self):
		return self.ConfirmTime.decode('ascii')

class CThostFtdcSyncDepositField(Structure):
	"""出入金同步"""
	_fields_ = [
		#出入金流水号
		("DepositSeqNo",c_char*15),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#入金金额
		("Deposit",c_double),
		#是否强制进行
		("IsForce",c_int32),
		#币种代码
		("CurrencyID",c_char*4),
		]

	def getDepositSeqNo(self):
		return self.DepositSeqNo.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getDeposit(self):
		return self.Deposit
	def getIsForce(self):
		return self.IsForce
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')

class CThostFtdcSyncFundMortgageField(Structure):
	"""货币质押同步"""
	_fields_ = [
		#货币质押流水号
		("MortgageSeqNo",c_char*15),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#源币种
		("FromCurrencyID",c_char*4),
		#质押金额
		("MortgageAmount",c_double),
		#目标币种
		("ToCurrencyID",c_char*4),
		]

	def getMortgageSeqNo(self):
		return self.MortgageSeqNo.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getFromCurrencyID(self):
		return self.FromCurrencyID.decode('ascii')
	def getMortgageAmount(self):
		return self.MortgageAmount
	def getToCurrencyID(self):
		return self.ToCurrencyID.decode('ascii')

class CThostFtdcBrokerSyncField(Structure):
	"""经纪公司同步"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')

class CThostFtdcSyncingInvestorField(Structure):
	"""正在同步中的投资者"""
	_fields_ = [
		#投资者代码
		("InvestorID",c_char*13),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者分组代码
		("InvestorGroupID",c_char*13),
		#投资者名称
		("InvestorName",c_char*81),
		#证件类型
		("IdentifiedCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#是否活跃
		("IsActive",c_int32),
		#联系电话
		("Telephone",c_char*41),
		#通讯地址
		("Address",c_char*101),
		#开户日期
		("OpenDate",c_char*9),
		#手机
		("Mobile",c_char*41),
		#手续费率模板代码
		("CommModelID",c_char*13),
		#保证金率模板代码
		("MarginModelID",c_char*13),
		]

	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorGroupID(self):
		return self.InvestorGroupID.decode('ascii')
	def getInvestorName(self):
		return self.InvestorName.decode('ascii')
	def getIdentifiedCardType(self):
		return IdCardTypeType(ord(self.IdentifiedCardType))
	def getIdentifiedCardNo(self):
		return self.IdentifiedCardNo.decode('ascii')
	def getIsActive(self):
		return self.IsActive
	def getTelephone(self):
		return self.Telephone.decode('ascii')
	def getAddress(self):
		return self.Address.decode('ascii')
	def getOpenDate(self):
		return self.OpenDate.decode('ascii')
	def getMobile(self):
		return self.Mobile.decode('ascii')
	def getCommModelID(self):
		return self.CommModelID.decode('ascii')
	def getMarginModelID(self):
		return self.MarginModelID.decode('ascii')

class CThostFtdcSyncingTradingCodeField(Structure):
	"""正在同步中的交易代码"""
	_fields_ = [
		#投资者代码
		("InvestorID",c_char*13),
		#经纪公司代码
		("BrokerID",c_char*11),
		#交易所代码
		("ExchangeID",c_char*9),
		#客户代码
		("ClientID",c_char*11),
		#是否活跃
		("IsActive",c_int32),
		#交易编码类型
		("ClientIDType",c_char),
		]

	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getClientID(self):
		return self.ClientID.decode('ascii')
	def getIsActive(self):
		return self.IsActive
	def getClientIDType(self):
		return ClientIDTypeType(ord(self.ClientIDType))

class CThostFtdcSyncingInvestorGroupField(Structure):
	"""正在同步中的投资者分组"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者分组代码
		("InvestorGroupID",c_char*13),
		#投资者分组名称
		("InvestorGroupName",c_char*41),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorGroupID(self):
		return self.InvestorGroupID.decode('ascii')
	def getInvestorGroupName(self):
		return self.InvestorGroupName.decode('ascii')

class CThostFtdcSyncingTradingAccountField(Structure):
	"""正在同步中的交易账号"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者帐号
		("AccountID",c_char*13),
		#上次质押金额
		("PreMortgage",c_double),
		#上次信用额度
		("PreCredit",c_double),
		#上次存款额
		("PreDeposit",c_double),
		#上次结算准备金
		("PreBalance",c_double),
		#上次占用的保证金
		("PreMargin",c_double),
		#利息基数
		("InterestBase",c_double),
		#利息收入
		("Interest",c_double),
		#入金金额
		("Deposit",c_double),
		#出金金额
		("Withdraw",c_double),
		#冻结的保证金
		("FrozenMargin",c_double),
		#冻结的资金
		("FrozenCash",c_double),
		#冻结的手续费
		("FrozenCommission",c_double),
		#当前保证金总额
		("CurrMargin",c_double),
		#资金差额
		("CashIn",c_double),
		#手续费
		("Commission",c_double),
		#平仓盈亏
		("CloseProfit",c_double),
		#持仓盈亏
		("PositionProfit",c_double),
		#期货结算准备金
		("Balance",c_double),
		#可用资金
		("Available",c_double),
		#可取资金
		("WithdrawQuota",c_double),
		#基本准备金
		("Reserve",c_double),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#信用额度
		("Credit",c_double),
		#质押金额
		("Mortgage",c_double),
		#交易所保证金
		("ExchangeMargin",c_double),
		#投资者交割保证金
		("DeliveryMargin",c_double),
		#交易所交割保证金
		("ExchangeDeliveryMargin",c_double),
		#保底期货结算准备金
		("ReserveBalance",c_double),
		#币种代码
		("CurrencyID",c_char*4),
		#上次货币质入金额
		("PreFundMortgageIn",c_double),
		#上次货币质出金额
		("PreFundMortgageOut",c_double),
		#货币质入金额
		("FundMortgageIn",c_double),
		#货币质出金额
		("FundMortgageOut",c_double),
		#货币质押余额
		("FundMortgageAvailable",c_double),
		#可质押货币金额
		("MortgageableFund",c_double),
		#特殊产品占用保证金
		("SpecProductMargin",c_double),
		#特殊产品冻结保证金
		("SpecProductFrozenMargin",c_double),
		#特殊产品手续费
		("SpecProductCommission",c_double),
		#特殊产品冻结手续费
		("SpecProductFrozenCommission",c_double),
		#特殊产品持仓盈亏
		("SpecProductPositionProfit",c_double),
		#特殊产品平仓盈亏
		("SpecProductCloseProfit",c_double),
		#根据持仓盈亏算法计算的特殊产品持仓盈亏
		("SpecProductPositionProfitByAlg",c_double),
		#特殊产品交易所保证金
		("SpecProductExchangeMargin",c_double),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getPreMortgage(self):
		return self.PreMortgage
	def getPreCredit(self):
		return self.PreCredit
	def getPreDeposit(self):
		return self.PreDeposit
	def getPreBalance(self):
		return self.PreBalance
	def getPreMargin(self):
		return self.PreMargin
	def getInterestBase(self):
		return self.InterestBase
	def getInterest(self):
		return self.Interest
	def getDeposit(self):
		return self.Deposit
	def getWithdraw(self):
		return self.Withdraw
	def getFrozenMargin(self):
		return self.FrozenMargin
	def getFrozenCash(self):
		return self.FrozenCash
	def getFrozenCommission(self):
		return self.FrozenCommission
	def getCurrMargin(self):
		return self.CurrMargin
	def getCashIn(self):
		return self.CashIn
	def getCommission(self):
		return self.Commission
	def getCloseProfit(self):
		return self.CloseProfit
	def getPositionProfit(self):
		return self.PositionProfit
	def getBalance(self):
		return self.Balance
	def getAvailable(self):
		return self.Available
	def getWithdrawQuota(self):
		return self.WithdrawQuota
	def getReserve(self):
		return self.Reserve
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getSettlementID(self):
		return self.SettlementID
	def getCredit(self):
		return self.Credit
	def getMortgage(self):
		return self.Mortgage
	def getExchangeMargin(self):
		return self.ExchangeMargin
	def getDeliveryMargin(self):
		return self.DeliveryMargin
	def getExchangeDeliveryMargin(self):
		return self.ExchangeDeliveryMargin
	def getReserveBalance(self):
		return self.ReserveBalance
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')
	def getPreFundMortgageIn(self):
		return self.PreFundMortgageIn
	def getPreFundMortgageOut(self):
		return self.PreFundMortgageOut
	def getFundMortgageIn(self):
		return self.FundMortgageIn
	def getFundMortgageOut(self):
		return self.FundMortgageOut
	def getFundMortgageAvailable(self):
		return self.FundMortgageAvailable
	def getMortgageableFund(self):
		return self.MortgageableFund
	def getSpecProductMargin(self):
		return self.SpecProductMargin
	def getSpecProductFrozenMargin(self):
		return self.SpecProductFrozenMargin
	def getSpecProductCommission(self):
		return self.SpecProductCommission
	def getSpecProductFrozenCommission(self):
		return self.SpecProductFrozenCommission
	def getSpecProductPositionProfit(self):
		return self.SpecProductPositionProfit
	def getSpecProductCloseProfit(self):
		return self.SpecProductCloseProfit
	def getSpecProductPositionProfitByAlg(self):
		return self.SpecProductPositionProfitByAlg
	def getSpecProductExchangeMargin(self):
		return self.SpecProductExchangeMargin

class CThostFtdcSyncingInvestorPositionField(Structure):
	"""正在同步中的投资者持仓"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#持仓多空方向
		("PosiDirection",c_char),
		#投机套保标志
		("HedgeFlag",c_char),
		#持仓日期
		("PositionDate",c_char),
		#上日持仓
		("YdPosition",c_int32),
		#今日持仓
		("Position",c_int32),
		#多头冻结
		("LongFrozen",c_int32),
		#空头冻结
		("ShortFrozen",c_int32),
		#开仓冻结金额
		("LongFrozenAmount",c_double),
		#开仓冻结金额
		("ShortFrozenAmount",c_double),
		#开仓量
		("OpenVolume",c_int32),
		#平仓量
		("CloseVolume",c_int32),
		#开仓金额
		("OpenAmount",c_double),
		#平仓金额
		("CloseAmount",c_double),
		#持仓成本
		("PositionCost",c_double),
		#上次占用的保证金
		("PreMargin",c_double),
		#占用的保证金
		("UseMargin",c_double),
		#冻结的保证金
		("FrozenMargin",c_double),
		#冻结的资金
		("FrozenCash",c_double),
		#冻结的手续费
		("FrozenCommission",c_double),
		#资金差额
		("CashIn",c_double),
		#手续费
		("Commission",c_double),
		#平仓盈亏
		("CloseProfit",c_double),
		#持仓盈亏
		("PositionProfit",c_double),
		#上次结算价
		("PreSettlementPrice",c_double),
		#本次结算价
		("SettlementPrice",c_double),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#开仓成本
		("OpenCost",c_double),
		#交易所保证金
		("ExchangeMargin",c_double),
		#组合成交形成的持仓
		("CombPosition",c_int32),
		#组合多头冻结
		("CombLongFrozen",c_int32),
		#组合空头冻结
		("CombShortFrozen",c_int32),
		#逐日盯市平仓盈亏
		("CloseProfitByDate",c_double),
		#逐笔对冲平仓盈亏
		("CloseProfitByTrade",c_double),
		#今日持仓
		("TodayPosition",c_int32),
		#保证金率
		("MarginRateByMoney",c_double),
		#保证金率(按手数)
		("MarginRateByVolume",c_double),
		#执行冻结
		("StrikeFrozen",c_int32),
		#执行冻结金额
		("StrikeFrozenAmount",c_double),
		#放弃执行冻结
		("AbandonFrozen",c_int32),
		]

	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getPosiDirection(self):
		return PosiDirectionType(ord(self.PosiDirection))
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getPositionDate(self):
		return PositionDateType(ord(self.PositionDate))
	def getYdPosition(self):
		return self.YdPosition
	def getPosition(self):
		return self.Position
	def getLongFrozen(self):
		return self.LongFrozen
	def getShortFrozen(self):
		return self.ShortFrozen
	def getLongFrozenAmount(self):
		return self.LongFrozenAmount
	def getShortFrozenAmount(self):
		return self.ShortFrozenAmount
	def getOpenVolume(self):
		return self.OpenVolume
	def getCloseVolume(self):
		return self.CloseVolume
	def getOpenAmount(self):
		return self.OpenAmount
	def getCloseAmount(self):
		return self.CloseAmount
	def getPositionCost(self):
		return self.PositionCost
	def getPreMargin(self):
		return self.PreMargin
	def getUseMargin(self):
		return self.UseMargin
	def getFrozenMargin(self):
		return self.FrozenMargin
	def getFrozenCash(self):
		return self.FrozenCash
	def getFrozenCommission(self):
		return self.FrozenCommission
	def getCashIn(self):
		return self.CashIn
	def getCommission(self):
		return self.Commission
	def getCloseProfit(self):
		return self.CloseProfit
	def getPositionProfit(self):
		return self.PositionProfit
	def getPreSettlementPrice(self):
		return self.PreSettlementPrice
	def getSettlementPrice(self):
		return self.SettlementPrice
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getSettlementID(self):
		return self.SettlementID
	def getOpenCost(self):
		return self.OpenCost
	def getExchangeMargin(self):
		return self.ExchangeMargin
	def getCombPosition(self):
		return self.CombPosition
	def getCombLongFrozen(self):
		return self.CombLongFrozen
	def getCombShortFrozen(self):
		return self.CombShortFrozen
	def getCloseProfitByDate(self):
		return self.CloseProfitByDate
	def getCloseProfitByTrade(self):
		return self.CloseProfitByTrade
	def getTodayPosition(self):
		return self.TodayPosition
	def getMarginRateByMoney(self):
		return self.MarginRateByMoney
	def getMarginRateByVolume(self):
		return self.MarginRateByVolume
	def getStrikeFrozen(self):
		return self.StrikeFrozen
	def getStrikeFrozenAmount(self):
		return self.StrikeFrozenAmount
	def getAbandonFrozen(self):
		return self.AbandonFrozen

class CThostFtdcSyncingInstrumentMarginRateField(Structure):
	"""正在同步中的合约保证金率"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#投资者范围
		("InvestorRange",c_char),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#投机套保标志
		("HedgeFlag",c_char),
		#多头保证金率
		("LongMarginRatioByMoney",c_double),
		#多头保证金费
		("LongMarginRatioByVolume",c_double),
		#空头保证金率
		("ShortMarginRatioByMoney",c_double),
		#空头保证金费
		("ShortMarginRatioByVolume",c_double),
		#是否相对交易所收取
		("IsRelative",c_int32),
		]

	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getLongMarginRatioByMoney(self):
		return self.LongMarginRatioByMoney
	def getLongMarginRatioByVolume(self):
		return self.LongMarginRatioByVolume
	def getShortMarginRatioByMoney(self):
		return self.ShortMarginRatioByMoney
	def getShortMarginRatioByVolume(self):
		return self.ShortMarginRatioByVolume
	def getIsRelative(self):
		return self.IsRelative

class CThostFtdcSyncingInstrumentCommissionRateField(Structure):
	"""正在同步中的合约手续费率"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#投资者范围
		("InvestorRange",c_char),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#开仓手续费率
		("OpenRatioByMoney",c_double),
		#开仓手续费
		("OpenRatioByVolume",c_double),
		#平仓手续费率
		("CloseRatioByMoney",c_double),
		#平仓手续费
		("CloseRatioByVolume",c_double),
		#平今手续费率
		("CloseTodayRatioByMoney",c_double),
		#平今手续费
		("CloseTodayRatioByVolume",c_double),
		]

	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getOpenRatioByMoney(self):
		return self.OpenRatioByMoney
	def getOpenRatioByVolume(self):
		return self.OpenRatioByVolume
	def getCloseRatioByMoney(self):
		return self.CloseRatioByMoney
	def getCloseRatioByVolume(self):
		return self.CloseRatioByVolume
	def getCloseTodayRatioByMoney(self):
		return self.CloseTodayRatioByMoney
	def getCloseTodayRatioByVolume(self):
		return self.CloseTodayRatioByVolume

class CThostFtdcSyncingInstrumentTradingRightField(Structure):
	"""正在同步中的合约交易权限"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#投资者范围
		("InvestorRange",c_char),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#交易权限
		("TradingRight",c_char),
		]

	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getTradingRight(self):
		return TradingRightType(ord(self.TradingRight))

class CThostFtdcQryOrderField(Structure):
	"""查询报单"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#报单编号
		("OrderSysID",c_char*21),
		#开始时间
		("InsertTimeStart",c_char*9),
		#结束时间
		("InsertTimeEnd",c_char*9),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getOrderSysID(self):
		return self.OrderSysID.decode('ascii')
	def getInsertTimeStart(self):
		return self.InsertTimeStart.decode('ascii')
	def getInsertTimeEnd(self):
		return self.InsertTimeEnd.decode('ascii')

class CThostFtdcQryTradeField(Structure):
	"""查询成交"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#成交编号
		("TradeID",c_char*21),
		#开始时间
		("TradeTimeStart",c_char*9),
		#结束时间
		("TradeTimeEnd",c_char*9),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getTradeID(self):
		return self.TradeID.decode('ascii')
	def getTradeTimeStart(self):
		return self.TradeTimeStart.decode('ascii')
	def getTradeTimeEnd(self):
		return self.TradeTimeEnd.decode('ascii')

class CThostFtdcQryInvestorPositionField(Structure):
	"""查询投资者持仓"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')

class CThostFtdcQryTradingAccountField(Structure):
	"""查询资金账户"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#币种代码
		("CurrencyID",c_char*4),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')

class CThostFtdcQryInvestorField(Structure):
	"""查询投资者"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')

class CThostFtdcQryTradingCodeField(Structure):
	"""查询交易编码"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		#客户代码
		("ClientID",c_char*11),
		#交易编码类型
		("ClientIDType",c_char),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getClientID(self):
		return self.ClientID.decode('ascii')
	def getClientIDType(self):
		return ClientIDTypeType(ord(self.ClientIDType))

class CThostFtdcQryInvestorGroupField(Structure):
	"""查询投资者组"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')

class CThostFtdcQryInstrumentMarginRateField(Structure):
	"""查询合约保证金率"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#投机套保标志
		("HedgeFlag",c_char),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))

class CThostFtdcQryInstrumentCommissionRateField(Structure):
	"""查询手续费率"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')

class CThostFtdcQryInstrumentTradingRightField(Structure):
	"""查询合约交易权限"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')

class CThostFtdcQryBrokerField(Structure):
	"""查询经纪公司"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')

class CThostFtdcQryTraderField(Structure):
	"""查询交易员"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#交易所交易员代码
		("TraderID",c_char*21),
		]

	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')

class CThostFtdcQrySuperUserFunctionField(Structure):
	"""查询管理用户功能权限"""
	_fields_ = [
		#用户代码
		("UserID",c_char*16),
		]

	def getUserID(self):
		return self.UserID.decode('ascii')

class CThostFtdcQryUserSessionField(Structure):
	"""查询用户会话"""
	_fields_ = [
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		]

	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')

class CThostFtdcQryPartBrokerField(Structure):
	"""查询经纪公司会员代码"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#经纪公司代码
		("BrokerID",c_char*11),
		#会员代码
		("ParticipantID",c_char*11),
		]

	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')

class CThostFtdcQryFrontStatusField(Structure):
	"""查询前置状态"""
	_fields_ = [
		#前置编号
		("FrontID",c_int32),
		]

	def getFrontID(self):
		return self.FrontID

class CThostFtdcQryExchangeOrderField(Structure):
	"""查询交易所报单"""
	_fields_ = [
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		]

	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getClientID(self):
		return self.ClientID.decode('ascii')
	def getExchangeInstID(self):
		return self.ExchangeInstID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')

class CThostFtdcQryOrderActionField(Structure):
	"""查询报单操作"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')

class CThostFtdcQryExchangeOrderActionField(Structure):
	"""查询交易所报单操作"""
	_fields_ = [
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#交易所代码
		("ExchangeID",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		]

	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getClientID(self):
		return self.ClientID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')

class CThostFtdcQrySuperUserField(Structure):
	"""查询管理用户"""
	_fields_ = [
		#用户代码
		("UserID",c_char*16),
		]

	def getUserID(self):
		return self.UserID.decode('ascii')

class CThostFtdcQryExchangeField(Structure):
	"""查询交易所"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		]

	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')

class CThostFtdcQryProductField(Structure):
	"""查询产品"""
	_fields_ = [
		#产品代码
		("ProductID",c_char*31),
		#产品类型
		("ProductClass",c_char),
		]

	def getProductID(self):
		return self.ProductID.decode('ascii')
	def getProductClass(self):
		return ProductClassType(ord(self.ProductClass))

class CThostFtdcQryInstrumentField(Structure):
	"""查询合约"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#产品代码
		("ProductID",c_char*31),
		]

	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getExchangeInstID(self):
		return self.ExchangeInstID.decode('ascii')
	def getProductID(self):
		return self.ProductID.decode('ascii')

class CThostFtdcQryDepthMarketDataField(Structure):
	"""查询行情"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')

class CThostFtdcQryBrokerUserField(Structure):
	"""查询经纪公司用户"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')

class CThostFtdcQryBrokerUserFunctionField(Structure):
	"""查询经纪公司用户权限"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')

class CThostFtdcQryTraderOfferField(Structure):
	"""查询交易员报盘机"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#交易所交易员代码
		("TraderID",c_char*21),
		]

	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')

class CThostFtdcQrySyncDepositField(Structure):
	"""查询出入金流水"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#出入金流水号
		("DepositSeqNo",c_char*15),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getDepositSeqNo(self):
		return self.DepositSeqNo.decode('ascii')

class CThostFtdcQrySettlementInfoField(Structure):
	"""查询投资者结算结果"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#交易日
		("TradingDay",c_char*9),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')

class CThostFtdcQryExchangeMarginRateField(Structure):
	"""查询交易所保证金率"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#合约代码
		("InstrumentID",c_char*31),
		#投机套保标志
		("HedgeFlag",c_char),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))

class CThostFtdcQryExchangeMarginRateAdjustField(Structure):
	"""查询交易所调整保证金率"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#合约代码
		("InstrumentID",c_char*31),
		#投机套保标志
		("HedgeFlag",c_char),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))

class CThostFtdcQryExchangeRateField(Structure):
	"""查询汇率"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#源币种
		("FromCurrencyID",c_char*4),
		#目标币种
		("ToCurrencyID",c_char*4),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getFromCurrencyID(self):
		return self.FromCurrencyID.decode('ascii')
	def getToCurrencyID(self):
		return self.ToCurrencyID.decode('ascii')

class CThostFtdcQrySyncFundMortgageField(Structure):
	"""查询货币质押流水"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#货币质押流水号
		("MortgageSeqNo",c_char*15),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getMortgageSeqNo(self):
		return self.MortgageSeqNo.decode('ascii')

class CThostFtdcQryHisOrderField(Structure):
	"""查询报单"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#报单编号
		("OrderSysID",c_char*21),
		#开始时间
		("InsertTimeStart",c_char*9),
		#结束时间
		("InsertTimeEnd",c_char*9),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getOrderSysID(self):
		return self.OrderSysID.decode('ascii')
	def getInsertTimeStart(self):
		return self.InsertTimeStart.decode('ascii')
	def getInsertTimeEnd(self):
		return self.InsertTimeEnd.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getSettlementID(self):
		return self.SettlementID

class CThostFtdcOptionInstrMiniMarginField(Structure):
	"""当前期权合约最小保证金"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#投资者范围
		("InvestorRange",c_char),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#单位（手）期权合约最小保证金
		("MinMargin",c_double),
		#取值方式
		("ValueMethod",c_char),
		#是否跟随交易所收取
		("IsRelative",c_int32),
		]

	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getMinMargin(self):
		return self.MinMargin
	def getValueMethod(self):
		return ValueMethodType(ord(self.ValueMethod))
	def getIsRelative(self):
		return self.IsRelative

class CThostFtdcOptionInstrMarginAdjustField(Structure):
	"""当前期权合约保证金调整系数"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#投资者范围
		("InvestorRange",c_char),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#投机空头保证金调整系数
		("SShortMarginRatioByMoney",c_double),
		#投机空头保证金调整系数
		("SShortMarginRatioByVolume",c_double),
		#保值空头保证金调整系数
		("HShortMarginRatioByMoney",c_double),
		#保值空头保证金调整系数
		("HShortMarginRatioByVolume",c_double),
		#套利空头保证金调整系数
		("AShortMarginRatioByMoney",c_double),
		#套利空头保证金调整系数
		("AShortMarginRatioByVolume",c_double),
		#是否跟随交易所收取
		("IsRelative",c_int32),
		]

	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getSShortMarginRatioByMoney(self):
		return self.SShortMarginRatioByMoney
	def getSShortMarginRatioByVolume(self):
		return self.SShortMarginRatioByVolume
	def getHShortMarginRatioByMoney(self):
		return self.HShortMarginRatioByMoney
	def getHShortMarginRatioByVolume(self):
		return self.HShortMarginRatioByVolume
	def getAShortMarginRatioByMoney(self):
		return self.AShortMarginRatioByMoney
	def getAShortMarginRatioByVolume(self):
		return self.AShortMarginRatioByVolume
	def getIsRelative(self):
		return self.IsRelative

class CThostFtdcOptionInstrCommRateField(Structure):
	"""当前期权合约手续费的详细内容"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#投资者范围
		("InvestorRange",c_char),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#开仓手续费率
		("OpenRatioByMoney",c_double),
		#开仓手续费
		("OpenRatioByVolume",c_double),
		#平仓手续费率
		("CloseRatioByMoney",c_double),
		#平仓手续费
		("CloseRatioByVolume",c_double),
		#平今手续费率
		("CloseTodayRatioByMoney",c_double),
		#平今手续费
		("CloseTodayRatioByVolume",c_double),
		#执行手续费率
		("StrikeRatioByMoney",c_double),
		#执行手续费
		("StrikeRatioByVolume",c_double),
		]

	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getOpenRatioByMoney(self):
		return self.OpenRatioByMoney
	def getOpenRatioByVolume(self):
		return self.OpenRatioByVolume
	def getCloseRatioByMoney(self):
		return self.CloseRatioByMoney
	def getCloseRatioByVolume(self):
		return self.CloseRatioByVolume
	def getCloseTodayRatioByMoney(self):
		return self.CloseTodayRatioByMoney
	def getCloseTodayRatioByVolume(self):
		return self.CloseTodayRatioByVolume
	def getStrikeRatioByMoney(self):
		return self.StrikeRatioByMoney
	def getStrikeRatioByVolume(self):
		return self.StrikeRatioByVolume

class CThostFtdcOptionInstrTradeCostField(Structure):
	"""期权交易成本"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#投机套保标志
		("HedgeFlag",c_char),
		#期权合约保证金不变部分
		("FixedMargin",c_double),
		#期权合约最小保证金
		("MiniMargin",c_double),
		#期权合约权利金
		("Royalty",c_double),
		#交易所期权合约保证金不变部分
		("ExchFixedMargin",c_double),
		#交易所期权合约最小保证金
		("ExchMiniMargin",c_double),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getFixedMargin(self):
		return self.FixedMargin
	def getMiniMargin(self):
		return self.MiniMargin
	def getRoyalty(self):
		return self.Royalty
	def getExchFixedMargin(self):
		return self.ExchFixedMargin
	def getExchMiniMargin(self):
		return self.ExchMiniMargin

class CThostFtdcQryOptionInstrTradeCostField(Structure):
	"""期权交易成本查询"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#投机套保标志
		("HedgeFlag",c_char),
		#期权合约报价
		("InputPrice",c_double),
		#标的价格,填0则用昨结算价
		("UnderlyingPrice",c_double),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getInputPrice(self):
		return self.InputPrice
	def getUnderlyingPrice(self):
		return self.UnderlyingPrice

class CThostFtdcQryOptionInstrCommRateField(Structure):
	"""期权手续费率查询"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')

class CThostFtdcIndexPriceField(Structure):
	"""股指现货指数"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#合约代码
		("InstrumentID",c_char*31),
		#指数现货收盘价
		("ClosePrice",c_double),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getClosePrice(self):
		return self.ClosePrice

class CThostFtdcInputExecOrderField(Structure):
	"""输入的执行宣告"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#执行宣告引用
		("ExecOrderRef",c_char*13),
		#用户代码
		("UserID",c_char*16),
		#数量
		("Volume",c_int32),
		#请求编号
		("RequestID",c_int32),
		#业务单元
		("BusinessUnit",c_char*21),
		#开平标志
		("OffsetFlag",c_char),
		#投机套保标志
		("HedgeFlag",c_char),
		#执行类型
		("ActionType",c_char),
		#保留头寸申请的持仓方向
		("PosiDirection",c_char),
		#期权行权后是否保留期货头寸的标记
		("ReservePositionFlag",c_char),
		#期权行权后生成的头寸是否自动平仓
		("CloseFlag",c_char),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getExecOrderRef(self):
		return self.ExecOrderRef.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getVolume(self):
		return self.Volume
	def getRequestID(self):
		return self.RequestID
	def getBusinessUnit(self):
		return self.BusinessUnit.decode('ascii')
	def getOffsetFlag(self):
		return OffsetFlagType(ord(self.OffsetFlag))
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getActionType(self):
		return ActionTypeType(ord(self.ActionType))
	def getPosiDirection(self):
		return PosiDirectionType(ord(self.PosiDirection))
	def getReservePositionFlag(self):
		return ExecOrderPositionFlagType(ord(self.ReservePositionFlag))
	def getCloseFlag(self):
		return ExecOrderCloseFlagType(ord(self.CloseFlag))

class CThostFtdcInputExecOrderActionField(Structure):
	"""输入执行宣告操作"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#执行宣告操作引用
		("ExecOrderActionRef",c_int32),
		#执行宣告引用
		("ExecOrderRef",c_char*13),
		#请求编号
		("RequestID",c_int32),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#交易所代码
		("ExchangeID",c_char*9),
		#执行宣告操作编号
		("ExecOrderSysID",c_char*21),
		#操作标志
		("ActionFlag",c_char),
		#用户代码
		("UserID",c_char*16),
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getExecOrderActionRef(self):
		return self.ExecOrderActionRef
	def getExecOrderRef(self):
		return self.ExecOrderRef.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getExecOrderSysID(self):
		return self.ExecOrderSysID.decode('ascii')
	def getActionFlag(self):
		return ActionFlagType(ord(self.ActionFlag))
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')

class CThostFtdcExecOrderField(Structure):
	"""执行宣告"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#执行宣告引用
		("ExecOrderRef",c_char*13),
		#用户代码
		("UserID",c_char*16),
		#数量
		("Volume",c_int32),
		#请求编号
		("RequestID",c_int32),
		#业务单元
		("BusinessUnit",c_char*21),
		#开平标志
		("OffsetFlag",c_char),
		#投机套保标志
		("HedgeFlag",c_char),
		#执行类型
		("ActionType",c_char),
		#保留头寸申请的持仓方向
		("PosiDirection",c_char),
		#期权行权后是否保留期货头寸的标记
		("ReservePositionFlag",c_char),
		#期权行权后生成的头寸是否自动平仓
		("CloseFlag",c_char),
		#本地执行宣告编号
		("ExecOrderLocalID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#执行宣告提交状态
		("OrderSubmitStatus",c_char),
		#报单提示序号
		("NotifySequence",c_int32),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#执行宣告编号
		("ExecOrderSysID",c_char*21),
		#报单日期
		("InsertDate",c_char*9),
		#插入时间
		("InsertTime",c_char*9),
		#撤销时间
		("CancelTime",c_char*9),
		#执行结果
		("ExecResult",c_char),
		#结算会员编号
		("ClearingPartID",c_char*11),
		#序号
		("SequenceNo",c_int32),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#用户端产品信息
		("UserProductInfo",c_char*11),
		#状态信息
		("StatusMsg",c_char*81),
		#操作用户代码
		("ActiveUserID",c_char*16),
		#经纪公司报单编号
		("BrokerExecOrderSeq",c_int32),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getExecOrderRef(self):
		return self.ExecOrderRef.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getVolume(self):
		return self.Volume
	def getRequestID(self):
		return self.RequestID
	def getBusinessUnit(self):
		return self.BusinessUnit.decode('ascii')
	def getOffsetFlag(self):
		return OffsetFlagType(ord(self.OffsetFlag))
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getActionType(self):
		return ActionTypeType(ord(self.ActionType))
	def getPosiDirection(self):
		return PosiDirectionType(ord(self.PosiDirection))
	def getReservePositionFlag(self):
		return ExecOrderPositionFlagType(ord(self.ReservePositionFlag))
	def getCloseFlag(self):
		return ExecOrderCloseFlagType(ord(self.CloseFlag))
	def getExecOrderLocalID(self):
		return self.ExecOrderLocalID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getClientID(self):
		return self.ClientID.decode('ascii')
	def getExchangeInstID(self):
		return self.ExchangeInstID.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')
	def getInstallID(self):
		return self.InstallID
	def getOrderSubmitStatus(self):
		return OrderSubmitStatusType(ord(self.OrderSubmitStatus))
	def getNotifySequence(self):
		return self.NotifySequence
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getSettlementID(self):
		return self.SettlementID
	def getExecOrderSysID(self):
		return self.ExecOrderSysID.decode('ascii')
	def getInsertDate(self):
		return self.InsertDate.decode('ascii')
	def getInsertTime(self):
		return self.InsertTime.decode('ascii')
	def getCancelTime(self):
		return self.CancelTime.decode('ascii')
	def getExecResult(self):
		return ExecResultType(ord(self.ExecResult))
	def getClearingPartID(self):
		return self.ClearingPartID.decode('ascii')
	def getSequenceNo(self):
		return self.SequenceNo
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getUserProductInfo(self):
		return self.UserProductInfo.decode('ascii')
	def getStatusMsg(self):
		return self.StatusMsg.decode('GB2312')
	def getActiveUserID(self):
		return self.ActiveUserID.decode('ascii')
	def getBrokerExecOrderSeq(self):
		return self.BrokerExecOrderSeq

class CThostFtdcExecOrderActionField(Structure):
	"""执行宣告操作"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#执行宣告操作引用
		("ExecOrderActionRef",c_int32),
		#执行宣告引用
		("ExecOrderRef",c_char*13),
		#请求编号
		("RequestID",c_int32),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#交易所代码
		("ExchangeID",c_char*9),
		#执行宣告操作编号
		("ExecOrderSysID",c_char*21),
		#操作标志
		("ActionFlag",c_char),
		#操作日期
		("ActionDate",c_char*9),
		#操作时间
		("ActionTime",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#本地执行宣告编号
		("ExecOrderLocalID",c_char*13),
		#操作本地编号
		("ActionLocalID",c_char*13),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#业务单元
		("BusinessUnit",c_char*21),
		#报单操作状态
		("OrderActionStatus",c_char),
		#用户代码
		("UserID",c_char*16),
		#执行类型
		("ActionType",c_char),
		#状态信息
		("StatusMsg",c_char*81),
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getExecOrderActionRef(self):
		return self.ExecOrderActionRef
	def getExecOrderRef(self):
		return self.ExecOrderRef.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getExecOrderSysID(self):
		return self.ExecOrderSysID.decode('ascii')
	def getActionFlag(self):
		return ActionFlagType(ord(self.ActionFlag))
	def getActionDate(self):
		return self.ActionDate.decode('ascii')
	def getActionTime(self):
		return self.ActionTime.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')
	def getInstallID(self):
		return self.InstallID
	def getExecOrderLocalID(self):
		return self.ExecOrderLocalID.decode('ascii')
	def getActionLocalID(self):
		return self.ActionLocalID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getClientID(self):
		return self.ClientID.decode('ascii')
	def getBusinessUnit(self):
		return self.BusinessUnit.decode('ascii')
	def getOrderActionStatus(self):
		return OrderActionStatusType(ord(self.OrderActionStatus))
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getActionType(self):
		return ActionTypeType(ord(self.ActionType))
	def getStatusMsg(self):
		return self.StatusMsg.decode('GB2312')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')

class CThostFtdcQryExecOrderField(Structure):
	"""执行宣告查询"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#执行宣告编号
		("ExecOrderSysID",c_char*21),
		#开始时间
		("InsertTimeStart",c_char*9),
		#结束时间
		("InsertTimeEnd",c_char*9),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getExecOrderSysID(self):
		return self.ExecOrderSysID.decode('ascii')
	def getInsertTimeStart(self):
		return self.InsertTimeStart.decode('ascii')
	def getInsertTimeEnd(self):
		return self.InsertTimeEnd.decode('ascii')

class CThostFtdcExchangeExecOrderField(Structure):
	"""交易所执行宣告信息"""
	_fields_ = [
		#数量
		("Volume",c_int32),
		#请求编号
		("RequestID",c_int32),
		#业务单元
		("BusinessUnit",c_char*21),
		#开平标志
		("OffsetFlag",c_char),
		#投机套保标志
		("HedgeFlag",c_char),
		#执行类型
		("ActionType",c_char),
		#保留头寸申请的持仓方向
		("PosiDirection",c_char),
		#期权行权后是否保留期货头寸的标记
		("ReservePositionFlag",c_char),
		#期权行权后生成的头寸是否自动平仓
		("CloseFlag",c_char),
		#本地执行宣告编号
		("ExecOrderLocalID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#执行宣告提交状态
		("OrderSubmitStatus",c_char),
		#报单提示序号
		("NotifySequence",c_int32),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#执行宣告编号
		("ExecOrderSysID",c_char*21),
		#报单日期
		("InsertDate",c_char*9),
		#插入时间
		("InsertTime",c_char*9),
		#撤销时间
		("CancelTime",c_char*9),
		#执行结果
		("ExecResult",c_char),
		#结算会员编号
		("ClearingPartID",c_char*11),
		#序号
		("SequenceNo",c_int32),
		]

	def getVolume(self):
		return self.Volume
	def getRequestID(self):
		return self.RequestID
	def getBusinessUnit(self):
		return self.BusinessUnit.decode('ascii')
	def getOffsetFlag(self):
		return OffsetFlagType(ord(self.OffsetFlag))
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getActionType(self):
		return ActionTypeType(ord(self.ActionType))
	def getPosiDirection(self):
		return PosiDirectionType(ord(self.PosiDirection))
	def getReservePositionFlag(self):
		return ExecOrderPositionFlagType(ord(self.ReservePositionFlag))
	def getCloseFlag(self):
		return ExecOrderCloseFlagType(ord(self.CloseFlag))
	def getExecOrderLocalID(self):
		return self.ExecOrderLocalID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getClientID(self):
		return self.ClientID.decode('ascii')
	def getExchangeInstID(self):
		return self.ExchangeInstID.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')
	def getInstallID(self):
		return self.InstallID
	def getOrderSubmitStatus(self):
		return OrderSubmitStatusType(ord(self.OrderSubmitStatus))
	def getNotifySequence(self):
		return self.NotifySequence
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getSettlementID(self):
		return self.SettlementID
	def getExecOrderSysID(self):
		return self.ExecOrderSysID.decode('ascii')
	def getInsertDate(self):
		return self.InsertDate.decode('ascii')
	def getInsertTime(self):
		return self.InsertTime.decode('ascii')
	def getCancelTime(self):
		return self.CancelTime.decode('ascii')
	def getExecResult(self):
		return ExecResultType(ord(self.ExecResult))
	def getClearingPartID(self):
		return self.ClearingPartID.decode('ascii')
	def getSequenceNo(self):
		return self.SequenceNo

class CThostFtdcQryExchangeExecOrderField(Structure):
	"""交易所执行宣告查询"""
	_fields_ = [
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		]

	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getClientID(self):
		return self.ClientID.decode('ascii')
	def getExchangeInstID(self):
		return self.ExchangeInstID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')

class CThostFtdcQryExecOrderActionField(Structure):
	"""执行宣告操作查询"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')

class CThostFtdcExchangeExecOrderActionField(Structure):
	"""交易所执行宣告操作"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#执行宣告操作编号
		("ExecOrderSysID",c_char*21),
		#操作标志
		("ActionFlag",c_char),
		#操作日期
		("ActionDate",c_char*9),
		#操作时间
		("ActionTime",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#本地执行宣告编号
		("ExecOrderLocalID",c_char*13),
		#操作本地编号
		("ActionLocalID",c_char*13),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#业务单元
		("BusinessUnit",c_char*21),
		#报单操作状态
		("OrderActionStatus",c_char),
		#用户代码
		("UserID",c_char*16),
		#执行类型
		("ActionType",c_char),
		]

	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getExecOrderSysID(self):
		return self.ExecOrderSysID.decode('ascii')
	def getActionFlag(self):
		return ActionFlagType(ord(self.ActionFlag))
	def getActionDate(self):
		return self.ActionDate.decode('ascii')
	def getActionTime(self):
		return self.ActionTime.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')
	def getInstallID(self):
		return self.InstallID
	def getExecOrderLocalID(self):
		return self.ExecOrderLocalID.decode('ascii')
	def getActionLocalID(self):
		return self.ActionLocalID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getClientID(self):
		return self.ClientID.decode('ascii')
	def getBusinessUnit(self):
		return self.BusinessUnit.decode('ascii')
	def getOrderActionStatus(self):
		return OrderActionStatusType(ord(self.OrderActionStatus))
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getActionType(self):
		return ActionTypeType(ord(self.ActionType))

class CThostFtdcQryExchangeExecOrderActionField(Structure):
	"""交易所执行宣告操作查询"""
	_fields_ = [
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#交易所代码
		("ExchangeID",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		]

	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getClientID(self):
		return self.ClientID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')

class CThostFtdcErrExecOrderField(Structure):
	"""错误执行宣告"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#执行宣告引用
		("ExecOrderRef",c_char*13),
		#用户代码
		("UserID",c_char*16),
		#数量
		("Volume",c_int32),
		#请求编号
		("RequestID",c_int32),
		#业务单元
		("BusinessUnit",c_char*21),
		#开平标志
		("OffsetFlag",c_char),
		#投机套保标志
		("HedgeFlag",c_char),
		#执行类型
		("ActionType",c_char),
		#保留头寸申请的持仓方向
		("PosiDirection",c_char),
		#期权行权后是否保留期货头寸的标记
		("ReservePositionFlag",c_char),
		#期权行权后生成的头寸是否自动平仓
		("CloseFlag",c_char),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getExecOrderRef(self):
		return self.ExecOrderRef.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getVolume(self):
		return self.Volume
	def getRequestID(self):
		return self.RequestID
	def getBusinessUnit(self):
		return self.BusinessUnit.decode('ascii')
	def getOffsetFlag(self):
		return OffsetFlagType(ord(self.OffsetFlag))
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getActionType(self):
		return ActionTypeType(ord(self.ActionType))
	def getPosiDirection(self):
		return PosiDirectionType(ord(self.PosiDirection))
	def getReservePositionFlag(self):
		return ExecOrderPositionFlagType(ord(self.ReservePositionFlag))
	def getCloseFlag(self):
		return ExecOrderCloseFlagType(ord(self.CloseFlag))
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return self.ErrorMsg.decode('GB2312')

class CThostFtdcQryErrExecOrderField(Structure):
	"""查询错误执行宣告"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')

class CThostFtdcErrExecOrderActionField(Structure):
	"""错误执行宣告操作"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#执行宣告操作引用
		("ExecOrderActionRef",c_int32),
		#执行宣告引用
		("ExecOrderRef",c_char*13),
		#请求编号
		("RequestID",c_int32),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#交易所代码
		("ExchangeID",c_char*9),
		#执行宣告操作编号
		("ExecOrderSysID",c_char*21),
		#操作标志
		("ActionFlag",c_char),
		#用户代码
		("UserID",c_char*16),
		#合约代码
		("InstrumentID",c_char*31),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getExecOrderActionRef(self):
		return self.ExecOrderActionRef
	def getExecOrderRef(self):
		return self.ExecOrderRef.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getExecOrderSysID(self):
		return self.ExecOrderSysID.decode('ascii')
	def getActionFlag(self):
		return ActionFlagType(ord(self.ActionFlag))
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return self.ErrorMsg.decode('GB2312')

class CThostFtdcQryErrExecOrderActionField(Structure):
	"""查询错误执行宣告操作"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')

class CThostFtdcOptionInstrTradingRightField(Structure):
	"""投资者期权合约交易权限"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#投资者范围
		("InvestorRange",c_char),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#买卖方向
		("Direction",c_char),
		#交易权限
		("TradingRight",c_char),
		]

	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getTradingRight(self):
		return TradingRightType(ord(self.TradingRight))

class CThostFtdcQryOptionInstrTradingRightField(Structure):
	"""查询期权合约交易权限"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#买卖方向
		("Direction",c_char),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getDirection(self):
		return DirectionType(ord(self.Direction))

class CThostFtdcInputForQuoteField(Structure):
	"""输入的询价"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#询价引用
		("ForQuoteRef",c_char*13),
		#用户代码
		("UserID",c_char*16),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getForQuoteRef(self):
		return self.ForQuoteRef.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')

class CThostFtdcForQuoteField(Structure):
	"""询价"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#询价引用
		("ForQuoteRef",c_char*13),
		#用户代码
		("UserID",c_char*16),
		#本地询价编号
		("ForQuoteLocalID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#报单日期
		("InsertDate",c_char*9),
		#插入时间
		("InsertTime",c_char*9),
		#询价状态
		("ForQuoteStatus",c_char),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#状态信息
		("StatusMsg",c_char*81),
		#操作用户代码
		("ActiveUserID",c_char*16),
		#经纪公司询价编号
		("BrokerForQutoSeq",c_int32),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getForQuoteRef(self):
		return self.ForQuoteRef.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getForQuoteLocalID(self):
		return self.ForQuoteLocalID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getClientID(self):
		return self.ClientID.decode('ascii')
	def getExchangeInstID(self):
		return self.ExchangeInstID.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')
	def getInstallID(self):
		return self.InstallID
	def getInsertDate(self):
		return self.InsertDate.decode('ascii')
	def getInsertTime(self):
		return self.InsertTime.decode('ascii')
	def getForQuoteStatus(self):
		return ForQuoteStatusType(ord(self.ForQuoteStatus))
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getStatusMsg(self):
		return self.StatusMsg.decode('GB2312')
	def getActiveUserID(self):
		return self.ActiveUserID.decode('ascii')
	def getBrokerForQutoSeq(self):
		return self.BrokerForQutoSeq

class CThostFtdcQryForQuoteField(Structure):
	"""询价查询"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#开始时间
		("InsertTimeStart",c_char*9),
		#结束时间
		("InsertTimeEnd",c_char*9),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getInsertTimeStart(self):
		return self.InsertTimeStart.decode('ascii')
	def getInsertTimeEnd(self):
		return self.InsertTimeEnd.decode('ascii')

class CThostFtdcExchangeForQuoteField(Structure):
	"""交易所询价信息"""
	_fields_ = [
		#本地询价编号
		("ForQuoteLocalID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#报单日期
		("InsertDate",c_char*9),
		#插入时间
		("InsertTime",c_char*9),
		#询价状态
		("ForQuoteStatus",c_char),
		]

	def getForQuoteLocalID(self):
		return self.ForQuoteLocalID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getClientID(self):
		return self.ClientID.decode('ascii')
	def getExchangeInstID(self):
		return self.ExchangeInstID.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')
	def getInstallID(self):
		return self.InstallID
	def getInsertDate(self):
		return self.InsertDate.decode('ascii')
	def getInsertTime(self):
		return self.InsertTime.decode('ascii')
	def getForQuoteStatus(self):
		return ForQuoteStatusType(ord(self.ForQuoteStatus))

class CThostFtdcQryExchangeForQuoteField(Structure):
	"""交易所询价查询"""
	_fields_ = [
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		]

	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getClientID(self):
		return self.ClientID.decode('ascii')
	def getExchangeInstID(self):
		return self.ExchangeInstID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')

class CThostFtdcInputQuoteField(Structure):
	"""输入的报价"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#报价引用
		("QuoteRef",c_char*13),
		#用户代码
		("UserID",c_char*16),
		#卖价格
		("AskPrice",c_double),
		#买价格
		("BidPrice",c_double),
		#卖数量
		("AskVolume",c_int32),
		#买数量
		("BidVolume",c_int32),
		#请求编号
		("RequestID",c_int32),
		#业务单元
		("BusinessUnit",c_char*21),
		#卖开平标志
		("AskOffsetFlag",c_char),
		#买开平标志
		("BidOffsetFlag",c_char),
		#卖投机套保标志
		("AskHedgeFlag",c_char),
		#买投机套保标志
		("BidHedgeFlag",c_char),
		#衍生卖报单引用
		("AskOrderRef",c_char*13),
		#衍生买报单引用
		("BidOrderRef",c_char*13),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getQuoteRef(self):
		return self.QuoteRef.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getAskPrice(self):
		return self.AskPrice
	def getBidPrice(self):
		return self.BidPrice
	def getAskVolume(self):
		return self.AskVolume
	def getBidVolume(self):
		return self.BidVolume
	def getRequestID(self):
		return self.RequestID
	def getBusinessUnit(self):
		return self.BusinessUnit.decode('ascii')
	def getAskOffsetFlag(self):
		return OffsetFlagType(ord(self.AskOffsetFlag))
	def getBidOffsetFlag(self):
		return OffsetFlagType(ord(self.BidOffsetFlag))
	def getAskHedgeFlag(self):
		return HedgeFlagType(ord(self.AskHedgeFlag))
	def getBidHedgeFlag(self):
		return HedgeFlagType(ord(self.BidHedgeFlag))
	def getAskOrderRef(self):
		return self.AskOrderRef.decode('ascii')
	def getBidOrderRef(self):
		return self.BidOrderRef.decode('ascii')

class CThostFtdcInputQuoteActionField(Structure):
	"""输入报价操作"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#报价操作引用
		("QuoteActionRef",c_int32),
		#报价引用
		("QuoteRef",c_char*13),
		#请求编号
		("RequestID",c_int32),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#交易所代码
		("ExchangeID",c_char*9),
		#报价操作编号
		("QuoteSysID",c_char*21),
		#操作标志
		("ActionFlag",c_char),
		#用户代码
		("UserID",c_char*16),
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getQuoteActionRef(self):
		return self.QuoteActionRef
	def getQuoteRef(self):
		return self.QuoteRef.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getQuoteSysID(self):
		return self.QuoteSysID.decode('ascii')
	def getActionFlag(self):
		return ActionFlagType(ord(self.ActionFlag))
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')

class CThostFtdcQuoteField(Structure):
	"""报价"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#报价引用
		("QuoteRef",c_char*13),
		#用户代码
		("UserID",c_char*16),
		#卖价格
		("AskPrice",c_double),
		#买价格
		("BidPrice",c_double),
		#卖数量
		("AskVolume",c_int32),
		#买数量
		("BidVolume",c_int32),
		#请求编号
		("RequestID",c_int32),
		#业务单元
		("BusinessUnit",c_char*21),
		#卖开平标志
		("AskOffsetFlag",c_char),
		#买开平标志
		("BidOffsetFlag",c_char),
		#卖投机套保标志
		("AskHedgeFlag",c_char),
		#买投机套保标志
		("BidHedgeFlag",c_char),
		#本地报价编号
		("QuoteLocalID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#报价提示序号
		("NotifySequence",c_int32),
		#报价提交状态
		("OrderSubmitStatus",c_char),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#报价编号
		("QuoteSysID",c_char*21),
		#报单日期
		("InsertDate",c_char*9),
		#插入时间
		("InsertTime",c_char*9),
		#撤销时间
		("CancelTime",c_char*9),
		#报价状态
		("QuoteStatus",c_char),
		#结算会员编号
		("ClearingPartID",c_char*11),
		#序号
		("SequenceNo",c_int32),
		#卖方报单编号
		("AskOrderSysID",c_char*21),
		#买方报单编号
		("BidOrderSysID",c_char*21),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#用户端产品信息
		("UserProductInfo",c_char*11),
		#状态信息
		("StatusMsg",c_char*81),
		#操作用户代码
		("ActiveUserID",c_char*16),
		#经纪公司报价编号
		("BrokerQuoteSeq",c_int32),
		#衍生卖报单引用
		("AskOrderRef",c_char*13),
		#衍生买报单引用
		("BidOrderRef",c_char*13),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getQuoteRef(self):
		return self.QuoteRef.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getAskPrice(self):
		return self.AskPrice
	def getBidPrice(self):
		return self.BidPrice
	def getAskVolume(self):
		return self.AskVolume
	def getBidVolume(self):
		return self.BidVolume
	def getRequestID(self):
		return self.RequestID
	def getBusinessUnit(self):
		return self.BusinessUnit.decode('ascii')
	def getAskOffsetFlag(self):
		return OffsetFlagType(ord(self.AskOffsetFlag))
	def getBidOffsetFlag(self):
		return OffsetFlagType(ord(self.BidOffsetFlag))
	def getAskHedgeFlag(self):
		return HedgeFlagType(ord(self.AskHedgeFlag))
	def getBidHedgeFlag(self):
		return HedgeFlagType(ord(self.BidHedgeFlag))
	def getQuoteLocalID(self):
		return self.QuoteLocalID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getClientID(self):
		return self.ClientID.decode('ascii')
	def getExchangeInstID(self):
		return self.ExchangeInstID.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')
	def getInstallID(self):
		return self.InstallID
	def getNotifySequence(self):
		return self.NotifySequence
	def getOrderSubmitStatus(self):
		return OrderSubmitStatusType(ord(self.OrderSubmitStatus))
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getSettlementID(self):
		return self.SettlementID
	def getQuoteSysID(self):
		return self.QuoteSysID.decode('ascii')
	def getInsertDate(self):
		return self.InsertDate.decode('ascii')
	def getInsertTime(self):
		return self.InsertTime.decode('ascii')
	def getCancelTime(self):
		return self.CancelTime.decode('ascii')
	def getQuoteStatus(self):
		return OrderStatusType(ord(self.QuoteStatus))
	def getClearingPartID(self):
		return self.ClearingPartID.decode('ascii')
	def getSequenceNo(self):
		return self.SequenceNo
	def getAskOrderSysID(self):
		return self.AskOrderSysID.decode('ascii')
	def getBidOrderSysID(self):
		return self.BidOrderSysID.decode('ascii')
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getUserProductInfo(self):
		return self.UserProductInfo.decode('ascii')
	def getStatusMsg(self):
		return self.StatusMsg.decode('GB2312')
	def getActiveUserID(self):
		return self.ActiveUserID.decode('ascii')
	def getBrokerQuoteSeq(self):
		return self.BrokerQuoteSeq
	def getAskOrderRef(self):
		return self.AskOrderRef.decode('ascii')
	def getBidOrderRef(self):
		return self.BidOrderRef.decode('ascii')

class CThostFtdcQuoteActionField(Structure):
	"""报价操作"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#报价操作引用
		("QuoteActionRef",c_int32),
		#报价引用
		("QuoteRef",c_char*13),
		#请求编号
		("RequestID",c_int32),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#交易所代码
		("ExchangeID",c_char*9),
		#报价操作编号
		("QuoteSysID",c_char*21),
		#操作标志
		("ActionFlag",c_char),
		#操作日期
		("ActionDate",c_char*9),
		#操作时间
		("ActionTime",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#本地报价编号
		("QuoteLocalID",c_char*13),
		#操作本地编号
		("ActionLocalID",c_char*13),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#业务单元
		("BusinessUnit",c_char*21),
		#报单操作状态
		("OrderActionStatus",c_char),
		#用户代码
		("UserID",c_char*16),
		#状态信息
		("StatusMsg",c_char*81),
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getQuoteActionRef(self):
		return self.QuoteActionRef
	def getQuoteRef(self):
		return self.QuoteRef.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getQuoteSysID(self):
		return self.QuoteSysID.decode('ascii')
	def getActionFlag(self):
		return ActionFlagType(ord(self.ActionFlag))
	def getActionDate(self):
		return self.ActionDate.decode('ascii')
	def getActionTime(self):
		return self.ActionTime.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')
	def getInstallID(self):
		return self.InstallID
	def getQuoteLocalID(self):
		return self.QuoteLocalID.decode('ascii')
	def getActionLocalID(self):
		return self.ActionLocalID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getClientID(self):
		return self.ClientID.decode('ascii')
	def getBusinessUnit(self):
		return self.BusinessUnit.decode('ascii')
	def getOrderActionStatus(self):
		return OrderActionStatusType(ord(self.OrderActionStatus))
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getStatusMsg(self):
		return self.StatusMsg.decode('GB2312')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')

class CThostFtdcQryQuoteField(Structure):
	"""报价查询"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#报价编号
		("QuoteSysID",c_char*21),
		#开始时间
		("InsertTimeStart",c_char*9),
		#结束时间
		("InsertTimeEnd",c_char*9),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getQuoteSysID(self):
		return self.QuoteSysID.decode('ascii')
	def getInsertTimeStart(self):
		return self.InsertTimeStart.decode('ascii')
	def getInsertTimeEnd(self):
		return self.InsertTimeEnd.decode('ascii')

class CThostFtdcExchangeQuoteField(Structure):
	"""交易所报价信息"""
	_fields_ = [
		#卖价格
		("AskPrice",c_double),
		#买价格
		("BidPrice",c_double),
		#卖数量
		("AskVolume",c_int32),
		#买数量
		("BidVolume",c_int32),
		#请求编号
		("RequestID",c_int32),
		#业务单元
		("BusinessUnit",c_char*21),
		#卖开平标志
		("AskOffsetFlag",c_char),
		#买开平标志
		("BidOffsetFlag",c_char),
		#卖投机套保标志
		("AskHedgeFlag",c_char),
		#买投机套保标志
		("BidHedgeFlag",c_char),
		#本地报价编号
		("QuoteLocalID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#报价提示序号
		("NotifySequence",c_int32),
		#报价提交状态
		("OrderSubmitStatus",c_char),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#报价编号
		("QuoteSysID",c_char*21),
		#报单日期
		("InsertDate",c_char*9),
		#插入时间
		("InsertTime",c_char*9),
		#撤销时间
		("CancelTime",c_char*9),
		#报价状态
		("QuoteStatus",c_char),
		#结算会员编号
		("ClearingPartID",c_char*11),
		#序号
		("SequenceNo",c_int32),
		#卖方报单编号
		("AskOrderSysID",c_char*21),
		#买方报单编号
		("BidOrderSysID",c_char*21),
		]

	def getAskPrice(self):
		return self.AskPrice
	def getBidPrice(self):
		return self.BidPrice
	def getAskVolume(self):
		return self.AskVolume
	def getBidVolume(self):
		return self.BidVolume
	def getRequestID(self):
		return self.RequestID
	def getBusinessUnit(self):
		return self.BusinessUnit.decode('ascii')
	def getAskOffsetFlag(self):
		return OffsetFlagType(ord(self.AskOffsetFlag))
	def getBidOffsetFlag(self):
		return OffsetFlagType(ord(self.BidOffsetFlag))
	def getAskHedgeFlag(self):
		return HedgeFlagType(ord(self.AskHedgeFlag))
	def getBidHedgeFlag(self):
		return HedgeFlagType(ord(self.BidHedgeFlag))
	def getQuoteLocalID(self):
		return self.QuoteLocalID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getClientID(self):
		return self.ClientID.decode('ascii')
	def getExchangeInstID(self):
		return self.ExchangeInstID.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')
	def getInstallID(self):
		return self.InstallID
	def getNotifySequence(self):
		return self.NotifySequence
	def getOrderSubmitStatus(self):
		return OrderSubmitStatusType(ord(self.OrderSubmitStatus))
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getSettlementID(self):
		return self.SettlementID
	def getQuoteSysID(self):
		return self.QuoteSysID.decode('ascii')
	def getInsertDate(self):
		return self.InsertDate.decode('ascii')
	def getInsertTime(self):
		return self.InsertTime.decode('ascii')
	def getCancelTime(self):
		return self.CancelTime.decode('ascii')
	def getQuoteStatus(self):
		return OrderStatusType(ord(self.QuoteStatus))
	def getClearingPartID(self):
		return self.ClearingPartID.decode('ascii')
	def getSequenceNo(self):
		return self.SequenceNo
	def getAskOrderSysID(self):
		return self.AskOrderSysID.decode('ascii')
	def getBidOrderSysID(self):
		return self.BidOrderSysID.decode('ascii')

class CThostFtdcQryExchangeQuoteField(Structure):
	"""交易所报价查询"""
	_fields_ = [
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		]

	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getClientID(self):
		return self.ClientID.decode('ascii')
	def getExchangeInstID(self):
		return self.ExchangeInstID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')

class CThostFtdcQryQuoteActionField(Structure):
	"""报价操作查询"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')

class CThostFtdcExchangeQuoteActionField(Structure):
	"""交易所报价操作"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#报价操作编号
		("QuoteSysID",c_char*21),
		#操作标志
		("ActionFlag",c_char),
		#操作日期
		("ActionDate",c_char*9),
		#操作时间
		("ActionTime",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#本地报价编号
		("QuoteLocalID",c_char*13),
		#操作本地编号
		("ActionLocalID",c_char*13),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#业务单元
		("BusinessUnit",c_char*21),
		#报单操作状态
		("OrderActionStatus",c_char),
		#用户代码
		("UserID",c_char*16),
		]

	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getQuoteSysID(self):
		return self.QuoteSysID.decode('ascii')
	def getActionFlag(self):
		return ActionFlagType(ord(self.ActionFlag))
	def getActionDate(self):
		return self.ActionDate.decode('ascii')
	def getActionTime(self):
		return self.ActionTime.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')
	def getInstallID(self):
		return self.InstallID
	def getQuoteLocalID(self):
		return self.QuoteLocalID.decode('ascii')
	def getActionLocalID(self):
		return self.ActionLocalID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getClientID(self):
		return self.ClientID.decode('ascii')
	def getBusinessUnit(self):
		return self.BusinessUnit.decode('ascii')
	def getOrderActionStatus(self):
		return OrderActionStatusType(ord(self.OrderActionStatus))
	def getUserID(self):
		return self.UserID.decode('ascii')

class CThostFtdcQryExchangeQuoteActionField(Structure):
	"""交易所报价操作查询"""
	_fields_ = [
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#交易所代码
		("ExchangeID",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		]

	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getClientID(self):
		return self.ClientID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')

class CThostFtdcOptionInstrDeltaField(Structure):
	"""期权合约delta值"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#投资者范围
		("InvestorRange",c_char),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#Delta值
		("Delta",c_double),
		]

	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getDelta(self):
		return self.Delta

class CThostFtdcForQuoteRspField(Structure):
	"""发给做市商的询价请求"""
	_fields_ = [
		#交易日
		("TradingDay",c_char*9),
		#合约代码
		("InstrumentID",c_char*31),
		#询价编号
		("ForQuoteSysID",c_char*21),
		#询价时间
		("ForQuoteTime",c_char*9),
		#业务日期
		("ActionDay",c_char*9),
		#交易所代码
		("ExchangeID",c_char*9),
		]

	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getForQuoteSysID(self):
		return self.ForQuoteSysID.decode('ascii')
	def getForQuoteTime(self):
		return self.ForQuoteTime.decode('ascii')
	def getActionDay(self):
		return self.ActionDay.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')

class CThostFtdcStrikeOffsetField(Structure):
	"""当前期权合约执行偏移值的详细内容"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#投资者范围
		("InvestorRange",c_char),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#执行偏移值
		("Offset",c_double),
		]

	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getOffset(self):
		return self.Offset

class CThostFtdcQryStrikeOffsetField(Structure):
	"""期权执行偏移值查询"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')

class CThostFtdcMarketDataField(Structure):
	"""市场行情"""
	_fields_ = [
		#交易日
		("TradingDay",c_char*9),
		#合约代码
		("InstrumentID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#最新价
		("LastPrice",c_double),
		#上次结算价
		("PreSettlementPrice",c_double),
		#昨收盘
		("PreClosePrice",c_double),
		#昨持仓量
		("PreOpenInterest",c_double),
		#今开盘
		("OpenPrice",c_double),
		#最高价
		("HighestPrice",c_double),
		#最低价
		("LowestPrice",c_double),
		#数量
		("Volume",c_int32),
		#成交金额
		("Turnover",c_double),
		#持仓量
		("OpenInterest",c_double),
		#今收盘
		("ClosePrice",c_double),
		#本次结算价
		("SettlementPrice",c_double),
		#涨停板价
		("UpperLimitPrice",c_double),
		#跌停板价
		("LowerLimitPrice",c_double),
		#昨虚实度
		("PreDelta",c_double),
		#今虚实度
		("CurrDelta",c_double),
		#最后修改时间
		("UpdateTime",c_char*9),
		#最后修改毫秒
		("UpdateMillisec",c_int32),
		#业务日期
		("ActionDay",c_char*9),
		]

	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getExchangeInstID(self):
		return self.ExchangeInstID.decode('ascii')
	def getLastPrice(self):
		return self.LastPrice
	def getPreSettlementPrice(self):
		return self.PreSettlementPrice
	def getPreClosePrice(self):
		return self.PreClosePrice
	def getPreOpenInterest(self):
		return self.PreOpenInterest
	def getOpenPrice(self):
		return self.OpenPrice
	def getHighestPrice(self):
		return self.HighestPrice
	def getLowestPrice(self):
		return self.LowestPrice
	def getVolume(self):
		return self.Volume
	def getTurnover(self):
		return self.Turnover
	def getOpenInterest(self):
		return self.OpenInterest
	def getClosePrice(self):
		return self.ClosePrice
	def getSettlementPrice(self):
		return self.SettlementPrice
	def getUpperLimitPrice(self):
		return self.UpperLimitPrice
	def getLowerLimitPrice(self):
		return self.LowerLimitPrice
	def getPreDelta(self):
		return self.PreDelta
	def getCurrDelta(self):
		return self.CurrDelta
	def getUpdateTime(self):
		return self.UpdateTime.decode('ascii')
	def getUpdateMillisec(self):
		return self.UpdateMillisec
	def getActionDay(self):
		return self.ActionDay.decode('ascii')

class CThostFtdcMarketDataBaseField(Structure):
	"""行情基础属性"""
	_fields_ = [
		#交易日
		("TradingDay",c_char*9),
		#上次结算价
		("PreSettlementPrice",c_double),
		#昨收盘
		("PreClosePrice",c_double),
		#昨持仓量
		("PreOpenInterest",c_double),
		#昨虚实度
		("PreDelta",c_double),
		]

	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getPreSettlementPrice(self):
		return self.PreSettlementPrice
	def getPreClosePrice(self):
		return self.PreClosePrice
	def getPreOpenInterest(self):
		return self.PreOpenInterest
	def getPreDelta(self):
		return self.PreDelta

class CThostFtdcMarketDataStaticField(Structure):
	"""行情静态属性"""
	_fields_ = [
		#今开盘
		("OpenPrice",c_double),
		#最高价
		("HighestPrice",c_double),
		#最低价
		("LowestPrice",c_double),
		#今收盘
		("ClosePrice",c_double),
		#涨停板价
		("UpperLimitPrice",c_double),
		#跌停板价
		("LowerLimitPrice",c_double),
		#本次结算价
		("SettlementPrice",c_double),
		#今虚实度
		("CurrDelta",c_double),
		]

	def getOpenPrice(self):
		return self.OpenPrice
	def getHighestPrice(self):
		return self.HighestPrice
	def getLowestPrice(self):
		return self.LowestPrice
	def getClosePrice(self):
		return self.ClosePrice
	def getUpperLimitPrice(self):
		return self.UpperLimitPrice
	def getLowerLimitPrice(self):
		return self.LowerLimitPrice
	def getSettlementPrice(self):
		return self.SettlementPrice
	def getCurrDelta(self):
		return self.CurrDelta

class CThostFtdcMarketDataLastMatchField(Structure):
	"""行情最新成交属性"""
	_fields_ = [
		#最新价
		("LastPrice",c_double),
		#数量
		("Volume",c_int32),
		#成交金额
		("Turnover",c_double),
		#持仓量
		("OpenInterest",c_double),
		]

	def getLastPrice(self):
		return self.LastPrice
	def getVolume(self):
		return self.Volume
	def getTurnover(self):
		return self.Turnover
	def getOpenInterest(self):
		return self.OpenInterest

class CThostFtdcMarketDataBestPriceField(Structure):
	"""行情最优价属性"""
	_fields_ = [
		#申买价一
		("BidPrice1",c_double),
		#申买量一
		("BidVolume1",c_int32),
		#申卖价一
		("AskPrice1",c_double),
		#申卖量一
		("AskVolume1",c_int32),
		]

	def getBidPrice1(self):
		return self.BidPrice1
	def getBidVolume1(self):
		return self.BidVolume1
	def getAskPrice1(self):
		return self.AskPrice1
	def getAskVolume1(self):
		return self.AskVolume1

class CThostFtdcMarketDataBid23Field(Structure):
	"""行情申买二、三属性"""
	_fields_ = [
		#申买价二
		("BidPrice2",c_double),
		#申买量二
		("BidVolume2",c_int32),
		#申买价三
		("BidPrice3",c_double),
		#申买量三
		("BidVolume3",c_int32),
		]

	def getBidPrice2(self):
		return self.BidPrice2
	def getBidVolume2(self):
		return self.BidVolume2
	def getBidPrice3(self):
		return self.BidPrice3
	def getBidVolume3(self):
		return self.BidVolume3

class CThostFtdcMarketDataAsk23Field(Structure):
	"""行情申卖二、三属性"""
	_fields_ = [
		#申卖价二
		("AskPrice2",c_double),
		#申卖量二
		("AskVolume2",c_int32),
		#申卖价三
		("AskPrice3",c_double),
		#申卖量三
		("AskVolume3",c_int32),
		]

	def getAskPrice2(self):
		return self.AskPrice2
	def getAskVolume2(self):
		return self.AskVolume2
	def getAskPrice3(self):
		return self.AskPrice3
	def getAskVolume3(self):
		return self.AskVolume3

class CThostFtdcMarketDataBid45Field(Structure):
	"""行情申买四、五属性"""
	_fields_ = [
		#申买价四
		("BidPrice4",c_double),
		#申买量四
		("BidVolume4",c_int32),
		#申买价五
		("BidPrice5",c_double),
		#申买量五
		("BidVolume5",c_int32),
		]

	def getBidPrice4(self):
		return self.BidPrice4
	def getBidVolume4(self):
		return self.BidVolume4
	def getBidPrice5(self):
		return self.BidPrice5
	def getBidVolume5(self):
		return self.BidVolume5

class CThostFtdcMarketDataAsk45Field(Structure):
	"""行情申卖四、五属性"""
	_fields_ = [
		#申卖价四
		("AskPrice4",c_double),
		#申卖量四
		("AskVolume4",c_int32),
		#申卖价五
		("AskPrice5",c_double),
		#申卖量五
		("AskVolume5",c_int32),
		]

	def getAskPrice4(self):
		return self.AskPrice4
	def getAskVolume4(self):
		return self.AskVolume4
	def getAskPrice5(self):
		return self.AskPrice5
	def getAskVolume5(self):
		return self.AskVolume5

class CThostFtdcMarketDataUpdateTimeField(Structure):
	"""行情更新时间属性"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#最后修改时间
		("UpdateTime",c_char*9),
		#最后修改毫秒
		("UpdateMillisec",c_int32),
		#业务日期
		("ActionDay",c_char*9),
		]

	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getUpdateTime(self):
		return self.UpdateTime.decode('ascii')
	def getUpdateMillisec(self):
		return self.UpdateMillisec
	def getActionDay(self):
		return self.ActionDay.decode('ascii')

class CThostFtdcMarketDataExchangeField(Structure):
	"""行情交易所代码属性"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		]

	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')

class CThostFtdcSpecificInstrumentField(Structure):
	"""指定的合约"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')

class CThostFtdcInstrumentStatusField(Structure):
	"""合约状态"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#结算组代码
		("SettlementGroupID",c_char*9),
		#合约代码
		("InstrumentID",c_char*31),
		#合约交易状态
		("InstrumentStatus",c_char),
		#交易阶段编号
		("TradingSegmentSN",c_int32),
		#进入本状态时间
		("EnterTime",c_char*9),
		#进入本状态原因
		("EnterReason",c_char),
		]

	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getExchangeInstID(self):
		return self.ExchangeInstID.decode('ascii')
	def getSettlementGroupID(self):
		return self.SettlementGroupID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getInstrumentStatus(self):
		return InstrumentStatusType(ord(self.InstrumentStatus))
	def getTradingSegmentSN(self):
		return self.TradingSegmentSN
	def getEnterTime(self):
		return self.EnterTime.decode('ascii')
	def getEnterReason(self):
		return InstStatusEnterReasonType(ord(self.EnterReason))

class CThostFtdcQryInstrumentStatusField(Structure):
	"""查询合约状态"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		]

	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getExchangeInstID(self):
		return self.ExchangeInstID.decode('ascii')

class CThostFtdcInvestorAccountField(Structure):
	"""投资者账户"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#投资者帐号
		("AccountID",c_char*13),
		#币种代码
		("CurrencyID",c_char*4),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')

class CThostFtdcPositionProfitAlgorithmField(Structure):
	"""浮动盈亏算法"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者帐号
		("AccountID",c_char*13),
		#盈亏算法
		("Algorithm",c_char),
		#备注
		("Memo",c_char*161),
		#币种代码
		("CurrencyID",c_char*4),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getAlgorithm(self):
		return AlgorithmType(ord(self.Algorithm))
	def getMemo(self):
		return self.Memo.decode('ascii')
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')

class CThostFtdcDiscountField(Structure):
	"""会员资金折扣"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者范围
		("InvestorRange",c_char),
		#投资者代码
		("InvestorID",c_char*13),
		#资金折扣比例
		("Discount",c_double),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getDiscount(self):
		return self.Discount

class CThostFtdcQryTransferBankField(Structure):
	"""查询转帐银行"""
	_fields_ = [
		#银行代码
		("BankID",c_char*4),
		#银行分中心代码
		("BankBrchID",c_char*5),
		]

	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBrchID(self):
		return self.BankBrchID.decode('ascii')

class CThostFtdcTransferBankField(Structure):
	"""转帐银行"""
	_fields_ = [
		#银行代码
		("BankID",c_char*4),
		#银行分中心代码
		("BankBrchID",c_char*5),
		#银行名称
		("BankName",c_char*101),
		#是否活跃
		("IsActive",c_int32),
		]

	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBrchID(self):
		return self.BankBrchID.decode('ascii')
	def getBankName(self):
		return self.BankName.decode('ascii')
	def getIsActive(self):
		return self.IsActive

class CThostFtdcQryInvestorPositionDetailField(Structure):
	"""查询投资者持仓明细"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')

class CThostFtdcInvestorPositionDetailField(Structure):
	"""投资者持仓明细"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#投机套保标志
		("HedgeFlag",c_char),
		#买卖
		("Direction",c_char),
		#开仓日期
		("OpenDate",c_char*9),
		#成交编号
		("TradeID",c_char*21),
		#数量
		("Volume",c_int32),
		#开仓价
		("OpenPrice",c_double),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#成交类型
		("TradeType",c_char),
		#组合合约代码
		("CombInstrumentID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#逐日盯市平仓盈亏
		("CloseProfitByDate",c_double),
		#逐笔对冲平仓盈亏
		("CloseProfitByTrade",c_double),
		#逐日盯市持仓盈亏
		("PositionProfitByDate",c_double),
		#逐笔对冲持仓盈亏
		("PositionProfitByTrade",c_double),
		#投资者保证金
		("Margin",c_double),
		#交易所保证金
		("ExchMargin",c_double),
		#保证金率
		("MarginRateByMoney",c_double),
		#保证金率(按手数)
		("MarginRateByVolume",c_double),
		#昨结算价
		("LastSettlementPrice",c_double),
		#结算价
		("SettlementPrice",c_double),
		#平仓量
		("CloseVolume",c_int32),
		#平仓金额
		("CloseAmount",c_double),
		]

	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getOpenDate(self):
		return self.OpenDate.decode('ascii')
	def getTradeID(self):
		return self.TradeID.decode('ascii')
	def getVolume(self):
		return self.Volume
	def getOpenPrice(self):
		return self.OpenPrice
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getSettlementID(self):
		return self.SettlementID
	def getTradeType(self):
		return TradeTypeType(ord(self.TradeType))
	def getCombInstrumentID(self):
		return self.CombInstrumentID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getCloseProfitByDate(self):
		return self.CloseProfitByDate
	def getCloseProfitByTrade(self):
		return self.CloseProfitByTrade
	def getPositionProfitByDate(self):
		return self.PositionProfitByDate
	def getPositionProfitByTrade(self):
		return self.PositionProfitByTrade
	def getMargin(self):
		return self.Margin
	def getExchMargin(self):
		return self.ExchMargin
	def getMarginRateByMoney(self):
		return self.MarginRateByMoney
	def getMarginRateByVolume(self):
		return self.MarginRateByVolume
	def getLastSettlementPrice(self):
		return self.LastSettlementPrice
	def getSettlementPrice(self):
		return self.SettlementPrice
	def getCloseVolume(self):
		return self.CloseVolume
	def getCloseAmount(self):
		return self.CloseAmount

class CThostFtdcTradingAccountPasswordField(Structure):
	"""资金账户口令域"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者帐号
		("AccountID",c_char*13),
		#密码
		("Password",c_char*41),
		#币种代码
		("CurrencyID",c_char*4),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getPassword(self):
		return self.Password.decode('ascii')
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')

class CThostFtdcMDTraderOfferField(Structure):
	"""交易所行情报盘机"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		#会员代码
		("ParticipantID",c_char*11),
		#密码
		("Password",c_char*41),
		#安装编号
		("InstallID",c_int32),
		#本地报单编号
		("OrderLocalID",c_char*13),
		#交易所交易员连接状态
		("TraderConnectStatus",c_char),
		#发出连接请求的日期
		("ConnectRequestDate",c_char*9),
		#发出连接请求的时间
		("ConnectRequestTime",c_char*9),
		#上次报告日期
		("LastReportDate",c_char*9),
		#上次报告时间
		("LastReportTime",c_char*9),
		#完成连接日期
		("ConnectDate",c_char*9),
		#完成连接时间
		("ConnectTime",c_char*9),
		#启动日期
		("StartDate",c_char*9),
		#启动时间
		("StartTime",c_char*9),
		#交易日
		("TradingDay",c_char*9),
		#经纪公司代码
		("BrokerID",c_char*11),
		#本席位最大成交编号
		("MaxTradeID",c_char*21),
		#本席位最大报单备拷
		("MaxOrderMessageReference",c_char*7),
		]

	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getPassword(self):
		return self.Password.decode('ascii')
	def getInstallID(self):
		return self.InstallID
	def getOrderLocalID(self):
		return self.OrderLocalID.decode('ascii')
	def getTraderConnectStatus(self):
		return TraderConnectStatusType(ord(self.TraderConnectStatus))
	def getConnectRequestDate(self):
		return self.ConnectRequestDate.decode('ascii')
	def getConnectRequestTime(self):
		return self.ConnectRequestTime.decode('ascii')
	def getLastReportDate(self):
		return self.LastReportDate.decode('ascii')
	def getLastReportTime(self):
		return self.LastReportTime.decode('ascii')
	def getConnectDate(self):
		return self.ConnectDate.decode('ascii')
	def getConnectTime(self):
		return self.ConnectTime.decode('ascii')
	def getStartDate(self):
		return self.StartDate.decode('ascii')
	def getStartTime(self):
		return self.StartTime.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getMaxTradeID(self):
		return self.MaxTradeID.decode('ascii')
	def getMaxOrderMessageReference(self):
		return self.MaxOrderMessageReference.decode('ascii')

class CThostFtdcQryMDTraderOfferField(Structure):
	"""查询行情报盘机"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#交易所交易员代码
		("TraderID",c_char*21),
		]

	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')

class CThostFtdcQryNoticeField(Structure):
	"""查询客户通知"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')

class CThostFtdcNoticeField(Structure):
	"""客户通知"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#消息正文
		("Content",c_char*501),
		#经纪公司通知内容序列号
		("SequenceLabel",c_char*2),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getContent(self):
		return self.Content.decode('ascii')
	def getSequenceLabel(self):
		return self.SequenceLabel.decode('ascii')

class CThostFtdcUserRightField(Structure):
	"""用户权限"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#客户权限类型
		("UserRightType",c_char),
		#是否禁止
		("IsForbidden",c_int32),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getUserRightType(self):
		return UserRightTypeType(ord(self.UserRightType))
	def getIsForbidden(self):
		return self.IsForbidden

class CThostFtdcQrySettlementInfoConfirmField(Structure):
	"""查询结算信息确认域"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')

class CThostFtdcLoadSettlementInfoField(Structure):
	"""装载结算信息"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')

class CThostFtdcBrokerWithdrawAlgorithmField(Structure):
	"""经纪公司可提资金算法表"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#可提资金算法
		("WithdrawAlgorithm",c_char),
		#资金使用率
		("UsingRatio",c_double),
		#可提是否包含平仓盈利
		("IncludeCloseProfit",c_char),
		#本日无仓且无成交客户是否受可提比例限制
		("AllWithoutTrade",c_char),
		#可用是否包含平仓盈利
		("AvailIncludeCloseProfit",c_char),
		#是否启用用户事件
		("IsBrokerUserEvent",c_int32),
		#币种代码
		("CurrencyID",c_char*4),
		#货币质押比率
		("FundMortgageRatio",c_double),
		#权益算法
		("BalanceAlgorithm",c_char),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getWithdrawAlgorithm(self):
		return AlgorithmType(ord(self.WithdrawAlgorithm))
	def getUsingRatio(self):
		return self.UsingRatio
	def getIncludeCloseProfit(self):
		return IncludeCloseProfitType(ord(self.IncludeCloseProfit))
	def getAllWithoutTrade(self):
		return AllWithoutTradeType(ord(self.AllWithoutTrade))
	def getAvailIncludeCloseProfit(self):
		return IncludeCloseProfitType(ord(self.AvailIncludeCloseProfit))
	def getIsBrokerUserEvent(self):
		return self.IsBrokerUserEvent
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')
	def getFundMortgageRatio(self):
		return self.FundMortgageRatio
	def getBalanceAlgorithm(self):
		return BalanceAlgorithmType(ord(self.BalanceAlgorithm))

class CThostFtdcTradingAccountPasswordUpdateV1Field(Structure):
	"""资金账户口令变更域"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#原来的口令
		("OldPassword",c_char*41),
		#新的口令
		("NewPassword",c_char*41),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getOldPassword(self):
		return self.OldPassword.decode('ascii')
	def getNewPassword(self):
		return self.NewPassword.decode('ascii')

class CThostFtdcTradingAccountPasswordUpdateField(Structure):
	"""资金账户口令变更域"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者帐号
		("AccountID",c_char*13),
		#原来的口令
		("OldPassword",c_char*41),
		#新的口令
		("NewPassword",c_char*41),
		#币种代码
		("CurrencyID",c_char*4),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getOldPassword(self):
		return self.OldPassword.decode('ascii')
	def getNewPassword(self):
		return self.NewPassword.decode('ascii')
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')

class CThostFtdcQryCombinationLegField(Structure):
	"""查询组合合约分腿"""
	_fields_ = [
		#组合合约代码
		("CombInstrumentID",c_char*31),
		#单腿编号
		("LegID",c_int32),
		#单腿合约代码
		("LegInstrumentID",c_char*31),
		]

	def getCombInstrumentID(self):
		return self.CombInstrumentID.decode('ascii')
	def getLegID(self):
		return self.LegID
	def getLegInstrumentID(self):
		return self.LegInstrumentID.decode('ascii')

class CThostFtdcQrySyncStatusField(Structure):
	"""查询组合合约分腿"""
	_fields_ = [
		#交易日
		("TradingDay",c_char*9),
		]

	def getTradingDay(self):
		return self.TradingDay.decode('ascii')

class CThostFtdcCombinationLegField(Structure):
	"""组合交易合约的单腿"""
	_fields_ = [
		#组合合约代码
		("CombInstrumentID",c_char*31),
		#单腿编号
		("LegID",c_int32),
		#单腿合约代码
		("LegInstrumentID",c_char*31),
		#买卖方向
		("Direction",c_char),
		#单腿乘数
		("LegMultiple",c_int32),
		#派生层数
		("ImplyLevel",c_int32),
		]

	def getCombInstrumentID(self):
		return self.CombInstrumentID.decode('ascii')
	def getLegID(self):
		return self.LegID
	def getLegInstrumentID(self):
		return self.LegInstrumentID.decode('ascii')
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getLegMultiple(self):
		return self.LegMultiple
	def getImplyLevel(self):
		return self.ImplyLevel

class CThostFtdcSyncStatusField(Structure):
	"""数据同步状态"""
	_fields_ = [
		#交易日
		("TradingDay",c_char*9),
		#数据同步状态
		("DataSyncStatus",c_char),
		]

	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getDataSyncStatus(self):
		return DataSyncStatusType(ord(self.DataSyncStatus))

class CThostFtdcQryLinkManField(Structure):
	"""查询联系人"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')

class CThostFtdcLinkManField(Structure):
	"""联系人"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#联系人类型
		("PersonType",c_char),
		#证件类型
		("IdentifiedCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#名称
		("PersonName",c_char*81),
		#联系电话
		("Telephone",c_char*41),
		#通讯地址
		("Address",c_char*101),
		#邮政编码
		("ZipCode",c_char*7),
		#优先级
		("Priority",c_int32),
		#开户邮政编码
		("UOAZipCode",c_char*11),
		#全称
		("PersonFullName",c_char*101),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getPersonType(self):
		return PersonTypeType(ord(self.PersonType))
	def getIdentifiedCardType(self):
		return IdCardTypeType(ord(self.IdentifiedCardType))
	def getIdentifiedCardNo(self):
		return self.IdentifiedCardNo.decode('ascii')
	def getPersonName(self):
		return self.PersonName.decode('ascii')
	def getTelephone(self):
		return self.Telephone.decode('ascii')
	def getAddress(self):
		return self.Address.decode('ascii')
	def getZipCode(self):
		return self.ZipCode.decode('ascii')
	def getPriority(self):
		return self.Priority
	def getUOAZipCode(self):
		return self.UOAZipCode.decode('ascii')
	def getPersonFullName(self):
		return self.PersonFullName.decode('ascii')

class CThostFtdcQryBrokerUserEventField(Structure):
	"""查询经纪公司用户事件"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#用户事件类型
		("UserEventType",c_char),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getUserEventType(self):
		return UserEventTypeType(ord(self.UserEventType))

class CThostFtdcBrokerUserEventField(Structure):
	"""查询经纪公司用户事件"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#用户事件类型
		("UserEventType",c_char),
		#用户事件序号
		("EventSequenceNo",c_int32),
		#事件发生日期
		("EventDate",c_char*9),
		#事件发生时间
		("EventTime",c_char*9),
		#用户事件信息
		("UserEventInfo",c_char*1025),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getUserEventType(self):
		return UserEventTypeType(ord(self.UserEventType))
	def getEventSequenceNo(self):
		return self.EventSequenceNo
	def getEventDate(self):
		return self.EventDate.decode('ascii')
	def getEventTime(self):
		return self.EventTime.decode('ascii')
	def getUserEventInfo(self):
		return self.UserEventInfo.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')

class CThostFtdcQryContractBankField(Structure):
	"""查询签约银行请求"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#银行代码
		("BankID",c_char*4),
		#银行分中心代码
		("BankBrchID",c_char*5),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBrchID(self):
		return self.BankBrchID.decode('ascii')

class CThostFtdcContractBankField(Structure):
	"""查询签约银行响应"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#银行代码
		("BankID",c_char*4),
		#银行分中心代码
		("BankBrchID",c_char*5),
		#银行名称
		("BankName",c_char*101),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBrchID(self):
		return self.BankBrchID.decode('ascii')
	def getBankName(self):
		return self.BankName.decode('ascii')

class CThostFtdcInvestorPositionCombineDetailField(Structure):
	"""投资者组合持仓明细"""
	_fields_ = [
		#交易日
		("TradingDay",c_char*9),
		#开仓日期
		("OpenDate",c_char*9),
		#交易所代码
		("ExchangeID",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#组合编号
		("ComTradeID",c_char*21),
		#撮合编号
		("TradeID",c_char*21),
		#合约代码
		("InstrumentID",c_char*31),
		#投机套保标志
		("HedgeFlag",c_char),
		#买卖
		("Direction",c_char),
		#持仓量
		("TotalAmt",c_int32),
		#投资者保证金
		("Margin",c_double),
		#交易所保证金
		("ExchMargin",c_double),
		#保证金率
		("MarginRateByMoney",c_double),
		#保证金率(按手数)
		("MarginRateByVolume",c_double),
		#单腿编号
		("LegID",c_int32),
		#单腿乘数
		("LegMultiple",c_int32),
		#组合持仓合约编码
		("CombInstrumentID",c_char*31),
		#成交组号
		("TradeGroupID",c_int32),
		]

	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getOpenDate(self):
		return self.OpenDate.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getSettlementID(self):
		return self.SettlementID
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getComTradeID(self):
		return self.ComTradeID.decode('ascii')
	def getTradeID(self):
		return self.TradeID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getTotalAmt(self):
		return self.TotalAmt
	def getMargin(self):
		return self.Margin
	def getExchMargin(self):
		return self.ExchMargin
	def getMarginRateByMoney(self):
		return self.MarginRateByMoney
	def getMarginRateByVolume(self):
		return self.MarginRateByVolume
	def getLegID(self):
		return self.LegID
	def getLegMultiple(self):
		return self.LegMultiple
	def getCombInstrumentID(self):
		return self.CombInstrumentID.decode('ascii')
	def getTradeGroupID(self):
		return self.TradeGroupID

class CThostFtdcParkedOrderField(Structure):
	"""预埋单"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#报单引用
		("OrderRef",c_char*13),
		#用户代码
		("UserID",c_char*16),
		#报单价格条件
		("OrderPriceType",c_char),
		#买卖方向
		("Direction",c_char),
		#组合开平标志
		("CombOffsetFlag",c_char*5),
		#组合投机套保标志
		("CombHedgeFlag",c_char*5),
		#价格
		("LimitPrice",c_double),
		#数量
		("VolumeTotalOriginal",c_int32),
		#有效期类型
		("TimeCondition",c_char),
		#GTD日期
		("GTDDate",c_char*9),
		#成交量类型
		("VolumeCondition",c_char),
		#最小成交量
		("MinVolume",c_int32),
		#触发条件
		("ContingentCondition",c_char),
		#止损价
		("StopPrice",c_double),
		#强平原因
		("ForceCloseReason",c_char),
		#自动挂起标志
		("IsAutoSuspend",c_int32),
		#业务单元
		("BusinessUnit",c_char*21),
		#请求编号
		("RequestID",c_int32),
		#用户强评标志
		("UserForceClose",c_int32),
		#交易所代码
		("ExchangeID",c_char*9),
		#预埋报单编号
		("ParkedOrderID",c_char*13),
		#用户类型
		("UserType",c_char),
		#预埋单状态
		("Status",c_char),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		#互换单标志
		("IsSwapOrder",c_int32),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getOrderRef(self):
		return self.OrderRef.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getOrderPriceType(self):
		return OrderPriceTypeType(ord(self.OrderPriceType))
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getCombOffsetFlag(self):
		return self.CombOffsetFlag.decode('ascii')
	def getCombHedgeFlag(self):
		return self.CombHedgeFlag.decode('ascii')
	def getLimitPrice(self):
		return self.LimitPrice
	def getVolumeTotalOriginal(self):
		return self.VolumeTotalOriginal
	def getTimeCondition(self):
		return TimeConditionType(ord(self.TimeCondition))
	def getGTDDate(self):
		return self.GTDDate.decode('ascii')
	def getVolumeCondition(self):
		return VolumeConditionType(ord(self.VolumeCondition))
	def getMinVolume(self):
		return self.MinVolume
	def getContingentCondition(self):
		return ContingentConditionType(ord(self.ContingentCondition))
	def getStopPrice(self):
		return self.StopPrice
	def getForceCloseReason(self):
		return ForceCloseReasonType(ord(self.ForceCloseReason))
	def getIsAutoSuspend(self):
		return self.IsAutoSuspend
	def getBusinessUnit(self):
		return self.BusinessUnit.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getUserForceClose(self):
		return self.UserForceClose
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getParkedOrderID(self):
		return self.ParkedOrderID.decode('ascii')
	def getUserType(self):
		return UserTypeType(ord(self.UserType))
	def getStatus(self):
		return ParkedOrderStatusType(ord(self.Status))
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return self.ErrorMsg.decode('GB2312')
	def getIsSwapOrder(self):
		return self.IsSwapOrder

class CThostFtdcParkedOrderActionField(Structure):
	"""输入预埋单操作"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#报单操作引用
		("OrderActionRef",c_int32),
		#报单引用
		("OrderRef",c_char*13),
		#请求编号
		("RequestID",c_int32),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#交易所代码
		("ExchangeID",c_char*9),
		#报单编号
		("OrderSysID",c_char*21),
		#操作标志
		("ActionFlag",c_char),
		#价格
		("LimitPrice",c_double),
		#数量变化
		("VolumeChange",c_int32),
		#用户代码
		("UserID",c_char*16),
		#合约代码
		("InstrumentID",c_char*31),
		#预埋撤单单编号
		("ParkedOrderActionID",c_char*13),
		#用户类型
		("UserType",c_char),
		#预埋撤单状态
		("Status",c_char),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getOrderActionRef(self):
		return self.OrderActionRef
	def getOrderRef(self):
		return self.OrderRef.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getOrderSysID(self):
		return self.OrderSysID.decode('ascii')
	def getActionFlag(self):
		return ActionFlagType(ord(self.ActionFlag))
	def getLimitPrice(self):
		return self.LimitPrice
	def getVolumeChange(self):
		return self.VolumeChange
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getParkedOrderActionID(self):
		return self.ParkedOrderActionID.decode('ascii')
	def getUserType(self):
		return UserTypeType(ord(self.UserType))
	def getStatus(self):
		return ParkedOrderStatusType(ord(self.Status))
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return self.ErrorMsg.decode('GB2312')

class CThostFtdcQryParkedOrderField(Structure):
	"""查询预埋单"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')

class CThostFtdcQryParkedOrderActionField(Structure):
	"""查询预埋撤单"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')

class CThostFtdcRemoveParkedOrderField(Structure):
	"""删除预埋单"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#预埋报单编号
		("ParkedOrderID",c_char*13),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getParkedOrderID(self):
		return self.ParkedOrderID.decode('ascii')

class CThostFtdcRemoveParkedOrderActionField(Structure):
	"""删除预埋撤单"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#预埋撤单编号
		("ParkedOrderActionID",c_char*13),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getParkedOrderActionID(self):
		return self.ParkedOrderActionID.decode('ascii')

class CThostFtdcInvestorWithdrawAlgorithmField(Structure):
	"""经纪公司可提资金算法表"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者范围
		("InvestorRange",c_char),
		#投资者代码
		("InvestorID",c_char*13),
		#可提资金比例
		("UsingRatio",c_double),
		#币种代码
		("CurrencyID",c_char*4),
		#货币质押比率
		("FundMortgageRatio",c_double),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getUsingRatio(self):
		return self.UsingRatio
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')
	def getFundMortgageRatio(self):
		return self.FundMortgageRatio

class CThostFtdcQryInvestorPositionCombineDetailField(Structure):
	"""查询组合持仓明细"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#组合持仓合约编码
		("CombInstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getCombInstrumentID(self):
		return self.CombInstrumentID.decode('ascii')

class CThostFtdcMarketDataAveragePriceField(Structure):
	"""成交均价"""
	_fields_ = [
		#当日均价
		("AveragePrice",c_double),
		]

	def getAveragePrice(self):
		return self.AveragePrice

class CThostFtdcVerifyInvestorPasswordField(Structure):
	"""校验投资者密码"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#密码
		("Password",c_char*41),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getPassword(self):
		return self.Password.decode('ascii')

class CThostFtdcUserIPField(Structure):
	"""用户IP"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#IP地址
		("IPAddress",c_char*16),
		#IP地址掩码
		("IPMask",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getIPAddress(self):
		return self.IPAddress.decode('ascii')
	def getIPMask(self):
		return self.IPMask.decode('ascii')
	def getMacAddress(self):
		return self.MacAddress.decode('ascii')

class CThostFtdcTradingNoticeInfoField(Structure):
	"""用户事件通知信息"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#发送时间
		("SendTime",c_char*9),
		#消息正文
		("FieldContent",c_char*501),
		#序列系列号
		("SequenceSeries",c_int32),
		#序列号
		("SequenceNo",c_int32),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getSendTime(self):
		return self.SendTime.decode('ascii')
	def getFieldContent(self):
		return self.FieldContent.decode('ascii')
	def getSequenceSeries(self):
		return self.SequenceSeries
	def getSequenceNo(self):
		return self.SequenceNo

class CThostFtdcTradingNoticeField(Structure):
	"""用户事件通知"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者范围
		("InvestorRange",c_char),
		#投资者代码
		("InvestorID",c_char*13),
		#序列系列号
		("SequenceSeries",c_int32),
		#用户代码
		("UserID",c_char*16),
		#发送时间
		("SendTime",c_char*9),
		#序列号
		("SequenceNo",c_int32),
		#消息正文
		("FieldContent",c_char*501),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getSequenceSeries(self):
		return self.SequenceSeries
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getSendTime(self):
		return self.SendTime.decode('ascii')
	def getSequenceNo(self):
		return self.SequenceNo
	def getFieldContent(self):
		return self.FieldContent.decode('ascii')

class CThostFtdcQryTradingNoticeField(Structure):
	"""查询交易事件通知"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')

class CThostFtdcQryErrOrderField(Structure):
	"""查询错误报单"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')

class CThostFtdcErrOrderField(Structure):
	"""错误报单"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#报单引用
		("OrderRef",c_char*13),
		#用户代码
		("UserID",c_char*16),
		#报单价格条件
		("OrderPriceType",c_char),
		#买卖方向
		("Direction",c_char),
		#组合开平标志
		("CombOffsetFlag",c_char*5),
		#组合投机套保标志
		("CombHedgeFlag",c_char*5),
		#价格
		("LimitPrice",c_double),
		#数量
		("VolumeTotalOriginal",c_int32),
		#有效期类型
		("TimeCondition",c_char),
		#GTD日期
		("GTDDate",c_char*9),
		#成交量类型
		("VolumeCondition",c_char),
		#最小成交量
		("MinVolume",c_int32),
		#触发条件
		("ContingentCondition",c_char),
		#止损价
		("StopPrice",c_double),
		#强平原因
		("ForceCloseReason",c_char),
		#自动挂起标志
		("IsAutoSuspend",c_int32),
		#业务单元
		("BusinessUnit",c_char*21),
		#请求编号
		("RequestID",c_int32),
		#用户强评标志
		("UserForceClose",c_int32),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		#互换单标志
		("IsSwapOrder",c_int32),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getOrderRef(self):
		return self.OrderRef.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getOrderPriceType(self):
		return OrderPriceTypeType(ord(self.OrderPriceType))
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getCombOffsetFlag(self):
		return self.CombOffsetFlag.decode('ascii')
	def getCombHedgeFlag(self):
		return self.CombHedgeFlag.decode('ascii')
	def getLimitPrice(self):
		return self.LimitPrice
	def getVolumeTotalOriginal(self):
		return self.VolumeTotalOriginal
	def getTimeCondition(self):
		return TimeConditionType(ord(self.TimeCondition))
	def getGTDDate(self):
		return self.GTDDate.decode('ascii')
	def getVolumeCondition(self):
		return VolumeConditionType(ord(self.VolumeCondition))
	def getMinVolume(self):
		return self.MinVolume
	def getContingentCondition(self):
		return ContingentConditionType(ord(self.ContingentCondition))
	def getStopPrice(self):
		return self.StopPrice
	def getForceCloseReason(self):
		return ForceCloseReasonType(ord(self.ForceCloseReason))
	def getIsAutoSuspend(self):
		return self.IsAutoSuspend
	def getBusinessUnit(self):
		return self.BusinessUnit.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getUserForceClose(self):
		return self.UserForceClose
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return self.ErrorMsg.decode('GB2312')
	def getIsSwapOrder(self):
		return self.IsSwapOrder

class CThostFtdcErrorConditionalOrderField(Structure):
	"""查询错误报单操作"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#报单引用
		("OrderRef",c_char*13),
		#用户代码
		("UserID",c_char*16),
		#报单价格条件
		("OrderPriceType",c_char),
		#买卖方向
		("Direction",c_char),
		#组合开平标志
		("CombOffsetFlag",c_char*5),
		#组合投机套保标志
		("CombHedgeFlag",c_char*5),
		#价格
		("LimitPrice",c_double),
		#数量
		("VolumeTotalOriginal",c_int32),
		#有效期类型
		("TimeCondition",c_char),
		#GTD日期
		("GTDDate",c_char*9),
		#成交量类型
		("VolumeCondition",c_char),
		#最小成交量
		("MinVolume",c_int32),
		#触发条件
		("ContingentCondition",c_char),
		#止损价
		("StopPrice",c_double),
		#强平原因
		("ForceCloseReason",c_char),
		#自动挂起标志
		("IsAutoSuspend",c_int32),
		#业务单元
		("BusinessUnit",c_char*21),
		#请求编号
		("RequestID",c_int32),
		#本地报单编号
		("OrderLocalID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#报单提交状态
		("OrderSubmitStatus",c_char),
		#报单提示序号
		("NotifySequence",c_int32),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#报单编号
		("OrderSysID",c_char*21),
		#报单来源
		("OrderSource",c_char),
		#报单状态
		("OrderStatus",c_char),
		#报单类型
		("OrderType",c_char),
		#今成交数量
		("VolumeTraded",c_int32),
		#剩余数量
		("VolumeTotal",c_int32),
		#报单日期
		("InsertDate",c_char*9),
		#委托时间
		("InsertTime",c_char*9),
		#激活时间
		("ActiveTime",c_char*9),
		#挂起时间
		("SuspendTime",c_char*9),
		#最后修改时间
		("UpdateTime",c_char*9),
		#撤销时间
		("CancelTime",c_char*9),
		#最后修改交易所交易员代码
		("ActiveTraderID",c_char*21),
		#结算会员编号
		("ClearingPartID",c_char*11),
		#序号
		("SequenceNo",c_int32),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#用户端产品信息
		("UserProductInfo",c_char*11),
		#状态信息
		("StatusMsg",c_char*81),
		#用户强评标志
		("UserForceClose",c_int32),
		#操作用户代码
		("ActiveUserID",c_char*16),
		#经纪公司报单编号
		("BrokerOrderSeq",c_int32),
		#相关报单
		("RelativeOrderSysID",c_char*21),
		#郑商所成交数量
		("ZCETotalTradedVolume",c_int32),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		#互换单标志
		("IsSwapOrder",c_int32),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getOrderRef(self):
		return self.OrderRef.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getOrderPriceType(self):
		return OrderPriceTypeType(ord(self.OrderPriceType))
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getCombOffsetFlag(self):
		return self.CombOffsetFlag.decode('ascii')
	def getCombHedgeFlag(self):
		return self.CombHedgeFlag.decode('ascii')
	def getLimitPrice(self):
		return self.LimitPrice
	def getVolumeTotalOriginal(self):
		return self.VolumeTotalOriginal
	def getTimeCondition(self):
		return TimeConditionType(ord(self.TimeCondition))
	def getGTDDate(self):
		return self.GTDDate.decode('ascii')
	def getVolumeCondition(self):
		return VolumeConditionType(ord(self.VolumeCondition))
	def getMinVolume(self):
		return self.MinVolume
	def getContingentCondition(self):
		return ContingentConditionType(ord(self.ContingentCondition))
	def getStopPrice(self):
		return self.StopPrice
	def getForceCloseReason(self):
		return ForceCloseReasonType(ord(self.ForceCloseReason))
	def getIsAutoSuspend(self):
		return self.IsAutoSuspend
	def getBusinessUnit(self):
		return self.BusinessUnit.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getOrderLocalID(self):
		return self.OrderLocalID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getClientID(self):
		return self.ClientID.decode('ascii')
	def getExchangeInstID(self):
		return self.ExchangeInstID.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')
	def getInstallID(self):
		return self.InstallID
	def getOrderSubmitStatus(self):
		return OrderSubmitStatusType(ord(self.OrderSubmitStatus))
	def getNotifySequence(self):
		return self.NotifySequence
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getSettlementID(self):
		return self.SettlementID
	def getOrderSysID(self):
		return self.OrderSysID.decode('ascii')
	def getOrderSource(self):
		return OrderSourceType(ord(self.OrderSource))
	def getOrderStatus(self):
		return OrderStatusType(ord(self.OrderStatus))
	def getOrderType(self):
		return OrderTypeType(ord(self.OrderType))
	def getVolumeTraded(self):
		return self.VolumeTraded
	def getVolumeTotal(self):
		return self.VolumeTotal
	def getInsertDate(self):
		return self.InsertDate.decode('ascii')
	def getInsertTime(self):
		return self.InsertTime.decode('ascii')
	def getActiveTime(self):
		return self.ActiveTime.decode('ascii')
	def getSuspendTime(self):
		return self.SuspendTime.decode('ascii')
	def getUpdateTime(self):
		return self.UpdateTime.decode('ascii')
	def getCancelTime(self):
		return self.CancelTime.decode('ascii')
	def getActiveTraderID(self):
		return self.ActiveTraderID.decode('ascii')
	def getClearingPartID(self):
		return self.ClearingPartID.decode('ascii')
	def getSequenceNo(self):
		return self.SequenceNo
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getUserProductInfo(self):
		return self.UserProductInfo.decode('ascii')
	def getStatusMsg(self):
		return self.StatusMsg.decode('GB2312')
	def getUserForceClose(self):
		return self.UserForceClose
	def getActiveUserID(self):
		return self.ActiveUserID.decode('ascii')
	def getBrokerOrderSeq(self):
		return self.BrokerOrderSeq
	def getRelativeOrderSysID(self):
		return self.RelativeOrderSysID.decode('ascii')
	def getZCETotalTradedVolume(self):
		return self.ZCETotalTradedVolume
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return self.ErrorMsg.decode('GB2312')
	def getIsSwapOrder(self):
		return self.IsSwapOrder

class CThostFtdcQryErrOrderActionField(Structure):
	"""查询错误报单操作"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')

class CThostFtdcErrOrderActionField(Structure):
	"""错误报单操作"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#报单操作引用
		("OrderActionRef",c_int32),
		#报单引用
		("OrderRef",c_char*13),
		#请求编号
		("RequestID",c_int32),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#交易所代码
		("ExchangeID",c_char*9),
		#报单编号
		("OrderSysID",c_char*21),
		#操作标志
		("ActionFlag",c_char),
		#价格
		("LimitPrice",c_double),
		#数量变化
		("VolumeChange",c_int32),
		#操作日期
		("ActionDate",c_char*9),
		#操作时间
		("ActionTime",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#本地报单编号
		("OrderLocalID",c_char*13),
		#操作本地编号
		("ActionLocalID",c_char*13),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#业务单元
		("BusinessUnit",c_char*21),
		#报单操作状态
		("OrderActionStatus",c_char),
		#用户代码
		("UserID",c_char*16),
		#状态信息
		("StatusMsg",c_char*81),
		#合约代码
		("InstrumentID",c_char*31),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getOrderActionRef(self):
		return self.OrderActionRef
	def getOrderRef(self):
		return self.OrderRef.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getOrderSysID(self):
		return self.OrderSysID.decode('ascii')
	def getActionFlag(self):
		return ActionFlagType(ord(self.ActionFlag))
	def getLimitPrice(self):
		return self.LimitPrice
	def getVolumeChange(self):
		return self.VolumeChange
	def getActionDate(self):
		return self.ActionDate.decode('ascii')
	def getActionTime(self):
		return self.ActionTime.decode('ascii')
	def getTraderID(self):
		return self.TraderID.decode('ascii')
	def getInstallID(self):
		return self.InstallID
	def getOrderLocalID(self):
		return self.OrderLocalID.decode('ascii')
	def getActionLocalID(self):
		return self.ActionLocalID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getClientID(self):
		return self.ClientID.decode('ascii')
	def getBusinessUnit(self):
		return self.BusinessUnit.decode('ascii')
	def getOrderActionStatus(self):
		return OrderActionStatusType(ord(self.OrderActionStatus))
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getStatusMsg(self):
		return self.StatusMsg.decode('GB2312')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return self.ErrorMsg.decode('GB2312')

class CThostFtdcQryExchangeSequenceField(Structure):
	"""查询交易所状态"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		]

	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')

class CThostFtdcExchangeSequenceField(Structure):
	"""交易所状态"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#序号
		("SequenceNo",c_int32),
		#合约交易状态
		("MarketStatus",c_char),
		]

	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getSequenceNo(self):
		return self.SequenceNo
	def getMarketStatus(self):
		return InstrumentStatusType(ord(self.MarketStatus))

class CThostFtdcQueryMaxOrderVolumeWithPriceField(Structure):
	"""根据价格查询最大报单数量"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#买卖方向
		("Direction",c_char),
		#开平标志
		("OffsetFlag",c_char),
		#投机套保标志
		("HedgeFlag",c_char),
		#最大允许报单数量
		("MaxVolume",c_int32),
		#报单价格
		("Price",c_double),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getOffsetFlag(self):
		return OffsetFlagType(ord(self.OffsetFlag))
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getMaxVolume(self):
		return self.MaxVolume
	def getPrice(self):
		return self.Price

class CThostFtdcQryBrokerTradingParamsField(Structure):
	"""查询经纪公司交易参数"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#币种代码
		("CurrencyID",c_char*4),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')

class CThostFtdcBrokerTradingParamsField(Structure):
	"""经纪公司交易参数"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#保证金价格类型
		("MarginPriceType",c_char),
		#盈亏算法
		("Algorithm",c_char),
		#可用是否包含平仓盈利
		("AvailIncludeCloseProfit",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#期权权利金价格类型
		("OptionRoyaltyPriceType",c_char),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getMarginPriceType(self):
		return MarginPriceTypeType(ord(self.MarginPriceType))
	def getAlgorithm(self):
		return AlgorithmType(ord(self.Algorithm))
	def getAvailIncludeCloseProfit(self):
		return IncludeCloseProfitType(ord(self.AvailIncludeCloseProfit))
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')
	def getOptionRoyaltyPriceType(self):
		return OptionRoyaltyPriceTypeType(ord(self.OptionRoyaltyPriceType))

class CThostFtdcQryBrokerTradingAlgosField(Structure):
	"""查询经纪公司交易算法"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#交易所代码
		("ExchangeID",c_char*9),
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')

class CThostFtdcBrokerTradingAlgosField(Structure):
	"""经纪公司交易算法"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#交易所代码
		("ExchangeID",c_char*9),
		#合约代码
		("InstrumentID",c_char*31),
		#持仓处理算法编号
		("HandlePositionAlgoID",c_char),
		#寻找保证金率算法编号
		("FindMarginRateAlgoID",c_char),
		#资金处理算法编号
		("HandleTradingAccountAlgoID",c_char),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getHandlePositionAlgoID(self):
		return HandlePositionAlgoIDType(ord(self.HandlePositionAlgoID))
	def getFindMarginRateAlgoID(self):
		return FindMarginRateAlgoIDType(ord(self.FindMarginRateAlgoID))
	def getHandleTradingAccountAlgoID(self):
		return HandleTradingAccountAlgoIDType(ord(self.HandleTradingAccountAlgoID))

class CThostFtdcQueryBrokerDepositField(Structure):
	"""查询经纪公司资金"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#交易所代码
		("ExchangeID",c_char*9),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')

class CThostFtdcBrokerDepositField(Structure):
	"""经纪公司资金"""
	_fields_ = [
		#交易日期
		("TradingDay",c_char*9),
		#经纪公司代码
		("BrokerID",c_char*11),
		#会员代码
		("ParticipantID",c_char*11),
		#交易所代码
		("ExchangeID",c_char*9),
		#上次结算准备金
		("PreBalance",c_double),
		#当前保证金总额
		("CurrMargin",c_double),
		#平仓盈亏
		("CloseProfit",c_double),
		#期货结算准备金
		("Balance",c_double),
		#入金金额
		("Deposit",c_double),
		#出金金额
		("Withdraw",c_double),
		#可提资金
		("Available",c_double),
		#基本准备金
		("Reserve",c_double),
		#冻结的保证金
		("FrozenMargin",c_double),
		]

	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getPreBalance(self):
		return self.PreBalance
	def getCurrMargin(self):
		return self.CurrMargin
	def getCloseProfit(self):
		return self.CloseProfit
	def getBalance(self):
		return self.Balance
	def getDeposit(self):
		return self.Deposit
	def getWithdraw(self):
		return self.Withdraw
	def getAvailable(self):
		return self.Available
	def getReserve(self):
		return self.Reserve
	def getFrozenMargin(self):
		return self.FrozenMargin

class CThostFtdcQryCFMMCBrokerKeyField(Structure):
	"""查询保证金监管系统经纪公司密钥"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')

class CThostFtdcCFMMCBrokerKeyField(Structure):
	"""保证金监管系统经纪公司密钥"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#经纪公司统一编码
		("ParticipantID",c_char*11),
		#密钥生成日期
		("CreateDate",c_char*9),
		#密钥生成时间
		("CreateTime",c_char*9),
		#密钥编号
		("KeyID",c_int32),
		#动态密钥
		("CurrentKey",c_char*21),
		#动态密钥类型
		("KeyKind",c_char),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getCreateDate(self):
		return self.CreateDate.decode('ascii')
	def getCreateTime(self):
		return self.CreateTime.decode('ascii')
	def getKeyID(self):
		return self.KeyID
	def getCurrentKey(self):
		return self.CurrentKey.decode('ascii')
	def getKeyKind(self):
		return CFMMCKeyKindType(ord(self.KeyKind))

class CThostFtdcCFMMCTradingAccountKeyField(Structure):
	"""保证金监管系统经纪公司资金账户密钥"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#经纪公司统一编码
		("ParticipantID",c_char*11),
		#投资者帐号
		("AccountID",c_char*13),
		#密钥编号
		("KeyID",c_int32),
		#动态密钥
		("CurrentKey",c_char*21),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getKeyID(self):
		return self.KeyID
	def getCurrentKey(self):
		return self.CurrentKey.decode('ascii')

class CThostFtdcQryCFMMCTradingAccountKeyField(Structure):
	"""请求查询保证金监管系统经纪公司资金账户密钥"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')

class CThostFtdcBrokerUserOTPParamField(Structure):
	"""用户动态令牌参数"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#动态令牌提供商
		("OTPVendorsID",c_char*2),
		#动态令牌序列号
		("SerialNumber",c_char*17),
		#令牌密钥
		("AuthKey",c_char*41),
		#漂移值
		("LastDrift",c_int32),
		#成功值
		("LastSuccess",c_int32),
		#动态令牌类型
		("OTPType",c_char),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getOTPVendorsID(self):
		return self.OTPVendorsID.decode('ascii')
	def getSerialNumber(self):
		return self.SerialNumber.decode('ascii')
	def getAuthKey(self):
		return self.AuthKey.decode('ascii')
	def getLastDrift(self):
		return self.LastDrift
	def getLastSuccess(self):
		return self.LastSuccess
	def getOTPType(self):
		return OTPTypeType(ord(self.OTPType))

class CThostFtdcManualSyncBrokerUserOTPField(Structure):
	"""手工同步用户动态令牌"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#动态令牌类型
		("OTPType",c_char),
		#第一个动态密码
		("FirstOTP",c_char*41),
		#第二个动态密码
		("SecondOTP",c_char*41),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getOTPType(self):
		return OTPTypeType(ord(self.OTPType))
	def getFirstOTP(self):
		return self.FirstOTP.decode('ascii')
	def getSecondOTP(self):
		return self.SecondOTP.decode('ascii')

class CThostFtdcCommRateModelField(Structure):
	"""投资者手续费率模板"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#手续费率模板代码
		("CommModelID",c_char*13),
		#模板名称
		("CommModelName",c_char*161),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getCommModelID(self):
		return self.CommModelID.decode('ascii')
	def getCommModelName(self):
		return self.CommModelName.decode('ascii')

class CThostFtdcQryCommRateModelField(Structure):
	"""请求查询投资者手续费率模板"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#手续费率模板代码
		("CommModelID",c_char*13),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getCommModelID(self):
		return self.CommModelID.decode('ascii')

class CThostFtdcMarginModelField(Structure):
	"""投资者保证金率模板"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#保证金率模板代码
		("MarginModelID",c_char*13),
		#模板名称
		("MarginModelName",c_char*161),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getMarginModelID(self):
		return self.MarginModelID.decode('ascii')
	def getMarginModelName(self):
		return self.MarginModelName.decode('ascii')

class CThostFtdcQryMarginModelField(Structure):
	"""请求查询投资者保证金率模板"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#保证金率模板代码
		("MarginModelID",c_char*13),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getMarginModelID(self):
		return self.MarginModelID.decode('ascii')

class CThostFtdcEWarrantOffsetField(Structure):
	"""仓单折抵信息"""
	_fields_ = [
		#交易日期
		("TradingDay",c_char*9),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		#合约代码
		("InstrumentID",c_char*31),
		#买卖方向
		("Direction",c_char),
		#投机套保标志
		("HedgeFlag",c_char),
		#数量
		("Volume",c_int32),
		]

	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getVolume(self):
		return self.Volume

class CThostFtdcQryEWarrantOffsetField(Structure):
	"""查询仓单折抵信息"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getExchangeID(self):
		return self.ExchangeID.decode('ascii')
	def getInstrumentID(self):
		return self.InstrumentID.decode('ascii')

class CThostFtdcQryInvestorProductGroupMarginField(Structure):
	"""查询投资者品种/跨品种保证金"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#品种/跨品种标示
		("ProductGroupID",c_char*31),
		#投机套保标志
		("HedgeFlag",c_char),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getProductGroupID(self):
		return self.ProductGroupID.decode('ascii')
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))

class CThostFtdcInvestorProductGroupMarginField(Structure):
	"""投资者品种/跨品种保证金"""
	_fields_ = [
		#品种/跨品种标示
		("ProductGroupID",c_char*31),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#冻结的保证金
		("FrozenMargin",c_double),
		#多头冻结的保证金
		("LongFrozenMargin",c_double),
		#空头冻结的保证金
		("ShortFrozenMargin",c_double),
		#占用的保证金
		("UseMargin",c_double),
		#多头保证金
		("LongUseMargin",c_double),
		#空头保证金
		("ShortUseMargin",c_double),
		#交易所保证金
		("ExchMargin",c_double),
		#交易所多头保证金
		("LongExchMargin",c_double),
		#交易所空头保证金
		("ShortExchMargin",c_double),
		#平仓盈亏
		("CloseProfit",c_double),
		#冻结的手续费
		("FrozenCommission",c_double),
		#手续费
		("Commission",c_double),
		#冻结的资金
		("FrozenCash",c_double),
		#资金差额
		("CashIn",c_double),
		#持仓盈亏
		("PositionProfit",c_double),
		#折抵总金额
		("OffsetAmount",c_double),
		#多头折抵总金额
		("LongOffsetAmount",c_double),
		#空头折抵总金额
		("ShortOffsetAmount",c_double),
		#交易所折抵总金额
		("ExchOffsetAmount",c_double),
		#交易所多头折抵总金额
		("LongExchOffsetAmount",c_double),
		#交易所空头折抵总金额
		("ShortExchOffsetAmount",c_double),
		#投机套保标志
		("HedgeFlag",c_char),
		]

	def getProductGroupID(self):
		return self.ProductGroupID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getSettlementID(self):
		return self.SettlementID
	def getFrozenMargin(self):
		return self.FrozenMargin
	def getLongFrozenMargin(self):
		return self.LongFrozenMargin
	def getShortFrozenMargin(self):
		return self.ShortFrozenMargin
	def getUseMargin(self):
		return self.UseMargin
	def getLongUseMargin(self):
		return self.LongUseMargin
	def getShortUseMargin(self):
		return self.ShortUseMargin
	def getExchMargin(self):
		return self.ExchMargin
	def getLongExchMargin(self):
		return self.LongExchMargin
	def getShortExchMargin(self):
		return self.ShortExchMargin
	def getCloseProfit(self):
		return self.CloseProfit
	def getFrozenCommission(self):
		return self.FrozenCommission
	def getCommission(self):
		return self.Commission
	def getFrozenCash(self):
		return self.FrozenCash
	def getCashIn(self):
		return self.CashIn
	def getPositionProfit(self):
		return self.PositionProfit
	def getOffsetAmount(self):
		return self.OffsetAmount
	def getLongOffsetAmount(self):
		return self.LongOffsetAmount
	def getShortOffsetAmount(self):
		return self.ShortOffsetAmount
	def getExchOffsetAmount(self):
		return self.ExchOffsetAmount
	def getLongExchOffsetAmount(self):
		return self.LongExchOffsetAmount
	def getShortExchOffsetAmount(self):
		return self.ShortExchOffsetAmount
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))

class CThostFtdcQueryCFMMCTradingAccountTokenField(Structure):
	"""查询监控中心用户令牌"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')

class CThostFtdcCFMMCTradingAccountTokenField(Structure):
	"""监控中心用户令牌"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#经纪公司统一编码
		("ParticipantID",c_char*11),
		#投资者帐号
		("AccountID",c_char*13),
		#密钥编号
		("KeyID",c_int32),
		#动态令牌
		("Token",c_char*21),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getParticipantID(self):
		return self.ParticipantID.decode('ascii')
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getKeyID(self):
		return self.KeyID
	def getToken(self):
		return self.Token.decode('ascii')

class CThostFtdcReqOpenAccountField(Structure):
	"""转帐开户请求"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#性别
		("Gender",c_char),
		#国家代码
		("CountryCode",c_char*21),
		#客户类型
		("CustType",c_char),
		#地址
		("Address",c_char*101),
		#邮编
		("ZipCode",c_char*7),
		#电话号码
		("Telephone",c_char*41),
		#手机
		("MobilePhone",c_char*21),
		#传真
		("Fax",c_char*41),
		#电子邮件
		("EMail",c_char*41),
		#资金账户状态
		("MoneyAccountStatus",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#安装编号
		("InstallID",c_int32),
		#验证客户证件号码标志
		("VerifyCertNoFlag",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#汇钞标志
		("CashExchangeCode",c_char),
		#摘要
		("Digest",c_char*36),
		#银行帐号类型
		("BankAccType",c_char),
		#渠道标志
		("DeviceID",c_char*3),
		#期货单位帐号类型
		("BankSecuAccType",c_char),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#期货单位帐号
		("BankSecuAcc",c_char*41),
		#银行密码标志
		("BankPwdFlag",c_char),
		#期货资金密码核对标志
		("SecuPwdFlag",c_char),
		#交易柜员
		("OperNo",c_char*17),
		#交易ID
		("TID",c_int32),
		#用户标识
		("UserID",c_char*16),
		]

	def getTradeCode(self):
		return self.TradeCode.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBranchID(self):
		return self.BankBranchID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBrokerBranchID(self):
		return self.BrokerBranchID.decode('ascii')
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getBankSerial(self):
		return self.BankSerial.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getCustomerName(self):
		return self.CustomerName.decode('ascii')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return self.IdentifiedCardNo.decode('ascii')
	def getGender(self):
		return GenderType(ord(self.Gender))
	def getCountryCode(self):
		return self.CountryCode.decode('ascii')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getAddress(self):
		return self.Address.decode('ascii')
	def getZipCode(self):
		return self.ZipCode.decode('ascii')
	def getTelephone(self):
		return self.Telephone.decode('ascii')
	def getMobilePhone(self):
		return self.MobilePhone.decode('ascii')
	def getFax(self):
		return self.Fax.decode('ascii')
	def getEMail(self):
		return self.EMail.decode('ascii')
	def getMoneyAccountStatus(self):
		return MoneyAccountStatusType(ord(self.MoneyAccountStatus))
	def getBankAccount(self):
		return self.BankAccount.decode('ascii')
	def getBankPassWord(self):
		return self.BankPassWord.decode('ascii')
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getPassword(self):
		return self.Password.decode('ascii')
	def getInstallID(self):
		return self.InstallID
	def getVerifyCertNoFlag(self):
		return YesNoIndicatorType(ord(self.VerifyCertNoFlag))
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')
	def getCashExchangeCode(self):
		return CashExchangeCodeType(ord(self.CashExchangeCode))
	def getDigest(self):
		return self.Digest.decode('ascii')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getDeviceID(self):
		return self.DeviceID.decode('ascii')
	def getBankSecuAccType(self):
		return BankAccTypeType(ord(self.BankSecuAccType))
	def getBrokerIDByBank(self):
		return self.BrokerIDByBank.decode('ascii')
	def getBankSecuAcc(self):
		return self.BankSecuAcc.decode('ascii')
	def getBankPwdFlag(self):
		return PwdFlagType(ord(self.BankPwdFlag))
	def getSecuPwdFlag(self):
		return PwdFlagType(ord(self.SecuPwdFlag))
	def getOperNo(self):
		return self.OperNo.decode('ascii')
	def getTID(self):
		return self.TID
	def getUserID(self):
		return self.UserID.decode('ascii')

class CThostFtdcReqCancelAccountField(Structure):
	"""转帐销户请求"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#性别
		("Gender",c_char),
		#国家代码
		("CountryCode",c_char*21),
		#客户类型
		("CustType",c_char),
		#地址
		("Address",c_char*101),
		#邮编
		("ZipCode",c_char*7),
		#电话号码
		("Telephone",c_char*41),
		#手机
		("MobilePhone",c_char*21),
		#传真
		("Fax",c_char*41),
		#电子邮件
		("EMail",c_char*41),
		#资金账户状态
		("MoneyAccountStatus",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#安装编号
		("InstallID",c_int32),
		#验证客户证件号码标志
		("VerifyCertNoFlag",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#汇钞标志
		("CashExchangeCode",c_char),
		#摘要
		("Digest",c_char*36),
		#银行帐号类型
		("BankAccType",c_char),
		#渠道标志
		("DeviceID",c_char*3),
		#期货单位帐号类型
		("BankSecuAccType",c_char),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#期货单位帐号
		("BankSecuAcc",c_char*41),
		#银行密码标志
		("BankPwdFlag",c_char),
		#期货资金密码核对标志
		("SecuPwdFlag",c_char),
		#交易柜员
		("OperNo",c_char*17),
		#交易ID
		("TID",c_int32),
		#用户标识
		("UserID",c_char*16),
		]

	def getTradeCode(self):
		return self.TradeCode.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBranchID(self):
		return self.BankBranchID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBrokerBranchID(self):
		return self.BrokerBranchID.decode('ascii')
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getBankSerial(self):
		return self.BankSerial.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getCustomerName(self):
		return self.CustomerName.decode('ascii')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return self.IdentifiedCardNo.decode('ascii')
	def getGender(self):
		return GenderType(ord(self.Gender))
	def getCountryCode(self):
		return self.CountryCode.decode('ascii')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getAddress(self):
		return self.Address.decode('ascii')
	def getZipCode(self):
		return self.ZipCode.decode('ascii')
	def getTelephone(self):
		return self.Telephone.decode('ascii')
	def getMobilePhone(self):
		return self.MobilePhone.decode('ascii')
	def getFax(self):
		return self.Fax.decode('ascii')
	def getEMail(self):
		return self.EMail.decode('ascii')
	def getMoneyAccountStatus(self):
		return MoneyAccountStatusType(ord(self.MoneyAccountStatus))
	def getBankAccount(self):
		return self.BankAccount.decode('ascii')
	def getBankPassWord(self):
		return self.BankPassWord.decode('ascii')
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getPassword(self):
		return self.Password.decode('ascii')
	def getInstallID(self):
		return self.InstallID
	def getVerifyCertNoFlag(self):
		return YesNoIndicatorType(ord(self.VerifyCertNoFlag))
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')
	def getCashExchangeCode(self):
		return CashExchangeCodeType(ord(self.CashExchangeCode))
	def getDigest(self):
		return self.Digest.decode('ascii')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getDeviceID(self):
		return self.DeviceID.decode('ascii')
	def getBankSecuAccType(self):
		return BankAccTypeType(ord(self.BankSecuAccType))
	def getBrokerIDByBank(self):
		return self.BrokerIDByBank.decode('ascii')
	def getBankSecuAcc(self):
		return self.BankSecuAcc.decode('ascii')
	def getBankPwdFlag(self):
		return PwdFlagType(ord(self.BankPwdFlag))
	def getSecuPwdFlag(self):
		return PwdFlagType(ord(self.SecuPwdFlag))
	def getOperNo(self):
		return self.OperNo.decode('ascii')
	def getTID(self):
		return self.TID
	def getUserID(self):
		return self.UserID.decode('ascii')

class CThostFtdcReqChangeAccountField(Structure):
	"""变更银行账户请求"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#性别
		("Gender",c_char),
		#国家代码
		("CountryCode",c_char*21),
		#客户类型
		("CustType",c_char),
		#地址
		("Address",c_char*101),
		#邮编
		("ZipCode",c_char*7),
		#电话号码
		("Telephone",c_char*41),
		#手机
		("MobilePhone",c_char*21),
		#传真
		("Fax",c_char*41),
		#电子邮件
		("EMail",c_char*41),
		#资金账户状态
		("MoneyAccountStatus",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#新银行帐号
		("NewBankAccount",c_char*41),
		#新银行密码
		("NewBankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#银行帐号类型
		("BankAccType",c_char),
		#安装编号
		("InstallID",c_int32),
		#验证客户证件号码标志
		("VerifyCertNoFlag",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#银行密码标志
		("BankPwdFlag",c_char),
		#期货资金密码核对标志
		("SecuPwdFlag",c_char),
		#交易ID
		("TID",c_int32),
		#摘要
		("Digest",c_char*36),
		]

	def getTradeCode(self):
		return self.TradeCode.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBranchID(self):
		return self.BankBranchID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBrokerBranchID(self):
		return self.BrokerBranchID.decode('ascii')
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getBankSerial(self):
		return self.BankSerial.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getCustomerName(self):
		return self.CustomerName.decode('ascii')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return self.IdentifiedCardNo.decode('ascii')
	def getGender(self):
		return GenderType(ord(self.Gender))
	def getCountryCode(self):
		return self.CountryCode.decode('ascii')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getAddress(self):
		return self.Address.decode('ascii')
	def getZipCode(self):
		return self.ZipCode.decode('ascii')
	def getTelephone(self):
		return self.Telephone.decode('ascii')
	def getMobilePhone(self):
		return self.MobilePhone.decode('ascii')
	def getFax(self):
		return self.Fax.decode('ascii')
	def getEMail(self):
		return self.EMail.decode('ascii')
	def getMoneyAccountStatus(self):
		return MoneyAccountStatusType(ord(self.MoneyAccountStatus))
	def getBankAccount(self):
		return self.BankAccount.decode('ascii')
	def getBankPassWord(self):
		return self.BankPassWord.decode('ascii')
	def getNewBankAccount(self):
		return self.NewBankAccount.decode('ascii')
	def getNewBankPassWord(self):
		return self.NewBankPassWord.decode('ascii')
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getPassword(self):
		return self.Password.decode('ascii')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getInstallID(self):
		return self.InstallID
	def getVerifyCertNoFlag(self):
		return YesNoIndicatorType(ord(self.VerifyCertNoFlag))
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')
	def getBrokerIDByBank(self):
		return self.BrokerIDByBank.decode('ascii')
	def getBankPwdFlag(self):
		return PwdFlagType(ord(self.BankPwdFlag))
	def getSecuPwdFlag(self):
		return PwdFlagType(ord(self.SecuPwdFlag))
	def getTID(self):
		return self.TID
	def getDigest(self):
		return self.Digest.decode('ascii')

class CThostFtdcReqTransferField(Structure):
	"""转账请求"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#客户类型
		("CustType",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#安装编号
		("InstallID",c_int32),
		#期货公司流水号
		("FutureSerial",c_int32),
		#用户标识
		("UserID",c_char*16),
		#验证客户证件号码标志
		("VerifyCertNoFlag",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#转帐金额
		("TradeAmount",c_double),
		#期货可取金额
		("FutureFetchAmount",c_double),
		#费用支付标志
		("FeePayFlag",c_char),
		#应收客户费用
		("CustFee",c_double),
		#应收期货公司费用
		("BrokerFee",c_double),
		#发送方给接收方的消息
		("Message",c_char*129),
		#摘要
		("Digest",c_char*36),
		#银行帐号类型
		("BankAccType",c_char),
		#渠道标志
		("DeviceID",c_char*3),
		#期货单位帐号类型
		("BankSecuAccType",c_char),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#期货单位帐号
		("BankSecuAcc",c_char*41),
		#银行密码标志
		("BankPwdFlag",c_char),
		#期货资金密码核对标志
		("SecuPwdFlag",c_char),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		#转账交易状态
		("TransferStatus",c_char),
		]

	def getTradeCode(self):
		return self.TradeCode.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBranchID(self):
		return self.BankBranchID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBrokerBranchID(self):
		return self.BrokerBranchID.decode('ascii')
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getBankSerial(self):
		return self.BankSerial.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getCustomerName(self):
		return self.CustomerName.decode('ascii')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return self.IdentifiedCardNo.decode('ascii')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getBankAccount(self):
		return self.BankAccount.decode('ascii')
	def getBankPassWord(self):
		return self.BankPassWord.decode('ascii')
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getPassword(self):
		return self.Password.decode('ascii')
	def getInstallID(self):
		return self.InstallID
	def getFutureSerial(self):
		return self.FutureSerial
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getVerifyCertNoFlag(self):
		return YesNoIndicatorType(ord(self.VerifyCertNoFlag))
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')
	def getTradeAmount(self):
		return self.TradeAmount
	def getFutureFetchAmount(self):
		return self.FutureFetchAmount
	def getFeePayFlag(self):
		return FeePayFlagType(ord(self.FeePayFlag))
	def getCustFee(self):
		return self.CustFee
	def getBrokerFee(self):
		return self.BrokerFee
	def getMessage(self):
		return self.Message.decode('ascii')
	def getDigest(self):
		return self.Digest.decode('ascii')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getDeviceID(self):
		return self.DeviceID.decode('ascii')
	def getBankSecuAccType(self):
		return BankAccTypeType(ord(self.BankSecuAccType))
	def getBrokerIDByBank(self):
		return self.BrokerIDByBank.decode('ascii')
	def getBankSecuAcc(self):
		return self.BankSecuAcc.decode('ascii')
	def getBankPwdFlag(self):
		return PwdFlagType(ord(self.BankPwdFlag))
	def getSecuPwdFlag(self):
		return PwdFlagType(ord(self.SecuPwdFlag))
	def getOperNo(self):
		return self.OperNo.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID
	def getTransferStatus(self):
		return TransferStatusType(ord(self.TransferStatus))

class CThostFtdcRspTransferField(Structure):
	"""银行发起银行资金转期货响应"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#客户类型
		("CustType",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#安装编号
		("InstallID",c_int32),
		#期货公司流水号
		("FutureSerial",c_int32),
		#用户标识
		("UserID",c_char*16),
		#验证客户证件号码标志
		("VerifyCertNoFlag",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#转帐金额
		("TradeAmount",c_double),
		#期货可取金额
		("FutureFetchAmount",c_double),
		#费用支付标志
		("FeePayFlag",c_char),
		#应收客户费用
		("CustFee",c_double),
		#应收期货公司费用
		("BrokerFee",c_double),
		#发送方给接收方的消息
		("Message",c_char*129),
		#摘要
		("Digest",c_char*36),
		#银行帐号类型
		("BankAccType",c_char),
		#渠道标志
		("DeviceID",c_char*3),
		#期货单位帐号类型
		("BankSecuAccType",c_char),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#期货单位帐号
		("BankSecuAcc",c_char*41),
		#银行密码标志
		("BankPwdFlag",c_char),
		#期货资金密码核对标志
		("SecuPwdFlag",c_char),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		#转账交易状态
		("TransferStatus",c_char),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getTradeCode(self):
		return self.TradeCode.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBranchID(self):
		return self.BankBranchID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBrokerBranchID(self):
		return self.BrokerBranchID.decode('ascii')
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getBankSerial(self):
		return self.BankSerial.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getCustomerName(self):
		return self.CustomerName.decode('ascii')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return self.IdentifiedCardNo.decode('ascii')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getBankAccount(self):
		return self.BankAccount.decode('ascii')
	def getBankPassWord(self):
		return self.BankPassWord.decode('ascii')
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getPassword(self):
		return self.Password.decode('ascii')
	def getInstallID(self):
		return self.InstallID
	def getFutureSerial(self):
		return self.FutureSerial
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getVerifyCertNoFlag(self):
		return YesNoIndicatorType(ord(self.VerifyCertNoFlag))
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')
	def getTradeAmount(self):
		return self.TradeAmount
	def getFutureFetchAmount(self):
		return self.FutureFetchAmount
	def getFeePayFlag(self):
		return FeePayFlagType(ord(self.FeePayFlag))
	def getCustFee(self):
		return self.CustFee
	def getBrokerFee(self):
		return self.BrokerFee
	def getMessage(self):
		return self.Message.decode('ascii')
	def getDigest(self):
		return self.Digest.decode('ascii')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getDeviceID(self):
		return self.DeviceID.decode('ascii')
	def getBankSecuAccType(self):
		return BankAccTypeType(ord(self.BankSecuAccType))
	def getBrokerIDByBank(self):
		return self.BrokerIDByBank.decode('ascii')
	def getBankSecuAcc(self):
		return self.BankSecuAcc.decode('ascii')
	def getBankPwdFlag(self):
		return PwdFlagType(ord(self.BankPwdFlag))
	def getSecuPwdFlag(self):
		return PwdFlagType(ord(self.SecuPwdFlag))
	def getOperNo(self):
		return self.OperNo.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID
	def getTransferStatus(self):
		return TransferStatusType(ord(self.TransferStatus))
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return self.ErrorMsg.decode('GB2312')

class CThostFtdcReqRepealField(Structure):
	"""冲正请求"""
	_fields_ = [
		#冲正时间间隔
		("RepealTimeInterval",c_int32),
		#已经冲正次数
		("RepealedTimes",c_int32),
		#银行冲正标志
		("BankRepealFlag",c_char),
		#期商冲正标志
		("BrokerRepealFlag",c_char),
		#被冲正平台流水号
		("PlateRepealSerial",c_int32),
		#被冲正银行流水号
		("BankRepealSerial",c_char*13),
		#被冲正期货流水号
		("FutureRepealSerial",c_int32),
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#客户类型
		("CustType",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#安装编号
		("InstallID",c_int32),
		#期货公司流水号
		("FutureSerial",c_int32),
		#用户标识
		("UserID",c_char*16),
		#验证客户证件号码标志
		("VerifyCertNoFlag",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#转帐金额
		("TradeAmount",c_double),
		#期货可取金额
		("FutureFetchAmount",c_double),
		#费用支付标志
		("FeePayFlag",c_char),
		#应收客户费用
		("CustFee",c_double),
		#应收期货公司费用
		("BrokerFee",c_double),
		#发送方给接收方的消息
		("Message",c_char*129),
		#摘要
		("Digest",c_char*36),
		#银行帐号类型
		("BankAccType",c_char),
		#渠道标志
		("DeviceID",c_char*3),
		#期货单位帐号类型
		("BankSecuAccType",c_char),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#期货单位帐号
		("BankSecuAcc",c_char*41),
		#银行密码标志
		("BankPwdFlag",c_char),
		#期货资金密码核对标志
		("SecuPwdFlag",c_char),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		#转账交易状态
		("TransferStatus",c_char),
		]

	def getRepealTimeInterval(self):
		return self.RepealTimeInterval
	def getRepealedTimes(self):
		return self.RepealedTimes
	def getBankRepealFlag(self):
		return BankRepealFlagType(ord(self.BankRepealFlag))
	def getBrokerRepealFlag(self):
		return BrokerRepealFlagType(ord(self.BrokerRepealFlag))
	def getPlateRepealSerial(self):
		return self.PlateRepealSerial
	def getBankRepealSerial(self):
		return self.BankRepealSerial.decode('ascii')
	def getFutureRepealSerial(self):
		return self.FutureRepealSerial
	def getTradeCode(self):
		return self.TradeCode.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBranchID(self):
		return self.BankBranchID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBrokerBranchID(self):
		return self.BrokerBranchID.decode('ascii')
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getBankSerial(self):
		return self.BankSerial.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getCustomerName(self):
		return self.CustomerName.decode('ascii')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return self.IdentifiedCardNo.decode('ascii')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getBankAccount(self):
		return self.BankAccount.decode('ascii')
	def getBankPassWord(self):
		return self.BankPassWord.decode('ascii')
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getPassword(self):
		return self.Password.decode('ascii')
	def getInstallID(self):
		return self.InstallID
	def getFutureSerial(self):
		return self.FutureSerial
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getVerifyCertNoFlag(self):
		return YesNoIndicatorType(ord(self.VerifyCertNoFlag))
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')
	def getTradeAmount(self):
		return self.TradeAmount
	def getFutureFetchAmount(self):
		return self.FutureFetchAmount
	def getFeePayFlag(self):
		return FeePayFlagType(ord(self.FeePayFlag))
	def getCustFee(self):
		return self.CustFee
	def getBrokerFee(self):
		return self.BrokerFee
	def getMessage(self):
		return self.Message.decode('ascii')
	def getDigest(self):
		return self.Digest.decode('ascii')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getDeviceID(self):
		return self.DeviceID.decode('ascii')
	def getBankSecuAccType(self):
		return BankAccTypeType(ord(self.BankSecuAccType))
	def getBrokerIDByBank(self):
		return self.BrokerIDByBank.decode('ascii')
	def getBankSecuAcc(self):
		return self.BankSecuAcc.decode('ascii')
	def getBankPwdFlag(self):
		return PwdFlagType(ord(self.BankPwdFlag))
	def getSecuPwdFlag(self):
		return PwdFlagType(ord(self.SecuPwdFlag))
	def getOperNo(self):
		return self.OperNo.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID
	def getTransferStatus(self):
		return TransferStatusType(ord(self.TransferStatus))

class CThostFtdcRspRepealField(Structure):
	"""冲正响应"""
	_fields_ = [
		#冲正时间间隔
		("RepealTimeInterval",c_int32),
		#已经冲正次数
		("RepealedTimes",c_int32),
		#银行冲正标志
		("BankRepealFlag",c_char),
		#期商冲正标志
		("BrokerRepealFlag",c_char),
		#被冲正平台流水号
		("PlateRepealSerial",c_int32),
		#被冲正银行流水号
		("BankRepealSerial",c_char*13),
		#被冲正期货流水号
		("FutureRepealSerial",c_int32),
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#客户类型
		("CustType",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#安装编号
		("InstallID",c_int32),
		#期货公司流水号
		("FutureSerial",c_int32),
		#用户标识
		("UserID",c_char*16),
		#验证客户证件号码标志
		("VerifyCertNoFlag",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#转帐金额
		("TradeAmount",c_double),
		#期货可取金额
		("FutureFetchAmount",c_double),
		#费用支付标志
		("FeePayFlag",c_char),
		#应收客户费用
		("CustFee",c_double),
		#应收期货公司费用
		("BrokerFee",c_double),
		#发送方给接收方的消息
		("Message",c_char*129),
		#摘要
		("Digest",c_char*36),
		#银行帐号类型
		("BankAccType",c_char),
		#渠道标志
		("DeviceID",c_char*3),
		#期货单位帐号类型
		("BankSecuAccType",c_char),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#期货单位帐号
		("BankSecuAcc",c_char*41),
		#银行密码标志
		("BankPwdFlag",c_char),
		#期货资金密码核对标志
		("SecuPwdFlag",c_char),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		#转账交易状态
		("TransferStatus",c_char),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getRepealTimeInterval(self):
		return self.RepealTimeInterval
	def getRepealedTimes(self):
		return self.RepealedTimes
	def getBankRepealFlag(self):
		return BankRepealFlagType(ord(self.BankRepealFlag))
	def getBrokerRepealFlag(self):
		return BrokerRepealFlagType(ord(self.BrokerRepealFlag))
	def getPlateRepealSerial(self):
		return self.PlateRepealSerial
	def getBankRepealSerial(self):
		return self.BankRepealSerial.decode('ascii')
	def getFutureRepealSerial(self):
		return self.FutureRepealSerial
	def getTradeCode(self):
		return self.TradeCode.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBranchID(self):
		return self.BankBranchID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBrokerBranchID(self):
		return self.BrokerBranchID.decode('ascii')
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getBankSerial(self):
		return self.BankSerial.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getCustomerName(self):
		return self.CustomerName.decode('ascii')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return self.IdentifiedCardNo.decode('ascii')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getBankAccount(self):
		return self.BankAccount.decode('ascii')
	def getBankPassWord(self):
		return self.BankPassWord.decode('ascii')
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getPassword(self):
		return self.Password.decode('ascii')
	def getInstallID(self):
		return self.InstallID
	def getFutureSerial(self):
		return self.FutureSerial
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getVerifyCertNoFlag(self):
		return YesNoIndicatorType(ord(self.VerifyCertNoFlag))
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')
	def getTradeAmount(self):
		return self.TradeAmount
	def getFutureFetchAmount(self):
		return self.FutureFetchAmount
	def getFeePayFlag(self):
		return FeePayFlagType(ord(self.FeePayFlag))
	def getCustFee(self):
		return self.CustFee
	def getBrokerFee(self):
		return self.BrokerFee
	def getMessage(self):
		return self.Message.decode('ascii')
	def getDigest(self):
		return self.Digest.decode('ascii')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getDeviceID(self):
		return self.DeviceID.decode('ascii')
	def getBankSecuAccType(self):
		return BankAccTypeType(ord(self.BankSecuAccType))
	def getBrokerIDByBank(self):
		return self.BrokerIDByBank.decode('ascii')
	def getBankSecuAcc(self):
		return self.BankSecuAcc.decode('ascii')
	def getBankPwdFlag(self):
		return PwdFlagType(ord(self.BankPwdFlag))
	def getSecuPwdFlag(self):
		return PwdFlagType(ord(self.SecuPwdFlag))
	def getOperNo(self):
		return self.OperNo.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID
	def getTransferStatus(self):
		return TransferStatusType(ord(self.TransferStatus))
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return self.ErrorMsg.decode('GB2312')

class CThostFtdcReqQueryAccountField(Structure):
	"""查询账户信息请求"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#客户类型
		("CustType",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#期货公司流水号
		("FutureSerial",c_int32),
		#安装编号
		("InstallID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#验证客户证件号码标志
		("VerifyCertNoFlag",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#摘要
		("Digest",c_char*36),
		#银行帐号类型
		("BankAccType",c_char),
		#渠道标志
		("DeviceID",c_char*3),
		#期货单位帐号类型
		("BankSecuAccType",c_char),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#期货单位帐号
		("BankSecuAcc",c_char*41),
		#银行密码标志
		("BankPwdFlag",c_char),
		#期货资金密码核对标志
		("SecuPwdFlag",c_char),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		]

	def getTradeCode(self):
		return self.TradeCode.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBranchID(self):
		return self.BankBranchID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBrokerBranchID(self):
		return self.BrokerBranchID.decode('ascii')
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getBankSerial(self):
		return self.BankSerial.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getCustomerName(self):
		return self.CustomerName.decode('ascii')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return self.IdentifiedCardNo.decode('ascii')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getBankAccount(self):
		return self.BankAccount.decode('ascii')
	def getBankPassWord(self):
		return self.BankPassWord.decode('ascii')
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getPassword(self):
		return self.Password.decode('ascii')
	def getFutureSerial(self):
		return self.FutureSerial
	def getInstallID(self):
		return self.InstallID
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getVerifyCertNoFlag(self):
		return YesNoIndicatorType(ord(self.VerifyCertNoFlag))
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')
	def getDigest(self):
		return self.Digest.decode('ascii')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getDeviceID(self):
		return self.DeviceID.decode('ascii')
	def getBankSecuAccType(self):
		return BankAccTypeType(ord(self.BankSecuAccType))
	def getBrokerIDByBank(self):
		return self.BrokerIDByBank.decode('ascii')
	def getBankSecuAcc(self):
		return self.BankSecuAcc.decode('ascii')
	def getBankPwdFlag(self):
		return PwdFlagType(ord(self.BankPwdFlag))
	def getSecuPwdFlag(self):
		return PwdFlagType(ord(self.SecuPwdFlag))
	def getOperNo(self):
		return self.OperNo.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID

class CThostFtdcRspQueryAccountField(Structure):
	"""查询账户信息响应"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#客户类型
		("CustType",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#期货公司流水号
		("FutureSerial",c_int32),
		#安装编号
		("InstallID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#验证客户证件号码标志
		("VerifyCertNoFlag",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#摘要
		("Digest",c_char*36),
		#银行帐号类型
		("BankAccType",c_char),
		#渠道标志
		("DeviceID",c_char*3),
		#期货单位帐号类型
		("BankSecuAccType",c_char),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#期货单位帐号
		("BankSecuAcc",c_char*41),
		#银行密码标志
		("BankPwdFlag",c_char),
		#期货资金密码核对标志
		("SecuPwdFlag",c_char),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		#银行可用金额
		("BankUseAmount",c_double),
		#银行可取金额
		("BankFetchAmount",c_double),
		]

	def getTradeCode(self):
		return self.TradeCode.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBranchID(self):
		return self.BankBranchID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBrokerBranchID(self):
		return self.BrokerBranchID.decode('ascii')
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getBankSerial(self):
		return self.BankSerial.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getCustomerName(self):
		return self.CustomerName.decode('ascii')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return self.IdentifiedCardNo.decode('ascii')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getBankAccount(self):
		return self.BankAccount.decode('ascii')
	def getBankPassWord(self):
		return self.BankPassWord.decode('ascii')
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getPassword(self):
		return self.Password.decode('ascii')
	def getFutureSerial(self):
		return self.FutureSerial
	def getInstallID(self):
		return self.InstallID
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getVerifyCertNoFlag(self):
		return YesNoIndicatorType(ord(self.VerifyCertNoFlag))
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')
	def getDigest(self):
		return self.Digest.decode('ascii')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getDeviceID(self):
		return self.DeviceID.decode('ascii')
	def getBankSecuAccType(self):
		return BankAccTypeType(ord(self.BankSecuAccType))
	def getBrokerIDByBank(self):
		return self.BrokerIDByBank.decode('ascii')
	def getBankSecuAcc(self):
		return self.BankSecuAcc.decode('ascii')
	def getBankPwdFlag(self):
		return PwdFlagType(ord(self.BankPwdFlag))
	def getSecuPwdFlag(self):
		return PwdFlagType(ord(self.SecuPwdFlag))
	def getOperNo(self):
		return self.OperNo.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID
	def getBankUseAmount(self):
		return self.BankUseAmount
	def getBankFetchAmount(self):
		return self.BankFetchAmount

class CThostFtdcFutureSignIOField(Structure):
	"""期商签到签退"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#安装编号
		("InstallID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#摘要
		("Digest",c_char*36),
		#币种代码
		("CurrencyID",c_char*4),
		#渠道标志
		("DeviceID",c_char*3),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		]

	def getTradeCode(self):
		return self.TradeCode.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBranchID(self):
		return self.BankBranchID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBrokerBranchID(self):
		return self.BrokerBranchID.decode('ascii')
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getBankSerial(self):
		return self.BankSerial.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getInstallID(self):
		return self.InstallID
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getDigest(self):
		return self.Digest.decode('ascii')
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')
	def getDeviceID(self):
		return self.DeviceID.decode('ascii')
	def getBrokerIDByBank(self):
		return self.BrokerIDByBank.decode('ascii')
	def getOperNo(self):
		return self.OperNo.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID

class CThostFtdcRspFutureSignInField(Structure):
	"""期商签到响应"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#安装编号
		("InstallID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#摘要
		("Digest",c_char*36),
		#币种代码
		("CurrencyID",c_char*4),
		#渠道标志
		("DeviceID",c_char*3),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		#PIN密钥
		("PinKey",c_char*129),
		#MAC密钥
		("MacKey",c_char*129),
		]

	def getTradeCode(self):
		return self.TradeCode.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBranchID(self):
		return self.BankBranchID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBrokerBranchID(self):
		return self.BrokerBranchID.decode('ascii')
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getBankSerial(self):
		return self.BankSerial.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getInstallID(self):
		return self.InstallID
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getDigest(self):
		return self.Digest.decode('ascii')
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')
	def getDeviceID(self):
		return self.DeviceID.decode('ascii')
	def getBrokerIDByBank(self):
		return self.BrokerIDByBank.decode('ascii')
	def getOperNo(self):
		return self.OperNo.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return self.ErrorMsg.decode('GB2312')
	def getPinKey(self):
		return self.PinKey.decode('ascii')
	def getMacKey(self):
		return self.MacKey.decode('ascii')

class CThostFtdcReqFutureSignOutField(Structure):
	"""期商签退请求"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#安装编号
		("InstallID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#摘要
		("Digest",c_char*36),
		#币种代码
		("CurrencyID",c_char*4),
		#渠道标志
		("DeviceID",c_char*3),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		]

	def getTradeCode(self):
		return self.TradeCode.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBranchID(self):
		return self.BankBranchID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBrokerBranchID(self):
		return self.BrokerBranchID.decode('ascii')
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getBankSerial(self):
		return self.BankSerial.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getInstallID(self):
		return self.InstallID
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getDigest(self):
		return self.Digest.decode('ascii')
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')
	def getDeviceID(self):
		return self.DeviceID.decode('ascii')
	def getBrokerIDByBank(self):
		return self.BrokerIDByBank.decode('ascii')
	def getOperNo(self):
		return self.OperNo.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID

class CThostFtdcRspFutureSignOutField(Structure):
	"""期商签退响应"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#安装编号
		("InstallID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#摘要
		("Digest",c_char*36),
		#币种代码
		("CurrencyID",c_char*4),
		#渠道标志
		("DeviceID",c_char*3),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getTradeCode(self):
		return self.TradeCode.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBranchID(self):
		return self.BankBranchID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBrokerBranchID(self):
		return self.BrokerBranchID.decode('ascii')
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getBankSerial(self):
		return self.BankSerial.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getInstallID(self):
		return self.InstallID
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getDigest(self):
		return self.Digest.decode('ascii')
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')
	def getDeviceID(self):
		return self.DeviceID.decode('ascii')
	def getBrokerIDByBank(self):
		return self.BrokerIDByBank.decode('ascii')
	def getOperNo(self):
		return self.OperNo.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return self.ErrorMsg.decode('GB2312')

class CThostFtdcReqQueryTradeResultBySerialField(Structure):
	"""查询指定流水号的交易结果请求"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#流水号
		("Reference",c_int32),
		#本流水号发布者的机构类型
		("RefrenceIssureType",c_char),
		#本流水号发布者机构编码
		("RefrenceIssure",c_char*36),
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#客户类型
		("CustType",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#币种代码
		("CurrencyID",c_char*4),
		#转帐金额
		("TradeAmount",c_double),
		#摘要
		("Digest",c_char*36),
		]

	def getTradeCode(self):
		return self.TradeCode.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBranchID(self):
		return self.BankBranchID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBrokerBranchID(self):
		return self.BrokerBranchID.decode('ascii')
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getBankSerial(self):
		return self.BankSerial.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getReference(self):
		return self.Reference
	def getRefrenceIssureType(self):
		return InstitutionTypeType(ord(self.RefrenceIssureType))
	def getRefrenceIssure(self):
		return self.RefrenceIssure.decode('ascii')
	def getCustomerName(self):
		return self.CustomerName.decode('ascii')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return self.IdentifiedCardNo.decode('ascii')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getBankAccount(self):
		return self.BankAccount.decode('ascii')
	def getBankPassWord(self):
		return self.BankPassWord.decode('ascii')
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getPassword(self):
		return self.Password.decode('ascii')
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')
	def getTradeAmount(self):
		return self.TradeAmount
	def getDigest(self):
		return self.Digest.decode('ascii')

class CThostFtdcRspQueryTradeResultBySerialField(Structure):
	"""查询指定流水号的交易结果响应"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		#流水号
		("Reference",c_int32),
		#本流水号发布者的机构类型
		("RefrenceIssureType",c_char),
		#本流水号发布者机构编码
		("RefrenceIssure",c_char*36),
		#原始返回代码
		("OriginReturnCode",c_char*7),
		#原始返回码描述
		("OriginDescrInfoForReturnCode",c_char*129),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#币种代码
		("CurrencyID",c_char*4),
		#转帐金额
		("TradeAmount",c_double),
		#摘要
		("Digest",c_char*36),
		]

	def getTradeCode(self):
		return self.TradeCode.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBranchID(self):
		return self.BankBranchID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBrokerBranchID(self):
		return self.BrokerBranchID.decode('ascii')
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getBankSerial(self):
		return self.BankSerial.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return self.ErrorMsg.decode('GB2312')
	def getReference(self):
		return self.Reference
	def getRefrenceIssureType(self):
		return InstitutionTypeType(ord(self.RefrenceIssureType))
	def getRefrenceIssure(self):
		return self.RefrenceIssure.decode('ascii')
	def getOriginReturnCode(self):
		return self.OriginReturnCode.decode('ascii')
	def getOriginDescrInfoForReturnCode(self):
		return self.OriginDescrInfoForReturnCode.decode('ascii')
	def getBankAccount(self):
		return self.BankAccount.decode('ascii')
	def getBankPassWord(self):
		return self.BankPassWord.decode('ascii')
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getPassword(self):
		return self.Password.decode('ascii')
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')
	def getTradeAmount(self):
		return self.TradeAmount
	def getDigest(self):
		return self.Digest.decode('ascii')

class CThostFtdcReqDayEndFileReadyField(Structure):
	"""日终文件就绪请求"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#文件业务功能
		("FileBusinessCode",c_char),
		#摘要
		("Digest",c_char*36),
		]

	def getTradeCode(self):
		return self.TradeCode.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBranchID(self):
		return self.BankBranchID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBrokerBranchID(self):
		return self.BrokerBranchID.decode('ascii')
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getBankSerial(self):
		return self.BankSerial.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getFileBusinessCode(self):
		return FileBusinessCodeType(ord(self.FileBusinessCode))
	def getDigest(self):
		return self.Digest.decode('ascii')

class CThostFtdcReturnResultField(Structure):
	"""返回结果"""
	_fields_ = [
		#返回代码
		("ReturnCode",c_char*7),
		#返回码描述
		("DescrInfoForReturnCode",c_char*129),
		]

	def getReturnCode(self):
		return self.ReturnCode.decode('ascii')
	def getDescrInfoForReturnCode(self):
		return self.DescrInfoForReturnCode.decode('ascii')

class CThostFtdcVerifyFuturePasswordField(Structure):
	"""验证期货资金密码"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#安装编号
		("InstallID",c_int32),
		#交易ID
		("TID",c_int32),
		#币种代码
		("CurrencyID",c_char*4),
		]

	def getTradeCode(self):
		return self.TradeCode.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBranchID(self):
		return self.BankBranchID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBrokerBranchID(self):
		return self.BrokerBranchID.decode('ascii')
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getBankSerial(self):
		return self.BankSerial.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getPassword(self):
		return self.Password.decode('ascii')
	def getBankAccount(self):
		return self.BankAccount.decode('ascii')
	def getBankPassWord(self):
		return self.BankPassWord.decode('ascii')
	def getInstallID(self):
		return self.InstallID
	def getTID(self):
		return self.TID
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')

class CThostFtdcVerifyCustInfoField(Structure):
	"""验证客户信息"""
	_fields_ = [
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#客户类型
		("CustType",c_char),
		]

	def getCustomerName(self):
		return self.CustomerName.decode('ascii')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return self.IdentifiedCardNo.decode('ascii')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))

class CThostFtdcVerifyFuturePasswordAndCustInfoField(Structure):
	"""验证期货资金密码和客户信息"""
	_fields_ = [
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#客户类型
		("CustType",c_char),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#币种代码
		("CurrencyID",c_char*4),
		]

	def getCustomerName(self):
		return self.CustomerName.decode('ascii')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return self.IdentifiedCardNo.decode('ascii')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getPassword(self):
		return self.Password.decode('ascii')
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')

class CThostFtdcDepositResultInformField(Structure):
	"""验证期货资金密码和客户信息"""
	_fields_ = [
		#出入金流水号，该流水号为银期报盘返回的流水号
		("DepositSeqNo",c_char*15),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#入金金额
		("Deposit",c_double),
		#请求编号
		("RequestID",c_int32),
		#返回代码
		("ReturnCode",c_char*7),
		#返回码描述
		("DescrInfoForReturnCode",c_char*129),
		]

	def getDepositSeqNo(self):
		return self.DepositSeqNo.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getDeposit(self):
		return self.Deposit
	def getRequestID(self):
		return self.RequestID
	def getReturnCode(self):
		return self.ReturnCode.decode('ascii')
	def getDescrInfoForReturnCode(self):
		return self.DescrInfoForReturnCode.decode('ascii')

class CThostFtdcReqSyncKeyField(Structure):
	"""交易核心向银期报盘发出密钥同步请求"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#安装编号
		("InstallID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#交易核心给银期报盘的消息
		("Message",c_char*129),
		#渠道标志
		("DeviceID",c_char*3),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		]

	def getTradeCode(self):
		return self.TradeCode.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBranchID(self):
		return self.BankBranchID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBrokerBranchID(self):
		return self.BrokerBranchID.decode('ascii')
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getBankSerial(self):
		return self.BankSerial.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getInstallID(self):
		return self.InstallID
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getMessage(self):
		return self.Message.decode('ascii')
	def getDeviceID(self):
		return self.DeviceID.decode('ascii')
	def getBrokerIDByBank(self):
		return self.BrokerIDByBank.decode('ascii')
	def getOperNo(self):
		return self.OperNo.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID

class CThostFtdcRspSyncKeyField(Structure):
	"""交易核心向银期报盘发出密钥同步响应"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#安装编号
		("InstallID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#交易核心给银期报盘的消息
		("Message",c_char*129),
		#渠道标志
		("DeviceID",c_char*3),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getTradeCode(self):
		return self.TradeCode.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBranchID(self):
		return self.BankBranchID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBrokerBranchID(self):
		return self.BrokerBranchID.decode('ascii')
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getBankSerial(self):
		return self.BankSerial.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getInstallID(self):
		return self.InstallID
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getMessage(self):
		return self.Message.decode('ascii')
	def getDeviceID(self):
		return self.DeviceID.decode('ascii')
	def getBrokerIDByBank(self):
		return self.BrokerIDByBank.decode('ascii')
	def getOperNo(self):
		return self.OperNo.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return self.ErrorMsg.decode('GB2312')

class CThostFtdcNotifyQueryAccountField(Structure):
	"""查询账户信息通知"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#客户类型
		("CustType",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#期货公司流水号
		("FutureSerial",c_int32),
		#安装编号
		("InstallID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#验证客户证件号码标志
		("VerifyCertNoFlag",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#摘要
		("Digest",c_char*36),
		#银行帐号类型
		("BankAccType",c_char),
		#渠道标志
		("DeviceID",c_char*3),
		#期货单位帐号类型
		("BankSecuAccType",c_char),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#期货单位帐号
		("BankSecuAcc",c_char*41),
		#银行密码标志
		("BankPwdFlag",c_char),
		#期货资金密码核对标志
		("SecuPwdFlag",c_char),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		#银行可用金额
		("BankUseAmount",c_double),
		#银行可取金额
		("BankFetchAmount",c_double),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getTradeCode(self):
		return self.TradeCode.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBranchID(self):
		return self.BankBranchID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBrokerBranchID(self):
		return self.BrokerBranchID.decode('ascii')
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getBankSerial(self):
		return self.BankSerial.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getCustomerName(self):
		return self.CustomerName.decode('ascii')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return self.IdentifiedCardNo.decode('ascii')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getBankAccount(self):
		return self.BankAccount.decode('ascii')
	def getBankPassWord(self):
		return self.BankPassWord.decode('ascii')
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getPassword(self):
		return self.Password.decode('ascii')
	def getFutureSerial(self):
		return self.FutureSerial
	def getInstallID(self):
		return self.InstallID
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getVerifyCertNoFlag(self):
		return YesNoIndicatorType(ord(self.VerifyCertNoFlag))
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')
	def getDigest(self):
		return self.Digest.decode('ascii')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getDeviceID(self):
		return self.DeviceID.decode('ascii')
	def getBankSecuAccType(self):
		return BankAccTypeType(ord(self.BankSecuAccType))
	def getBrokerIDByBank(self):
		return self.BrokerIDByBank.decode('ascii')
	def getBankSecuAcc(self):
		return self.BankSecuAcc.decode('ascii')
	def getBankPwdFlag(self):
		return PwdFlagType(ord(self.BankPwdFlag))
	def getSecuPwdFlag(self):
		return PwdFlagType(ord(self.SecuPwdFlag))
	def getOperNo(self):
		return self.OperNo.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID
	def getBankUseAmount(self):
		return self.BankUseAmount
	def getBankFetchAmount(self):
		return self.BankFetchAmount
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return self.ErrorMsg.decode('GB2312')

class CThostFtdcTransferSerialField(Structure):
	"""银期转账交易流水表"""
	_fields_ = [
		#平台流水号
		("PlateSerial",c_int32),
		#交易发起方日期
		("TradeDate",c_char*9),
		#交易日期
		("TradingDay",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#交易代码
		("TradeCode",c_char*7),
		#会话编号
		("SessionID",c_int32),
		#银行编码
		("BankID",c_char*4),
		#银行分支机构编码
		("BankBranchID",c_char*5),
		#银行帐号类型
		("BankAccType",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行流水号
		("BankSerial",c_char*13),
		#期货公司编码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#期货公司帐号类型
		("FutureAccType",c_char),
		#投资者帐号
		("AccountID",c_char*13),
		#投资者代码
		("InvestorID",c_char*13),
		#期货公司流水号
		("FutureSerial",c_int32),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#币种代码
		("CurrencyID",c_char*4),
		#交易金额
		("TradeAmount",c_double),
		#应收客户费用
		("CustFee",c_double),
		#应收期货公司费用
		("BrokerFee",c_double),
		#有效标志
		("AvailabilityFlag",c_char),
		#操作员
		("OperatorCode",c_char*17),
		#新银行帐号
		("BankNewAccount",c_char*41),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getPlateSerial(self):
		return self.PlateSerial
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getTradeCode(self):
		return self.TradeCode.decode('ascii')
	def getSessionID(self):
		return self.SessionID
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBranchID(self):
		return self.BankBranchID.decode('ascii')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getBankAccount(self):
		return self.BankAccount.decode('ascii')
	def getBankSerial(self):
		return self.BankSerial.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBrokerBranchID(self):
		return self.BrokerBranchID.decode('ascii')
	def getFutureAccType(self):
		return FutureAccTypeType(ord(self.FutureAccType))
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getInvestorID(self):
		return self.InvestorID.decode('ascii')
	def getFutureSerial(self):
		return self.FutureSerial
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return self.IdentifiedCardNo.decode('ascii')
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')
	def getTradeAmount(self):
		return self.TradeAmount
	def getCustFee(self):
		return self.CustFee
	def getBrokerFee(self):
		return self.BrokerFee
	def getAvailabilityFlag(self):
		return AvailabilityFlagType(ord(self.AvailabilityFlag))
	def getOperatorCode(self):
		return self.OperatorCode.decode('ascii')
	def getBankNewAccount(self):
		return self.BankNewAccount.decode('ascii')
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return self.ErrorMsg.decode('GB2312')

class CThostFtdcQryTransferSerialField(Structure):
	"""请求查询转帐流水"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者帐号
		("AccountID",c_char*13),
		#银行编码
		("BankID",c_char*4),
		#币种代码
		("CurrencyID",c_char*4),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')

class CThostFtdcNotifyFutureSignInField(Structure):
	"""期商签到通知"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#安装编号
		("InstallID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#摘要
		("Digest",c_char*36),
		#币种代码
		("CurrencyID",c_char*4),
		#渠道标志
		("DeviceID",c_char*3),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		#PIN密钥
		("PinKey",c_char*129),
		#MAC密钥
		("MacKey",c_char*129),
		]

	def getTradeCode(self):
		return self.TradeCode.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBranchID(self):
		return self.BankBranchID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBrokerBranchID(self):
		return self.BrokerBranchID.decode('ascii')
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getBankSerial(self):
		return self.BankSerial.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getInstallID(self):
		return self.InstallID
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getDigest(self):
		return self.Digest.decode('ascii')
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')
	def getDeviceID(self):
		return self.DeviceID.decode('ascii')
	def getBrokerIDByBank(self):
		return self.BrokerIDByBank.decode('ascii')
	def getOperNo(self):
		return self.OperNo.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return self.ErrorMsg.decode('GB2312')
	def getPinKey(self):
		return self.PinKey.decode('ascii')
	def getMacKey(self):
		return self.MacKey.decode('ascii')

class CThostFtdcNotifyFutureSignOutField(Structure):
	"""期商签退通知"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#安装编号
		("InstallID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#摘要
		("Digest",c_char*36),
		#币种代码
		("CurrencyID",c_char*4),
		#渠道标志
		("DeviceID",c_char*3),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getTradeCode(self):
		return self.TradeCode.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBranchID(self):
		return self.BankBranchID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBrokerBranchID(self):
		return self.BrokerBranchID.decode('ascii')
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getBankSerial(self):
		return self.BankSerial.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getInstallID(self):
		return self.InstallID
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getDigest(self):
		return self.Digest.decode('ascii')
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')
	def getDeviceID(self):
		return self.DeviceID.decode('ascii')
	def getBrokerIDByBank(self):
		return self.BrokerIDByBank.decode('ascii')
	def getOperNo(self):
		return self.OperNo.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return self.ErrorMsg.decode('GB2312')

class CThostFtdcNotifySyncKeyField(Structure):
	"""交易核心向银期报盘发出密钥同步处理结果的通知"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#安装编号
		("InstallID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#交易核心给银期报盘的消息
		("Message",c_char*129),
		#渠道标志
		("DeviceID",c_char*3),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getTradeCode(self):
		return self.TradeCode.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBranchID(self):
		return self.BankBranchID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBrokerBranchID(self):
		return self.BrokerBranchID.decode('ascii')
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getBankSerial(self):
		return self.BankSerial.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getInstallID(self):
		return self.InstallID
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getMessage(self):
		return self.Message.decode('ascii')
	def getDeviceID(self):
		return self.DeviceID.decode('ascii')
	def getBrokerIDByBank(self):
		return self.BrokerIDByBank.decode('ascii')
	def getOperNo(self):
		return self.OperNo.decode('ascii')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return self.ErrorMsg.decode('GB2312')

class CThostFtdcQryAccountregisterField(Structure):
	"""请求查询银期签约关系"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者帐号
		("AccountID",c_char*13),
		#银行编码
		("BankID",c_char*4),
		#银行分支机构编码
		("BankBranchID",c_char*5),
		#币种代码
		("CurrencyID",c_char*4),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBranchID(self):
		return self.BankBranchID.decode('ascii')
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')

class CThostFtdcAccountregisterField(Structure):
	"""客户开销户信息表"""
	_fields_ = [
		#交易日期
		("TradeDay",c_char*9),
		#银行编码
		("BankID",c_char*4),
		#银行分支机构编码
		("BankBranchID",c_char*5),
		#银行帐号
		("BankAccount",c_char*41),
		#期货公司编码
		("BrokerID",c_char*11),
		#期货公司分支机构编码
		("BrokerBranchID",c_char*31),
		#投资者帐号
		("AccountID",c_char*13),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#客户姓名
		("CustomerName",c_char*51),
		#币种代码
		("CurrencyID",c_char*4),
		#开销户类别
		("OpenOrDestroy",c_char),
		#签约日期
		("RegDate",c_char*9),
		#解约日期
		("OutDate",c_char*9),
		#交易ID
		("TID",c_int32),
		#客户类型
		("CustType",c_char),
		#银行帐号类型
		("BankAccType",c_char),
		]

	def getTradeDay(self):
		return self.TradeDay.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBranchID(self):
		return self.BankBranchID.decode('ascii')
	def getBankAccount(self):
		return self.BankAccount.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBrokerBranchID(self):
		return self.BrokerBranchID.decode('ascii')
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return self.IdentifiedCardNo.decode('ascii')
	def getCustomerName(self):
		return self.CustomerName.decode('ascii')
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')
	def getOpenOrDestroy(self):
		return OpenOrDestroyType(ord(self.OpenOrDestroy))
	def getRegDate(self):
		return self.RegDate.decode('ascii')
	def getOutDate(self):
		return self.OutDate.decode('ascii')
	def getTID(self):
		return self.TID
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))

class CThostFtdcOpenAccountField(Structure):
	"""银期开户信息"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#性别
		("Gender",c_char),
		#国家代码
		("CountryCode",c_char*21),
		#客户类型
		("CustType",c_char),
		#地址
		("Address",c_char*101),
		#邮编
		("ZipCode",c_char*7),
		#电话号码
		("Telephone",c_char*41),
		#手机
		("MobilePhone",c_char*21),
		#传真
		("Fax",c_char*41),
		#电子邮件
		("EMail",c_char*41),
		#资金账户状态
		("MoneyAccountStatus",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#安装编号
		("InstallID",c_int32),
		#验证客户证件号码标志
		("VerifyCertNoFlag",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#汇钞标志
		("CashExchangeCode",c_char),
		#摘要
		("Digest",c_char*36),
		#银行帐号类型
		("BankAccType",c_char),
		#渠道标志
		("DeviceID",c_char*3),
		#期货单位帐号类型
		("BankSecuAccType",c_char),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#期货单位帐号
		("BankSecuAcc",c_char*41),
		#银行密码标志
		("BankPwdFlag",c_char),
		#期货资金密码核对标志
		("SecuPwdFlag",c_char),
		#交易柜员
		("OperNo",c_char*17),
		#交易ID
		("TID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getTradeCode(self):
		return self.TradeCode.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBranchID(self):
		return self.BankBranchID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBrokerBranchID(self):
		return self.BrokerBranchID.decode('ascii')
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getBankSerial(self):
		return self.BankSerial.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getCustomerName(self):
		return self.CustomerName.decode('ascii')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return self.IdentifiedCardNo.decode('ascii')
	def getGender(self):
		return GenderType(ord(self.Gender))
	def getCountryCode(self):
		return self.CountryCode.decode('ascii')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getAddress(self):
		return self.Address.decode('ascii')
	def getZipCode(self):
		return self.ZipCode.decode('ascii')
	def getTelephone(self):
		return self.Telephone.decode('ascii')
	def getMobilePhone(self):
		return self.MobilePhone.decode('ascii')
	def getFax(self):
		return self.Fax.decode('ascii')
	def getEMail(self):
		return self.EMail.decode('ascii')
	def getMoneyAccountStatus(self):
		return MoneyAccountStatusType(ord(self.MoneyAccountStatus))
	def getBankAccount(self):
		return self.BankAccount.decode('ascii')
	def getBankPassWord(self):
		return self.BankPassWord.decode('ascii')
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getPassword(self):
		return self.Password.decode('ascii')
	def getInstallID(self):
		return self.InstallID
	def getVerifyCertNoFlag(self):
		return YesNoIndicatorType(ord(self.VerifyCertNoFlag))
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')
	def getCashExchangeCode(self):
		return CashExchangeCodeType(ord(self.CashExchangeCode))
	def getDigest(self):
		return self.Digest.decode('ascii')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getDeviceID(self):
		return self.DeviceID.decode('ascii')
	def getBankSecuAccType(self):
		return BankAccTypeType(ord(self.BankSecuAccType))
	def getBrokerIDByBank(self):
		return self.BrokerIDByBank.decode('ascii')
	def getBankSecuAcc(self):
		return self.BankSecuAcc.decode('ascii')
	def getBankPwdFlag(self):
		return PwdFlagType(ord(self.BankPwdFlag))
	def getSecuPwdFlag(self):
		return PwdFlagType(ord(self.SecuPwdFlag))
	def getOperNo(self):
		return self.OperNo.decode('ascii')
	def getTID(self):
		return self.TID
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return self.ErrorMsg.decode('GB2312')

class CThostFtdcCancelAccountField(Structure):
	"""银期销户信息"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#性别
		("Gender",c_char),
		#国家代码
		("CountryCode",c_char*21),
		#客户类型
		("CustType",c_char),
		#地址
		("Address",c_char*101),
		#邮编
		("ZipCode",c_char*7),
		#电话号码
		("Telephone",c_char*41),
		#手机
		("MobilePhone",c_char*21),
		#传真
		("Fax",c_char*41),
		#电子邮件
		("EMail",c_char*41),
		#资金账户状态
		("MoneyAccountStatus",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#安装编号
		("InstallID",c_int32),
		#验证客户证件号码标志
		("VerifyCertNoFlag",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#汇钞标志
		("CashExchangeCode",c_char),
		#摘要
		("Digest",c_char*36),
		#银行帐号类型
		("BankAccType",c_char),
		#渠道标志
		("DeviceID",c_char*3),
		#期货单位帐号类型
		("BankSecuAccType",c_char),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#期货单位帐号
		("BankSecuAcc",c_char*41),
		#银行密码标志
		("BankPwdFlag",c_char),
		#期货资金密码核对标志
		("SecuPwdFlag",c_char),
		#交易柜员
		("OperNo",c_char*17),
		#交易ID
		("TID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getTradeCode(self):
		return self.TradeCode.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBranchID(self):
		return self.BankBranchID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBrokerBranchID(self):
		return self.BrokerBranchID.decode('ascii')
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getBankSerial(self):
		return self.BankSerial.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getCustomerName(self):
		return self.CustomerName.decode('ascii')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return self.IdentifiedCardNo.decode('ascii')
	def getGender(self):
		return GenderType(ord(self.Gender))
	def getCountryCode(self):
		return self.CountryCode.decode('ascii')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getAddress(self):
		return self.Address.decode('ascii')
	def getZipCode(self):
		return self.ZipCode.decode('ascii')
	def getTelephone(self):
		return self.Telephone.decode('ascii')
	def getMobilePhone(self):
		return self.MobilePhone.decode('ascii')
	def getFax(self):
		return self.Fax.decode('ascii')
	def getEMail(self):
		return self.EMail.decode('ascii')
	def getMoneyAccountStatus(self):
		return MoneyAccountStatusType(ord(self.MoneyAccountStatus))
	def getBankAccount(self):
		return self.BankAccount.decode('ascii')
	def getBankPassWord(self):
		return self.BankPassWord.decode('ascii')
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getPassword(self):
		return self.Password.decode('ascii')
	def getInstallID(self):
		return self.InstallID
	def getVerifyCertNoFlag(self):
		return YesNoIndicatorType(ord(self.VerifyCertNoFlag))
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')
	def getCashExchangeCode(self):
		return CashExchangeCodeType(ord(self.CashExchangeCode))
	def getDigest(self):
		return self.Digest.decode('ascii')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getDeviceID(self):
		return self.DeviceID.decode('ascii')
	def getBankSecuAccType(self):
		return BankAccTypeType(ord(self.BankSecuAccType))
	def getBrokerIDByBank(self):
		return self.BrokerIDByBank.decode('ascii')
	def getBankSecuAcc(self):
		return self.BankSecuAcc.decode('ascii')
	def getBankPwdFlag(self):
		return PwdFlagType(ord(self.BankPwdFlag))
	def getSecuPwdFlag(self):
		return PwdFlagType(ord(self.SecuPwdFlag))
	def getOperNo(self):
		return self.OperNo.decode('ascii')
	def getTID(self):
		return self.TID
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return self.ErrorMsg.decode('GB2312')

class CThostFtdcChangeAccountField(Structure):
	"""银期变更银行账号信息"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#性别
		("Gender",c_char),
		#国家代码
		("CountryCode",c_char*21),
		#客户类型
		("CustType",c_char),
		#地址
		("Address",c_char*101),
		#邮编
		("ZipCode",c_char*7),
		#电话号码
		("Telephone",c_char*41),
		#手机
		("MobilePhone",c_char*21),
		#传真
		("Fax",c_char*41),
		#电子邮件
		("EMail",c_char*41),
		#资金账户状态
		("MoneyAccountStatus",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#新银行帐号
		("NewBankAccount",c_char*41),
		#新银行密码
		("NewBankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#银行帐号类型
		("BankAccType",c_char),
		#安装编号
		("InstallID",c_int32),
		#验证客户证件号码标志
		("VerifyCertNoFlag",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#银行密码标志
		("BankPwdFlag",c_char),
		#期货资金密码核对标志
		("SecuPwdFlag",c_char),
		#交易ID
		("TID",c_int32),
		#摘要
		("Digest",c_char*36),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getTradeCode(self):
		return self.TradeCode.decode('ascii')
	def getBankID(self):
		return self.BankID.decode('ascii')
	def getBankBranchID(self):
		return self.BankBranchID.decode('ascii')
	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getBrokerBranchID(self):
		return self.BrokerBranchID.decode('ascii')
	def getTradeDate(self):
		return self.TradeDate.decode('ascii')
	def getTradeTime(self):
		return self.TradeTime.decode('ascii')
	def getBankSerial(self):
		return self.BankSerial.decode('ascii')
	def getTradingDay(self):
		return self.TradingDay.decode('ascii')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getCustomerName(self):
		return self.CustomerName.decode('ascii')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return self.IdentifiedCardNo.decode('ascii')
	def getGender(self):
		return GenderType(ord(self.Gender))
	def getCountryCode(self):
		return self.CountryCode.decode('ascii')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getAddress(self):
		return self.Address.decode('ascii')
	def getZipCode(self):
		return self.ZipCode.decode('ascii')
	def getTelephone(self):
		return self.Telephone.decode('ascii')
	def getMobilePhone(self):
		return self.MobilePhone.decode('ascii')
	def getFax(self):
		return self.Fax.decode('ascii')
	def getEMail(self):
		return self.EMail.decode('ascii')
	def getMoneyAccountStatus(self):
		return MoneyAccountStatusType(ord(self.MoneyAccountStatus))
	def getBankAccount(self):
		return self.BankAccount.decode('ascii')
	def getBankPassWord(self):
		return self.BankPassWord.decode('ascii')
	def getNewBankAccount(self):
		return self.NewBankAccount.decode('ascii')
	def getNewBankPassWord(self):
		return self.NewBankPassWord.decode('ascii')
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getPassword(self):
		return self.Password.decode('ascii')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getInstallID(self):
		return self.InstallID
	def getVerifyCertNoFlag(self):
		return YesNoIndicatorType(ord(self.VerifyCertNoFlag))
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')
	def getBrokerIDByBank(self):
		return self.BrokerIDByBank.decode('ascii')
	def getBankPwdFlag(self):
		return PwdFlagType(ord(self.BankPwdFlag))
	def getSecuPwdFlag(self):
		return PwdFlagType(ord(self.SecuPwdFlag))
	def getTID(self):
		return self.TID
	def getDigest(self):
		return self.Digest.decode('ascii')
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return self.ErrorMsg.decode('GB2312')

class CThostFtdcSecAgentACIDMapField(Structure):
	"""二级代理操作员银期权限"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#资金账户
		("AccountID",c_char*13),
		#币种
		("CurrencyID",c_char*4),
		#境外中介机构资金帐号
		("BrokerSecAgentID",c_char*13),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')
	def getBrokerSecAgentID(self):
		return self.BrokerSecAgentID.decode('ascii')

class CThostFtdcQrySecAgentACIDMapField(Structure):
	"""二级代理操作员银期权限查询"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#资金账户
		("AccountID",c_char*13),
		#币种
		("CurrencyID",c_char*4),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')

class CThostFtdcUserRightsAssignField(Structure):
	"""灾备中心交易权限"""
	_fields_ = [
		#应用单元代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#交易中心代码
		("DRIdentityID",c_int32),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getDRIdentityID(self):
		return self.DRIdentityID

class CThostFtdcBrokerUserRightAssignField(Structure):
	"""经济公司是否有在本标示的交易权限"""
	_fields_ = [
		#应用单元代码
		("BrokerID",c_char*11),
		#交易中心代码
		("DRIdentityID",c_int32),
		#能否交易
		("Tradeable",c_int32),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getDRIdentityID(self):
		return self.DRIdentityID
	def getTradeable(self):
		return self.Tradeable

class CThostFtdcDRTransferField(Structure):
	"""灾备交易转换报文"""
	_fields_ = [
		#原交易中心代码
		("OrigDRIdentityID",c_int32),
		#目标交易中心代码
		("DestDRIdentityID",c_int32),
		#原应用单元代码
		("OrigBrokerID",c_char*11),
		#目标易用单元代码
		("DestBrokerID",c_char*11),
		]

	def getOrigDRIdentityID(self):
		return self.OrigDRIdentityID
	def getDestDRIdentityID(self):
		return self.DestDRIdentityID
	def getOrigBrokerID(self):
		return self.OrigBrokerID.decode('ascii')
	def getDestBrokerID(self):
		return self.DestBrokerID.decode('ascii')

class CThostFtdcFensUserInfoField(Structure):
	"""Fens用户信息"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#登录模式
		("LoginMode",c_char),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')
	def getLoginMode(self):
		return LoginModeType(ord(self.LoginMode))

class CThostFtdcCurrTransferIdentityField(Structure):
	"""当前银期所属交易中心"""
	_fields_ = [
		#交易中心代码
		("IdentityID",c_int32),
		]

	def getIdentityID(self):
		return self.IdentityID

class CThostFtdcLoginForbiddenUserField(Structure):
	"""禁止登录用户"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')

class CThostFtdcQryLoginForbiddenUserField(Structure):
	"""查询禁止登录用户"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getUserID(self):
		return self.UserID.decode('ascii')

class CThostFtdcMulticastGroupInfoField(Structure):
	"""UDP组播组信息"""
	_fields_ = [
		#组播组IP地址
		("GroupIP",c_char*16),
		#组播组IP端口
		("GroupPort",c_int32),
		#源地址
		("SourceIP",c_char*16),
		]

	def getGroupIP(self):
		return self.GroupIP.decode('ascii')
	def getGroupPort(self):
		return self.GroupPort
	def getSourceIP(self):
		return self.SourceIP.decode('ascii')

class CThostFtdcTradingAccountReserveField(Structure):
	"""资金账户基本准备金"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者帐号
		("AccountID",c_char*13),
		#基本准备金
		("Reserve",c_double),
		#币种代码
		("CurrencyID",c_char*4),
		]

	def getBrokerID(self):
		return self.BrokerID.decode('ascii')
	def getAccountID(self):
		return self.AccountID.decode('ascii')
	def getReserve(self):
		return self.Reserve
	def getCurrencyID(self):
		return self.CurrencyID.decode('ascii')

