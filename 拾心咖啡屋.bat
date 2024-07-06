@echo off

rem Conda 环境名称
set conda_env=Cafe

rem 地址端口配置
set ip_address=0.0.0.0
set port=11451

rem Conda 安装路径
set conda_path=C:\Users\RoyCoya\anaconda3

rem 你的 Django 项目路径
set project_path=D:\Github\CoyaCoffee

rem 激活 Conda 环境
call "%conda_path%\Scripts\activate" %conda_env%

rem 启动 Django 项目
start cmd /k "python %project_path%\manage.py runserver %ip_address%:%port%"
