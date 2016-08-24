# encoding: UTF-8

__author__ = 'CHENXY'

from ctp_data_type import *
import os

def main():
    """主函数"""
    fcpp = open(os.path.join('C:\\Users\\Administrator\\Documents\\Codes\\hf_proxy\\ctp\\ctp_6.3.0_x64', 'ThostFtdcUserApiStruct.h'), 'r', encoding='GB2312')
    fpy = open(os.path.join(os.path.abspath('..'), 'ctp_struct.py'), 'w', encoding='utf-8')
    
    fpy.write('#!/usr/bin/env python\n')    
    fpy.write('#coding:utf-8\n')
    fpy.write('from ctypes import *\n')
    fpy.write('from ctp_enum import *\n')
    
    fpy.write('\n')
    #fpy.write('structDict = {}\n')
    #fpy.write('\n')

    for no, line in enumerate(fcpp):
        
        # 结构体申明注释
        if '///' in line and '\t' not in line:
            remark = line[3:-1]
            continue

        # 结构体变量注释
        elif '\t///' in line:
            remark = line[4:-1]
            continue;

        # 结构体申明
        elif 'struct ' in line:            
            content = line.split(' ')
            name = content[1].replace('\n','')
            py_line = '%s = {}\n' % name
            
            #struct begin
            py_line = 'class %s(Structure):\n' % name
            py_line += '\t"""%s"""\n' % remark
            py_line += '\t_fields_ = [\n'

        # 结构体变量
        elif '\t' in line and '///' not in line:
            content = line.split('\t')
            typedef = content[1]
            type_ = typedefDict[typedef]
            variable = content[2].replace(';\n', "")
            py_line = '%s["%s"] = "%s"\n' % (name, variable, type_)
            #fields
            py_line = '\t\t#%s\n' % remark
            py_line += '\t\t("%s",%s),\n' % (variable, type_)
            
            #
            if type_.find('c_char*') >= 0:
                if variable.find('Msg') >= 0:
                    py_get += "\tdef get%s(self):\n\t\treturn self.%s.decode('GB2312')\n" % (variable, variable)
                else:
                    py_get +="\tdef get%s(self):\n\t\treturn self.%s.decode('ascii')\n" % (variable, variable)
            elif type_.find('c_char') >= 0:
                py_get +="\tdef get{0}(self):\n\t\treturn {1}(ord(self.{0}))\n".format(variable, typedef[typedef.find('Ftdc')+4:])
            else:
                py_get +="\tdef get{0}(self):\n\t\treturn self.{0}\n".format(variable)

        # 结构体结束
        elif '}' in line:
            py_line = "structDict['%s'] = %s\n\n" % (name, name)
            
            #struct end
            py_line = '\t\t]\n\n'
            py_line += py_get + '\n'

        # 结构体开始
        elif '{' in line:
            py_line = ''
            py_get = ''

        # 其他
        else:
            py_line = '\n'
            continue

        fpy.write(py_line)


if __name__ == '__main__':
    main()