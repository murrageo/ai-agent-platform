# Agent Contract

## Core rules
- Agents accept `State` and return `State`.
- Agents must not call other agents directly.
- Agents must not write to DB directly (engine handles logging/persistence).
- Agents must not call provider SDKs directly (use src/core/llm.py).
- Agents may only write to their own namespace in State.

## Prompt rules
- Prompts are stored as versioned files in /prompts/**.
- Prompt version used must be logged.

## Tool rules
- Any external side effect uses tools registered in the tool registry.

