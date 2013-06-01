from django.utils.translation import ugettext_lazy as _
from admin_tools.dashboard import modules, Dashboard


class PhillyDashboard(Dashboard):
    columns = 3

    def __init__(self, **kwargs):

        self.children = self.children or []

        self.children.append(modules.ModelList(
            title=_('Site Content'),
            models=(
                'elephantblog.*',
                'feincms.module.page.*',
                'pathways.*',
            ),
        ))

        self.children.append(modules.ModelList(
            title=_('Lots'),
            models=(
                'lots.*',
            ),
        ))

        self.children.append(modules.ModelList(
            title=_('Organize'),
            models=(
                'phillyorganize.*',
            ),
        ))

        self.children.append(modules.AppList(
            title=_('Applications'),
            exclude=(
                'django.contrib.*',
                'elephantblog.*',
                'feincms.module.page.*',
                'phillydata.*',
                'libapps.content.*',
                'lots.*',
            ),
        ))

        self.children.append(modules.ModelList(
            title=_('Lot Content'),
            models=('libapps.content.*',),
        ))

        self.children.append(modules.AppList(
            title=_('Data'),
            models=('phillydata.*',),
        ))

        self.children.append(modules.AppList(
            title=_('Administration'),
            models=('django.contrib.*',),
        ))

        self.children.append(modules.RecentActions(
            title=_('Recent Actions'),
            limit=5
        ))