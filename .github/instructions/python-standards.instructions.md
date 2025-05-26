---
applyTo: "**/*.py"
---

# Python Development Standards for OpenEHR

Use Python 3.11+ with strict typing enabled via `mypy --strict`.
Add type hints for all function parameters and return values.
Use `Optional[Type]` for nullable values and import from typing module.

Use Pydantic for data validation and serialization.
Use FastAPI for REST API development when applicable.
Use parameterized PostgreSQL queries, never string concatenation.
Configure environment via Conda `environment.yml`.

Generate composition UIDs via EHRbase, never manually create them.
Preserve archetype node IDs from original CKM archetypes.
Validate terminology bindings before composition storage.
Use anonymization patterns for test datasets.

Use try/catch blocks for async operations.
Always log errors with contextual information.
Implement proper error boundaries for API interactions.
