pkgname = "cosmic-applibrary"
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
url = "https://github.com/pop-os/cosmic-applibrary"
source = f"{url}/archive/refs/tags/epoch-{pkgver}-beta.1.1.tar.gz"
sha256 = "70ac9f2fe3fca8ab7188a3c1cdca6b1c20d198d888bf6f50093d962e7cab4ad7"


def install(self):
    self.do(
        "just",
        f"rootdir={self.chroot_destdir}",
        f"cargo-target-dir={self.chroot_srcdir}/target/{self.profile().triplet}",
        "install",
    )
