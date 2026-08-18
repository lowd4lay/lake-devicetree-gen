from pathlib import Path
from sebaubuntu_libs.libandroid.device_info import DeviceInfo
from twrpdtgen.device_tree import DeviceTree

orig_get_first_prop = DeviceInfo.get_first_prop

# Fingerprint chuan dinh dang Android de bypass thu vien kiem tra
FAKE_FINGERPRINT = "Xiaomi/lake/lake:16/AP2A.240805.005/V3.0.1.0:user/release-keys"

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
    "ro.build.fingerprint": FAKE_FINGERPRINT,
    "ro.system.build.fingerprint": FAKE_FINGERPRINT,
    "ro.bootimage.build.fingerprint": FAKE_FINGERPRINT,
    "ro.build.description": "lake-user 16 AP2A.240805.005 release-keys",
    "ro.build.display.id": "HyperOS 3.0.1.0",
    "ro.build.date.utc": "1735689600",
}

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

    # Kiem tra neu dang truy van thuoc tinh fingerprint
    if any("fingerprint" in str(p).lower() for p in props):
        return FAKE_FINGERPRINT

    return "lake"

DeviceInfo.get_first_prop = patched_get_first_prop

img_path = Path("vendor_boot.img")
out_path = Path("output")

dt = DeviceTree(img_path)
dt.dump(out_path)
print("--> Tao Device Tree thanh cong cho Redmi 14C (lake)!")