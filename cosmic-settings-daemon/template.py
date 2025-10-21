pkgname = "cosmic-settings-daemon"
pkgver = "1.0.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "libinput-devel",
    "libpulse-devel",
    "openssl3-devel",
    "udev-devel",
    "zstd-devel",
]
depends = ["so:libEGL.so.1!mesa-egl-libs"]
pkgdesc = "Placeholder, add later"
license = "GPL-3.0-or-later"
url = "https://github.com/pop-os/cosmic-settings-daemon"
source = f"{url}/archive/refs/tags/epoch-{pkgver}-beta.1.1.tar.gz"
sha256 = "49a3557ed7696807d6f7e4688c9da2711139c358975e11b4b67bc7ac13e023bd"


def install(self):
    self.do(
        "make",
        "install",
        f"DESTDIR={self.chroot_destdir}",
        f"CARGO_TARGET_DIR={self.chroot_srcdir}/target/{self.profile().triplet}",
    )
