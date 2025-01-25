



from PIL import Image
import win32print
import win32ui

def print_image(printer_name, image_path):
    # 프린터 열기
    hPrinter = win32print.OpenPrinter(printer_name)

    try:
        # 프린터 설정 시작
        win32print.StartDocPrinter(hPrinter, 1, ("Image Print", None, "RAW"))
        win32print.StartPagePrinter(hPrinter)

        # 이미지 로드 및 변환
        img = Image.open(image_path)
        img = img.convert("1")  # 흑백(B/W)로 변환
        img_width, img_height = img.size

        # ESC/POS 명령 생성
        data = bytearray()

        with open("cha.png", "rb") as f:
            byte = f.read(1)
            while byte != b"":
                data+=byte
                byte = f.read(1)

        # 출력 및 자원 해제
        win32print.WritePrinter(hPrinter, data)
        win32print.EndPagePrinter(hPrinter)
        win32print.EndDocPrinter(hPrinter)

    finally:
        # 프린터 닫기
        win32print.ClosePrinter(hPrinter)

# 사용 예제
printer_name = "POS-80_thermal"
image_path = "cha.png"
print_image(printer_name, image_path)
