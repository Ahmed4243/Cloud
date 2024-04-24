import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# Download stopwords if not already downloaded
nltk.download('stopwords')
nltk.download('punkt')

def main():
    try:
        with open('random_paragraphs.txt', 'r') as file:
            content = file.read()

        stop_words = set(stopwords.words('english'))

        word_tokens = word_tokenize(content.lower())  # Tokenize and lowercase the content

        filtered_sentence = [w for w in word_tokens if w not in stop_words]

        fd = FreqDist(filtered_sentence)

        # Sort word frequencies
        sorted_frequencies = sorted(fd.items(), key=lambda x: x[1], reverse=True)
        # Write sorted word frequencies to a text file
        with open('word_frequencies.txt', 'w') as output_file:
            for word, frequency in sorted_frequencies:
                print(f"{word}: {frequency}\n")
                output_file.write(f"{word}: {frequency}\n")

        print("Word frequencies saved to 'word_frequencies.txt'.")

    except FileNotFoundError:
        print("File not found. Make sure 'random_paragraphs.txt' exists in the current directory.")

if __name__ == "__main__":
    main()
