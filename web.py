from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<!DOCTYPE html>
<html>
<head>
    <title>TCP/IP Model Protocols</title>
</head>
<body>

    <h2>List of Protocols in TCP/IP Model</h2>

    <ol>
        <li>
            <b>Application Layer</b>
            <ul>
                <li>HTTP</li>
                <li>HTTPS</li>
                <li>FTP</li>
                <li>SMTP</li>
                <li>DNS</li>
                <li>DHCP</li>
            </ul>
        </li>

        <li>
            <b>Transport Layer</b>
            <ul>
                <li>TCP</li>
                <li>UDP</li>
            </ul>
        </li>

        <li>
            <b>Internet Layer</b>
            <ul>
                <li>IP</li>
                <li>ICMP</li>
                <li>ARP</li>
            </ul>
        </li>

        <li>
            <b>Network Access Layer</b>
            <ul>
                <li>Ethernet</li>
                <li>Wi-Fi</li>
                <li>PPP</li>
            </ul>
        </li>
    </ol>

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