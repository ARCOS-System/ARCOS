---
layout: default
title: Getting Started
nav_order: 4
---

# Getting Started Tutorial

This tutorial provides a hands-on walkthrough of the ARCOS repository. You will learn how to clone the project, locate key files, and perform a basic validation of a sample XML file against its schema.

## Prerequisites

Before you begin, ensure you have the following tools installed:
*   **Git:** For cloning the repository.
*   **An XML Schema Validator:** We will use `xmllint`, which is a standard command-line tool for XML validation, often pre-installed on Linux and macOS.

## 1. Clone the Repository

First, clone the ARCOS repository to your local machine using the following command:

```bash
git clone https://github.com/ARCOS-System/ARCOS.git
cd ARCOS
```

## 2. Locate the Sample Files

This repository includes sample domains to help you understand how ARCOS works. For this tutorial, we will use the `BLEU` sample domain.

Navigate to the directory containing the sample XML and its corresponding schema:

```bash
cd SampleDomains/BLEU/v5/
```

You will find two key files here:
*   `BLEU_parts_v5.xsd`: The XML Schema Definition (XSD) that defines the structure and rules for the inventory of a fictional parts manufacturer.
*   `BLEU_inventory_v5_sample.xml`: A sample XML file containing inventory data that conforms to the schema.

## 3. Understand the Schema and XML

The **XSD file (`BLEU_parts_v5.xsd`)** acts as a blueprint, defining the expected structure of the data. It specifies what elements are allowed (e.g., `Bolt`, `Nut`, `Washer`), their attributes (e.g., `id`, `code`), and their data types.

The **XML file (`BLEU_inventory_v5_sample.xml`)** is an instance of this blueprint. It contains the actual inventory data, structured according to the rules defined in the XSD. Notice the `xsi:noNamespaceSchemaLocation` attribute in the XML, which points to the location of the schema file that should be used for validation.

## 4. Validate the XML

The core principle of ARCOS is schema-driven validation. You can test this yourself by validating the sample XML against its schema using `xmllint`:

```bash
xmllint --noout --schema BLEU_parts_v5.xsd BLEU_inventory_v5_sample.xml
```

If the validation is successful, the command will output:
```
BLEU_inventory_v5_sample.xml validates
```

This confirms that the sample data adheres to the rules defined in the schema.

## Conclusion

Congratulations! You have successfully cloned the ARCOS repository and validated a sample XML file. This simple exercise demonstrates the fundamental concept of ARCOS: ensuring that all data and messages conform to a predefined, verifiable structure.

From here, you can explore the other documentation sections to learn more about the system's [Architecture](./architecture.md) and [Component Guides](./guides.md).