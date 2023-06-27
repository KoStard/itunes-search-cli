import argparse
import requests
import json

def search(args):
    base_url = "https://itunes.apple.com/search"
    params = {
        'term': args.term,
        'country': args.country,
        'media': args.media,
        'entity': args.entity,
        'attribute': args.attribute,
        'callback': args.callback,
        'limit': args.limit,
        'lang': args.lang,
        'version': args.version,
        'explicit': args.explicit
    }
    response = requests.get(base_url, params=params)
    print(json.dumps(response.json(), indent=4))

def lookup(args):
    base_url = "https://itunes.apple.com/lookup"
    params = {
        'id': args.id
    }
    response = requests.get(base_url, params=params)
    print(json.dumps(response.json(), indent=4))

def main():
    parser = argparse.ArgumentParser(description='CLI tool for iTunes Search API')
    subparsers = parser.add_subparsers()

    search_parser = subparsers.add_parser('search', help='Search in iTunes')
    search_parser.add_argument('term', help='The URL-encoded text string you want to search for.')
    search_parser.add_argument('--country', default='us', help='The two-letter country code for the store you want to search.')
    search_parser.add_argument('--media', default='all', choices=['movie', 'podcast', 'music', 'musicVideo', 'audiobook', 'shortFilm', 'tvShow', 'software', 'ebook', 'all'], help='The media type you want to search for.')
    search_parser.add_argument('--entity', help='The type of results you want returned, relative to the specified media type.')
    search_parser.add_argument('--attribute', help='The attribute you want to search for in the stores, relative to the specified media type.')
    search_parser.add_argument('--callback', help='The name of the Javascript callback function you want to use when returning search results to your website.')
    search_parser.add_argument('--limit', type=int, default=50, choices=range(1, 201), help='The number of search results you want the iTunes Store to return.')
    search_parser.add_argument('--lang', default='en_us', choices=['en_us', 'ja_jp'], help='The language, English or Japanese, you want to use when returning search results.')
    search_parser.add_argument('--version', type=int, default=2, choices=[1, 2], help='The search result key version you want to receive back from your search.')
    search_parser.add_argument('--explicit', choices=['Yes', 'No'], default='Yes', help='A flag indicating whether or not you want to include explicit content in your search results.')
    search_parser.set_defaults(func=search)

    lookup_parser = subparsers.add_parser('lookup', help='Lookup resources in iTunes')
    lookup_parser.add_argument('id', help='Resource ID')
    lookup_parser.set_defaults(func=lookup)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
