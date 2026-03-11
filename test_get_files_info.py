from functions.get_files_info import get_files_info

def test():
    tests = [
        {
            "message": "Result for current directory:",
            "data": get_files_info("calculator", "."),
        },
        {
            "message": "Result for 'pkg' directory:",
            "data": get_files_info("calculator", "pkg"),
        },
        {
            "message": "Result for '/bin' directory:",
            "data": get_files_info("calculator", "/bin"),
        },
        {
            "message": "Result for '../' directory:",
            "data": get_files_info("calculator", "../"),
        },
    ]

    for test in tests:
        print(test["message"])
        print(test["data"])

if __name__ == "__main__":
    test()