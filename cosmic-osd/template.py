pkgname = "cosmic-osd"
pkgver = "1.0.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "just",
    "pkgconf",
]
makedepends = [
    "libinput-devel",
    "libxkbcommon-devel",
    "pipewire-devel",
    "udev-devel",
]
depends = []
pkgdesc = "COSMIC on screen display"
license = "GPL-3.0-or-later"
url = "https://github.com/pop-os/cosmic-osd"
source = f"{url}/archive/refs/tags/epoch-{pkgver}-beta.1.1.tar.gz"
sha256 = "108479a1c1bf30cc54aacd9daca041bc24b720e39aa66ed2a5d6a9d1919215c4"


def install(self):
    self.do(
        "make",
        "install",
        f"DESTDIR={self.chroot_destdir}",
        f"CARGO_TARGET_DIR={self.chroot_srcdir}/target/{self.profile().triplet}",
    )
