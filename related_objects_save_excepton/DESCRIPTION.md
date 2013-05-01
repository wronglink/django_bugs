I create 2 model related objects:

```pycon
>>> from related_objects_save_excepton.models import *
>>> a = A()
>>> b = B()
>>> b.a = a
>>> a.save()
```

After that I expect that calling `b.save()` would be successfully executed. But ORM throws an exception: 

```pycon
>>> b.save()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "/Users/wronglink/.virtualenvs/djtest/lib/python2.7/site-packages/django/db/models/base.py", line 532, in save
    force_update=force_update, update_fields=update_fields)
  File "/Users/wronglink/.virtualenvs/djtest/lib/python2.7/site-packages/django/db/models/base.py", line 627, in save_base
    result = manager._insert([self], fields=fields, return_id=update_pk, using=using, raw=raw)
  File "/Users/wronglink/.virtualenvs/djtest/lib/python2.7/site-packages/django/db/models/manager.py", line 215, in _insert
    return insert_query(self.model, objs, fields, **kwargs)
  File "/Users/wronglink/.virtualenvs/djtest/lib/python2.7/site-packages/django/db/models/query.py", line 1660, in insert_query
    return query.get_compiler(using=using).execute_sql(return_id)
  File "/Users/wronglink/.virtualenvs/djtest/lib/python2.7/site-packages/django/db/models/sql/compiler.py", line 889, in execute_sql
    cursor.execute(sql, params)
  File "/Users/wronglink/.virtualenvs/djtest/lib/python2.7/site-packages/django/db/backends/util.py", line 41, in execute
    return self.cursor.execute(sql, params)
  File "/Users/wronglink/.virtualenvs/djtest/lib/python2.7/site-packages/django/db/backends/mysql/base.py", line 127, in execute
    six.reraise(utils.IntegrityError, utils.IntegrityError(*tuple(e.args)), sys.exc_info()[2])
  File "/Users/wronglink/.virtualenvs/djtest/lib/python2.7/site-packages/django/db/backends/mysql/base.py", line 120, in execute
    return self.cursor.execute(query, args)
  File "/Users/wronglink/.virtualenvs/djtest/lib/python2.7/site-packages/MySQLdb/cursors.py", line 174, in execute
    self.errorhandler(self, exc, value)
  File "/Users/wronglink/.virtualenvs/djtest/lib/python2.7/site-packages/MySQLdb/connections.py", line 36, in defaulterrorhandler
    raise errorclass, errorvalue
IntegrityError: (1048, "Column 'a_id' cannot be null")
```
