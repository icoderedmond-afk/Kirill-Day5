import pyperclip
import requests


def fetch_random_quote():
    url = 'https://quoteslate.vercel.app/api/quotes/random'
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        )
    }

    try:
        # verify=True is the default in requests, leaving it on prevents SSL warnings
        response = requests.get(url, headers=headers, timeout=5)

        if response.status_code == 200:
            data = response.json()
            return {'quote': data['quote'], 'author': data['author']}
        else:
            print(
                f'Error fetching quote. Server responded with status code: {response.status_code}'
            )
            return None

    except requests.exceptions.SSLError:
        print(
            'SSL Certificate error. If you are on a restricted school or corporate network, it may be intercepting HTTPS requests.'
        )
        return None
    except requests.exceptions.RequestException as e:
        print(f'Network error occurred: {e}')
        return None


def display_menu():
    print('\n--- Python Quote Generator ---')
    print('1. Generate a new random quote')
    print('2. Copy the quote to clipboard')
    print('3. Exit')


def run_quote_generator():
    current_quote = None

    while True:
        display_menu()
        choice = input('Choose an option (1-3): ').strip()

        if choice == '1':
            current_quote = fetch_random_quote()
            if current_quote:
                print(f"\nQuote:  \"{current_quote['quote']}\"")
                print(f"Author: {current_quote['author']}")

        elif choice == '2':
            if current_quote:
                quote_text = (
                    f"\"{current_quote['quote']}\" - {current_quote['author']}"
                )
                pyperclip.copy(quote_text)
                print('\nYour quote has been copied to the clipboard!')
            else:
                print('\nPlease generate a quote first.')

        elif choice == '3':
            print('\nThank you! Goodbye.')
            break

        else:
            print('\nInvalid option. Please enter 1, 2, or 3.')


if __name__ == '__main__':
    run_quote_generator()