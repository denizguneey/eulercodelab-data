from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

ANSWER_RE = re.compile(r"answer\s*:\s*(.+)$", re.IGNORECASE)
EQUAL_RE = re.compile(r"=\s*(.+)$")


def parse_output(stdout: str) -> str:
    lines = [line.strip() for line in stdout.splitlines() if line.strip()]
    if not lines:
        return ""
    answers = []
    equals = []
    for line in lines:
        m1 = ANSWER_RE.search(line)
        if m1:
            answers.append(m1.group(1).strip())
        m2 = EQUAL_RE.search(line)
        if m2:
            equals.append(m2.group(1).strip())
    if answers:
        return answers[-1]
    if equals:
        return equals[-1]
    return lines[-1]


def solve() -> str:
    problem_id = __file__.split("Euler")[-1].split(".")[0]
    root = Path(__file__).resolve().parent.parent
    src = root / "solutionsCpp" / f"Euler{problem_id}.cpp"
    binary = root / "solutionsCpp" / f".euler{problem_id}_py_bridge"

    if not binary.exists() or src.stat().st_mtime > binary.stat().st_mtime:
        compiler = shutil.which("clang++") or shutil.which("g++")
        if not compiler:
            raise RuntimeError("No C++ compiler found (clang++/g++).")
        subprocess.check_call([compiler, "-std=c++17", "-O2", str(src), "-o", str(binary)])

    output = subprocess.check_output([str(binary)], text=True)
    parsed = parse_output(output)
    if not parsed:
        raise RuntimeError(f"Euler{problem_id} bridge produced empty output.")
    return parsed


if __name__ == "__main__":
    print(solve())
