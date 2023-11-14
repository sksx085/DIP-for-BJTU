from pyzbar.pyzbar import decode
from PIL import Image

def decode_qr_code(image_path):
    try:
        # 打开图片文件
        img = Image.open(image_path)
        
        # 使用 pyzbar 库来解码二维码信息
        decoded_objects = decode(img)
        
        if decoded_objects:
            # 返回二维码信息
            return decoded_objects[0].data.decode('utf-8')
        else:
            return None
    except Exception as e:
        print("Error:", e)
        return None

if __name__ == "__main__":
    image_path = input("Enter the path to the image containing the QR code: ")
    result = decode_qr_code(image_path)
    
    if result:
        print("QR Code Contents:", result)
    else:
        print("Failed to decode QR Code or no QR code found in the image.")
