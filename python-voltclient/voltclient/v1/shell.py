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

from __future__ import print_function

import copy
import six

from voltclient.common import exception
from voltclient.common import utils
from voltclient.openstack.common import strutils
from voltclient.v1 import volumes


@utils.arg('--volume-id', metavar='<VOLUME-ID>',
           help='Filter volumes to those that have this id.')
def do_volume_list(gc, *args, **kwargs):
    """List volume you can access."""

    volumes = gc.volumes.list(**kwargs)

    columns = ['peer_id', 'host', 'port', 'iqn', 'lun']
    utils.print_list(volumes, columns)
