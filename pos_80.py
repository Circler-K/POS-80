import os

# os.startfile("C:/Users/admin/Documents/project/POS_80/pos_80.py", "print")

# rundll32 shimgvw.dll,ImageView_PrintTo "cha.png" "POS-80_thermal"


import win32print
import win32ui
from PIL import Image

def print_image(image_path, printer_name):
    printer = win32print.OpenPrinter(printer_name)
    hprinterdc = win32print.WritePrinter(printer_name)
    # hprinterdc = win32print.CreatePrinterDC(printer_name)

    # Open image and get dimensions
    img = Image.open(image_path)
    hbitmap = win32ui.CreateBitmapFromImage(img)

    hprinterdc.StartDoc("Image Print")
    hprinterdc.StartPage()
    hbitmap.Paint(hprinterdc.GetHandleOutput())
    hprinterdc.EndPage()
    hprinterdc.EndDoc()
    hbitmap.DeleteObject()
    hprinterdc.DeleteDC()
    win32print.ClosePrinter(printer)

# 사용 예:
print_image("cha.png", "POS-80_thermal")
# print_image("cha.png", "Microsoft Print to PDF")



# win32printing




# from PIL import Image
# import win32print
# import win32ui
# import win32api

# def print_image_with_thermal(image_path, printer_name):
#     # 열려 있는 프린터 핸들
#     printer = win32print.OpenPrinter(printer_name)
#     printer_info = win32print.GetPrinter(printer, 2)
    
#     # Device Context 생성
#     hdc = win32ui.CreateDC()
#     hdc.CreatePrinterDC(printer_name)

#     # 이미지 열기
#     img = Image.open(image_path)
#     img = img.convert("RGB")  # 필요한 경우 이미지 변환

#     # 이미지 크기 조정 (Thermal 프린터에 맞게)
#     width, height = img.size
#     max_width = 384  # 예제: Thermal 프린터의 폭 (픽셀)
#     if width > max_width:
#         ratio = max_width / width
#         img = img.resize((max_width, int(height * ratio)))
    
#     # 출력 시작
#     hdc.StartDoc('Image Print')
#     hdc.StartPage()

#     # 이미지 출력
#     dib = win32ui.CreateBitmap()
#     dib.CreateCompatibleBitmap(hdc, img.width, img.height)
#     hdc.SelectObject(dib)
#     dib.Paint(hdc.GetHandleOutput(), 0, 0, img.width, img.height)

#     hdc.EndPage()
#     hdc.EndDoc()
#     hdc.DeleteDC()
#     win32print.ClosePrinter(printer)

# # 사용법
# printer_name = "POS-80_thermal"
# image_path = "cha.png"
# print_image_with_thermal(image_path, printer_name)
