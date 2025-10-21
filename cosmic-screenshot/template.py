pkgname = "cosmic-screenshot"
pkgver = "1.0.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "just",
    "libxkbcommon-devel",
    "pkgconf",
]
pkgdesc = "COSMIC screenshot utility"
license = "MPL-2.0"
url = "https://github.com/pop-os/cosmic-screenshot"
source = f"{url}/archive/refs/tags/epoch-1.0.0-alpha.7.tar.gz"
sha256 = "0fd467bd94e0e3537e6833ec9068b84f4f1453510a2599cc69a61d014dc6e873"


def install(self):
    self.do(
        "just",
        f"rootdir={self.chroot_destdir}",
        f"cargo-target-dir={self.chroot_srcdir}/target/{self.profile().triplet}",
        "install",
    )
