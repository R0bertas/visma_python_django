from rest_framework import viewsets
from .models import Company
from .serializers import CompanySerializer
from django.http import HttpResponse
import csv
from .models import Company
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Company
from .serializers import CompanySerializer
import yfinance as yf
from rest_framework.response import Response


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = 'symbol'

    def create(self, request, *args, **kwargs):
            symbol = request.data.get('symbol')
            stock = yf.Ticker(symbol)
            data = stock.info
            company, created = Company.objects.update_or_create(
                symbol=symbol,
                defaults={'name': data.get('longName', 'Unknown')}
            )
            return JsonResponse({'symbol': symbol, 'name': company.name, 'created': created})

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    

def export_companies(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="companies.csv"'

    writer = csv.writer(response)
    writer.writerow(['Symbol', 'Name', 'Last Fetch'])

    companies = Company.objects.all()
    for company in companies:
        writer.writerow([company.symbol, company.name, company.last_fetch])

    return response
