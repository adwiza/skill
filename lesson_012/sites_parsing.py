import multiprocessing

import requests

from extractor import LinkExtractor
from utils import time_track

sites = [
    'https://fl.ru',
    # 'https://www.wildberries.ru',
    # 'https://pass.mos.ru',
    'https://weblancer.ru',
    'https://freelancejob.ru',
    'https://kwork.ru',
    'https://work-zilla.com',
    'https://iklife.ru/udalennaya-rabota-i-frilans/poisk-raboty/vse-samye-luchshie-sajty-i-birzhi-v-internete.html',
]


class PageSizer(multiprocessing.Process):

    def __init__(self, url, collector, go_ahead=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = url
        self.go_ahead = go_ahead
        self.total_bytes = 0
        self.collector = collector

    def run(self):
        self.total_bytes = 0
        html_data = self._get_html(url=self.url)
        if html_data is None:
            return
        self.total_bytes += len(html_data)
        if self.go_ahead:
            extractor = LinkExtractor(base_url=self.url)
            extractor.feed(html_data)
            collector = multiprocessing.Queue()
            sizers = [PageSizer(url=link, collector=collector, go_ahead=False) for link in extractor.links]
            for sizer in sizers:
                sizer.start()
            for sizer in sizers:
                sizer.join()
            while not collector.empty():
                data = collector.get()
                self.total_bytes += data['total_bytes']
        self.collector.put = (dict(url=self.url, total_bytes=self.total_bytes))

    def _get_html(self, url):
        try:
            print(f'Go {url}...')
            res = requests.get(url)
        except Exception as exc:
            print(exc)
        else:
            return res.text


@time_track
def main():
    collector = multiprocessing.Queue()
    sizers = [PageSizer(url=url, collector=collector) for url in sites]

    for sizer in sizers:
        sizer.start()
    for sizer in sizers:
        sizer.join()

    while not collector.empty():
        data = collector.get()
        print(f"For url {data['url']} need download {data['url'] // 1024} Kbytes ({data['url']} bytes)")


if __name__ == '__main__':
    main()
