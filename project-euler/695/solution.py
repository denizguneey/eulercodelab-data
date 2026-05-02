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
    answer_like = []
    answers = []
    equals = []
    for line in lines:
        lower = line.lower()
        if "answer" in lower:
            if ":" in line:
                answer_like.append(line.rsplit(":", 1)[1].strip())
            elif "=" in line:
                answer_like.append(line.rsplit("=", 1)[1].strip())
        m1 = ANSWER_RE.search(line)
        if m1:
            answers.append(m1.group(1).strip())
        m2 = EQUAL_RE.search(line)
        if m2:
            equals.append(m2.group(1).strip())
    if answer_like:
        return answer_like[-1]
    if answers:
        return answers[-1]
    if equals:
        return equals[-1]
    if ":" in lines[-1]:
        tail = lines[-1].rsplit(":", 1)[1].strip()
        if tail:
            return tail
    return lines[-1]


def should_skip_cpp_checkpoints(src: Path) -> bool:
    try:
        text = src.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return False
    return "--skip-checkpoints" in text


def run_cpp(binary: Path, src: Path, root: Path) -> str:
    cmd = [str(binary)]
    if should_skip_cpp_checkpoints(src):
        cmd.append("--skip-checkpoints")

    try:
        return subprocess.check_output(cmd, text=True, cwd=root)
    except subprocess.CalledProcessError:
        return subprocess.check_output(cmd, text=True, cwd=src.parent)


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

    output = run_cpp(binary=binary, src=src, root=root)
    parsed = parse_output(output)
    if not parsed:
        raise RuntimeError(f"Euler{problem_id} bridge produced empty output.")
    return parsed


if __name__ == "__main__":
    print(solve())
