from paddleocr import PaddleOCR
import numpy as np
from cap import get_screenshot
from llm import get_ans
import ctypes
import time


# 加载 OCR 模型
ocr = PaddleOCR(
    use_angle_cls=True,
    lang="ch",
    det_model_dir="det_model_dir",
    rec_model_dir="rec_model_dir",
    cls_model_dir="cls_model_dir",
)
while True:
    screenshot, (absolute_left, absolute_top, absolute_right, absolute_bottom) = get_screenshot("BlueStacks App Player")
    img_array = np.array(
        screenshot
    )  # 还记得上面截图得到的 screenshot 嘛，在这里被转化成了 numpy 数组
    result = ocr.ocr(img_array, cls=True)  # OCR 识别
    questionBody = ""
    for idx, line in enumerate(result[0]):
        text = line[1][0]
        if idx == 0:
            questionBody += f"<Question>{text}"
        else:
            boxes = line[0]
            questionBody += f"\n<Option>{str(idx)}. {text}"

    print(questionBody)
    # print(get_ans(questionBody))

    final_selection = int(get_ans(questionBody).content.split(".")[0][-1])
    # final_selection = 4
    print(f"最终选择: {final_selection}")

    def get_click_position(selection):
        """
        根据选择题选项，返回点击位置。
        """
        # 选项相对位置
        select_rel_pos = result[0][selection][0]
        x = (select_rel_pos[0][0] + select_rel_pos[2][0]) // 2 + absolute_left
        y = (select_rel_pos[0][1] + select_rel_pos[2][1]) // 2 + absolute_top
        
        return x, y

    click_x, click_y = get_click_position(final_selection)

    print(f"点击位置: ({click_x}, {click_y})")

    # 设置 Windows API 函数的参数类型
    SetCursorPos = ctypes.windll.user32.SetCursorPos
    SetCursorPos.argtypes = [ctypes.c_int, ctypes.c_int]

    mouse_event = ctypes.windll.user32.mouse_event
    mouse_event.argtypes = [ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong]

    def click(x, y):
        """
        模拟鼠标在屏幕上的点击
        """
        # 移动鼠标到指定坐标 (x, y)
        SetCursorPos(x, y)
        
        # 模拟鼠标左键按下和释放
        mouse_event(2, 0, 0, 0, 0)  # 左键按下
        mouse_event(4, 0, 0, 0, 0)  # 左键释放
        
        SetCursorPos(0, 0)

        
    click(int(click_x), int(click_y))
    time.sleep(0.4)
