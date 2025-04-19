# Svelte Basics for OpenEHR Applications

This guide provides a concise introduction to using Svelte for building OpenEHR applications, focusing on the specific patterns and techniques needed for the bootcamp.

## What is Svelte?

Svelte is a modern JavaScript framework that compiles your code at build time rather than interpreting it at runtime. This approach results in highly optimized applications with minimal bundle sizes.

Key features:
- No virtual DOM
- True reactivity
- Less boilerplate code
- Built-in transitions and animations

## Setting Up a Svelte Project

### Prerequisites

- Node.js installed (version 14 or later)
- npm or yarn package manager

### Creating a New Project

```bash
# Create a new project
npm create svelte@latest my-openehr-app

# Navigate to project directory
cd my-openehr-app

# Install dependencies
npm install

# Start development server
npm run dev
```

## Svelte Component Basics

Svelte components are single `.svelte` files that contain:
1. Script (JavaScript)
2. Style (CSS)
3. Template (HTML)

### Basic Component Structure

```svelte
<script>
  // JavaScript goes here
  let name = 'Patient';
</script>

<style>
  /* CSS goes here */
  h1 {
    color: #3b82f6;
  }
</style>

<!-- HTML template goes here -->
<h1>Hello {name}!</h1>
```

## Data Binding and Reactivity

### Two-way Binding

```svelte
<script>
  let patientName = '';
</script>

<input bind:value={patientName}>
<p>Patient name: {patientName}</p>
```

### Reactive Declarations

```svelte
<script>
  let systolic = 120;
  let diastolic = 80;
  
  // This will update automatically when systolic or diastolic changes
  $: meanArterialPressure = ((2 * diastolic) + systolic) / 3;
</script>

<input type="number" bind:value={systolic}>
<input type="number" bind:value={diastolic}>
<p>Mean Arterial Pressure: {meanArterialPressure.toFixed(1)}</p>
```

## Handling OpenEHR Data

### Fetching Data from OpenEHR Server

```svelte
<script>
  import { onMount } from 'svelte';
  
  let compositions = [];
  let loading = true;
  let error = null;
  
  onMount(async () => {
    try {
      const response = await fetch('http://localhost:8080/ehrbase/rest/openehr/v1/query/aql', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          q: 'SELECT c FROM COMPOSITION c'
        })
      });
      
      if (!response.ok) {
        throw new Error('Failed to fetch data');
      }
      
      const data = await response.json();
      compositions = data.rows || [];
    } catch (err) {
      error = err.message;
    } finally {
      loading = false;
    }
  });
</script>

{#if loading}
  <p>Loading compositions...</p>
{:else if error}
  <p class="error">Error: {error}</p>
{:else if compositions.length === 0}
  <p>No compositions found</p>
{:else}
  <ul>
    {#each compositions as composition}
      <li>{composition.name}</li>
    {/each}
  </ul>
{/if}
```

### Creating a Form for OpenEHR Data

```svelte
<script>
  let vitalSigns = {
    systolic: 120,
    diastolic: 80,
    heartRate: 72,
    temperature: 37,
    respiratoryRate: 16
  };
  
  async function submitVitalSigns() {
    // Transform to OpenEHR composition format
    const composition = {
      // Simplified example - actual structure depends on your template
      "archetype_details": {
        "template_id": {
          "value": "vital_signs"
        }
      },
      "content": [
        {
          "archetype_node_id": "openEHR-EHR-OBSERVATION.blood_pressure.v2",
          "data": {
            "events": [{
              "data": {
                "items": [
                  {
                    "archetype_node_id": "at0004",
                    "value": {
                      "magnitude": vitalSigns.systolic,
                      "units": "mm[Hg]"
                    }
                  },
                  {
                    "archetype_node_id": "at0005",
                    "value": {
                      "magnitude": vitalSigns.diastolic,
                      "units": "mm[Hg]"
                    }
                  }
                ]
              }
            }]
          }
        }
        // Additional observations would be added here
      ]
    };
    
    try {
      const response = await fetch('http://localhost:8080/ehrbase/rest/openehr/v1/composition', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify(composition)
      });
      
      if (!response.ok) {
        throw new Error('Failed to submit data');
      }
      
      alert('Vital signs submitted successfully!');
    } catch (error) {
      alert(`Error: ${error.message}`);
    }
  }
</script>

<form on:submit|preventDefault={submitVitalSigns}>
  <div>
    <label>
      Systolic BP (mmHg):
      <input type="number" bind:value={vitalSigns.systolic}>
    </label>
  </div>
  
  <div>
    <label>
      Diastolic BP (mmHg):
      <input type="number" bind:value={vitalSigns.diastolic}>
    </label>
  </div>
  
  <div>
    <label>
      Heart Rate (bpm):
      <input type="number" bind:value={vitalSigns.heartRate}>
    </label>
  </div>
  
  <div>
    <label>
      Temperature (°C):
      <input type="number" step="0.1" bind:value={vitalSigns.temperature}>
    </label>
  </div>
  
  <div>
    <label>
      Respiratory Rate (breaths/min):
      <input type="number" bind:value={vitalSigns.respiratoryRate}>
    </label>
  </div>
  
  <button type="submit">Submit Vital Signs</button>
</form>
```

## Best Practices for OpenEHR Applications

1. **Separate Data Transformation Logic**
   - Create utility functions to transform between OpenEHR formats and your application's data model

2. **Create Reusable Components**
   - Build components for common OpenEHR structures (observations, evaluations, etc.)

3. **Handle Authentication**
   - Implement proper authentication for OpenEHR server requests

4. **Validate Data**
   - Validate user input against OpenEHR constraints before submission

5. **Error Handling**
   - Implement comprehensive error handling for API requests

## References

- [Svelte Documentation](https://svelte.dev/docs)
- [OpenEHR REST API Specification](https://specifications.openehr.org/releases/ITS-REST/latest/)
- [EHRbase Documentation](https://ehrbase.readthedocs.io/en/latest/)
- [Svelte Tutorial](https://www.youtube.com/watch?v=zojEMeQGGHs)
