# Module 1: Introduction to openEHR & Creating My First Template

## Overview
This module introduces the fundamentals of openEHR and guides you through creating your first template for capturing vital signs. The focus is on understanding the two-level modeling approach and applying it to a practical clinical scenario.

## Assignment Objective
Create an openEHR template for a nurse to capture patient vital signs during a hospital visit.

### Deliverables
1. A modeled openEHR template capturing:
   - Pulse
   - Blood Pressure (BP)
   - Oxygen Saturation (SpO2)
   - Height
   - Weight

2. Template requirements:
   - Template ID must include your name (using standard English characters)
   - Template must be posted to the bootcamp's shared openEHR server
   - Base URL: [https://openehr-bootcamp.medblocks.com/ehrbase](https://openehr-bootcamp.medblocks.com/ehrbase)

## Learning Path

### 1. Core openEHR Concepts

#### Two-Level Modeling
- **Reference Model (RM)**: The stable, technical foundation
- **Archetypes & Templates**: The clinical content layer

#### Key Components
- **Archetypes**: Reusable, fine-grained clinical concepts that define the maximum possible data structure
- **Templates**: Constrained sets of archetypes combined for specific use cases, defining the minimum dataset required
- **Compositions**: Clinical documents containing entries
- **Entry Types**:
  - **Observation**: Data obtained through observation (vital signs, symptoms)
  - **Evaluation**: Clinical judgments (diagnoses)
  - **Instruction**: Plans or requests (prescriptions)
  - **Action**: Execution of instructions (medication administration)
  - **Admin Entry**: Administrative data
- **Clusters**: Reusable groups of data points used within other entry types

### 2. Modeling Tools

#### Recommended Tool
- **Better Archetype Designer** (tools.openehr.org)
  - Web-based, accessible across platforms
  - Requires account creation
  - Supports Git integration

#### Alternative Tools
- ADL Workbench (Free & Open Source)
- Archetype Editor (Free & Open Source)
- Ocean Template Designer (Commercial)
- Link EHR Studio (Free & Open Source)
- NeedApp Visual Studio (Commercial)

### 3. Template Formats and Specifications
- **OPT (Operational Template) XML**: Primary output format, verbose, meant for system consumption
- **Web Template**: More human-readable format (often JSON), easier for troubleshooting

#### ADL (Archetype Definition Language)
- **ADL 1.4**: The widely adopted standard by most vendors
- **ADL 2.0**: Introduced breaking changes, but has limited adoption
- **Current Recommendation**: For practical purposes and current implementations, stick with ADL 1.4

### 4. openEHR Ecosystem
- **Clinical Knowledge Manager (CKM)**: Central repository for archetypes and templates
- **Modeling Tools**: For creating archetypes and templates
- **Clinical Decision Support Tools**: Including GDL2 editors
- **CDR Platforms**: Both open-source and commercial options

## Development Environment Setup

A crucial part of this module is setting up your local openEHR server, EHRbase, and your API testing tool, Postman. We have prepared detailed guides to walk you through these processes:

*   **[EHRbase Setup Guide for the Bootcamp](../../docs/guides/ehrbase_setup.md)**
*   **[Postman Setup Guide for openEHR Bootcamp](../../docs/guides/postman_guide.md)**

Please follow these guides to get EHRbase up and running and Postman configured before proceeding with the module's assignments and API interactions.

## Implementation Guide

### Step 1: Research Archetypes
1. Access the Clinical Knowledge Manager (CKM)
2. Search for relevant archetypes:
   - Use the "Find Resources" tab for powerful searching
   - Search for clinical terms if exact names are unknown
   - Review "use and misuse" sections in documentation

### Step 2: Create a Template
1. Access the Archetype Designer
2. Create a new template
3. Import archetypes individually (avoid bulk imports)
   - Blood Pressure
   - Pulse/Heart Rate
   - Pulse Oximetry (for SpO2)
   - Height
   - Weight

### Step 3: Configure the Template
1. Organize archetypes using sections (Ad Hoc Heading)
2. Adjust cardinality (occurrences) as needed
   - Consider which elements should be mandatory (1..1) vs. optional (0..1)
3. Remove unnecessary elements
   - Set occurrences to 0..0 or use the hide option
4. Extract components for potential reuse

### Step 4: Export and Upload
1. Save the template with a unique ID including your name
2. Export as an OPT (Operational Template) file
3. Use Postman/Insomnia to upload to the bootcamp server
   - Ensure correct environment is selected
   - Use the provided API endpoint

## Troubleshooting Guide

### Common Challenges

#### Finding Archetypes
- **Problem**: Searching for "SpO2" doesn't find the right archetype
- **Solution**: Search for "Pulse oximetry" or use the "Find Resources" tab

#### Template Versioning
- **Problem**: Confusion between semantic versioning and Template IDs
- **Solution**: Use unique Template IDs for server uploads, especially for breaking changes

#### Template Upload Issues
- **Problem**: Upload fails in Postman/Insomnia
- **Solution**: Verify correct environment is selected and Template ID is unique

#### Archetype Versions
- **Problem**: Using outdated archetype versions
- **Solution**: Import archetypes individually after verification from CKM

#### Template Authoring Errors
- **Problem**: Template authoring is error-prone, often requiring multiple versions
- **Solution**:
  - Double-check cardinality constraints
  - Ensure all necessary elements are included
  - Use the web template format (JSON) for easier troubleshooting than OPT XML
  - Avoid direct OPT XML manipulation; use proper tooling instead

#### Platform Access Issues
- **Problem**: Access denied to modeling platforms
- **Solution**: Contact support/instructors for assistance

## Technology Comparison

### openEHR vs. FHIR
- openEHR excels in capturing deep clinical semantics and longitudinal records
- openEHR's two-level modeling handles varying data granularity well
- FHIR is generally considered easier for application developers initially
- Integration between openEHR and FHIR is possible through various patterns:
  - **Facade**: Presenting a FHIR interface on top of an openEHR CDR for reads/writes
  - **Synchronization**: Keeping data in both openEHR and FHIR servers in sync
  - **Hybrid approaches**: Combining different integration methods
  - These integrations typically use declared mappings between AQL paths (openEHR) and FHIR paths

### openEHR vs. Data Lakes
- openEHR is a standard for clinical data modeling, not a specific storage technology
- An openEHR CDR could be implemented on top of data lake infrastructure
- The key difference is in query approaches: AQL/SQL vs. optimized analytics formats

## Resources

### Official Documentation
- [openEHR Architecture Overview](https://specifications.openehr.org/releases/BASE/latest/architecture_overview.html)
- [openEHR Specifications Home](https://specifications.openehr.org/)
- [Clinical Knowledge Manager (CKM)](https://ckm.openehr.org/ckm/)

### Relevant Archetypes
These archetypes can be found in the Clinical Knowledge Manager (CKM) after logging in:
- Blood Pressure (openEHR-EHR-OBSERVATION.blood_pressure.v2)
- Pulse/Heart Rate (openEHR-EHR-OBSERVATION.pulse.v2)
- Respiration (openEHR-EHR-OBSERVATION.respiration.v2)
- Body Temperature (openEHR-EHR-OBSERVATION.body_temperature.v2)
- Pulse Oximetry (openEHR-EHR-OBSERVATION.pulse_oximetry.v2) (for SpO2)
- Height (openEHR-EHR-OBSERVATION.height.v2)
- Weight (openEHR-EHR-OBSERVATION.body_weight.v2)

### Tutorials
- [What is openEHR and How Do I use it?](https://www.youtube.com/watch?v=Zn4Muj2IOlM) (YouTube)
- [openEHR step by step tutorial](https://www.youtube.com/watch?v=mqV6QQ-aaDA) (YouTube)

## Next Steps
After completing this module, proceed to [Module 2: Building My First openEHR App](../module-2-first-app/README.md) where you'll create a web application that uses this template.

## Sources
- [Medblocks OpenEHR Bootcamp - Module 1](https://medblocks.com/openehr-bootcamp)
- Module 1 Kickoff Summary (module-1-kickoff-summary.md)
- Transcript from Class 2 (transcript_class_2.md)
- [OpenEHR Foundation Resources](https://openehr.org/)
