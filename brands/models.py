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
    name = models.CharField(max_length=100,null = True)
    engine = models.CharField(max_length=100,null = True,blank=True)
    clutch = models.CharField(max_length=100,null = True,blank=True)
    front_axle = models.CharField(max_length=100,null = True,blank=True)
    front_suspension = models.CharField(max_length=100,null = True,blank=True)
    rear_suspension = models.CharField(max_length=100,null = True,blank=True)
    brakes = models.CharField(max_length=100,null = True,blank=True)
    chassis = models.CharField(max_length=100,null = True,blank=True)
    dimension = models.CharField(max_length=100,null = True,blank=True)    
    cabin_specs = models.CharField(max_length=100,null = True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,blank=True)
    main_photo = models.ImageField()
    photo1 = models.ImageField(blank=True)
    photo2 = models.ImageField(null = True,blank=True)
    photo3 = models.ImageField(null = True,blank=True)

    def __str__(self):
        return self.name
        
