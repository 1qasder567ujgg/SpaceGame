from django.db import models
from django.urls import reverse

class StarSystem(models.Model):
    """docstring for ClassName"""
    
    STAR_SIZE_PX = 50
    NAMES = ['ACAMAR', 'ACHERNAR', 'Achird', 'ACRUX', 'Acubens', 'ADARA', 'Adhafera', 'Adhil', 'AGENA', 'Ain al Rami', 'Ain', 'Al Anz', 'Al Kalb al Rai', 'Al Minliar al Asad', 'Al Minliar al Shuja', 'Aladfar', 'Alathfar', 'Albaldah', 'Albali', 'ALBIREO', 'Alchiba', 'ALCOR', 'ALCYONE', 'ALDEBARAN', 'ALDERAMIN', 'Aldhibah', 'Alfecca Meridiana', 'Alfirk', 'ALGENIB', 'ALGIEBA', 'ALGOL', 'Algorab', 'ALHENA', 'ALIOTH', 'ALKAID', 'Alkalurops', 'Alkes', 'Alkurhah', 'ALMAAK', 'ALNAIR', 'ALNATH', 'ALNILAM', 'ALNITAK', 'Alniyat', 'Alniyat', 'ALPHARD', 'ALPHEKKA', 'ALPHERATZ', 'Alrai', 'Alrisha', 'Alsafi', 'Alsciaukat', 'ALSHAIN', 'Alshat', 'Alsuhail', 'ALTAIR', 'Altarf', 'Alterf', 'Aludra', 'Alula Australis', 'Alula Borealis', 'Alya', 'Alzirr', 'Ancha', 'Angetenar', 'ANKAA', 'Anser', 'ANTARES', 'ARCTURUS', 'Arkab Posterior', 'Arkab Prior', 'ARNEB', 'Arrakis', 'Ascella', 'Asellus Australis', 'Asellus Borealis', 'Asellus Primus', 'Asellus Secondus', 'Asellus Tertius', 'Asterope', 'Atik', 'Atlas', 'Auva', 'Avior', 'Azelfafage', 'Azha', 'Azmidiske', 'Baham', 'Baten Kaitos', 'Becrux', 'Beid', 'BELLATRIX', 'BETELGEUSE', 'Botein', 'Brachium', 'CANOPUS', 'CAPELLA', 'Caph', 'CASTOR', 'Cebalrai', 'Celaeno', 'Chara', 'Chort', 'COR CAROLI', 'Cursa', 'Dabih', 'Deneb Algedi', 'Deneb Dulfim', 'Deneb el Okab', 'Deneb el Okab', 'Deneb Kaitos Shemali', 'DENEB', 'DENEBOLA', 'Dheneb', 'Diadem', 'DIPHDA', 'Double Double (7051)', 'Double Double (7052)', 'Double Double (7053)', 'Double Double (7054)', 'Dschubba', 'Dsiban', 'DUBHE', 'Ed Asich', 'Electra', 'ELNATH', 'ENIF', 'ETAMIN', 'FOMALHAUT', 'Fornacis', 'Fum al Samakah', 'Furud', 'Gacrux', 'Gianfar', 'Gienah Cygni', 'Gienah Ghurab', 'Gomeisa', 'Gorgonea Quarta', 'Gorgonea Secunda', 'Gorgonea Tertia', 'Graffias', 'Grafias', 'Grumium', 'HADAR', 'Haedi', 'HAMAL', 'Hassaleh', 'Head of Hydrus', 'Herschels "Garnet Star"', 'Heze', 'Hoedus II', 'Homam', 'Hyadum I', 'Hyadum II', 'IZAR', 'Jabbah', 'Kaffaljidhma', 'Kajam', 'KAUS AUSTRALIS', 'Kaus Borealis', 'Kaus Meridionalis', 'Keid', 'Kitalpha', 'KOCAB', 'Kornephoros', 'Kraz', 'Kuma', 'Lesath', 'Maasym', 'Maia', 'Marfak', 'Marfak', 'Marfic', 'Marfik', 'MARKAB', 'Matar', 'Mebsuta', 'MEGREZ', 'Meissa', 'Mekbuda', 'Menkalinan', 'MENKAR', 'Menkar', 'Menkent', 'Menkib', 'MERAK', 'Merga', 'Merope', 'Mesarthim', 'Metallah', 'Miaplacidus', 'Minkar', 'MINTAKA', 'MIRA', 'MIRACH', 'Miram', 'MIRPHAK', 'MIZAR', 'Mufrid', 'Muliphen', 'Murzim', 'Muscida', 'Muscida', 'Muscida', 'Nair al Saif', 'Naos', 'Nash', 'Nashira', 'Nekkar', 'NIHAL', 'Nodus Secundus', 'NUNKI', 'Nusakan', 'Peacock', 'PHAD', 'Phaet', 'Pherkad Minor', 'Pherkad', 'Pleione', 'Polaris Australis', 'POLARIS', 'POLLUX', 'Porrima', 'Praecipua', 'Prima Giedi', 'PROCYON', 'Propus', 'Propus', 'Propus', 'Rana', 'Ras Elased Australis', 'Ras Elased Borealis', 'RASALGETHI', 'RASALHAGUE', 'Rastaban', 'REGULUS', 'Rigel Kentaurus', 'RIGEL', 'Rijl al Awwa', 'Rotanev', 'Ruchba', 'Ruchbah', 'Rukbat', 'Sabik', 'Sadalachbia', 'SADALMELIK', 'Sadalsuud', 'Sadr', 'SAIPH', 'Salm', 'Sargas', 'Sarin', 'Sceptrum', 'SCHEAT', 'Secunda Giedi', 'Segin', 'Seginus', 'Sham', 'Sharatan', 'SHAULA', 'SHEDIR', 'Sheliak', 'SIRIUS', 'Situla', 'Skat', 'SPICA', 'Sterope II', 'Sualocin', 'Subra', 'Suhail al Muhlif', 'Sulafat', 'Syrma', 'Tabit (1543)', 'Tabit (1544)', 'Tabit (1552)', 'Tabit (1570)', 'Talitha', 'Tania Australis', 'Tania Borealis', 'TARAZED', 'Taygeta', 'Tegmen', 'Tejat Posterior', 'Terebellum', 'Terebellum', 'Terebellum', 'Terebellum', 'Thabit', 'Theemim', 'THUBAN', 'Torcularis Septentrionalis', 'Turais', 'Tyl', 'UNUKALHAI', 'VEGA', 'VINDEMIATRIX', 'Wasat', 'Wezen', 'Wezn', 'Yed Posterior', 'Yed Prior', 'Yildun', 'Zaniah', 'Zaurak', 'Zavijah', 'Zibal', 'Zosma', 'Zuben Elakrab', 'Zuben Elakribi', 'Zuben Elgenubi', 'Zuben Elschemali']

    pos_x = models.IntegerField()
    pos_y = models.IntegerField(default=0)
    size = models.FloatField()
    color = models.CharField(max_length=8)
    temp = models.FloatField()
    name = models.CharField(max_length=50)
    mass = models.FloatField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("space:system_map", kwargs={"id": self.id}) 


