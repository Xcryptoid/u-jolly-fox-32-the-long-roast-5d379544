import os
import shutil

# This little script only moves the finished line from the repo into the
# folder the grader reads. It does not touch the wording, so the roast
# that gets judged is exactly the one saved in entry.txt.


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    shutil.copyfile(src, os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
