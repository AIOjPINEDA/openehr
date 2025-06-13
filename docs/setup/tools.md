# OpenEHR Bootcamp Tools Reference

This document provides an overview of the key tools used in the OpenEHR Bootcamp, with links to official documentation and resources.

## Core OpenEHR Tools

### EHRbase

EHRbase is an open-source openEHR server implementation that provides a clinical data repository based on the openEHR Reference Model.

- **Purpose**: Storing and querying clinical data
- **Official Website**: [ehrbase.org](https://ehrbase.org/)
- **GitHub Repository**: [ehrbase/ehrbase](https://github.com/ehrbase/ehrbase)
- **Documentation**: [EHRbase Documentation](https://ehrbase.readthedocs.io/en/latest/)
- **Setup**: See [Environment Setup](environment_setup.md#ehrbase-setup)

### Archetype Designer

Archetype Designer is a web-based tool for creating and editing openEHR archetypes and templates.

- **Purpose**: Modeling clinical concepts as archetypes and templates
- **Official Website**: [tools.openehr.org/designer](https://tools.openehr.org/designer)
- **Documentation**: [Archetype Designer Documentation](https://openehr.atlassian.net/wiki/spaces/healthmod/pages/415465475/Archetype+Designer+Documentation)
- **Access**: Web-based tool, no installation required

### Clinical Knowledge Manager (CKM)

CKM is a repository of community-validated archetypes and templates.

- **Purpose**: Accessing, reviewing, and contributing to shared archetypes
- **Official Website**: [ckm.openehr.org/ckm](https://ckm.openehr.org/ckm/)
- **Documentation**: [CKM Documentation](https://openehr.atlassian.net/wiki/spaces/healthmod/pages/2949126/Clinical+Knowledge+Manager)
- **Access**: Web-based tool, registration required

## Development Tools

### VS Code Extensions for OpenEHR Development

#### Essential OpenEHR Extensions
```vscode-extensions
nedaphealthcare.openehr-adl-lsp,dipsas.aql
```

#### Detailed Extension Analysis

**nedaphealthcare.openehr-adl-lsp** - *Comprehensive OpenEHR Development Suite*
- **File Support**: .adl, .adl2, .adlf, .adlt, .adls, .aql, .opt2
- **ADL 2 Features**:
  - Advanced syntax highlighting and validation
  - Model validation with real-time error checking
  - Code folding and document outline navigation
  - Example generation (JSON, Flat JSON, XML formats)
  - OPT2 generation (ADL, JSON, XML outputs)
  - Hover info for complex objects and attributes
  - Automatic terminology constraint addition
- **AQL Features**:
  - Syntax highlighting and validation
  - Path annotation with human-readable names
  - Code completion for archetype paths
  - Integration with known archetypes
- **ADL 1.4 Support**: Basic highlighting, outline, ADL 2 conversion
- **Use Cases**: Complete OpenEHR development lifecycle, template creation, archetype modeling

**dipsas.aql** - *Specialized AQL Query Development*
- **File Support**: .aql files exclusively
- **Core Features**:
  - Optimized syntax highlighting for AQL
  - File extension association and recognition
  - Clean, focused AQL development experience
- **Developer**: DIPS ASA (Norwegian healthcare IT leader)
- **Use Cases**: Intensive AQL query development, data retrieval optimization

#### Bootcamp Module Applications

**Module 2 (Current)**: 
- `nedaphealthcare.openehr-adl-lsp` → Template review, basic AQL queries
- `dipsas.aql` → Composition listing queries, data filtering

**Module 3-5 (Future)**:
- Complex archetype modeling (nedap extension)
- Advanced AQL analytics queries (dips extension)
- Template validation and OPT generation (nedap extension)

**Recommendation**: Install both extensions for complementary OpenEHR development capabilities.

### Postman

Postman is a platform for API development and testing.

- **Purpose**: Testing and interacting with openEHR REST APIs
- **Official Website**: [postman.com](https://www.postman.com/)
- **Documentation**: [Postman Documentation](https://learning.postman.com/docs/getting-started/introduction/)
- **Setup**: See [Environment Setup](environment_setup.md#postman-for-openehr)

### Svelte

Svelte is a modern JavaScript framework for building user interfaces.

- **Purpose**: Developing frontend applications for openEHR
- **Official Website**: [svelte.dev](https://svelte.dev/)
- **Documentation**: [Svelte Documentation](https://svelte.dev/docs)
- **Setup**: See [Environment Setup](environment_setup.md#svelte-development-environment)

### Java Development Kit (JDK)

Java is used for backend development and interacting with openEHR servers.

- **Purpose**: Backend development and server integration
- **Official Website**: [adoptium.net](https://adoptium.net/) (Eclipse Temurin)
- **Documentation**: [Java Documentation](https://docs.oracle.com/en/java/)
- **Setup**: Install JDK 11 or higher

## Interoperability Tools

### FHIR Tools

Tools for working with Fast Healthcare Interoperability Resources (FHIR).

- **Purpose**: Mapping between openEHR and FHIR
- **Official Website**: [hl7.org/fhir](https://www.hl7.org/fhir/)
- **Tools**:
  - [HAPI FHIR](https://hapifhir.io/) - Java implementation of FHIR
  - [openEHR2FHIR transformer](https://discourse.openehr.org/t/online-openehr2fhir-transformer/2606)

### OMOP Tools

Tools for working with the Observational Medical Outcomes Partnership (OMOP) Common Data Model.

- **Purpose**: Mapping openEHR data to OMOP for analytics
- **Official Website**: [ohdsi.org](https://www.ohdsi.org/)
- **Tools**:
  - [WhiteRabbit & Rabbit-in-a-Hat](https://ohdsi.github.io/WhiteRabbit/) - ETL design and mapping
  - [NACHC-CAD/fhir-to-omop](https://github.com/NACHC-CAD/fhir-to-omop) - FHIR to OMOP ETL

## Future Tools (To Be Added)

The following tools will be added to the bootcamp environment as needed:

- **Better Platform**: Commercial openEHR platform
- **Medblocks UI**: UI components for openEHR
- **Terminology servers**: For managing clinical terminologies

## Sources

This tools reference is based on:

- [OpenEHR Specifications](https://specifications.openehr.org/)
- [Medblocks OpenEHR Bootcamp](https://medblocks.com/openehr-bootcamp)
- [EHRbase Documentation](https://ehrbase.readthedocs.io/en/latest/)
- [Postman Documentation](https://learning.postman.com/docs/getting-started/introduction/)
- [Svelte Documentation](https://svelte.dev/docs)
- [FHIR Documentation](https://www.hl7.org/fhir/)
