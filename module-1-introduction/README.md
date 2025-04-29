# Module 1: Introduction to openEHR & Creating My First Template

This module covers the fundamentals of openEHR and guides me through creating my first openEHR template for capturing vital signs.

## Assignment Specification

A nurse wants to capture the patient's vital signs when they visit the hospital. Our task is to help by creating an appropriate openEHR template.

### Requirements

1. Model an openEHR template to capture basic vital signs including:
   - Pulse
   - BP (Blood Pressure)
   - SpO2 (Oxygen Saturation)
   - Height
   - Weight

2. The template ID should include your name for identification.
   - Use standard English characters to avoid potential issues with special characters or emojis.

3. Post the openEHR template to the bootcamp's shared openEHR server.
   - Base URL: [https://openehr-bootcamp.medblocks.com/ehrbase](https://openehr-bootcamp.medblocks.com/ehrbase)

## Learning Objectives

- Understand the core principles and architecture of openEHR
- Learn about the two-level modeling approach (Reference Model & Archetypes)
- Explore the Clinical Knowledge Manager (CKM) and find relevant archetypes
- Create a template for capturing basic vital signs using the Archetype Designer

## Key Concepts to Master

### openEHR Architecture

- Reference Model (RM)
- Archetypes and Templates
- Compositions and Entries
- Two-level modeling approach

### Core openEHR Concepts

#### Archetypes
Reusable, fine-grained clinical concepts (e.g., Pulse, Blood Pressure, Height, Weight, SpO2). They define the **maximum possible data structure** for a concept.

#### Templates
Constrained sets of archetypes or parts of archetypes combined for a specific clinical use case or form (e.g., "Nursing Vital Signs Form"). They define the **minimum dataset required** and allow for local variations (cardinality, terminology bindings). Templates are the fundamental interoperability blocks in openEHR when posting data.

#### Entry Types
Different categories of clinical data structures within archetypes, used in compositions:

- **Observation:** Data obtained through observation (e.g., vital signs, signs/symptoms reported by patient)
- **Evaluation:** A clinical decision or judgment based on observations (e.g., diagnosis)
- **Instruction:** A plan or request for action (e.g., prescription order, procedure request)
- **Action:** The execution of an instruction (e.g., administering medication, performing a procedure)
- **Admin Entry:** Miscellaneous administrative or non-clinical data

#### Clusters
Reusable groups of data points that describe a specific aspect, often used *within* other Entry types (e.g., "Level of Exertion" cluster used within a Blood Pressure observation, "Circular Anatomical Location" cluster describing a body site). A cluster is a general concept that is not typically recorded on its own but in the context of another entry.

### Clinical Knowledge Manager (CKM)

- Searching for archetypes
- Understanding archetype metadata
- Evaluating archetype quality and maturity
- The central repository for openEHR archetypes and some templates
- CKM archetype pages contain documentation, including "use and misuse" sections

### openEHR Modeling Tools

#### Recommended Tool for Bootcamp
- **Better Archetype Designer (tools.openehr.org):** A web-based tool chosen for tutorials due to ease of access across different operating systems.
  - Requires account creation
  - Supports local repositories or Git synchronization
  - Not open source

#### Other Available Tools
- ADL Workbench (Free & Open Source)
- Archetype Editor (Free & Open Source)
- Ocean Template Designer (Commercial, but also developed CKM)
- Link EHR Studio (Free & Open Source - pronounced "Linker")
- NeedApp Visual Studio (Commercial, primarily used by NeedApp)

#### Using Archetype Designer
- Creating a new template
- Adding archetypes to a template
- Constraining archetypes for specific use cases
- Validating and exporting templates
- Using sections (Ad Hoc Heading) to organize templates
- Extracting components for reuse

### Template Formats

- **OPT (Operational Template) XML:** The primary output format from modeling tools. It's verbose and not easy to read or troubleshoot directly. It's a compiled artifact meant to be consumed by systems, not manually edited.
- **Web Template:** An alternative, more human-readable format (often JSON) derived from the OPT, which is easier for diffing and troubleshooting.

### openEHR Specification Versions

- **ADL (Archetype Definition Language):** The language used to define archetypes and templates.
  - **ADL 1.4:** The widely adopted standard by most vendors.
  - **ADL 2.0:** Introduced breaking changes, but has limited adoption.
  - **Current Recommendation:** For practical purposes and current implementations, stick with ADL 1.4.

## Project: Vital Signs Template

I'll create a template for capturing basic vital signs including:

- Blood Pressure (Systolic and Diastolic)
- Heart Rate (Pulse)
- Oxygen Saturation (SpO2)
- Height
- Weight

### Implementation Steps

1. Research existing vital signs archetypes in the CKM
   - Use the "Find Resources" tab for more powerful searching
   - Be aware that some terms may have clinical names (e.g., "Pulse oximetry" for SpO2)

2. Create a new template in the Archetype Designer
   - Ensure proper access to the learning platform/environment

3. Add and configure the appropriate archetypes
   - Import archetypes individually to ensure correct versions
   - Be cautious with bulk imports which might bring outdated versions
   - Use sections (Ad Hoc Heading) to organize related archetypes

4. Constrain the archetypes as needed for my use case
   - Adjust cardinality (occurrences) as appropriate
   - Remove unnecessary elements by setting occurrences to 0..0
   - Consider making critical elements mandatory (1..1)

5. Validate and export the template
   - Export as an OPT (Operational Template) file
   - Ensure the Template ID includes my name and is unique

6. Upload the template to the bootcamp server
   - Use the provided Postman/Insomnia collection
   - Ensure the correct environment is selected

## Resources

### Official Documentation

- [openEHR Architecture Overview](https://specifications.openehr.org/releases/BASE/latest/architecture_overview.html)
- [Archetype Designer User Guide](https://ehrscape.marand.si/designerhelp/index.html)
- [CKM User Guide](https://ckm.openehr.org/ckm/help)

### Tutorials and Guides

- [Introduction to openEHR](https://www.youtube.com/watch?v=kOU2HGqK23o) (YouTube)
- [Creating Templates with Archetype Designer](https://www.youtube.com/watch?v=DRbBjqWzcz0) (YouTube)

### Relevant Archetypes

- [Blood Pressure](https://ckm.openehr.org/ckm/archetypes/1013.1.3574)
- [Pulse/Heart Rate](https://ckm.openehr.org/ckm/archetypes/1013.1.3621)
- [Respiration](https://ckm.openehr.org/ckm/archetypes/1013.1.3640)
- [Body Temperature](https://ckm.openehr.org/ckm/archetypes/1013.1.3668)
- [Pulse Oximetry](https://ckm.openehr.org/ckm/archetypes/1013.1.3620) (for SpO2)

## Notes and Progress

I'll document my learning journey and progress here as I work through this module.

### Day 1: Understanding openEHR Basics

Key learnings:
- openEHR is fundamentally a standard for clinical data modeling and storage structure, not a specific storage technology itself
- The two-level modeling approach separates the reference model (stable) from clinical content (archetypes and templates)
- openEHR excels in capturing deep, complex clinical semantics and building longitudinal health records from diverse sources

### Day 2: Exploring the CKM

Tips for effective archetype searching:
- Use the "Find Resources" tab for more powerful searching across all fields
- Search for clinical terms if you don't know the exact archetype name
- Review the "use and misuse" sections in archetype documentation
- Check archetype versions - always try to use the latest validated version

### Day 3: Creating My First Template

Practical implementation notes:
- Organize related archetypes using sections (Ad Hoc Heading)
- Adjust cardinality (occurrences) based on clinical requirements
- Remove unnecessary elements to simplify the template
- Extract components for reuse in other templates
- Export as OPT (Operational Template) XML for uploading to the server

## Troubleshooting and Common Challenges

### Finding the Right Archetypes
- **Challenge**: Searching for "SpO2" doesn't find the right archetype
- **Solution**:
  - Use the "Find Resources" tab for more powerful searching across all fields
  - Search for clinical terms if you don't know the exact archetype name (e.g., "oximetry" instead of "SpO2")
  - Use external resources like Google to identify the correct medical concept

### Template Versioning
- **Challenge**: Confusion between semantic versioning and Template IDs
- **Solution**:
  - Understand that Archetype Designer handles semantic versioning automatically (e.g., 1.0.0 to 1.0.1)
  - Use unique Template IDs for server uploads, especially for breaking changes
  - Consider including version numbers in the Template ID itself (e.g., my_template_v1, my_template_v2)

### Template Upload Issues
- **Challenge**: Template upload fails in Postman/Insomnia
- **Solution**:
  - Verify the correct environment is selected in Postman/Insomnia
  - Ensure the Template ID doesn't already exist on the server (unless overwriting)
  - Check that the OPT file is valid and properly formatted

### Archetype Versions
- **Challenge**: Accidentally using outdated archetype versions
- **Solution**:
  - Import archetypes individually after verifying they are the correct versions from CKM
  - Be cautious with bulk imports which might bring outdated versions
  - Check the archetype details and compare with CKM if unsure

### Template Authoring Errors
- **Challenge**: Template authoring is error-prone, often requiring multiple versions
- **Solution**:
  - Double-check cardinality constraints
  - Ensure all necessary elements are included
  - Use the web template format (JSON) for easier troubleshooting than OPT XML
  - Avoid direct OPT XML manipulation; use proper tooling instead

### Platform Access Issues
- **Challenge**: Access denied to modeling platforms
- **Solution**: Contact support/instructors for assistance

## openEHR Platforms and Servers

### Open-Source Options
- **Airbase:** The server used for the bootcamp. Described as the most well-maintained, fully implemented (according to the REST API spec), and properly vetted open-source openEHR server.
- **EHR Server:** Another open-source option (in Java) but does not implement the REST API spec 100%.
- **Ethersys:** A predecessor to Airbase, less actively maintained (last commit several years ago) and not up-to-date with the current spec.

### Commercial Vendors
Numerous companies provide openEHR-based platforms and tools (Better, Code24, NeedApp, Ocean, etc.). A list is available on openehr.org under "Tools and Products".

### openEHR Ecosystem Overview
The ecosystem includes:
- Modeling tools (like Archetype Designer)
- Clinical decision support (CDS) tools/repositories (like GDL2 editors)
- Knowledge management tools
- CDR (Clinical Data Repository) platforms

## Comparison with Other Technologies

### openEHR vs. FHIR
- openEHR excels in capturing deep clinical semantics and building longitudinal records
- openEHR's two-level modeling handles varying data granularity well
- FHIR is generally considered easier for application developers initially
- Integration between openEHR and FHIR is possible through various patterns:
  - Facade: Presenting a FHIR interface on top of an openEHR CDR
  - Synchronization: Keeping data in both systems in sync
  - Hybrid approaches

### openEHR vs. Data Lakes
- openEHR CDRs and data lakes are often separate solutions
- An openEHR CDR could potentially be implemented on top of data lake infrastructure
- The key difference is in how data is queried: AQL/SQL in openEHR vs. SQL on optimized formats in data lakes

## Next Steps

After completing this module, I'll move on to [Module 2: Building My First openEHR App](../module-2-first-app/README.md) where I'll create a web application that uses this template.

## Sources

This module outline is based on:

- [Medblocks OpenEHR Bootcamp - Module 1](https://medblocks.com/openehr-bootcamp) - "Introduction to openEHR & Create Your First Template"
- Module 1 Kickoff Summary (module-1-kickoff-summary.md)
- Transcript from Class 2 (transcript_class_2.md)
- [OpenEHR Foundation Resources](https://openehr.org/)
- [Clinical Knowledge Manager Documentation](https://ckm.openehr.org/ckm/)
