# GitHub Copilot Instructions Structure

This project uses an optimized GitHub Copilot instructions structure following Microsoft's best practices.

## Structure Overview

### Main Instructions File
- `.github/copilot-instructions.md` - Core project context and general guidelines (automatically applied to all requests)

### Specific Instructions Files
- `.github/instructions/python-standards.instructions.md` - Applied to Python files (`**/*.py`)
- `.github/instructions/svelte-typescript.instructions.md` - Applied to JS/TS/Svelte files (`**/*.{js,ts,svelte}`)
- `.github/instructions/openehr-api.instructions.md` - Applied to all files (`**`)
- `.github/instructions/clinical-modeling.instructions.md` - Applied to all files (`**`)
- `.github/instructions/testing-standards.instructions.md` - Applied to test files
- `.github/instructions/documentation-standards.instructions.md` - Applied to documentation files (`**/*.{md,rst,txt}`)
- `.github/instructions/sql-database.instructions.md` - Applied to SQL files (`**/*.sql`)

## Key Optimizations

1. **Short and Self-contained**: Each instruction is concise and focused
2. **Context-specific**: Different instructions apply to different file types
3. **Automatic Application**: Uses `applyTo` property for auto-inclusion
4. **Modular**: Easy to maintain and update individual instruction sets
5. **No External References**: All instructions are self-contained

## Benefits

- ⚡ Faster Copilot responses
- 🎯 More precise suggestions per file type
- 🔧 Easier maintenance of instructions
- 👥 Better team collaboration
- 📈 Improved code consistency

## Migration from Original

The original comprehensive instructions file has been:
- Backed up as `.github/copilot-instructions-backup.md`
- Split into focused, modular instruction files
- Optimized for GitHub Copilot's processing capabilities

## VS Code Configuration

Enable the instructions in your VS Code settings:
```json
{
  "chat.promptFiles": true,
  "github.copilot.chat.codeGeneration.useInstructionFiles": true,
  "chat.instructionsFilesLocations": {
    ".github/instructions": true
  }
}
```

## Usage

Instructions are automatically applied based on the file types you're working with. No manual intervention required - GitHub Copilot will automatically use the appropriate instructions for each context.
