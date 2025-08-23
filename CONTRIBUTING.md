# Contributing to ARCOS (Agent Developers)

Thank you for your interest in contributing to **ARCOS (AI Rule-Constrained Orchestrating System)**.  
As an agent developer (Speculus, Producer, Validator, Post-Processor), you help expand the ARCOS ecosystem
by writing modules that communicate via XML over schema-defined contracts.

---

## 📜 Guiding Principles

1. **Schema-Driven Contracts**
   - All inter-agent communication is XML validated against XSD schemas in the `XSD/` directory.
   - Your agent must *only* accept and produce XML conforming to its messaging/response schemas.
   - Shared primitives (e.g., checksums) come from `XSD/Common.xsd`.

2. **Fail-Fast Philosophy**
   - If incoming XML fails validation, the agent must reject it clearly with a schema-valid error response.
   - Never attempt to “guess” intent on malformed input.

3. **Domain Stance: Your Agent, Your Rules**
   - ARCOS core and Maestro remain domain-agnostic.
   - **Agents can be fully domain-specific.** You may hardcode domain knowledge, business rules, or opinionated behavior inside your agent.
   - Agents should still *speak ARCOS* at their boundaries: inputs and outputs must validate against the ARCOS XSDs, and checksums/types must come from shared primitives where defined.

---

## 🛠 Development Workflow

1. **Setup**
   - Clone the repository and review the schemas under `XSD/`.
   - Identify which schema governs your agent’s inputs and outputs.
     - Example: Producer → `Maestro_Producer_Messaging.xsd` + `Producer_Response.xsd`.

2. **Implementing an Agent**
   - Agents are standalone programs or services (CLI, daemon, HTTP API, etc.).
   - Input: XML file/string → validate against schema.
   - Process: Apply logic (e.g., generate code, validate, compile). Domain-specific logic is welcome.
   - Output: XML file/string → validate against schema before returning.

3. **Validation**
   - Always run an XSD validator on both inputs and outputs.
   - Include schema validation in your automated tests.

4. **Error Handling**
   - On failure, return the schema-defined error structure (`Clarification`, `Failure`, etc.).
   - Always include a checksum where required (`common:SHA256Type`).

5. **Testing**
   - Add sample XML input/output files in `2-Components/<AgentName>/SampleXML/`.
   - Ensure all examples validate against the schemas.
   - If your agent emits artifacts (e.g., zips, logs), consider attaching an `artifact_manifest.xml` or `focus_manifest.xml` for traceability.

---

## ✅ Contribution Checklist

Before submitting a Pull Request:
- [ ] Inputs/outputs validate against schemas
- [ ] Code is heavily commented (ARCOS values transparency)
- [ ] Added/updated sample XML files
- [ ] Added/updated README.md for your agent
- [ ] All automated tests pass

---

## 📂 Key Schemas for Agents

- **ARCOS Speculus**  
  - Input: `Maestro_ARCOS_Speculus_Messaging.xsd`  
  - Output: `ARCOS_Speculus_Response.xsd`

- **Domain Speculus**  
  - Input: `Maestro_Domain_Speculus_Messaging.xsd`  
  - Output: `Domain_Speculus_Response.xsd`

- **Producer**  
  - Input: `Maestro_Producer_Messaging.xsd`  
  - Output: `Producer_Response.xsd`

- **Validator**  
  - Input: `Maestro_Validator_Messaging.xsd`  
  - Output: `Validator_Response.xsd` + `Validator_Report.xsd`

- **Post-Processor**  
  - Input: `Maestro_Post_Processor_Messaging.xsd`  
  - Output: `Post_Processor_Response.xsd` + `Post_Processor_Report.xsd`

- **Shared Primitives**  
  - `XSD/Common.xsd` (e.g., `SHA256Type` for checksums)

- **Artifacts & Focus (optional, recommended when producing files)**  
  - `artifact_manifest.xsd`, `focus_manifest.xsd`

---

## 💬 Communication

- Use GitHub Issues for bugs and feature requests.
- Use Discussions for design proposals and schema changes.
- Major agent behavior changes should be discussed before implementation.

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the same license as ARCOS.
