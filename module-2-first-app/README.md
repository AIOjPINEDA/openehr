# Module 2: Building My First openEHR App

This module guides me through building my first web application that interacts with an openEHR server, allowing patients to record their vital signs.

## Module Documentation

- **[Module 2 Kickoff Summary](./module-2-00-kickoff-summary.md)** - Comprehensive overview of assignment requirements, conceptual framework, and technical guidance

## Assignment Specification

Create an EHR ID manually. Your app should be able to do the following within this EHR ID:

1. Create new compositions for your template
2. List all compositions that exist for your template
3. Allow the user to delete compositions
4. Optional: Allow users to edit compositions

You can build your application in any framework or technology of your choice as long as it works. Use the common bootcamp openEHR endpoint: https://openehr-bootcamp.medblocks.com/ehrbase

## Learning Objectives

- Understand how to interact with an openEHR server via REST API
- Learn about Web Templates and simplified openEHR data formats
- Create, retrieve, and query openEHR compositions
- Build a simple web interface for capturing and displaying vital signs data

## Key Concepts to Master

### openEHR REST API

- Authentication and authorization
- Creating and retrieving EHRs (Electronic Health Records)
- Working with compositions
- Understanding Web Templates

### Compositions

- Structure of a composition
- Creating valid compositions
- Validating data against templates
- Submitting compositions to an openEHR server

### Archetype Query Language (AQL)

- Basic AQL syntax
- Querying compositions
- Filtering and sorting results
- Handling query results

## Project: Patient Vital Signs App

I'll build a web application that allows patients to:

1. Record their vital signs (using the template created in Module 1)
2. View their previously recorded vital signs
3. See basic trends in their vital signs data

### Technical Stack

- **Frontend**: React with TypeScript and Tailwind CSS
- **Backend**: EHRbase openEHR server
- **API Communication**: Fetch API or Axios

### Implementation Steps

1. Set up a new React project with Vite
2. Create components for data entry forms
3. Implement API service for communicating with EHRbase
4. Create data visualization components
5. Implement error handling and validation
6. Add basic styling with Tailwind CSS

## Resources

### Official Documentation

- [EHRbase REST API Documentation](https://ehrbase.readthedocs.io/en/latest/02_getting_started/04_rest_api.html)
- [openEHR REST API Specification](https://specifications.openehr.org/releases/ITS-REST/latest/index.html)
- [AQL Documentation](https://specifications.openehr.org/releases/QUERY/latest/AQL.html)

### Tutorials and Guides

- [Working with openEHR Compositions](https://www.youtube.com/watch?v=DRbBjqWzcz0) (YouTube)
- [Introduction to AQL](https://www.youtube.com/watch?v=LHNyqUPYVEk) (YouTube)

### Code Examples

- [EHRbase Client Examples](https://github.com/ehrbase/ehrbase/tree/develop/examples)
- [openEHR REST API Examples](https://github.com/openEHR/specifications-ITS-REST/tree/master/examples)

## Project Structure

```
/
├── src/
│   ├── components/
│   │   ├── VitalSignsForm.tsx
│   │   ├── VitalSignsList.tsx
│   │   └── VitalSignsChart.tsx
│   ├── services/
│   │   ├── ehrbaseService.ts
│   │   └── types.ts
│   ├── utils/
│   │   ├── compositionBuilder.ts
│   │   └── aqlQueries.ts
│   ├── App.tsx
│   └── main.tsx
├── public/
│   └── templates/
│       └── vital_signs_template.json
└── package.json
```

## Notes and Progress

I'll document my learning journey and progress here as I work through this module.

### Day 1: Setting Up the Project

(I'll add my notes here)

### Day 2: Implementing the API Service

(I'll add my notes here)

### Day 3: Building the User Interface

(I'll add my notes here)

### Day 4: Testing and Refinement

(I'll add my notes here)

## Questions and Challenges

I'll track any questions or challenges I encounter here for future reference.

## Next Steps

After completing this module, I'll move on to [Module 3: Modeling a Complex Assessment Form](../module-3-complex-assessment/README.md) where I'll learn to model more complex clinical data.

## Sources

This module outline is based on:

- [Medblocks OpenEHR Bootcamp - Module 2](https://medblocks.com/openehr-bootcamp) - "Build Your First openEHR App"
- Personal bootcamp reference document (bootcamp_reference.md)
- [EHRbase Documentation](https://ehrbase.readthedocs.io/en/latest/)
- [OpenEHR REST API Specifications](https://specifications.openehr.org/releases/ITS-REST/latest/)
- [Archetype Query Language Documentation](https://specifications.openehr.org/releases/QUERY/latest/AQL.html)
