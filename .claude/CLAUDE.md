# FastAPI Hexagonal Architecture Starter - Project Instructions

## Project Structure
This is the main CLAUDE.md for this FastAPI starter project. Documentation is organized in subdirectories:

- `.claude/project/` - General project guidelines and conventions

## Project Guidelines
Always follow the conventions in:
- **General Guidelines**: `.claude/project/general-guidelines.md` - Code formatting and file conventions

## Architecture
This project follows Hexagonal Architecture (Ports & Adapters) with clear separation between:
- **Domain Layer**: Business logic, independent of infrastructure
- **API Layer**: HTTP interface, request/response handling
- **External Layer**: Infrastructure implementations (database, logging, etc.)

## Development Guidelines
- Follow the hexagonal architecture principles when creating new features
- Keep domain logic independent of infrastructure concerns
- Use repository interfaces (ports) for data access
- Implement concrete repositories (adapters) in the external layer

## Tool Usage
- Use the GitHub grep MCP tool (`mcp__grep__searchGitHub`) **conservatively** to minimize credit usage
- Only use it when there's significant benefit, such as:
  - Being stuck on a specific implementation problem where real-world examples are critical
  - User explicitly requests examples from real codebases
  - Dealing with highly specialized cases where production patterns are essential
- For most tasks, rely on existing knowledge, project codebase patterns, and standard practices
