# GIT PACKAGE, FIX LATER
pkgname = "cosmic-session"
pkgver = "1.0.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["cosmic-just"]
depends = ["so:libEGL.so.1!mesa-egl-libs"]
pkgdesc = "Placeholder, add later"
license = "GPL-3.0-or-later"
url = "https://github.com/pop-os/cosmic-session"
source = f"{url}/archive/refs/tags/epoch-{pkgver}-beta.1.1.tar.gz"
sha256 = "74072f8c75548256582c7a615798569ff7095c6b6e026aa82bd5e141ecacbb0c"


def install(self):
    self.do(
        "just",
        f"rootdir={self.chroot_destdir}",
        f"cargo-target-dir={self.chroot_srcdir}/target/{self.profile().triplet}",
        "install",
    )
