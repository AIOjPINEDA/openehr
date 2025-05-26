# Module 2: Retrieving, Updating, and Versioning Compositions

This guide explains how to retrieve and update openEHR compositions using the EHRbase REST API, typically via a tool like Postman, as demonstrated in the bootcamp.

## 1. Retrieving Compositions

After a composition has been created (as covered in `module-2-01-creating-compositions-api.md`), you can retrieve it using its unique identifier.

### Key Concepts:

*   **Composition UID**: When a composition is successfully posted to the EHRbase server, the response includes a `uid` (or `versioned_object_id` for the specific version). This UID is crucial for retrieving or updating the composition.
*   **Versioned Object ID**: This ID has three parts:
    1.  **Object ID (UUID)**: The unique identifier for the composition itself (e.g., `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`). This is the part you use when you want to refer to the latest version of the object.
    2.  **Creating System ID**: Identifies the system that created this version (e.g., `local.ehrbase.org`).
    3.  **Version Number**: An integer indicating the version of the composition (e.g., `1`, `2`).
    The full `versioned_object_id` looks like: `[UUID]::[Creating System ID]::[Version]`.

### API Endpoint for Retrieval:

*   `GET /rest/openehr/v1/ehr/{ehr_id}/composition/{composition_uid}`
    *   `{ehr_id}`: The ID of the EHR containing the composition.
    *   `{composition_uid}`: The UUID part of the composition's `versioned_object_id`.

### Steps to Retrieve a Composition (e.g., in Postman):

1.  **Obtain the Composition UID**: After creating a composition, copy the UUID from the response (usually found at the end of the `versioned_object_id` string, before `::local.ehrbase.org::1`).
2.  **Set up the Request**:
    *   Method: `GET`
    *   URL: `https://openehr-bootcamp.medblocks.com/ehrbase/rest/openehr/v1/ehr/{your_ehr_id}/composition/{composition_uuid_copied_in_step_1}`
3.  **Specify `Accept` Header for Desired Format**:
    You can retrieve the composition in various formats by setting the `Accept` header:
    *   `application/json`: For Canonical JSON.
    *   `application/xml`: For Canonical XML.
    *   `application/openehr.wt.flat+json`: For Flat JSON (if using a Web Template).
    *   `application/openehr.wt.structured+json`: For Structured JSON (if using a Web Template).
    The system stores the data in a standard openEHR format, and these are just different serialization options. You are not losing data by posting in one format and retrieving in another.

**Example**:
If you posted a composition and got back `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx::local.ehrbase.org::1`, you would use `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx` as the `{composition_uid}` in the GET request.

## 2. Updating Compositions

Existing compositions can be updated. OpenEHR handles this by creating a new version of the composition, preserving the history.

### Key Concepts:

*   **Preceding Version UID**: To update a composition, you MUST provide the complete `versioned_object_id` of the *specific version* you intend to update. This is used in the `If-Match` header.
*   **Versioning**: Each update creates a new version of the composition (e.g., version 1 becomes version 2, version 2 becomes version 3, and so on). All previous versions are retained.

### API Endpoint for Update:

*   `PUT /rest/openehr/v1/ehr/{ehr_id}/composition/{object_id}`
    *   `{ehr_id}`: The ID of the EHR.
    *   `{object_id}`: The UUID part of the composition's `versioned_object_id` (the object ID itself, not the full versioned ID).

### Headers for Update:

*   `Content-Type`: Must match the format of the composition data you are sending in the request body (e.g., `application/openehr.wt.flat+json`, `application/json`, `application/xml`).
*   `Accept`: Specifies the desired format for the response (e.g., `application/json`).
*   `If-Match`: **Crucial for updates**. This header must contain the full `versioned_object_id` of the composition version you are updating (e.g., `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx::local.ehrbase.org::1`).

### Steps to Update a Composition (e.g., in Postman):

