# My OpenEHR Bootcamp Journey

This repository documents my personal learning journey through the [Medblocks OpenEHR Bootcamp](https://medblocks.com/openehr-bootcamp), a 10-week program designed to teach practical openEHR skills through building real-world healthcare applications.

## About OpenEHR

OpenEHR is an open standard specification that describes the management and storage, retrieval and exchange of health data in electronic health records (EHRs). It provides a flexible, adaptable approach to electronic health records with a focus on interoperability and future-proofing health data.

## Prerequisites

This bootcamp requires a foundational understanding of:

- Making HTTP requests
- Basic programming skills
- JavaScript for front-end development
- Java for back-end processes

Recommended resources for preparation:

- **Postman:** [Documentation](https://learning.postman.com/docs/getting-started/introduction/) | [Beginner's Course](https://www.postman.com/prasandhkishorep/postman-beginner-s-course-freecodecamp/overview)
- **JavaScript:** [MDN Tutorial](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide) | [freeCodeCamp Course](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/)
- **Svelte:** [YouTube Tutorial](https://www.youtube.com/watch?v=zojEMeQGGHs)
- **Java:** [Oracle Documentation](https://docs.oracle.com/en/java/) | [Beginner's Tutorial](https://www.youtube.com/watch?v=eIrMbAQSU34)

## Learning Path

This repository is structured to follow the bootcamp's five modules, each representing approximately two weeks of learning:

| Weeks | Module Title | Key Topics & Activities |
|-------|-------------|-------------------------|
| 1-2 | Introduction to openEHR | openEHR architecture, motivation, two-level modeling (Reference Model & Archetypes), use cases |
| 3-4 | Archetypes & Templates | Clinical Knowledge Manager (CKM), creating/editing archetypes, template design for real scenarios |
| 5-6 | Data Modeling & Persistence | openEHR data structures (Compositions, EHR, Entry, Observations), AQL (Archetype Query Language) |
| 7-8 | Application Development | openEHR REST APIs, integration with servers (e.g., EHRbase), frontend basics, authentication/authorization |
| 9-10 | Interoperability & Projects | FHIR integration, data mapping, real-world use cases, final project presentations |

## Repository Structure

This repository is organized to track my progress through each module:

```
/
├── docs/                         # Documentation
│   ├── setup/                    # Setup documentation
│   ├── reference/                # Reference materials
│   ├── guides/                   # Guides and tutorials
│   └── README.md                 # Documentation index
├── module-1-introduction/        # Module 1 directory
├── module-2-first-app/           # Module 2 directory
├── module-3-complex-assessment/  # Module 3 directory
├── module-4-practitioner-app/    # Module 4 directory
├── module-5-dashboard/           # Module 5 directory
├── resources/                    # Common resources and examples
├── environment.yml               # Conda environment configuration
└── verify_environment.py         # Environment verification script
```

Each module directory will contain:
- Project code and assets
- Personal notes and learnings
- References to key resources used

## Documentation

Comprehensive documentation is available in the [docs](./docs) directory:

- [Setup Documentation](./docs/setup) - Environment setup and configuration
- [Reference Documentation](./docs/reference) - OpenEHR concepts and terminology
- [Guides and Tutorials](./docs/guides) - Practical guides (to be expanded)

## Development Environment

I'll be using the following tools throughout this bootcamp:

- **EHRbase** - An open-source openEHR server for storing and querying clinical data
- **Archetype Designer** - A web tool for creating and editing openEHR archetypes
- **Clinical Knowledge Manager (CKM)** - A repository of community-validated archetypes
- **Postman** - A tool for testing and developing APIs
- **Svelte** - A framework for building user interfaces
- **Java** - For server-side applications and backend processes

## Interoperability

The bootcamp covers integration between different healthcare data standards:

- **openEHR** - For detailed clinical data modeling and long-term EHR storage
- **FHIR** - For real-time data exchange and interoperability between systems
- **OMOP CDM** - For standardized analytics and research across large datasets

## Progress Tracking

I'll update this repository as I progress through each module, documenting my learning process, challenges faced, and solutions implemented.

## License

[MIT License](LICENSE)

## Sources

This repository structure and documentation is based on:

- [Medblocks OpenEHR Bootcamp](https://medblocks.com/openehr-bootcamp) - Primary source for module structure and content
- [OpenEHR Foundation Resources](https://openehr.org/)
- [EHRbase Documentation](https://ehrbase.readthedocs.io/en/latest/)
- [OpenEHR Specifications](https://specifications.openehr.org/)
- [Medblocks Documentation](https://docs.medblocks.com/)
