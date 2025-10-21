pkgname = "cosmic-store"
pkgver = "1.0.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "just",
    "pkgconf",
]
makedepends = [
    "appstream-devel",
    "flatpak-devel",
    "glib-devel",
    "libxkbcommon-devel",
    "openssl3-devel",
]
depends = ["flatpak"]
pkgdesc = "COSMIC software manager"
license = "GPL-3.0-or-later"
url = "https://github.com/pop-os/cosmic-store"
source = f"{url}/archive/refs/tags/epoch-{pkgver}-beta.2.tar.gz"
sha256 = "e2e266cce68cd9659049f30b84cfd9af638b17d96850e6c5db39e5a2df0c77bb"


def install(self):
    self.do(
        "just",
        f"rootdir={self.chroot_destdir}",
        f"cargo-target-dir={self.chroot_srcdir}/target/{self.profile().triplet}",
        "install",
    )
