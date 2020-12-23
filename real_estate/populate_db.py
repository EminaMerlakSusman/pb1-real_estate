'''This generates random data, and writes it into a csv file'''
import csv
import random


with open('C:/Users/Emina/Desktop/icons/projects/real_estate/real_estate/listings_random.csv', 'w', newline='', encoding='utf-8') as csvfile:
    dbwriter = csv.writer(csvfile, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    # getting sale types
    sale_types = []
    types_file = open('C:/Users/Emina/Desktop/icons/projects/real_estate/real_estate/sale_type.csv', 'r',
                      encoding='utf-8')
    for line in types_file:
        typ = line.split(';')[1]
        sale_types.append(typ.strip())

    # getting listing type data
    listing_types = []
    types_file = open('C:/Users/Emina/Desktop/icons/projects/real_estate/real_estate/listing_types.csv', 'r', encoding='utf-8')
    for line in types_file:
        typ = line.split(';')[1]
        listing_types.append(typ.strip())

    # getting region data
    regions = []
    for line in open('C:/Users/Emina/Desktop/icons/projects/real_estate/real_estate/regions.csv', 'r', encoding='utf-8'):
        reg = line.split(';')[1]
        regions.append(reg.strip())

    # generating random values and writing them to csv file
    for i in range(100):
        id = i
        l_type = listing_types[random.randint(0, len(listing_types) - 1)]
        region = regions[random.randint(0, len(regions) - 1)]
        sale_type = sale_types[random.randint(0, len(sale_types)-1)]

        # square footage and price need to be realistic based on region and listing type
        square_footage = 0
        price = 0

        if l_type == 'Posest':
            square_footage = random.randint(300, 1500)
            sale_type = 'Prodaja'
            price = random.randint(30, 65) * square_footage


        elif l_type == 'Stanovanje':
            square_footage = random.randint(16, 120)
            if sale_type == 'Prodaja':
                price = random.randint(1000, 2500) * square_footage
            else:
                price = random.randint(5, 10) * square_footage
            nu_rooms = random.randint(1, 4)

        elif l_type == 'Hiša':
            square_footage = random.randint(70, 250)
            if sale_type == 'Prodaja':
                price = random.randint(1000, 2500) * square_footage
            else:
                price = random.randint(5, 10) * square_footage
            nu_rooms = random.randint(2, 5)

        elif l_type == 'Poslovni prostor':
            square_footage = random.randint(30, 500)
            if sale_type == 'Prodaja':
                price = random.randint(300, 700) * square_footage
            else:
                price = random.randint(10, 20) * square_footage

        elif l_type == 'Vikend':
            square_footage = random.randint(30, 130)
            price = random.randint(700, 2000) * square_footage
            nu_rooms = random.randint(1, 3)
            sale_type = 'Prodaja'

        if l_type != 'Posest' and l_type != 'Poslovni prostor':
            if l_type == 'Stanovanje':
                square_footage_str = str(nu_rooms) + "-sobno"
            elif l_type == 'Hiša':
                square_footage_str = str(nu_rooms) + "-sobna"
            elif l_type == 'Vikend':
                square_footage_str = str(nu_rooms) + "-sobni"

            title_l = [l_type, str(square_footage) + " m2", square_footage_str, region, sale_type,str(price) + "€"]

            title = (', ').join(title_l)
            dbwriter.writerow([id, title, square_footage, nu_rooms, region, l_type, price, sale_type])
        else:
            title_l = [l_type, str(square_footage) + " m2", region, sale_type, str(price) + "€"]

            title = (', ').join(title_l)
            dbwriter.writerow([id, title, str(square_footage), region, l_type, price, sale_type])

