# Module 2: Building Your First OpenEHR Application - Kickoff Summary

This document summarizes the key concepts, assignment details, and discussions from the MedBlocks OpenEHR Bootcamp Module 2 kickoff session.

## Core Assignment: First OpenEHR Application

The primary goal of Module 2 is to build a functional application that interacts with an OpenEHR server to manage clinical data compositions.

**Key Requirements:**

1.  **EHR ID Creation:**
    *   Students are expected to create an Electronic Health Record (EHR) ID manually. This can be done using tools like Postman.
2.  **Application Functionality:**
    *   **Create Compositions:** The application must be able to create new compositions based on the template designed in Module 1. This involves creating a user interface (UI) for data entry.
    *   **List Compositions:** Display all compositions that exist for the specific template within the created EHR.
    *   **Delete Compositions:** Allow users to delete existing compositions.
    *   **(Optional) Edit Compositions:** Optionally, implement functionality for users to edit previously created compositions.
3.  **Target OpenEHR Server:**
    *   Primarily use the shared OpenEHR server provided by the bootcamp (e.g., `https://openehr-bootcamp.medblocks.com/ehrbase`).
    *   Local testing should be done using a Docker-based EHRbase instance.
4.  **Technology Stack:**
    *   Flexible: Students can choose any technology stack they are comfortable with (e.g., Python/Django for backend, Svelte for frontend). MedBlocks UI components are available but not mandatory.

## Key Concepts and Clarifications

### Template vs. Composition

*   **Template:**
    *   Defines the schema or structure for capturing clinical data (analogous to a form definition or a database schema).
    *   Created in Module 1 using tools like Archetype Designer.
*   **Composition:**
    *   An instance of a template containing actual patient data (analogous to a filled-out form or a record in a database).
    *   The application in Module 2 will focus on creating and managing these compositions.
*   **Analogy:** A template is the blueprint for a form; a composition is the form filled with specific information.

### Creating Compositions

*   The process involves building a UI that allows users to input data corresponding to the fields defined in the template.
*   This data is then structured according to the template and sent to the OpenEHR server.
*   Tools like MedBlocks UI can help generate a composition from a template, or one can start with an example composition (e.g., from the EHRbase `/example` endpoint) and modify it.

### OpenEHR vs. EHRbase

*   **OpenEHR:**
    *   An open standard and set of specifications for health data. It defines models, APIs, and query languages but is not a software application itself.
    *   Comparable to standards like HTTP, DICOM, or SQL.
*   **EHRbase:**
    *   An open-source software platform that implements the OpenEHR standard.
    *   It provides a persistent data repository and exposes OpenEHR-compliant REST APIs.
    *   Actively maintained, with significant contributions from companies like Intergroup (Germany).

## Tooling and Development Environment

### MedBlocks UI

*   **`AutoForm` Component:**
    *   Useful for quickly generating forms from simple templates.
    *   May not enforce all complex template validations client-side. Basic validations (e.g., min/max for `DV_QUANTITY`) might be supported, but thorough testing is needed.
*   **Individual Components:**
    *   Recommended for real-world scenarios requiring more control over UI/UX, styling, and validation logic.
    *   If the underlying OpenEHR template changes, the UI code using these components will likely need manual updates.

### EHRbase Local Setup (Docker)

*   **`docker-compose.yml`:**
    *   Used to define and run the multi-container EHRbase environment (typically EHRbase service + PostgreSQL database service).
*   **Passwords and Authentication:**
    *   **Database Level:** Credentials like `POSTGRES_USER`, `POSTGRES_PASSWORD`, `EHRBASE_DB_USER`, `EHRBASE_DB_ADMIN_PASSWORD` are configured in `docker-compose.yml` for the PostgreSQL database and the user EHRbase connects with.
    *   **EHRbase Service to Database:** The EHRbase service configuration within `docker-compose.yml` uses these credentials to establish a connection with its database.
    *   **HTTP Basic Authentication (EHRbase API):** Configured via environment variables like `SECURITY_AUTH_USER`, `SECURITY_AUTH_PASSWORD` (and admin equivalents) in `docker-compose.yml`. This is the authentication used for API calls (e.g., from Postman or the application).
