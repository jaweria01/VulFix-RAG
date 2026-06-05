import ast
import json


class VulnerabilityDetector(ast.NodeVisitor):

    def __init__(self):
        self.vulnerabilities = []
# Detect dangerous function calls
    def visit_Call(self, node):

        # Detect os.system()

        if (
            isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "os"
            and node.func.attr == "system"
        ):
            self.vulnerabilities.append({
                "vulnerability": "Command Injection",
                "cwe": "CWE-78",
                "severity": "Critical",
                "line": node.lineno
            })
        self.generic_visit(node)
           
 # Detect hardcoded credentials
    def visit_Assign(self, node):

        secret_keywords = [
            "password",
            "passwd",
            "secret",
            "token",
            "api_key",
            "apikey",
            "key"
        ]

        for target in node.targets:

            if isinstance(target, ast.Name):

                variable_name = target.id.lower()

                if variable_name in secret_keywords:

                    if isinstance(node.value, ast.Constant):

                        if isinstance(node.value.value, str):

                            self.vulnerabilities.append({
                                "vulnerability": "Hardcoded Credential",
                                "cwe": "CWE-798",
                                "severity": "High",
                                "line": node.lineno
                            })
        self.generic_visit(node)

    def visit_BinOp(self, node):

        if isinstance(node.op, ast.Add):

            if (
                isinstance(node.left, ast.Constant)
                and isinstance(node.left.value, str)
            ):

                sql_keywords = [
                    "select",
                    "insert",
                    "update",
                    "delete"
                ]

                left_string = node.left.value.lower()

                if any(
                    keyword in left_string
                    for keyword in sql_keywords
                ):

                    self.vulnerabilities.append({
                        "vulnerability": "SQL Injection",
                        "cwe": "CWE-89",
                        "severity": "High",
                        "line": node.lineno
                    })

      

        self.generic_visit(node)


def scan_file(filepath):

    with open(filepath, "r", encoding="utf-8") as f:
        source_code = f.read()

    lines = source_code.splitlines()

    tree = ast.parse(source_code)

    detector = VulnerabilityDetector()

    detector.visit(tree)

    for vuln in detector.vulnerabilities:

        vuln["code"] = lines[vuln["line"] - 1]

    return detector.vulnerabilities


if __name__ == "__main__":

    results = scan_file("sample_vulnerable.py")

    print(
        json.dumps(
            results,
            indent=4
        )
    )