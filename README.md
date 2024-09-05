# 中文英文OCR

从网易开源项目QAnything提取出来的中文OCR识别代码和模型，可以准确识别中文字符

https://github.com/netease-youdao/QAnything

使用方法：

```
from ocr import  OCRQAnything
import cv2

if __name__ == '__main__':
    ocr_re = OCRQAnything(model_dir='ocr_models',
                       device='gpu') # device='cpu'
   
    image = cv2.imread('1.png')
    res = ocr_re(image)
    print(res)
```