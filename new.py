from PIL import Image
import win32print
import win32ui

def print_image_with_thermal(image_path, printer_name):
    # 프린터 DC 생성
    hdc = win32ui.CreateDC()
    hdc.CreatePrinterDC(printer_name)

    # 이미지 로드 및 변환
    img = Image.open(image_path)
    img = img.convert("RGB")  # RGB로 변환

    # 이미지 크기 조정
    max_width = 384  # Thermal 프린터 폭
    if img.width > max_width:
        ratio = max_width / img.width
        img = img.resize((max_width, int(img.height * ratio)))

    # 비트맵 생성
    dib = win32ui.CreateBitmap()
    dib.CreateCompatibleBitmap(hdc, img.width, img.height)

    # DC에 비트맵 연결
    hdc.SelectObject(dib)

    # 출력 시작
    hdc.StartDoc('Image Print')
    hdc.StartPage()

    # 비트맵에 이미지 그리기
    dib_bits = img.tobytes("raw", "BGRX")
    dib.SetBitmapBits(dib_bits)
    hdc.StretchBlt(0, 0, img.width, img.height, hdc, 0, 0, img.width, img.height, win32ui.SRCCOPY)

    # 출력 종료
    hdc.EndPage()
    hdc.EndDoc()

    # 자원 정리
    hdc.DeleteDC()

# 사용 예제
printer_name = "POS-80_thermal"
image_path = "cha.png"
print_image_with_thermal(image_path, printer_name)
