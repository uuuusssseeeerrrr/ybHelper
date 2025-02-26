import keyboard
import time
import threading
import win32api, win32con

h = None
healKeys, honKeys, healDelay, honDelay = '', '', '', ''
keys = (win32con.VK_NUMPAD0, win32con.VK_NUMPAD1, win32con.VK_NUMPAD2, win32con.VK_NUMPAD3, win32con.VK_NUMPAD4, 
        win32con.VK_NUMPAD5, win32con.VK_NUMPAD6, win32con.VK_NUMPAD7, win32con.VK_NUMPAD8, win32con.VK_NUMPAD9)

class readThread(threading.Thread):
    def __init__(self):
        super(readThread, self).__init__()  # parent class __init__ 실행
        self.daemon = True  # 데몬쓰레드로 설정
        self.stop_flag = threading.Event()
        
    def run(self):  # run method override
        print('Hooking Started')
        while not self.stop_flag.is_set():
            exec()
    def stop(self):
        self.stop_flag.set()

def eventListener(e):
    global h

    if(e.name == 'f2'):
        if h is None or not h.is_alive():
            h = readThread()  # 새 인스턴스 생성
            h.start()
    elif(e.name == 'f4'):
        if h is not None and h.is_alive():
            print('Hooking Stoped')
            h.stop()
            h.join()
            h = None

def exec():
    for i in range(1,3):
        heal()
        time.sleep(healDelay / 1000)
    pushKey(win32con.VK_ESCAPE)
    for i in range(1,4):
        hon()
    time.sleep(0.002)
    pushKey(win32con.VK_TAB)
    time.sleep(0.002)
    pushKey(win32con.VK_TAB)

def pushKey(key):
    win32api.keybd_event(key, 0, 0, 0)

def heal():
    win32api.keybd_event(keys[healKeys], 0, 0, 0)

def hon():
    win32api.keybd_event(keys[honKeys], 0, 0, 0)
    time.sleep(honDelay / 1000)
    win32api.keybd_event(win32con.VK_UP, 0, 0, 0)
    time.sleep(honDelay / 1000)
    win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)
