# OpenEHR Bootcamp Development Assistant

**All code, documentation, and explanations must be in English.**

## Technology Stack

### Primary Technologies
- **OpenEHR**: Clinical data modeling using Reference Model + Archetypes approach
- **EHRbase**: Open-source openEHR repository (Docker-based local setup)
- **Python 3.11+**: Primary backend language with strict typing (`mypy --strict`)
- **SQL**: PostgreSQL for EHRbase and custom queries
- **Svelte + TypeScript**: Frontend framework with strict TypeScript config
- **Tailwind CSS**: Utility-first styling framework

### Development Tools
- **Conda**: Environment management via `environment.yml`
- **pnpm**: Package manager for Node.js dependencies 
- **Archetype Designer**: Visual archetype creation at tools.openehr.org/designer
- **Postman**: API testing with collections organized by bootcamp modules
- **Docker**: EHRbase containerization and deployment
- **Java 11+**: Secondary language for understanding existing implementations

### Secondary/Learning Technologies
- **Java**: For comprehending existing EHRbase modules and OpenEHR reference implementations
- **FHIR**: For interoperability mappings (modules 4-5)
- **OMOP CDM**: For analytics transformations (module 5)

## OpenEHR Implementation Standards

### Data Modeling Conventions
- Templates (.opt files) as primary clinical data structures
- Archetypes follow openEHR CKM validation standards
- Compositions for clinical data persistence with proper metadata
- Use SNOMED CT, LOINC, ICD-10 terminology codes with explicit system references
- ISO 8601 timestamps, UCUM units of measure
- Anonymized but realistic test data patterns

### API Integration Patterns
- EHR creation before storing any compositions
- Template upload and validation before data persistence
- Proper openEHR headers: Content-Type: application/json, Accept: application/json
- AQL queries for structured data extraction and reporting
- Version management for composition updates
- Participation objects for clinical actor identification

## EHRbase REST API Endpoints

### Core Endpoints
- `POST /rest/openehr/v1/ehr` - Create new Electronic Health Record
- `GET /rest/openehr/v1/ehr/{ehr_id}` - Retrieve EHR summary
- `POST /rest/openehr/v1/ehr/{ehr_id}/composition` - Store composition
- `PUT /rest/openehr/v1/ehr/{ehr_id}/composition/{object_id}` - Update composition
- `GET /rest/openehr/v1/ehr/{ehr_id}/composition/{object_id}` - Retrieve composition
- `POST /rest/openehr/v1/query/aql` - Execute AQL query
- `POST /rest/openehr/v1/definition/template/adl1.4` - Upload template
- `GET /rest/openehr/v1/definition/template/adl1.4/{template_id}` - Retrieve template

### Authentication & Headers
- Basic Authentication when `SECURITY_AUTHTYPE=BASIC` configured
- Required headers: `Content-Type: application/json`, `Accept: application/json`
- CORS enabled for frontend development

## Module-Specific Context

### Module 1: Introduction (Weeks 1-2) - ACTIVE
- **Focus**: OpenEHR fundamentals, Reference Model, archetypes, templates
- **Current Status**: Nearing completion with vital signs template created
- **Key Files**: `module-1-introduction/JaimePM_vital_signs.v0.opt`
- **Next Steps**: API integration and composition creation

### Module 2: First App (Weeks 3-4) - UPCOMING
- **Focus**: Basic Svelte application with EHRbase integration
- **Tech Stack**: Svelte + TypeScript, Tailwind CSS, basic API calls
- **Learning Goals**: EHR creation, composition storage, basic queries
- **Template Dependencies**: Reuse Module 1 vital signs template

### Module 3: Complex Assessment (Weeks 5-6) - PLANNED
- **Focus**: Advanced clinical modeling (gynecology use case)
- **Tech Stack**: Complex archetype design, advanced AQL, nested compositions
- **Key Resources**: `Gynaec OP Case Record.pdf` for requirements analysis
- **Skills**: Multi-section templates, complex validation rules

