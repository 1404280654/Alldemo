from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Link(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    title = models.CharField(verbose_name="标题", max_length=50)
    href = models.URLField(verbose_name="链接")   # 默认长度200
    status = models.PositiveIntegerField(verbose_name="状态", choices=STATUS_ITEMS, default=STATUS_NORMAL)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    owner = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)
    weight = models.PositiveIntegerField(default=1, choices=zip(range(1, 6), range(1, 6)),
                                         verbose_name="权重", help_text="权重高展示顺序靠前")

    class Meta:
        verbose_name = verbose_name_plural = "朋友链接"


class SideBar(models.Model):
    STATUS_SHOW = 1
    STATUS_HIDE = 0
    STATUS_ITEMS = (
        (STATUS_SHOW, "展示"),
        (STATUS_HIDE, "隐藏"),
    )
    SIDE_TYPE = (
        (1, 'HTML'),
        (2, '最新文章'),
        (3, '最热文章'),
        (4, "最近评论"),
    )
    title = models.CharField(verbose_name="标题", max_length=50)
    display_type = models.PositiveIntegerField(verbose_name="展示类型", default=1,
                                               choices=SIDE_TYPE)
    content = models.CharField(verbose_name="内容", max_length=500, blank=True,
                               help_text="如果设置的不是HTML类型，可为空")
    status = models.PositiveIntegerField(verbose_name="状态", default=STATUS_SHOW, choices=STATUS_ITEMS)
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = "侧边栏"


