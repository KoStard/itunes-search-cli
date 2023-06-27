# iTunes Search CLI

A command-line interface tool for searching and looking up items in the iTunes store using the iTunes Search API.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/itunes-search-cli.git
   ```
2. Navigate to the project directory:
   ```
   cd itunes-search-cli
   ```
3. Create a virtual environment:
   ```
   python3 -m venv env
   ```
4. Activate the virtual environment:
   ```
   source env/bin/activate
   ```
5. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To search for items in the iTunes store, use the `search` command followed by your search term. You can also specify additional parameters:

```bash
python itunes_search.py search "jack johnson" --country us --media music --limit 10
```

This will search for "jack johnson" in the US iTunes store, limit the results to music, and return the top 10 results.

To lookup an item by its ID, use the `lookup` command followed by the item ID:

```bash
python itunes_search.py lookup 909253
```

This will lookup the item with the ID 909253 in the iTunes store.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the terms of the MIT license.
