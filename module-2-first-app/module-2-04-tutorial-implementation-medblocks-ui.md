# OpenEHR Bootcamp - Module 2: Step-by-Step Implementation Tutorial

This document provides a comprehensive walkthrough of building the Module 2 vital signs application, following Professor Siddarth Ramesh's step-by-step tutorial implementation using Medblocks UI and Svelte.

## Tutorial Overview

The implementation is divided into five main tutorials:
1. **Setup and Creating an EHR** - Environment setup and EHR creation
2. **Creating Compositions using Medblocks UI** - Form implementation and composition submission
3. **Listing Compositions** - AQL queries and data display
4. **Deleting Compositions** - Composition removal functionality
5. **Clean up and Updating Compositions** - Form clearing and update operations

## Prerequisites

### Required Tools
- **Node.js and npm/pnpm** - JavaScript runtime and package managers
- **Postman** - API testing and EHR creation
- **Code Editor** - Cursor IDE (AI-enhanced) or VS Code
- **EHRbase Server** - OpenEHR repository (bootcamp shared instance)

### Technology Stack
- **Frontend Framework**: Svelte + SvelteKit
- **Styling**: Tailwind CSS
- **Package Manager**: pnpm
- **OpenEHR UI Library**: Medblocks UI
- **Language**: JavaScript (with optional TypeScript)

## Part 1: Setup and Creating an EHR

### Step 1: Create EHR ID via Postman

**Endpoint**: `POST /rest/openehr/v1/ehr`
**Server**: `https://openehr-bootcamp.medblocks.com/ehrbase`

1. Open Postman and navigate to the EHR creation endpoint
2. Send POST request to create new EHR
3. **Save the returned EHR ID** - this will be used throughout the application

**Expected Response**:
```json
{
  "ehr_id": {
    "value": "550e8400-e29b-41d4-a716-446655440000"
  }
}
```

### Step 2: Initialize Svelte Project

```bash
# Create new SvelteKit project
npx sv create 2-first-app

# Configuration choices:
# - SvelteKit minimal
# - JavaScript (or TypeScript if preferred)
# - Tailwind CSS: Yes
# - Package manager: pnpm
```

### Step 3: Project Setup

```bash
# Navigate to project directory
cd 2-first-app

# Open in Cursor IDE (or preferred editor)
cursor .

# Start development server
npm run dev
```

**Verify setup**: Application should run on `http://localhost:5173`

### Step 4: Configure EHR ID in Application

Edit `src/routes/+page.svelte`:

```javascript
<script>
  // Store the EHR ID from Postman response
  let ehrId = "550e8400-e29b-41d4-a716-446655440000"; // Replace with your actual EHR ID
</script>

<h1>Vital Signs Application</h1>
<p>EHR ID: {ehrId}</p>
```

## Part 2: Creating Compositions using Medblocks UI

### Step 1: Export Web Template

1. Open Archetype Designer
2. Navigate to your vital signs template from Module 1
3. Click **Export** → **Export Web Template**
4. Save the JSON file to your project: `src/routes/nursing_vitals_siddarth_v0.json`

### Step 2: Install Medblocks UI

```bash
# Add Medblocks UI to project
pnpm add medblocks-ui
```

### Step 3: Configure Server-Side Rendering

Create `src/routes/+page.js`:

```javascript
// Disable server-side rendering for Medblocks UI compatibility
export const ssr = false;
```

**Important**: Medblocks UI is a frontend-only library and requires SSR to be disabled.

### Step 4: Implement Form Layout

Update `src/routes/+page.svelte`:

```svelte
<script>
  import webTemplate from './nursing_vitals_siddarth_v0.json';
  
  let ehrId = "your-ehr-id-here";
  let form; // Binding for MB auto form
  
  // OpenEHR REST endpoint configuration
  const openEhrRestEndpoint = "https://openehr-bootcamp.medblocks.com/ehrbase/rest/openehr/v1";
</script>

<div class="flex h-screen">
  <!-- Left side: Form (75% width) -->
  <div class="w-3/4 p-6">
    <h2 class="text-2xl font-bold mb-4 text-gray-800">Nursing Form</h2>
    
    <mb-auto-form 
      bind:this={form}
      web-template={webTemplate}
    ></mb-auto-form>
    
    <button 
      on:click={submitVitals}
      class="mt-4 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
    >
      Submit Vitals
    </button>
  </div>
  
  <!-- Right side: Previous entries (25% width) -->
  <div class="w-1/4 bg-gray-100 p-6">
    <h3 class="text-lg font-semibold mb-4">Previous Entries</h3>
    <!-- Entries will be populated here -->
  </div>
</div>
```

### Step 5: Implement Composition Submission

Add submission logic to the script section:

```javascript
async function submitVitals() {
  try {
    // Export composition data from form
    const composition = form.export();
    console.log('Composition to submit:', composition);
    
    // Prepare API request
    const url = `${openEhrRestEndpoint}/ehr/${ehrId}/composition?templateId=${webTemplate.templateId}`;
    
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Prefer': 'return=representation'
      },
      body: JSON.stringify(composition)
    });
    
    const data = await response.json();
    console.log('Submission response:', data);
    
    if (response.ok) {
      // Show success notification
      alert('Vitals submitted successfully!');
      // Optionally refresh the entries list
    } else {
      console.error('Submission failed:', data);
    }
  } catch (error) {
    console.error('Error submitting vitals:', error);
  }
}
```

### Step 6: Add Toast Notifications (Optional Enhancement)

