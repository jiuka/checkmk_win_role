#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-
#
# Copyright (C) 2021  Marius Rieder <marius.rieder@scs.ch>
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

import pytest  # type: ignore[import]
from cmk.base.plugins.agent_based.agent_based_api.v1 import (
    HostLabel
)
from cmk.base.plugins.agent_based import win_role


@pytest.mark.parametrize('string_table, result', [
    ([], []),
    (
        [
            ['FileAndStorage-Services', 'File and Storage Services'],
            ['Remote-Desktop-Services', 'Remote Desktop Services'],
            ['Web-Server', 'Web Server (IIS)'],
        ],
        [
            HostLabel('win_role/FileAndStorage-Services', 'installed'),
            HostLabel('win_role/Remote-Desktop-Services', 'installed'),
            HostLabel('win_role/Web-Server', 'installed'),
        ]
    ),
])
def test_win_role_host_labels(string_table, result):
    assert list(win_role.win_role_host_labels(string_table)) == result

