from django.db import models

# class Dept(models.Model):
#     deptno = models.IntegerField(db_column='DEPTNO', primary_key=True)  # Field name made lowercase.
#     dname = models.CharField(db_column='DNAME', max_length=14, blank=True, null=True)  # Field name made lowercase.
#     loc = models.CharField(db_column='LOC', max_length=13, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'DEPT'


# class Emp(models.Model):
#     empno = models.IntegerField(db_column='EMPNO', primary_key=True)  # Field name made lowercase.
#     ename = models.CharField(db_column='ENAME', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     job = models.CharField(db_column='JOB', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     mgr = models.IntegerField(db_column='MGR', blank=True, null=True)  # Field name made lowercase.
#     hiredate = models.DateField(db_column='HIREDATE', blank=True, null=True)  # Field name made lowercase.
#     sal = models.FloatField(db_column='SAL', blank=True, null=True)  # Field name made lowercase.
#     comm = models.FloatField(db_column='COMM', blank=True, null=True)  # Field name made lowercase.
#     deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DEPTNO', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP'


# class Salgrade(models.Model):
#     grade = models.IntegerField(db_column='GRADE', blank=True, null=True)  # Field name made lowercase.
#     losal = models.FloatField(db_column='LOSAL', blank=True, null=True)  # Field name made lowercase.
#     hisal = models.FloatField(db_column='HISAL', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'SALGRADE'


# class Menu(models.Model):
#     name = models.CharField(max_length=10)
#     open = models.CharField(max_length=1)
#     url = models.CharField(max_length=1000)

#     class Meta:
#         managed = False
#         db_table = 'menu'


# class Test2(models.Model):
#     peopleid = models.IntegerField(db_column='peopleId', blank=True, null=True)  # Field name made lowercase.
#     name = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'test2'


# class User(models.Model):
#     id = models.AutoField()
#     nickname = models.CharField(max_length=20)
#     phone = models.CharField(max_length=11)
#     password = models.CharField(max_length=100)
#     sex = models.CharField(max_length=1)
#     birthday = models.CharField(max_length=11)
#     type_id = models.IntegerField()
#     is_delete = models.CharField(max_length=1, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'user'


# class UserType(models.Model):
#     id = models.IntegerField()
#     label = models.CharField(max_length=10)
#     type = models.CharField(max_length=10)
#     is_delete = models.CharField(max_length=1)

#     class Meta:
#         managed = False
#         db_table = 'user_type'


class Xiaohua(models.Model):
    content = models.TextField()
    create_at = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'xiaohua'
