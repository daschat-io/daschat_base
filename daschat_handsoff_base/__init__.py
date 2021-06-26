# type: ignore[attr-defined]
"""Daschat handsoff plugin base."""

from pkg_resources import DistributionNotFound, get_distribution

try:
    __version__ = get_distribution("daschat_handsoff_base").version
except DistributionNotFound:
    __version__ = "(local)"

__author__ = "Daschat.io"
__email__ = "admin@daschat.io"
