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

2. The template ID should include your name.

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

### Clinical Knowledge Manager (CKM)

- Searching for archetypes
- Understanding archetype metadata
- Evaluating archetype quality and maturity

### Archetype Designer

- Creating a new template
- Adding archetypes to a template
- Constraining archetypes for specific use cases
- Validating and exporting templates

## Project: Vital Signs Template

I'll create a template for capturing basic vital signs including:

- Blood Pressure
- Heart Rate
- Respiratory Rate
- Body Temperature
- Oxygen Saturation (SpO2)

### Implementation Steps

1. Research existing vital signs archetypes in the CKM
2. Create a new template in the Archetype Designer
3. Add and configure the appropriate archetypes
4. Constrain the archetypes as needed for my use case
5. Validate and export the template

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
- [Pulse Oximetry](https://ckm.openehr.org/ckm/archetypes/1013.1.3620)

## Notes and Progress

I'll document my learning journey and progress here as I work through this module.

### Day 1: Understanding openEHR Basics

(I'll add my notes here)

### Day 2: Exploring the CKM

(I'll add my notes here)

### Day 3: Creating My First Template

(I'll add my notes here)

## Questions and Challenges

I'll track any questions or challenges I encounter here for future reference.

## Next Steps

After completing this module, I'll move on to [Module 2: Building My First openEHR App](../module-2-first-app/README.md) where I'll create a web application that uses this template.

## Sources

This module outline is based on:

- [Medblocks OpenEHR Bootcamp - Module 1](https://medblocks.com/openehr-bootcamp) - "Introduction to openEHR & Create Your First Template"
- Personal bootcamp reference document (bootcamp_reference.md)
- [OpenEHR Foundation Resources](https://openehr.org/)
- [Clinical Knowledge Manager Documentation](https://ckm.openehr.org/ckm/)
