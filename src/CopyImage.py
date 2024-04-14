from io import BytesIO
import win32clipboard # type: ignore
from PIL import Image

def copy_to_clipboard(path):       
        
    image = Image.open(path)

    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()



if __name__ == '__main__':
    copy_to_clipboard(r'Gold.jpg')