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

from voltclient.common import base
from voltclient.v1.volumes import Volume


class Member(base.Resource):
    def __repr__(self):
        return "<Member %s>" % self._info

    @property
    def id(self):
        return self.member_id

    def delete(self):
        self.manager.delete(self)


class MemberManager(base.Manager):
    resource_class = Member

    def heartbeat(self):
        """Send heartbeat message to volt
        and receive hint information.

        :param host: the host name of this server
        :rtype: :class:`Image`
        """
        url = '/v1/members/heartbeat'

        _, body_iter = self.api.raw_request('PUT', url)

        info = eval(''.join([c for c in body_iter]))

        print info

        host_info = []
        for volume in info:
            parents_list = []
            for parent in volume['parents']:
                parents_list.append(Volume(self, parent))
            host_info.append(
                {
                    'peer_id': volume['peer_id'],
                    'parents': parents_list,
                }
            )

        return host_info