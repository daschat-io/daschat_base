# type: ignore[attr-defined]
"""Daschat base fro modules and plugins."""

from pkg_resources import DistributionNotFound, get_distribution

try:
    __version__ = get_distribution("daschat_base").version
except DistributionNotFound:
    __version__ = "(local)"

__author__ = "Daschat.io"
__email__ = "admin@daschat.io"
