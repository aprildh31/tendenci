from __future__ import print_function
from django.conf import settings
from django.utils.translation import ugettext_noop as _
from django.db.models.signals import post_migrate

if "tendenci.apps.notifications" in settings.INSTALLED_APPS:
    from tendenci.apps.notifications import models as notification

    def create_notice_types(app, verbosity, **kwargs):
        notification.create_notice_type("directory_added", _("Directory Added"), _("A directory has been added."), verbosity=verbosity)
        notification.create_notice_type("directory_approved_user_notice", _("Directory Approved User Notice"), _("A directory has been approved - user notice."), verbosity=verbosity)
        #notification.create_notice_type("directory_edited", _("Directory Edited"), _("A directory has been edited."), verbosity=verbosity)
        notification.create_notice_type("directory_deleted", _("Directory Deleted"), _("A directory has been deleted"), verbosity=verbosity)
        notification.create_notice_type("directory_renewed", _("Directory Renewed"), _("A directory has been renewed"), verbosity=verbosity)
        notification.create_notice_type("directory_renewal_eligible", _("Directory Eligible for Renewal"), _("A directory is eligible for renewal"), verbosity=verbosity)

    post_migrate.connect(create_notice_types, sender=notification)
else:
    print("Directories: Skipping creation of NoticeTypes as notification app not found")
