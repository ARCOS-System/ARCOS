# ARCOS System — TODO (Programming-Oriented)

> **Design choice**: All code in **Rust**.  
> **Contract-first**: All inter-component I/O is XML validated by XSD.  
> **Goal**: Each checklist item should map cleanly to issues/PRs.

## Core Entities (used across components)
- [ ] **Project** (id, name, status, domains, versions)
- [ ] **User/Session** (login, permissions)
- [ ] **Message** (User↔Maestro (Orchestrator), ARCOS-Speculus, Domain Speculus, Validator, Post-Processor)
- [ ] **Speculus** (ARCOS Speculus, Domain Speculus)
- [ ] **Vocabulary & Rules** (Vocabulary, predefined and current project rules)
- [ ] **Producer Brief** (inputs distilled for generation)
- [ ] **Artifacts** (files, directories)
- [ ] **Manifest** (artifact inventory / checksums)
- [ ] **Validation Report** (errors/warnings, locations, suggestions)
- [ ] **Focus Set** (file+section subset for retries)
- [ ] **Delta Policy** (rebuild/replay constraints)

---

## 1) Portal (Local App)
### Entities → Concepts → Functionality
**User/Session**
- [ ] Auth: Username/password store (local SQLite / Postgres) and session tokens.
- [ ] Roles: Basic RBAC (owner, editor, viewer).

**Project**
- [ ] CRUD: Create, list, update, delete projects.
- [ ] Workspace: Local project directory bootstrap (config, schema refs).
- [ ] Status: Display last run state (Validated / Failed / Draft).

**Message**
- [ ] Builder: UI to compose *New Project* / *Edit Project* messages.
- [ ] XSD guardrails: Inline validation against messaging schemas with errors surfaced to UI.

**Speculus (ARCOS)**
- [ ] Selectors: Choose Domain specific AI agents, + Domain package (schema URIs).
- [ ] Integrity: Fetch & cache schemas; verify checksums (if provided).
**Speculus (Domain)**
- [ ] UI: From the free form user's text, extract project's rules

**Run Control**
- [ ] Invoke Orchestrator: Fire-and-log request; show live run log (tail).
- [ ] Attachments: Attach local files when required (e.g., initial ARCOSProject inline).

**Nice to have**
- [ ] Browser: Tree viewer of latest output, with quick open in external editor.

---

## 2) Orchestrator
### Entities → Concepts → Functionality
**Message**
- [ ] Router: Deserialize & dispatch requests to Speculus/Validator/Producer/Post-Processor.
- [ ] Contracts: Strongly-typed Rust models bound to XSD (serde + quick-xml).

**Project**
- [ ] State Machine: Draft → Generated → Validated → Failed → Retrying.
- [ ] Persistence: Run history with timestamps, component versions, checksums.

**Speculus**
- [ ] ARCOS pass: Define AI Agents to use, and domain schemas
- [ ] Domain pass: Load domain-specific constraints and options.

**Producer Brief**
- [ ] Synthesis: Build minimal, deterministic brief (inputs, constraints, examples).
- [ ] Redaction: Strip irrelevant context on retries using Focus Set.

**Focus Set / Artefact Manifest**
- [ ] Retry Logic: If validation fails, compute target subset & pass to Producer.
- [ ] After Production, extract all files from the output.zip and create them locally in a User's space (UserID, ProjectID)

**Validation Report**
- [ ] Reroute: On error, send back to producer, including the report, and previous code.

**Observability**
- [ ] Tracing: `tracing` spans across components with run-id propagation.
- [ ] Audit: Append-only log file per project.

---

## 3) ARCOS-Speculus
### Entities → Concepts → Functionality
**Speculus (ARCOS)**
- [ ] Selectors / Registry: Load Domain Schema and IA Agents from a bank of domains
- [ ] Write a Purpose.

**Process Expansion**
- [ ] Subprojects: Support multiple producers (e.g., CodeGen, DocGen) per run.
- [ ] Constraints: System-level rules (e.g., mandatory reports, packaging policy).

**Messaging**
- [ ] Output: Emit Maestro/Orchestrator messages, and an initial ARCOS_Project conforming to ARCOS_Project schema

---

## 4) Domain Speculus
### Entities → Concepts → Functionality
**Vocabulary & Rules**
- [ ] Load Packs: `DomainVocabularyAndRules.xml` (predefined = read-only; project rules = editable).
- [ ] Integrity: Verify external domain schema checksum (if provided).

**Rule Extraction**
- [ ] Intent Linkage: Map user intents → candidate rules; surface dependencies.
- [ ] Dependency Graph: Build DAG; detect sub-rules and cycles.
- [ ] Application: Apply accepted rules to produce domain constraints.

