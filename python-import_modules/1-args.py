import sys

def main():
    num_args = len(sys.argv) - 1
    args = sys.argv[1:]

    if num_args == 0:
        print("0 arguments.")
        return

    print(f"{num_args} argument{'s' if num_args > 1 else ''}:")
    for i, arg in enumerate(args, 1):
        print(f"{i}: {arg}")

if __name__ == "__main__":
    main()
