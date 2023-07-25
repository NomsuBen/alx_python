import importlib

def main():
    module_name = "variable_load_2"
    module = importlib.import_module(module_name)

    if hasattr(module, "a"):
        a_value = getattr(module, "a")
        print(f"The value of 'a' is: {a_value}")
    else:
        print("Variable 'a' not found in the imported module.")

if __name__ == "__main__":
    main()
