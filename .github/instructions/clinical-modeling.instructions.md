---
applyTo: "**"
---

# OpenEHR Clinical Data Modeling Standards

Use templates (.opt files) as primary clinical data structures.
Follow openEHR CKM validation standards for archetypes.
Use snake_case format for template IDs: `vital_signs_v1`, `gynaec_assessment_v2`.

Create compositions for clinical data persistence with proper metadata.
Include participation objects for clinical actor identification.
Preserve archetype node IDs from original CKM archetypes.

Use SNOMED CT with full URI format: `http://snomed.info/sct|123456789`.
Include display names and system references for LOINC codes.
Use official WHO classifications for ICD-10 codes.
Prefix local codes with organization identifier.

Create realistic but anonymized clinical scenarios for test data.
Maintain consistent patient demographics across modules.
Use varied but clinically plausible vital signs ranges.
Include edge cases: pediatric, geriatric, and critical values.

Validate templates via Archetype Designer before upload.
Validate terminology bindings before composition storage.
Perform round-trip testing: Create → Store → Query → Retrieve.
