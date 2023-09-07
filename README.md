
# Datamuse Word Fetcher
This Python script fetches words from the Datamuse API based on a given starting letter. It aims to collect a specific amount of words for each letter of the alphabet and saves them to a text file.

## Features

- Fetch words by starting letter from the Datamuse API.
- Handles API rate limits by introducing sleep between requests.
- Uses progress bar to display the fetching progress.
- Ensures unique word collection.
- Allows for safe interruption via `KeyboardInterrupt` and saves progress.

## Requirements

- `requests`: To make HTTP requests to the Datamuse API.
- `tqdm`: To display a progress bar during word collection.

You can install these requirements using `pip`:

```bash
pip install requests tqdm
```

## Usage

Run the script using Python:

```bash
python wordList.py
```

### Output

- The script will save the fetched words to `output.txt` by default.
- The words are separated by commas.

## Functions

### 1. `get_words_from_datamuse(starting_letter='', limit=1000)`

Fetches words from the Datamuse API based on the starting letter provided. If no starting letter is provided, it fetches random words. The limit parameter specifies the maximum number of words to fetch.

### 2. `save_words_to_file(words, filename='output.txt')`

Saves a list of words to the specified file. Words are separated by commas.

## Note

The script uses a `time.sleep(1)` delay between requests to avoid hitting the API's rate limit. Be cautious about making rapid or large numbers of requests.

If the script doesn't find new words for three consecutive batches for a particular letter, it will move on to the next letter.

## License

This script is provided as-is under the MIT License. Use at your own discretion.
