# Creating Compositions via OpenEHR API

This guide provides a practical walkthrough for creating your first composition using the OpenEHR REST API, based on the vital signs template from Module 1.

## Overview

Creating a composition involves two main steps:
1. **Create an EHR** (patient record container)
2. **Post a composition** (clinical data) to that EHR

This process transforms your template into real clinical data stored in the OpenEHR system.

## Step 1: Create an EHR (Patient Record)

Before creating compositions, you must first create an EHR container for the patient.

### API Call Details
- **Endpoint**: `POST /rest/openehr/v1/ehr`
- **Method**: POST
- **Headers**: `Content-Type: application/json`, `Accept: application/json`
- **Body**: Empty (EHR ID is auto-generated)

### Expected Response
```json
{
  "ehr_id": {
    "value": "550e8400-e29b-41d4-a716-446655440000"
  }
}
```

### Important Notes
- **Save the EHR ID**: You'll need this for all future composition operations
- **One EHR per patient**: Each patient should have only one EHR
- **Persistent identifier**: The EHR ID remains constant throughout the patient's record

## Step 2: Prepare Composition Data

Use canonical JSON format for your first composition. Start with an example from your template and customize the key fields.

### Essential Fields to Customize

#### 1. Composer Information
Update who is creating the composition:
```json
"composer": {
  "_type": "PARTY_IDENTIFIED",
  "name": "Your Name Here"
}
```

#### 2. Context Timing
Update dates to reflect current time:
```json
"context": {
  "_type": "EVENT_CONTEXT",
  "start_time": {
    "_type": "DV_DATE_TIME",
    "value": "2024-05-24T21:00:00"
  },
  "end_time": {
    "_type": "DV_DATE_TIME",
    "value": "2024-05-24T21:00:00"
  }
}
```

#### 3. Clinical Values
Update the actual vital signs measurements:

**Pulse Rate Example:**
```json
"value": {
  "_type": "DV_QUANTITY",
  "magnitude": 84,
  "units": "/min",
  "precision": 0
}
```

**Blood Pressure Example:**
```json
"items": [
  {
    "name": {"value": "Systolic"},
    "value": {
      "_type": "DV_QUANTITY", 
      "magnitude": 120,
      "units": "mm[Hg]",
      "precision": 0
    }
  },
  {
    "name": {"value": "Diastolic"},
    "value": {
      "_type": "DV_QUANTITY",
      "magnitude": 80, 
      "units": "mm[Hg]",
      "precision": 0
    }
  }
]
```

### Locating Values in Canonical JSON

The canonical JSON structure can be complex. Here's how to find the right fields:

1. **Navigate to content array**: Look for `"content": [...]`
2. **Find the observation**: Look for `"_type": "OBSERVATION"`
3. **Locate the data section**: Find `"data": {...}`
4. **Find events array**: Look for `"events": [...]`
5. **Locate data items**: Find `"items": [...]` within events
6. **Update values**: Look for `"value": {...}` objects

### Realistic Clinical Values

Use clinically appropriate values for testing:

| Vital Sign | Normal Range | Example Value |
|------------|--------------|---------------|
| Heart Rate | 60-100 bpm | 84 bpm |
| Systolic BP | 90-140 mmHg | 120 mmHg |
| Diastolic BP | 60-90 mmHg | 80 mmHg |
| Body Temperature | 36.0-37.5°C | 36.8°C |
| SpO2 | 95-100% | 98% |

## Step 3: Submit the Composition

### API Call Details
- **Endpoint**: `POST /rest/openehr/v1/ehr/{ehr_id}/composition`
- **Method**: POST
- **Headers**: `Content-Type: application/json`, `Accept: application/json`
- **URL Parameter**: Replace `{ehr_id}` with your actual EHR ID
- **Body**: Your customized canonical JSON composition

### Process Checklist
1. ✅ Replace `{ehr_id}` in the URL with your actual EHR ID
2. ✅ Paste your customized canonical JSON into the request body
3. ✅ Verify headers are set correctly
4. ✅ Send the POST request
5. ✅ Check for HTTP status 201 (Created)

## Step 4: Verify Success

### Successful Response Indicators
- **HTTP Status**: 201 (Created)
- **Response Body**: Echo of your composition data with added system metadata
- **Composition UID**: System-generated unique identifier for the composition
- **Version**: Composition version information (usually v1 for first creation)

### Example Success Response Structure
```json
{
  "composition": {
    "uid": {
      "value": "your-composition-uid-here::system::1"
    },
    // ... your composition data with system metadata
  }
}
```

## Common Issues and Solutions

### Problem: "EHR not found"
- **Cause**: EHR ID doesn't exist or is incorrect
- **Solution**: Verify EHR ID is correctly copied and EHR was created successfully

### Problem: "Template not found"
- **Cause**: Template ID in composition doesn't match uploaded template
- **Solution**: Ensure your vital signs template is uploaded to the server

### Problem: "Invalid composition"
- **Cause**: Composition doesn't match template constraints
- **Solution**: Check that all required fields are present and values are within valid ranges

### Problem: "Invalid JSON"
- **Cause**: Malformed JSON syntax
- **Solution**: Validate JSON format using a JSON validator tool

