from django.db import models
from django.utils.translation import ugettext_lazy as _

from phillydata.owners.models import BillingAccount, Owner
from phillydata.parcels.models import Parcel
from phillydata.violations.models import Violation
from places.models import Place


class Lot(Place):

    owner = models.ForeignKey(Owner,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text=_('The owner of this lot.'),
        verbose_name=_('owner'),
    )
    billing_account = models.ForeignKey(BillingAccount,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text=_("The owner's billing account for this lot."),
        verbose_name=_('billing account'),
    )
    parcel = models.ForeignKey(Parcel,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text=_('The parcel this lot is based on.'),
        verbose_name=_('parcel'),
    )
    violations = models.ManyToManyField(Violation,
        blank=True,
        null=True,
        help_text=_('The violations associated with this lot.'),
        verbose_name=_('violations'),
    )

    # TODO
    # available for purchase (public)
    # land use
    # owner
    # recent sale
    # tax delinquency (private)
    # zoning

    def __unicode__(self):
        return u'Lot (%s)' % (self.address_line1,)
