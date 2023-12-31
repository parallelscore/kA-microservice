
def data():
    data = data = {
    "resourceType": "PlanDefinition",
    "id": "2",
    "meta": {
        "versionId": "1",
        "lastUpdated": "2023-09-19T18:49:51.103+00:00",
        "source": "#q83myb3baobYKNKV",
        "profile": [
            "http://hl7.org/fhir/us/medmorph/StructureDefinition/medmorph-plandefinition",
            "http://hl7.org/fhir/us/medmorph/StructureDefinition/us-ph-plandefinition"
        ]
    },
    "text": {
        "status": "extensions",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>MedMorph PlanDefinition Example</b></p></div>"
    },
    "url": "http://hl7.org/fhir/us/medmorph/StructureDefinition/medmorph-plandefinition-example",
    "version": "1.0.0",
    "name": "MedMorphPlanDefinitionExample",
    "title": "MedMorph PlanDefinition Example",
    "type": {
        "coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/plan-definition-type",
                "code": "workflow-definition",
                "display": "Workflow Definition"
            }
        ]
    },
    "status": "active",
    "date": "2020-07-31T12:32:29.858-05:00",
    "publisher": "HL7 International - Public Health Work Group",
    "contact": [
        {
            "telecom": [
                {
                    "system": "url",
                    "value": "http://hl7.org/Special/committees/pher"
                }
            ]
        }
    ],
    "description": "An example MedMorph PlanDefinition",
    "jurisdiction": [
        {
            "coding": [
                {
                    "system": "urn:iso:std:iso:3166",
                    "code": "US"
                }
            ]
        }
    ],
    "effectivePeriod": {
        "start": "2020-12-01"
    },
    "relatedArtifact": [
        {
            "type": "depends-on",
            "label": "Value Set Library of Trigger Codes",
            "resource": "http://hl7.org/fhir/us/medmorph/ValueSet/valueset-cancer-trigger-codes-example"
        }
    ],
    "action": [
        {
            "id": "start-workflow",
            "description": "This action represents the start of the reporting workflow in response to the encounter-start event. Other named events can be used instead of encounter-start.",
            "textEquivalent": "Start the reporting workflow in response to an encounter-start event",
            "code": [
                {
                    "coding": [
                        {
                            "system": "http://hl7.org/fhir/us/medmorph/CodeSystem/us-ph-plandefinition-actions",
                            "code": "initiate-reporting-workflow",
                            "display": "Initiate a reporting workflow"
                        }
                    ]
                }
            ],
            "trigger": [
                {
                    "id": "new-diagnosis",
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/us/medmorph/StructureDefinition/us-ph-named-eventtype",
                            "valueCodeableConcept": {
                                "coding": [
                                    {
                                        "system": "http://hl7.org/fhir/us/medmorph/CodeSystem/us-ph-triggerdefinition-namedevents",
                                        "code": "new-diagnosis",
                                        "display": "Indicates the end of a diagnosis"
                                    }
                                ]
                            }
                        }
                    ],
                    "type": "named-event",
                    "name": "new-diagnosis"
                }
            ]
        },
        {
            "id": "check-reportability",
            "description": "This action represents the start of the check for reportable conditions in response to the encounter-start event. This is an example of executing a reporting workflow with other actions.",
            "textEquivalent": "Check Reportability and setup jobs for future reportability checks.",
            "code": [
                {
                    "coding": [
                        {
                            "system": "http://hl7.org/fhir/us/medmorph/CodeSystem/us-ph-plandefinition-actions",
                            "code": "execute-reporting-workflow"
                        }
                    ]
                }
            ],
            "action": [
                {
                    "id": "is-encounter-reportable",
                    "description": "This action represents the check for reportability to create the Report.",
                    "textEquivalent": "Check Trigger Codes based on Value sets.",
                    "code": [
                        {
                            "coding": [
                                {
                                    "system": "http://hl7.org/fhir/us/medmorph/CodeSystem/us-ph-plandefinition-actions",
                                    "code": "check-trigger-codes"
                                }
                            ]
                        }
                    ],
                    "condition": [
                        {
                            "kind": "applicability",
                            "expression": {
                                "language": "text/fhirpath",
                                "expression": "%encounter.where(%encounterStartDate + 1 day * %normalReportingDuration >= now()).select(true) and (%conditions.exists() or %encounters.exists() or %immunizations.exists() or %procedures.exists() or %procedureOrders.exists() or %labOrders.exists() or %labTests.exists() or %labResults.exists() or %medicationAdministrations.exists() or %medicationOrders.exists() or %medicationDispenses.exists())"
                            }
                        }
                    ]
                }
            ]
        }

           ]
}
    return data

