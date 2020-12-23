'''Functions to execute on different URLs'''
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from real_estate import models
from real_estate.models import *
from django.shortcuts import render
from real_estate.forms import ToFromForm, AddListingForm

@csrf_exempt
def list_items(request):
    #print(request.method)
    if request.method == "GET":

        if request.GET.get('csrfmiddlewaretoken', '') != "": # if request has get parameters
            form = ToFromForm(request.GET)
            if form.is_valid():
                all_items = Listing.objects.all()
                from_val = request.GET.get('from_field', '') # price choices
                to_val = request.GET.get('to_field', '')
                # if from value is bigger than to value, switch them
                if from_val != '' and to_val != '':
                    if int(from_val) > int(to_val):

                        c = to_val
                        to_val = from_val
                        from_val = c

                region = request.GET.getlist('region_choice', '') # multiple choices of regions
                type_choice = request.GET.getlist('type_choice', '') # choices for type of real_estate
                sale_type_choice = request.GET.get('sale_type_choice', '')
                size = request.GET.get('size', '')
                print(region, type_choice, sale_type_choice, size)

                region_choice = list(map(int, region))
                type_choice = list(map(int, type_choice))
                sale_type_choice = list(sale_type_choice)
                if size != 500 and size!='':
                    size_list = list(map(int, size.split('x')))
                elif size==500:
                    size_list = [500]
                else:
                    size_list = []

                print(from_val, to_val, region_choice, type_choice, size_list, sale_type_choice)


                '''Filtering items in database according to chosen options'''
                # filtering by from-to
                if from_val != '':
                    all_items = Listing.objects.filter(price__gt=from_val)

                if to_val != '':
                    all_items = all_items.filter(price__lt=to_val)

                # filtering by size
                if len(size_list) == 2:
                    st = size_list[0]
                    end = size_list[1]
                    all_items = all_items.filter(square_footage__gt=st)
                    all_items = all_items.filter(square_footage__lt=end)
                elif size_list == [500]:
                    all_items = all_items.filter(square_footage__gt=500)



                # filtering by region, if it exists
                if region_choice != []:
                    all_items = all_items.filter(region_id__in = region_choice)

                # filtering by type if t exists
                if type_choice != []:
                    all_items = all_items.filter(listing_type_id__in = type_choice)

                # filtering by sale type
                if sale_type_choice != [] and sale_type_choice != ['3']:
                    all_items = all_items.filter(sale_type_id = int(sale_type_choice[0]))



                # print('next', all_items)
                # print(request.GET.get)
                form = form
                # print(form)
                context = {'items': all_items, 'form': form}
                return render(request, "homepage.html", context=context)
        else:  # if request does not have get parameters, such as initial page load
            all_items = Listing.objects.all()
            # print("not valid")
            form = ToFromForm()
            context = {'items': all_items, 'form': form}
            return render(request, "homepage.html", context=context)

    '''Handling request to delete listing'''
    if request.method == "POST" and request.is_ajax():
        id_del = int(request.POST['id'])
        print(id_del)
        listing_to_delete = Listing.objects.filter(id=id_del)
        print(listing_to_delete)
        listing_to_delete.delete()
        return HttpResponse("Success")

def add_listing(request):
    if request.method == "POST":
        form = AddListingForm(request.POST)
        if form.is_valid(): # saving listing to database
            title = form.cleaned_data['title']
            region = form.cleaned_data['region_choice']
            listing_type = form.cleaned_data['type_choice']
            sale_type = form.cleaned_data['sale_type_choice']
            size = form.cleaned_data['size']
            nu_rooms = form.cleaned_data['nu_rooms']
            price = form.cleaned_data['price']
            print(form.cleaned_data['nu_rooms'], 'nu_ rooms')

            region_foreign_key = Region.objects.get(id=int(region))
            listing_type_key = ListingType.objects.get(id=int(listing_type))
            sale_type_key = SaleType.objects.get(id = int(sale_type))

            listing = Listing(title=title, region=region_foreign_key, listing_type=listing_type_key, sale_type=sale_type_key, square_footage=size, price=price, nu_rooms=nu_rooms)
            listing.save()


            return render(request, 'dodaj-oglas.html', context={'form': form, 'message': 'Oglas je bil uspešno dodan v bazo!'})

        return render(request, 'dodaj-oglas.html', context={'form':form})
    else:
        form = AddListingForm()
        return render(request, 'dodaj-oglas.html', context={'form': form})



