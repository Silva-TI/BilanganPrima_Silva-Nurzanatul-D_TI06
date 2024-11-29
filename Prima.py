from flask import Flask, request, render_template

app = Flask(__name__)

# Fungsi untuk memeriksa apakah angka adalah bilangan prima
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_prime():
    try:
        number = int(request.form['number'])
        if is_prime(number):
            result = f"{number} adalah bilangan prima."
        else:
            result = f"{number} bukan bilangan prima."
    except ValueError:
        result = "Harap masukkan angka yang valid."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
