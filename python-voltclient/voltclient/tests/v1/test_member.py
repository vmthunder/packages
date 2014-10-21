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

from voltclient.v1 import members
from voltclient.tests import utils

fixtures = {
    '/v1/members/heartbeat': {
        'PUT': (
            {},
            {
                'next_beat': '10',
                'change': (
                    'peer1', 'peer2'
                )
            }
        )
    }
}


class MemberManagerTest(testtools.TestCase):

    def setUp(self):
        super(MemberManagerTest, self).setUp()
        self.api = utils.FakeAPI(fixtures)
        self.mgr = members.MemberManager(self.api)

    def test_heartbeat(self):
        test_info = self.mgr.heartbeat(
            host='localhost'
        )
        expect = [
            (
                'PUT',
                '/v1/members/heartbeat',
                {},
                {
                    'host': 'localhost'
                }
            )
        ]
        self.assertEqual(self.api.calls, expect)
        self.assertEqual(test_info.next_beat, '10')
        self.assertEqual(len(test_info.change), 2)
