from distutils.core import setup
import py2exe

data_files = [('de422.bsp', [r"C:\Users\DELL\PycharmProjects\pythonProject2\de422.bsp"])]  # 替换为您的数据文件的路径和名称

setup(
    console=['可视化界面.py'],  # 替换为您的Python脚本文件名
    data_files=data_files
)
