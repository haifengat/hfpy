#!/usr/bin/env python
#coding:utf-8
"""
  Author:  HaiFeng --<galaxy>
  Purpose: 
  Created: 2016/7/5
"""
import os

# C++和python类型的映射字典
type_dict = {
    'int': 'c_int32',
    'char': 'c_char',
    'double': 'c_double',
    'short': 'c_int32',
    'string': 'c_char_p'
}

defline = []
fenum = open(os.path.join(os.path.abspath('..'), 'ctp_enum.py'), 'w', encoding='utf-8') #增加utf-8解决乱码问题
enum_comment = {}

def process_line(line):
	"""处理每行"""
	if '///' in line:           # 注释
		py_line = process_comment(line)
		
		#comment for enum
		if py_line.find('是一个') > 0:
			enum_comment[py_line[py_line.find('Ftdc')+4:py_line.find('是一个')]] = '\t"""%s"""\n' % py_line[py_line.find('是一个')+3:-1]
		
	elif 'typedef' in line:     # 类型申明
		py_line = process_typedef(line)
		
		#enum -> clase xxx(Enum)
		if line.find(' char ') > 0 and line.find('[') < 0:
			key = line.split(' ')[2][:-2]
			key = key[key.find('Ftdc')+4:]
			enum_line = 'class %s(Enum):\n' % key
			enum_line += enum_comment[key]
			for l in defline:
				enum_line += '\t%s\n' % l
			enum_line += '\n\t#----------------------------------------------------------------------\n'
			enum_line += '\tdef __int__(self):\n'
			enum_line += '\t\t"""return int value"""\n'
			enum_line += '\t\treturn self.value\n\n'	
			enum_line += '\t#----------------------------------------------------------------------\n'
			enum_line += '\tdef __char__(self):\n'
			enum_line += '\t\t"""return c_char value"""\n'
			enum_line += '\t\treturn ctypes.c_char(chr(self.value))\n\n'
			
			print (enum_line)
			fenum.write(enum_line)
		defline.clear()
		
	elif '#define' in line:     # 定义常量
		py_line = process_define(line)
		
		#enum relate define
		if py_line:
			defline.append('%s = %s' % (py_line[py_line.find('[')+2:py_line.find(']')-1].split('_')[-1], ord(py_line[py_line.find("'"):py_line.find("'")+3][1])))
			
	elif line == '\n':          # 空行
		py_line = line
	else:
		py_line = ''

	return py_line


def process_comment(line):
	"""处理注释"""
	# if line[3] == '/':
	#     py_line = ''
	# else:
	#     py_line = '#' + line[3:]
	py_line = '#' + line[3:]
	return py_line


def process_typedef(line):
	"""处理类型申明"""
	content = line.split(' ')
	type_ = type_dict[content[1]]

	if type_ == 'c_char' and '[' in line:
		#type_ = 'string'
		type_ = '%s*%s' % (type_, line[line.index('[')+1:line.index(']')])

	keyword = content[2]
	if '[' in keyword:
		i = keyword.index('[')
		keyword = keyword[:i]
	else:
		keyword = keyword.replace(';\n', '')  # 删除行末分号

	py_line = 'typedefDict["%s"] = "%s"\n' % (keyword, type_)

	return py_line


def process_define(line):
	"""处理定义常量"""
	content = line.split(' ')
	constant = content[1]

	if len(content)>2:
		value = content[-1]
		py_line = 'defineDict["%s"] = %s' % (constant, value)
	else:
		py_line = ''

	return py_line


def main():
	"""主函数"""
	try:
		fcpp = open(os.path.join('C:\\Users\\Administrator\\Documents\\Codes\\hf_proxy\\ctp\\ctp_6.3.0_x64', 'ThostFtdcUserApiDataType.h'),'r', encoding='gbk')
		fpy = open('ctp_data_type.py', 'w', encoding='utf-8') #增加utf-8解决乱码问题
	
		fpy.write('#!/usr/bin/env python\n')    
		fpy.write('#coding:utf-8\n')
		fpy.write('\n')
		fpy.write('defineDict = {}\n')
		fpy.write('typedefDict = {}\n')
		fpy.write('\n')

	
		fenum.write('#!/usr/bin/env python\n')    
		fenum.write('#coding:utf-8\n')

		for line in fcpp:
			py_line = process_line(line)
			if py_line:
				fpy.write(py_line)
				#print(py_line)

		fcpp.close()
		fpy.close()
		fenum.close()

		print('data_type.py生成过程完成')
	except:
		print('data_type.py生成过程出错')


if __name__ == '__main__':
	main()

