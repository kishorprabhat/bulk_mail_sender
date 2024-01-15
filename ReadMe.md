# Bulk Mail Sender

## Python smtp library docs

<https://docs.python.org/3/library/smtplib.html>

## Open SSL command to show certs

```openssl s_client -showcerts -connect  smtp.gmail.com:465```

## Requirements

Python

Pip

Pyyaml

## For getting smtp passwords

<https://mailmeteor.com/blog/gmail-smtp-settings>

## How to Run

*Step 1:* Update config.yaml with your smtp details refer above link to generate google mail server passwords

*Step 2:* Update `recipients.csv` with recipients email addresses

*Step 3:* Run below command in your terminal

    python3 mailer.py

## Special thanks to bard for doing most of the work

<https://bard.google.com>
