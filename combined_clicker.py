import pyautogui
import cv2
import numpy as np
import time

# 设置图像路径
button_red_img = 'button_red.png'
button_green_img = 'button_green.png'
checkbox_img = 'checkbox.png'
finish_img = 'finish.png'

# 匹配图像并返回中心坐标
def locate_button(template_path, confidence=0.8):
    screenshot = pyautogui.screenshot()
    screenshot_rgb = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    template = cv2.imread(template_path)
    
    if template is None:
        print(f"无法加载图像: {template_path}")
        return None
        
    result = cv2.matchTemplate(screenshot_rgb, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= confidence:
        # 返回中心点位置
        h, w = template.shape[:2]
        center_x = max_loc[0] + w // 2
        center_y = max_loc[1] + h // 2
        return center_x, center_y, max_val
    else:
        return None

# 自动点击按钮
def auto_click_button(template_path, button_name):
    result = locate_button(template_path)
    if result:
        x, y, confidence = result
        print(f"检测到{button_name}，点击位置：({x}, {y})，匹配度：{confidence:.2f}")
        pyautogui.click(x, y)
        return True
    else:
        print(f"未检测到{button_name}，无需点击")
        return False

# 检查所有按钮
def check_all_buttons():
    # 检查并点击 hyper.py 中的红色按钮
    auto_click_button(button_red_img, "红色按钮")
    
    # 检查并点击 hyper.py 中的绿色按钮
    auto_click_button(button_green_img, "绿色按钮")
    
    # 检查并点击 onprover.py 中的复选框
    auto_click_button(checkbox_img, "复选框")
    
    # 检查并点击 onprover.py 中的完成按钮
    auto_click_button(finish_img, "完成按钮")

# 主循环（每隔5秒检测一次）
def main_loop():
    print("开始自动检测并点击所有按钮...")
    try:
        while True:
            check_all_buttons()
            time.sleep(5)
    except KeyboardInterrupt:
        print("程序已手动停止")

if __name__ == '__main__':
    main_loop()
