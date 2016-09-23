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

from oslo_config import cfg

dashboard_group = cfg.OptGroup(name="dashboard",
                               title="Dashboard options")

DashboardGroup = [
    cfg.StrOpt('dashboard_url',
               default='http://localhost/',
               help="Where the dashboard can be found"),
    cfg.StrOpt('login_url',
               default='http://localhost/auth/login/',
               help="Login page for the dashboard",
               deprecated_for_removal=True),
    cfg.BoolOpt('disable_ssl_certificate_validation',
                default=False,
                help="Set to True if using self-signed SSL certificates."),
]

# service_opt = cfg.BoolOpt(
#    'horizon', default=True,
#    help="Whether or not Horizon is expected to be available")
#
service_available_group = cfg.OptGroup(name="service_available",
                                       title="Available OpenStack Services")

ServiceAvailableGroup = [
    cfg.BoolOpt('horizon',
                default=True,
                help="Whether or not Horizon is expected to be available"),
]