class Planet(models.Model):
    """docstring for ClassName"""
    
    PLANET_SIZE_PX = 10
    NAMES = ['PSR B1257+12 b', 'PSR B1257+12 c', 'PSR B1257+12 d', '1RXS J160929.1-210524 b', '2M1207b', '2MASS J21402931+1625183 Ab', 'AB Pictoris b', 'Beta Pictoris b', 'CHXR 73 b', 'CT Chamaeleontis b', 'DH Tauri b', 'DP Leonis b', 'FU Tauri b', 'Fomalhaut b', 'GQ Lupi b', 'HD 203030 b', 'HN Pegasi b', 'HR 8799 b', 'HR 8799 c', 'HR 8799 d', 'Oph 162225-240515 b', 'PSR B1620-26 b', 'UScoCTIO 108 b', 'V391 Pegasi b', '2MASS J04414489+2301513 b', 'DT Virginis c', 'GSC 06214-00210 b', 'HIP 78530 b', 'HR 8799 e', 'NN Serpentis c', 'NN Serpentis d', 'SR 12 c', 'CFBDSIR J145829+101343 b', 'Kepler-19c', 'Kepler-70b', 'Kepler-70c', 'NY Virginis b', 'PSR J1719-1438 b', 'UZ Fornacis b', 'UZ Fornacis c', 'WD 0806-661 b', 'Kappa Andromedae b', 'Kepler-46c', 'RR Caeli b', 'WISE 1217+1626 b', '2MASS J01225093-2439505 b', 'DENIS-P J082303.1-491201 b', 'Gliese 504 b', 'HD 95086 b', 'HD 106906 b', 'Kepler-88c', 'ROXs 12b', 'ROXs 42Bb', 'GU Piscium b', 'HD 100546 b', 'KIC 10001893 b', 'KIC 10001893 c', 'KIC 10001893 d', 'Kepler-37e', 'Kepler-122f', 'Kepler-338e', 'Kepler-414b', 'Kepler-414c', 'Kepler-415b', 'Kepler-415c', 'Kepler-416b', 'Kepler-416c', 'Kepler-417b', 'Kepler-417c', 'Kepler-419c', '2MASS J02192210-3925225 b', '2MASS J19383260+4603591 b', '51 Eridani b', 'LkCa 15 b', 'LkCa 15 c', 'VHS 1256-1257 b', '2MASS J22362452+4751425 b', 'HR 2562 b', 'KIC 7917485 b', 'HIP 65426 b', 'MXB 1658-298 b']

    star_system = models.ForeignKey(StarSystem)
    inhabited = models.BooleanField(default=False)
    atmosphere = models.BooleanField(default=False)
    distance = models.FloatField()   
    diameter = models.FloatField()
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=8, default='#FFFFFF')

    def __str__(self):
        return self.name


