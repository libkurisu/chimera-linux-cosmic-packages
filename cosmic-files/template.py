pkgname = "cosmic-files"
pkgver = "1.0.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "glib-devel",
    "just",
    "libxkbcommon-devel",
    "pkgconf",
    "zstd-devel",
]
pkgdesc = "COSMIC session service which applies backgrounds to displays"
license = "MPL-2.0"
url = "https://github.com/pop-os/cosmic-files"
source = f"{url}/archive/refs/tags/epoch-{pkgver}-beta.1.1.tar.gz"
sha256 = "96fdf51baa63824cfa2dd4b1d2410290385cb60f8338eab2d58654da5be7f2c3"


def build(self):
    self.cargo.build(args=["--package", "cosmic-files-applet"])
    self.cargo.build()


def install(self):
    self.do(
        "just",
        f"rootdir={self.chroot_destdir}",
        f"cargo-target-dir={self.chroot_srcdir}/target/{self.profile().triplet}",
        "install",
    )
