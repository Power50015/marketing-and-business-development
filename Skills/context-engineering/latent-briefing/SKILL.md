# Latent Briefing

## When to Use
Use this skill when orchestrating multi-agent workflows where worker agents need context from previous agents without re-computing it. Enables efficient state transfer via KV cache compaction.

## Before Starting
- [ ] Multi-agent architecture is in place (orchestrator + workers)
- [ ] Worker agents need shared context from prior executions
- [ ] Token budget is a concern (want to reduce repeated context)
- [ ] KV cache access is available in your agent framework

## Framework / Methodology
1. **Identify Shareable Context** — Determine which parts of the orchestrator's state are needed by workers
2. **Compact into Latent Form** — Compress context into a minimal representation (embeddings, summaries, or KV cache pointers)
3. **Transfer to Worker** — Inject latent state into worker's context window or cache
4. **Worker Execution** — Worker operates with compacted context, producing outputs
5. **Update Orchestrator State** — Worker outputs are integrated back into orchestrator's state

## Output Format
A latent briefing protocol document specifying:
- What context is shared
- Compression method (summary, embedding, cache pointer)
- Transfer mechanism (file, API, shared memory)
- Worker agent interface contract
- State integration rules

## Related Skills
- `multi-agent-patterns/` — For orchestrator/worker architectures
- `context-compression/` — For compaction techniques
- `memory-systems/` — For persistent state storage
- `tool-design/` — For implementing briefing interfaces

## Common Mistakes
- Over-compression (loses critical nuance)
- Under-compression (saves too little, defeats the purpose)
- No versioning (worker uses stale latent state)
- Assuming all workers need the same briefing (different roles need different context)