"""Entry point for ``python -m reduce``."""

from __future__ import annotations

import sys

from reduce.cli import main

if __name__ == "__main__":
    sys.exit(main())
