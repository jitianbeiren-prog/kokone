"""Build the Japanese edition into dist/ and serve it on http://127.0.0.1:<port>/ , then open the browser.
usage: python3 start.py [--port 8000] [--no-open] [--no-build]"""
import http.server, os, subprocess, sys, threading, webbrowser
ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
args = sys.argv[1:]
port = int(args[args.index('--port') + 1]) if '--port' in args else 8000
if '--no-build' not in args or not os.path.exists('dist/index.html'):
    subprocess.run([sys.executable, 'build.py', '--local'], check=True)
class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k): super().__init__(*a, directory=os.path.join(ROOT, 'dist'), **k)
    def log_message(self, *a): pass
server = http.server.ThreadingHTTPServer(('127.0.0.1', port), Handler)
url = f'http://127.0.0.1:{port}/'
print(f'JIZURA を起動しました: {url}  （終了は Ctrl+C）')
if '--no-open' not in args: threading.Timer(0.5, webbrowser.open, (url,)).start()
try: server.serve_forever()
except KeyboardInterrupt: print('\n終了しました')
