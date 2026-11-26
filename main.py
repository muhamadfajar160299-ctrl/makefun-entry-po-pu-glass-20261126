import os

# Output directory is taken from MAKEFUN_OUTPUT_DIR.
TEXT = "I gave the glass five seconds to vacate my sunbeam, and it chose the floor, so legally this is its own decision."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
