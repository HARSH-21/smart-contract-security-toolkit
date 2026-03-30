#!/usr/bin/env python3

import sys
import subprocess
import os

# -----------------------------
# Helper function to run command
# -----------------------------
def run_command(cmd, name):
    print(f"[+] Running {name}...")
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        return output.decode()
    except subprocess.CalledProcessError as e:
        print(f"[!] {name} failed")
        return e.output.decode()


# -----------------------------
# Exploit Detection (custom logic)
# -----------------------------
def detect_exploits(code):
    findings = []

    if "call{value:" in code and "balances[msg.sender] = 0" in code:
        findings.append({
            "type": "Reentrancy",
            "severity": "Critical",
            "description": "External call before state update"
        })

    if "tx.origin" in code:
        findings.append({
            "type": "Phishing Risk",
            "severity": "High",
            "description": "Use of tx.origin for authentication"
        })

    if ".call(" in code and "require(" not in code:
        findings.append({
            "type": "Unchecked Call",
            "severity": "High",
            "description": "External call without checking return value"
        })

    return findings


# -----------------------------
# Main Scanner
# -----------------------------
def main(contract_path):

    if not os.path.exists(contract_path):
        print("❌ Contract file not found")
        return

    print(f"\n🚀 Scanning Contract: {contract_path}\n")

    # Read contract
    with open(contract_path, "r") as f:
        code = f.read()

    results = []

    # -----------------------------
    # Run Tools
    # -----------------------------
    results.append(run_command(["slither", contract_path], "Slither"))
    results.append(run_command(["myth", "analyze", contract_path], "Mythril"))
    results.append(run_command(["manticore", contract_path], "Manticore"))

    # -----------------------------
    # Custom Exploit Detection
    # -----------------------------
    exploit_findings = detect_exploits(code)

    # -----------------------------
    # Generate Report
    # -----------------------------
    os.makedirs("output", exist_ok=True)

    report_file = "output/report.md"

    with open(report_file, "w") as f:
        f.write("# Smart Contract Audit Report\n\n")
        f.write(f"Contract: {contract_path}\n\n")

        f.write("## 🔍 Tool Outputs\n\n")
        for r in results:
            f.write("```\n")
            f.write(r[:1000])  # limit output
            f.write("\n```\n\n")

        f.write("## 🚨 Custom Exploit Detection\n\n")

        if not exploit_findings:
            f.write("✅ No major issues detected\n")
        else:
            for issue in exploit_findings:
                f.write(f"### {issue['severity']} - {issue['type']}\n")
                f.write(f"{issue['description']}\n\n")

    print(f"\n✅ Report generated: {report_file}")


# -----------------------------
# Entry Point
# -----------------------------
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 smart_contract_audit_toolkit.py <contract.sol>")
    else:
        main(sys.argv[1])
