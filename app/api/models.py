import graphene
from datetime import datetime
from django.db import models
from utils import Utils
from logger import logger

import json
from django.conf import settings
from operator import itemgetter



class claveS(graphene.InputObjectType):
    S = graphene.String()

class claveoS(graphene.InputObjectType):
    S = graphene.String()

class claveN(graphene.InputObjectType):
    S = graphene.Int()

class claveoN(graphene.InputObjectType):
    S = graphene.Int()






class LastEvaluatedKeyApi(graphene.InputObjectType):
    ID = claveS()

class Api(models.Model):


    ID = models.TextField(primary_key=True)
    IncidentNumber = models.TextField(null=True)
    ExposureNumber = models.TextField(null=True)
    Address = models.TextField(null=True)
    IncidentDate = models.TextField(null=True)
    CallNumber = models.TextField(null=True)
    AlarmDtTm = models.TextField(null=True)
    ArrivalDtTm = models.TextField(null=True)
    CloseDtTm = models.TextField(null=True)
    City = models.TextField(null=True)
    zipcode = models.TextField(null=True)
    Battalion = models.TextField(null=True)
    StationArea = models.TextField(null=True)
    Box = models.TextField(null=True)
    SuppressionUnits = models.TextField(null=True)
    SuppressionPersonnel = models.TextField(null=True)
    EMSUnits = models.TextField(null=True)
    EMSPersonnel = models.TextField(null=True)
    OtherUnits = models.TextField(null=True)
    OtherPersonnel = models.TextField(null=True)
    FirstUnitOnScene = models.TextField(null=True)
    EstimatedPropertyLoss = models.TextField(null=True)
    EstimatedContentsLoss = models.TextField(null=True)
    FireFatalities = models.TextField(null=True)
    FireInjuries = models.TextField(null=True)
    CivilianFatalities = models.TextField(null=True)
    CivilianInjuries = models.TextField(null=True)
    NumberofAlarms = models.TextField(null=True)
    PrimarySituation = models.TextField(null=True)
    MutualAid = models.TextField(null=True)
    ActionTakenPrimary = models.TextField(null=True)
    ActionTakenSecondary = models.TextField(null=True)
    ActionTakenOther = models.TextField(null=True)
    DetectorAlertedOccupants = models.TextField(null=True)
    PropertyUse = models.TextField(null=True)
    AreaofFireOrigin = models.TextField(null=True)
    IgnitionCause = models.TextField(null=True)
    IgnitionFactorPrimary = models.TextField(null=True)
    IgnitionFactorSecondary = models.TextField(null=True)
    HeatSource = models.TextField(null=True)
    ItemFirstIgnited = models.TextField(null=True)
    HumanFactorsAssociatedwithIgnition = models.TextField(null=True)
    StructureType = models.TextField(null=True)
    StructureStatus = models.TextField(null=True)
    FloorofFireOrigin = models.TextField(null=True)
    FireSpread = models.TextField(null=True)
    NoFlameSpead = models.TextField(null=True)
    Numberoffloorswithminimumdamage = models.TextField(null=True)
    Numberoffloorswithsignificantdamage = models.TextField(null=True)
    Numberoffloorswithheavydamage = models.TextField(null=True)
    Numberoffloorswithextremedamage = models.TextField(null=True)
    DetectorsPresent = models.TextField(null=True)
    DetectorType = models.TextField(null=True)
    DetectorOperation = models.TextField(null=True)
    DetectorEffectiveness = models.TextField(null=True)
    DetectorFailureReason = models.TextField(null=True)
    AutomaticExtinguishingSystemPresent = models.TextField(null=True)
    AutomaticExtinguishingSytemType = models.TextField(null=True)
    AutomaticExtinguishingSytemPerfomance = models.TextField(null=True)
    AutomaticExtinguishingSytemFailureReason = models.TextField(null=True)
    NumberofSprinklerHeadsOperating = models.TextField(null=True)
    SupervisorDistrict = models.TextField(null=True)
    neighborhood_district = models.TextField(null=True)
    point = models.TextField(null=True)
    IngestionDate = models.TextField(null=False)

def get_api( ID , limit = 100, ascendente = True, last_evaluated_key = None ):

    if config.conf["tracklogs"]:
        config.log.Info("Consulta get_api con parametros: clave_primaria={}".format(clave_primaria))

    result = Api.query(hash_key = clave_primaria, filter_condition=Api.activo==1, limit=limit, scan_index_forward=ascendente,  last_evaluated_key=last_evaluated_key)
    
    return list(result)

class ApiDataInput(graphene.InputObjectType):
    
    ID = graphene.String()
    IncidentNumber = graphene.String()
    ExposureNumber = graphene.String()
    Address = graphene.String()
    IncidentDate = graphene.String()
    CallNumber = graphene.String()
    AlarmDtTm = graphene.String()
    ArrivalDtTm = graphene.String()
    CloseDtTm = graphene.String()
    City = graphene.String()
    zipcode = graphene.String()
    Battalion = graphene.String()
    StationArea = graphene.String()
    Box = graphene.String()
    SuppressionUnits = graphene.String()
    SuppressionPersonnel = graphene.String()
    EMSUnits = graphene.String()
    EMSPersonnel = graphene.String()
    OtherUnits = graphene.String()
    OtherPersonnel = graphene.String()
    FirstUnitOnScene = graphene.String()
    EstimatedPropertyLoss = graphene.String()
    EstimatedContentsLoss = graphene.String()
    FireFatalities = graphene.String()
    FireInjuries = graphene.String()
    CivilianFatalities = graphene.String()
    CivilianInjuries = graphene.String()
    NumberofAlarms = graphene.String()
    PrimarySituation = graphene.String()
    MutualAid = graphene.String()
    ActionTakenPrimary = graphene.String()
    ActionTakenSecondary = graphene.String()
    ActionTakenOther = graphene.String()
    DetectorAlertedOccupants = graphene.String()
    PropertyUse = graphene.String()
    AreaofFireOrigin = graphene.String()
    IgnitionCause = graphene.String()
    IgnitionFactorPrimary = graphene.String()
    IgnitionFactorSecondary = graphene.String()
    HeatSource = graphene.String()
    ItemFirstIgnited = graphene.String()
    HumanFactorsAssociatedwithIgnition = graphene.String()
    StructureType = graphene.String()
    StructureStatus = graphene.String()
    FloorofFireOrigin = graphene.String()
    FireSpread = graphene.String()
    NoFlameSpead = graphene.String()
    Numberoffloorswithminimumdamage = graphene.String()
    Numberoffloorswithsignificantdamage = graphene.String()
    Numberoffloorswithheavydamage = graphene.String()
    Numberoffloorswithextremedamage = graphene.String()
    DetectorsPresent = graphene.String()
    DetectorType = graphene.String()
    DetectorOperation = graphene.String()
    DetectorEffectiveness = graphene.String()
    DetectorFailureReason = graphene.String()
    AutomaticExtinguishingSystemPresent = graphene.String()
    AutomaticExtinguishingSytemType = graphene.String()
    AutomaticExtinguishingSytemPerfomance = graphene.String()
    AutomaticExtinguishingSytemFailureReason = graphene.String()
    NumberofSprinklerHeadsOperating = graphene.String()
    SupervisorDistrict = graphene.String()
    neighborhood_district = graphene.String()
    point = graphene.String()
    IngestionDate = graphene.String()
