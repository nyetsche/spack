# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class Libmolgrid(CMakePackage):
    """libmolgrid is a library to generate tensors from molecular data, with properties
    that make its output particularly suited to machine learning."""

    homepage = "https://gnina.github.io/libmolgrid/"
    url = "https://github.com/gnina/libmolgrid/archive/refs/tags/v0.5.2.tar.gz"

    maintainers("RMeli")

    license("Apache-2.0")

    version("0.5.5", sha256="fe038d4c5fe96d73eadbe433cfd13c109446e8fd0af8d8739394966ea57afecd")
    version("0.5.4", sha256="2eea846acd6c0d75cefaac3217fcafe56656fc38ba100f8b387e13078cea4ff2")
    version("0.5.3", sha256="a9f7a62cdeb516bc62a06b324cdd33b095a787df175c6166d74a8d30b6916abb")
    version("0.5.2", sha256="e732d13a96c2f374d57a73999119bef700172d392c195c751214aa6ac6680c3a")

    depends_on("cxx", type="build")  # generated

    depends_on("zlib-api")
    depends_on("boost +regex +test +program_options +system +filesystem +iostreams +python")
    depends_on("openbabel@3:~gui~cairo")
    depends_on("cuda@11:")
    depends_on("cuda@12:", when="@0.5.5:")

    depends_on("python")
    depends_on("py-numpy")
    depends_on("py-pytest")

    def cmake_args(self):
        ob_incl = os.path.join(self.spec["openbabel"].prefix.include, "openbabel3")
        ob_libs = self.spec["openbabel"].libs.joined(";")

        return ["-DOPENBABEL3_INCLUDE_DIR=" + ob_incl, "-DOPENBABEL3_LIBRARIES=" + ob_libs]
