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

        # 이미지 데이터 ESC/POS 포맷으로 변환
        for y in range(0, img_height, 24):  # Thermal 프린터는 24픽셀 단위로 처리
            row_bytes = bytearray()
            for x in range(img_width):
                byte = 0
                for bit in range(8):
                    if y + bit < img_height:  # 이미지 경계 체크
                        pixel = img.getpixel((x, y + bit))
                        if pixel == 0:  # 검정색 픽셀은 0
                            byte |= (1 << (7 - bit))
                row_bytes.append(byte)
            # ESC/POS 명령: 이미지를 지정 위치로 출력
            data += b'\x1b*'  # ESC/POS 이미지 명령
            data += bytes([33, len(row_bytes) % 256, len(row_bytes) // 256])
            data += row_bytes

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
