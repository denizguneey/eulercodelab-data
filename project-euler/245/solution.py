from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path


def pick_compiler() -> str:
    for compiler in ("clang++", "g++"):
        if shutil.which(compiler):
            return compiler
    raise RuntimeError("No C++ compiler found (clang++/g++).")


def ensure_bridge_binary(root: Path) -> Path:
    src = root / "solutionsCpp" / "Euler245.cpp"
    bin_path = root / "solutionsCpp" / ".euler245_py_bridge"
    if (not bin_path.exists()) or (src.stat().st_mtime > bin_path.stat().st_mtime):
        compiler = pick_compiler()
        cmd = [compiler, "-std=c++17", "-O2", str(src), "-o", str(bin_path)]
        subprocess.check_call(cmd)
    return bin_path


def solve() -> str:
    root = Path(__file__).resolve().parent.parent
    binary = ensure_bridge_binary(root)
    threads = str(max(1, min(8, os.cpu_count() or 1)))
    cmd = [str(binary), "-n", "200000000000", "-t", threads, "--no-validate"]
    out = subprocess.check_output(cmd, text=True)
    lines = [line.strip() for line in out.splitlines() if line.strip()]
    if not lines:
        raise RuntimeError("Euler245 bridge produced empty output.")
    return lines[-1]


if __name__ == "__main__":
    print(solve())
