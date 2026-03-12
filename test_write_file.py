from functions.write_file import write_file

def test():
    tests = [
        {
            "message": "Result for writing to 'calculator/lorem.txt' file:",
            "data": write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
        },
        {
            "message": "Result for writing to 'pkg/morelorem.txt' file:",
            "data": write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
        },
        {
            "message": "Result for writing to '/tmp/temp.txt' file:",
            "data": write_file("calculator", "/tmp/temp.txt", "this should not be allowed"),
        },
    ]

    for test in tests:
        print(test["message"])
        print(test["data"])

if __name__ == "__main__":
    test()