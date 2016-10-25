# The requests module is used to visit web pages from Python
import requests


#
#
#
def load_site(url):

    # Using requests, hit the given URL
    page = requests.get(url)

    # Extract the content from the results
    content = page.content

    # Return the content, transformed to all lowercase
    return content.lower()


#
#
#
def search_for_vacations(destination):

    print('Searching for: ' + destination)
    destination = destination.lower()

    sites = [
        'https://www.travelzoo.com/top20/',
        'https://www.groupon.com/occasion/last-minute-travel-deals',
        'http://thewcc.com/files/python/vacations/']

    for url in sites:

        content = load_site(url)

        print('\nChecking site: ' + url)

        if destination in content:
            print('-> FOUND! ')
        else:
            print('-> Not found.')

search_for_vacations('Spain')

# Extra feature ideas:
# Search for multiple destinations
# Send an email when destinations are found
