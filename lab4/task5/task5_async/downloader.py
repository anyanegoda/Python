import urllib.request as req
from urllib.parse import unquote
from os import path
from datetime import datetime


class download(object):
    def __init__(self, response, output, count):
        self._response = response
        self._output = output
        self._count = count

    def __await__(self):
        self._output.write(self._response.read(self._count))
        yield


class downloader_async(object):

    def __init__(self, url, update_callback):
        self._url = url
        self._update_callback = update_callback

    async def __call__(self):
        self.filename = unquote(self._url).split('/')[-1]
        response = req.urlopen(self._url)
        count = 4096
        self.file_size = response.length
        with open(path.join('downloads', self.filename), 'wb') as output:
            start_time = datetime.now()
            while response.length:
                await download(response, output, count)
                self._update_callback(1 - response.length / self.file_size)
            self.timedelta = datetime.now() - start_time
            self._update_callback(1)
