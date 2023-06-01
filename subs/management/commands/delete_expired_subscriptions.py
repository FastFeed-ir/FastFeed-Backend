# subs/management/commands/delete_expired_subscriptions.py

from django.core.management.base import BaseCommand
from django.utils import timezone
from subs.models import Subscription


class Command(BaseCommand):
    help = 'Deletes expired subscriptions'

    def handle(self, *args, **options):
        now = timezone.now()
        expired_subs = Subscription.objects.filter(end_date__lt=now)
        for sub in expired_subs:
            sub.delete()

        self.stdout.write(f'{len(expired_subs)} subscriptions deleted.')