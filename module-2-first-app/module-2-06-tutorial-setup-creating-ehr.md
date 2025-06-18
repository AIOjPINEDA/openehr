# Tutorial: Setup and Creating EHR - Module 2

## Overview

This tutorial covers the complete initial setup for Module 2's vital signs application, including template preparation, EHR creation via Postman, and Svelte project configuration.

## Prerequisites

- **Node.js and npm** installed
- **Postman** for API testing  
- **Code editor** (Cursor IDE or VS Code recommended)
- **Template from Module 1** (vital signs template created in Archetype Designer)
- Access to bootcamp OpenEHR server: `https://openehr-bootcamp.medblocks.com/ehrbase`

## Step 1: Create EHR ID via Postman

### API Endpoint
- **Method**: `POST`
- **URL**: `/rest/openehr/v1/ehr`
- **Server**: `https://openehr-bootcamp.medblocks.com/ehrbase`

### Process
1. Open Postman
2. Navigate to the EHR creation endpoint
3. Send POST request
4. **Save the returned EHR ID** - you'll use it throughout the application

### Expected Response
```json
{
  "ehr_id": {
    "value": "550e8400-e29b-41d4-a716-446655440000"
  }
}
```

## Step 2: Initialize Svelte Project

### Terminal Commands
```bash
# Create new Svelte project
npx sv create

# Follow the interactive prompts:
```

### Configuration Prompts
```
? What would you like your project to be called? 
> 2-first-app

? Which template would you like?
> SvelteKit minimal

? Do you want TypeScript?
> No (select JavaScript for simplicity)

? Do you want Tailwind CSS?
> Yes

? Which package manager?
> pnpm (faster than npm)
```

### Navigate to Project
```bash
cd 2-first-app
```

### Open in Code Editor
```bash
# For Cursor IDE
cursor 2-first-app

# For VS Code  
code 2-first-app
```

### Project Structure
```
2-first-app/
├── src/
│   ├── routes/
│   │   └── +page.svelte    # Main application page
│   ├── app.html
│   └── app.css
├── package.json
├── svelte.config.js
└── tailwind.config.js
```

## Step 3: Development Environment Setup

### Open Project in Editor
```bash
cursor 2-first-app
```

### Start Development Server
```bash
npm run dev
```
- Application runs on `http://localhost:5173`
- Default page shows SvelteKit welcome message

## Step 4: Integrate EHR ID into Application

### Edit Main Route File
**File**: `src/routes/+page.svelte`

```svelte
<script>
  let ehrId = "550e8400-e29b-41d4-a716-446655440000"; // Your actual EHR ID
</script>

<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>

<p>EHR ID: {ehrId}</p>
```

### Verification
- Save the file
- Check browser to see EHR ID displayed
- Confirms Svelte reactive updates are working

## Technology Stack Summary

- **Frontend Framework**: Svelte + SvelteKit
- **Styling**: Tailwind CSS
- **Package Manager**: pnpm
- **Language**: JavaScript (TypeScript optional)
- **Development Server**: Vite (built into SvelteKit)

## Next Steps

With the basic setup complete, the next tutorials will cover:
1. **Creating compositions** using Medblocks UI
2. **Listing compositions** with AQL queries
3. **Deleting compositions** via REST API
4. **Updating compositions** (optional advanced feature)

## Key Takeaways

- **EHR ID is essential** - it's required for all composition operations
- **Svelte is beginner-friendly** - similar to HTML/CSS/JS with reactive features
- **Tailwind CSS** accelerates styling development
- **Development environment** should be tested before proceeding with features

## Troubleshooting

- **Port conflicts**: Change port in `vite.config.js` if 5173 is occupied
- **Package installation**: Use `pnpm install` if dependencies are missing
- **EHR ID issues**: Verify the POST request succeeded and copy the exact ID value
