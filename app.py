from flask import Flask, jsonify, request
import smtplib
user = "example@email.com"  # Senders email
pwd = "*********"  # Sender's password
recipient = "example@email.com"  # Reciever's email
subject = "Feedback Form"  # Subject Of the email


def send_email(body, userid):
    SUBJECT = subject

    TEXT = F"{userid} \n\n{body}"  # body of the email to be send

    # message to be send
    message = f"From: {user}\nTo:{recipient if isinstance(recipient, list) else [recipient]}\nSubject: {SUBJECT}\n\n{TEXT}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(user, recipient if isinstance(
            recipient, list) else [recipient], message)
        server.close()
        print('successfully sent the mail')
        return {"status": 'Thank You For the Feedback'}
    except Exception as e:
        print(e)
        print("failed to send mail")
        return {"status": "failed to send Feedback", "Reason": e}


app = Flask(__name__)


@app.route('/', methods=['POST'])
def welcome():
    args = request.form
    if (args.get("userid") != None and args.get("body") != None and args.get("userid") != "" and args.get("body") != ""):
        userid = args.get("userid")
        body = args.get("body")
        return jsonify(send_email(userid=userid, body=body))
    else:
        return jsonify({"status": "Couldn't find UserId Or Message Body"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8000")
