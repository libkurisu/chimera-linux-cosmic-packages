pkgname = "pop-launcher"
pkgver = "1.2.7"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf", "just", "libxkbcommon-devel"]
depends = []
pkgdesc = "Modular IPC-based desktop launcher service"
license = "MPL-2.0"
url = "https://github.com/pop-os/launcher"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e02ffd9876bb11c50118bf5e9c0bec57132f7010831da749dc6107e31ca198a6"


def build(self):
    self.cargo.build(args=["--package", "pop-launcher-bin"])
    self.cargo.build()


def install(self):
    self.do(
        "just",
        f"rootdir={self.chroot_destdir}",
        f"target-dir={self.chroot_srcdir}/target/{self.profile().triplet}/release",
        "install",
    )
