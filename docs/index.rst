
Welcome to python-consistency's documentation!
==============================================
I love Python. But there's one thing that bothers me: inconsistent naming in
many modules in its `standard Library`_.

Some names are surprising, inconsistent across modules, or simply incorrect.
This is mostly caused by the fact tha several modules were developed before
the introduction of PEP-8_, and now we're stuck with these names in older
modules.

It has been said and discussed in the past that the stdlib is in fact
inconsistent, but fixing this has almost always been disregarded as being too
painful (after all, we don't want a new Python 3 all over again). However,
this way, we will never move away from these inconsistencies.
Perhaps this is fine, but I believe that with some effort, we can fix this
for generations to come.

This module was written based on a discussion on python-ideas_ I started in
July 2016 as an attempt to get this fixed for once and for all. Although the
core developers don't see a need to fix this at this point in time, as it
requires a lot of effort that is simply not worth the benefits, I still feel it
should be part of Python's future.

While maintaining full backwards compatibility, this module adds consistently
named aliases to modules in the standard library (as suggested in the linked
thread). This module currently is nothing more than a bunch of renames that
you can import. For instance::

    from consistency import logging

    logging.logger(__name__)

Ultimately, I feel that Python itself should provide these properly named
alternatives. The original variant should be aliased with them (or the other
way around), without defining a deprecation timeline for the original
names. This should make it possible to eventually make the stdlib
consistent, Pythonic and unsurprising.

.. _standard Library: https://docs.python.org/3/library/index.html
.. _PEP-8: https://www.python.org/dev/peps/pep-0008/
.. _python-ideas: https://mail.python.org/pipermail/python-ideas/2016-July/041210.html


.. toctree::
   :maxdepth: 2
   :caption: General

   conventions


.. toctree::
   :maxdepth: 1
   :caption: Modules
   :glob:

   modules/*


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
