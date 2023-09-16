# Author: Sakthi Santhosh
# Created on: 26/08/2023
#
# Flask Hello World App
from flask import Flask, render_template_string
from secrets import token_hex

def main() -> None:
    TOKEN = token_hex(4)

    app_handle = Flask(__name__)

    @app_handle.route('/')
    def index_handle():
        return render_template_string(
            f"<h1 style='font-family: system-ui;'>Hello World ({TOKEN})</h1>"
        )

    app_handle.run(debug=True, host="0.0.0.0")

if __name__ == "__main__":
    main()
