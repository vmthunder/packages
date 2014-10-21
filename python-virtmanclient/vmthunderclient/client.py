import requests
from vmthunderclient.openstack.common import jsonutils


class Client(object):

    USER_AGENT = 'python-vmthunderclient'

    def __init__(self, endpoint, *args, **kwargs):
        self.endpoint = endpoint

    def create(self, instance_name, image_name, image_connections, snapshot):
        url = self._get_url('create')
        body = {
            'instance_name': instance_name,
            'image_name': image_name,
            'image_connections': image_connections,
            'snapshot': snapshot
        }
        resp = self._post(url, body)
        #fix? jsonutils.loads(resp.content)?
        return resp.content

    def destroy(self, instance_name):
        url = self._get_url('destroy')
        body = {
            'instance_name': instance_name,
        }
        self._post(url, body)

    def list(self):
        url = self._get_url('list')
        resp = self._get(url)
        instance_list = jsonutils.loads(resp.content)
        return instance_list

    def _post(self, url, body):
        kwargs = self._get_kwargs(body)
        resp = requests.request('POST', url, **kwargs)
        return resp

    def _get(self, url):
        resp = requests.request('GET', url)
        return resp

    def _get_url(self, function):
        return "http://%s/%s" % (self.endpoint, function)

    def _get_kwargs(self, body={}):
        kwargs = {}
        kwargs.setdefault('headers', kwargs.get('headers', {}))
        kwargs['headers']['Accept'] = 'application/json'
        kwargs['headers']['Content-Type'] = 'application/json'
        if not body == {}:
            kwargs['data'] = jsonutils.dumps(body)
        return kwargs

