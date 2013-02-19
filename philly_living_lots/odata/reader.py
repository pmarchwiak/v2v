from datetime import datetime
from dateutil.tz import tzlocal
import json
import re
from urllib import urlencode
from urllib2 import urlopen

DATETIME_REGEX = re.compile('\D*(\d+)\D*')


class ODataReader(object):

    def __init__(self, service_url):
        self.service_url = service_url

    def get(self, endpoint, params={}):
        """
        Get data from the given service and endpoint.

        """
        params.update({ '$format': 'json' })
        url = self.service_url + endpoint + '?' + urlencode(params)
        return self.get_url(url)

    def get_url(self, url):
        response = json.load(urlopen(url))

        for result in response['d']['results']:
            yield result

        next_url = response['d'].get('__next', None)
        if next_url:
            yield self.get_url(next_url)

    @classmethod
    def get_datetime(cls, timestamp):
        if not timestamp: return None
        timestamp = re.match(DATETIME_REGEX, timestamp).group(1)
        return datetime.fromtimestamp(float(timestamp[:-3]), tzlocal())
