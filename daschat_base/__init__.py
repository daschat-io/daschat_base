# type: ignore[attr-defined]
"""Daschat base fro modules and plugins."""

from pkg_resources import DistributionNotFound, get_distribution

from daschat_base.version import VERSION

try:
    __version__ = VERSION  # get_distribution("daschat_base").version
except DistributionNotFound:
    __version__ = "(local)"

__author__ = "Daschat.io"
__email__ = "admin@daschat.io"

try:
    import cython  # type: ignore
except ImportError:
    compiled: bool = False
else:  # pragma: no cover
    try:
        compiled = cython.compiled
    except AttributeError:
        compiled = False

# __all__ = "__version__", "__author__", "__email__", "compiled"
