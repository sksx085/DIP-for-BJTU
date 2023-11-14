import qrcode

def generate_qr_code(data, file_name):
    # 创建二维码对象
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    # 向二维码中添加数据
    qr.add_data(data)
    qr.make(fit=True)
    
    # 创建并保存二维码图片
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

if __name__ == "__main__":
    # 要嵌入二维码的数据
    data = "Hello, this is a QR Code!"
    
    # 生成的二维码图片文件名
    file_name = "my_qr_code.png"
    
    # 调用函数生成二维码
    generate_qr_code(data, file_name)
    print(f"QR Code generated as {file_name}")
