#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 8:15
# @Author  : HaiFeng
# @Email   : 24918700@qq.com


from setuptools import setup
import os

this_directory = os.path.abspath(os.path.dirname(__file__))


# 读取文件内容
def read_file(filename):
    with open(os.path.join(this_directory, filename), encoding='utf-8') as f:
        desc = f.read()
    return desc


# 获取依赖
def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]


long_description = read_file('README.md')
long_description_content_type = "text/markdown",  # 指定包文档格式为markdown

# talib无需加入 os.system('pipreqs . --encoding=utf8 --force')  # 生成 requirements.txt

setup(
    name='hfpy',  # 包名
    python_requires='>=3.4.0',  # python环境
    version='0.1.6',  # 包的版本
    description="Hai Feng Python Future Trading Platform",  # 包简介，显示在PyPI�
    long_description=long_description,  # 读取的Readme文档内容
    long_description_content_type=long_description_content_type,  # 指定包文档格式为markdown
    author="HaiFeng",  # 作者相关信�
    author_email='haifengat@vip.qq.com',
    url='https://github.com/haifengat/hf_at_py',
    # 指定包信息，还可以用find_packages()函数
    # packages=find_packages(),
    packages=['hfpy'],
    install_requires=read_requirements('requirements.txt'),  # 指定需要安装的依赖
    include_package_data=True,
    license="MIT License",
    platforms="any",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
