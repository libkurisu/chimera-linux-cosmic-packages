pkgname = "cosmic-randr"
pkgver = "1.0.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "glib-devel",
    "just",
    "pkgconf",
]
pkgdesc = "Utility for displaying and configuring Wayland outputs"
license = "MPL-2.0"
url = "https://github.com/pop-os/cosmic-randr"
source = f"{url}/archive/refs/tags/epoch-{pkgver}-beta.1.1.tar.gz"
sha256 = "0b39233b16d9e9e427149f6d28bd4f80bdf41a19dfa6086c7afb17f7af9f94b8"


def install(self):
    self.do(
        "just",
        f"rootdir={self.chroot_destdir}",
        f"cargo-target-dir={self.chroot_srcdir}/target/{self.profile().triplet}",
        "install",
    )
