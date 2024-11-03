import pyvjoy
import atexit

j0 = pyvjoy.VJoyDevice(1)
j1 = pyvjoy.VJoyDevice(2)

def reset(device):
    device.set_axis(pyvjoy.HID_USAGE_X, 0x4000)
    device.set_axis(pyvjoy.HID_USAGE_Y, 0x4000)
    device.set_axis(pyvjoy.HID_USAGE_Z, 0x4000)
    device.set_axis(pyvjoy.HID_USAGE_RX, 0x4000)
    device.set_axis(pyvjoy.HID_USAGE_RY, 0x4000)
    device.set_axis(pyvjoy.HID_USAGE_RZ, 0x4000)
    device.set_axis(pyvjoy.HID_USAGE_SL0, 0x0)
    device.set_axis(pyvjoy.HID_USAGE_SL1, 0x0)

def reset_all_devices():
    reset(j0)
    reset(j1)

reset_all_devices()

atexit.register(reset_all_devices)

while True:
    j0.set_axis(pyvjoy.HID_USAGE_X, 0x8000)
    j1.set_axis(pyvjoy.HID_USAGE_X, 0x0)
