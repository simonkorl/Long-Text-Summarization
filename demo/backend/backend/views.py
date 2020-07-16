from django.http import JsonResponse

from . import textsumm


class Response:
    STATUS_INVALID_REQUEST = 500
    STATUS_SERVER_ERROR = 501
    STATUS_SUCCESS = 200

    @staticmethod
    def _make_response(msg, status, payload):
        return {"msg": msg, "status": status, "payload": payload}

    @classmethod
    def invalid_request(cls):
        return cls._make_response(msg="Invalid Request", status=cls.STATUS_INVALID_REQUEST, payload={})

    @classmethod
    def server_error(cls):
        return cls._make_response(msg="Server Error", status=cls.STATUS_SERVER_ERROR, payload={})

    @classmethod
    def success(cls, payload):
        return cls._make_response(msg="Success", status=cls.STATUS_SUCCESS, payload=payload)


def text_summ(request):
    response = None
    try:
        if request.POST:
            text = request.POST['text']
            res_textrank = textsumm.textrank(text)
            res_tfidf = textsumm.tfidf(text)
            res_lead1 = textsumm.lead1(text)
            response = Response.success({
                "textrank": res_textrank,
                "tfidf": res_tfidf,
                "lead1": res_lead1,
            })
        else:
            raise ValueError
    except (ValueError, KeyError):
        response = Response.invalid_request()
    except:
        response = Response.server_error()
    finally:
        return JsonResponse(response)
