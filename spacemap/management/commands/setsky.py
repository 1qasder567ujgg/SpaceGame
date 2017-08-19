from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from spacemap.models import StarSystem, Planet, City
import random

class Command(BaseCommand):

    help = 'Generates random sky'

    def add_arguments(self, parser):

        parser.add_argument(
            '--stars_count',
            action='store',
            dest='stars_count',
            help='Number of stars to add',
        )
        parser.add_argument(
            '--flush',
            action='store_true',
            dest='flush',
            default=False,
            help='Flush existing stars',
        )

    def handle(self, *args, **options): 

        def getStarXY():
            safe_range = int(3.5*StarSystem.STAR_SIZE_PX)
            for i in range(100):
                x = random.randint(5, 1280)
                y = random.randint(5, 650)
                if StarSystem.objects.filter(pos_x__range=[x - safe_range, x + safe_range], \
                                             pos_y__range=[y - safe_range, y + safe_range]).count() == 0:
                    break

            return [x, y]


        def getPlanetDistance(star_system):
            safe_range = int(3.5*Planet.PLANET_SIZE_PX)
            for i in range(100):
                dist = random.randint(5, 100)
                if Planet.objects.filter(star_system=star_system, 
                                             distance__range=[dist - safe_range, 
                                                            dist + safe_range]).count() == 0:
                    break

            return dist


        def getName(obj_class):
            for i in range(100):
                name = random.choice(obj_class.NAMES)
                if obj_class.objects.filter(name=name).count() == 0:
                    break

            return name


        def getWebColor():

            colors = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    
            color = '#' + random.choice(colors) + random.choice(colors) + \
                            random.choice(colors) + random.choice(colors) + \
                            random.choice(colors) + random.choice(colors)
            return color


        booleans = [True, False]
        N = int(options['stars_count'])

        if options['flush']:
            City.objects.all().delete()
            Planet.objects.all().delete()
            StarSystem.objects.all().delete()

        for _ in range(N):

            #New star
            star_x, star_y = getStarXY()
            star_system = StarSystem(pos_x=star_x, 
                                        pos_y=star_y, 
                                        size=random.randint(5, 100), 
                                        name=getName(StarSystem), 
                                        color=getWebColor(), 
                                        temp=random.randint(5000, 10000),
                                        mass=random.randint(500, 10000)
                                    )
            star_system.save()

            #New planets
            for _ in range(random.randint(1, 10)):
                planet = Planet(star_system=star_system, 
                                    inhabited=random.choice(booleans), 
                                    atmosphere=random.choice(booleans), 
                                    distance=getPlanetDistance(star_system),
                                    diameter=random.randint(1, 50),
                                    name=getName(Planet)
                                    )
                planet.save()

                #New cities
                for _ in range(random.randint(1, 5)):

                    population = random.randint(1000, 10000000)
                    if population < 100000:
                        city_status = 'Village'
                    elif population > 1000000:
                        city_status = 'Town'
                    else:
                        city_status = 'City'

                    city = City(planet=planet,
                                inhabited=random.choice(booleans),
                                shop=random.choice(booleans),
                                garage=random.choice(booleans),
                                space_port=random.choice(booleans),
                                population=population,
                                name=getName(City),
                                city_status=city_status
                                )

                    city.save()
        # self.stdout.write(str(StarSystem.objects.all().count()), ending='')
        # self.stdout.write(options, ending='')

