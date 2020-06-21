from django.contrib import admin

# Register your models here.


from charles import models

admin.site.register(models.Author)


from djcelery.models import (
            TaskState, WorkerState,
                PeriodicTask, IntervalSchedule, CrontabSchedule,
                )
#admin.site.register(IntervalSchedule) # 存储循环任务设置的时间
#admin.site.register(CrontabSchedule) # 存储定时任务设置的时间
#admin.site.register(PeriodicTask) # 存储任务
#admin.site.register(TaskState) # 存储任务执行状态
#admin.site.register(WorkerState) # 存储执行任务的worker