```bash
# Install toast notification library
pnpm install svelte-sonner
```

Update the script to include toast notifications:

```javascript
import { toast } from 'svelte-sonner';

// In submitVitals function, replace alert with:
toast.success('Vitals submitted successfully!');
```

Add toast container to the template:

```svelte
<script>
  import { Toaster } from 'svelte-sonner';
</script>

<!-- Add at the end of the template -->
<Toaster />
```

## Part 3: Listing Compositions

### Step 1: Implement AQL Query for Listing

Add the listing function to your script:

```javascript
async function getVitals() {
  try {
    // AQL query to fetch compositions for this EHR and template
    const aqlQuery = `
      SELECT 
        c/uid/value,
        c/context/start_time/value
      FROM EHR e 
      CONTAINS COMPOSITION c
      WHERE c/archetype_details/template_id/value = '${webTemplate.templateId}'
      AND e/ehr_id/value = '${ehrId}'
    `;
    
    const response = await fetch(`${openEhrRestEndpoint}/query/aql`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify({
        q: aqlQuery
      })
    });
    
    const data = await response.json();
    console.log('Query response:', data);
    
    // Process the results
    if (data.rows && data.rows.length > 0) {
      const vitals = data.rows.map(row => ({
        uid: row[0],
        timestamp: row[1]
      }));
      
      return vitals;
    }
    
    return [];
  } catch (error) {
    console.error('Error fetching vitals:', error);
    return [];
  }
}
```

### Step 2: Display Previous Entries

Update the right panel to show entries:

```svelte
<script>
  import { onMount } from 'svelte';
  
  let previousEntries = [];
  let loading = false;
  
  onMount(async () => {
    await loadVitals();
  });
  
  async function loadVitals() {
    loading = true;
    previousEntries = await getVitals();
    loading = false;
  }
  
  // Format timestamp for display
  function formatTimestamp(timestamp) {
    return new Date(timestamp).toLocaleString();
  }
</script>

<!-- Update the right panel -->
<div class="w-1/4 bg-gray-100 p-6">
  <h3 class="text-lg font-semibold mb-4">Previous Entries</h3>
  
  {#if loading}
    <p>Loading...</p>
  {:else if previousEntries.length > 0}
    {#each previousEntries as entry}
      <div class="mb-3 p-3 bg-white rounded shadow">
        <p class="text-sm text-gray-600">ID: {entry.uid}</p>
        <p class="text-sm">{formatTimestamp(entry.timestamp)}</p>
      </div>
    {/each}
  {:else}
    <p class="text-gray-500">No entries found</p>
  {/if}
</div>
```

### Step 3: Auto-refresh After Submission

Update the `submitVitals` function to refresh the list:

```javascript
async function submitVitals() {
  try {
    // ... existing submission code ...
    
    if (response.ok) {
      toast.success('Vitals submitted successfully!');
      // Refresh the entries list
      await loadVitals();
    }
  } catch (error) {
    console.error('Error submitting vitals:', error);
  }
}
```

## Key Implementation Notes

### OpenEHR API Integration
- **Base URL**: `https://openehr-bootcamp.medblocks.com/ehrbase/rest/openehr/v1`
- **Required Headers**: `Content-Type: application/json`, `Accept: application/json`
- **Template ID Parameter**: Must be included in composition creation URL

### Medblocks UI Usage
- **Auto Form Generation**: `<mb-auto-form>` automatically creates form fields from web template
- **Data Export**: `form.export()` returns valid flat JSON composition
- **Data Import**: `form.import(data)` populates form with existing composition data

### AQL Query Structure
```sql
SELECT 
  c/uid/value,
  c/context/start_time/value
FROM EHR e 
CONTAINS COMPOSITION c
WHERE c/archetype_details/template_id/value = 'template_id'
AND e/ehr_id/value = 'ehr_id'
```

### SvelteKit Specific Considerations
- **SSR Disabled**: Required for Medblocks UI frontend library
- **Reactive Variables**: Use Svelte's reactive statements for dynamic updates
- **Component Lifecycle**: Use `onMount` for initial data loading

## Testing the Implementation

### Manual Testing Steps
1. **Form Submission**: Fill out vital signs form and submit
2. **Console Verification**: Check browser console for successful API responses
3. **Postman Verification**: Verify composition creation using GET endpoint
4. **List Verification**: Confirm new entries appear in the right panel

### Expected Results
- Form submits successfully with toast notification
- New composition appears in previous entries list
- Console logs show proper API responses
- Composition can be retrieved via Postman

## Next Steps

The following tutorials will cover:
- **Tutorial 4**: Implementing delete functionality for compositions
- **Tutorial 5**: Form clearing and composition update operations

## Common Issues and Solutions

### SSR Related Errors
**Issue**: `Cannot use import statement outside a module`
**Solution**: Create `+page.js` with `export const ssr = false`

### Form Binding Issues
**Issue**: `form.export()` returns undefined
**Solution**: Ensure proper binding with `bind:this={form}` in template

### API Request Failures
**Issue**: 401/403 authentication errors
**Solution**: Verify EHR ID exists and endpoint URL is correct

## References

- [Medblocks UI Documentation](https://medblocks.com/docs/medblocks-ui)
- [SvelteKit Documentation](https://kit.svelte.dev/docs)
- [OpenEHR REST API](https://specifications.openehr.org/releases/ITS-REST/latest/)
- [AQL Query Language](https://specifications.openehr.org/releases/QUERY/latest/AQL.html)
