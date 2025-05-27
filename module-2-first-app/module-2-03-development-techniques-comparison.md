# OpenEHR Bootcamp - Module 2: Development Techniques Comparison

This document summarizes the two primary development techniques presented by Professor Siddarth Ramesh for building OpenEHR applications in Module 2. These approaches provide different levels of control and complexity for implementing the vital signs management application.

## Overview

During the live session, Professor Siddarth demonstrated two distinct approaches for developing OpenEHR applications:

1. **Manual Technique**: Using flat JSON format with direct API manipulation
2. **Medblocks UI Technique**: Using the Medblocks UI library for automated form generation

Both techniques are valid approaches for completing the Module 2 assignment requirements, each with their own advantages and trade-offs.

## Technique 1: Manual Flat JSON Approach

### Concept
This technique involves manually handling OpenEHR compositions using the flat JSON format, which provides a simplified key-value structure compared to the canonical JSON format.

### Implementation Process

#### Step 1: Obtain Example Composition
- Retrieve example composition from your template in flat format
- Use the OpenEHR REST API to get template examples
- Flat format is preferred due to its simplicity and readability

#### Step 2: Data Transformation
- Replace placeholder values with real form data
- Map user input fields to corresponding flat JSON paths
- Example: Replace `"500"` with actual pulse rate from form input

#### Step 3: Composition Submission
- Submit transformed flat JSON to OpenEHR server
- Use `POST /rest/openehr/v1/ehr/{ehr_id}/composition` endpoint
- Include proper headers: `Content-Type: application/json`, `Accept: application/json`

#### Step 4: Optional Update Functionality
- Retrieve existing composition from server
- Convert composition data back to form fields (reverse mapping)
- Allow user to edit and resubmit updated composition

### Advantages
- **Full Control**: Complete control over data structure and validation
- **Deep Learning**: Provides thorough understanding of OpenEHR flat format
- **Flexibility**: Can customize every aspect of the data handling process
- **No Dependencies**: No external UI libraries required

### Disadvantages
- **Complexity**: Requires manual mapping between form fields and OpenEHR paths
- **Error-Prone**: Manual transformations can introduce structural errors
- **Development Time**: More time-consuming to implement correctly
- **Maintenance**: Bidirectional mapping (create/update) is challenging

### Example Flat JSON Structure
```json
{
  "nursing_vital_sign_jaimepm/language|code": "en",
  "nursing_vital_sign_jaimepm/language|terminology": "ISO_639-1",
  "nursing_vital_sign_jaimepm/territory|code": "US",
  "nursing_vital_sign_jaimepm/category|code": "433",
  "nursing_vital_sign_jaimepm/category|value": "event",
  "nursing_vital_sign_jaimepm/category|terminology": "openehr",
  "nursing_vital_sign_jaimepm/composer|name": "JaimePM",
  "nursing_vital_sign_jaimepm/vital_signs/pulse_heart_rate/any_event:0/pulse_rate|magnitude": 89,
  "nursing_vital_sign_jaimepm/vital_signs/pulse_heart_rate/any_event:0/pulse_rate|unit": "/min",
  "nursing_vital_sign_jaimepm/vital_signs/blood_pressure/any_event:0/systolic|magnitude": 120,
  "nursing_vital_sign_jaimepm/vital_signs/blood_pressure/any_event:0/systolic|unit": "mm[Hg]",
  "nursing_vital_sign_jaimepm/vital_signs/blood_pressure/any_event:0/diastolic|magnitude": 78,
  "nursing_vital_sign_jaimepm/vital_signs/blood_pressure/any_event:0/diastolic|unit": "mm[Hg]"
}
```

## Technique 2: Medblocks UI Library Approach

### Concept
Medblocks UI is a comprehensive suite of Web Components designed specifically for OpenEHR application development. It provides automatic form generation and validation based on OpenEHR web templates.

### Implementation Process

#### Step 1: Include Medblocks UI Dependencies
```html
<!-- Main Package -->
<script src="https://unpkg.com/medblocks-ui@0.0.211/dist/bundle.js"></script>
<!-- Styling -->
<link href="https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@2.0.0-beta.71/dist/themes/light.min.css" rel="stylesheet"/>
```

#### Step 2: Create Auto-Generated Form
```html
<mb-auto-form id="form"></mb-auto-form>

<script>
  let form = document.getElementById("form")
  form.webTemplate = {
    // Insert your OpenEHR web template here
  }
</script>
```

