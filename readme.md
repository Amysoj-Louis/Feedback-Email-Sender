# Feedback Email Sender

This is a Flask application that allows users to send feedback to a recipient email. The recipient email, subject, sender's email and password are set in the code.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

- Flask: A python micro framework for web development
- smtplib: A library for sending emails using the Simple Mail Transfer Protocol

## Installing

- Clone the repository to your local machine

```
$ git clone https://github.com/Amysoj-Louis/Feedback-Email-Sender.git
```

- Navigate to the cloned repository

```
$ cd Feedback-Email-Sender
```

### Configuration

Set the recipient email, subject, sender's email, and password in the code

```
user = "example@email.com" # Senders email
pwd = "\***\*\*\*\***" # Sender's password
recipient = "example@email.com" # Reciever's email
subject = "Feedback Form" # Subject Of the email
```

## Running the Application

To start the Flask application, run the following command:

```
$ python app.py
```

The application will run on http://0.0.0.0:8000/

## Usage

To send feedback, make a POST request to the / endpoint with the following parameters:

```
userid: The user's id or email
body: The feedback message
```