def plandef():
    pd = {
    "resourceType": "PlanDefinition",
    "id": "2",
    "meta": {
        "versionId": "1",
        "lastUpdated": "2023-09-19T18:49:51.103+00:00",
        "source": "#q83myb3baobYKNKV",
        "profile": [
            "http://hl7.org/fhir/us/medmorph/StructureDefinition/medmorph-plandefinition",
            "http://hl7.org/fhir/us/medmorph/StructureDefinition/us-ph-plandefinition"
        ]
    },
    "text": {
        "status": "extensions",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>MedMorph PlanDefinition Example</b></p></div>"
    },
    "url": "http://hl7.org/fhir/us/medmorph/StructureDefinition/medmorph-plandefinition-example",
    "version": "1.0.0",
    "name": "MedMorphPlanDefinitionExample",
    "title": "MedMorph PlanDefinition Example",
    "type": {
        "coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/plan-definition-type",
                "code": "workflow-definition",
                "display": "Workflow Definition"
            }
        ]
    },
    "status": "active",
    "date": "2020-07-31T12:32:29.858-05:00",
    "publisher": "HL7 International - Public Health Work Group",
    "contact": [
        {
            "telecom": [
                {
                    "system": "url",
                    "value": "http://hl7.org/Special/committees/pher"
                }
            ]
        }
    ],
    "description": "An example MedMorph PlanDefinition",
    "jurisdiction": [
        {
            "coding": [
                {
                    "system": "urn:iso:std:iso:3166",
                    "code": "US"
                }
            ]
        }
    ],
    "effectivePeriod": {
        "start": "2020-12-01"
    },
    "relatedArtifact": [
        {
            "type": "depends-on",
            "label": "Value Set Library of Trigger Codes",
            "resource": "http://hl7.org/fhir/us/medmorph/ValueSet/valueset-cancer-trigger-codes-example"
        }
    ],
    "action": [
        {
            "id": "start-workflow",
            "description": "This action represents the start of the reporting workflow in response to the encounter-start event. Other named events can be used instead of encounter-start.",
            "textEquivalent": "Start the reporting workflow in response to an encounter-start event",
            "code": [
                {
                    "coding": [
                        {
                            "system": "http://hl7.org/fhir/us/medmorph/CodeSystem/us-ph-plandefinition-actions",
                            "code": "initiate-reporting-workflow",
                            "display": "Initiate a reporting workflow"
                        }
                    ]
                }
            ],
            "trigger": [
                {
                    "id": "new-diagnosis",
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/us/medmorph/StructureDefinition/us-ph-named-eventtype",
                            "valueCodeableConcept": {
                                "coding": [
                                    {
                                        "system": "http://hl7.org/fhir/us/medmorph/CodeSystem/us-ph-triggerdefinition-namedevents",
                                        "code": "new-diagnosis",
                                        "display": "Indicates the end of a diagnosis"
                                    }
                                ]
                            }
                        }
                    ],
                    "type": "named-event",
                    "name": "new-diagnosis"
                }
            ]
        },
        {
            "id": "check-reportability",
            "description": "This action represents the start of the check for reportable conditions in response to the encounter-start event. This is an example of executing a reporting workflow with other actions.",
            "textEquivalent": "Check Reportability and setup jobs for future reportability checks.",
            "code": [
                {
                    "coding": [
                        {
                            "system": "http://hl7.org/fhir/us/medmorph/CodeSystem/us-ph-plandefinition-actions",
                            "code": "execute-reporting-workflow"
                        }
                    ]
                }
            ],
            "action": [
                {
                    "id": "is-encounter-reportable",
                    "description": "This action represents the check for reportability to create the Report.",
                    "textEquivalent": "Check Trigger Codes based on Value sets.",
                    "code": [
                        {
                            "coding": [
                                {
                                    "system": "http://hl7.org/fhir/us/medmorph/CodeSystem/us-ph-plandefinition-actions",
                                    "code": "check-trigger-codes"
                                }
                            ]
                        }
                    ],
                    "condition": [
                        {
                            "kind": "applicability",
                            "expression": {
                                "language": "text/fhirpath",
                                "expression": "%encounter.where(%encounterStartDate + 1 day * %normalReportingDuration >= now()).select(true) and (%conditions.exists() or %encounters.exists() or %immunizations.exists() or %procedures.exists() or %procedureOrders.exists() or %labOrders.exists() or %labTests.exists() or %labResults.exists() or %medicationAdministrations.exists() or %medicationOrders.exists() or %medicationDispenses.exists())"
                            }
                        }
                    ]
                }
            ]
        }

           ]
}
    return pd