pkgname = "xdg-desktop-portal-cosmic"
pkgver = "1.0.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "cmake",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "libxkbcommon-devel",
    "mesa-gbm-devel",
    "pipewire-devel",
    "zstd-devel",
]
pkgdesc = "Desktop portal backend for COSMIC"
license = "GPL-3.0-or-later"
url = "https://github.com/pop-os/xdg-desktop-portal-cosmic"
source = f"{url}/archive/refs/tags/epoch-{pkgver}-beta.1.1.tar.gz"
sha256 = "3a5f15d6b3f5e64e2078ebe22c44c33e1fef55408bf3cdef8b438bed7344dc0f"


def install(self):
    self.do(
        "make",
        "install",
        f"DESTDIR={self.chroot_destdir}",
        f"CARGO_TARGET_DIR={self.chroot_srcdir}/target/{self.profile().triplet}",
    )