## Troubleshooting Common Errors

### Error: "Observation contains no results"

**Full Error Message:**
```json
{
  "error": "Unprocessable Entity",
  "message": "/content[openEHR-EHR-OBSERVATION.pulse.v2, 1]/data[at0002]/events[at1036, 1]: Observation contains no results, /content[openEHR-EHR-OBSERVATION.blood_pressure.v2, 2]/data[at0001]/events[at1042, 1]: Observation contains no results"
}
```

**Cause:** The observation events have empty `items` arrays instead of actual clinical values.

**Problem in JSON:** 
```json
"data": {
  "_type": "ITEM_TREE",
  "name": {"value": "structure"},
  "items": [], // ❌ Empty array - no actual values
  "archetype_node_id": "at0001"
}
```

**Solution:** Add actual clinical values to the `items` arrays. Here's how to fix it:

#### Fix for Pulse Rate Observation

Replace the empty `items: []` in the pulse observation with:
```json
"items": [
  {
    "_type": "ELEMENT",
    "name": {
      "_type": "DV_TEXT",
      "value": "Rate"
    },
    "value": {
      "_type": "DV_QUANTITY",
      "magnitude": 84,
      "units": "/min",
      "precision": 0
    },
    "archetype_node_id": "at0004"
  }
]
```

#### Fix for Blood Pressure Observation

Replace the empty `items: []` in the blood pressure observation with:
```json
"items": [
  {
    "_type": "ELEMENT",
    "name": {
      "_type": "DV_TEXT",
      "value": "Systolic"
    },
    "value": {
      "_type": "DV_QUANTITY",
      "magnitude": 120,
      "units": "mm[Hg]",
      "precision": 0
    },
    "archetype_node_id": "at0004"
  },
  {
    "_type": "ELEMENT",
    "name": {
      "_type": "DV_TEXT",
      "value": "Diastolic"
    },
    "value": {
      "_type": "DV_QUANTITY",
      "magnitude": 80,
      "units": "mm[Hg]",
      "precision": 0
    },
    "archetype_node_id": "at0005"
  }
]
```

#### Complete Event Structure Example

Here's what a complete event with actual values should look like:
```json
{
  "_type": "INTERVAL_EVENT",
  "name": {
    "_type": "DV_TEXT",
    "value": "Any event"
  },
  "time": {
    "_type": "DV_DATE_TIME",
    "value": "2025-05-24T21:00:00"
  },
  "data": {
    "_type": "ITEM_TREE",
    "name": {
      "_type": "DV_TEXT",
      "value": "structure"
    },
    "items": [
      // ✅ Add actual clinical values here
      {
        "_type": "ELEMENT",
        "name": {
          "_type": "DV_TEXT",
          "value": "Rate"
        },
        "value": {
          "_type": "DV_QUANTITY",
          "magnitude": 84,
          "units": "/min",
          "precision": 0
        },
        "archetype_node_id": "at0004"
      }
    ],
    "archetype_node_id": "at0001"
  },
  "archetype_node_id": "at0003"
}
```

### Quick Fix Steps

1. **Open your composition.json file**
2. **Find each observation with empty `items: []`**
3. **Replace empty arrays with actual clinical values**
4. **Focus on the "Any event" events** (not the specialized ones like "Maximum" or "24 hour average")
5. **Use realistic clinical values** (pulse: 60-100 bpm, BP: 90-140/60-90 mmHg)
6. **Save and retry the POST request**

### Prevention Strategy

To avoid this error in the future:
- **Use Web Template format** instead of canonical JSON for easier development
- **Get example compositions** with actual values from the `/example` endpoint
- **Validate before submission** by checking that all required observations have values
- **Start with minimal viable data** and add complexity gradually

## Next Steps After First Success

Once you've successfully created your first composition:

### 1. Retrieve the Composition
Test fetching the composition back:
```
GET /rest/openehr/v1/ehr/{ehr_id}/composition/{composition_uid}
```

### 2. Query Compositions
Use AQL to find compositions:
```sql
SELECT c FROM COMPOSITION c 
WHERE c/archetype_details/template_id/value = 'JaimePM_vital_signs.v0'
```

### 3. Create More Compositions
Practice with different vital signs values to build familiarity.

### 4. Integrate into Your Application
Use this workflow as the foundation for your Module 2 application:
- Create EHR (if needed)
- Capture user input for vital signs
- Format as canonical JSON
- Submit to OpenEHR server
- Handle success/error responses

## Development Tips

### For Your Module 2 Application
1. **Error Handling**: Always check HTTP status codes and handle failures gracefully
2. **Data Validation**: Validate user input before formatting as canonical JSON
3. **Template Management**: Cache your template structure to format compositions correctly
4. **User Experience**: Provide clear feedback for successful data submission

### Testing Strategy
1. **Start with Postman**: Master the API calls manually first
2. **Use realistic data**: Test with clinically appropriate values
3. **Test edge cases**: Try boundary values and error conditions
4. **Automate gradually**: Move to programmatic API calls once manual process works

---

This practical guide provides the foundation for building your vital signs application. The composition creation workflow is central to any OpenEHR application, making this knowledge essential for Module 2 success.