*   **Environment Variables:** It was suggested as good practice to move sensitive environment variables (like passwords) from `docker-compose.yml` into a separate `.env` file (which would be gitignored).
*   **Running on Cloud VMs (e.g., AWS EC2):**
    *   Possible and a common practice.
    *   Micro instances might be underpowered for EHRbase; a more substantial VM may be needed.

### Other Tools

*   **Svelte:** Suggested as a beginner-friendly framework for frontend development, being close to HTML, CSS, and JavaScript.
*   **Postman:** Essential for testing API endpoints, manually creating EHRs, and can export cURL commands.
*   **Python/Django:** A viable option for building the backend logic of the application.

## Validation Logic

*   **Client-Side Validation:**
    *   Can be implemented in the UI (e.g., using MedBlocks UI components or custom code).
    *   Typically handles basic checks like required fields, data types, and simple range constraints.
*   **Backend Validation (EHRbase):**
    *   EHRbase performs comprehensive validation of incoming compositions against the specified template and OpenEHR rules.
    *   Error messages returned by EHRbase upon validation failure are generally instructive and help in debugging.

## Terminology Services

A significant portion of the discussion focused on the use and challenges of terminology services.

### Importance and Integration

*   Terminology is crucial for ensuring data is structured, standardized, and interoperable.
*   **EHRbase Integration with FHIR Terminology Servers:** EHRbase can be configured to validate terminology codes in compositions against any FHIR-compliant terminology server (e.g., Termex, Snowstorm). This allows OpenEHR systems to leverage existing FHIR-based terminology infrastructure.
*   **Application UI Integration:** The application itself is responsible for querying terminology servers (which could be FHIR-based) to provide features like auto-completion or selection lists for coded text fields.

### Types of Terminology Servers and Approaches

1.  **Local Database (e.g., PostgreSQL, MySQL):**
    *   Simplest approach: Import terminology files (e.g., SNOMED CT RF2 files) into database tables and use SQL for querying.
    *   Often sufficient for small to medium-scale applications needing value set validation or simple searches. Sidharth emphasized this as a good starting point due to its simplicity and reduced maintenance overhead compared to dedicated servers.
2.  **Search-Specific Services (e.g., Elasticsearch, Typesense):**
    *   Offer better performance for complex searches and can handle larger datasets more efficiently.
    *   Require separate setup and maintenance.
3.  **Specialized Health IT Terminology Servers (e.g., Snowstorm, Snow Owl, Hermes, Metriport, HAPI FHIR):**
    *   Provide advanced features like SNOMED CT Expression Constraint Language (ECL) queries, complex semantic operations, and comprehensive terminology management.
    *   Can be resource-intensive and overkill if only basic functionality is needed.
    *   Recommended FHIR-compliant servers mentioned for consideration (though not explicitly for "saving time" but as capable systems) include Snowstorm, Snow Owl, Hermes, Metriport, and HAPI FHIR.
    *   **Common Pattern:** Use a powerful terminology server to define complex value sets (e.g., via ECL queries) once, export the resulting flat list of codes, and load this list into the application's local database for routine validation and search operations.

### Challenges with Terminology

*   **Maintenance:** Terminologies (SNOMED CT, LOINC, ICD-10) are updated regularly. The terminology server and its data must be kept current.
*   **Complexity:** Setting up and maintaining full-fledged terminology servers (e.g., Snowstorm often requires Elasticsearch) can be complex.
*   **Synchronization with FHIR (as a general challenge):** While not explicitly detailed as a "synchronization with FHIR" problem, the instructor highlighted that managing and updating terminology is an ongoing challenge. The federated nature of FHIR APIs (where a terminology service might itself connect to multiple other sources) adds layers of complexity. Keeping data consistent across different systems and standards is inherently difficult.
*   **Mapping between Terminologies (e.g., SNOMED CT to ICD-10, local codes to SNOMED CT):**
    *   A highly challenging area with no perfect open-source solutions currently available.
    *   Often requires significant manual effort, domain expertise, and human oversight.
    *   Context is critical for accurate mapping. For example, mapping a lab code like "hemoglobin" requires knowing if it was measured in serum or whole blood, information often missing from the raw data and requiring human investigation.
    *   Mapping from a high-granularity system (like SNOMED CT) to a lower-granularity one (like ICD-10) is generally more feasible for automation than the reverse or between equally complex systems.
    *   The instructor mentioned that even with multiple human mappers working blindly on the same dataset, discrepancies are common, highlighting the subjective and context-dependent nature of mapping.
    *   **Role of AI (like ChatGPT):** AI tools like ChatGPT, potentially combined with search, can be useful for suggesting *potential candidate terms* for a mapping. However, they are not a complete solution and should be used to assist, not replace, human oversight and validation. The final decision on a mapping often requires expert review.

