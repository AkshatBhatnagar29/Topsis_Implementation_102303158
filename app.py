from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def send_email(to_email, filename):
    # --- EMAIL CONFIGURATION ---
    from_email = "abhatnagar_be23@thapar.edu"
    password = os.getenv('password')  
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "TOPSIS Result"

    body = "Please find the attached result file containing the TOPSIS scores and ranks."
    msg.attach(MIMEText(body, 'plain'))

    with open(filename, "rb") as attachment:
        p = MIMEBase('application', 'octet-stream')
        p.set_payload(attachment.read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', f"attachment; filename={os.path.basename(filename)}")
        msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(from_email, password)
    s.sendmail(from_email, to_email, msg.as_string())
    s.quit()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file uploaded"
        
        file = request.files['file']
        weights_str = request.form['weights']
        impacts_str = request.form['impacts']
        email = request.form['email']

        if file.filename == '':
            return "No file selected"

        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], "result.csv")
        file.save(input_path)

        try:
            df = pd.read_csv(input_path)
            
            # Check for sufficient columns
            if df.shape[1] < 3:
                return "Error: Input file must contain three or more columns."

            try:
                data = df.iloc[:, 1:].values.astype(float)
            except ValueError:
                return "Error: Columns from 2nd to last must contain numeric values only."

            try:
                weights = [float(w) for w in weights_str.split(',')]
                impacts = impacts_str.split(',')
            except ValueError:
                return "Error: Weights must be numeric and separated by comma."

            if len(weights) != data.shape[1] or len(impacts) != data.shape[1]:
                return "Error: Number of weights, impacts, and numeric columns must be the same."

            if not all(i in ['+', '-'] for i in impacts):
                return "Error: Impacts must be either + or -."

            
            normalized_data = data / np.sqrt((data**2).sum(axis=0))

            weighted_data = normalized_data * weights

            ideal_best = []
            ideal_worst = []

            for i in range(len(impacts)):
                if impacts[i] == '+':
                    ideal_best.append(max(weighted_data[:, i]))  # Max is best for +
                    ideal_worst.append(min(weighted_data[:, i])) # Min is worst for +
                else:
                    ideal_best.append(min(weighted_data[:, i]))  # Min is best for -
                    ideal_worst.append(max(weighted_data[:, i])) # Max is worst for -

            s_best = np.sqrt(((weighted_data - ideal_best) ** 2).sum(axis=1))
            s_worst = np.sqrt(((weighted_data - ideal_worst) ** 2).sum(axis=1))

            total_s = s_best + s_worst
            scores = np.divide(s_worst, total_s, out=np.zeros_like(s_worst), where=total_s!=0)

            df['Topsis Score'] = scores
            df['Rank'] = df['Topsis Score'].rank(ascending=False)

            df.to_csv(output_path, index=False)

            
            send_email(email, output_path)
            return "Success! Result file has been sent to your email."

        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)