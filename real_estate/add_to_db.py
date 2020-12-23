from real_estate.models import *
#
'''This adds default things to the database'''

for reg in open("real_estate/regions.csv", 'r', encoding='utf-8'):
    '''Adding regions, just reading them from a text file and inputting them to the db'''
    data = reg.split(";")
    id = int(data[0])
    region_t = data[1].strip()

    region_obj = Region(id = id, region = region_t)
    region_obj.save()

'''Adding listing types'''
for typ in open('real_estate/listing_types.csv', 'r', encoding='utf-8'):
    data = typ.split(';')
    id = int(data[0])
    listing_type = data[1].strip()
    type_obj = ListingType(id = id, listing_type=listing_type)
    type_obj.save()

'''Adding sale types'''
for typ in open('real_estate/sale_type.csv', 'r', encoding='utf-8'):
    data = typ.split(';')
    id = int(data[0])
    sale = data[1].strip()
    type_obj = SaleType(id = id, sale_type=sale)
    type_obj.save()



'''Adding some sample listings'''
for ltg in open('C:/Users/Emina/Desktop/icons/projects/real_estate/real_estate/listings_random.csv', 'r', encoding='utf-8'):
    data = ltg.split(';')

    listing_type_txt = data[-3].strip()

    listing_type_obj = ListingType.objects.get(listing_type=listing_type_txt)
    sale_type_txt = data[-1].strip()

    sale_obj = SaleType.objects.get(sale_type=sale_type_txt)

    if listing_type_txt in ['Posest', 'Poslovni prostor']:
        region_txt = data[3].strip()

        region_obj = Region.objects.get(region=region_txt)
        ltg_obj = Listing(id=int(data[0]), title=data[1].strip(), square_footage=int(data[2]),
                          region=region_obj, listing_type=listing_type_obj, price=data[5], sale_type = sale_obj)
        ltg_obj.save()
    else:
        region_txt = data[4].strip()

        region_obj = Region.objects.get(region=region_txt)
        ltg_obj = Listing(id=int(data[0]), title=data[1].strip(), square_footage=int(data[2]), nu_rooms=int(data[3]),
                          region=region_obj, listing_type=listing_type_obj, price=data[6], sale_type = sale_obj)
        ltg_obj.save()

