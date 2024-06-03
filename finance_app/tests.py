from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Company
import csv
import io

class CompanyTests(APITestCase):

    def setUp(self):
        # Pre-create a company for update, retrieve, delete tests
        Company.objects.create(symbol='AAPL', name='Apple Inc')

    def test_create_company(self):
        """
        Ensure we can create a new company object.
        """
        url = reverse('company-list')
        data = {'symbol': 'GOOGL'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  
        self.assertEqual(Company.objects.count(), 2)  # Considering one company created in setUp
        self.assertEqual(Company.objects.filter(symbol='GOOGL').exists(), True)

    def test_retrieve_company(self):
        """
        Ensure we can retrieve a company object.
        """
        url = reverse('company-detail', args=['AAPL'])  # Assuming you are using the symbol as the lookup field
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['symbol'], 'AAPL')

    def test_update_company(self):
        """
        Ensure we can update an existing company object.
        """
        url = reverse('company-detail', args=['AAPL'])
        updated_data = {'name': 'Apple Inc. Updated'}
        
        response = self.client.put(url, updated_data, format='json')
        

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Company.objects.get(symbol='AAPL').name, 'Apple Inc. Updated')

    def test_delete_company(self):
        """
        Ensure we can delete a company object.
        """
        url = reverse('company-detail', args=['AAPL'])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Company.objects.filter(symbol='AAPL').exists(), False)

    def test_list_companies(self):
        """
        Ensure we can retrieve all companies.
        """
        url = reverse('company-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Assuming pagination is not setup, otherwise adjust the expected count
        self.assertEqual(len(response.data), 1)  # Only one company exists after setUp

    def test_export_companies(self):
        """
        Ensure we can export companies to a CSV file.
        """
        url = reverse('export-companies')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'text/csv')

        # Read the content of the response to validate CSV data
        content = response.content.decode('utf-8')
        csv_reader = csv.reader(io.StringIO(content))
        header = next(csv_reader)
        self.assertEqual(header, ['Symbol', 'Name', 'Last Fetch'])
        data = list(csv_reader)
        self.assertEqual(data[0][0], 'AAPL')  # Check if the symbol matches
        self.assertEqual(len(data), 1)  # Assuming only one company
