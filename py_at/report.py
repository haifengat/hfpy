#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/11/2'
"""

import webbrowser


def show(data, bars_json):
    '''生成网页版报告'''
    tmp = open('report.html', 'w', encoding='utf-8')
    tmp.write('''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>交易策略绩效报告</title>
            <!-- 引入 echarts.js -->

            <script src="https://cdn.bootcss.com/echarts/4.0.2/echarts.js"></script>
        </head>
        <body>
    <h3>策略详情</h3>
    <div id="title">

    <table style="width:100%;height:50px;" border="1", align="center">
  <tr>
    <td width="20%" height="24"><div align="center">策略名</div></td>
    <td width="25%"><div align="center" id="ID"></div></td>
    <td width="24%"><div align="center">交易合约</div></td>
    <td width="31%"><div align="center" id="Ins"></div></td>
  </tr>
  <tr>
    <td height="28"><div align="center">开始时间</div></td>
    <td><div align="center" id="BeginTime"></div></td>
    <td><div align="center">最小时间周期</div></td>
    <td><div align="center" id="Internal"></div></td>
  </tr>
  <tr>
    <td height="32"><div align="center">周期类型</div></td>
    <td> <div align="center" id="InternalType"> </div></td>
    <td><div align="center">参数</div></td>
    <td><div align="center" id="Params"></div></td>
  </tr>
   </table>
  </div>
	<br/>
    <!-- 为ECharts准备一个具备大小（宽高）的Dom -->
    <div id="main" align="center" style="width:100%;height:600px;"></div><br/>
	<h3>收益曲线</h3>
	<div id="sub" style="width:100%;height:600px;"></div><br/>
	<div id="table" style="width:100%;height:400px;"><br/>
	<h3>绩效报告</h3>
    <table style="width:100%;height:400px;" border="1", align="center">
      <tr>
        <td height="37" colspan="6"><div align="center">一、按1分钟Bar计算</div></td>
      </tr>
      <tr>
	    <td width="172"><div align="center">初始资金</div></td>
	    <td width="230"><div align="center" id="bInitFund"></div></td>
		<td width="154" height="26"><div align="center">最大回撤比率</div></td>
			<td width="212"><div align="center" id="bMddRate"></div></td>
      
		   <td width="221"><div align="center">
        <div align="center">最大回撤区间</div></td>
           <td colspan="3"><div align="center" id="dDropDownPeriod"></div></td>
      </tr>
	 
      <tr>
        <td height="35" colspan="6"><div align="center">二、按成交记录计算</div></td>
      </tr>
      <tr>
        <td><div align="center">净利润</div></td>
        <td><div align="center" id="tTotalNetProfit"></div></td>
        <td><div align="center">总盈利</div></td>
        <td width="212"><div align="center" id="tGainAmount"></div></td>
        <td width="221"><div align="center">最大盈利占比</div></td>
        <td width="255"><div align="center" id="tMaxGainRatio"></div></td>
      </tr>
      <tr>
        <td><div align="center">交易次数</div></td>
        <td><div align="center" id="tTotalCount"></div></td>
        <td><div align="center">总亏损</div></td>
        <td><div align="center" id="tLossAmount"></div></td>
        <td><div align="center">最大亏损占比</div></td>
        <td><div align="center" id="tMaxLossRatio"></div></td>
      </tr>
      <tr>
        <td><div align="center">盈利次数</div></td>
        <td><div align="center" id="tGainCount"></div></td>
        <td><div align="center">盈利因子</div></td>
        <td><div align="center" id="tProfitFactor"></div></td>
        <td><div align="center">最大连续盈利次数</div></td>
        <td><div align="center" id="tMaxContGainCount"></div></td>
      </tr>
      <tr>
        <td><div align="center">亏损次数</div></td>
        <td><div align="center" id="tLossCount"></div></td>
        <td><div align="center">胜率</div></td>
        <td><div align="center" id="tWinRate"></div></td>
        <td><div align="center">最大连续亏损次数</div></td>
        <td><div align="center" id="tMaxContLossCount"></div></td>
      </tr>
      <tr>
        <td><div align="center">持平次数</div></td>
        <td><div align="center" id="tHoldCount"></div></td>
        <td><div align="center">平均盈亏比</div></td>
        <td><div align="center" id="tAvgGLRate"></div></td>
        <td><div align="center">最大连续盈利金额</div></td>
        <td><div align="center" id="tMaxContGainAmount"></div></td>
      </tr>
      <tr>
        <td><div align="center">平均盈利</div></td>
        <td><div align="center" id="tAvgGain"></div></td>
        <td><div align="center">最大盈利</div></td>
        <td><div align="center" id="tMaxGain"></div></td>
        <td><div align="center">最大连续亏损金额</div></td>
        <td><div align="center" id="tMaxContLossAmount"></div></td>
      </tr>
      <tr>
        <td><div align="center">平均亏损</div></td>
        <td><div align="center" id="tAvgLoss"></div></td>
        <td><div align="center">最大亏损</div></td>
        <td><div align="center" id="tMaxLoss"></div></td>
        <td><div align="center"></div></td>
        <td><div align="center"></div></td>
      </tr>
      <tr>
        <td colspan="6"><div align="center">三、按日计算</div></td>
      </tr>
      <tr>
        <td><div align="center">总收益率</div></td>
        <td><div align="center" id="dTotalyield"></div></td>
        <td><div align="center">胜率</div></td>
        <td><div align="center" id="dWinRate"></div></td>
        <td><div align="center">持平天数</div></td>
        <td><div align="center" id="dHoldCount"></div></td>
      </tr>
      <tr>
        <td><div align="center">年化收益率</div></td>
        <td><div align="center" id="dYearYield"></div></td>
        <td><div align="center">平均日收益</div></td>
        <td><div align="center" id="dAvgYield"></div></td>
        <td><div align="center">日均盈亏比比率</div></td>
        <td><div align="center" id="dAvgGLRate"></div></td>
      </tr>
      <tr>
        <td><div align="center">波动率</div></td>
        <td><div align="center" id="dVolatility"></div></td>
        <td><div align="center">平均每天亏损</div></td>
        <td><div align="center" id="dAvgLoss"></div></td>
        <td><div align="center">最大连续盈利天数</div></td>
        <td><div align="center" id="dMaxContGainCount"></div></td>
      </tr>
      <tr>
        <td><div align="center">夏普比率</div></td>
        <td><div align="center" id="dSharpRitio"></div></td>
        <td><div align="center">平均每天盈利</div></td>
        <td><div align="center" id="dAvgGain"></div></td>
        <td><div align="center">最大连续亏损天数</div></td>
        <td><div align="center" id="dMaxContLossCount"></div></td>
      </tr>
      <tr>
        <td><div align="center">MAR比率</div></td>
        <td><div align="center" id="dMarRate"></div></td>
        <td><div align="center">盈利天数</div></td>
        <td><div align="center" id="dGainCount"></div></td>
        <td><div align="center">最大净值不创新高天数</div></td>
        <td><div align="center" id="dNoNewHighDays"></div></td>
      </tr>
      <tr>
        <td><div align="center">总交易天数</div></td>
        <td><div align="center" id="dTotalCount"></div></td>
        <td><div align="center">亏损天数</div></td>
        <td><div align="center" id="dLossCount"></div></td>
        <td><div align="center">最大净值不创新高区间</div></td>
        <td><div align="center" id="dNoNewHighPeriod"></div></td>
      </tr>
      <tr>
        <td colspan="6"><div align="center">四、按周计算</div></td>
      </tr>
      <tr>
        <td><div align="center">总交易周数</div></td>
        <td><div align="center" id="wTotalCount"></div></td>
        <td><div align="center">周胜率</div></td>
        <td><div align="center" id="wWinRate"></div></td>
        <td><div align="center">最大连续亏损周数</div></td>
        <td><div align="center" id="wMaxContLossCount"></div></td>
      </tr>
      <tr>
        <td><div align="center">盈利周数</div></td>
        <td><div align="center" id="wGainCount"></div></td>
        <td><div align="center">平均每周亏损</div></td>
        <td><div align="center" id="wAvgLoss"></div></td>
        <td><div align="center">最大连续盈利周数</div></td>
        <td><div align="center" id="wMaxContGainCount"></div></td>
      </tr>
      <tr>
        <td><div align="center">亏损周数</div></td>
        <td><div align="center" id="wLossCount"></div></td>
        <td><div align="center">平均每周盈利</div></td>
        <td><div align="center" id="wwvgGain"></div></td>
        <td><div align="center"></div></td>
        <td><div align="center"></div></td>
      </tr>
      <tr>
        <td><div align="center">持平周数</div></td>
        <td><div align="center" id="wHoldCount"></div></td>
        <td><div align="center"></div></td>
        <td><div align="center"></div></td>
        <td><div align="center"></div></td>
        <td><div align="center"></div></td>
      </tr>
      <tr>
        <td colspan="6"><div align="center">五、按月计算</div></td>
      </tr>
      <tr>
        <td><div align="center">总交易月数</div></td>
        <td><div align="center" id="mTotalCount"></div></td>
        <td><div align="center">最大连续盈利月数</div></td>
        <td><div align="center" id="mMaxContGainCount"></div></td>
        <td><div align="center">平均每月亏损</div></td>
        <td><div align="center" id="mAvgLoss"></div></td>
      </tr>
      <tr>
        <td><div align="center">盈利月数</div></td>
        <td><div align="center" id="mGainCount"></div></td>
        <td><div align="center">最大连续亏损月数</div></td>
        <td><div align="center" id="mMaxContLossCount"></div></td>
        <td><div align="center">平均每月盈利</div></td>
        <td><div align="center" id="mAvgGain"></div></td>
      </tr>
      <tr>
        <td><div align="center">亏损月数</div></td>
        <td><div align="center" id="mLossCount"></div></td>
        <td>&nbsp;</td>
        <td><div align="center"></div></td>
        <td><div align="center"></div></td>
        <td><div align="center"></div></td>
      </tr>
      <tr>
        <td><div align="center">持平月数</div></td>
        <td><div align="center" id="mHoldCount"></div></td>
        <td>&nbsp;</td>
        <td><div align="center"></div></td>
        <td><div align="center"></div></td>
        <td><div align="center"></div></td>
      </tr>
      <tr>
        <td colspan="5"><div align="center">&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;六、按年计算</div></td>
        <td><div align="center"></div></td>
      </tr>
      <tr>
        <td><div align="center">总交易年数</div></td>
        <td><div align="center" id="yTotalCount"></div></td>
        <td><div align="center">持平年数</div></td>
        <td><div align="center" id="yHoldCount"></div></td>
        <td><div align="center">
          <div align="center">平均每年盈利</div>
        </div></td>
        <td><div align="center" id="yAvgGain"></div></td>
      </tr>
      <tr>
        <td><div align="center">盈利年数</div></td>
        <td><div align="center" id="yGainCount"></div></td>
        <td><div align="center">最大连续盈利年数</div></td>
        <td><div align="center" id="yMAxContGainCount"></div></td>
        <td><div align="center">平均每年亏损</div></td>
        <td><div align="center" id="yAvgLoss"></div></td>
      </tr>
      <tr>
        <td><div align="center">亏损年数</div></td>
        <td><div align="center" id="yLossCount"></div></td>
        <td><div align="center">最大连续亏损年数</div></td>
        <td><div align="center" id="yMaxContLossCount"></div></td>
        <td><div align="center"></div></td>
        <td><div align="center"></div></td>
      </tr>
    </table>

	</div>
        
        <script type="text/javascript">
            // 基于准备好的dom，初始化echarts实例
            var myChart = echarts.init(document.getElementById('main'));

            // 指定图表的配置项和数据
            var upColor = '#ec0000';
            var upBorderColor = '#8A0000';
            var downColor = '#00da3c';
            var downBorderColor = '#008F28';


        // 数据意义：开盘(open)，收盘(close)，最低(lowest)，最高(highest)
        var data0=splitData({0})
        //数据意义：日期，方向（0为买，1为卖），开平（0为开，1为平）,价格,手数

        var data1={1}
        var data2={2}
        var data3={3}
        var data4={4}


        function splitData(rawData) {{
            var categoryData = [];
            var values = [];
            for (var i = 0; i < rawData.length; i++) {{
                categoryData.push(rawData[i].splice(0, 1)[0]);
                values.push(rawData[i]);
            }}
            return {{
                categoryData: categoryData,
                values: values
            }};
        }}
        function splitData2(rawData) {{
            var categoryData = [];
            var values = [];
            for (var i = 0; i < rawData.length; i++) {{
                categoryData.push(rawData[i].splice(0, 1)[0]);
                values.push(rawData[i][0]);
            }}
            return {{
                categoryData: categoryData,
                values: values
            }};
        }}



        var pointers=[]
        
        //构造点
        for(var i=0;i<data1.length;i++)
        {{
            if(data1[i][1]==0)
            {{
                pointers.push({{
                name: 'XX标点',
                direction:data1[i][1],
                offset:data1[i][2],
                price:data1[i][3],
                coord: [data1[i][0],data1[i][3]],
                value: data1[i][4],
                dtime:data1[i][0],
                itemStyle: {{
                    normal: {{color: 'red'}}
                }}
                }},)
            }}
            else
            {{
                pointers.push({{
                name: 'XX标点',
                direction:data1[i][1],
                offset:data1[i][2],
                price:data1[i][3],
                coord: [data1[i][0],data1[i][3]],
                value: data1[i][4],
                dtime:data1[i][0],
                itemStyle: {{
                    normal: {{color: 'rgb(41,150,85)'}}
                }}
                }},)
            }}
        }}
        


        //构造连线
        var marklines=[]
        var vol=0
        var position=[]
        var pos={{}}
        var closevolume=0
        for(var i=0;i<pointers.length;i++)
        {{
            if(pointers[i]['offset']==0)
            {{
                position.push({{'direction':pointers[i]['direction'],'dtime':pointers[i]['dtime'],'volume':pointers[i]['value'],'price':pointers[i]['price']}})
            }}
            else
            {{
                closevolume=pointers[i]['value']
            
                for(var pos of position)
                {{  
                    if(pos['direction']==0)
                    {{
                        if(pos['volume']==closevolume)
                        {{
                            marklines.push(
                            [
                                {{
                                    lineStyle: {{
                                    normal: {{
                                        color: pos['price'] < pointers[i]['Price']?'red':'green',
                                        width: 1,
                                        type: 'dashed'
                                    }}
                                    }},
                                    itemStyle: {{
                                        normal: {{
                                            borderWidth: 3,
                                            borderColor: 'yellow',
                                            color: 'red'
                                        }}
                                    }},
                                    symbol:'triangle',
                                    symbolSize:8,
                                    coord: [pos['dtime'], pos['price']],
                                }},
                                {{
                                    symbol:'triangle',
                                    symbolSize:8,
                                    coord: [pointers[i]['dtime'], pointers[i]['price']],
                                }}
                            ],
                            )
                            position.shift() 
                            break                   
                        }}
                        else if(pos['volume']>closevolume)
                        {{
                            pos['volume']-=closevolume
                            marklines.push(
                                [
                                    {{
                                        lineStyle: {{
                                        normal: {{
                                            color: pos['price'] > pointers[i]['Price']?'red':'green',
                                            width: 1,
                                            type: 'dashed'
                                        }}
                                        }},
                                        itemStyle: {{
                                            normal: {{
                                                borderWidth: 3,
                                                borderColor: 'yellow',
                                                color: 'blue'
                                            }}
                                        }},
                                        symbol:'triangle',
                                        symbolSize:8,
                                        coord: [pos['dtime'], pos['price']],
                                                                    
                                    }},
                                    {{
                                        symbol:'triangle',
                                        symbolSize:8,
                                        coord: [pointers[i]['dtime'], pointers[i]['price']],
                                    }}
                                ],
                            )
                            break
                        }}
                        else
                        {{
                            marklines.push(
                                [
                                    {{
                                        lineStyle: {{
                                        normal: {{
                                            color: pos['price'] > pointers[i]['Price']?'red':'green',
                                            width: 1,
                                            type: 'dashed'
                                        }}
                                        }},
                                        itemStyle: {{
                                            normal: {{
                                                borderWidth: 3,
                                                borderColor: 'yellow',
                                                color: 'blue'
                                            }}
                                        }},
                                        symbol:'triangle',
                                        symbolSize:8,
                                        coord: [pos['dtime'], pos['price']],
                                                                    
                                    }},
                                    {{
                                        symbol:'triangle',
                                        symbolSize:8,
                                        coord: [pointers[i]['dtime'], pointers[i]['price']],
                                    }}
                                ],
                            )
                            position.shift()
                        }}
                    }} 
                    else
                    {{
                        if(pos['volume']==closevolume)
                        {{
                            marklines.push(
                                [
                                    {{
                                        lineStyle: {{
                                        normal: {{
                                            color: pos['price'] > pointers[i]['Price']?'red':'green',
                                            width: 1,
                                            type: 'dashed'
                                        }}
                                        }},
                                        itemStyle: {{
                                            normal: {{
                                                borderWidth: 3,
                                                borderColor: 'yellow',
                                                color: 'blue'
                                            }}
                                        }},
                                        symbol:'triangle',
                                        symbolSize:8,
                                        coord: [pos['dtime'], pos['price']],
                                                                    
                                    }},
                                    {{
                                        symbol:'triangle',
                                        symbolSize:8,
                                        coord: [pointers[i]['dtime'], pointers[i]['price']],
                                    }}
                                ],
                            )
                            position.shift() 
                            break                   
                        }}
                        else if(pos['volume']>closevolume)
                        {{
                            pos['volume']-=closevolume
                            marklines.push(
                                [
                                    {{
                                        lineStyle: {{
                                        normal: {{
                                            color: pos['price'] > pointers[i]['Price']?'red':'green',
                                            width: 1,
                                            type: 'dashed'
                                        }}
                                        }},
                                        itemStyle: {{
                                            normal: {{
                                                borderWidth: 3,
                                                borderColor: 'yellow',
                                                color: 'blue'
                                            }}
                                        }},
                                        symbol:'triangle',
                                        symbolSize:8,
                                        coord: [pos['dtime'], pos['price']],
                                                                    
                                    }},
                                    {{
                                        symbol:'triangle',
                                        symbolSize:8,
                                        coord: [pointers[i]['dtime'], pointers[i]['price']],
                                    }}
                                ],
                            )
                            break
                        }}
                        else
                        {{
                            marklines.push(
                                [
                                    {{
                                        lineStyle: {{
                                        normal: {{
                                            color: pos['price'] > pointers[i]['Price']?'red':'green',
                                            width: 1,
                                            type: 'dashed'
                                        }}
                                        }},
                                        itemStyle: {{
                                            normal: {{
                                                borderWidth: 3,
                                                borderColor: 'yellow',
                                                color: 'blue'
                                            }}
                                        }},
                                        symbol:'triangle',
                                        symbolSize:8,
                                        coord: [pos['dtime'], pos['price']],
                                                                    
                                    }},
                                    {{
                                        symbol:'triangle',
                                        symbolSize:8,
                                        coord: [pointers[i]['dtime'], pointers[i]['price']],
                                        
                                    
                                    }}
                                ],
                            )
                            position.shift()
                        }}
                    }}
                }}
            }}
        }}
        //构造指标
        //var indexs=[]
        //for(var ind in data2)
        //{{
        //    indexs.push(ind['up'])
        //}}

        option = 
        {{
            title: {{
                text: '信号图',
                left: 0
            }},
            tooltip: {{
                trigger: 'axis',
                axisPointer: {{
                    type: 'cross'
                }}
            }},
            //legend: {{
            //    data: ['日K']
            //}},
            grid: {{
                left: '10%',
                right: '10%',
                bottom: '15%'
            }},
            xAxis: {{
                type: 'category',
                data: data0.categoryData,
                scale: true,
                boundaryGap : false,
                axisLine: {{onZero: false}},
                splitLine: {{show: false}},
                splitNumber: 20,
                min: 'dataMin',
                max: 'dataMax'
            }},
            yAxis: {{
                scale: true,
                splitArea: {{
                    show: true
                }}
            }},
            dataZoom: [
                {{
                    type: 'inside',
                    start: 50,
                    end: 100
                }},
                {{
                    show: true,
                    type: 'slider',
                    y: '90%',
                    start: 50,
                    end: 100
                }}
            ],
            series: 
            [
                {{
                    name: '日K',
                    type: 'candlestick',
                    data: data0.values,
                    itemStyle: {{
                        normal: {{
                            color: upColor,
                            color0: downColor,
                            borderColor: upBorderColor,
                            borderColor0: downBorderColor
                        }}
                    }},
                    markPoint: {{
                        label: {{
                            normal: {{
                                formatter: function (param) {{
                                    return param != null ? Math.round(param.value) : '';
                                }}
                            }}
                        }},
                        data: pointers,
                        tooltip: {{
                            formatter: function (param) {{
                                return param.name + '<br>' + (param.data.coord || '');
                            }}
                        }}
                    }},
                    markLine:{{
                        symbol: ['circle', 'circle'],
                        
                        symbolSize:10,
                        data: marklines,
                    }}
                }},
                /*
                {{
                    {{
                        name: 'MA5',
                        type: 'line',
                        data: indexs,
                        smooth: true,
                        lineStyle: {{
                        normal: {{opacity: 0.5}}
                        }}
                    }}
                }}*/
            ]
        }};

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);

        var dayEquity=splitData2(data3['dayEquity'])
        var myChart2 = echarts.init(document.getElementById('sub'));
	
        option2 = {{
            xAxis: {{
                type: 'category',
                data: dayEquity.categoryData
            }},
            yAxis: {{
                type: 'value',
                max: function(value) {{
                    return value.max + 20
                }},
                min: function(value) {{
                return value.min - 20
                }}
            }},
            series: [{{
                data: dayEquity.values,
                type: 'line',
                smooth: true
            }}]
	    }};
                    
        myChart2.setOption(option2);
        
        document.getElementById("bInitFund").innerHTML=data3["bInitFund"]
        document.getElementById("bMddRate").innerHTML=data3["bMddRate"]
        document.getElementById("dNoNewHighPeriod").innerHTML=data3["dNoNewHighPeriod"] 
        document.getElementById("dDropDownPeriod").innerHTML=data3["dDropDownPeriod"] 
        document.getElementById("tTotalNetProfit").innerHTML=data3["tTotalNetProfit"]
        document.getElementById("tTotalCount").innerHTML=data3["tTotalCount"] 
        document.getElementById("tGainCount").innerHTML=data3["tGainCount"] 
        document.getElementById("tLossCount").innerHTML=data3["tLossCount"]  
        document.getElementById("tHoldCount").innerHTML=data3["tHoldCount"] 
        document.getElementById("tGainAmount").innerHTML=data3["tGainAmount"] 
        document.getElementById("tLossAmount").innerHTML=data3["tLossAmount"]
        document.getElementById("tProfitFactor").innerHTML=data3["tProfitFactor"] 
        document.getElementById("tWinRate").innerHTML=data3["tWinRate"] 
        document.getElementById("tAvgGain").innerHTML=data3["tAvgGain"]
        document.getElementById("tAvgLoss").innerHTML=data3["tAvgLoss"] 
        document.getElementById("tAvgGLRate").innerHTML=data3["tAvgGLRate"] 
        document.getElementById("tMaxGain").innerHTML=data3["tMaxGain"]
        document.getElementById("tMaxLoss").innerHTML=data3["tMaxLoss"] 
        document.getElementById("tMaxGainRatio").innerHTML=data3["tMaxGainRatio"] 
        document.getElementById("tMaxLossRatio").innerHTML=data3["tMaxLossRatio"]
        document.getElementById("tMaxContGainCount").innerHTML=data3["tMaxContGainCount"] 
        document.getElementById("tMaxContLossCount").innerHTML=data3["tMaxContLossCount"] 
        document.getElementById("tMaxContGainAmount").innerHTML=data3["tMaxContGainAmount"]
        document.getElementById("tMaxContLossAmount").innerHTML=data3["tMaxContLossAmount"] 
        document.getElementById("dTotalCount").innerHTML=data3["dTotalCount"] 
        document.getElementById("dGainCount").innerHTML=data3["dGainCount"]
        document.getElementById("dLossCount").innerHTML=data3["dLossCount"] 
        document.getElementById("dHoldCount").innerHTML=data3["dHoldCount"] 
        document.getElementById("dWinRate").innerHTML=data3["dWinRate"]
        document.getElementById("dAvgYield").innerHTML=data3["dAvgYield"] 
        document.getElementById("dAvgLoss").innerHTML=data3["dAvgLoss"] 
        document.getElementById("dAvgGain").innerHTML=data3["dAvgGain"]
        document.getElementById("dAvgGLRate").innerHTML=data3["dAvgGLRate"] 
        document.getElementById("dMaxContGainCount").innerHTML=data3["dMaxContGainCount"] 
        document.getElementById("dMaxContLossCount").innerHTML=data3["dMaxContLossCount"]
        document.getElementById("dNoNewHighDays").innerHTML=data3["dNoNewHighDays"] 
        document.getElementById("dNoNewHighPeriod").innerHTML=data3["dNoNewHighPeriod"] 
        document.getElementById("dTotalyield").innerHTML=data3["dTotalyield"]
        document.getElementById("dYearYield").innerHTML=data3["dYearYield"] 
        document.getElementById("dVolatility").innerHTML=data3["dVolatility"] 
        document.getElementById("dSharpRitio").innerHTML=data3["dSharpRitio"]
        document.getElementById("dMarRate").innerHTML=data3["dMarRate"] 
        document.getElementById("wTotalCount").innerHTML=data3["wTotalCount"] 
        document.getElementById("wGainCount").innerHTML=data3["wGainCount"]
        document.getElementById("wLossCount").innerHTML=data3["wLossCount"] 
        document.getElementById("wHoldCount").innerHTML=data3["wHoldCount"] 
        document.getElementById("wWinRate").innerHTML=data3["wWinRate"]
        document.getElementById("wAvgLoss").innerHTML=data3["wAvgLoss"] 
        document.getElementById("wwvgGain").innerHTML=data3["wwvgGain"] 
        document.getElementById("wMaxContGainCount").innerHTML=data3["wMaxContGainCount"]
        document.getElementById("wMaxContLossCount").innerHTML=data3["wMaxContLossCount"] 
        document.getElementById("mTotalCount").innerHTML=data3["mTotalCount"] 
        document.getElementById("mGainCount").innerHTML=data3["mGainCount"]
        document.getElementById("mLossCount").innerHTML=data3["mLossCount"] 
        document.getElementById("mHoldCount").innerHTML=data3["mHoldCount"] 
        document.getElementById("mMaxContGainCount").innerHTML=data3["mMaxContGainCount"]
        document.getElementById("mMaxContLossCount").innerHTML=data3["mMaxContLossCount"] 
        document.getElementById("mAvgLoss").innerHTML=data3["mAvgLoss"] 
        document.getElementById("mAvgGain").innerHTML=data3["mAvgGain"]
        document.getElementById("yTotalCount").innerHTML=data3["yTotalCount"] 
        document.getElementById("yGainCount").innerHTML=data3["yGainCount"] 
        document.getElementById("yLossCount").innerHTML=data3["yLossCount"]
        document.getElementById("yHoldCount").innerHTML=data3["yHoldCount"] 
        document.getElementById("yMAxContGainCount").innerHTML=data3["yMAxContGainCount"] 
        document.getElementById("yMaxContLossCount").innerHTML=data3["yMaxContLossCount"]
        document.getElementById("mAvgLoss").innerHTML=data3["mAvgLoss"] 
        document.getElementById("mAvgGain").innerHTML=data3["mAvgGain"] 
        document.getElementById("yTotalCount").innerHTML=data3["yTotalCount"]
        document.getElementById("yGainCount").innerHTML=data3["yGainCount"] 
        document.getElementById("yLossCount").innerHTML=data3["yLossCount"] 
        document.getElementById("yHoldCount").innerHTML=data3["yHoldCount"]
        document.getElementById("yMAxContGainCount").innerHTML=data3["yMAxContGainCount"] 
        document.getElementById("yMaxContLossCount").innerHTML=data3["yMaxContLossCount"] 
        document.getElementById("yAvgLoss").innerHTML=data3["yAvgLoss"]
        document.getElementById("yAvgGain").innerHTML=data3["yAvgGain"]

        document.getElementById("ID").innerHTML=data4["id"]
        document.getElementById("Ins").innerHTML=data4["instrument"]
        document.getElementById("BeginTime").innerHTML=data4["begin"]
        document.getElementById("Internal").innerHTML=data4["interval"]
        document.getElementById("InternalType").innerHTML=data4["intervalType"]
        document.getElementById("Params").innerHTML=data4["params"]
       

        </script>
    </body>
    </html>
'''.format(bars_json, data['orders'], data['indexes'], data['report'], data['req']))
    tmp.close()
    webbrowser.open('report.html')
