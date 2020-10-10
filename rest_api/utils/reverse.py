#reverse(viewname, *args, **kwargs)
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from django.utils.timezone import now


class APIRootView(APIView):
    def get(self, request):
        year = now().year
        data = {
            ...
            'year-summary-url': reverse('year-summary', args=[year], request=request)
        }
        return Response(data)


#reverse_lazy(viewname, *args, **kwargs)
api_root = reverse_lazy('api-root', request=request)
