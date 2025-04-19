# My OpenEHR Bootcamp Journey

This repository documents my personal learning journey through the [Medblocks OpenEHR Bootcamp](https://medblocks.com/openehr-bootcamp), a 10-week program designed to teach practical openEHR skills through building real-world healthcare applications.

## About OpenEHR

OpenEHR is an open standard specification that describes the management and storage, retrieval and exchange of health data in electronic health records (EHRs). It provides a flexible, adaptable approach to electronic health records with a focus on interoperability and future-proofing health data.

## Learning Path

This repository is structured to follow the bootcamp's five modules, each representing approximately two weeks of learning:

| Module | Title | Key Deliverable |
|--------|-------|----------------|
| 1 | Introduction to openEHR & Create Your First Template | An openEHR template for capturing vital signs |
| 2 | Build Your First openEHR App | A web app for patients to record vital signs |
| 3 | Model a complex assessment form in openEHR | A complex clinical assessment modeled as archetypes and templates |
| 4 | Build a Practitioner-Facing App | An app for practitioners to capture detailed assessments |
| 5 | Build a dashboard that reuses data | A dashboard visualizing data from multiple templates |

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
- **Modern web development stack** - JavaScript/TypeScript, React, and related technologies

## Progress Tracking

I'll update this repository as I progress through each module, documenting my learning process, challenges faced, and solutions implemented.

## License

[MIT License](LICENSE)

## Sources

This repository structure and documentation is based on:

- [Medblocks OpenEHR Bootcamp](https://medblocks.com/openehr-bootcamp) - Primary source for module structure and content
- [OpenEHR Foundation Resources](https://openehr.org/)
- [EHRbase Documentation](https://ehrbase.readthedocs.io/en/latest/)
- [Better Platform Documentation](https://docs.better.care/openehr-platform/)
- [Medblocks Documentation](https://docs.medblocks.com/)
