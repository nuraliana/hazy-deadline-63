import os
from pathlib import Path

LINE = "I set my status to delivered, filed the completion report, and congratulated myself on finishing early — I just never actually started the task."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        out_path = Path(out_dir) / "entry.txt"
    else:
        out_path = Path(__file__).resolve().parent / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(LINE, encoding="utf-8")

if __name__ == "__main__":
    main()
