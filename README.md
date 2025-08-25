# ARCOS – AI Rule-Constrained Orchestration System

[![License](https://img.shields.io/github/license/ARCOS-System/ARCOS)](LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/ARCOS-System/ARCOS)](https://github.com/ARCOS-System/ARCOS/issues)
[![GitHub stars](https://img.shields.io/github/stars/ARCOS-System/ARCOS)](https://github.com/ARCOS-System/ARCOS/stargazers)
[![GitHub Pages](https://img.shields.io/badge/docs-online-blue)](https://arcos-system.github.io/ARCOS/)

ARCOS is a **schema-driven framework** for orchestrating AI agents under strict 
specification and validation rules. It defines how a Coordinator (*Maestro*) 
interacts with **Speculus**, **Producer**, **Validator**, and **Post-Processor** agents, 
with domain-specific schemas providing the business rules.

📦 This repository publishes the **ARCOS schemas (XSD)**, example XML files, 
documentation PDFs, and architecture diagrams.  
🔗 It also provides a **stable URL base** for referencing schemas in XML documents.

---

## ✨ Why ARCOS?
- **Deterministic AI orchestration** – every interaction is validated against XSD contracts.  
- **Composable agents** – swap in your own Producers, Validators, or Post-Processors.  
- **Domain-agnostic** – bring your own schema; ARCOS enforces the rules.  
- **Fail-fast philosophy** – invalid XML is rejected immediately.  

## 🚀 Quick Links
- [ARCOS Documentation (.io site)](https://arcos-system.github.io/ARCOS/)  
- [Schema Directory (XSD)](https://github.com/ARCOS-System/ARCOS/tree/main/3-Stable/v0.3.1)  
- [Example XML Files](https://github.com/ARCOS-System/ARCOS/tree/main/2-Components)  
- [ARCOS PDF Overview](https://github.com/ARCOS-System/ARCOS/tree/main/1-Docs%20(Current))  

## 📖 Getting Started
1. Clone this repo.  
2. Validate an example XML against its schema with your favorite XSD validator.  
3. Explore how Maestro coordinates Speculus → Producer → Validator → Post-Processor using the included diagrams.  

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
│ ├── 2-ARCOS-Architecture-and-Messaging.pdf
│ ├── 3-Domain and ARCOS-Speculus Guide.pdf
│ ├── 4-Domain-Producer Guide.pdf
│ ├── 5-Domain-Validator Guide.pdf
│ ├── 6-Domain-Post-Processor Guide.pdf
│ ├── 7-Domain-Filtering-Input Guide.pdf
│ ├── 8-ARCOS-Orchestrator Guide.pdf
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
