# coding=utf-8
from django.db import models
from datetime import datetime
from managers import ActiveManager, MPTTActiveManager
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext_lazy as _


class ActiveTimeModel(models.Model):
    is_active = models.BooleanField(_("Active"), default=True)
    ordering = models.IntegerField(_("Ordering"), default=0)
    date_added = models.DateTimeField(_("Date added"), editable=False)
    date_updated = models.DateTimeField(_("Date updated"), editable=False)

    objects = ActiveManager()

    class Meta:
        ordering = ('ordering', )
        abstract = True

    def save(self, *args, **kwargs):
        if not self.date_added:
            self.date_added = datetime.now()
        self.date_updated = datetime.now()
        super(ActiveTimeModel, self).save(*args, **kwargs)


class MPTTActiveTimeModel(MPTTModel):
    parent = TreeForeignKey('self', null=True, verbose_name=_("Parent"), blank=True, related_name='children')
    is_active = models.BooleanField(_("Active"), default=True)
    ordering = models.IntegerField(_("Ordering"), default=0)
    date_added = models.DateTimeField(_("Date added"), editable=False)
    date_updated = models.DateTimeField(_("Date updated"), editable=False)

    objects = MPTTActiveManager()

    class Meta:
        ordering = ('ordering', )
        abstract = True

    def _recurse_for_children(self, node):
        children = []
        for child in node.get_children():
            children.append(child)
            if child != self:
                children_list = self._recurse_for_children(child)
                children.extend(children_list)
        return children

    def childrens(self):
        return self._recurse_for_children(self)

    def _recurse_for_parents(self, cat_obj):
        p_list = []
        if cat_obj.parent_id:
            p = cat_obj.parent
            p_list.append(p)
            if p != self:
                more = self._recurse_for_parents(p)
                p_list.extend(more)
        if cat_obj == self and p_list:
            p_list.reverse()
        return p_list

    def parents(self):
        return self._recurse_for_parents(self)

    def children_active(self):
        return self.children.all()

    def has_active_children(self):
        return self.children_active().count() > 0

    def save(self, *args, **kwargs):
        if not self.date_added:
            self.date_added = datetime.now()
        self.date_updated = datetime.now()
        super(MPTTActiveTimeModel, self).save(*args, **kwargs)
