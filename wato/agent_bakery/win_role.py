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
from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    DropdownChoice,
)
from cmk.gui.plugins.wato import (
    HostRulespec,
    rulespec_registry,
)

try:
    from cmk.gui.cee.plugins.wato.agent_bakery.rulespecs.utils import (
        RulespecGroupMonitoringAgentsAgentPlugins
    )
except Exception:
    RulespecGroupMonitoringAgentsAgentPlugins = None


def _valuespec_agent_config_win_role():
    return DropdownChoice(
        title=_('Windows Server Role Label Discovery'),
        help=_('This will deploy the agent plugin <tt>win_role</tt> '
               'for discovering host labels for the server roles.'),
        choices=[
            (True, _('Deploy Windows Server Role plugin')),
            (None, _('Do not deploy Windows Server Role plugin')),
        ],
    )


if RulespecGroupMonitoringAgentsAgentPlugins is not None:
    rulespec_registry.register(
        HostRulespec(
            group=RulespecGroupMonitoringAgentsAgentPlugins,
            name='agent_config:win_role',
            valuespec=_valuespec_agent_config_win_role,
        ))
