# OpenEHR Bootcamp - Module 2: Technique 2 - Using Medblocks UI for Automated Form Generation

This document covers Technique 2 for building OpenEHR applications: using the Medblocks UI library to automatically generate forms from OpenEHR templates. This approach significantly simplifies frontend development by eliminating manual form creation.

## Overview

**Medblocks UI** is a specialized web components library designed specifically for OpenEHR development. It provides the `<mb-autoform>` component that can automatically render clinical forms from OpenEHR WebTemplates, handle data import/export, and generate valid compositions in flat JSON format.

### Why Medblocks UI?

According to Professor Siddhart: *"I'd like to say there are other options, but then we built this UI library called Medblocks UI because we couldn't find anything else that does something similar."*

**Key Benefits:**
- **Automatic form generation** from OpenEHR templates
- **Built-in data validation** following OpenEHR standards
- **Seamless composition handling** (import/export)
- **Framework agnostic** - works with any frontend framework or vanilla HTML
- **Rapid prototyping** capabilities for clinical applications

## Implementation Guide

### Step 1: Include Medblocks UI in Your Project

Add both CSS and JavaScript to your HTML file:

```html
<!DOCTYPE html>
<html>
<head>
    <!-- Medblocks UI CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@medblocks/ui/dist/medblocks-ui.min.css" />
</head>
<body>
    <!-- Your content here -->
    
    <!-- Medblocks UI JavaScript (ES Module) -->
    <script type="module" src="https://cdn.jsdelivr.net/npm/@medblocks/ui/dist/medblocks-ui.esm.js"></script>
</body>
</html>
```

### Step 2: Create the Auto-Form Component

```html
<div style="max-width: 800px;">
    <h1>Vital Signs Form</h1>
    <mb-autoform id="vitalsForm"></mb-autoform>
</div>
```

**Important Notes:**
- `<mb-autoform>` is a **web component** that behaves like any standard HTML element
- Use CSS to control form width and styling
- The component will be empty until you load a WebTemplate

### Step 3: Load Your WebTemplate

#### Getting the WebTemplate

1. **From Archetype Designer:**
   - Open your template in Archetype Designer
   - Click **Export** → **Export WebTemplate**
   - Save the resulting JSON file

2. **Load into the form:**

```javascript
// Get reference to the form component
const form = document.getElementById('vitalsForm');

// Load your WebTemplate JSON
form.webTemplate = {
    "templateId": "nursing_vital_signs_jaime.v0",
    "semVer": "0.1.0",
    "version": "2.3",
    "defaultLanguage": "en",
    // ... rest of your WebTemplate JSON
};
```

**Alternative Loading Methods:**

```javascript
// From external JSON file
fetch('./path/to/your-webtemplate.json')
    .then(response => response.json())
    .then(webTemplate => {
        form.webTemplate = webTemplate;
    });

// Direct assignment (for frameworks like Svelte)
import webTemplate from './your-webtemplate.json';
form.webTemplate = webTemplate;
```

### Step 4: Working with Form Data

#### Exporting Data (Create/Update Compositions)

```javascript
// Get current form data in flat JSON format
const compositionData = form.export();

console.log(compositionData);
// Output example:
// {
//   "nursing_vital_signs_jaime.v0/context/start_time": "2025-06-17T10:30:00Z",
//   "nursing_vital_signs_jaime.v0/vital_signs/pulse/any_event/rate|magnitude": 89,
//   "nursing_vital_signs_jaime.v0/vital_signs/pulse/any_event/rate|unit": "/min",
//   "nursing_vital_signs_jaime.v0/vital_signs/blood_pressure/any_event/systolic|magnitude": 120,
//   "nursing_vital_signs_jaime.v0/vital_signs/blood_pressure/any_event/systolic|unit": "mm[Hg]",
//   "nursing_vital_signs_jaime.v0/vital_signs/blood_pressure/any_event/diastolic|magnitude": 78,
//   "nursing_vital_signs_jaime.v0/vital_signs/blood_pressure/any_event/diastolic|unit": "mm[Hg]"
// }
```

#### Importing Data (Edit Existing Compositions)

```javascript
// Load existing composition data into the form
const existingData = {
    "nursing_vital_signs_jaime.v0/vital_signs/pulse/any_event/rate|magnitude": 120,
    "nursing_vital_signs_jaime.v0/vital_signs/blood_pressure/any_event/systolic|magnitude": 160,
    "nursing_vital_signs_jaime.v0/vital_signs/blood_pressure/any_event/diastolic|magnitude": 99
    // ... other fields
};

form.import(existingData);
// Form will automatically populate with these values
```

