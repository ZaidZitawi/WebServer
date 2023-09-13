from socket import *

serverPort=12345 #Server port number to 7788
serverSocket=socket(AF_INET,SOCK_STREAM) #creating a socket
serverSocket.bind(("192.168.1.9",serverPort)) #put server port number  with the socket
serverSocket.listen(1) #lesten for one queued connection
print("The web server is ready to receive") 
while True:
    connectionSocket, addr = serverSocket.accept()
    ip=addr[0]
    port=addr[1]
    print(f"Tcp connection from {addr} has been established : ")
    # Receive the HTTP request headers
    data = b""
    while True:
        chunk = connectionSocket.recv(1024)
        if not chunk:
            break
        data += chunk
        if b"\r\n\r\n" in data:
            break
    header_end = data.index(b"\r\n\r\n")
    header_bytes = data[:header_end + 4]
    header = header_bytes.decode("utf-8")
    print(addr)
    print(header)
    object = header.split()[1]  # Extract the requested object from the header
    print(f"The HTTP request is: {object}")
    if (object == '/' or object == '/index.html' or object == '/main_en.html' or object == '/en'):#check the domain 
        # requist
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode()) # if true,it sends an HTTP response with a "200 OK" status code and the  HTML file.
        connectionSocket.send("Content-Type: text/html \r\n".encode()) # send the HTML file: the content type "text/html"
        connectionSocket.send("\r\n".encode())
        
        file1=open("main_en.html", "rb") # server send main_en.html file, header,html, footer.html
        headerfile=open("header.html", "rb")
        footerfile=open("footer.html", "rb")


        connectionSocket.send(headerfile.read()) # read the file 
        connectionSocket.send(file1.read()) 
        connectionSocket.send(footerfile.read())

    elif (object == '/ar'): #check the domain
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        file2=open("main_ar.html", "rb") #if true send html file main_ar.html(Arabic Version)
        ar_header=open("headerar.html", "rb")
        ar_footer=open("footerar.html", "rb")
        connectionSocket.send(ar_header.read()) # Read Files Respectivlt
        connectionSocket.send(file2.read())
        connectionSocket.send(ar_footer.read())

        #when the object requested by the client is either an HTML file or a CSS file. then send the dothtml.html file or stylesheet.html(depends on the two
        # condition statment below )
    elif (object.endswith('.html')):
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        file3=open("dothtml.html", "rb")
        connectionSocket.send(file3.read())

    elif (object.endswith('.css')):
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: text/css \r\n".encode())
        connectionSocket.send("\r\n".encode())
        cssfile= open("stylesheet.css", "rb")
        connectionSocket.send(cssfile.read())
    
    #when the object requested by the client is laptop.csv when clicking the link in main_en.html then the csv file is downloaded 
    # as an excell spread sheet with 10 random laptops names and their prices.
    elif (object == '/laptop.csv'):
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: text/csv \r\n".encode())
        connectionSocket.send("\r\n".encode())
        laptop=open("laptop.csv", "rb")
        connectionSocket.send(laptop.read())
    
    #when the object requested by the client is /SortByName it responces with an html file called SortByName.html which contains 10 random laptops names and their prices.
    elif (object == '/SortByName'): 
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        laptopSBN=open("SortByName.html", "rb")
        connectionSocket.send(laptopSBN.read())

    elif (object == '/SortByPrice'): 
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        laptopSBP=open("SortByPrice.html", "rb")
        connectionSocket.send(laptopSBP.read())


    elif (object.endswith('.png')): # files with the extensions '.png' and '.jpg'.
        # If the requested object (which is the name of the file being requested by the client) ends with '.png',
        # the server sends an HTTP response with a 200 OK status and a content type of "image/png".
        # It then opens the file "pngImage.png" and sends it to the client.
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: image/png \r\n".encode())
        connectionSocket.send("\r\n".encode())
        png = open("images/png.png", "rb")
        connectionSocket.send(png.read())

    elif (object.endswith('.jpg')):#The same process occurs for '.jpg' files,
        # with the file "jpgImage.jpg" being sent to the client with a content type of "image/jpeg".
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: image/jpeg \r\n".encode())
        connectionSocket.send("\r\n".encode())
        jpg= open("images/jpg.jpg", "rb") #open the image with jpg extension.
        connectionSocket.send(jpg.read())

    elif (object == '/azn'): #status code 307 Temporary Redirect: If the request is for '/go',
        # the server sends a 307 Temporary Redirect HTTP response to the client with
        # the Location header set to GOOGLE
        # This instructs the client to make a new request to the specified URL.
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("Location: https://www.amazon.com \r\n".encode())
        connectionSocket.send("\r\n".encode())

    elif (object == '/so'): #Similarly, if the request is for '/so', the server sends a 307 Temporary Redirect
        # HTTP response with the Location header set to 'https://stackoverflow.com',
        # instructing the client to make a new request to Stack Overflow.
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("Location: https://stackoverflow.com \r\n".encode())
        connectionSocket.send("\r\n".encode())

    elif (object == '/bzu'):#HTTP request that includes the string "/bzu" in the URL. If this string is present.
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode()) #HTTP response to the client with a "307 Temporary Redirect" status code
        # and a "Location" header specifying that
        # the client should be redirected to the URL "https://www.birzeit.edu/en".This will cause the client's web browser to send a new request to the specified URL.
        connectionSocket.send("Content-Type: text/html \r\n".encode())#The response also includes a "Content-Type" header with a value of "text/html",
        # which indicates that the body of the response contains HTML content.
        connectionSocket.send("Location: https://www.birzeit.edu/en \r\n".encode())# HTTP response with the Location header set to birzeit edu
        connectionSocket.send("\r\n".encode())



    else: #scenario where a requested resource is not found by a client.
        connectionSocket.send("HTTP/1.1 404 Not Found \r\n".encode())#in this case, the server sends a 404 Not Found HTTP response to the client
        connectionSocket.send("Content-Type: text/html \r\n".encode()) #type text HTML
        connectionSocket.send("\r\n".encode()) #HTML document containing a message indicating that the requested resource was not found
        #includes information about our team's names and IDs ALSO IP and port of the server.
        notFoundHtmlString = "<html>"\
                    "<head>"\
                    "<meta charset='UTF-8'>"\
                    "<title> 404 - Requested File Not Found </title>"\
                    "</head>"\
                    "<body style='background-color: #f7f7f7;'>"\
                    "<div style='text-align: center; margin-top: 100px;'>"\
                    "<h1 style='font-family: Arial, sans-serif; color: #333;'>Oops! Error 404</h1>"\
                    "<p style='font-family: Verdana, sans-serif; font-size: 18px; color: #666;'>The requested File could not be found on the server.</p>"\
                    "<hr style='border: 1px dashed #aaa; width: 50%;'>"\
                    "<p style='font-family: Helvetica, sans-serif; font-size: 14px; color: #888;'>Please check the URL or contact the website administrator for assistance.</p>"\
                    "<p style='font-family: 'Trebuchet MS', sans-serif; font-size: 14px; color: #555; margin-top: 20px;'>Team:</p>"\
                    "<ul style='font-family: 'Trebuchet MS', sans-serif; font-size: 14px; color: #555; list-style-type: square;'>"\
                    "<li>كان معكم الجدعان</li>"\
                    "<li>Zaid Zitawi ID: 1203101</li>"\
                    "<li>Maen Alamleh ID: 1201183</li>"\
                    "<li>Firas Albarghouthy - ID: 1201921</li>"\
                    "<li>و صامدون كالجبل في وجه الكسارة كلبواب فيه وجه العمارة ولا تموت قبل أن تكون نداً ولا حول ولا قوة بالله العلي العظيم، والسلام عليكم ورحمة الله تعالي وبركاته</li>"\
                    "</ul>"\
                    "<p style='font-family: 'Courier New', monospace; font-size: 12px; color: #777;'>"\
                    f"IP: {ip}<br>"\
                    f"Port: {port}"\
                    "</p>"\
                    "</div>"\
                    "</body>"\
                    "</html>"

        #if the request is wrong or the file doesn’t exist the server should return a simple HTML webpage that contains with
        #some design and color needed
        notFoundHtmlBytes = bytes(notFoundHtmlString, "UTF-8")
        connectionSocket.send(notFoundHtmlBytes)

    connectionSocket.close() #close the connection
