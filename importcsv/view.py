import csv
from .models import CSVSource
from django.views import View
from django.http import JsonResponse
from rest_framework.generics import ListAPIView
from .serializer import CSVSerializer
from rest_framework.pagination import PageNumberPagination
from user.permissions import Administrator, Tenant


class CSVSourceView(View):
    def get(self, request):
        with open('newfile.csv', 'r') as file:
            file_data = csv.reader(file)
            list_of_dict = list(file_data)
            objs = [
                CSVSource(
                    brand=row[2],
                    manufacturer=row[10],
                    name=row[12],
                    reviews=row[18],
                    text_reviews=row[19],
                    review_title=row[20],
                    reviews_username=row[23],
                    weight=row[26]
                )
                for row in list_of_dict
            ]

            try:
                msg = CSVSource.objects.bulk_create(objs)
                returnmsg = {'status code': 200}

            except Exception as e:
                returnmsg = {'status code': 500,
                             "message": "Error while importing file"}

            return JsonResponse(returnmsg)


class CSVView(ListAPIView):
    queryset = CSVSource.objects.all().order_by('id')
    serializer_class = CSVSerializer
    pagination_class = PageNumberPagination
    permission_classes = [Administrator, Tenant]
































