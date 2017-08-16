from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from spacemap.models import StarSystem
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
            action='store',
            dest='flush',
            default='n',
            help='Flush existing stars? [y/n]',
        )

    def handle(self, *args, **options): 

        def getStarName():
            names = ['ACAMAR', 'ACHERNAR', 'Achird', 'ACRUX', 'Acubens', 'ADARA', 'Adhafera', 'Adhil', 'AGENA', 'Ain al Rami', 'Ain', 'Al Anz', 'Al Kalb al Rai', 'Al Minliar al Asad', 'Al Minliar al Shuja', 'Aladfar', 'Alathfar', 'Albaldah', 'Albali', 'ALBIREO', 'Alchiba', 'ALCOR', 'ALCYONE', 'ALDEBARAN', 'ALDERAMIN', 'Aldhibah', 'Alfecca Meridiana', 'Alfirk', 'ALGENIB', 'ALGIEBA', 'ALGOL', 'Algorab', 'ALHENA', 'ALIOTH', 'ALKAID', 'Alkalurops', 'Alkes', 'Alkurhah', 'ALMAAK', 'ALNAIR', 'ALNATH', 'ALNILAM', 'ALNITAK', 'Alniyat', 'Alniyat', 'ALPHARD', 'ALPHEKKA', 'ALPHERATZ', 'Alrai', 'Alrisha', 'Alsafi', 'Alsciaukat', 'ALSHAIN', 'Alshat', 'Alsuhail', 'ALTAIR', 'Altarf', 'Alterf', 'Aludra', 'Alula Australis', 'Alula Borealis', 'Alya', 'Alzirr', 'Ancha', 'Angetenar', 'ANKAA', 'Anser', 'ANTARES', 'ARCTURUS', 'Arkab Posterior', 'Arkab Prior', 'ARNEB', 'Arrakis', 'Ascella', 'Asellus Australis', 'Asellus Borealis', 'Asellus Primus', 'Asellus Secondus', 'Asellus Tertius', 'Asterope', 'Atik', 'Atlas', 'Auva', 'Avior', 'Azelfafage', 'Azha', 'Azmidiske', 'Baham', 'Baten Kaitos', 'Becrux', 'Beid', 'BELLATRIX', 'BETELGEUSE', 'Botein', 'Brachium', 'CANOPUS', 'CAPELLA', 'Caph', 'CASTOR', 'Cebalrai', 'Celaeno', 'Chara', 'Chort', 'COR CAROLI', 'Cursa', 'Dabih', 'Deneb Algedi', 'Deneb Dulfim', 'Deneb el Okab', 'Deneb el Okab', 'Deneb Kaitos Shemali', 'DENEB', 'DENEBOLA', 'Dheneb', 'Diadem', 'DIPHDA', 'Double Double (7051)', 'Double Double (7052)', 'Double Double (7053)', 'Double Double (7054)', 'Dschubba', 'Dsiban', 'DUBHE', 'Ed Asich', 'Electra', 'ELNATH', 'ENIF', 'ETAMIN', 'FOMALHAUT', 'Fornacis', 'Fum al Samakah', 'Furud', 'Gacrux', 'Gianfar', 'Gienah Cygni', 'Gienah Ghurab', 'Gomeisa', 'Gorgonea Quarta', 'Gorgonea Secunda', 'Gorgonea Tertia', 'Graffias', 'Grafias', 'Grumium', 'HADAR', 'Haedi', 'HAMAL', 'Hassaleh', 'Head of Hydrus', 'Herschels "Garnet Star"', 'Heze', 'Hoedus II', 'Homam', 'Hyadum I', 'Hyadum II', 'IZAR', 'Jabbah', 'Kaffaljidhma', 'Kajam', 'KAUS AUSTRALIS', 'Kaus Borealis', 'Kaus Meridionalis', 'Keid', 'Kitalpha', 'KOCAB', 'Kornephoros', 'Kraz', 'Kuma', 'Lesath', 'Maasym', 'Maia', 'Marfak', 'Marfak', 'Marfic', 'Marfik', 'MARKAB', 'Matar', 'Mebsuta', 'MEGREZ', 'Meissa', 'Mekbuda', 'Menkalinan', 'MENKAR', 'Menkar', 'Menkent', 'Menkib', 'MERAK', 'Merga', 'Merope', 'Mesarthim', 'Metallah', 'Miaplacidus', 'Minkar', 'MINTAKA', 'MIRA', 'MIRACH', 'Miram', 'MIRPHAK', 'MIZAR', 'Mufrid', 'Muliphen', 'Murzim', 'Muscida', 'Muscida', 'Muscida', 'Nair al Saif', 'Naos', 'Nash', 'Nashira', 'Nekkar', 'NIHAL', 'Nodus Secundus', 'NUNKI', 'Nusakan', 'Peacock', 'PHAD', 'Phaet', 'Pherkad Minor', 'Pherkad', 'Pleione', 'Polaris Australis', 'POLARIS', 'POLLUX', 'Porrima', 'Praecipua', 'Prima Giedi', 'PROCYON', 'Propus', 'Propus', 'Propus', 'Rana', 'Ras Elased Australis', 'Ras Elased Borealis', 'RASALGETHI', 'RASALHAGUE', 'Rastaban', 'REGULUS', 'Rigel Kentaurus', 'RIGEL', 'Rijl al Awwa', 'Rotanev', 'Ruchba', 'Ruchbah', 'Rukbat', 'Sabik', 'Sadalachbia', 'SADALMELIK', 'Sadalsuud', 'Sadr', 'SAIPH', 'Salm', 'Sargas', 'Sarin', 'Sceptrum', 'SCHEAT', 'Secunda Giedi', 'Segin', 'Seginus', 'Sham', 'Sharatan', 'SHAULA', 'SHEDIR', 'Sheliak', 'SIRIUS', 'Situla', 'Skat', 'SPICA', 'Sterope II', 'Sualocin', 'Subra', 'Suhail al Muhlif', 'Sulafat', 'Syrma', 'Tabit (1543)', 'Tabit (1544)', 'Tabit (1552)', 'Tabit (1570)', 'Talitha', 'Tania Australis', 'Tania Borealis', 'TARAZED', 'Taygeta', 'Tegmen', 'Tejat Posterior', 'Terebellum', 'Terebellum', 'Terebellum', 'Terebellum', 'Thabit', 'Theemim', 'THUBAN', 'Torcularis Septentrionalis', 'Turais', 'Tyl', 'UNUKALHAI', 'VEGA', 'VINDEMIATRIX', 'Wasat', 'Wezen', 'Wezn', 'Yed Posterior', 'Yed Prior', 'Yildun', 'Zaniah', 'Zaurak', 'Zavijah', 'Zibal', 'Zosma', 'Zuben Elakrab', 'Zuben Elakribi', 'Zuben Elgenubi', 'Zuben Elschemali']
            for i in range(100):
                name = random.choice(names)
                if StarSystem.objects.filter(name=name).count() == 0:
                    break

            return name

        def getStarXY():
            safe_range = 10*StarSystem.STAR_SIZE_PX
            for i in range(100):
                x = random.randint(5, 1200)
                y = random.randint(5, 800)
                if StarSystem.objects.filter(pos_x__range=[x - safe_range, x + safe_range], \
                                             pos_y__range=[y - safe_range, y + safe_range]).count() == 0:
                    break

            return [x, y]

        colors = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

        N = int(options['stars_count'])

        if options['flush'] == 'y':
            StarSystem.objects.all().delete()

        for i in range(N):
            star_color = '#' + random.choice(colors) + random.choice(colors) + \
                            random.choice(colors) + random.choice(colors) + \
                            random.choice(colors) + random.choice(colors)

            star_x, star_y = getStarXY()

            StarSystem.objects.create(pos_x=star_x, \
                                        pos_y=star_y, \
                                        size=random.randint(5, 100), \
                                        name=getStarName(), \
                                        color=star_color, \
                                        temp=random.randint(5000, 10000),
                                        mass=random.randint(500, 10000))


        # self.stdout.write(str(StarSystem.objects.all().count()), ending='')
        # self.stdout.write(options, ending='')

        # Двигать близкие звезды без перекрытия. Задать расстояние между звездами.