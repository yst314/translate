import pyautogui
import keyboard
import dataclasses
import time

class Region:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1: int = x1
        self.y1: int = y1
        self.x2: int = x2
        self.y2: int = y2

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

class SelectRegion:
    def __init__(self, hotkey):
        self.region = Region()
        self.num_press = 0
        self.kill = False
        self.active = True
        keyboard.add_hotkey(hotkey, self.on_triggered)
    
    def on_triggered(self):
        if self.active:
            self.num_press += 1
            if self.num_press == 1:
                x, y = pyautogui.position()
                print(f'Start:{x},{y}')
                self.region.x1, self.region.y1 = x, y
            elif self.num_press >= 2:
                x, y = pyautogui.position()
                print(f'End  :{x},{y}')
                self.region.x2, self.region.y2 = x, y
                self.active = False

        
    def select_region(self):
        self.active = True
        while True:
            if self.kill:
                return False
            elif not self.active:
                self.region.sort()
                self.num_press = 0 
                return self.region
            else:
                time.sleep(0.5)
                continue

if __name__ == "__main__":
    import config
    cfg = config.load_config()
    hotkey = cfg["hotkey"]
    select_region = SelectRegion(hotkey)
    region = select_region.select_region()
    print(region.get_points())
