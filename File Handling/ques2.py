file = open("certificate.txt", "r")
content = file.read()
content = content.lower()

if "live" in content:
    print("The certificate has the word live in it.")
else:
    print("No, it doesn't have the word live in it.")
