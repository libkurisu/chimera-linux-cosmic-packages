# This will serve as a reference for packaging other COSMIC software.
pkgname = "cosmic-workspaces-epoch"
pkgver = "1.0.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "just",
    "pkgconf",
]  # Things that should be installed on the host machine for building.
makedepends = [
    "libinput-devel",
    "libxkbcommon-devel",
    "mesa-gbm-devel",
    "udev-devel",
]  # Things that are required to build a package.
depends = []  # Things that have to be installed on target machine for the program to work properly.
pkgdesc = "COSMIC workspaces epoch"
license = "GPL-3.0-or-later"  # Cosmic uses GPL or MPL for just about everything, so double check that this is correct
url = "https://github.com/pop-os/cosmic-workspaces-epoch"  # align with pkgname or use pkgname variable if possible
source = f"{url}/archive/refs/tags/epoch-{pkgver}-beta.1.1.tar.gz"
sha256 = "3588c8f4dad6211c41ab6c5cd8017a224042532128fcf9f9f9815a201952f1b4"  # DELETE AND THEN RUN ./cbuild prepare-upgrade user/blahblahblah


def install(self):
    self.do(
        "make",
        "install",
        f"DESTDIR={self.chroot_destdir}",
        f"CARGO_TARGET_DIR={self.chroot_srcdir}/target/{self.profile().triplet}",
    )


# This will either use this varient here for make files or it will use just as shown below
# self.do(
#         "just",
#         f"rootdir={self.chroot_destdir}",
#         f"cargo-target-dir={self.chroot_srcdir}/target/{self.profile().triplet}",
#         "install",
#     )
