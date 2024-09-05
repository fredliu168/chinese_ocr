from ocr_src.ocr import  OCRQAnything
import cv2

if __name__ == '__main__':
    ocr_re = OCRQAnything(model_dir='ocr_models',
                       device='gpu') # device='cpu'
   
    image = cv2.imread('images/1.png')
    res = ocr_re(image)
    print(res)
 