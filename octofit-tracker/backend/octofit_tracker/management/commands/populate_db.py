from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data in correct order to avoid unhashable errors
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        if User.objects.exists():
            User.objects.all().delete()
        if Team.objects.exists():
            Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel)
        spiderman = User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team=marvel)
        batman = User.objects.create(email='batman@dc.com', name='Batman', team=dc)
        superman = User.objects.create(email='superman@dc.com', name='Superman', team=dc)

        # Create Activities
        Activity.objects.create(user=ironman, type='run', duration=30, calories=300, date=date(2026, 5, 13))
        Activity.objects.create(user=spiderman, type='cycle', duration=45, calories=400, date=date(2026, 5, 12))
        Activity.objects.create(user=batman, type='swim', duration=60, calories=500, date=date(2026, 5, 11))
        Activity.objects.create(user=superman, type='fly', duration=120, calories=1000, date=date(2026, 5, 10))

        # Create Workouts
        Workout.objects.create(name='Pushups', description='Do 50 pushups', difficulty='Easy')
        Workout.objects.create(name='Pullups', description='Do 20 pullups', difficulty='Medium')
        Workout.objects.create(name='Squats', description='Do 100 squats', difficulty='Hard')

        # Create Leaderboard
        Leaderboard.objects.create(user=ironman, score=150, rank=2)
        Leaderboard.objects.create(user=spiderman, score=200, rank=1)
        Leaderboard.objects.create(user=batman, score=120, rank=4)
        Leaderboard.objects.create(user=superman, score=130, rank=3)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