## OpenEHR Specifics Discussed

### Context Field in Templates

*   The `context` section is a mandatory part of an OpenEHR Composition.
*   It typically includes information like `start_time` (the time the overall clinical event or session began) and `setting` (e.g., home, hospital).
*   These fields might be auto-populated by the system or application rather than being manually entered by the user in a form.
*   Individual clinical entries within the composition (e.g., a blood pressure observation) can also have their own specific `time` fields, allowing for granularity if observations were made at different times within the same overall encounter. However, in many simple cases, these times align with the main composition context time.

### Template Design in Archetype Designer

*   **Cardinality:** Pay close attention to setting the correct cardinalities (e.g., 0..0 to exclude, 0..1 for optional, 1..1 for mandatory) for all relevant nodes and data elements within the template.
*   **Excluding Unnecessary Fields:** If an archetype contains optional sections or elements not needed for the specific template (e.g., "birth weight" in a general vital signs template, or "24-hour average" in blood pressure), these should be explicitly excluded by setting their cardinality to 0..0 at their own level, not just by removing their child nodes.

## General Advice for Module 2

*   This module represents a significant step up in complexity, especially for those new to programming or API interactions.
*   Students are encouraged to make use of one-on-one support sessions if they encounter difficulties.
*   The focus should be on successfully building an application that can perform the core CRUD (Create, Read, Update, Delete - though Update is optional) operations for compositions via the EHRbase API.

## Potentially Useful Questions, Solutions, and Clarifications from the Session

*   **MedBlocks UI `AutoForm` vs. Individual Components:** For simple templates, `AutoForm` is quick. For complex UIs, custom styling, and robust validation, individual components are better, though they require manual updates if the template changes.
*   **Client-Side vs. Backend Validation:** MedBlocks UI might do some basic client-side validation, but EHRbase handles comprehensive backend validation. Rely on EHRbase error messages for debugging.
*   **EHRbase Docker Password Configuration:** Clarification on which environment variables in `docker-compose.yml` control database-level access versus HTTP Basic Auth for the API.
*   **Creating Compositions without MedBlocks UI:** Start with an example composition from EHRbase, strip unnecessary fields, and use application logic to populate the required fields. EHRbase error messages will guide debugging.
*   **Template Design - Excluding Fields:** When excluding optional parts of an archetype (e.g., "24-hour average" in blood pressure), ensure the parent node itself is set to 0..0 cardinality, not just its children.
*   **OpenEHR `context` field:** It's mandatory in compositions (for `start_time`, `setting`) but often auto-populated, not manually entered in forms.
*   **Terminology Server Choice:** For small/medium needs, using your existing application database (e.g., PostgreSQL) to store and query terminology is often the simplest and recommended first approach. Full terminology servers add complexity and maintenance.
*   **SNOMED CT ECL Queries:** Powerful for defining value sets, but the resulting list of codes can then be used in simpler systems.
*   **Terminology Mapping (e.g., LOINC to SNOMED CT):** Still largely a manual, context-dependent process. Open-source tools are lacking. AI can suggest candidates but human oversight is essential.

## Miscellaneous Q&A Points

*   **Windows Development Environment:** Some students experienced challenges with Docker setup on work computers (potentially due to security restrictions) versus personal PCs.
*   **EHRbase API Endpoints:** Beyond the primary `/ehrbase` path, students might explore other EHRbase API endpoints (e.g., for listing uploaded templates). These can be found in the EHRbase documentation.
