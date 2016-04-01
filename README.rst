behaving.cmd
============

*behaving.cmd* is a command and file additional feature set for the
`behaving`_ testing framework for Behavior-Driven-Development,
similar to `Cucumber`_ or `lettuce`_. It focuses on command
and file interactions. *behaving.cmd* is written in Python and is based
on `behaving`_, which is based on `behave`_, and uses  `sh`_.

Please refer to *behave*'s excellent `documentation
<http://pythonhosted.org/behave/>`_ for a guide on how to use it, how
to write your custom steps and make it possible to extend *behaving*.

Right now, this project is just a proposal for how the `behave`_ community
can create independent step libraries to work well together. It adopts
the `behaving`_  Python namespace packages and layout. It has only a few steps
as a proof-of-concept, but the main idea is to get the layout and packaging
blessed by the BBDFL (Benevolent Behave Dictator for Life :-) to be
the way forward for packaging step libraries. Then the `behave`_ community
can work together without fragmentation and the havoc wrecked by entropy.

For the documentation, see the `wiki`_.

Contributing to behaving
------------------------
Please see the `Contribution Guidelines`_

.. _`Cucumber`: http://cukes.info/
.. _`lettuce`: http://lettuce.it/
.. _`behaving`: http://pypi.python.org/pypi/behaving
.. _`behave`: http://pypi.python.org/pypi/behave
.. _`sh`: http://pypi.python.org/pypi/sh
.. _`Contribution Guidelines`: https://github.com/ggozad/behaving/blob/master/CONTRIBUTING.rst
.. _`wiki`: https://github.com/lampmantech/behaving.cmd/wiki

