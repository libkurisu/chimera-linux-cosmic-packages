pkgname = "cosmic-just"
pkgver = "1.0.0"
pkgrel = 0
build_style = "cargo"
make_check_args = ["--", "--skip", "completions::bash"]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["just", "rust-std"]
checkdepends = ["python", "bash"]
depends = []
pkgdesc = "Placeholder, add later"
license = "GPL-3.0-or-later"
url = "https://github.com/pop-os/just"
source = f"{url}/archive/refs/heads/master.zip"
sha256 = "c03f758ad3ba8f2ec570fbf6c0821c6c526a49bd44e11f55f02268b2b68ecdff"


def post_build(self):
    for shell in []:
        with open(self.cwd / f"just.{shell}", "w") as f:
            self.do(
                f"./target/{self.profile().triplet}/release/just",
                "--completions",
                shell,
                stdout=f,
            )
    with open(self.cwd / "just.1", "w") as f:
        self.do(
            f"./target/{self.profile().triplet}/release/just",
            "--man",
            stdout=f,
        )


def post_install(self):
    self.install_man("just.1")
    for shell in []:
        self.install_completion(f"just.{shell}", shell)
