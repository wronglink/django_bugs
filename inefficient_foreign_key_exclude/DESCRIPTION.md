I've got two basic models:

```python
class A(models.Model):
    pass

class B(models.Model):
    name = models.CharField(max_length=15)
    a = models.ForeignKey(A)
```

Now I want to select rows from table `a` that are refered from table `b` that dont have some value in collumn `name`.

Here is sample SQL I expect Django ORM to produce:

```sql
SELECT * FROM inefficient_foreign_key_exclude_a a
INNER JOIN inefficient_foreign_key_exclude_b b ON a.id = b.a_id
WHERE NOT (b.name = '123');
```

In case of `filter()` method of `django.db.models.query.QuerySet` it works as expected:

```pycon
>>> from infficient_foreign_key_exclude.models import A
>>> print A.objects.filter(b__name='123').query
SELECT `infficient_foreign_key_exclude_a`.`id` FROM `infficient_foreign_key_exclude_a`
INNER JOIN `infficient_foreign_key_exclude_b` ON (`infficient_foreign_key_exclude_a`.`id` = `infficient_foreign_key_exclude_b`.`a_id`)
WHERE `infficient_foreign_key_exclude_b`.`name` = 123
```

But if I use `exclude()` method (a negative form of `Q` object in underlaying logic) it creates a lot of unefficient SQL:
```pycon
>>> print A.objects.exclude(b__name='123').query
SELECT `infficient_foreign_key_exclude_a`.`id` FROM `infficient_foreign_key_exclude_a`
WHERE NOT ((`infficient_foreign_key_exclude_a`.`id` IN (
    SELECT U1.`a_id` FROM `infficient_foreign_key_exclude_b` U1
    WHERE (U1.`name` = 123  AND U1.`a_id` IS NOT NULL)
) AND `infficient_foreign_key_exclude_a`.`id` IS NOT NULL))
