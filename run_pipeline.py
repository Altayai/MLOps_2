#!/usr/bin/env python3
import subprocess
import sys
import argparse

def run(cmd):
    print(">>>", " ".join(cmd))
    subprocess.check_call(cmd)

def main():
    parser = argparse.ArgumentParser(description="Run DVC pipeline or a stage.")
    parser.add_argument("-s", "--stage", help="run a specific dvc stage name (e.g. ingest, train)")
    parser.add_argument("--pull", action="store_true", help="run 'dvc pull' before repro")
    args = parser.parse_args()

    try:
        if args.pull:
            run(["dvc", "pull"])
        if args.stage:
            run(["dvc", "repro", args.stage])
        else:
            run(["dvc", "repro"])
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Command failed with exit code {e.returncode}")
        sys.exit(e.returncode)

if __name__ == "__main__":
    main()
