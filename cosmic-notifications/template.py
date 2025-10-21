pkgname = "cosmic-notifications"
pkgver = "1.0.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "glib-devel",
    "libxkbcommon-devel",
    "pkgconf",
    "zstd-devel",
]
makedepends = ["just"]
pkgdesc = "COSMIC session service which applies backgrounds to displays"
license = "CC-BY-SA-4.0"
url = "https://github.com/pop-os/cosmic-notifications"
source = f"{url}/archive/refs/tags/epoch-{pkgver}-beta.1.1.tar.gz"
sha256 = "010457c0ff82b074d508a28ab005969e4080f05087e28c05f30425bc79ca7060"


def install(self):
    self.do(
        "just",
        f"rootdir={self.chroot_destdir}",
        f"cargo-target-dir={self.chroot_srcdir}/target/{self.profile().triplet}",
        "install",
    )
