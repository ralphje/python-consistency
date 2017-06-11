==================
Naming Conventions
==================
This module uses several naming conventions. These conventions are invented,
as PEP-8_ only specifies how you should format your names (e.g. snake_case)
and not how you should actually pick your names.

We refer you to PEP-8_ for naming styles, such as when to use CamelCase or
snake_case. There are actually many violations inside the standard library
for this simple convention, e.g. ``unittest`` and ``logging`` for CamelCased
function names, and ``collections`` and ``datetime`` for lowercased class names.

.. _PEP-8: https://www.python.org/dev/peps/pep-0008/

Naming
======

* **Consistency across modules**

  Modules should be consistent with each other, e.g. ``tarfile.TarFile.add`` and
  ``zipfile.ZipFile.write`` are inconsistent.

* **Underscores between words**

  There should be underscores between different English words, e.g.
  ``http.client.HTTPConnection.getresponse`` is wrong. There are some exceptions
  listed below.

* **American English**

  A quick survey found that most of Python is currently in American English, so
  we prefer this.

Accepted single-worded names
----------------------------
The following words are accepted as single words, although the dictionary may
say otherwise. However, this also means that we always must see these words in
the form listed in this table. There's no 'sometimes' here.

=============== ===============================================================
**Name**        **Reason**
filename        Commonly used and interpreted as single word.
=============== ===============================================================

Properties
==========

* **Properties in favor of getters/setters**

  Getters and setters that are simple, e.g. no parameters in the getter and a
  single in the setter, should be a property. However, if there are
  significant side effects to the getter or the setter, that must be made
  clear to the programmer, use the function style.

* **Do not use** ``get_``

  Prefer to use the name without the ``get_`` prefix. This is in line with the
  use of properties, but also when it is a method, prefer to use it without the
  prefix. Unless you also have a setter, but then you would have used a property
  anyway.
  Conversely, ``set_`` should be avoided as well, but only if this is clear.

* ``is__`` **is a property**

  If you have a method that is simply a ``def is_foo(self):``, it is a property
  with that name.

* **Prefer using iterators, avoid** ``iter_``

  Unless you need to distinguish between iterators and lists, you should avoid
  the prefix ``iter_``. Furthermore, if your code of returning a list is simply
  ``list(iter)``, avoid that method at all. But if you have a list, return it.
  A list is iterable after all.

Files
=====

* **Avoid many methods for working on strings and bytes and file-like objects**

  Having four methods for working on a set of different inputs really does not
  look very nice. Python 3.4 introduced the notion of single-dispatch generic
  functions (see PEP-443_), so we should use those.

* **Avoid writing to a file directly**

  Avoid writing your output to a file. You need the ``io`` library to get your
  raw output. If you have useful optimizations by writing to a file instead of
  to a string, at least make it an option.

.. _PEP-443: https://www.python.org/dev/peps/pep-0443/

This module
===========

* **Low-level modules that have a higher level module are not renamed**

  We do not provide renames for modules that are low-level and a higher level
  exists. This includes, for instance, the ``os.path`` module, as you you should
  be using ``pathlib`` anyway.

* **Superseded modules are not renamed**

  We do not provide renames for obsolete modules, such as ``optparse``.

* **Builtins are not renamed**

  For now. We spotted the forbiddenfruit_ module, so there's still hope.

.. _forbiddenfruit: https://github.com/clarete/forbiddenfruit
