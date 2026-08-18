from pathlib import Path
from sebaubuntu_libs.libandroid.device_info import DeviceInfo
from twrpdtgen.device_tree import DeviceTree

orig_get_first_prop = DeviceInfo.get_first_prop

DEFAULTS = {
    "ro.product.system.device": "lake",
    "ro.product.device": "lake",
    "ro.product.system.model": "Redmi 14C",
    "ro.product.model": "Redmi 14C",
    "ro.product.system.brand": "Xiaomi",
    "ro.product.brand": "Xiaomi",
    "ro.product.system.name": "lake",
    "ro.product.name": "lake",
    "ro.product.manufacturer": "Xiaomi",
    "ro.product.system.manufacturer": "Xiaomi",
    "ro.build.version.release": "16",
    "ro.build.version.sdk": "36",
    "ro.product.cpu.abi": "arm64-v8a",
}

# Them *args và **kwargs de hung moi tham so truyen vao
def patched_get_first_prop(self, props, *args, **kwargs):
    try:
        res = orig_get_first_prop(self, props, *args, **kwargs)
        if res:
            return res
    except Exception:
        pass

    for p in props:
        if p in DEFAULTS:
            return DEFAULTS[p]
    return "lake"

DeviceInfo.get_first_prop = patched_get_first_prop

img_path = Path("vendor_boot.img")
out_path = Path("output")

dt = DeviceTree(img_path)
dt.dump(out_path)
print("--> Tao Device Tree thanh cong cho Redmi 14C (lake)!")