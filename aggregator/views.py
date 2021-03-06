from http import HTTPStatus
from django.http import HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import tempfile

from .utills import resolve_table_name
from .analyzers import analyzer_factory
from .tasks import persist_data


@csrf_exempt
def aggregate(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id', None)
        if customer_id is None:
            return HttpResponseBadRequest()

        with tempfile.NamedTemporaryFile(delete=False) as f:
            for chunk in request.FILES['file'].chunks():
                f.write(chunk)

        persist_data.delay(customer_id, f.name)

        return JsonResponse({'msg': 'success'})

    return HttpResponseBadRequest()


@csrf_exempt
def analyze(request):
    if request.method == 'POST':
        params = json.loads(request.body.decode('utf-8'))
        customer_id = params['customer_id']
        analyzer_type = params['analyzer_type']

        class_ = analyzer_factory.get_analyzer(analyzer_type)
        table_name = resolve_table_name(customer_id)

        result = class_(table_name).analyze()

        return JsonResponse(result, status=HTTPStatus.OK, safe=False)

    return HttpResponseBadRequest()