### Module 4: Practitioner App (Weeks 7-8) - PLANNED  
- **Focus**: Production-ready healthcare professional application
- **Tech Stack**: Python/SQL backend, Svelte frontend, full EHRbase integration
- **Advanced Topics**: Authentication, role-based access, audit trails

### Module 5: Dashboard (Weeks 9-10) - PLANNED
- **Focus**: Analytics and visualization dashboard
- **Tech Stack**: Python data processing, AQL aggregation queries, Svelte charts
- **Interoperability**: FHIR mapping, OMOP transformation examples

## Development Standards

### Python Backend Standards  
- Python 3.11+ with strict typing: `mypy --strict`
- Use type hints for all function parameters and return values
- Pydantic for data validation and serialization
- FastAPI for REST API development (when applicable)
- PostgreSQL queries with parameterized statements
- Environment-based configuration via Conda `environment.yml`

### Frontend Development Standards (Svelte)
- Svelte with TypeScript strict mode enabled
- Tailwind CSS for consistent, responsive design
- Component naming: PascalCase for components, kebab-case for files
- Props validation using TypeScript interfaces
- Custom stores for openEHR-specific state management
- Error boundaries for API interaction failures
- Accessibility compliance (ARIA labels, semantic HTML)

### OpenEHR-Specific Coding Standards
- Template IDs in snake_case format: `vital_signs_v1`, `gynaec_assessment_v2`
- Composition UIDs generated via EHRbase, not manually created
- AQL queries with proper escaping and parameterization  
- Archetype node IDs preserved from original CKM archetypes
- Terminology binding validation before composition storage
- Clinical data anonymization patterns for test datasets

### Code Organization Patterns
- Feature-based directory structure within modules
- Separation: UI components, API clients, data models, utilities
- Shared components in `/src/lib/` for reusability across modules
- Environment variables in `.env` files (excluded from git)
- Documentation co-located with code (README.md per module)

## Clinical Data Standards

### Data Format Requirements
- Patient identifiers: UUID format for anonymization
- Timestamps: ISO 8601 format (`2024-01-15T14:30:00Z`)
- Units of measure: UCUM standard (kg, cm, mmHg, °C)
- Language codes: ISO 639-1 (en, es, fr)
- Territory codes: ISO 3166-1 (GB, US, DE)

### Terminology Standards
- SNOMED CT: Use full URI format `http://snomed.info/sct|123456789`
- LOINC: Include display names and system references
- ICD-10: Use official WHO classifications
- Local codes: Prefix with organization identifier

### Test Data Conventions
- Realistic but anonymized clinical scenarios
- Consistent patient demographics across modules
- Varied but clinically plausible vital signs ranges
- Edge cases: pediatric, geriatric, critical values
- Multi-language support for international use cases

## Development Workflow

### Environment Management
- Primary environment: `conda activate openehr-bootcamp`
- Package installation: Use `conda install` when possible, `pip` as fallback
- Node.js dependencies: `pnpm install` (not npm or yarn)
- Docker services: `docker-compose up -d` for EHRbase

### Testing Approach
- Postman collections for API endpoint testing
- Manual validation of archetype constraints
- Cross-browser testing for Svelte components
- Round-trip testing: Create → Store → Query → Retrieve
- Template validation via Archetype Designer before upload

### Documentation Requirements
- README.md per module with setup and learning objectives
- Inline code comments for complex openEHR operations
- API usage examples in Postman collection format
- Architecture decisions recorded in `/docs/` directory
- Progress tracking in module-specific markdown files
- **Mermaid Diagrams**:
    - When creating Mermaid diagrams (e.g., flowcharts, sequence diagrams) for documentation:
        - Ensure all node labels and edge labels containing special characters (e.g., `::`, `/`, `<br>`, `#`, `-`, `.`, `!`, `(`, `)`) or newlines are enclosed in double quotes (`"`) to prevent parsing errors. Example: `A["Node with :: special chars"] -->|"Edge label with / slash"| B["Another Node<br>with newline"];`
        - Avoid starting node text with patterns that Mermaid might misinterpret as lists (e.g., `1. Text`). Instead, use phrasing like `Step 1: Text`.
        - For better readability and theme compatibility, prefer relying on default Mermaid/theme fill colors for nodes. If custom styling is necessary, prioritize changing stroke (border) colors or using `classDef` sparingly, ensuring high contrast with text.

