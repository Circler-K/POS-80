from PIL import ImageWin, Image
import win32print
import win32ui

def print_image_with_driver(printer_name, image_path):
    # 프린터 DC 설정
    hPrinter = win32print.OpenPrinter(printer_name)
    hdc = win32ui.CreateDC()
    hdc.CreatePrinterDC(printer_name)

    try:
        # 이미지 로드
        img = Image.open(image_path)
        img_width, img_height = img.size

        # 프린터 해상도 가져오기
        printer_width = hdc.GetDeviceCaps(110)  # HORZRES
        printer_height = hdc.GetDeviceCaps(111)  # VERTRES

        # 이미지 비율에 맞게 크기 조정
        aspect_ratio = img.height / img.width
        target_width = printer_width
        target_height = int(printer_width * aspect_ratio)
        img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)

        # 출력 설정
        hdc.StartDoc("Printing Image")
        hdc.StartPage()

        # 이미지를 DIB로 변환 및 출력
        dib = ImageWin.Dib(img)
        dib.draw(hdc.GetHandleOutput(), (0, 0, target_width, target_height))

        hdc.EndPage()
        hdc.EndDoc()

    finally:
        hdc.DeleteDC()
        win32print.ClosePrinter(hPrinter)

# 사용 예제
printer_name = "POS-80_thermal"
# image_path = "zerotwo.jpg"
image_path = "123.png"
image_path = "cha.png"
print_image_with_driver(printer_name, image_path)