**Producer Brief (Domain)**
- [ ] Domain Shaping: Extract project rules from free-form user text and serialize into ARCOS_Project update.
- [ ] Sanitization: Enforce domain schema enumerations & ranges.

**Messaging**
- [ ] Emit Domain Speculus outputs consumable by Orchestrator/Producer, and Updated ARCOS_Project .

---

## 5) Validator
### Entities → Concepts → Functionality
**Validation Report**
- [ ] Structure: Errors, warnings, notes; file path + line/col; codes; suggestions.
- [ ] Output: Emit ARCOS_Project conformity in a validation_report.xml respecting the schema.

**Checks**
- [ ] Schema Validation: Validate outputs against ARCOS_Project rules.
- [ ] Semantic Rules: Domain rule checks (deps satisfied, uniqueness, invariants).
- [ ] Cross-file: Manifest vs. disk, references resolvable, orphan files.
- [ ] Policy: Enforce packaging/naming conventions.

**Focus Hints**
- [ ] Extraction: Identify failing files/sections to seed Focus Set.

**Tooling**
- [ ] Test Fixtures: Golden files; property tests for rule invariants.

---

## 6) Post-Processor
### Entities → Concepts → Functionality
**Artifacts**
- [ ] Normalization: Rename, format, layout (e.g., license headers).
- [ ] Synthesis: Generate secondary artefacts (indexes, READMEs, reports).

**Packaging**
- [ ] Bundle: Zip vs. raw files policy; embed manifest & reports.

**Reporting**
- [ ] Post-Process Report: Summarize actions (added/removed/renamed), timings.

**Messaging**
- [ ] Response: Structured success/failure with links to outputs.

**Milestone 1**
- [ ] Actions: run cargo check/cargo build on generated code,  
      capture compiler diagnostics,  
      send structured report back to Orchestrator.

---

## 7) Artefact Extractor *(Nice to have)*
### Entities → Concepts → Functionality
**Manifest**
- [ ] Create: Enumerate files, sizes, checksums, provenance. Local UserID/ProjectID storage space ... 
          where code will be compiled
- [ ] Version: Manifest per run; link to run-id and component versions.

**Delta Policy**
- [ ] Compute: Changes between manifests; classify (added/removed/modified).
- [ ] Apply: Rebuild requested bundle from local store deterministically.

**Repro**
- [ ] Rebuild: Produce output.zip solely from manifest + deltas.

---

## 8) Focus Extractor *(Nice to have)*
### Entities → Concepts → Functionality
**Focus Set**
- [ ] Derive: From validation report + manifest; map to file paths/regions.
- [ ] Granularity: File-level first; region-level (line ranges) when available.

**Producer Brief Integration**
- [ ] Filter: Reduce inputs to only necessary context; retain dependencies.

**Safety**
- [ ] Guardrails: Ensure required context (schemas, shared headers) stays included.

---

## 9) Producer (Shell)
### Entities → Concepts → Functionality
**Producer Brief**
- [ ] IO: Read ARCOS+Domain brief(s) and serialize prompts.

**Generation**
- [ ] Callout: Invoke OpenAI; stream responses; handle multi-file boundaries.
- [ ] Capture: Write files; preserve structure; detect collisions.

**Zip Safety**
- [ ] Auto-bundle: Zip outputs.
- [ ] Integrity: Compute manifest and attach to run.

**Retry Mode**
- [ ] Focus: Accept Focus Set and prune context accordingly.

**Hygiene**
- [ ] PII/Secrets: Static scan for PII/secrets; optional user-configurable patterns.

---

## Cross-Cutting (Shared crates & infra)
- [ ] **arcos-common**: error types, run-id, paths, checksums.
- [ ] **arcos-xml**: XSD-backed structs, (de)serialization helpers, schema loader/cache.
- [ ] **arcos-io**: workspace fs ops, zipping, hashing, manifest utils.
- [ ] **arcos-messaging**: generated Rust bindings for all schemas.
- [ ] **config**: env + TOML; per-project overrides.
- [ ] **telemetry**: `tracing`, structured logs, optional JSON export.
- [ ] **testing**: fixtures, golden files, end-to-end harness (orchestrator-driven).

---

## Acceptance Criteria (per component)
- [ ] **Schemas enforced**: All inputs/outputs validated at boundaries.
- [ ] **Determinism**: Same inputs → same outputs (manifest proves it).
- [ ] **Traceability**: Every file in outputs ties to a run-id and checksum.
- [ ] **Retry discipline**: Failed run produces Focus Set; next run consumes it.
- [ ] **Reproducibility**: Artefact Extractor can rebuild any validated bundle.
