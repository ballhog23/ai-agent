from functions.run_python_file import run_python_file

def test():
    tests = [
        {
            "message": "should print the calculator's usage instructions:",
            "data": run_python_file("calculator", "main.py"),
        },
        {
            "message": "should run the calculator... which gives a kinda nasty rendered result:",
            "data": run_python_file("calculator", "main.py", ["3 + 5"]),
        },
        {
            "message": "should run the calculator's tests successfully:",
            "data": run_python_file("calculator", "tests.py"),
        },
        {
            "message": "this should return an error:",
            "data": run_python_file("calculator", "../main.py"),
        },
        {
            "message": "this should return an error:",
            "data": run_python_file("calculator", "nonexistent.py"),
        },
        {
            "message": "this should return an error:",
            "data": run_python_file("calculator", "lorem.txt"),
        },
    ]

    for test in tests:
        print(test["message"])
        print(test["data"])

if __name__ == "__main__":
    test()