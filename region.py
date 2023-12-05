import pyautogui
import keyboard
import dataclasses

class Region:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1: int = x1
        self.y1: int = y1
        self.x2: int = x2
        self.y2: int = y2
        self.active = False

    def get_points(self):
        return self.x1, self.y1, self.x2, self.y2

    def sort(self):
        if self.x1 > self.x2:
            tmp = self.x1
            self.x1 = self.x2
            self.x2 = tmp
        if self.y1 > self.y2:
            tmp = self.y1
            self.y1 = self.y2
            self.y2 = tmp

region = Region()

num_press = 0
kill = False
class SelectRegion:
    def __init__(self, hotkey):
        keyboard.add_hotkey(hotkey, self.on_triggered)
    
    def on_triggered(self):
        global region, num_press, kill

        try:
            
            num_press += 1
            print(num_press)
            if num_press == 1:
                x, y = pyautogui.position()
                print(f'Start:{x},{y}')
                region.x1, region.y1 = x, y
            elif num_press >= 2:
                x, y = pyautogui.position()
                print(f'End  :{x},{y}')
                region.x2, region.y2 = x, y
                region.active = True
        except:
            pass

    def select_region(self):
        global region, num_press, kill

        while True:
            if kill:
                return False
            elif region.active:
                region.sort()
                region.active = False
                num_press = 0 
                return region
            else:
                continue

if __name__ == "__main__":
    import config
    cfg = config.load_config()
    hotkey = cfg["hotkey"]
    select_region = SelectRegion(hotkey)
    region = select_region.select_region()
    print(region.get_points())
