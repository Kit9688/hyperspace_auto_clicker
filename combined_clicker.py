import pyautogui
import cv2
import numpy as np
import time

# 设置图像路径
# 需要点击的按钮
button_red_img = 'button_red.png'  # 红色按钮 - 需要点击
checkbox_img = 'checkbox.png'    # 复选框 - 需要点击

# 已点击状态的指示器
button_green_img = 'button_green.png'  # 绿色按钮 - 已点击状态
finish_img = 'finish.png'          # 完成按钮 - 已点击状态

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

# 检查按钮状态并点击需要点击的按钮
def check_all_buttons():
    # 检查红色按钮是否存在，如果存在则点击
    red_clicked = auto_click_button(button_red_img, "红色按钮")
    
    # 检查绿色按钮是否存在（已点击状态的指示器）
    green_result = locate_button(button_green_img)
    if green_result:
        x, y, confidence = green_result
        print(f"检测到绿色按钮（已点击状态），位置：({x}, {y})，匹配度：{confidence:.2f}")
    
    # 检查复选框是否存在，如果存在则点击
    checkbox_clicked = auto_click_button(checkbox_img, "复选框")
    
    # 检查完成按钮是否存在（已点击状态的指示器）
    finish_result = locate_button(finish_img)
    if finish_result:
        x, y, confidence = finish_result
        print(f"检测到完成按钮（已点击状态），位置：({x}, {y})，匹配度：{confidence:.2f}")

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