#### Step 3: Data Export (Create Composition)
```javascript
// Automatically generates valid flat JSON
const compositionData = form.export()
// Submit to OpenEHR server
```

#### Step 4: Data Import (Load Existing Composition)
```javascript
// Load composition data into form
form.import({
  // Insert composition in flat format
})
```

### Key Features Demonstrated
- **Automatic Form Generation**: Creates form fields based on web template structure
- **Built-in Validation**: Ensures data conforms to OpenEHR standards
- **Bidirectional Data Flow**: Seamless export/import functionality
- **Live Updates**: Form reflects imported data immediately

### Advantages
- **Rapid Development**: Minimal code required for full functionality
- **Automatic Validation**: Built-in OpenEHR compliance checking
- **Error Reduction**: Less prone to structural errors
- **Maintenance**: Easy to update and modify
- **Bidirectional**: Export/import functionality works out of the box

### Disadvantages
- **External Dependency**: Requires Medblocks UI library
- **Less Control**: Limited customization of form appearance and behavior
- **Learning Curve**: Need to understand Medblocks UI component system
- **Framework Compatibility**: May have integration challenges with some frameworks

### Browser Console Testing
Professor Siddarth demonstrated interactive testing using browser developer tools:

```javascript
// Select the form element
const form = document.querySelector('#form')
// Or use Chrome's $0 shortcut after selecting element

// Export current form data
form.export()
// Returns: valid flat JSON composition

// Import test data
form.import({
  "template_id/pulse_rate|magnitude": 89,
  "template_id/systolic|magnitude": 120,
  "template_id/diastolic|magnitude": 78
})
```

## Integration with Module 2 Requirements

Both techniques can fulfill all Module 2 assignment requirements:

### Required Functionality Mapping

#### 1. Create New Compositions
- **Manual**: Form data → flat JSON transformation → POST API
- **Medblocks UI**: Form input → `form.export()` → POST API

#### 2. List Existing Compositions
- **Manual**: AQL query → data parsing → custom display
- **Medblocks UI**: AQL query → `form.import()` for individual display

#### 3. Delete Compositions
- **Manual**: DELETE API call with composition ID
- **Medblocks UI**: DELETE API call with composition ID

#### 4. Update Compositions (Optional)
- **Manual**: GET composition → reverse mapping → form → forward mapping → PUT
- **Medblocks UI**: GET composition → `form.import()` → edit → `form.export()` → PUT

## Recommendation for Module 2

### Recommended Approach: Medblocks UI

Based on the learning objectives and time constraints of Module 2, **Medblocks UI is recommended** for the following reasons:

1. **Focus on Concepts**: Allows concentration on OpenEHR concepts rather than data transformation logic
2. **Reduced Complexity**: Minimizes potential for structural errors
3. **Complete Implementation**: Easier to implement all requirements including optional update functionality
4. **Industry Relevance**: Demonstrates use of specialized OpenEHR tooling

### When to Consider Manual Approach

The manual technique is valuable when:
- Deep understanding of OpenEHR data structures is required
- Custom validation logic is needed
- Integration with existing data processing pipelines
- Learning objectives include data transformation mastery

## Integration with Svelte + TypeScript

For the bootcamp's technology stack, Medblocks UI integrates well with Svelte:

```typescript
// Svelte component integration
import { onMount } from 'svelte'

let formElement: HTMLElement
let webTemplate: any // Import your web template JSON

onMount(() => {
  // Configure Medblocks UI after component mounts
  formElement.webTemplate = webTemplate
})

// Create composition function
async function createComposition() {
  try {
    const compositionData = formElement.export()
    await submitToOpenEHR(compositionData)
  } catch (error) {
    console.error('Composition creation failed:', error)
  }
}
```

## Next Steps

1. **Choose Implementation Technique**: Select based on learning goals and available time
2. **Setup Development Environment**: Ensure EHRbase is running and template is uploaded
3. **Create EHR ID**: Use Postman to create patient EHR before development
4. **Implement Core Functionality**: Start with create/list operations
5. **Add Optional Features**: Implement update/delete as time permits

## References

- [Medblocks UI Documentation](https://medblocks.com/docs/medblocks-ui)
- [OpenEHR REST API Specification](https://specifications.openehr.org/releases/ITS-REST/latest/)
- [Flat JSON Format Documentation](https://ehrbase.readthedocs.io/en/latest/03_development/02_flat_json/index.html)
- [Module 2 Assignment Requirements](./module-2-00-kickoff-summary.md)
