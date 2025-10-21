# random_quotes.py
import random

def get_random_quote():
    quotes = [
        "The best way to get started is to quit talking and begin doing. – Walt Disney",
        "Success is not final; failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
        "Don’t let yesterday take up too much of today. – Will Rogers",
        "It always seems impossible until it’s done. – Nelson Mandela",
        "In the middle of difficulty lies opportunity. – Albert Einstein"
    ]
    return random.choice(quotes)

if __name__ == "__main__":
    print("Random Quote:")
    print(get_random_quote())
