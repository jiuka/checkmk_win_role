#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
#
# win_role - Windows Role label discovery
#
# Copyright (C) 2021  Marius Rieder <marius.rieder@durchmesser.ch>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from typing import Dict

from .agent_based_api.v1.type_defs import HostLabelGenerator
from .agent_based_api.v1 import HostLabel, register


def win_role_host_labels(section: Dict) -> HostLabelGenerator:
    for role in section:
        yield HostLabel(f'win_role/{role[0]}', u'installed')


register.agent_section(
    name='win_role',
    host_label_function=win_role_host_labels,
)
