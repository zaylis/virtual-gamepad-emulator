import vgamepad as vg
import time
import serial
import pydirectinput
import keyboard
import vgamepad as vg

gamepad = vg.VX360Gamepad()

def while_pressed_down(event):
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()
def while_released_down(event):
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()
keyboard.on_press_key("Down", while_pressed_down)
keyboard.on_release_key("Down", while_released_down)

def while_pressed_left(event):
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
    gamepad.update()
def while_released_left(event):
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
    gamepad.update()
keyboard.on_press_key("left", while_pressed_left)
keyboard.on_release_key("left", while_released_left)

def while_pressed_right(event):
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    gamepad.update()
def while_released_right(event):
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    gamepad.update()
keyboard.on_press_key("right", while_pressed_right)
keyboard.on_release_key("right", while_released_right)

def while_pressed_up(event):
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
    gamepad.update()
def while_released_up(event):
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
    gamepad.update()
keyboard.on_press_key("up", while_pressed_up)
keyboard.on_release_key("up", while_released_up)



def while_pressed_w(event):
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
    gamepad.update()
def while_released_w(event):
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
    gamepad.update()
keyboard.on_press_key("w", while_pressed_w)
keyboard.on_release_key("w", while_released_w)

def while_pressed_s(event):
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
    gamepad.update()
def while_released_s(event):
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
    gamepad.update()
keyboard.on_press_key("s", while_pressed_s)
keyboard.on_release_key("s", while_released_s)

def while_pressed_d(event):
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
    gamepad.update()
def while_released_d(event):
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
    gamepad.update()
keyboard.on_press_key("d", while_pressed_d)
keyboard.on_release_key("d", while_released_d)

def while_pressed_a(event):
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
    gamepad.update()
def while_released_a(event):
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
    gamepad.update()
keyboard.on_press_key("a", while_pressed_a)
keyboard.on_release_key("a", while_released_a)

if (keyboard.on_press_key("a", while_pressed_a), keyboard.on_press_key("w", while_pressed_w)):
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
else:
    (keyboard.on_release_key("a", while_pressed_a), keyboard.on_release_key("w", while_pressed_w))
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)





def while_pressed_space(event):
    gamepad.left_trigger(value=255)
    gamepad.update()
def while_released_space(event):
    gamepad.left_trigger(value=0)
    gamepad.update()
keyboard.on_press_key("space", while_pressed_space)
keyboard.on_release_key("space", while_released_space)

def while_pressed_lctrl(event):
    gamepad.right_trigger(value=255)
    gamepad.update()
def while_released_lctrl(event):
    gamepad.right_trigger(value=0)
    gamepad.update()
keyboard.on_press_key("ctrl", while_pressed_lctrl)
keyboard.on_release_key("ctrl", while_released_lctrl)

def while_pressed_q(event):
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
    gamepad.update()
def while_released_q(event):
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
    gamepad.update()
keyboard.on_press_key("q", while_pressed_q)
keyboard.on_release_key("q", while_released_q)

def while_pressed_e(event):
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
    gamepad.update()
def while_released_e(event):
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
    gamepad.update()
keyboard.on_press_key("e", while_pressed_e)
keyboard.on_release_key("e", while_released_e)

def while_pressed_tab(event):
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
    gamepad.update()
def while_released_tab(event):
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
    gamepad.update()
keyboard.on_press_key("tab", while_pressed_tab)
keyboard.on_release_key("tab", while_released_tab)

def while_pressed_enter(event):
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
    gamepad.update()
def while_released_enter(event):
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
    gamepad.update()
keyboard.on_press_key("enter", while_pressed_enter)
keyboard.on_release_key("enter", while_released_enter)

keyboard.wait("")
