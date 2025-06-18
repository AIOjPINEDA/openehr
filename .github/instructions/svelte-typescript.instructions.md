---
applyTo: "**/*.{js,ts,svelte}"
---

# Svelte + JavaScript Standards for OpenEHR Bootcamp

Based on Professor Siddarth's bootcamp methodology and real project setup.

Use Svelte with JavaScript and JSDoc comments (not TypeScript strict mode).
Name components with PascalCase, files with kebab-case.
Use JSDoc for type annotations instead of TypeScript interfaces.
Use basic Svelte component structure without complex typing.

Use pnpm as package manager following bootcamp standards.
Focus on learning OpenEHR concepts first, advanced typing later.
Implement simple reactive variables with `let` declarations.
Use Medblocks UI web components for OpenEHR form generation.

Organize code in SvelteKit route-based structure (`src/routes/`).
Keep components simple and focused on OpenEHR learning objectives.
Store EHR IDs and composition data in component state.
Handle EHRbase API calls with basic fetch() and error handling.

Reference official Svelte documentation: https://svelte.dev/docs/kit/introduction
Use SvelteKit minimal template as starting point.
Implement loading states for async OpenEHR operations.
Store OpenEHR templates as JSON files in routes directory.
