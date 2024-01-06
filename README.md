### REAL ESTATE MANAGEMENT SYSTEM - Django 
----------

Clone Git
----------

git clone https://github.com/Rayeesac/real_estate_django.git

Run Docker 
----------

```
cd real_estate_django/ && docker-compose -f docker-compose.yml up -d --build
```

Restore Database
---------

```
cd db/ && cat real_estate.sql | docker exec -i postgres psql -U postgres
```

Down and Up Docker
--------

```
cd ../ && docker-compose -f docker-compose.yml down && docker-compose -f docker-compose.yml up -d
```

URL List
-------------------

Here is the complete list of URL: 

1. Home - http://127.0.0.1:8000/
2. Admin Login - http://127.0.0.1:8000/admin/login
```
email : admin@realestate.com
password : admin@2024
```
3. Properties List - http://127.0.0.1:8000/properties/
4. Add Properties - http://127.0.0.1:8000/properties/add
5. Search - http://127.0.0.1:8000/property_and_unit_search/
6. Tenants List - http://127.0.0.1:8000/tenants/
7. Add Tenants - http://127.0.0.1:8000/tenants/add
