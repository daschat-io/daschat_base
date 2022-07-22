VERSION = "0.15.9"


def version_info() -> str:
    import platform
    import sys
    from importlib import import_module
    from pathlib import Path

    from daschat_base import compiled

    optional_deps = []
    for p in ("pydantic", "cuid", "loguru", "fastapi"):
        try:
            import_module(p.replace("-", "_"))
        except ImportError:
            continue
        optional_deps.append(p)

    info = {
        "daschat-base version": VERSION,
        "daschat-base compiled": compiled,
        "install path": Path(__file__).resolve().parent,
        "python version": sys.version,
        "platform": platform.platform(),
        "deps. installed": optional_deps,
    }
    return "\n".join(
        "{:>30} {}".format(k + ":", str(v).replace("\n", " ")) for k, v in info.items()
    )
