# Module 1.4: The openEHR Template API - Uploading Your First Template

This lesson guides you through your first interaction with the openEHR Template API using Postman. You will learn how to upload the "Vital Signs" Operational Template (OPT) that you created in the previous lesson to your local EHRbase server. This is a fundamental step before you can start working with clinical data based on this template.

We will follow the workflow demonstrated by the course instructor, focusing on practical API interactions.

## Prerequisites

*   **EHRbase Running:** Your local EHRbase instance should be running via Docker. (See [EHRbase Setup Guide](../../docs/guides/ehrbase_setup.md)).
*   **Postman Configured:** Postman should be set up with the "openEHR APIs" collection and the "openEHR Local" environment active. (See [Postman Setup Guide](../../docs/guides/postman_guide.md)).
*   **"Vital Signs" OPT File:** You must have the `[YourName]_vital_signs.v0.opt` file (or similarly named, e.g., `VitalSigns.v0.opt`) downloaded from Archetype Designer from the previous lesson ([Module 1.3: Creating Your First Template - Vital Signs](./module-1-03-creating-a-template-vital-signs.md)).

## Understanding the openEHR REST API

The openEHR REST API provides a standardized way to interact with an openEHR server. EHRbase implements this specification.

*   **Official Specification:** The complete standard is detailed at the [openEHR REST API Specification page](https://specifications.openehr.org/releases/ITS-REST/latest/).
    *   *Instructor's Advice:* "I don't recommend that you dive deep into this first. We will first take a look at our postman collection and then do a few practical exercises. And then if you want to explore further, then you go and look at the... open air REST API specification."
*   **EHRbase API URL Structure:**
    *   The base URL for the openEHR v1 API in EHRbase is typically: `{{baseUrl}}/rest/openehr/v1`
    *   In your Postman "openEHR Local" environment, `{{baseUrl}}` is set to `http://localhost:8080/ehrbase`.
    *   So, the full path prefix for openEHR API v1 endpoints will be: `http://localhost:8080/ehrbase/rest/openehr/v1`
    *   *Instructor's Note:* "The open air base URL is slightly different from the air base base URL... it's the air base base URL, which is localhost 8080 slash air base and then slash REST slash open air slash V1."

## Steps to Upload Your Template

### 1. Optional: Resetting Your EHRbase Instance (Clean Slate)

If you want to ensure a completely empty EHRbase instance (no pre-existing templates or data), you can reset your Docker environment. This is helpful for predictable exercise outcomes.

*   *Instructor's Method:* "If you just want to nuke everything and start everything from scratch... do `docker compose down` and then a `-v` to get rid of all of this data... and then we are doing a `docker compose up`."
*   **Commands:**
    1.  Open your terminal.
    2.  Navigate to the directory containing your EHRbase `docker-compose.yaml` file (this is `openehr-bootcamp-original/` in your project structure).
        ```bash
        cd path/to/your/LearningJourney/openehr-bootcamp-original/
        ```
    3.  Run: `docker-compose down -v`
        *   The `-v` flag removes the named volumes associated with the services, thereby deleting persisted data (like the PostgreSQL database for EHRbase).
    4.  Then, restart the services: `docker-compose up -d`
        *   The `-d` flag runs the containers in detached mode (in the background).
    5.  Allow a minute or two for EHRbase to start up fully.

### 2. Verify EHRbase Status & Initial Template List in Postman

*   **Activate Environment:** In Postman, ensure the **"openEHR Local"** environment is selected in the top-right dropdown.
*   **Status Check (EHRbase):**
    *   From the "openEHR APIs" collection in Postman, find a request to check the EHRbase server status. This is often a `GET` request to `{{baseUrl}}/status`.
    *   Send the request. You should receive a `200 OK` HTTP status code, confirming EHRbase is responsive.
    *   *Instructor's Action:* "The status check, let's just do this once again. Yep, perfect, it works."
*   **List Templates (Initial State):**
    *   In the "openEHR APIs" collection, find the request for listing templates. This corresponds to the endpoint: `GET {{baseUrl}}/rest/openehr/v1/template`.
    *   Send this request.
    *   *Expected Result (on a clean slate):* An empty JSON array `[]` in the response body, and a `200 OK` status.
    *   *Instructor's Expectation:* "Let's also do the list template once and we want to see an empty list of templates. Okay, empty."

### 3. Prepare Your OPT File Content

*   Locate the `.opt` file you downloaded from Archetype Designer in the previous lesson (e.g., `YourName_vital_signs.v0.opt`).
*   Open this file using a plain text editor (like VS Code, Notepad++, Sublime Text, TextEdit, etc.).
*   The content of this file is in XML format.
*   Select **all** the text (the entire XML content) and copy it to your clipboard (Ctrl+C or Cmd+C).
    *   *Instructor's Instruction:* "Make sure that you are able to open that in text editor... This will be in the XML format and just make sure you're able to copy all of this."

### 4. Upload the Template via Postman

*   **Select Request:** In the "openEHR APIs" Postman collection, find the request designed to upload a template. This corresponds to the endpoint: `POST {{baseUrl}}/rest/openehr/v1/template`.
*   **Configure Request Body:**
    *   Select the **"Body"** tab for this request.
    *   Choose the **`raw`** radio button.
    *   In the dropdown menu to the right of the `raw` option (which might default to `JSON` or `Text`), select **`XML`**.
    *   Paste the XML content you copied from your `.opt` file into the large text area provided for the raw body.
    *   *Instructor's Guidance:* "Paste in the XML that you copied. And you have this post and make sure that the body type is raw and choose XML if it's not already selected."
*   **Send Request:** Click the **"Send"** button.

### 5. Verify Upload Success

*   **Response Code:** You should receive an HTTP status code of `201 Created`.
*   **Response Body:** The body of the response will typically contain the XML of the template you just successfully uploaded.
    *   *Instructor's Observation:* "Perfect! You get 201 created and you get a return of the exact same template that you just posted."
*   **List Templates Again:**
    *   Go back to the `GET {{baseUrl}}/rest/openehr/v1/template` request (from step 2).
    *   Send this request again.
    *   You should now see your "VitalSigns.v0" template (or the `template_id` you defined) listed in the JSON array response.
    *   *Instructor's Confirmation:* "Now if you go and list the templates, you can see that you have VitalScience V0 showing up here."

## Congratulations!

You have successfully used the openEHR Template API to upload your first Operational Template to your local EHRbase instance. This means EHRbase is now aware of the "Vital Signs" data structure you defined and is ready to accept data conforming to this template.

*Instructor's Summary:* "This is your first interaction with the OpenAir REST API and you have successfully posted a template."

## Next Steps

With the template in place, the next logical step is to learn how to create and store clinical data (Compositions) that adhere to this "Vital Signs" template structure. This will be covered in upcoming modules.
