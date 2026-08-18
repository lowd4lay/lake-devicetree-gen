from pathlib import Path
import twrpdtgen.extractors.image
from twrpdtgen.device_tree import DeviceTree

# Hook hàm giải nén của twrpdtgen để bơm build.prop giả lập
old_extract = twrpdtgen.extractors.image.ImageExtractor.extract

def new_extract(self):
    old_extract(self)
    prop_file = self.ramdisk / "default.prop"
    prop_file.write_text("""
ro.product.system.device=lake
ro.product.device=lake
ro.product.system.model=Redmi 14C
ro.product.model=Redmi 14C
ro.product.system.brand=Xiaomi
ro.product.brand=Xiaomi
ro.product.system.name=lake
ro.product.name=lake
ro.product.manufacturer=Xiaomi
ro.product.system.manufacturer=Xiaomi
ro.build.version.release=16
ro.build.version.sdk=36
""")

twrpdtgen.extractors.image.ImageExtractor.extract = new_extract

# Tiến hành xuất Device Tree từ vendor_boot.img
img_path = Path("vendor_boot.img")
out_path = Path("output")

dt = DeviceTree(img_path)
dt.dump(out_path)
print("--> Tao Device Tree thanh cong cho Redmi 14C (lake)!")