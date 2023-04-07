import datetime
import cv2
from pyzbar import pyzbar

LOG_FILE_PATH = "log.txt"

cap = cv2.VideoCapture(0)

while True:
    # カメラから画像を取得
    _, frame = cap.read()

    # QRコードを読み取り
    decoded_objs = pyzbar.decode(frame)
    for obj in decoded_objs:
        # QRコードの内容をログファイルに書き出し
        with open(LOG_FILE_PATH, "a") as f:
            f.write("{}: {}\n".format(datetime.datetime.now(), obj.data))

    # 画像を表示
    cv2.imshow("frame", frame)

    # キー入力待ち
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# 終了処理
cap.release()
cv2.destroyAllWindows()