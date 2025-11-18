---
layout: default
title: Introduction
nav_order: 1
---

# Introduction to ARCOS

**ARCOS (AI Rule-Constrained Orchestration System)** is a schema-driven framework for orchestrating AI agents under strict specification and validation rules. It defines how a Coordinator (**Maestro**) interacts with **Speculus**, **Producer**, **Validator**, and **Post-Processor** agents through domain-agnostic XML messaging validated against schemas.

## Why ARCOS?

- **Deterministic AI orchestration**: Every interaction is validated against XSD contracts.
- **Composable agents**: Swap in your own Producers, Validators, or Post-Processors.
- **Domain-agnostic**: Bring your own schema; ARCOS will give it to each domain component.
- **Fail-fast philosophy**: Invalid XML is rejected immediately.

This documentation site will guide you through the core concepts, architecture, and components of the ARCOS system.