"""SlingshotWorld - aplicatie desktop (fereastra proprie, fara browser vizibil).

Ruleaza jocul HTML local. Datele (turnee, scoruri) se salveaza in
%APPDATA%\\SlingshotWorld si raman si dupa inchiderea aplicatiei.
"""
import os
import sys
import threading
import functools
import webbrowser
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

APP_NAME = "SlingshotWorld"
HTML_FILE = "index.html"  # a repo gyokereben levo app
PREFERRED_PORT = 8765  # port fix => acelasi "origin" => datele se pastreaza


def resource_dir():
    # Cand e impachetat cu PyInstaller, fisierele sunt in sys._MEIPASS.
    # Altfel (rulare din sursa) index.html e in radacina repo-ului, un nivel mai sus.
    if hasattr(sys, "_MEIPASS"):
        return sys._MEIPASS
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def data_dir():
    base = os.environ.get("APPDATA") or os.path.expanduser("~")
    path = os.path.join(base, APP_NAME)
    os.makedirs(path, exist_ok=True)
    return path


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def start_server():
    handler = functools.partial(QuietHandler, directory=resource_dir())
    for port in [PREFERRED_PORT] + list(range(PREFERRED_PORT + 1, PREFERRED_PORT + 20)):
        try:
            server = ThreadingHTTPServer(("127.0.0.1", port), handler)
            break
        except OSError:
            continue
    else:
        raise RuntimeError("Nu am gasit niciun port liber.")
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server.server_address[1]


def main():
    port = start_server()
    url = "http://127.0.0.1:%d/%s" % (port, HTML_FILE)
    try:
        import webview  # pywebview
    except ImportError:
        # Varianta de rezerva: deschide in browserul implicit
        webbrowser.open(url)
        print("Aplicatia ruleaza la", url, "- apasa Ctrl+C pentru oprire.")
        try:
            threading.Event().wait()
        except KeyboardInterrupt:
            pass
        return
    try:
        webview.settings['ALLOW_DOWNLOADS'] = True  # necesar pentru Export JPG / JSON
    except Exception:
        pass
    webview.create_window(APP_NAME, url, width=1200, height=820, min_size=(420, 600))
    webview.start(private_mode=False, storage_path=data_dir())


if __name__ == "__main__":
    main()
