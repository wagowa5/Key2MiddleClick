from pynput import keyboard
import ctypes
import time

# Windows mouse_event flags
MOUSEEVENTF_MIDDLEDOWN = 0x0020
MOUSEEVENTF_MIDDLEUP = 0x0040

last_click_time = 0


def middle_click():
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_MIDDLEDOWN, 0, 0, 0, 0)
    time.sleep(0.03)
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_MIDDLEUP, 0, 0, 0, 0)


def on_press(key):
    global last_click_time

    print("pressed:", key)

    # Menuキー / アプリケーションキー
    # Windowsの仮想キーコードは 93
    vk = getattr(key, "vk", None)

    if key == keyboard.Key.menu or vk == 93:
        now = time.time()

        # 押しっぱなし連打防止
        if now - last_click_time > 0.2:
            print("Menuキー検出 → ミドルクリック")
            middle_click()
            last_click_time = now


with keyboard.Listener(on_press=on_press) as listener:
    print("起動しました。Menuキーを押すとミドルクリックします。終了は Ctrl+C")
    listener.join()
