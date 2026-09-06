"""Validate the Mach-O fixture with pinned macholib."""

from macholib.MachO import MachO
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
obj = MachO(str(ROOT / "tests/fixtures/sample.macho"))
assert len(obj.headers) == 1
print("sample-macho: macholib parsed one Mach-O header")
