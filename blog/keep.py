import qrcode
import time

# QRコードを生成する関数
def generate_qrcode():
    # 現在の日付と時刻を取得
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    # QRコードの内容として、現在の日付と時刻を設定
    qr = qrcode.QRCode(version=1, box_size=10, border=2)
    qr.add_data(now)
    qr.make(fit=True)
    # QRコードを保存
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")

# メイン関数
if __name__ == "__main__":
    # QRコードを生成
    generate_qrcode()

    # ユーザーにQRコードをスキャンするように促す
    print("QRコードをスキャンしてください。")
    input()

    # 勤怠時間をログに記録
    with open("log.txt", "a") as f:
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{now}\n")

    print("勤怠時間を記録しました。")