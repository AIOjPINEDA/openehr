---
applyTo: "**"
---

# OpenEHR API Integration Standards

Create EHR before storing any compositions via `POST /rest/openehr/v1/ehr`.
Upload and validate templates before data persistence via `POST /rest/openehr/v1/definition/template/adl1.4`.
Always include headers: `Content-Type: application/json`, `Accept: application/json`.
Use Basic Authentication when `SECURITY_AUTHTYPE=BASIC` is configured.

Store compositions via `POST /rest/openehr/v1/ehr/{ehr_id}/composition`.
Update compositions via `PUT /rest/openehr/v1/ehr/{ehr_id}/composition/{object_id}`.
Execute AQL queries via `POST /rest/openehr/v1/query/aql`.
Retrieve compositions via `GET /rest/openehr/v1/ehr/{ehr_id}/composition/{object_id}`.

Use UUID format for patient identifiers to ensure anonymization.
Use ISO 8601 format for timestamps: `2024-01-15T14:30:00Z`.
Use UCUM standard for units: kg, cm, mmHg, °C.
Use full URI format for SNOMED CT: `http://snomed.info/sct|123456789`.

Use proper escaping and parameterization for AQL queries.
Implement version management for composition updates.
Include participation objects for clinical actor identification.

Reference Postman collection files in `openehr-bootcamp-original/postman/` for exact API syntax and examples.
