from setuptools import setup, find_packages
import sys
from img_fit import __version__

data_files = []
if sys.platform == "win32":
    data_files = [('scripts',["scripts/img.exe"])]

setup(
    name = "imgfit",
    version = __version__,
    packages = find_packages(),
    install_requires = ["pillow >= 8", "matplotlib >= 3.4", "PyLaTeXenc >= 2"],
    python_requires = ">=3",
    author = "xystudio",
    author_email = "173288240@qq.com",
    description = "Change your images.",
    long_description = open("README.md",encoding="utf-8").read(),
    license = "MIT",
    url = "https://github.com/xystudio889/imgfit",
    data_files = data_files,
    include_package_data = True
)
