import os
from PIL import Image


def convert_png_to_jpg(directory='.'):
    """
    将指定目录下的所有PNG图片转换为JPG格式
    :param directory: 要处理的目录，默认为当前目录
    """
    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        if filename.lower().endswith('.png'):
            try:
                # 打开PNG图片
                png_path = os.path.join(directory, filename)
                img = Image.open(png_path)

                # 创建JPG文件名（相同的文件名，只是扩展名改为.jpg）
                jpg_path = os.path.join(directory, filename[:-4] + '.jpg')

                # 转换为RGB模式（JPG不支持透明度）
                if img.mode in ('RGBA', 'LA'):
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    background.paste(img, mask=img.split()[-1])
                    img = background
                else:
                    img = img.convert('RGB')

                # 保存为JPG格式
                img.save(jpg_path, 'JPEG', quality=95)
                print(f"转换成功: {png_path} -> {jpg_path}")

                # 可选：删除原始PNG文件
                # os.remove(png_path)
                # print(f"已删除原始文件: {png_path}")

            except Exception as e:
                print(f"处理文件 {filename} 时出错: {e}")


if __name__ == '__main__':
    print("开始转换PNG到JPG...")
    convert_png_to_jpg()
    print("转换完成！")