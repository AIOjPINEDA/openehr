# OpenEHR Bootcamp - Module 2: Unified Kickoff Summary

This document provides a consolidated overview of the key concepts, requirements, and technical guidance for Module 2, focusing on building your first OpenEHR application.

## 1. Module 2 Assignment: First OpenEHR Application

### Assignment Goals
Develop a web application to manage vital signs data using the OpenEHR template created in Module 1. This application will interact with an OpenEHR server (EHRbase).

### Core Requirements
Your application must implement the following functionality:

1.  **EHR ID Creation:**
    *   Manually create an Electronic Health Record (EHR) ID using tools like Postman before using the application.
2.  **Create New Vital Signs Compositions:**
    *   Utilize the Vital Signs template from Module 1.
    *   Develop a User Interface (UI) for data entry to create new composition instances with patient data.
3.  **List Existing Compositions:**
    *   Display all compositions for your specific template within a given EHR ID.
    *   Present composition data in a readable format.
4.  **Delete Compositions:**
    *   Enable users to remove existing compositions safely.
5.  **Optional: Edit Compositions:**
    *   Implement functionality to modify existing composition data (recommended for learning).

### Technical Flexibility & Prerequisites
*   **Technology Stack:** You are free to choose any programming language or framework (e.g., Python/Django for backend, Svelte for frontend). MedBlocks UI components are available but not mandatory.
*   **Architecture:** Frontend-only, full-stack, or desktop GUI applications are acceptable (web applications preferred).
*   **Target OpenEHR Server:**
    *   Primarily use the shared OpenEHR server provided by the bootcamp (e.g., `https://openehr-bootcamp.medblocks.com/ehrbase`).
    *   Conduct local testing using a Docker-based EHRbase instance.
*   **Prerequisites:**
    *   The Vital Signs template from Module 1 must be available and deployed on the server.

## 2. Core OpenEHR Concepts

Understanding these concepts is crucial for developing OpenEHR applications:

### Template: The Unfilled Form
*   **Analogy:** A blank form or a database schema.
*   **Definition:** Defines the structure, data types, and constraints for capturing clinical information.
*   **Characteristics:** Based on OpenEHR archetypes, reusable across patients. Created in Module 1 (e.g., using Archetype Designer).

