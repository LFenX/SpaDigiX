import pyautogui
import time


def send_message(contact, message, count, interval, duration):
    # 打开微信并搜索联系人
    a=pyautogui.position()
    pyautogui.click()  # 设置微信搜索栏的坐标
    pyautogui.write(contact, interval=0.25)  # 输入联系人的名字
    time.sleep(1)  # 等待微信响应
    pyautogui.press('enter')  # 进入聊天窗口
    # 开始发送消息
    end_time = time.time() + duration
    sent_count = 0
    while time.time() < end_time and sent_count < count:
        pyautogui.write(message, interval=0.05)  # 输入消息内容
        pyautogui.press('enter')  # 发送消息
        sent_count += 1
        time.sleep(interval)  # 等待下次发送

    print(f"已成功发送 {sent_count} 条消息")


# 参数说明
contact_name = "文件传输助手"  # 联系人名字
message_content = "你好，这是一条自动发送的消息。"  # 发送的消息内容
message_count = 5  # 要发送的消息条数
send_interval = 2  # 每条消息之间的时间间隔，单位：秒
send_duration = 10  # 总共发送消息的时间限制，单位：秒

# 执行发送操作
send_message(contact_name, "cc", message_count, send_interval, send_duration)
