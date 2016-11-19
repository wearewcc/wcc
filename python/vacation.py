# The requests module is used to visit web pages from Python
import requests

# https://github.com/kootenpv/yagmail
import yagmail


def load_site(url):

    # Using requests, hit the given URL
    page = requests.get(url)

    # Extract the content from the results
    content = page.content

    # Return the content, transformed to all lowercase
    return content.lower()


def send_email(recipient, subject, body):

    # Intialize yagmail
    yag = yagmail.SMTP('wcc.python@gmail.com')

    # Send the email
    yag.send(recipient, subject, body)


def search_for_vacations(destination, url):

    # Convert destination to lowercase so search is case insensitive
    destination = destination.lower()

    content = load_site(url)

    print('Searching for: ' + destination + '\nChecking site: ' + url)

    if destination in content:
        print('-> FOUND! ')

        # Send email
        recipient = 'elizabeth@thewcc.com' # Update with your email address
        subject = 'Vacation deal found for ' + destination + '!'
        body = 'Quick! Check out ' + url + ' -- they just posted a deal for a trip to ' + destination + '.'
        send_email(recipient, subject, body)
    else:
        print('-> Not found ')


# Run!
search_for_vacations('NYC', 'https://www.travelzoo.com/top20')
