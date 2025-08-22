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

```text
ARCOS_Repo/
├── README.md # This file
├── LICENSE
├── CONTRIBUTING.md
├── index.html # Interactive architecture viewer (loads architecture.svg)
│
├── 1- Docs (Current)/ # Overview PDFs & support files
│ ├── 1-ARCOS.pdf
│ ├── 2-ARCOS-Orchestrator.pdf
│ ├── 3-ARCOS-Speculus.pdf
│ ├── 4-Domain-Speculus.pdf
│ ├── 5-Domain-Producer.pdf
│ ├── 6-Domain-Validator.pdf
│ ├── 7-Domain-Post-Processor.pdf
│ ├── 8-Domain-Filtering-Input.pdf
│ ├── JPG/, SVG/, PNG/ # Supporting images for docs/viewer
│
├── 2- Components/ # Per-component details and sample XML
│ ├── Core Related/
│ │ ├── 1-ARCOS-Orchestrator/
│ │ ├── 2-ARCOS-Speculus/
│ ├── Domain Related/
│   ├─ 3-Domain-Speculus/
│   ├─ 4-Domain-Producer/
│   ├─ 5-Domain-Validator/
│   ├─ 6-Domain-Post-Processor/
│
└── 3- Stable/ # Published schemas (XSD), versioned & immutable
├── v0.3.1/
│ ├── Arcos_Project.xsd
│ ├── Maestro_.xsd
│ ├── Producer_Response.xsd
│ ├── Validator_.xsd
│ ├── PostProcessor_*.xsd
│ ├── Domain_Rules.xsd
│ ├── Predefined_Domain_Rules.xsd
│ ├── bleu_parts_v5.xsd
│ ├──
│ ├──
│ ├──
│ ├──
│ ├──
│ ├──
│ ├──
│ ├──
│ ├──
│ ├──
└── latest/ # Copy of the most recent version (convenience for viewer)
```
