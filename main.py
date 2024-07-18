from flask import Flask, request, render_template_string
import sys
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="zh-Hant">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>日本計程車費用計算</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f8ff;
                color: #333;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background-color: #fff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                text-align: center;
                max-width: 400px;
                width: 100%;
            }
            h1 {
                color: #4CAF50;
                margin-bottom: 20px;
            }
            input[type="text"] {
                width: calc(100% - 24px);
                padding: 10px;
                margin-bottom: 20px;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 16px;
            }
            button {
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                cursor: pointer;
            }
            button:hover {
                background-color: #45a049;
            }
            pre {
                background-color: #f8f8f8;
                padding: 10px;
                border-radius: 5px;
                text-align: left;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>日本計程車輸入公尺-金額</h1>
            <form method="post" action="/execute">
                <input type="text" name="meters" placeholder="請輸入公尺數">
                <button type="submit">送出</button>
            </form>
            {% if result %}
                <h2>結果:</h2>
                <pre>{{ result }}</pre>
            {% endif %}
        </div>
    </body>
    </html>
    ''')

@app.route('/execute', methods=['POST'])
def execute():
    meters = request.form['meters']
    try:
        a = int(meters)
        if a <= 1000:
            a = 430
        else:
            a = 430 + (a / 230) * 80
        result_jpy = f"日幣: {a:.0f}"
        b = a * 0.207
        result_twd = f"台幣: {b:.0f}"
        result = f"{result_jpy}\n{result_twd}"
    except Exception as e:
        result = f"錯誤: {str(e)}"
    
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="zh-Hant">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>日本計程車費用計算</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f8ff;
                color: #333;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background-color: #fff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                text-align: center;
                max-width: 400px;
                width: 100%;
            }
            h1 {
                color: #4CAF50;
                margin-bottom: 20px;
            }
            input[type="text"] {
                width: calc(100% - 24px);
                padding: 10px;
                margin-bottom: 20px;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 16px;
            }
            button {
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                cursor: pointer;
            }
            button:hover {
                background-color: #45a049;
            }
            pre {
                background-color: #f8f8f8;
                padding: 10px;
                border-radius: 5px;
                text-align: left;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>日本計程車輸入公尺-金額</h1>
            <form method="post" action="/execute">
                <input type="text" name="meters" placeholder="請輸入公尺數">
                <button type="submit">送出</button>
            </form>
            {% if result %}
                <h2>結果:</h2>
                <pre>{{ result }}</pre>
            {% endif %}
        </div>
    </body>
    </html>
    ''', result=result)

if __name__ == '__main__':
    app.run(debug=True)
