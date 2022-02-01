CREATE SCHEMA raw;
CREATE SCHEMA processed;

-- TODO: PARTITION BY
CREATE TABLE IF NOT EXISTS raw.fire_incidents(
    "IncidentNumber" VARCHAR,
    "ExposureNumber" VARCHAR,
    "ID" VARCHAR,
    "Address" VARCHAR,
    "IncidentDate" VARCHAR,
    "CallNumber" VARCHAR,
    "AlarmDtTm" VARCHAR,
    "ArrivalDtTm" VARCHAR,
    "CloseDtTm" VARCHAR,
    "City" VARCHAR,
    "zipcode" VARCHAR,
    "Battalion" VARCHAR,
    "StationArea" VARCHAR,
    "Box" VARCHAR,
    "SuppressionUnits" VARCHAR,
    "SuppressionPersonnel" VARCHAR,
    "EMSUnits" VARCHAR,
    "EMSPersonnel" VARCHAR,
    "OtherUnits" VARCHAR,
    "OtherPersonnel" VARCHAR,
    "FirstUnitOnScene" VARCHAR,
    "EstimatedPropertyLoss" VARCHAR,
    "EstimatedContentsLoss" VARCHAR,
    "FireFatalities" VARCHAR,
    "FireInjuries" VARCHAR,
    "CivilianFatalities" VARCHAR,
    "CivilianInjuries" VARCHAR,
    "NumberofAlarms" VARCHAR,
    "PrimarySituation" VARCHAR,
    "MutualAid" VARCHAR,
    "ActionTakenPrimary" VARCHAR,
    "ActionTakenSecondary" VARCHAR,
    "ActionTakenOther" VARCHAR,
    "DetectorAlertedOccupants" VARCHAR,
    "PropertyUse" VARCHAR,
    "AreaofFireOrigin" VARCHAR,
    "IgnitionCause" VARCHAR,
    "IgnitionFactorPrimary" VARCHAR,
    "IgnitionFactorSecondary" VARCHAR,
    "HeatSource" VARCHAR,
    "ItemFirstIgnited" VARCHAR,
    "HumanFactorsAssociatedwithIgnition" VARCHAR,
    "StructureType" VARCHAR,
    "StructureStatus" VARCHAR,
    "FloorofFireOrigin" VARCHAR,
    "FireSpread" VARCHAR,
    "NoFlameSpead" VARCHAR,
    "Numberoffloorswithminimumdamage" VARCHAR,
    "Numberoffloorswithsignificantdamage" VARCHAR,
    "Numberoffloorswithheavydamage" VARCHAR,
    "Numberoffloorswithextremedamage" VARCHAR,
    "DetectorsPresent" VARCHAR,
    "DetectorType" VARCHAR,
    "DetectorOperation" VARCHAR,
    "DetectorEffectiveness" VARCHAR,
    "DetectorFailureReason" VARCHAR,
    "AutomaticExtinguishingSystemPresent" VARCHAR,
    "AutomaticExtinguishingSytemType" VARCHAR,
    "AutomaticExtinguishingSytemPerfomance" VARCHAR,
    "AutomaticExtinguishingSytemFailureReason" VARCHAR,
    "NumberofSprinklerHeadsOperating" VARCHAR,
    "SupervisorDistrict" VARCHAR,
    "neighborhood_district" VARCHAR,
    "point" VARCHAR,
    "IngestionDate" VARCHAR
) PARTITION BY RANGE ("IngestionDate");