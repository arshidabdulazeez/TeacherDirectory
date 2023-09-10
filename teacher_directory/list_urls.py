# list_urls.py (in your project directory)

from django.urls import get_resolver

resolver = get_resolver(None)
url_patterns = resolver.url_patterns
print('List of URL patterns:')
for pattern in url_patterns:
    print(f'- {pattern}')
