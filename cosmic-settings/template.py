pkgname = "cosmic-settings"
pkgver = "1.0.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "just",
    "libinput-devel",
    "libxkbcommon-devel",
    "pipewire-devel",
    "pkgconf",
    "udev-devel",
]
pkgdesc = "Settings application for the COSMIC desktop"
license = "MPL-2.0"
url = "https://github.com/pop-os/cosmic-settings"
source = f"{url}/archive/refs/tags/epoch-{pkgver}-beta.1.1.tar.gz"
sha256 = "d66ab851496c48c1f3eacd35a57f561111ef86b073a9ddeb8f78408a83946d51"


def install(self):
    self.do(
        "just",
        f"rootdir={self.chroot_destdir}",
        f"cargo-target-dir={self.chroot_srcdir}/target/{self.profile().triplet}",
        "install",
    )
