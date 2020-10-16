from django.shortcuts import render, redirect
from map.models import MapData
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# Create your views here.
def Map(request):   
    if request.method == "POST":
        store_name = request.POST['store_name']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        phone = request.POST['phone']
        lat = request.POST['lat']
        lon = request.POST['lon']

        MapData.objects.create(store_name=store_name, address=address,city=city,state=state,zipcode=zipcode,phone=phone,lat=lat,lon=lon)

        locations = MapData.objects.all().order_by('store_name')
        data = []
        for store in locations:
            data.append({
                "store_name":store.store_name,
                "address":store.address,
                "city":store.city,
                "state":store.state,
                "zipcode":store.zipcode,
                "phone":store.phone,
                "coordinates" : {"lat":f"{store.lat}", "lon":f"{store.lon}"},
                "addressLines" : [f"{store.address}", f"{store.city}, {store.state} {store.zipcode}"]
                })
            
        json_data = json.dumps(data, indent=4)
        json_file = BASE_DIR / "static/js/store_data.json"
        with open(json_file, "w") as outfile:
            outfile.write(json_data)

        return render(request, 'googlemap.html')

    else:

        return render(request, 'googlemap.html')

def dataDelete(request):
    MapData.objects.last().delete()
    return redirect('/map/google/')