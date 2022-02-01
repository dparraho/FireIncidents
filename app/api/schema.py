import graphene
from graphene_django.types import DjangoObjectType

from api.models import Api, get_api, ApiDataInput, LastEvaluatedKeyApi


from itertools import islice
from api.errors import CustomFatalError
import operator as op
from datetime import datetime
from pytz import timezone


def getCrud():
    tzx = timezone("America/Bogota")
    modificacioncrudint = int(datetime.now(tzx).strftime("%Y%m%d%H%M%S"))
    return modificacioncrudint

class ApiType(DjangoObjectType):
    class Meta:
        model = Api

class ApiType_all(graphene.ObjectType):
    total_count = graphene.Int(required=True)
    api = graphene.List(ApiType)


class Query(graphene.ObjectType):

    api_all = graphene.Field(ApiType_all, ID=graphene.String(), limit=graphene.Int(),
                             ascendente=graphene.Boolean(), last_evaluated_key=LastEvaluatedKeyApi())
    api = graphene.List(ApiType, ID=graphene.String(), limit=graphene.Int(),
                        ascendente=graphene.Boolean(), last_evaluated_key=LastEvaluatedKeyApi())

    status = graphene.String()

    def resolve_status(self, info, **kwargs):
        return "Ok"

    def resolve_api_all(self, info, ID, limit=100, ascendente=True, last_evaluated_key=None, **kwargs):

        complete = ApiType_all()

        if ID is not None:
            result = get_api(ID, limit, ascendente, last_evaluated_key)
        else:
            result = None

        complete.total_count = len(result)
        complete.api = result

        return complete

    def resolve_api(self, info, ID, limit=100, ascendente=True, last_evaluated_key=None, **kwargs):

        if ID is not None:
            result = get_api(ID, limit, ascendente, last_evaluated_key)
        else:
            result = None

        return result





schema = graphene.Schema(query=Query, types=[ApiType, ApiType_all])
