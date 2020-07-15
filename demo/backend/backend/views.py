from django.http import JsonResponse

from . import textsumm


class Response:
    STATUS_INVALID_REQUEST = 500
    STATUS_SERVER_ERROR = 501
    STATUS_SUCCESS = 200

    @staticmethod
    def invalid_request():
        return {"msg": "Invalid Request", "status": Response.STATUS_INVALID_REQUEST}

    @staticmethod
    def server_error():
        return {"msg": "Server Error", "status": Response.STATUS_SERVER_ERROR}


def text_summ(request):
    response = None
    try:
        if request.POST:
            text = request.POST['text']
            res_textrank = textsumm.textrank(text)
            res_tfidf = textsumm.tfidf(text)
            res_lead1 = textsumm.lead1(text)
            response = {
                "msg": "success",
                "status": Response.STATUS_SUCCESS,
                "textrank": res_textrank,
                "tfidf": res_tfidf,
                "lead1": res_lead1,
            }
        else:
            raise ValueError
    except (ValueError, KeyError):
        response = Response.invalid_request()
    except:
        response = Response.server_error()
    finally:
        return JsonResponse(response)