1.  **Retrieve the Composition to Update (Optional but Recommended)**: First, GET the composition you want to update. This helps ensure you have the latest version and its full `versioned_object_id`.
2.  **Copy the Full `versioned_object_id`**: From the retrieved composition's metadata (e.g., in the response headers or body, often labeled `ETag` or `VERSION_UID`), copy the complete `versioned_object_id` (e.g., `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx::local.ehrbase.org::1`).
3.  **Prepare the Request Body**:
    *   Use the same format (Flat, Canonical JSON, XML) as the `Content-Type` header will indicate.
    *   Modify the composition data as needed (e.g., change a vital sign value).
    *   **Important**: If your request body format includes a field for the composition's UID (like `_uid` in some flat formats or a specific path in canonical formats), you might need to remove or nullify it. The system will generate the UID for the new version. The transcript specifically mentions removing the `vital_signs/uid` field when updating a flat JSON composition.
4.  **Set up the PUT Request**:
    *   Method: `PUT`
    *   URL: `https://openehr-bootcamp.medblocks.com/ehrbase/rest/openehr/v1/ehr/{your_ehr_id}/composition/{composition_uuid}` (use the UUID part only in the URL).
    *   Headers:
        *   `Content-Type`: e.g., `application/openehr.wt.flat+json`
        *   `Accept`: e.g., `application/json`
        *   `If-Match`: The full `versioned_object_id` copied in step 2.
    *   Body: The modified composition data.
5.  **Execute the Request**:
    *   A successful update will typically return a `200 OK` or `204 No Content` status, and the response headers will contain the `versioned_object_id` of the *newly created version* (e.g., `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx::local.ehrbase.org::2`).

**Example Workflow**:

1.  You have a composition with `versioned_object_id`: `abc-123::local.ehrbase.org::1`.
2.  To update it, you make a `PUT` request to `/rest/openehr/v1/ehr/{ehr_id}/composition/abc-123`.
3.  The `If-Match` header of this `PUT` request must be `abc-123::local.ehrbase.org::1`.
4.  The request body contains the new data for the composition.
5.  Upon success, EHRbase creates a new version. If you retrieve `abc-123` again, you'll get version 2, and its `versioned_object_id` will be `abc-123::local.ehrbase.org::2`.
6.  If you want to update it again, your next `PUT` request's `If-Match` header must be `abc-123::local.ehrbase.org::2`.

## 3. Retrieving Specific Versions

You can retrieve a specific version of a composition if you know its full `versioned_object_id`. This is useful for viewing the history of changes.

#### API Endpoint for Retrieving a Specific Version:

*   `GET /rest/openehr/v1/ehr/{ehr_id}/composition/{versioned_composition_id}`
    *   `{ehr_id}`: The ID of the EHR.
    *   `{versioned_composition_id}`: This is the **full** versioned ID of the composition, including the UUID, creating system, and version number (e.g., `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx::local.ehrbase.org::1`).

#### Steps to Retrieve a Specific Version:

1.  **Identify the `versioned_object_id`**: You need the complete `versioned_object_id` of the specific version you want to retrieve. For example, if you updated a composition from version 1 to version 2, and then to version 3, you can retrieve version 1, 2, or 3 by using their respective full `versioned_object_id`s.
2.  **Set up the GET Request**:
    *   Method: `GET`
    *   URL: `https://openehr-bootcamp.medblocks.com/ehrbase/rest/openehr/v1/ehr/{your_ehr_id}/composition/{full_versioned_composition_id_from_step_1}`
    *   Headers: Specify the `Accept` header for the desired format (e.g., `application/openehr.wt.flat+json`, `application/json`).

**Example**:
To retrieve version 1 of a composition whose `versioned_object_id` is `abc-123::local.ehrbase.org::1`, you would use that full string as the `{versioned_composition_id}` in the GET request. To get version 2 (`abc-123::local.ehrbase.org::2`), you would use that specific versioned ID.

This allows you to access the historical state of the composition. All versions are preserved in the system by default, providing a full audit trail of changes.

**When to Update vs. Create New Compositions**:

*   **Updating existing compositions** is generally used for correcting errors or for specific use cases like managing a "living" document (e.g., a medication list that is always current).
*   **Creating new compositions** is the more common pattern for recording new clinical events or encounters (e.g., a new vital signs observation, a new consultation note). This reflects the chronological nature of most health records.

The system maintains a full history regardless, so you don't lose data. The choice depends on the clinical workflow and data modeling decisions for the specific template.

This documentation should help you understand the processes of retrieving, updating, and managing versions of compositions as discussed in the bootcamp sessions.