## Key Reference Materials and Documentation

When providing information or assistance, prioritize these official sources aligned with bootcamp curriculum:

### Primary OpenEHR Resources
- **OpenEHR Specifications**: https://specifications.openehr.org/ (authoritative technical standards)
- **Architecture Overview**: https://specifications.openehr.org/releases/BASE/latest/architecture_overview.html
- **REST API Specification**: https://specifications.openehr.org/releases/ITS-REST/latest/
- **AQL Specification**: https://specifications.openehr.org/releases/QUERY/latest/aql.html
- **Archetype Formalism**: https://specifications.openehr.org/releases/AM/latest/
- **UML Class Index**: https://specifications.openehr.org/releases/RM/latest/class_index.html

### Community and Tools
- **OpenEHR Foundation**: https://openehr.org/ (organization and community resources)
- **Clinical Knowledge Manager**: https://ckm.openehr.org/ckm/ (validated archetypes repository)
- **Archetype Designer**: https://tools.openehr.org/designer (visual archetype modeling)
- **OpenEHR Discourse**: https://discourse.openehr.org/ (community support forum)
- **OpenEHR Wiki**: https://wiki.openehr.org/ (collaborative documentation)
- **OpenEHR GitHub**: https://github.com/openEHR (reference implementations)

### Bootcamp-Specific Resources
- **Medblocks OpenEHR Bootcamp**: https://medblocks.com/openehr-bootcamp (main program page)
- **Bootcamp Repository**: https://github.com/medblocks/openehr-bootcamp (official exercises and examples)
- **Medblocks Documentation**: https://docs.medblocks.com/ (implementation guides)
- **Cloud EHRbase Setup**: https://medblocks.com/blog/host-an-authenticated-ehrbase-server-in-the-cloud-in-under-15-mins

### Technology Documentation
- **EHRbase Server**: https://ehrbase.readthedocs.io/ (server administration and API usage)
- **Svelte Framework**: https://svelte.dev/ (component framework documentation)
- **TypeScript Language**: https://www.typescriptlang.org/docs/ (type system and tooling)
- **Tailwind CSS**: https://tailwindcss.com/docs (utility-first CSS framework)
- **Postman Learning**: https://learning.postman.com/docs/getting-started/introduction/ (API testing)

### Development Environment
- **Python Official**: https://docs.python.org/3/ (language reference and stdlib)
- **PostgreSQL Docs**: https://www.postgresql.org/docs/ (database administration)
- **Conda User Guide**: https://docs.conda.io/projects/conda/en/stable/user-guide/ (environment management)
- **Docker Documentation**: https://docs.docker.com/ (containerization platform)

### Interoperability Standards  
- **FHIR R4**: https://hl7.org/fhir/R4/ (health data exchange standard)
- **OMOP CDM**: https://ohdsi.github.io/CommonDataModel/ (analytics data model)
- **SNOMED CT**: https://www.snomed.org/ (clinical terminology)
- **LOINC**: https://loinc.org/ (laboratory data codes)

### Learning Supplementary Resources
- **JavaScript (MDN)**: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide
- **Java Documentation**: https://docs.oracle.com/en/java/ (for understanding legacy implementations)
- **Git Version Control**: https://git-scm.com/doc (code versioning and collaboration)

## Usage Guidelines

### Prioritization Order
1. **Official OpenEHR specifications** for technical implementation details
2. **Bootcamp-specific materials** for exercises and learning progression  
3. **Technology documentation** for framework-specific implementation
4. **Community resources** for troubleshooting and best practices
5. **Supplementary materials** for foundational programming concepts

### Context-Aware Assistance
- Reference appropriate documentation based on current module progression
- Suggest official examples from CKM when modeling clinical data
- Link to relevant specification sections when explaining OpenEHR concepts
- Provide bootcamp repository examples when available
- Escalate to community forums for edge cases or advanced scenarios

This ensures all guidance aligns with the structured learning path and authoritative sources used throughout the bootcamp curriculum.
