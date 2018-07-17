========================
Team and repository tags
========================

.. image:: http://governance.openstack.org/badges/tempest-horizon.svg
    :target: http://governance.openstack.org/reference/tags/index.html

.. Change things from this point on

===============================
tempest-horizon
===============================

Tempest Plugin for Horizon tests

* Free software: Apache license

Using
--------
Install this plugin in the same python environment as tempest.

In tempest directory, run::

  stestr run tempest_horizon.tests.scenario.test_dashboard_basic_ops.TestDashboardBasicOps
