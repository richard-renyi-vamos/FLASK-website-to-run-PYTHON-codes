from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run-script', methods=['POST'])
def run_script():
    # Example: Replace 'your_script.py' with the script to run
    try:
        result = subprocess.check_output(['python', 'scripts/your_script.py'], text=True)
        return {'status': 'success', 'output': result}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}

if __name__ == '__main__':
    app.run(debug=True)
