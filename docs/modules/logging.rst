=======
logging
=======

.. warning::

   The logging module is intended to be subclassed. We currently do not provide
   a way for this. We are working on it.


.. note::
   Only those documented in section 16.6 have been done, logging.handlers and
   logging.config are still to be done.

Renames
=======
The following renames have been made:

Logger
------
+-------------------------+---------------------------+-----------------------+
| Previous name           | New name                  | Rationale             |
+=========================+===========================+=======================+
| ``setLevel``            | ``set_level``             | CamelCasing           |
+-------------------------+---------------------------+-----------------------+
| ``isEnabledFor``        | ``is_enabled_for``        | CamelCasing           |
+-------------------------+---------------------------+-----------------------+
| ``getEffectiveLevel``   | ``effective_level``       | CamelCasing and       |
|                         | (property)                | getter should be      |
|                         |                           | property              |
+-------------------------+---------------------------+-----------------------+
| ``getChild``            | ``child``                 | CamelCasing           |
+-------------------------+---------------------------+-----------------------+
| ``addFilter``           | ``add_filter``            | CamelCasing           |
+-------------------------+---------------------------+-----------------------+
| ``removeFilter``        | ``remove_filter``         | CamelCasing           |
+-------------------------+---------------------------+-----------------------+
| ``addHandler``          | ``add_handler``           | CamelCasing           |
+-------------------------+---------------------------+-----------------------+
| ``removeHandler``       | ``remove_handler``        | CamelCasing           |
+-------------------------+---------------------------+-----------------------+
| ``findCaller``          | ``find_caller``           | CamelCasing           |
+-------------------------+---------------------------+-----------------------+
| ``makeRecord``          | ``make_record``           | CamelCasing           |
+-------------------------+---------------------------+-----------------------+
| ``hasHandlers``         | ``has_handlers``          | CamelCasing and       |
|                         | (property)                | getter should be      |
|                         |                           | property              |
+-------------------------+---------------------------+-----------------------+

Handler
-------
+-------------------------+---------------------------+-----------------------+
| Previous name           | New name                  | Rationale             |
+=========================+===========================+=======================+
| ``createLock``          | ``create_lock``           | CamelCasing           |
+-------------------------+---------------------------+-----------------------+
| ``setLevel`` / ``level``| ``level`` (property)      | setLevel was a setter |
|                         | (and ``_level``)          | for the already       |
|                         |                           | existing level        |
|                         |                           | property              |
+-------------------------+---------------------------+-----------------------+
| ``setFormatter``        | ``formatter``             | setFormatter did only |
|                         |                           | change existing       |
|                         |                           | property              |
+-------------------------+---------------------------+-----------------------+
| ``addFilter``           | ``add_filter``            | CamelCasing           |
+-------------------------+---------------------------+-----------------------+
| ``removeFilter``        | ``remove_filter``         | CamelCasing           |
+-------------------------+---------------------------+-----------------------+
| ``addHandler``          | ``add_handler``           | CamelCasing           |
+-------------------------+---------------------------+-----------------------+
| ``handleError``         | ``handle_error``          | CamelCasing           |
+-------------------------+---------------------------+-----------------------+


Formatter
---------
+-------------------------+---------------------------+-----------------------+
| Previous name           | New name                  | Rationale             |
+=========================+===========================+=======================+
| ``formatTime``          | ``format_time``           | CamelCasing           |
+-------------------------+---------------------------+-----------------------+
| ``formatException``     | ``format_exception``      | CamelCasing           |
+-------------------------+---------------------------+-----------------------+
| ``formatStack``         | ``format_stack``          | CamelCasing           |
+-------------------------+---------------------------+-----------------------+


Module-level
------------

.. note::
   This still needs a lot of work, as we actually want to change the way the
   getters and setters work. Also, last_resort does not work properly yet.

+-------------------------+---------------------------+-----------------------+
| Previous name           | New name                  | Rationale             |
+=========================+===========================+=======================+
| ``getLogger``           | ``logger``                | CamelCasing and losing|
|                         |                           | get as this is implied|
|                         |                           | by the name           |
+-------------------------+---------------------------+-----------------------+
| ``getLoggerClass``      | ``get_logger_class``      | CamelCasing and since |
|                         |                           | this is module-level, |
|                         |                           | doing properties would|
|                         |                           | be too hard           |
+-------------------------+---------------------------+-----------------------+
| ``setLoggerClass``      | ``set_logger_class``      | see above             |
+-------------------------+---------------------------+-----------------------+
| ``getLogRecordFactory`` | ``get_log_record_factory``| see above             |
+-------------------------+---------------------------+-----------------------+
| ``setLogRecordFactory`` | ``set_log_record_factory``| see above             |
+-------------------------+---------------------------+-----------------------+
| ``addLevelName``        | ``add_level_name``        | CamelCasing           |
+-------------------------+---------------------------+-----------------------+
| ``getLevelName``        | ``get_level_name``        | CamelCasing           |
+-------------------------+---------------------------+-----------------------+
| ``makeLogRecord``       | ``make_log_record``       | CamelCasing           |
+-------------------------+---------------------------+-----------------------+
| ``basicConfig``         | ``basic_config``          | CamelCasing           |
+-------------------------+---------------------------+-----------------------+
| ``lastResort``          | ``last_resort``           | CamelCasing           |
+-------------------------+---------------------------+-----------------------+
| ``captureWarnings``     | ``capture_warnings``      | CamelCasing           |
+-------------------------+---------------------------+-----------------------+
