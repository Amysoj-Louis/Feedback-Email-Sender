# Import required libraries for Flask, JSON, and SMTP email
from flask import Flask, jsonify, request
import smtplib

# Sender's email and password
user = "example@email.com"
pwd = "*********"

# Receiver's email
recipient = "example@email.com"

# Subject of the email
subject = "Feedback Form"

# Function to send the email


def send_email(body, userid):
    # Set the subject of the email
    SUBJECT = subject

    # Build the body of the email using the userid and body arguments
    TEXT = F"{userid} \n\n{body}"

    # Build the entire email message
    message = f"From: {user}\nTo:{recipient if isinstance(recipient, list) else [recipient]}\nSubject: {SUBJECT}\n\n{TEXT}"

    # Try to send the email using the Gmail SMTP server
    try:
        # Connect to Gmail SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()  # Identify the server
        server.starttls()  # Start encrypted connection
        server.login(user, pwd)  # Login to the email account
        server.sendmail(user, recipient if isinstance(recipient, list) else [
                        recipient], message)  # Send the email
        server.close()  # Close the connection
        print('successfully sent the mail')
        # Return success message
        return {"status": 'Thank You For the Feedback'}
    except Exception as e:
        print(e)  # Print the error if the email fails to send
        print("failed to send mail")
        # Return failure message
        return {"status": "failed to send Feedback", "Reason": e}


# Initialize the Flask application
app = Flask(__name__)

# Route for sending feedback


@app.route('/', methods=['POST'])
def welcome():
    # Get the data from the request form
    args = request.form
    # Check if the request has both userid and body
    if (args.get("userid") != None and args.get("body") != None and args.get("userid") != "" and args.get("body") != ""):
        userid = args.get("userid")
        body = args.get("body")
        # Call the send_email function with userid and body
        return jsonify(send_email(userid=userid, body=body))
    else:
        # Return error message if userid or body is missing
        return jsonify({"status": "Couldn't find UserId Or Message Body"})


# Run the Flask app if it's the main module
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8000")
