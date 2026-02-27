# print("Hello")
# print("Goodbye")

def header(text, surround):
    length = len(text) + 4
    # length = 16 # 16 = 12 + 4
    # surround = "*"
    # text = "Hello, World!"
    print(surround * length)
    print(surround, text, surround)
    print(surround * length)

def main():
    header("Hello, World!", "*")
    header("Welcome to Python!", "#")
    header("Python Rocks", "!")
    header("Coders 4 EVER", "+")

main()