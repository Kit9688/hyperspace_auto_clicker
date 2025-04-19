import pyautogui
import cv2
import numpy as np
import time

# 设置图像路径
red_button_img = 'button_red.png'
green_button_img = 'button_green.png'

# 匹配图像并返回中心坐标
def locate_button(template_path, confidence=0.8):
    screenshot = pyautogui.screenshot()
    screenshot_rgb = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    template = cv2.imread(template_path)

    result = cv2.matchTemplate(screenshot_rgb, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= confidence:
        # 返回中心点位置
        h, w = template.shape[:2]
        center_x = max_loc[0] + w // 2
        center_y = max_loc[1] + h // 2
        return center_x, center_y
    else:
        return None

# 自动点击红色按钮（关闭状态）
def auto_click_button():
    pos = locate_button(red_button_img)
    if pos:
        print(f"检测到红色按钮，点击位置：{pos}")
        pyautogui.click(pos)
    else:
        print("未检测到红色按钮，无需点击")

# 主循环（每隔5秒检测一次）
def main_loop():
    print("开始自动检测并点击...")
    try:
        while True:
            auto_click_button()
            time.sleep(5)
    except KeyboardInterrupt:
        print("程序已手动停止")

if __name__ == '__main__':
    main_loop()
