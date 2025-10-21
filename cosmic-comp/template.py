pkgname = "cosmic-comp"
pkgver = "1.0.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf", "pixman-devel"]
makedepends = [
    "gmake",
    "libdisplay-info-devel",
    "libinput-devel",
    "libinput-devel",
    "libseat-devel",
    "libxkbcommon-devel",
    "mesa-gbm-devel",
    "pipewire-devel",
    "pixman-devel",
    "udev-devel",
]
depends = ["so:libEGL.so.1!mesa-egl-libs"]
pkgdesc = "Placeholder, add later"
license = "GPL-3.0-or-later"
url = "https://github.com/pop-os/cosmic-comp"
source = f"{url}/archive/refs/tags/epoch-{pkgver}-beta.1.1.tar.gz"
sha256 = "3ba4f6d94f6c0717ebbefd6c888c0e0a43038cdc02414d6cc51f9a4d7014c1c2"


def install(self):
    self.do(
        "make",
        "install",
        f"DESTDIR={self.chroot_destdir}",
        f"CARGO_TARGET_DIR={self.chroot_srcdir}/target/{self.profile().triplet}",
    )
