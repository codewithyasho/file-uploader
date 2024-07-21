from flask import Flask, request, render_template
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key'


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file provided."

        file = request.files['file']

        if file.filename == '':
            return "No selected file."

        # Save the file to the 'uploads' folder
        file.save('static/' + file.filename)

        # Render the display template with the filename
        return render_template('display.html', filename=file.filename)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
