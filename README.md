# VulFix-RAG: Knowledge-Augmented Vulnerability Repair Framework
## Overview

VulFix-RAG is a Retrieval-Augmented Generation (RAG) framework for automated software vulnerability detection and repair.

The framework combines:

- AST-based static program analysis
- CWE vulnerability classification
- ChromaDB semantic retrieval
- Security knowledge augmentation
- DeepSeek LLM-based patch generation
- Automated patch validation

VulFix-RAG detects vulnerable code, retrieves relevant security guidance, generates secure patches, and validates the generated fixes.

## Motivation

Traditional static analysis tools can identify vulnerabilities but cannot automatically repair them.

Recent advances in Large Language Models (LLMs) enable automated code repair; however, generated fixes may be inaccurate when security context is missing.

VulFix-RAG addresses this challenge by combining vulnerability detection with security knowledge retrieval to improve the quality and reliability of generated security patches.

*The project explores the intersection of:*

- Software Security
- Program Analysis
- Retrieval-Augmented Generation (RAG)
- LLMs for Code
- Automated Vulnerability Repair
  
## Features
**Static Vulnerability Detection**

Detects vulnerabilities using Python Abstract Syntax Tree (AST) analysis.

**Supported Vulnerabilities:**

- SQL Injection (CWE-89)
- Command Injection (CWE-78)
- Hardcoded Credentials (CWE-798)

**CWE-Based Classification**

Maps detected vulnerabilities to Common Weakness Enumeration (CWE) categories.

**Security Knowledge Base**

Stores structured vulnerability knowledge including:

- Description
- Risk Level
- Detection Indicators
- Secure Coding Guidance
- Repair Strategies

**Semantic Retrieval**

Uses ChromaDB and Sentence Transformers to retrieve relevant security guidance using vector similarity search.

**LLM-Based Repair**

Uses DeepSeek through OpenRouter to generate secure code patches.

**Patch Validation**

Automatically validates generated patches against vulnerability-specific security rules.

## System Architecture
![System Architecture](https://github.com/jaweria01/VulFix-RAG/blob/cae03f7ccc3338ae2ea99996a0875d36122e6624/Screenshots/Fig1-VulFix-RAG%20System%20Architecture.png)

## Figure 2 — Vulnerability Detection

![Vulnerability Detection](screenshots/detection.png)

*AST-based vulnerability detection identifying SQL Injection, Command Injection, and Hardcoded Credentials.*

## Figure 3 — Patch Generation

![Patch Generation](screenshots/patch_generation.png)

*DeepSeek-generated security patch using retrieved vulnerability knowledge from the RAG pipeline.*

## Figure 4 — Patch Validation

![Patch Validation](screenshots/validation.png)

*Automated validation confirming that generated patches successfully mitigate identified vulnerabilities.*


## Workflow Explanation

**1. Input Source Code**

The framework receives vulnerable Python source code as input. The code may contain security weaknesses such as SQL Injection, Command Injection, or Hardcoded Credentials.

**2. AST-Based Static Analysis**

The source code is parsed into an Abstract Syntax Tree (AST). AST analysis allows the framework to inspect program structure without executing the code.

**3. Vulnerability Detection**

Custom AST rules analyze the code and identify insecure coding patterns. The framework currently supports:

- SQL Injection (CWE-89)
- Command Injection (CWE-78)
- Hardcoded Credentials (CWE-798)
  
**4. CWE Classification**

Each detected vulnerability is mapped to its corresponding Common Weakness Enumeration (CWE) category, providing a standardized security classification.

**5. ChromaDB Semantic Retrieval**

The detected vulnerability information is converted into vector embeddings and used to query the ChromaDB vector database.

**6. Security Knowledge Retrieval**

The most relevant security guidance is retrieved from the knowledge base, including:

- Vulnerability descriptions
- Risk levels
- Secure coding recommendations
- Repair strategies
- Secure code examples

**7. DeepSeek LLM**

The retrieved security knowledge and vulnerable code snippet are provided to the DeepSeek Large Language Model through a carefully designed security-focused prompt.

**8. Patch Generation**

DeepSeek generates a secure patch that aims to eliminate the vulnerability while preserving the original functionality of the code.

**9. Patch Validation**

The generated patch is automatically validated using vulnerability-specific security rules to determine whether the identified weakness has been successfully mitigated.

**10. Validated Security Patch**

If validation succeeds, the framework outputs a validated security patch that can be reviewed and integrated by developers.

## Future Work

- Support for additional CWE categories
- Multi-language vulnerability analysis
- Automatic patch ranking and scoring
- Vulnerability dataset generation
- CI/CD security integration
- Comparative evaluation of multiple code LLMs
- Automated vulnerability repair benchmarking
- LLM agent security analysis
