from django.db import models

class Truck(models.Model):
    MODEL = (
        ('Scania','Scania'),
        ('Mercedes','Mercedes'),
        ('Volvo','Volvo'),
        ('DAF','DAF'),
        ('MAN','MAN'),
    )
    model = models.CharField(max_length=20,choices=MODEL)
    name = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    clutch = models.CharField(max_length=100)
    front_axle = models.CharField(max_length=100)
    front_suspension = models.CharField(max_length=100)
    rear_suspension = models.CharField(max_length=100)
    brakes = models.CharField(max_length=100)
    chassis = models.CharField(max_length=100)
    dimension = models.CharField(max_length=100)    
    cabin_specs = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    main_photo = models.ImageField()
    photo1 = models.ImageField()
    photo2 = models.ImageField(null = True)
    photo3 = models.ImageField(null = True)

    def __str__(self):
        return self.name
        
