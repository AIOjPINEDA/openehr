# openEHR Bootcamp Reference Guide

## Overview

The [openEHR Bootcamp by Medblocks](https://medblocks.com/openehr-bootcamp) is a 10-week, hands-on training program designed to guide participants from foundational openEHR concepts to the development of real-world healthcare applications. The bootcamp is suitable for both developers and healthcare professionals, focusing on practical skills, standards compliance, and interoperability with other key healthcare data models such as FHIR and OMOP CDM.

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

- **EHRbase:** Open-source openEHR server for storing and querying clinical data ([EHRbase](https://ehrbase.org/))
- **Archetype Designer:** Tool for creating and editing openEHR archetypes ([Archetype Designer](https://tools.openehr.org/designer))
- **Clinical Knowledge Manager (CKM):** Repository of community-validated archetypes and templates ([openEHR CKM](https://ckm.openehr.org/ckm/))

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

---

*This guide provides a consolidated reference for the openEHR Bootcamp, summarizing its curriculum, resources, tools, and best practices. For the most up-to-date materials and exercises, always refer to the official bootcamp repository and website.*
