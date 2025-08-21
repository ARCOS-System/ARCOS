# ARCOS – AI Rule-Constrained Orchestration System

ARCOS is a schema-driven framework for orchestrating AI agents under strict 
specification and validation rules. It defines how a Coordinator (Maestro) 
interacts with Speculus, Producer, Validator, and Post-Processor agents, 
with domain-specific schemas providing the business rules.

This repository publishes the **ARCOS schemas (XSD)**, example XML files, 
documentation PDFs, and diagrams. 

It also provides a stable URL base for referencing schemas in XML documents.

---

## 📂 Repository Structure

<details>
<summary>Directory structure</summary>

**Top-level files**
- README.md
- LICENSE
- CONTRIBUTING.md
- index.html

<details>
<summary>1- Docs (Current) — Overview PDFs & support files</summary>

```text
1- Docs (Current)/
├── ARCOS.pdf
├── ARCOS-Orchestrator.pdf
├── ARCOS-Speculus.pdf
├── Domain-Speculus.pdf
├── Domain-Producer.pdf
├── Domain-Validator.pdf
├── Domain-Post-Processor.pdf
└── JPG/, SVG/, PNG/
```

</details>

<details>
<summary>2- Components — Per-component details and sample XML</summary>

<details>
<summary>Core Related</summary>

```text
Core Related/
├── 1-ARCOS-Orchestrator/
└── 2-ARCOS-Speculus/
```

</details>

<details>
<summary>Domain Related</summary>

```text
Domain Related/
├── 3-Domain-Speculus/
├── 4-Domain-Producer/
├── 5-Domain-Validator/
└── 6-Domain-Post-Processor/
```

</details>

</details>

<details>
<summary>3- Stable — Published schemas (XSD), versioned & immutable</summary>

<details>
<summary>v0.3.1</summary>

```text
v0.3.1/
├── Arcos_Project.xsd
├── ARCOS_Speculus_Response.xsd
├── Domain_Rules.xsd
├── Maestro_ArcosSpeculus_Messaging.xsd
├── Maestro_DomainSpeculus_Messaging.xsd
├── Maestro_PostProcessor_Messaging.xsd
├── Maestro_Producer_Messaging.xsd
├── Maestro_Validator_Messaging.xsd
├── PostProcessor_Report.xsd
├── PostProcessor_Response.xsd
├── Predefined_Domain_Rules.xsd
├── Producer_Response.xsd
├── Validator_Report.xsd
├── Validator_Response.xsd
└── bleu_parts_v5.xsd
```

</details>

</details>

<details>
<summary>latest — Copy of the most recent version</summary>

```text
latest/
└── v0.3.1/  (symlink or copy)
```

</details>

</details>
