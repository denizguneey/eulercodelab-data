def solve():
    words = [
        "affine", "plane",
        "radically", "integral", "local", "field",
        "open", "oriented", "line", "section",
        "jacobian",
        "orthogonal", "kernel", "embedding"
    ]
    ans = "".join(w[0].lower() for w in words)
    return ans

if __name__ == "__main__":
    print(solve())
