import pyautogui
from region import Region

def capture(region:Region):
    x1, y1, x2, y2 = region.get_points()
    try:
        im = pyautogui.screenshot("screenshot.jpg", region=(x1,y1, x2-x1,y2-y1))
    except ValueError as e:
        raise e
    return im 

if __name__ == '__main__':
    region = Region(10, 10, 50, 50)
    im = capture(region)
    print(im)