from django.urls import path

from .views import (
    LocationList,
    LocationDetail,
    DepartmentList,
    DepartmentDetail,
    CategoryList,
    CategoryDetail,
    SubcategoryList,
    SubcategoryDetail,
    SKUSearch,
)

urlpatterns = [

    path('api/v1/location/', LocationList.as_view()),
    path('api/v1/location/<int:location_id>/', LocationDetail.as_view()),
    path('api/v1/location/<int:location_id>/department/', DepartmentList.as_view()),
    path('api/v1/location/<int:location_id>/department/<int:department_id>/', DepartmentDetail.as_view()),
    path('api/v1/location/<int:location_id>/department/<int:department_id>/category/',CategoryList.as_view()),
    path('api/v1/location/<int:location_id>/department/<int:department_id>/category/<int:category_id>/', CategoryDetail.as_view()),
    path('api/v1/location/<int:location_id>/department/<int:department_id>/category/<int:category_id>/subcategory/',
         SubcategoryList.as_view()),
    path('api/v1/location/<int:location_id>/department/<int:department_id>/category/<int:category_id>/subcategory/<int:subcategory_id>/',
         SubcategoryDetail.as_view()),
    path('api/v1/sku-search/', SKUSearch.as_view()),
]
