
import json
from json import JSONDecodeError

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.views import APIView
from tether_utils.ExternalApiHandler import ExternalApiHandlerBase




class SubscriberSnsView(APIView):
    @swagger_auto_schema(
        method="post",
        operation_description="Esta vista tiene por finalidad el controlar los eventos base gatillado por SNS."
        "Tiene por restricción la reacción ante los eventos HTTPs gatillados desde el servicio"
        "Es decir, controlara basicamente el mensaje entrante y el tipo de evento, el resto"
        "debera ser implementado por la vista local. Todos los mensajes desde SNS llegan via"
        "POST por lo que el método debe ser implementado como post, y respondiendo un status"
        "200 por defecto",
    )
    @action(detail=True, methods=["post"])
    def post(self, request):
        headers = request.headers
        body = request.body
        message_type = headers["X-Amz-Sns-Message-Type"]
        msg = json.loads(body)

        def_response = {
            "event_type": message_type,
            "event_data": None,
            "event_attributes": None,
        }

        if message_type.__eq__("SubscriptionConfirmation"):
            handler = ExternalApiHandlerBase()

            subscribe_resp = handler.get(endpoint=msg["SubscribeURL"])

            print(f"SubscriptionConfirmation {subscribe_resp}")

        elif message_type.__eq__("Notification"):

            try:
                event_data = json.loads(msg["Message"])
            except JSONDecodeError as error:
                event_data = msg["Message"].replace("'", "\"")
                event_data = json.loads(event_data)

            event_attributes = msg["MessageAttributes"]
            def_response["event_data"] = event_data
            def_response["event_attributes"] = event_attributes

        return def_response
