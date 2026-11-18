texto = input("File name: ").strip().lower() 
if texto.endswith(".gif"):
    print ("image/gif")
elif texto.endswith(".jpg") or texto.endswith(".jpeg"):
    print ("image/gif")
elif texto.endswith(".png"):
    print ("image/png")
elif texto.endswith(".pdf"):
    print ("application/pdf")
elif texto.endswith(".txt"):
    print ("text/plain")
elif texto.endswith(".zip"):
    print ("application/zip")
else:
    print ("application/octet-stream")