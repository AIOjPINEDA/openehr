---
applyTo: "**/*.{test.js,test.ts,spec.js,spec.ts,test.py,spec.py}"
---

# OpenEHR Testing Standards

Use Postman collections for API endpoint testing.
Test round-trip workflows: Create → Store → Query → Retrieve.
Validate archetype constraints manually during development.
Perform cross-browser testing for Svelte components.

Validate templates via Archetype Designer before upload.
Test EHR creation before composition storage.
Verify proper headers in API requests.
Test error handling for API interaction failures.

Create realistic but anonymized clinical test scenarios.
Use consistent patient demographics across test modules.
Include edge cases: pediatric, geriatric, and critical values.
Test multi-language support for international use cases.

Test both positive and negative scenarios for API endpoints.
Verify composition UID generation via EHRbase.
Test AQL query escaping and parameterization.
Validate terminology binding before composition storage.
