# coding:utf-8

from setuptools import setup

setup(
        name='frelation',
        version='0.0.1',
        description='在机器学习中，构造的特征多且乱，这个库用来展示已经构造的特征关系，方便查漏补缺',
        author='pipdax',
        author_email='pipdax@126.com',
        url='https://github.com/pipdax/frelation',
        py_modules=['frelation'],
        install_requires=[    # 依赖列表
        'pyecharts>=0.5.8',
    ]
)
