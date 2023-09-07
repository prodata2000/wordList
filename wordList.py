import requests
from tqdm import tqdm
import time

def get_words_from_datamuse(starting_letter='', limit=1000):
    """Fetch words from Datamuse API with the specified length and starting letter."""
    url = f"https://api.datamuse.com/words?sp={starting_letter}???*&max={limit}"
    response = requests.get(url)
    response.raise_for_status()
    return [word_data["word"] for word_data in response.json()]


def save_words_to_file(words, filename='output.txt'):
    """Save a list of words to a file, separated by commas."""
    with open(filename, 'w') as f:
        f.write(', '.join(words))


if __name__ == "__main__":
    total_words_required_per_letter = 3000
    batch_size = 1000
    unique_words = set()

    # Progress bar setup
    try:
        with tqdm(total=total_words_required_per_letter * 26) as pbar:  # We're trying all 26 letters
            for letter in 'abcdefghijklmnopqrstuvwxyz':
                words_for_this_letter = set()
                no_new_words_counter = 0  # Counter for consecutive batches without new words

                while len(words_for_this_letter) < total_words_required_per_letter:
                    new_words = get_words_from_datamuse(starting_letter=letter, limit=batch_size)

                    if not new_words:  # break the loop if we don't get any new words
                        break

                    prev_length = len(words_for_this_letter)
                    words_for_this_letter.update(new_words)
                    unique_words.update(new_words)
                    pbar.update(len(new_words))

                    # Check if no new words have been added in this batch
                    if prev_length == len(words_for_this_letter):
                        no_new_words_counter += 1
                    else:
                        no_new_words_counter = 0  # Reset the counter if new words have been added

                    if no_new_words_counter == 3:  # Break the loop if two consecutive batches had no new words
                        break

                    # Pause to avoid rate limits
                    time.sleep(1)  # Sleep for 1 second

    except KeyboardInterrupt:
        print("\nInterrupted. Saving current words to file...")
        save_words_to_file(list(unique_words))
        print(f"Words saved to output.txt")
        exit()

    # Save to file (in case the process completes successfully)
    save_words_to_file(list(unique_words))
    print(f"Words saved to output.txt")
