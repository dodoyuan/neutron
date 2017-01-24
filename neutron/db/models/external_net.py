# Copyright (c) 2013 OpenStack Foundation.
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


from neutron_lib.db import model_base
import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy import sql

from neutron.db import models_v2


class ExternalNetwork(model_base.BASEV2):
    network_id = sa.Column(sa.String(36),
                           sa.ForeignKey('networks.id', ondelete="CASCADE"),
                           primary_key=True)
    # introduced by auto-allocated-topology extension
    is_default = sa.Column(sa.Boolean(), nullable=False,
                           server_default=sql.false())
    # Add a relationship to the Network model in order to instruct
    # SQLAlchemy to eagerly load this association
    network = orm.relationship(
        models_v2.Network,
        backref=orm.backref("external", lazy='joined',
                            uselist=False, cascade='delete'))
    revises_on_change = ('network', )