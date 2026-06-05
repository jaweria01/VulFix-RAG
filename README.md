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

The project explores the intersection of:

- Software Security
- Program Analysis
- Retrieval-Augmented Generation (RAG)
- LLMs for Code
- Automated Vulnerability Repair
