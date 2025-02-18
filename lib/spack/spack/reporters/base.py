# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from typing import Any, Dict, List


class Reporter:
    """Base class for report writers."""

    def build_report(self, filename: str, specs: List[Dict[str, Any]]):
        raise NotImplementedError("must be implemented by derived classes")

    def test_report(self, filename: str, specs: List[Dict[str, Any]]):
        raise NotImplementedError("must be implemented by derived classes")

    def concretization_report(self, filename: str, msg: str):
        raise NotImplementedError("must be implemented by derived classes")
