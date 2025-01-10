with open("sample.txt", "w") as file:
    file.write("This is the first line of random text.\n")
    file.write("Here is the second line of random text.\n")
    file.write("Finally, this is the third line of random text.\n")

with open("sample.txt", "r") as file:
    content = file.read()

print("\nContents of the file:")
print(content)
