pkgname = "cosmic-launcher"
pkgver = "1.0.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf", "just"]
makedepends = [
    "libxkbcommon-devel",
]
depends = ["so:libEGL.so.1!mesa-egl-libs"]
pkgdesc = "Placeholder, add later"
license = "GPL-3.0-or-later"
url = "https://github.com/pop-os/cosmic-launcher"
source = f"{url}/archive/refs/tags/epoch-{pkgver}-beta.1.1.tar.gz"
sha256 = "9b11d3239238b666a560457b65de3fce0fba4d24b679b8f017ba117676ccf932"


def install(self):
    self.do(
        "just",
        f"rootdir={self.chroot_destdir}",
        f"cargo-target-dir={self.chroot_srcdir}/target/{self.profile().triplet}",
        "install",
    )
