from functions.get_file_content import get_file_content

def test():
    tests = [
        {
            "message": "Result for 'calculator/lorem.txt' file:",
            "data": get_file_content("calculator", "lorem.txt"),
        },
        {
            "message": "Result for 'calculator/main.py' file:",
            "data": get_file_content("calculator", "main.py"),
        },
        {
            "message": "Result for 'pkg/calculator.py' file:",
            "data": get_file_content("calculator", "pkg/calculator.py"),
        },
        {
            "message": "Result for '/bin/cat':",
            "data": get_file_content("calculator", "/bin/cat"),
        },
        {
            "message": "Result for 'pkg/does_not_exist.py' file:",
            "data": get_file_content("calculator", "pkg/does_not_exist.py"),
        },
    ]

    for test in tests:
        print(test["message"])
        print(test["data"])

if __name__ == "__main__":
    test()