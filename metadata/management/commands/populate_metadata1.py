import csv
from django.core.management.base import BaseCommand
from metadata.models import Location, Department, Category, SubCategory, SKU

class Command(BaseCommand):
    help = 'Populate the database with data from CSV'

    def handle(self, *args, **options):
        csv_file = r'C:\Users\avina\PycharmProjects\pythonProject\metadata_api\metadata\management\commands\csvfiles\metadata.csv'

        try:
            with open(csv_file, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                for row in reader:
                    location_description, department_description, category_description, subcategory_description = row
                    print(f"{location_description}, {department_description}, {category_description}, {subcategory_description}")
                    # Create or get Location
                    location, created = Location.objects.get_or_create(description=location_description)

                    # Create or get Department using department_description
                    department, created = Department.objects.get_or_create(description=department_description, location=location)

                    # Create or get Category
                    category, created = Category.objects.get_or_create(description=category_description, department=department)

                    # Create or get SubCategory
                    subcategory, created = SubCategory.objects.get_or_create(description=subcategory_description, category=category)

                    # Create SKU
                    SKU.objects.create(
                        name=f'SKUDESC-{len(SKU.objects.all()) + 1}',
                        location=location,
                        department=department,
                        category=category,
                        subcategory=subcategory
                    )

        except FileNotFoundError as e:
            print(f"File not found {csv_file} with {e}")
