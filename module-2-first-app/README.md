# Module 2: Building My First openEHR App

This module guides me through building my first web application that interacts with an openEHR server, allowing patients to record their vital signs.

## Module Documentation

- **[Module 2 Kickoff Summary](./module-2-00-kickoff-summary.md)** - Comprehensive overview of assignment requirements, conceptual framework, and technical guidance
- **[Creating Compositions via API](./module-2-01-creating-compositions-api.md)** - Step-by-step guide for creating EHRs and compositions using OpenEHR REST API
- **[Retrieving and Updating Compositions](./module-2-02-retrieving-and-updating-compositions.md)** - Guide for querying and updating existing compositions
- **[Development Techniques Comparison](./module-2-03-development-techniques-comparison.md)** - Detailed comparison of manual flat JSON vs. Medblocks UI approaches for building OpenEHR applications
- **[Tutorial Implementation with Medblocks UI](./module-2-04-tutorial-implementation-medblocks-ui.md)** - Complete step-by-step tutorial following Professor Siddarth's implementation using Svelte and Medblocks UI

## Assignment Specification

Create an EHR ID manually. Your app should be able to do the following within this EHR ID:

1. Create new compositions for your template
2. List all compositions that exist for your template
3. Allow the user to delete compositions
4. Optional: Allow users to edit compositions

You can build your application in any framework or technology of your choice as long as it works. Use the common bootcamp openEHR endpoint: https://openehr-bootcamp.medblocks.com/ehrbase

## Submission Requirements

### Deliverable Format
Submit your project as either:
- **ZIP file**: Exclude `node_modules`, build artifacts, and other dependencies (include only source code and configuration files)
- **Public GitHub repository**: Provide the repository URL with clear setup instructions in README

### Technical Requirements
- **OpenEHR Server**: Must use the common bootcamp endpoint: `https://openehr-bootcamp.medblocks.com/ehrbase`
- **EHR ID**: Create and use a unique EHR ID on the bootcamp server for your application
- **Template**: Use your vital signs template from Module 1
- **Functionality**: Implement all core features (create, list, delete compositions) plus optional edit functionality

### Reference Implementation
A sample application demonstrating these requirements can be found in the bootcamp tutorial materials. Use this as a reference for expected functionality and structure.

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

## Project: Vital Signs Management Application

Based on the bootcamp curriculum, I'll build a web application that allows users to:

1. **Create compositions** for vital signs (using my Module 1 template)
2. **List all compositions** that exist for the template  
3. **Delete compositions** from the EHRbase server
4. **Optional: Edit existing compositions** (advanced feature)

### Core Learning Objectives Covered

✅ **Completed Topics** (14/30 from curriculum):
- OpenEHR REST API fundamentals
- EHR and Composition concepts
- Web Templates and data formats (Canonical vs. Flat JSON)
- Two implementation techniques (Manual vs. Medblocks UI)
- CRUD operations (Create, Read, Update, Delete)
- AQL queries for data retrieval

🔄 **Remaining Advanced Topics**:
- Subject IDs and patient identification
- Directory API and data organization
- Contribution API for change tracking
- Context auto-population
- Manual composition creation (deep dive)

### Technical Stack (As Taught in Bootcamp)

- **Frontend**: Svelte + SvelteKit with JavaScript
- **Styling**: Tailwind CSS
- **OpenEHR UI**: Medblocks UI web components
- **Package Manager**: pnpm
- **Backend**: EHRbase openEHR server
- **API Communication**: Fetch API with OpenEHR REST endpoints

### Implementation Approaches (From Curriculum)

The bootcamp teaches two primary techniques:

1. **Manual Flat JSON Approach**
   - Direct API manipulation with flat JSON format
   - Full control over data transformation
   - Manual mapping between form fields and OpenEHR paths

2. **Medblocks UI Approach** (Recommended)
   - Auto-generated forms from OpenEHR templates
   - Built-in validation and OpenEHR compliance
   - Simplified development workflow

## Resources

### Official Documentation

- [EHRbase REST API Documentation](https://docs.ehrbase.org/api/hip-ehrbase/openehr)
- [openEHR EHR REST API Specification](https://specifications.openehr.org/releases/ITS-REST/Release-1.0.3/ehr.html)
- [AQL Documentation](https://specifications.openehr.org/releases/QUERY/latest/AQL.html)

### Tutorials and Guides

- [Working with openEHR Compositions](https://www.youtube.com/watch?v=DRbBjqWzcz0) (YouTube)
- [Introduction to AQL](https://www.youtube.com/watch?v=LHNyqUPYVEk) (YouTube)

### Code Examples

- [EHRbase Client Examples](https://github.com/ehrbase/ehrbase/tree/develop/examples)
- [openEHR REST API Examples](https://github.com/openEHR/specifications-ITS-REST/tree/master/examples)

## Project Structure (Svelte + Medblocks UI)

Based on the bootcamp tutorial implementation:

### Option A: Medblocks UI Approach (Recommended)
```
/
├── src/
│   ├── routes/
│   │   ├── +layout.svelte        # Global layout
│   │   ├── +page.svelte          # Main application page
│   │   ├── +page.js              # Page load function
│   │   └── vital_signs.json      # OpenEHR web template
│   ├── lib/
│   │   └── index.js              # Utility functions
│   ├── app.html                  # HTML template
│   ├── app.css                   # Global styles
│   └── app.d.ts                  # Type definitions
├── static/
│   └── favicon.png
├── package.json
├── svelte.config.js
├── tailwind.config.js
└── vite.config.js
```

### Option B: Manual Implementation Structure
```
/
├── src/
│   ├── routes/
│   │   ├── +page.svelte          # Main page with manual forms
│   │   └── +page.js              # API service functions
│   ├── lib/
│   │   ├── api.js                # EHRbase API service
│   │   ├── compositions.js       # Composition utilities
│   │   └── templates.js          # Template handling
│   └── app.css
├── static/
│   └── templates/
│       └── vital_signs.json      # OpenEHR template
└── package.json
```

### Key Files and Their Purpose

- **`+page.svelte`**: Main application interface with forms and data display
- **`+page.js`**: Server-side data loading and API integration
- **`vital_signs.json`**: OpenEHR web template (exported from Template Designer)
- **`lib/`**: Utility functions for API calls and data processing
- **`app.css`**: Tailwind CSS imports and custom styles

## Notes and Progress

I'll document my learning journey and progress here as I work through this module.

### ✅ Completed Learning (Phase 1-3)
- **OpenEHR Fundamentals**: Templates, EHRs, Compositions relationship
- **API Mastery**: Create, retrieve, update, delete compositions via REST API
- **Implementation Techniques**: Manual flat JSON vs. Medblocks UI approaches
- **Practical Tutorial**: Full Svelte application with Medblocks UI integration

### 🔄 Current Focus Areas
- Advanced manual composition creation
- Context auto-population techniques
- Directory API and folder organization
- Production deployment considerations

### 📝 Development Notes

#### Day 1: Understanding OpenEHR Concepts
- Learned relationship between templates, EHRs, and compositions
- Practiced API calls with Postman
- Created EHR ID on bootcamp server

#### Day 2: Exploring Implementation Approaches  
- Compared manual flat JSON vs. Medblocks UI techniques
- Reviewed Svelte + SvelteKit project structure
- Analyzed example compositions and web templates

#### Day 3: Hands-on Tutorial Implementation
- Followed Professor Siddarth's step-by-step Medblocks UI tutorial
- Implemented CRUD operations with auto-generated forms
- Practiced AQL queries for composition retrieval

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
