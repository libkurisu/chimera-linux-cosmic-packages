pkgname = "cosmic-icons"
pkgver = "1.0.0"
pkgrel = 0
makedepends = ["just"]
pkgdesc = "COSMIC session service which applies backgrounds to displays"
license = "CC-BY-SA-4.0"
url = "https://github.com/pop-os/cosmic-icons"
source = f"{url}/archive/refs/tags/epoch-{pkgver}-beta.1.1.tar.gz"
sha256 = "8b34b0a850043fcebb09959d746bb305f73a7ca71cae76edff5c9aaa83ff1c4c"
# def build(self):
#     print("test")
#     #testing
tools = {
    "xargs": "findutils",
}


def install(self):
    # targeting the base dir instead of rootdir cause I think the just file is trying to sanitize it
    self.do("just", f"rootdir={self.chroot_destdir}", "install")
