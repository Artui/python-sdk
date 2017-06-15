import unittest

import requests_mock
from six.moves import urllib

from . import request_body_matcher
from transloadit.client import Transloadit
from transloadit.request import Request


class RequestTest(unittest.TestCase):
    def setUp(self):
        self.transloadit = Transloadit('key', 'secret')
        self.request = Request(self.transloadit)

    @requests_mock.Mocker()
    def test_get(self, mock):
        url = '{}/foo'.format(self.transloadit.host)
        mock.get(url, text='{"ok": "it works"}')

        response = self.request.get('/foo')
        self.assertEqual(response.data['ok'], 'it works')

    @requests_mock.Mocker()
    def test_post(self, mock):
        url = '{}/foo'.format(self.transloadit.host)
        sub_body = urllib.parse.quote_plus('"foo": "bar"')
        mock.post(url, text='{"ok": "it works"}',
                  additional_matcher=request_body_matcher(sub_body))

        response = self.request.post('/foo', data={'foo': 'bar'})
        self.assertEqual(response.data['ok'], 'it works')

    @requests_mock.Mocker()
    def test_put(self, mock):
        url = '{}/foo'.format(self.transloadit.host)
        sub_body = urllib.parse.quote_plus('"foo": "bar"')
        mock.put(url, text='{"ok": "it works"}',
                 additional_matcher=request_body_matcher(sub_body))

        response = self.request.put('/foo', data={'foo': 'bar'})
        self.assertEqual(response.data['ok'], 'it works')

    @requests_mock.Mocker()
    def test_delete(self, mock):
        url = '{}/foo'.format(self.transloadit.host)
        sub_body = urllib.parse.quote_plus('"foo": "bar"')
        mock.delete(url, text='{"ok": "it works"}',
                    additional_matcher=request_body_matcher(sub_body))

        response = self.request.delete('/foo', data={'foo': 'bar'})
        self.assertEqual(response.data['ok'], 'it works')
