# OpenEHR Glossary

This glossary provides definitions for key terms and concepts used in the OpenEHR ecosystem. Understanding these terms is essential for working effectively with OpenEHR.

## Core Concepts

### OpenEHR
An open standard specification for the management, storage, retrieval, and exchange of health data in electronic health records. It provides a comprehensive and flexible approach to electronic health records with a focus on interoperability.

### Two-Level Modeling
OpenEHR's approach to separating technical concerns (Reference Model) from clinical content modeling (Archetypes and Templates). This separation allows for greater flexibility and future-proofing of health data.

### Reference Model (RM)
The stable, technical foundation of the OpenEHR architecture that defines the logical structure of electronic health records, including data types, data structures, and the relationships between them.

## Data Modeling

### Archetype
A computable definition of a domain-level concept, expressed as constraints on the Reference Model. Archetypes define the structure and semantics of information for clinical concepts (e.g., blood pressure, medication order).

### Template
A composition of archetypes configured for a specific use case or context, such as a specific form, document, or screen. Templates constrain and combine archetypes to create usable data entry and display formats.

### Operational Template (OPT)
A flattened, technically processable form of a template that can be directly used by OpenEHR systems for data validation and form generation.

### Clinical Knowledge Manager (CKM)
A web-based tool and repository for the collaborative development, management, and publishing of OpenEHR archetypes and templates.

### Archetype Designer
A web-based tool for creating and editing OpenEHR archetypes and templates.

## Data Structures

### Composition
The top-level structure in the OpenEHR health record, representing a clinical document (e.g., a consultation note, discharge summary, or test result).

### Section
A navigational structure within a composition that helps organize entries into logical groups (e.g., "Vital Signs", "Medication", "Assessment").

### Entry
The primary clinical content within a composition. Entries include:
- **Observation**: Records of clinical observations (e.g., blood pressure readings)
- **Evaluation**: Clinical assessments, diagnoses, or interpretations
- **Instruction**: Orders or prescriptions for actions to be performed
- **Action**: Records of activities that have been performed

### Cluster
A reusable structure for grouping related data items (e.g., a group of related measurements).

### Element
The lowest level data item in the OpenEHR model, representing a single piece of information (e.g., systolic blood pressure value).

## Query and Access

### Archetype Query Language (AQL)
A query language specifically designed for retrieving clinical data from OpenEHR-based systems. AQL allows querying based on archetype paths and structures.

### REST API
The standard interface for interacting with OpenEHR systems, allowing for the creation, retrieval, update, and deletion of health records and their components.

### EHRbase
An open-source implementation of the OpenEHR specification, providing a server for storing and querying clinical data.

## Terminology and Semantics

### Terminology Binding
The association of archetype data elements with external terminology codes (e.g., SNOMED CT, LOINC) to provide standardized semantics.

### Ontology
In OpenEHR, a section of an archetype that defines the terms and constraints used within the archetype, including bindings to external terminologies.

## Implementation Concepts

### Web Template
A simplified JSON representation of an OpenEHR template, designed for easier consumption by web applications.

### Composition
A JSON document representing a clinical document, structured according to the constraints defined in archetypes and templates.

### EHR (Electronic Health Record)
In OpenEHR, a container for all health information about a single patient. Each patient has one EHR that contains all their health data over time.

### Contribution
A set of changes to an EHR made during a single interaction with the system, similar to a transaction in database terms.

### Version
A specific state of a versioned object (like a composition) at a point in time. OpenEHR maintains the version history of clinical documents.

## Interoperability

### FHIR (Fast Healthcare Interoperability Resources)
A standard for healthcare data exchange that can be used alongside OpenEHR. While OpenEHR focuses on comprehensive clinical modeling, FHIR provides a more lightweight approach to interoperability.

### OMOP (Observational Medical Outcomes Partnership)
A common data model for standardizing health data from different sources, often used for research and analytics. OpenEHR data can be mapped to OMOP for research purposes.

## Additional Resources

For more detailed information on OpenEHR terminology, refer to:

- [OpenEHR Architecture Overview](https://specifications.openehr.org/releases/BASE/latest/architecture_overview.html)
- [OpenEHR Glossary](https://specifications.openehr.org/releases/BASE/latest/docs/support/glossary/master.html)

## Sources

This glossary is compiled from:

- [OpenEHR Specifications](https://specifications.openehr.org/)
- [OpenEHR Glossary](https://specifications.openehr.org/releases/BASE/latest/docs/support/glossary/master.html)
- [Medblocks OpenEHR Bootcamp](https://medblocks.com/openehr-bootcamp)
- [EHRbase Documentation](https://ehrbase.readthedocs.io/en/latest/)
- Personal bootcamp reference document (bootcamp_reference.md)
