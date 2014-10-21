# -*- coding: utf-8 -*-

# Copyright (c) 2014 National University of Defense Technology.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from voltclient.common import http
from voltclient.common import utils
from voltclient.v1 import volumes
from voltclient.v1 import members


class Client(object):
    """Client for the OpenStack volt service v1 API.

    :param string endpoint: A user-supplied endpoint URL for the volt
                            service.
    :param string token: Token for authentication.
    :param integer timeout: Allows customization of the timeout for client
                            http requests. (optional)
    """

    def __init__(self, endpoint, *args, **kwargs):
        """Initialize a new client for the volt v1 API."""
        self.http_client = http.HTTPClient(utils.strip_version(endpoint),
                                           *args, **kwargs)
        self.volumes = volumes.VolumeManager(self.http_client)
        self.members = members.MemberManager(self.http_client)