#### Browser Console Debugging

When developing, you can use browser DevTools:

```javascript
// Select the mb-autoform element in DevTools, then in console:
$0.export();    // Get current form data
$0.import(data); // Load data into form
```

## Complete Example Implementation

### HTML Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vital Signs Application</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@medblocks/ui/dist/medblocks-ui.min.css" />
    <style>
        .form-container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        .button-group {
            margin-top: 20px;
            display: flex;
            gap: 10px;
        }
        button {
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .primary { background-color: #007bff; color: white; }
        .secondary { background-color: #6c757d; color: white; }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Vital Signs Entry</h1>
        <mb-autoform id="vitalsForm"></mb-autoform>
        
        <div class="button-group">
            <button class="primary" onclick="submitVitals()">Submit Vitals</button>
            <button class="secondary" onclick="clearForm()">Clear Form</button>
            <button class="secondary" onclick="loadSampleData()">Load Sample</button>
        </div>
        
        <div id="output"></div>
    </div>

    <script type="module" src="https://cdn.jsdelivr.net/npm/@medblocks/ui/dist/medblocks-ui.esm.js"></script>
    <script>
        // Your JavaScript implementation here
    </script>
</body>
</html>
```

### JavaScript Implementation

```javascript
// Configuration
const EHR_ID = "your-ehr-id-here";
const OPENEHR_BASE_URL = "https://openehr-bootcamp.medblocks.com/ehrbase/rest/openehr/v1";

// Initialize form
const form = document.getElementById('vitalsForm');

// Load WebTemplate (replace with your actual template)
const webTemplate = {
    // Your WebTemplate JSON here
};

form.webTemplate = webTemplate;

// Submit vitals to OpenEHR server
async function submitVitals() {
    try {
        const compositionData = form.export();
        
        const response = await fetch(`${OPENEHR_BASE_URL}/ehr/${EHR_ID}/composition`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/openehr.wt.flat.schema+json',
                'Accept': 'application/openehr.wt.flat.schema+json',
                'Prefer': 'return=representation'
            },
            body: JSON.stringify(compositionData)
        });

        if (response.ok) {
            const result = await response.json();
            document.getElementById('output').innerHTML = 
                `<p style="color: green;">✅ Vitals submitted successfully! UID: ${result.uid?.value}</p>`;
            clearForm();
        } else {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
    } catch (error) {
        document.getElementById('output').innerHTML = 
            `<p style="color: red;">❌ Error: ${error.message}</p>`;
    }
}

// Clear the form
function clearForm() {
    form.import({});
}

// Load sample data for testing
function loadSampleData() {
    const sampleData = {
        [`${webTemplate.templateId}/vital_signs/pulse/any_event/rate|magnitude`]: 84,
        [`${webTemplate.templateId}/vital_signs/pulse/any_event/rate|unit`]: "/min",
        [`${webTemplate.templateId}/vital_signs/blood_pressure/any_event/systolic|magnitude`]: 120,
        [`${webTemplate.templateId}/vital_signs/blood_pressure/any_event/systolic|unit`]: "mm[Hg]",
        [`${webTemplate.templateId}/vital_signs/blood_pressure/any_event/diastolic|magnitude`]: 80,
        [`${webTemplate.templateId}/vital_signs/blood_pressure/any_event/diastolic|unit`]: "mm[Hg]"
    };
    
    form.import(sampleData);
}
```

## Integration with Popular Frameworks

### Svelte Integration

```svelte
<script>
    import "medblocks-ui";
    import webTemplate from './path/to/webtemplate.json';
    
    let form;
    
    function handleSubmit() {
        const data = form.export();
        // Handle submission
    }
    
    function loadExisting(compositionData) {
        form.import(compositionData);
    }
</script>

<mb-autoform bind:this={form} {webTemplate}></mb-autoform>
<button on:click={handleSubmit}>Submit</button>
```

### React Integration

```jsx
import { useRef, useEffect } from 'react';

function VitalSignsForm({ webTemplate }) {
    const formRef = useRef();
    
    useEffect(() => {
        if (formRef.current) {
            formRef.current.webTemplate = webTemplate;
        }
    }, [webTemplate]);
    
    const handleSubmit = () => {
        const data = formRef.current.export();
        // Handle submission
    };
    
    return (
        <div>
            <mb-autoform ref={formRef}></mb-autoform>
            <button onClick={handleSubmit}>Submit</button>
        </div>
    );
}
```

## Advanced Features

### Custom Validation

```javascript
// Add custom validation before submission
function validateVitals(data) {
    const pulseRate = data[`${templateId}/vital_signs/pulse/any_event/rate|magnitude`];
    const systolic = data[`${templateId}/vital_signs/blood_pressure/any_event/systolic|magnitude`];
    const diastolic = data[`${templateId}/vital_signs/blood_pressure/any_event/diastolic|magnitude`];
    
    const errors = [];
    
    if (pulseRate < 30 || pulseRate > 200) {
        errors.push("Pulse rate should be between 30-200 bpm");
    }
    
    if (systolic < 70 || systolic > 250) {
        errors.push("Systolic BP should be between 70-250 mmHg");
    }
    
    if (diastolic < 40 || diastolic > 150) {
        errors.push("Diastolic BP should be between 40-150 mmHg");
    }
    
    if (systolic <= diastolic) {
        errors.push("Systolic BP should be higher than diastolic BP");
    }
    
    return errors;
}
```

### Form State Management

```javascript
// Track form changes
let isFormDirty = false;

form.addEventListener('input', () => {
    isFormDirty = true;
});

// Warn before leaving page if form has unsaved changes
window.addEventListener('beforeunload', (e) => {
    if (isFormDirty) {
        e.preventDefault();
        e.returnValue = 'You have unsaved changes. Are you sure you want to leave?';
    }
});
```

## Comparison: Technique 1 vs Technique 2

| Aspect | Technique 1 (Manual) | Technique 2 (Medblocks UI) |
|--------|----------------------|----------------------------|
| **Form Creation** | Manual HTML/framework forms | Automatic with `<mb-autoform>` |
| **Development Time** | Longer - need to build each field | Faster - instant form generation |
| **Customization** | Full control over UI/UX | Limited to component styling |
| **Data Handling** | Manual JSON construction | Automatic import/export |
| **Validation** | Custom implementation needed | Built-in OpenEHR validation |
| **Template Changes** | Requires code updates | Automatically adapts |
| **Best For** | Production apps, custom UI | Prototypes, MVPs, rapid development |
| **Learning Curve** | Steeper - need OpenEHR knowledge | Gentler - abstracts complexity |

## Best Practices

### 1. Development Workflow

```javascript
// Recommended development approach
const form = document.getElementById('vitalsForm');

// 1. Load template
form.webTemplate = webTemplate;

// 2. Test with sample data
form.import(sampleVitals);

// 3. Verify export format
console.log('Export format:', form.export());

// 4. Test submission
submitToOpenEHR(form.export());
```

### 2. Error Handling

```javascript
async function submitVitals() {
    try {
        // Validate form has data
        const data = form.export();
        if (Object.keys(data).length === 0) {
            throw new Error('Please fill in the form before submitting');
        }
        
        // Custom validation
        const errors = validateVitals(data);
        if (errors.length > 0) {
            throw new Error(errors.join(', '));
        }
        
        // Submit to server
        await submitToOpenEHR(data);
        
    } catch (error) {
        console.error('Submission error:', error);
        showUserError(error.message);
    }
}
```

### 3. Performance Optimization

```javascript
// Debounce form changes to avoid excessive processing
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

const debouncedValidation = debounce(() => {
    const data = form.export();
    validateVitals(data);
}, 500);

form.addEventListener('input', debouncedValidation);
```

## Troubleshooting

### Common Issues

**1. Form doesn't render:**
- Verify WebTemplate is properly loaded
- Check browser console for JavaScript errors
- Ensure Medblocks UI script is loaded

**2. Export returns empty object:**
- Form may not have any user input
- WebTemplate might not be properly assigned
- Check form validation errors

**3. Import doesn't populate fields:**
- Verify data format matches WebTemplate structure
- Check field paths in the flat JSON
- Ensure data types are correct

### Debug Commands

```javascript
// Useful debugging commands in browser console
$0.webTemplate;  // View loaded template
$0.export();     // Get current form data
$0.import({});   // Clear form
$0.validate();   // Check form validation
```

## Next Steps

After mastering Technique 2 with Medblocks UI:

1. **Integrate with real OpenEHR server** for complete CRUD operations
2. **Combine with AQL queries** to retrieve and edit existing compositions
3. **Add custom styling** to match your application design
4. **Implement user authentication** for multi-user scenarios
5. **Consider hybrid approach** - use Medblocks UI for rapid prototyping, then customize critical forms manually

This technique provides an excellent foundation for quickly building functional OpenEHR applications while learning the underlying concepts.

---

*For complete documentation and advanced features, visit: [Medblocks UI Documentation](https://medblocks.com/docs/medblocks-ui)*
