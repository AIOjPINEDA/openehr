# openEHR Bootcamp Reference Guide

## Overview

The [openEHR Bootcamp by Medblocks](https://medblocks.com/openehr-bootcamp) is a 10-week, hands-on training program designed to guide participants from foundational openEHR concepts to the development of real-world healthcare applications. The bootcamp is suitable for both developers and healthcare professionals, focusing on practical skills, standards compliance, and interoperability with other key healthcare data models such as FHIR and OMOP CDM.

---

## Prerequisites & Tools

This course emphasizes hands-on development. You should have a foundational understanding of making HTTP requests and basic programming skills—especially using JavaScript for front-end development and Java for back-end processes. If you are new to these, use the following resources to get started:

- **Postman:** Tool for testing and developing APIs.  
  - [Postman Documentation](https://learning.postman.com/docs/getting-started/introduction/)
  - [Postman Beginner's Course (freeCodeCamp)](https://www.postman.com/prasandhkishorep/postman-beginner-s-course-freecodecamp/overview)
- **JavaScript:** Widely used for web development.  
  - [JavaScript Tutorial (MDN)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
  - [JavaScript Course (freeCodeCamp)](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/)
- **Svelte:** Front-end framework used in some bootcamp applications.  
  - [Svelte YouTube Tutorial](https://www.youtube.com/watch?v=zojEMeQGGHs)
- **Java:** Used for server-side applications and backend processes.  
  - [Java Documentation (Oracle)](https://docs.oracle.com/en/java/)
  - [Java Beginner's Tutorial (Telusko)](https://www.youtube.com/watch?v=eIrMbAQSU34)
- **openEHR:**  
  - [Official openEHR Documentation](https://specifications.openehr.org/)
  - [openEHR Community Forums](https://discourse.openehr.org/)

---

## Bootcamp Structure and Curriculum

The curriculum is organized into five progressive modules, each lasting two weeks:

| Weeks | Module Title                | Key Topics & Activities                                                                                     |
|-------|-----------------------------|-------------------------------------------------------------------------------------------------------------|
| 1-2   | Introduction to openEHR     | openEHR architecture, motivation, two-level modeling (Reference Model & Archetypes), use cases              |
| 3-4   | Archetypes & Templates      | Clinical Knowledge Manager (CKM), creating/editing archetypes, template design for real scenarios           |
| 5-6   | Data Modeling & Persistence | openEHR data structures (Compositions, EHR, Entry, Observations), AQL (Archetype Query Language)            |
| 7-8   | Application Development     | openEHR REST APIs, integration with servers (e.g., EHRbase), frontend basics, authentication/authorization  |
| 9-10  | Interoperability & Projects | FHIR integration, data mapping, real-world use cases, final project presentations                            |

---

## Learning Approach

- **Weekly Milestones:** Each week features a clear technical goal and deliverable.
- **Live Sessions:** Weekly live classes and bi-weekly demo sessions with expert instructors.
- **Mentorship:** One-on-one mentorship to resolve technical or conceptual challenges.
- **Peer Community:** Access to a collaborative group for discussion and support.
- **Active Projects:** Each participant develops a real-world use case from modeling to implementation.
- **Continuous Feedback:** Quizzes, code reviews, and project presentations ensure ongoing assessment and improvement.

---

## Technical Resources Provided

### Official Bootcamp Repository

- **GitHub Repository:** [medblocks/openehr-bootcamp](https://github.com/medblocks/openehr-bootcamp)
  - Contains exercises, sample code, templates, and step-by-step guides.
  - Example structure:
    - `/exercises`: Practical modeling and querying exercises
    - `/solutions`: Example solutions for self-assessment
    - `/templates`: Sample archetypes and templates for clinical scenarios
    - `/api-examples`: Scripts for API interaction
    - `README.md`: Main onboarding guide

### Core openEHR Tools

- **EHRbase:** Open-source openEHR server for storing and querying clinical data ([EHRbase](https://ehrbase.org/)).
  - The bootcamp primarily uses a local Docker-based setup for EHRbase (see `docs/guides/ehrbase_setup.md`).
- **Archetype Designer:** Tool for creating and editing openEHR archetypes ([Archetype Designer](https://tools.openehr.org/designer))
- **Clinical Knowledge Manager (CKM):** Repository of community-validated archetypes and templates ([openEHR CKM](https://ckm.openehr.org/ckm/))

### Advanced EHRbase Deployment: Cloud Hosting with Authentication

While the bootcamp focuses on a local EHRbase setup for development and learning, deploying EHRbase to a cloud environment for broader access or production-like scenarios involves additional considerations, particularly around security and accessibility.

The article "[Host An Authenticated EHRbase Server In The Cloud In Under 15 Mins](https://medblocks.com/blog/host-an-authenticated-ehrbase-server-in-the-cloud-in-under-15-mins#introduction)" by Medblocks provides a comprehensive guide for such a setup. Key aspects covered include:

*   **Cloud VPS Setup:** Using a Virtual Private Server (e.g., on AWS, Azure, GCP) with Ubuntu/Debian.
*   **Docker and Docker Compose:** As the foundation for deploying EHRbase and its dependencies.
*   **HTTPS/SSL with Traefik:** Implementing Traefik as a reverse proxy to manage SSL certificates (e.g., from Let's Encrypt) for secure HTTPS communication. This is crucial for protecting data in transit when EHRbase is exposed to the internet.
*   **Basic Authentication:** Configuring EHRbase for Basic Authentication (`SECURITY_AUTHTYPE: BASIC`) to control access to the server.
*   **Enhanced `docker-compose.yaml`:** The article provides a `docker-compose.yaml` that includes services for `postgres`, `ehrbase`, and `traefik`. It demonstrates:
    *   Persistent data volumes for PostgreSQL.
    *   Environment variables for database credentials and EHRbase security settings.
    *   CORS (Cross-Origin Resource Sharing) configuration.
*   **Comprehensive `init.sql`:** A more detailed PostgreSQL initialization script that sets up specific user roles, permissions, and database extensions suitable for a more robust deployment.

**Key Differences from Bootcamp Local Setup:**

*   **Security:** The cloud setup explicitly adds layers of security (HTTPS, Basic Authentication) not typically configured in the simplified local development environment.
*   **Accessibility:** Designed for access over the internet, requiring DNS configuration and a reverse proxy.
*   **Complexity:** The `docker-compose.yaml` and `init.sql` are more complex to handle the requirements of a public-facing, authenticated service.

This Medblocks article serves as an excellent reference for those looking to understand or implement a more production-ready EHRbase deployment. For the bootcamp's direct exercises, the local setup guide (`docs/guides/ehrbase_setup.md`) remains the primary reference.

### Integration and Automation

- **API Interaction:** Examples using REST APIs, Postman, and curl for automated data operations.
- **AQL Queries:** Sample Archetype Query Language scripts for extracting structured clinical data.
- **FHIR Integration:** Guidance and code for mapping openEHR data to FHIR resources.

### Documentation and Support

- **Video Tutorials:** 20+ hours of exclusive video content covering all modules.
- **Guides:** Step-by-step written tutorials for each exercise and project.
- **Community Forums:** Access to online discussion boards and peer support.

---

## Official openEHR Specifications and Resources

The [openEHR Specifications portal](https://specifications.openehr.org/) is the authoritative source for the technical and clinical standards that underpin the openEHR ecosystem. Bootcamp participants should use these resources to ensure standards-compliant modeling, implementation, and integration.

### Key Specification Links

- [openEHR Specifications Portal](https://specifications.openehr.org/)
- [Architecture Overview](https://specifications.openehr.org/releases/BASE/latest/architecture_overview.html)
- [UML Class Index](https://specifications.openehr.org/releases/RM/latest/class_index.html)
- [REST API Specification](https://specifications.openehr.org/releases/ITS-REST/latest/)
- [Archetype Formalism](https://specifications.openehr.org/releases/AM/latest/)
- [AQL Specification](https://specifications.openehr.org/releases/QUERY/latest/aql.html)
- [Conformance Specifications](https://specifications.openehr.org/releases/CONFORMANCE/latest/)

### Community and Implementation Support

- [openEHR Discourse Forums](https://discourse.openehr.org/)
- [openEHR Wiki](https://wiki.openehr.org/)
- [openEHR@GitHub](https://github.com/openEHR)

#### Best Practice

- **Start with the Architecture Overview** to understand the big picture.
- **Use the UML Class Index** when modeling or developing against the openEHR Reference Model.
- **Refer to the REST API documentation** for all API-based exercises.
- **Consult the Archetype and AQL specs** when designing clinical models or writing queries.
- **Participate in the community** for support, updates, and collaborative problem-solving.

---

## Interoperability and Data Transformation Context

### openEHR, FHIR, and OMOP: Complementary Roles

- **openEHR**: Best for detailed, semantically rich clinical data modeling and long-term EHR storage.
- **FHIR**: Best for real-time data exchange and interoperability between systems.
- **OMOP CDM**: Best for standardized analytics and research across large, heterogeneous datasets.

> “An interoperable health system would use openEHR to collect data, FHIR to transmit data between systems and organizations, and OMOP to find insights in the data.”  
> — [Tsafnat et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11040436)

### Mapping and Transformation

- **openEHR ↔ FHIR**: Use tools like the [openEHR2FHIR transformer](https://discourse.openehr.org/t/online-openehr2fhir-transformer/2606) and REST APIs for bidirectional conversion.
- **FHIR ↔ OMOP**: Use open-source ETL tools (e.g., [NACHC-CAD/fhir-to-omop](https://github.com/NACHC-CAD/fhir-to-omop)), configuration-based mappings, and the [FHIR-to-OMOP Implementation Guide](https://build.fhir.org/ig/HL7/fhir-omop-ig/).
- **openEHR ↔ OMOP**: Typically involves extracting data via AQL, mapping archetype elements to OMOP domains, and using terminology services for code translation.

#### Key Transformation Challenges

- **Structural differences**: openEHR’s hierarchical compositions vs. OMOP’s flat tables vs. FHIR’s resource bundles.
- **Terminology alignment**: Ensuring consistent mapping between SNOMED CT, LOINC, RxNorm, and OMOP concept IDs.
- **Information loss**: Some clinical context may not be preserved when moving to analytical or exchange models.
- **Validation**: Use conformance specs, community tools, and round-trip testing to ensure fidelity.

#### Tools for ETL and Mapping

- [WhiteRabbit & Rabbit-in-a-Hat](https://ohdsi.github.io/WhiteRabbit/) – ETL design and mapping for OMOP.
- [openEHR2FHIR transformer](https://discourse.openehr.org/t/online-openehr2fhir-transformer/2606) – openEHR to FHIR conversion.
- [NACHC-CAD/fhir-to-omop](https://github.com/NACHC-CAD/fhir-to-omop) – FHIR to OMOP ETL.

---

## Example Workflow

1. **Model a clinical scenario** using Archetype Designer and validate with CKM.
2. **Consult the [Architecture Overview](https://specifications.openehr.org/releases/BASE/latest/architecture_overview.html)** before starting new modules.
3. **Upload templates** to an EHRbase server.
4. **Create patient records** and persist clinical data via REST API.
5. **Query data** using AQL scripts.
6. **Validate your archetypes and templates** against the [Archetype Formalism](https://specifications.openehr.org/releases/AM/latest/).
7. **Integrate with FHIR** or map to OMOP for interoperability.
8. **Present final project** demonstrating end-to-end openEHR implementation.

---

## Best Practices Emphasized

- **Active, Project-Based Learning:** Build real applications, not just theoretical knowledge.
- **Modular Progression:** Each module builds on the previous, ensuring a logical learning path.
- **Mentorship & Feedback:** Direct access to experts and regular feedback accelerates learning.
- **Use of Open Standards:** Focus on community-validated archetypes and templates for interoperability.
- **Integration Readiness:** Prepares participants for real-world scenarios, including FHIR and OMOP mapping.
- **Reference Specifications:** Always consult the [official openEHR specifications](https://specifications.openehr.org/) for authoritative guidance.

---

## Certification

Upon successful completion of the bootcamp, participants receive a certificate of completion, validating their skills in openEHR modeling and application development.

---

## Key Links and References

- **Bootcamp Main Page:** [https://medblocks.com/openehr-bootcamp](https://medblocks.com/openehr-bootcamp)
- **GitHub Repository:** [https://github.com/medblocks/openehr-bootcamp](https://github.com/medblocks/openehr-bootcamp)
- **EHRbase:** [https://ehrbase.org/](https://ehrbase.org/)
- **Archetype Designer:** [https://tools.openehr.org/designer](https://tools.openehr.org/designer)
- **openEHR CKM:** [https://ckm.openehr.org/ckm/](https://ckm.openehr.org/ckm/)
- **openEHR Specifications:** [https://specifications.openehr.org/](https://specifications.openehr.org/)
- **openEHR Discourse Forums:** [https://discourse.openehr.org/](https://discourse.openehr.org/)
- **openEHR Wiki:** [https://wiki.openehr.org/](https://wiki.openehr.org/)
- **openEHR@GitHub:** [https://github.com/openEHR](https://github.com/openEHR)
- **Postman Documentation:** [https://learning.postman.com/docs/getting-started/introduction/](https://learning.postman.com/docs/getting-started/introduction/)
- **JavaScript Tutorial (MDN):** [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
- **JavaScript Course (freeCodeCamp):** [https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/)
- **Svelte YouTube Tutorial:** [https://www.youtube.com/watch?v=zojEMeQGGHs](https://www.youtube.com/watch?v=zojEMeQGGHs)
- **Java Documentation (Oracle):** [https://docs.oracle.com/en/java/](https://docs.oracle.com/en/java/)
- **Java Beginner's Tutorial (Telusko):** [https://www.youtube.com/watch?v=eIrMbAQSU34](https://www.youtube.com/watch?v=eIrMbAQSU34)

---

*This guide provides a consolidated reference for the openEHR Bootcamp, summarizing its curriculum, prerequisites, resources, tools, and best practices. For the most up-to-date materials and exercises, always refer to the official bootcamp repository and website.*
