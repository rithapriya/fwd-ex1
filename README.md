# EX01 Developing a Simple Webserver
## Date: 24.10.2026
## Register No: 26012923
## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
~~~
<!DOCTYPE html>
<html>
<head>
    <title>Network Protocols</title>
</head>
<body>

    <h2 align="center">Network Protocols and Their Abbreviations</h2>

    <table border="1" cellpadding="10" cellspacing="0" align="center">
        <tr>
            <th>S.No</th>
            <th>Protocol</th>
            <th>Abbreviation</th>
            <th>Purpose</th>
        </tr>

        <tr>
            <td>1</td>
            <td>Hypertext Transfer Protocol</td>
            <td>HTTP</td>
            <td>Transfers web pages</td>
        </tr>

        <tr>
            <td>2</td>
            <td>Hypertext Transfer Protocol Secure</td>
            <td>HTTPS</td>
            <td>Secure communication on websites</td>
        </tr>

        <tr>
            <td>3</td>
            <td>File Transfer Protocol</td>
            <td>FTP</td>
            <td>Transfers files</td>
        </tr>

        <tr>
            <td>4</td>
            <td>Transmission Control Protocol</td>
            <td>TCP</td>
            <td>Reliable data transmission</td>
        </tr>

        <tr>
            <td>5</td>
            <td>Internet Protocol</td>
            <td>IP</td>
            <td>Addresses and routes data packets</td>
        </tr>

        <tr>
            <td>6</td>
            <td>Domain Name System</td>
            <td>DNS</td>
            <td>Converts domain names into IP addresses</td>
        </tr>

        <tr>
            <td>7</td>
            <td>Simple Mail Transfer Protocol</td>
            <td>SMTP</td>
            <td>Sends emails</td>
        </tr>

        <tr>
            <td>8</td>
            <td>Post Office Protocol Version 3</td>
            <td>POP3</td>
            <td>Retrieves emails from a server</td>
        </tr>

        <tr>
            <td>9</td>
            <td>Internet Message Access Protocol</td>
            <td>IMAP</td>
            <td>Accesses and manages emails on a server</td>
        </tr>

        <tr>
            <td>10</td>
            <td>Dynamic Host Configuration Protocol</td>
            <td>DHCP</td>
            <td>Automatically assigns IP addresses</td>
        </tr>
    </table>

</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',880)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
~~~
## OUTPUT:
![alt text](<../screenshot fwd.jpeg>)

## RESULT:
The program for implementing simple webserver is executed successfully.

