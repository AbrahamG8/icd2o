import random
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)

        if parsed_url.path == '/word_count':
            if 'text' in query_params:
                text = query_params['text'][0]
                word_count = len(text.split())
                result = f"Word count: {word_count}"
            else:
                result = "Missing 'text' parameter"

        elif parsed_url.path == '/celsius_to_fahrenheit':
            if 'celsius' in query_params:
                celsius = float(query_params['celsius'][0])
                fahrenheit = (celsius * 9/5) + 32
                result = f"{celsius} Celsius is {fahrenheit} Fahrenheit"
            else:
                result = "Missing 'celsius' parameter"

        elif parsed_url.path == '/fahrenheit_to_celsius':
            if 'fahrenheit' in query_params:
                fahrenheit = float(query_params['fahrenheit'][0])
                celsius = (fahrenheit - 32) * 5/9
                result = f"{fahrenheit} Fahrenheit is {celsius} Celsius"
            else:
                result = "Missing 'fahrenheit' parameter"

        elif parsed_url.path == '/random_number':
            if 'min' in query_params and 'max' in query_params:
                min_num = int(query_params['min'][0])
                max_num = int(query_params['max'][0])
                if min_num <= max_num:
                    random_num = random.randint(min_num, max_num)
                    result = f"Random number between {min_num} and {max_num}: {random_num}"
                else:
                    result = "'min' should be less than or equal to 'max'"
            else:
                result = "Missing 'min' or 'max' parameter"

        else:
            result = "Invalid endpoint"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(str(result).encode('utf-8'))

server_address = ('', 8080)
httpd = HTTPServer(server_address, RequestHandler)

print('Starting server...')
httpd.serve_forever()
