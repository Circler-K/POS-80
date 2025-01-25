import win32print
import win32ui

# 프린터 열기
printer_name = "POS-80_thermal"
hPrinter = win32print.OpenPrinter(printer_name)

try:
    # 프린터 설정 시작
    win32print.StartDocPrinter(hPrinter, 1, ("Test Document", None, "RAW"))
    win32print.StartPagePrinter(hPrinter)

    # 프린터로 보낼 데이터 (텍스트 출력)
    data = "Hello, World!\n".encode('utf-8')  # 바이트로 변환
    win32print.WritePrinter(hPrinter, data)

    # 페이지 및 문서 종료
    win32print.EndPagePrinter(hPrinter)
    win32print.EndDocPrinter(hPrinter)

finally:
    # 프린터 닫기
    print('hi')
    win32print.ClosePrinter(hPrinter)
