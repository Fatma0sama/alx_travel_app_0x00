from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth import get_user_model
import random

User = get_user_model()

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **options):
        users = User.objects.all()
        if not users:
            self.stdout.write(self.style.WARNING("No users found to assign listings"))
            return

        for i in range(10):
            Listing.objects.create(
                title=f"Sample Listing {i+1}",
                description="This is a sample description.",
                price=random.randint(50, 500),
                host=random.choice(users)
            )
        self.stdout.write(self.style.SUCCESS("Successfully seeded 10 listings"))
