from pynput import mouse, keyboard
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

cursor_x, cursor_y = 0, 0

def move(x,y):
    global cursor_x, cursor_y
    cursor_x=x
    cursor_y=y
num_press = 0
kill = False

def select_region():
    global region, num_press, kill

    def press(key):
        global region, num_press, kill
        try:
            if key == keyboard.Key.esc:
                mouse_listener.stop()       # mouseのListenerを止める
                keyboard_listener.stop()
                kill = True
        except:
            pass
        try:
            
            if key.char == "z":
                num_press += 1
                if num_press == 1:
                    print(f'Start:{cursor_x},{cursor_y}')
                    region.x1, region.y1 = cursor_x, cursor_y
                elif num_press >= 2:
                    print(f'End  :{cursor_x},{cursor_y}')
                    region.x2, region.y2 = cursor_x, cursor_y
                
                    mouse_listener.stop()       # mouseのListenerを止める
                    keyboard_listener.stop()
                    region.active = True
        except:
            pass
    

    
    mouse_listener = mouse.Listener(on_move=move)
    mouse_listener.start()
    keyboard_listener = keyboard.Listener(on_press=press)
    keyboard_listener.start()    
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
    region = select_region()
    print(region.get_points())
