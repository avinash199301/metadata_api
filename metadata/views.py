from .models import Location, Department, Category, SubCategory, SKU
from .serializers import (
    LocationSerializer,
    DepartmentSerializer,
    CategorySerializer,
    SubCategorySerializer,
    SKUSerializer,
)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class LocationList(APIView):
    def get(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LocationDetail(APIView):
    def get_object(self, location_id):
        try:
            return Location.objects.get(pk=location_id)
        except Location.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, location_id):
        location = self.get_object(location_id)
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    def put(self, request, location_id):
        location = self.get_object(location_id)
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, location_id):
        location = self.get_object(location_id)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DepartmentList(APIView):
    def get(self, request, location_id):
        departments = Department.objects.filter(location=location_id)
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    def post(self, request, location_id):
        request.data['location'] = location_id  # Set the location for the new department
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartmentDetail(APIView):
    def get_object(self, location_id, department_id):
        try:
            return Department.objects.get(location=location_id, department_id=department_id)
        except Department.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, location_id, department_id):
        department = self.get_object(location_id, department_id)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

    def put(self, request, location_id, department_id):
        department = self.get_object(location_id, department_id)
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, location_id, department_id):
        department = self.get_object(location_id, department_id)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryList(APIView):
    def get(self, request, location_id, department_id):
        categories = Category.objects.filter(department=department_id)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, location_id, department_id):
        request.data['department'] = department_id  # Set the department for the new category
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetail(APIView):
    def get_object(self, department_id, category_id):
        try:
            return Category.objects.get(department=department_id, category_id=category_id)
        except Category.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, location_id, department_id, category_id):
        category = self.get_object(department_id, category_id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request,location_id, department_id, category_id):
        category = self.get_object(department_id, category_id)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, location_id, department_id, category_id):
        category = self.get_object(department_id, category_id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubcategoryList(APIView):
    def get(self, request, location_id, department_id, category_id):
        subcategories = SubCategory.objects.filter(category=category_id)
        serializer = SubCategorySerializer(subcategories, many=True)
        return Response(serializer.data)

    def post(self, request, location_id, department_id, category_id):
        request.data['category'] = category_id  # Set the category for the new subcategory
        serializer = SubCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubcategoryDetail(APIView):
    def get_object(self, category_id, subcategory_id):
        try:
            return SubCategory.objects.get(category=category_id, subcategory_id=subcategory_id)
        except SubCategory.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, location_id, department_id, category_id, subcategory_id):
        subcategory = self.get_object(category_id, subcategory_id)
        serializer = SubCategorySerializer(subcategory)
        return Response(serializer.data)

    def put(self, request, location_id, department_id, category_id, subcategory_id):
        subcategory = self.get_object(category_id, subcategory_id)
        serializer = SubCategorySerializer(subcategory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, location_id, department_id, category_id, subcategory_id):
        subcategory = self.get_object(category_id, subcategory_id)
        subcategory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SKUSearch(APIView):
    def post(self, request):
        metadata = request.data
        try:
            # Query the database for SKUs based on the metadata
            skus = SKU.objects.filter(
                location__description=metadata['location'],
                department__description=metadata['department'],
                category__description=metadata['category'],
                subcategory__description=metadata['subcategory']
            )
            serializer = SKUSerializer(skus, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'An error occurred while searching for SKUs.'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)



