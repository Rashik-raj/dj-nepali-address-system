from nepali_address_system.addresses import Address
from nepali_address.models import Province, District, Municipality

address = Address()

all_address = address.get_all_addresses()

def migrate_addresses():
    for province_name, districts in all_address.items():
        province, _ = Province.objects.get_or_create(name = province_name)
        for district_name, municipalities in districts.items():
            district, _ = District.objects.get_or_create(name=district_name, province=province)
            for municipality_name in municipalities:
                try:
                    _, _ = Municipality.objects.get_or_create(name=municipality_name, district=district)
                except:
                    print(municipality_name)
    print("Migration complete.")

if __name__ == '__main__':
    migrate_addresses()
