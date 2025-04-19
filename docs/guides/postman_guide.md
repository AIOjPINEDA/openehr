# Using Postman with OpenEHR

This guide provides practical instructions for using Postman to interact with OpenEHR REST APIs, specifically focusing on EHRbase.

## Prerequisites

- Postman installed ([Download here](https://www.postman.com/downloads/))
- EHRbase running locally or access to an OpenEHR server
- Basic understanding of HTTP requests and REST APIs

## Setting Up Postman for OpenEHR

### 1. Import the OpenEHR Collection

1. Open Postman
2. Click "Import" in the top left corner
3. Select "Link" and enter: `https://www.postman.com/collections/856f491b8b75b7fbb696`
4. Click "Import"

### 2. Configure Environment Variables

1. Click "Environments" in the sidebar
2. Click "+" to create a new environment
3. Name it "EHRbase Local"
4. Add the following variables:
   - `baseUrl`: `http://localhost:8080/ehrbase/`
   - `username`: `ehrbase-user` (if authentication is enabled)
   - `password`: `SuperSecretPassword` (if authentication is enabled)
5. Click "Save"
6. Select the environment from the dropdown in the top right corner

## Common OpenEHR API Requests

### 1. Create a Patient EHR

**Request:**
- Method: `POST`
- URL: `{{baseUrl}}/rest/openehr/v1/ehr`
- Headers:
  - `Content-Type`: `application/json`
  - `Accept`: `application/json`
- Body:
  ```json
  {
    "_type": "EHR_STATUS",
    "archetype_node_id": "openEHR-EHR-EHR_STATUS.generic.v1",
    "name": {
      "value": "EHR Status"
    },
    "subject": {
      "external_ref": {
        "id": {
          "_type": "GENERIC_ID",
          "value": "patient123",
          "scheme": "id_scheme"
        },
        "namespace": "demographic",
        "type": "PERSON"
      }
    },
    "is_modifiable": true,
    "is_queryable": true
  }
  ```

**Response:**
- Status: `201 Created`
- Body includes the EHR ID that you'll need for subsequent requests

### 2. Upload a Template

**Request:**
- Method: `POST`
- URL: `{{baseUrl}}/rest/openehr/v1/definition/template/adl1.4`
- Headers:
  - `Content-Type`: `application/xml`
  - `Accept`: `application/json`
- Body: Your operational template XML file

**Response:**
- Status: `201 Created`
- Body includes the template ID

### 3. Create a Composition

**Request:**
- Method: `POST`
- URL: `{{baseUrl}}/rest/openehr/v1/composition`
- Headers:
  - `Content-Type`: `application/json`
  - `Accept`: `application/json`
  - `Prefer`: `return=representation`
  - `X-VERSIONED-EHR-ID`: `<ehr_id>` (from step 1)
- Body: Your composition JSON (structure depends on your template)

**Response:**
- Status: `201 Created`
- Body includes the composition ID and version information

### 4. Query Data with AQL

**Request:**
- Method: `POST`
- URL: `{{baseUrl}}/rest/openehr/v1/query/aql`
- Headers:
  - `Content-Type`: `application/json`
  - `Accept`: `application/json`
- Body:
  ```json
  {
    "q": "SELECT c FROM COMPOSITION c WHERE c/archetype_details/template_id/value = 'your_template_id'"
  }
  ```

**Response:**
- Status: `200 OK`
- Body includes the query results

## Testing Your Requests

1. Start with creating an EHR
2. Upload your template
3. Create a composition using the template
4. Query the data to verify it was stored correctly

## Troubleshooting

### Common Issues

1. **Connection refused**
   - Ensure EHRbase is running
   - Check the baseUrl environment variable

2. **Authentication errors**
   - Verify username and password
   - Check if Basic Auth is enabled in EHRbase

3. **Invalid template**
   - Validate your template XML
   - Ensure it's a valid operational template (OPT)

4. **Invalid composition**
   - Check that your composition JSON matches the template structure
   - Verify all required fields are present

## References

- [EHRbase REST API Documentation](https://ehrbase.readthedocs.io/en/latest/03_development/04_api/04_api.html)
- [OpenEHR REST API Specification](https://specifications.openehr.org/releases/ITS-REST/latest/)
- [Postman Documentation](https://learning.postman.com/docs/getting-started/introduction/)
- [Archetype Query Language Specification](https://specifications.openehr.org/releases/QUERY/latest/AQL.html)
