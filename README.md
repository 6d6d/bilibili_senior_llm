# bilibili_senior_llm

## 简介

`bilibili_senior_llm` 是一个用于帮助通过 B站硬核会员考试的工具。该工具利用 OCR 技术识别屏幕上的题目和选项，然后使用语言模型来生成答案，并模拟鼠标点击来自动答题。

## 功能特点

- 使用 PaddleOCR 进行文字识别。
- 自动合并接近的文字框以提高识别准确性。
- 使用豆包doubao-1-5-pro-32k-250115模型生成答案。
- 模拟鼠标点击选择正确答案。

## 安装依赖

确保已安装依赖库：

```bash
pip install -r requirements.txt
```

或

```bash
pip install paddlepaddle paddleocr pyautogui pywin32
```

## 配置文件

你需要配置 `llm.py` 文件中的 `get_ans` 函数，确保它能够调用你的语言模型 API 并返回答案。

## 使用方法

1. **获取屏幕截图**：确保你的设备或模拟器窗口标题为 "BlueStacks"(BlueStacks4) 或其他你定义的标题(main中的get_screenshot处修改）。
2. **运行脚本**：启动 `main.py` 脚本。
3. **开始考试**：在 B站上开始硬核会员考试，脚本将自动进行识别和答题。

## 注意事项

- 确保考试界面在屏幕中央，并且没有遮挡物。（建议打开后全屏，保证画面居中）
- 如果考试界面不在屏幕中央，请调整截图区域。
- 请遵循 B站的相关规定，合理使用此工具，避免违规。
