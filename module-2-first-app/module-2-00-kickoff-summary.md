# OpenEHR Bootcamp - Module 2 Kickoff Summary

This document summarizes the key concepts, requirements, and technical guidance from the Module 2 kickoff sessions. The primary focus is building a first application that interacts with an OpenEHR server, creating compositions from templates, and understanding the relationship between templates, EHRs, and compositions.

## 1. Module 2 Assignment Overview

### Assignment Goals
Build a web application that interacts with an OpenEHR server to manage vital signs data using the template created in Module 1.

### Core Requirements
Your application must implement the following functionality:

1. **Create New Vital Signs Compositions**
   - Use your Vital Signs template from Module 1
   - Create new composition instances with patient data

2. **List Existing Compositions**
   - Display all compositions for your template within a specific EHR ID
   - Show composition data in a readable format

3. **Delete Compositions**
   - Allow users to remove existing compositions
   - Handle deletion operations safely

4. **Optional: Edit Compositions**
   - Not mandatory but recommended for learning
   - Modify existing composition data

### Technical Flexibility
- **Language/Framework**: Any programming language or framework
- **Architecture**: Frontend-only, full-stack, or desktop GUI applications
- **Platform**: Web applications preferred, but desktop GUIs acceptable

### Prerequisites
- EHR ID must be created manually using Postman before application use
- Vital Signs template from Module 1 must be available on the server

## 2. Conceptual Framework: Template, EHR, and Composition
Understanding these three core concepts is essential for building OpenEHR applications.

### Template: The Unfilled Form
- **Real-world analogy**: Stack of blank forms at a hospital reception desk
- **Technical definition**: Schema defining what data needs to be captured
- **Key characteristics**:
  - Defines structure and constraints
  - Reusable across multiple patients
  - Based on OpenEHR archetypes

### EHR (Electronic Health Record): The Patient File
- **Real-world analogy**: Individual patient's medical file folder
- **Technical definition**: Container for all clinical data of one patient
- **Key characteristics**:
  - One EHR per patient
  - Contains multiple compositions
  - Persistent patient identifier
![alt text](https://specifications.openehr.org/releases/RM/latest/ehr/diagrams/high_level_ehr_structure.svg)

### Composition: The Filled Form
- **Real-world analogy**: Completed form with doctor's handwriting
- **Technical definition**: Instance of a template with actual patient data
- **Key characteristics**:
  - Always belongs to an EHR
  - Always based on a template
  - Contains real clinical observations

![alt text](https://specifications.openehr.org/releases/BASE/latest/architecture_overview/diagrams/composition_structure.png)

### Relationship Hierarchy
```
EHR (Patient File)
├── Composition 1 (Vital Signs - Visit 1)
├── Composition 2 (Vital Signs - Visit 2)
└── Composition N (Other Templates)
```

## 3. Composition Data Formats

OpenEHR systems support multiple data formats for compositions. Understanding these formats is crucial for application development.

### Available Formats

#### 1. Canonical JSON
- **Description**: Traditional OpenEHR format
- **Characteristics**:
  - Verbose and detailed
  - Supported by all OpenEHR systems
  - Complex nested structure
  - Contains all OpenEHR metadata

#### 2. Canonical XML
- **Description**: XML version of canonical format
- **Characteristics**:
  - One-to-one mapping with canonical JSON
  - Same verbosity as JSON version
  - Preferred by some legacy systems

#### 3. Flat JSON (Simplified)
- **Description**: Flattened, simplified format
- **Characteristics**:
  - Key-value pair structure
  - More readable and intuitive
  - Easier to work with programmatically
  - Removes non-essential metadata

#### 4. Structured JSON (Simplified)
- **Description**: Nested simplified format
- **Characteristics**:
  - Slightly nested structure
  - Balance between flat and canonical
  - Maintains logical grouping
  - Good for complex templates

### Format Recommendation
- **Beginner-friendly**: Start with Flat JSON for its simplicity
- **Production use**: Choose based on your application's requirements
- **Learning**: Experiment with different formats to understand trade-offs

## 4. Using the Example Composition Endpoint

### Purpose
The example endpoint generates sample compositions from your template, providing a starting point for development.

### Workflow
1. **Set Template ID**: Configure your environment with the template ID from Module 1
2. **Call Example Endpoint**: Request example composition in your preferred format
3. **Analyze Structure**: Understand the expected data format
4. **Modify for Real Data**: Replace example values with actual patient data

### Example Structure Analysis
When examining the example composition, look for:
- **Data fields**: Blood pressure (systolic/diastolic), pulse rate, SPO2
- **Required vs optional fields**: Identify mandatory data points
- **Data types**: Understand numeric values, units, timestamps
- **Metadata**: Composition context, language, territory

## 4. Creating Compositions via API

For detailed step-by-step instructions on creating your first composition, see the dedicated guide:
**[Creating Compositions via OpenEHR API](./module-2-01-creating-compositions-api.md)**

This guide covers:
- Creating EHR records (patient containers)
- Preparing and customizing composition data
- Submitting compositions via REST API
- Verifying successful creation
- Common issues and troubleshooting
- Next steps for building your application

## 5. Development Strategy

### Recommended Approach
1. **Start Simple**: Begin with the example endpoint to understand data structure
2. **Choose Format**: Pick one composition format for consistency
3. **Implement CRUD**: Build Create, Read, Update, Delete operations incrementally
4. **Test Thoroughly**: Use Postman to verify API interactions
5. **Iterate**: Refine UI and functionality based on testing

### Technical Considerations
- **Error Handling**: Implement proper error responses for API failures
- **Data Validation**: Ensure compositions match template constraints
- **User Experience**: Design intuitive interfaces for clinical users
- **Performance**: Consider caching strategies for composition lists

## 6. Success Criteria

Your application will be evaluated on:
- **Functionality**: All required features working correctly
- **OpenEHR Compliance**: Proper use of OpenEHR APIs and data formats
- **Code Quality**: Clean, readable, and maintainable code
- **User Interface**: Intuitive and practical design
- **Documentation**: Clear setup and usage instructions

## 7. Next Steps

1. **Review Module 1 Template**: Ensure your Vital Signs template is properly deployed
2. **Create Your First Composition**: Follow the **[Creating Compositions via API guide](./module-2-01-creating-compositions-api.md)** to create an EHR and post your first composition
3. **Set Up Development Environment**: Configure your chosen technology stack
4. **Explore API Endpoints**: Use Postman to understand OpenEHR REST APIs beyond composition creation
5. **Plan Application Architecture**: Design your application structure
6. **Start Implementation**: Begin building your application with the composition creation workflow

*For deeper architectural understanding, refer to the official OpenEHR specifications linked in the Additional Learning Resources section.*

## 8. Additional Learning Resources

### Official OpenEHR Specifications
- **[Archetypes and Templates](https://specifications.openehr.org/releases/BASE/latest/architecture_overview.html#_archetypes_and_templates)** - Foundation for understanding clinical modeling and the two-level architecture
- **[The EHR](https://specifications.openehr.org/releases/BASE/latest/architecture_overview.html#_the_ehr)** - Comprehensive EHR system architecture and clinical data organization
- **[REST API Specification](https://specifications.openehr.org/releases/ITS-REST/latest/)** - Complete API reference for implementation

---

*This module builds directly on the foundation established in Module 1, transitioning from clinical modeling to practical application development. The focus shifts from understanding OpenEHR concepts to implementing real-world interactions with OpenEHR systems.*
