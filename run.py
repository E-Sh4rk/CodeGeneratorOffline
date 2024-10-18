import http.server
import socketserver
import os
import threading
import webbrowser

PORT = 8080
handler = http.server.SimpleHTTPRequestHandler

web_dir = os.path.join(os.getcwd(), 'app')
os.chdir(web_dir)

def start_server():
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Serving content of {web_dir} at http://localhost:{PORT}")
        httpd.serve_forever()

# Start the server in a separate thread
server_thread = threading.Thread(target=start_server)
server_thread.daemon = True
server_thread.start()

# Open the web browser to the localhost address
webbrowser.open(f'http://localhost:{PORT}')

# Keep the script running so the server stays active
input("Press Enter to stop the server...\n")
