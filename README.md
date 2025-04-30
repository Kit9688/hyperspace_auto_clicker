**🌌 Hyperspace 自动点击助手**

这是一个使用图像识别技术的自动点击脚本，适用于检测并保持 Hyperspace 客户端中的某个按钮处于“开启”（绿色）状态。如果检测到按钮变为红色（关闭），脚本会自动点击重新打开。

ONProver脚本请使用 onprover.py finish.png checkbox.png

**🖥 运行环境**

- Python 3.10 或 3.11
- 支持 macOS 和 Windows


**📦 创建并激活虚拟环境**

- 💻 macOS / Linux：
```bash
python3 -m venv venv
source venv/bin/activate
```

- 🪟 Windows：
```bash
python -m venv venv
venv\Scripts\activate
```


**🔧 安装依赖**

```bash
pip install pyautogui opencv-python numpy pillow
```


**✅ 运行脚本**

```bash
python hyper.py
```


**❗️ 注意事项**

- Hyperspace客户端窗口需要置顶，不要被其它窗口覆盖，可以放到桌面角落
