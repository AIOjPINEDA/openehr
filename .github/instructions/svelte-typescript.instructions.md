---
applyTo: "**/*.{js,ts,svelte}"
---

# Svelte + TypeScript Standards for OpenEHR

Use Svelte with TypeScript strict mode enabled.
Name components with PascalCase, files with kebab-case.
Validate props using TypeScript interfaces.
Use `SvelteComponent` types for component props.

Use Tailwind CSS for consistent, responsive design.
Create custom stores for openEHR-specific state management.
Implement accessibility compliance with ARIA labels and semantic HTML.
Add error boundaries for API interaction failures.

Organize shared components in `/src/lib/` for reusability.
Use feature-based directory structure.
Separate UI components, API clients, data models, and utilities.

Handle EHRbase API calls with proper error handling.
Store composition UIDs in component state.
Use reactive statements for data updates.
Implement loading states for async operations.