class City(models.Model):

    CITY_STAUS = (
        ('Village','Village'), 
        ('Town','Town'), 
        ('City','City')
        )
    NAMES = ['Dry Gulch ', 'Aylesbury', 'Lingmell', 'Shipton', 'Mirefield', 'Haran ', 'Peatsland', 'Beckinsale', 'Elinmylly', 'Kara\'s Vale ', 'Bannockburn', 'Farnfoss', 'Lhanbryde', 'Taedmorden', 'Troutberk', 'Old Ashton ', 'Beckton', 'Kincardine', 'Narfolk', 'Bredon', 'Waeldestone', 'Tow', 'Macclesfield', 'Hogsfeet ', 'Kirekwall', 'Berkton', 'Streatham', 'Acomb', 'Bellechulish', 'Lancaster', 'isasi', 'Djele', 'Yu', 'Katalaie', 'Kimbonga', 'Selenkey', 'Mukana', 'Batangu', 'Batalagi', 'Rwe', 'Nandjale', 'Metawaie', 'Pensa', 'Bangu', 'Shanaka', 'Tshalamukombo', 'Mulamba', 'Liuba', 'Kituru', 'Kabetesa', 'Tshintsina', 'Itikala', 'Tshipanga', 'Bokongwa', 'Lokoyo', 'Giata', 'Yaliambi', 'Bokole', 'Katoka', 'Tshakosa', 'Lozi', 'Sakoi', 'Tshalu', 'Kabaya', 'Kiminania', 'Nanuyombo', 'Batenawane', 'Moini', 'Shombio', 'Banangu', 'Fwila', 'Muvuanu', 'Sibabo', 'Ifambu', 'Yanguba', 'Kibilango', 'Sekwa', 'Mubuabua', 'Muamungu', 'Delebokonde',]

    planet = models.ForeignKey(Planet)
    inhabited = models.BooleanField(default=False)
    shop = models.BooleanField(default=False)
    garage = models.BooleanField(default=False)
    space_port = models.BooleanField(default=False)
    population = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    city_status = models.CharField(max_length=10, choices=CITY_STAUS, default='Village')

    def __str__(self):
        return self.name

#TODO: Создать рандомные планеты для существующих звезд и города для планет