### EHR (Electronic Health Record): The Patient File
*   **Analogy:** An individual patient\'s medical file folder.
*   **Definition:** A container for all clinical data (compositions) for a single patient.
*   **Characteristics:** One EHR per patient, identified by a persistent patient identifier.
![alt text](https://specifications.openehr.org/releases/RM/latest/ehr/diagrams/high_level_ehr_structure.svg)

### Composition: The Filled Form
*   **Analogy:** A completed form with specific patient data.
*   **Definition:** An instance of a template populated with actual clinical observations and data.
*   **Characteristics:** Always belongs to a specific EHR and is based on a specific template.
![alt text](https://specifications.openehr.org/releases/BASE/latest/architecture_overview/diagrams/composition_structure.png)

### Relationship Hierarchy
```
EHR (Patient File)
├── Composition 1 (Based on Template A, e.g., Vital Signs - Visit 1)
├── Composition 2 (Based on Template A, e.g., Vital Signs - Visit 2)
└── Composition N (Based on Template B, C, etc.)
```

## 3. Composition Data Formats

OpenEHR systems support multiple data formats for compositions:

*   **Canonical JSON:** Traditional, verbose, detailed OpenEHR format with all metadata. Supported by all systems.
*   **Canonical XML:** XML version of the canonical format, with a one-to-one mapping to canonical JSON.
*   **Flat JSON (Simplified):** Flattened key-value pair structure, more readable and easier to work with programmatically. Removes non-essential metadata. **Recommended for beginners.**
*   **Structured JSON (Simplified):** Nested simplified format, offering a balance between flat and canonical, good for complex templates.

**Recommendation:** Start with Flat JSON for simplicity. Experiment with other formats to understand their trade-offs.

## 4. Creating and Managing Compositions

### Process
1.  **UI Development:** Build an interface allowing users to input data according to the template fields.
2.  **Data Structuring:** Structure the collected data according to the chosen composition format (e.g., Flat JSON) and the template definition.
3.  **API Interaction:** Send the structured data to the OpenEHR server via REST API to create a new composition.
4.  **Example Composition Endpoint:** EHRbase provides an `/example` endpoint that can generate a sample composition from your template. This is a good starting point to understand the expected structure.

### API for Compositions
*   Refer to the OpenEHR REST API specifications and the bootcamp's Postman collections for detailed API calls.
*   Key operations include creating, retrieving, updating (optional), and deleting compositions.

## 5. OpenEHR vs. EHRbase

*   **OpenEHR:** An open standard and set of specifications for health data, defining models, APIs, and query languages (like SQL or HTTP for their respective domains). It is not software itself.
*   **EHRbase:** An open-source software platform that implements the OpenEHR standard. It acts as a persistent data repository and exposes OpenEHR-compliant REST APIs.

## 6. Tooling and Development Environment

### EHRbase Local Setup (Docker)
*   Use `docker-compose.yml` to run EHRbase (service + PostgreSQL database).
*   Manage database credentials and API authentication (HTTP Basic Auth) via environment variables in `docker-compose.yml` or, preferably, a separate `.env` file (git-ignored).

### MedBlocks UI
*   **`AutoForm` Component:** Useful for quickly generating forms from simple templates. May have limitations with complex client-side validation.
*   **Individual Components:** Recommended for more control over UI/UX, styling, and validation. Requires manual updates if the underlying template changes.

### Other Recommended Tools
*   **Svelte:** Beginner-friendly frontend framework.
*   **Postman:** Essential for testing API endpoints, manual EHR creation, and exploring API responses.
*   **Python/Django:** Viable for backend development.

## 7. Data Validation

*   **Client-Side Validation:** Implement in the UI for basic checks (required fields, data types, simple ranges). MedBlocks UI components might offer some.
*   **Backend Validation (EHRbase):** EHRbase performs comprehensive validation of incoming compositions against the template and OpenEHR rules. EHRbase error messages are instructive for debugging.

## 8. Terminology Services

*   **Importance:** Crucial for standardized and interoperable data.
*   **EHRbase Integration:** Can validate terminology codes against FHIR-compliant terminology servers (e.g., Termex, Snowstorm).
*   **Application UI Integration:** The application is responsible for querying terminology services for features like auto-completion.
*   **Approaches for Terminology:**
    *   **Local Database (e.g., PostgreSQL):** Simplest for small/medium needs. Import terminology files (e.g., SNOMED CT RF2) and query using SQL. **Recommended starting point.**
    *   **Search-Specific Services (e.g., Elasticsearch):** Better for complex searches.
    *   **Specialized Health IT Terminology Servers (e.g., Snowstorm, HAPI FHIR):** Advanced features, but can be resource-intensive.
*   **Challenges:** Maintenance (updates), complexity of setup, mapping between terminologies (highly manual, context-dependent; AI can assist but not replace human oversight).

## 9. Key OpenEHR Specifics for Module 2

### `context` Field in Compositions
*   A mandatory section in every OpenEHR Composition.
*   Includes `start_time` (of the clinical event/session) and `setting` (e.g., home, hospital).
*   Often auto-populated by the system/application rather than manual user entry.
*   Individual observations within a composition can have their own specific `time` fields.

### Template Design in Archetype Designer
*   **Cardinality:** Carefully set cardinalities (e.g., `0..0` to exclude, `0..1` for optional, `1..1` for mandatory) for all nodes.
*   **Excluding Fields:** To exclude optional archetype sections/elements not needed in your template, set their cardinality to `0..0` at their own level.

## 10. Development Strategy & Success Criteria

### Recommended Approach
1.  **Start Simple:** Use the example endpoint to understand data structure.
2.  **Choose Format:** Select a composition format (e.g., Flat JSON).
3.  **Implement CRUD:** Build Create, Read, (Update - optional), Delete operations incrementally.
4.  **Test Thoroughly:** Use Postman to verify API interactions.
5.  **Iterate:** Refine UI and functionality.

### Success Criteria
*   **Functionality:** All required features working.
*   **OpenEHR Compliance:** Proper use of APIs and data formats.
*   **Code Quality:** Clean, readable, maintainable.
*   **User Interface:** Intuitive and practical.
*   **Documentation:** Clear setup/usage instructions.

## 11. Next Steps
1.  Review your Module 1 Vital Signs template.
2.  Create an EHR and post your first composition manually (e.g., via Postman, following relevant guides).
3.  Set up your development environment.
4.  Explore OpenEHR REST APIs.
5.  Plan and start building your application.

*This module transitions from clinical modeling theory to practical application development, building upon Module 1.*
