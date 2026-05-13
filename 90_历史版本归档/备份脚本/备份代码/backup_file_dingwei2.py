import shutil
import os
import time

def backup_file(source_file, backup_folder):
    # 获取当前时间
    current_time = time.strftime('%Y-%m-%d_%H-%M-%S')
    # 构造备份文件名
    backup_file_name = f"backup_{current_time}SpaDigiX_1.1.1.20231029_Alpha.py"
    # 构造备份文件的完整路径
    backup_file_path = os.path.join(backup_folder, backup_file_name)

    # 备份文件
    shutil.copy(source_file, backup_file_path)
    print(f"Backup created: {backup_file_path}")

# 源文件路径
source_file = r"C:\Users\DELL\PycharmProjects\pythonProject2\定位定级+应用2\SpaDigiX_1.1.2.20231125_Alpha.py"
# 备份文件夹路径
backup_folder = r"G:\SpaDigiX_backup\SpaDigiX_1.1.2.20231125_Alpha_backup"

# 定时备份的时间间隔（秒）
backup_interval = 15 * 60  # 每十五分钟备份一次

while True:
    # 执行备份操作
    backup_file(source_file, backup_folder)
    # 等待指定的时间间隔
    time.sleep(backup_interval)
