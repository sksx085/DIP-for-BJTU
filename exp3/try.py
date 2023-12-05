import numpy as np
from PIL import Image

def save_image_from_matrix(img_matrix, file_path):

    # The height and width of the image
    height = len(img_matrix)
    width = len(img_matrix[0])
    
    # Create a new Image object in RGB mode
    img = Image.new('RGB', (width, height))
    pixels = img.load()
    
    # Copy data to the image
    for y in range(height):
        for x in range(width):
            pixels[x, y] = img_matrix[y][x]
    
    # Save the image
    img.save(file_path)


def read_bmp(filename):
    with open(filename, 'rb') as f:
        # BMP文件头部信息通常是54字节
        bmp_header = f.read(54)  
        
        # 从头部信息中解析宽度和高度
        # 使用小端字节序解析32位整数
        w = int.from_bytes(bmp_header[18:22], 'little')
        h = int.from_bytes(bmp_header[22:26], 'little')
        
        # 每行的像素数据长度必须是4的倍数
        bytes_per_row = ((w * 3 + 3) // 4) * 4
        
        # 读取所有像素数据
        pixel_data = f.read()
        
        # 创建一个空的图像矩阵
        image_matrix = [[None for _ in range(w)] for _ in range(h)]
        
        # 填充图像矩阵
        for j in range(h):
            for i in range(w):
                # 计算当前行的开始位置
                row_start = bytes_per_row * (h - 1 - j)
                # 像素数据的索引计算需要考虑每行的填充字节
                index = row_start + i * 3
                # 检查索引是否在像素数据的长度内
                if index + 3 <= len(pixel_data):
                    # BMP格式存储顺序是BGR
                    b, g, r = pixel_data[index:index+3]
                    # 将BGR转换为RGB，并存储到图像矩阵中
                    image_matrix[j][i] = (r, g, b)
                else:
                    # 如果索引超出范围，则填充为黑色或任何默认值
                    image_matrix[j][i] = (0, 0, 0)
        
        return image_matrix


    
def mean_filter_color(img_matrix, kernel_size):
    """
    Apply mean filter to the color image matrix.
    :param img_matrix: 3D list of tuples - the image matrix where each tuple represents a pixel's RGB values.
    :param kernel_size: integer - the size of the kernel; it should be an odd number.
    :return: 3D list of tuples - the filtered image matrix.
    """
    k = kernel_size // 2
    width = len(img_matrix[0])
    height = len(img_matrix)
    
    filtered_img = [[(0, 0, 0)] * width for _ in range(height)]
    
    for y in range(height):
        for x in range(width):
            sum_r = sum_g = sum_b = 0
            count_pixels = 0
            
            for ky in range(-k, k + 1):
                for kx in range(-k, k + 1):
                    new_x = x + kx
                    new_y = y + ky
                    
                    if 0 <= new_x < width and 0 <= new_y < height:
                        r, g, b = img_matrix[new_y][new_x]
                        sum_r += r
                        sum_g += g
                        sum_b += b
                        count_pixels += 1
            
            mean_r = sum_r // count_pixels
            mean_g = sum_g // count_pixels
            mean_b = sum_b // count_pixels
            
            filtered_img[y][x] = (mean_r, mean_g, mean_b)

    return filtered_img



def median_filter(img_matrix, kernel_size):
    """
    Apply median filter to the image matrix.
    :param img_matrix: 2D list of integers - the image matrix where each value represents a pixel's intensity.
    :param kernel_size: integer - the size of the kernel; it should be an odd number.
    :return: 2D list of integers - the filtered image matrix.
    """
    k = kernel_size // 2
    width = len(img_matrix[0])
    height = len(img_matrix)
    
    filtered_img = [[0] * width for _ in range(height)]
    
    for y in range(height):
        for x in range(width):
            # Collect all the pixels within the kernel
            kernel_pixels = []
            for ky in range(-k, k+1):
                for kx in range(-k, k+1):
                    new_x = x + kx
                    new_y = y + ky
                    
                    if (0 <= new_x < width) and (0 <= new_y < height):
                        kernel_pixels.append(img_matrix[new_y][new_x])
            
            # Sort the list of pixels and choose the median value
            kernel_pixels.sort()
            filtered_img[y][x] = kernel_pixels[len(kernel_pixels) // 2]

    return filtered_img

filename = '/Users/sksx085/Desktop/各种实验报告等狗屎/数字图像处理/converted_image.bmp' 
image_matrix = read_bmp(filename)

"""
mean_filtered_img = mean_filter_color(image_matrix, 3)
median_filtered_img = median_filter(image_matrix, 3)

#print(mean_filtered_img, median_filtered_img)

for row in mean_filtered_img:
    show_row = '[' + ','.join(str(elem) for elem in row) +']'
    print(show_row)
    
"""

# Assuming you have your image_matrix and the functions mean_filter_color and median_filter are defined and working properly
mean_filtered_img = mean_filter_color(image_matrix, 3)
median_filtered_img = median_filter(image_matrix, 3)

# Save the mean filtered image to a file
save_image_from_matrix(mean_filtered_img, 'mean_filtered_image.bmp')

# Save the median filtered image to a file
save_image_from_matrix(median_filtered_img, 'median_filtered_image.bmp')