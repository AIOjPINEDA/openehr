# OpenEHR Bootcamp Development Assistant

**All code, documentation, and explanations must be in English.**

## Core Technology Stack
Use OpenEHR for clinical data modeling with Reference Model + Archetypes approach.
Use EHRbase as Docker-based openEHR repository.
Use Python 3.11+ as primary backend language with strict typing.
Use Svelte + TypeScript for frontend with strict configuration.
Use Tailwind CSS for styling.

## Development Environment
Use Conda for environment management via `environment.yml`.
Use pnpm as package manager (never npm or yarn).
Start EHRbase services with `docker-compose up -d`.

## OpenEHR Core Standards
Create EHR before storing any compositions.
Upload and validate templates before data persistence.
Use headers: `Content-Type: application/json`, `Accept: application/json`.
Use ISO 8601 timestamps and UCUM units for measurements.
Use snake_case for template IDs: `vital_signs_v1`, `gynaec_assessment_v2`.

## Code Organization
Use feature-based directory structure within modules.
Separate UI components, API clients, data models, and utilities.
Store environment variables in `.env` files (git-excluded).
Use strict typing with type hints for all Python functions.

## Current Bootcamp Context
This is a personal academic journey repository tracking progress through the Medblocks OpenEHR Bootcamp.
Currently working on Module 2: First Svelte application with EHRbase integration.
Module 1 completed with vital signs template `JaimePM_vital_signs.v0.opt` created.
Next modules planned: Complex Assessment (Module 3), Practitioner App (Module 4), Dashboard (Module 5).
Focus on EHR creation, composition storage, and basic AQL queries for current learning stage.

## Learning Progression Context
- Module 1 (Weeks 1-2): OpenEHR fundamentals, Reference Model, archetypes, templates - COMPLETED
- Module 2 (Weeks 3-4): Basic Svelte application with EHRbase integration - CURRENT
- Module 3 (Weeks 5-6): Advanced clinical modeling, gynecology use case - PLANNED
- Module 4 (Weeks 7-8): Production-ready healthcare application - PLANNED
- Module 5 (Weeks 9-10): Analytics dashboard with FHIR integration - PLANNED

## API Reference Authority
Use Postman collection files in `openehr-bootcamp-original/postman/` as primary source for API syntax and examples.
