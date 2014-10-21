# Copyright 2012 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import testtools

from voltclient.v1 import volumes
from voltclient.tests import utils

fixtures = {
    '/v1/volumes': {
        'GET': (
            {},
            [{
                'host': 'localhost',
                'port': '9527',
                'iqn': 'iqn.2014-3-16.com:pdl',
                'lun': '2'
            },
            {
                'host': 'localhost',
                'port': '9527',
                'iqn': 'iqn.2014-3-16.com:pdl',
                'lun': '2'
            }]
        ),
        'DELETE': (
            {},
            None
        )
    },
    '/v1/volumes/5cc4bebc-db27-11e1-a1eb-080027cbe205': {
        'POST': (
            {},
            {
                'peer_id': 'peer1',
                'host': 'localhost',
                'port': '9527',
                'iqn': 'iqn.2014-3-16.com:pdl',
                'lun': '2'
            }
        ),
        'GET': (
            {},
            [{
                'host': 'localhost',
                'port': '9527',
                'iqn': 'iqn.2014-3-17.com:pdl',
                'lun': '2'
            },
            {
                'host': 'localhost',
                'port': '7447',
                'iqn': 'iqn.2014-3-16.com:pdl',
                'lun': '3'
            }]
        ),
        'HEAD': (
            {},
            [{
                'host': 'localhost',
                'port': '9527',
                'iqn': 'iqn.2014-3-16.com:pdl',
                'lun': '2'
            }]

        ),
        'DELETE': (
            {},
            None
        )
    },
}


class VolumeManagerTest(testtools.TestCase):

    def setUp(self):
        super(VolumeManagerTest, self).setUp()
        self.api = utils.FakeAPI(fixtures)
        self.mgr = volumes.VolumeManager(self.api)

    def test_volumes_list(self):
        test_volumes = self.mgr.list()
        expect = [
            ('GET', '/v1/volumes', {}, None),
        ]
        self.assertEqual(self.api.calls, expect)
        self.assertEqual(len(test_volumes), 2)
        self.assertEqual(test_volumes[0].host, 'localhost')
        self.assertEqual(test_volumes[0].port, '9527')
        self.assertEqual(test_volumes[0].iqn, 'iqn.2014-3-16.com:pdl')
        self.assertEqual(test_volumes[0].lun, '2')

    def test_volumes_list_with_id(self):
        test_volumes = self.mgr.list(
            volume_id='5cc4bebc-db27-11e1-a1eb-080027cbe205'
        )
        expect = [
            (
                'HEAD',
                '/v1/volumes/5cc4bebc-db27-11e1-a1eb-080027cbe205',
                {},
                None
            ),
        ]
        self.assertEqual(self.api.calls, expect)
        self.assertEqual(len(test_volumes), 1)
        self.assertEqual(test_volumes[0].host, 'localhost')
        self.assertEqual(test_volumes[0].port, '9527')
        self.assertEqual(test_volumes[0].iqn, 'iqn.2014-3-16.com:pdl')
        self.assertEqual(test_volumes[0].lun, '2')

    def test_get(self):
        test_volumes = self.mgr.get(
            volume_id='5cc4bebc-db27-11e1-a1eb-080027cbe205'
        )
        expect = [
            (
                'GET',
                '/v1/volumes/5cc4bebc-db27-11e1-a1eb-080027cbe205',
                {},
                {}
            ),
        ]
        self.assertEqual(self.api.calls, expect)
        self.assertEqual(len(test_volumes), 2)
        volume = test_volumes[0]
        self.assertEqual(volume.host, 'localhost')
        self.assertEqual(volume.port, '9527')

    def test_logout_with_id(self):
        self.mgr.logout(
            volume_id='5cc4bebc-db27-11e1-a1eb-080027cbe205',
            peer_id='peer1'
        )
        expect = [
            (
                'DELETE',
                '/v1/volumes/5cc4bebc-db27-11e1-a1eb-080027cbe205',
                {},
                {'peer_id':'peer1'}
            )
        ]
        self.assertEqual(self.api.calls, expect)

    def test_logout(self):
        self.mgr.logout()
        expect = [
            (
                'DELETE',
                '/v1/volumes',
                {},
                {}
            )
        ]
        self.assertEqual(self.api.calls, expect)

    def test_login(self):
        test_volume = self.mgr.login(
            volume_id='5cc4bebc-db27-11e1-a1eb-080027cbe205',
            host='localhost',
            port='9527',
            iqn='iqn.2014-3-16.com:pdl',
            lun='2'
        )

        expect = [
            (
                'POST',
                '/v1/volumes/5cc4bebc-db27-11e1-a1eb-080027cbe205',
                {},
                {
                    'host': 'localhost',
                    'port': '9527',
                    'iqn': 'iqn.2014-3-16.com:pdl',
                    'lun': '2'
                }
            )
        ]

        self.assertEqual(self.api.calls, expect)
        self.assertIsInstance(test_volume, volumes.Volume)
        self.assertEqual(test_volume.port, '9527')
        self.assertEqual(test_volume.peer_id, 'peer1')

