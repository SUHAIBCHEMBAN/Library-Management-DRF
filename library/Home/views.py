from django.shortcuts import render
from django.views import View

# Create your views here.

class Home(View):
    """
    A class-based view that handles GET requests to the home page.

    This view returns a simple HTTP response with the message 'API is Running!'.
    """
    def get(self,request):
        """
        Handles GET requests to the home page.
        """
        return render(request,'home.html')