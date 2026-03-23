with open("sorting.py", "w") as file:
    code = file.read()
    print(code)

file=open("pop.py", "w")
file.close()

file=open("fun.py", "w")
file.write("def fun():\n    print('Hello, World!')")

file=open("pop2.py","w")
file.write("def fun():")
file.write("\n    print('Hello, World!')")
file.close()


file=open("base.html","x")
file.close()

with open("index.html","w") as file:
    file.write("<html>\n")
    file.write("<head>\n")
    file.write("<title>My Website</title>\n")
    file.write("</head>\n")
    file.write("<body>\n")
    file.write("<h1>Welcome to My Website</h1>\n")
    file.write("<p>This is a sample HTML template.</p>\n")
    file.write("</body>\n")
    file.write("</html>")
    
    