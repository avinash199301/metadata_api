from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from unittest.mock import patch
from .models import Location, Department, Category, SubCategory, SKU

class MetadataAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.location = Location.objects.create(name="Perimeter")
        self.department = Department.objects.create(name="Bakery", location=self.location)
        self.category = Category.objects.create(name="Bakery Bread", department=self.department)
        self.subcategory = SubCategory.objects.create(name="Bagels", category=self.category)
        self.sku = SKU.objects.create(name="SKUDESC1", location=self.location, department=self.department, category=self.category, subcategory=self.subcategory)

    # Test Location API
    def test_create_location(self):
        data = {'name': 'New Location'}
        response = self.client.post('/api/v1/location/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Location.objects.count(), 2)

    def test_get_location_list(self):
        response = self.client.get('/api/v1/location/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_location_detail(self):
        response = self.client.get('/api/v1/location/{}/'.format(self.location.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Perimeter')

    def test_update_location(self):
        data = {'name': 'Updated Location'}
        response = self.client.put('/api/v1/location/{}/'.format(self.location.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.location.refresh_from_db()
        self.assertEqual(self.location.name, 'Updated Location')

    def test_delete_location(self):
        response = self.client.delete('/api/v1/location/{}/'.format(self.location.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Location.objects.count(), 0)


    # Test Department API
    def test_create_department(self):
        data = {'name': 'New Department', 'location': self.location.id}
        response = self.client.post('/api/v1/location/{}/department/'.format(self.location.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Department.objects.count(), 2)

    def test_get_department_list(self):
        response = self.client.get('/api/v1/location/{}/department/'.format(self.location.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_department_detail(self):
        response = self.client.get('/api/v1/location/{}/department/{}/'.format(self.location.id, self.department.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Bakery')

    def test_update_department(self):
        data = {'name': 'Updated Department'}
        response = self.client.put('/api/v1/location/{}/department/{}/'.format(self.location.id, self.department.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.department.refresh_from_db()
        self.assertEqual(self.department.name, 'Updated Department')

    def test_delete_department(self):
        response = self.client.delete('/api/v1/location/{}/department/{}/'.format(self.location.id, self.department.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Department.objects.count(), 0)

    # Test Category API
    def test_create_category(self):
        data = {'name': 'New Category', 'department': self.department.id}
        response = self.client.post('/api/v1/location/{}/department/{}/category/'.format(self.location.id, self.department.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)

    def test_get_category_list(self):
        response = self.client.get('/api/v1/location/{}/department/{}/category/'.format(self.location.id, self.department.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_category_detail(self):
        response = self.client.get('/api/v1/location/{}/department/{}/category/{}/'.format(self.location.id, self.department.id, self.category.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Bakery Bread')

    def test_update_category(self):
        data = {'name': 'Updated Category'}
        response = self.client.put('/api/v1/location/{}/department/{}/category/{}/'.format(self.location.id, self.department.id, self.category.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category.refresh_from_db()
        self.assertEqual(self.category.name, 'Updated Category')

    def test_delete_category(self):
        response = self.client.delete('/api/v1/location/{}/department/{}/category/{}/'.format(self.location.id, self.department.id, self.category.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)

    # Test SubCategory API
    def test_create_subcategory(self):
        data = {'name': 'New SubCategory', 'category': self.category.id}
        response = self.client.post('/api/v1/location/{}/department/{}/category/{}/subcategory/'.format(self.location.id, self.department.id, self.category.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SubCategory.objects.count(), 2)

    def test_get_subcategory_list(self):
        response = self.client.get('/api/v1/location/{}/department/{}/category/{}/subcategory/'.format(self.location.id, self.department.id, self.category.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_subcategory_detail(self):
        response = self.client.get('/api/v1/location/{}/department/{}/category/{}/subcategory/{}/'.format(self.location.id, self.department.id, self.category.id, self.subcategory.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Bagels')

    def test_update_subcategory(self):
        data = {'name': 'Updated SubCategory'}
        response = self.client.put('/api/v1/location/{}/department/{}/category/{}/subcategory/{}/'.format(self.location.id, self.department.id, self.category.id, self.subcategory.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.subcategory.refresh_from_db()
        self.assertEqual(self.subcategory.name, 'Updated SubCategory')

    def test_delete_subcategory(self):
        response = self.client.delete('/api/v1/location/{}/department/{}/category/{}/subcategory/{}/'.format(self.location.id, self.department.id, self.category.id, self.subcategory.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(SubCategory.objects.count(), 0)

    # Test SKU API
    def test_create_sku(self):
        data = {'name': 'New SKU', 'location': self.location.id, 'department': self.department.id, 'category': self.category.id, 'subcategory': self.subcategory.id}
        response = self.client.post('/api/v1/location/{}/department/{}/category/{}/subcategory/{}/sku/'.format(self.location.id, self.department.id, self.category.id, self.subcategory.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SKU.objects.count(), 2)

    def test_get_sku_list(self):
        response = self.client.get('/api/v1/location/{}/department/{}/category/{}/subcategory/{}/sku/'.format(self.location.id, self.department.id, self.category.id, self.subcategory.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_sku_detail(self):
        response = self.client.get('/api/v1/location/{}/department/{}/category/{}/subcategory/{}/sku/{}/'.format(self.location.id, self.department.id, self.category.id, self.subcategory.id, self.sku.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'SKUDESC1')

    def test_update_sku(self):
        data = {'name': 'Updated SKU'}
        response = self.client.put('/api/v1/location/{}/department/{}/category/{}/subcategory/{}/sku/{}/'.format(self.location.id, self.department.id, self.category.id, self.subcategory.id, self.sku.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.sku.refresh_from_db()
        self.assertEqual(self.sku.name, 'Updated SKU')

    def test_delete_sku(self):
        response = self.client.delete('/api/v1/location/{}/department/{}/category/{}/subcategory/{}/sku/{}/'.format(self.location.id, self.department.id, self.category.id, self.subcategory.id, self.sku.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(SKU.objects.count(), 0)


from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Location


class LocationListTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_location(self):
        # Define the data for creating a new Location
        data = {
            'name': 'Test Location'
        }

        # Send a POST request to create a new Location
        response = self.client.post('/api/v1/location/', data, format='json')

        # Assert that the response status code is 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the Location's description matches the data sent in the request
        self.assertEqual(Location.objects.get().name, 'Test Location')

    def test_get_all_locations(self):
        # Create some sample Location objects
        Location.objects.create(name='Location 1')
        Location.objects.create(name='Location 2')

        # Send a GET request to retrieve all locations
        response = self.client.get('/api/v1/location/')

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the response contains the expected number of Location objects
        self.assertEqual(len(response.data), 2)

    def test_get_nonexistent_location(self):
        # Send a GET request for a Location that does not exist
        response = self.client.get('/api/v1/location/999/')

        # Assert that the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_location(self):
        # Create a sample Location
        location = Location.objects.create(description='Location 1')

        # Define the data for updating the Location
        updated_data = {
            'description': 'Updated Location'
        }

        # Send a PUT request to update the Location
        response = self.client.put(f'/api/v1/location/{location.pk}/', updated_data, format='json')

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Reload the Location from the database and assert that it has been updated
        location.refresh_from_db()
        self.assertEqual(location.description, 'Updated Location')

    def test_delete_location(self):
        # Create a sample Location
        location = Location.objects.create(description='Location 1')

        # Send a DELETE request to delete the Location
        response = self.client.delete(f'/api/v1/location/{location.pk}/')

        # Assert that the response status code is 204 (No Content)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Assert that the Location has been deleted from the database
        self.assertEqual(Location.objects.count(), 0)


