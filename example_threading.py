from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from diskcache import FanoutCache

cache = FanoutCache()

urls = [
    "https://google.com",
    "https://python.org",
    "https://bitecode.dev",
    "https://formationspython.com",
    "https://google.com",
    "https://python.org",
    "https://bitecode.dev",
    "https://formationspython.com",
] * 20


def print_page_size(url):
    value = cache.get(url)
    if value:
        return url, value

    res = len(requests.get(url).content)
    cache.set(url, res, expire=3600 * 24)

    return url, res


futures = []

with ThreadPoolExecutor(max_workers=100) as pool:
    for url in urls:
        fut = pool.submit(print_page_size, url)
        futures.append(fut)

for fut in as_completed(futures):
    url, value = fut.result()
    print(url, value)
