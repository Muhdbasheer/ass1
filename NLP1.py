import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import re

# Download nltk resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Function to fetch HTML content from URL and extract text
def get_text_from_url(url):
    # extract HTML content. This line makes a GET request to the specified URL using the requests.get() function from the requests library and assigns the response to the response variable. The .text attribute of the response object (response.text) then contains the HTML content of the webpage.
    response = requests.get(url)
    html_content = response.text

    #enables us to extract text
    # Parse HTML using BeautifulSoup.After this line, the variable soup holds the BeautifulSoup object representing the parsed HTML content. You can then use methods and properties provided by BeautifulSoup to navigate and manipulate the HTML content more easily
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract text from HTML.This line uses BeautifulSoup's get_text() method on the soup object, which represents the parsed HTML content. It extracts all the textual content from the HTML, stripping away any HTML tags, and assigns it to the variable text. This text variable then contains the extracted text from the HTML.
    text = soup.get_text()

    return text

# Function to process text (clean, stem, remove stopwords, normalize)
def process_text(text):
    #the regular expression pattern [^a-zA-Z\s] is used to match any character that is not an alphabetic character (uppercase or lowercase) or a whitespace character. The pattern.sub('', text) call removes all such characters from the text, leaving only alphabetic characters and spaces.


    # Tokenization
    words = word_tokenize(text)

    # Lowercasing and removing non-alphabetic characters
    words = [word.lower() for word in words if word.isalpha()]

    # Removing stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    # Stemming
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]

    # Get unique words
    unique_words = set(words)

    return unique_words

# URL of wikipedia
url = 'https://en.wikipedia.org'

# Get text from URL
text = get_text_from_url(url)

# Process text
unique_words = process_text(text)

# Print unique words
print("Unique words:", unique_words)
words = [word for word in unique_words if len(word)<3]
print(words)
