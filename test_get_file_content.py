from functions.get_file_content import get_file_content

def test():
    tests = [
        {
            "message": "Result for current directory:",
            "data": get_file_content("calculator", "main.py"),
        },
        {
            "message": "Result for 'pkg' directory:",
            "data": get_file_content("calculator", "pkg/calculator.py"),
        },
        {
            "message": "Result for '/bin' directory:",
            "data": get_file_content("calculator", "/bin/cat"),
        },
        {
            "message": "Result for '../' directory:",
            "data": get_file_content("calculator", "pkg/does_not_exist.py"),
        },
    ]

    for test in tests:
        print(test["message"])
        print(test["data"])

if __name__ == "__main__":
    test()