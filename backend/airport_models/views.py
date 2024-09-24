from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Airline, Aircraft
from .serializers import AirlineSerializer, AircraftSerializer
from django.http import Http404

# Utility function to handle 404 errors
def get_object_or_404(model, pk):
    try:
        return model.objects.get(pk=pk)
    except model.DoesNotExist:
        raise Http404

def data_with_id(serializer):
    return {'id': serializer.instance.id, **serializer.data}

# Airline List and Create View
class AirlineList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        GET: List all airlines.
        """
        airlines = Airline.objects.all()
        serializer = AirlineSerializer(airlines, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        POST: Create a new airline.
        """
        serializer = AirlineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data_with_id(serializer=serializer), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Airline Retrieve, Update, and Delete View
class AirlineDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Airline, pk)

    def get(self, request, pk):
        """
        GET: Retrieve a specific airline by ID.
        """
        airline = self.get_object(pk)
        serializer = AirlineSerializer(airline)
        return Response(serializer.data)

    def patch(self, request, pk):
        """
        PATCH: Partially update an airline.
        """
        airline = self.get_object(pk)
        serializer = AirlineSerializer(airline, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk):
        """
        POST: Delete an airline.
        """
        airline = self.get_object(pk)
        airline.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Aircraft Create View
class AircraftCreate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        POST: Create a new aircraft.
        """
        serializer = AircraftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data_with_id(serializer=serializer), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Aircraft Retrieve, Update, and Delete View
class AircraftDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Aircraft, pk)

    def get(self, request, pk):
        """
        GET: Retrieve a specific aircraft by ID.
        """
        aircraft = self.get_object(pk)
        serializer = AircraftSerializer(aircraft)
        return Response(serializer.data)

    def patch(self, request, pk):
        """
        PATCH: Partially update an aircraft.
        """
        aircraft = self.get_object(pk)
        serializer = AircraftSerializer(aircraft, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk):
        """
        POST: Delete an aircraft.
        """
        aircraft = self.get_object(pk)
        aircraft.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)