#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-
#
# win_role - Windows Role label discovery
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

from pathlib import Path
from typing import Any

from cmk.base.cee.plugins.bakery.bakery_api.v1 import FileGenerator, OS, Plugin, register


def get_win_role(conf: Any) -> FileGenerator:
    yield Plugin(base_os=OS.WINDOWS, source=Path('win_role.ps1'))


register.bakery_plugin(
    name='win_role',
    files_function=get_win_role,
)
