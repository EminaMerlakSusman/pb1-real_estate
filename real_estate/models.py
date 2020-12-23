'''Database models that represent listings'''
from django.db import models


class Region(models.Model):
    id = models.IntegerField(primary_key=True, null=False, default=None)
    region = models.CharField(null=False, default=None,max_length=100)

    def __str__(self):
        return self.region
class SaleType(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    sale_type = models.CharField(null=False, default=None,max_length=100)
    def __str__(self):
        return self.sale_type

class ListingType(models.Model):
    id = models.IntegerField(primary_key=True, null=False, default=None)
    listing_type = models.CharField(null=False,default=None,max_length=100)

    def __str__(self):
        return self.listing_type



class Listing(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    title = models.CharField(null=False, default=None,max_length=100)
    square_footage = models.IntegerField(null=False, default=None)
    nu_rooms = models.IntegerField(null=True, default=1)
    region = models.ForeignKey(Region, on_delete=models.RESTRICT)
    listing_type = models.ForeignKey(ListingType, on_delete=models.RESTRICT)
    sale_type = models.ForeignKey(SaleType, default=None, on_delete=models.CASCADE)
    price = models.IntegerField(null=False, default=1.00)



    def __str__(self):
        listing_string = "{}, {} region, {} m2, {} rooms".format(self.title, self.region, self.square_footage, self.nu_rooms)
        return listing_string


