# Smart-contract-security-toolkit
An all-in-one Smart Contract Security Toolkit that combines SAST, fuzzing, symbolic execution, invariant testing, and formal verification into a single automated pipeline. The toolkit enhances audit workflows with visual analysis,custom exploit detection, and structured reporting for efficient and scalable smart contract security assessments.


# Smart Contract Security Toolkit

The Smart Contract Security Toolkit is a multi-engine auditing framework that streamlines Web3 security assessments. 

By integrating established security tools with custom exploit detection and visual analysis, this toolkit provides an end-to-end auditing workflow. It is designed for security engineers, auditors, researchers, and developers looking to bridge the gap between running isolated tools and performing comprehensive, structured smart contract audits.

## Overview

Running individual security tools can be time-consuming and often results in fragmented data. This framework automates the execution of multiple analysis engines—ranging from static analysis to formal verification—and aggregates the findings into a single, highly readable report. 

**Core Capabilities:**
* **Multi-layer Security Analysis:** Comprehensive coverage combining static checks, symbolic execution, fuzzing, and formal verification.
* **Custom Exploit Detection:** Identifies complex vulnerabilities such as reentrancy patterns, `tx.origin` misuse, and unchecked external calls.
* **Visual Analysis:** Automatically generates call graphs, control flow graphs (CFGs), and UML diagrams to map contract architecture.
* **Automated Reporting:** Consolidates outputs from all underlying tools and custom rules into a single markdown report.

---

## Installation

### Prerequisites
Ensure you have `python3`, `pip`, and `docker` installed on your system. Docker is highly recommended for environment isolation.

### One-Line Installer (Recommended)
You can set up the entire toolkit and its dependencies using the automated installation script:

```bash
bash <(curl -s [https://raw.githubusercontent.com/YOUR_USERNAME/smart-contract-security-toolkit/main/scripts/install_all.sh](https://raw.githubusercontent.com/YOUR_USERNAME/smart-contract-security-toolkit/main/scripts/install_all.sh))
````

### Manual Setup

To install the toolkit manually, clone the repository and execute the setup script:

```bash
git clone [https://github.com/YOUR_USERNAME/smart-contract-security-toolkit.git](https://github.com/YOUR_USERNAME/smart-contract-security-toolkit.git)
cd smart-contract-security-toolkit
chmod +x scripts/install_all.sh
./scripts/install_all.sh
```

-----

## Usage

You can run the toolkit on any standard Solidity contract. Point the main Python script to your target file to begin the audit.

**Command:**

```bash
python3 smart_contract_audit_toolkit.py contracts/Smartcontract.sol
```

**Output Structure:**
Once the execution is complete, the framework generates a clean directory containing your audit report and visual aids:

```text
output/
├── report.md           # Aggregated findings and structured audit report
└── graphs/
    ├── callgraph.svg   # Function interaction map
    ├── cfg.png         # Control flow execution paths
    └── uml.svg         # Contract architecture diagram
```

-----

## Analysis Engines and Core Tools

This framework orchestrates several highly regarded security tools. The table below outlines how each tool is utilized within the automated pipeline:

| Security Layer | Core Tool(s) | Purpose within the Toolkit |
| :--- | :--- | :--- |
| **Static Analysis (SAST)** | Slither | Parses the Solidity AST to identify common vulnerabilities (e.g., uninitialized variables, strict equalities) without code execution. |
| **Symbolic Execution** | Mythril, Manticore | Mathematically explores contract execution paths to uncover edge-case logic flaws and state manipulation vulnerabilities. |
| **Fuzzing & Invariants** | Echidna | Generates randomized inputs to stress-test the contract logic and verify custom property invariants. |
| **Formal Verification** | Halmos | Provides mathematical proofs of smart contract properties to ensure the code behaves strictly as intended. |
| **Visual Analysis** | Surya, Solgraph, Sol2UML | Generates visual architectures to assist auditors in mapping complex contract interactions and data flows. |
| **Custom Rules** | Python Engine | Overlays custom exploit detection logic tailored to the OWASP Smart Contract Top 10 and OpenZeppelin standards. |

-----

## License and Credits

This project is licensed under the **MIT License**.

This toolkit relies on the excellent work of the Web3 security community. Full credit goes to the creators and maintainers of the underlying tools:

  * **Trail of Bits:** For Slither, Echidna, and Manticore.
  * **ConsenSys:** For Mythril and Surya.
  * **a16z Crypto:** For Halmos.
  * **naddison36:** For Sol2UML.
  * **devstein:** For Solgraph.

-----

## Author

**Harsh (CyberVenom)** *Smart Contract Security Engineer | Product Security | Web3 Security Enthusiast*

  * **GitHub:** [@HARSH-21](https://www.google.com/search?q=https://github.com/HARSH-21)
  * **Twitter/X:** [@H4r5h_T4nd37](https://twitter.com/H4r5h_T4nd37)
  * **LinkedIn:** [Harsh Tandel](https://www.google.com/search?q=https://linkedin.com/in/harsh-tandel-939785193)

-----

*Contributions are welcome. Please feel free to fork the repository, create a feature branch, and submit a pull request.*
