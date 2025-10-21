pkgname = "cosmic-bg"
pkgver = "0.0.7"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "libxkbcommon-devel",
    "pkgconf",
]
pkgdesc = "COSMIC session service which applies backgrounds to displays"
license = "MPL-2.0"
url = "https://github.com/pop-os/cosmic-bg"
source = f"{url}/archive/refs/tags/epoch-1.0.0-alpha.7.tar.gz"
sha256 = "9a514472379412635a1d75325c9bb03313ed170634b841c75a65f73de62d0b1d"


def install(self):
    self.do(
        "just",
        f"rootdir={self.chroot_destdir}",
        f"cargo-target-dir={self.chroot_srcdir}/target/{self.profile().triplet}",
        "install",
    )
