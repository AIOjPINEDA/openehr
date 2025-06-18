# Tutorial: Setup and Creating EHR - Module 2

## Overview

This tutorial covers the complete initial setup for Module 2's vital signs application, including template preparation, EHR creation via Postman, and Svelte project configuration.

## Prerequisites

- **Conda environment** activated (`openehr-env`)
- **Postman** for API testing  
- **VS Code** as code editor
- Access to bootcamp OpenEHR server: `https://openehr-bootcamp.medblocks.com/ehrbase`

## Step 1: Create EHR ID via Postman

### API Endpoint
- **Method**: `POST`
- **URL**: `/rest/openehr/v1/ehr`
- **Server**: `https://openehr-bootcamp.medblocks.com/ehrbase`

### Process
1. Open Postman
2. Create POST request to: `https://openehr-bootcamp.medblocks.com/ehrbase/rest/openehr/v1/ehr`
3. Set headers: `Content-Type: application/json`, `Accept: application/json`
4. Send request and **save the returned EHR ID**

### Expected Response
```json
{
  "ehr_id": {
    "value": "73a2a39a-1583-42ff-ad2f-641e52bbc687"
  }
}
```

## Step 2: Initialize Svelte Project

### Create Project
```bash
npx sv create
```

### Configuration Choices
```
? Where would you like your project to be created?
> 2-first-app

? Which template would you like?
> SvelteKit minimal

? Add type checking with TypeScript?
> Yes, using JavaScript with JSDoc comments

? What would you like to add to your project?
> none

? Which package manager do you want to install dependencies with?
> pnpm
```

### Handle Installation Issues
If pnpm installation fails:
```bash
# Install pnpm globally
npm install -g pnpm

# Navigate to project and install dependencies
cd 2-first-app
pnpm install
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

## Step 3: Start Development Environment

### Open Project in VS Code
```bash
code 2-first-app
```

### Start Development Server
```bash
pnpm run dev
```
- Application runs on `http://localhost:5173`
- You'll see the SvelteKit welcome page

## Step 4: Integrate EHR ID

### Edit Main Page
**File**: `src/routes/+page.svelte`

```svelte
<script>
  let ehrId = "73a2a39a-1583-42ff-ad2f-641e52bbc687"; // Replace with your EHR ID
</script>

<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>

<p>EHR ID: {ehrId}</p>
```

### Verify Setup
- Save the file
- Check `http://localhost:5173` to see your EHR ID displayed
- Setup is complete when you see the EHR ID on the page

## Technology Stack

- **Frontend**: Svelte + SvelteKit  
- **Package Manager**: pnpm
- **Language**: JavaScript with JSDoc
- **Development Server**: Vite

## Next Steps

Ready for the next tutorial: **Creating compositions using Medblocks UI**

## Troubleshooting

**pnpm not found**: Install with `npm install -g pnpm`
**Port 5173 occupied**: Project will automatically use next available port
**Dependencies missing**: Run `pnpm install` in project directory
