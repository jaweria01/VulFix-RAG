from detector.detector import scan_file
from rag.retriever import retrieve_knowledge
from llm.llm_client import generate_patch
from llm.prompts import SECURITY_PATCH_PROMPT
from validator.patch_validator import validate_patch

def main():

    vulnerabilities = scan_file(
        "detector/sample_vulnerable.py"
    )

    if not vulnerabilities:
        print("No vulnerabilities found.")
        return

    for vulnerability in vulnerabilities:
        knowledge = retrieve_knowledge(
            vulnerability["vulnerability"]
            )




        prompt = SECURITY_PATCH_PROMPT.format(
            vulnerability=vulnerability["vulnerability"],
            knowledge=knowledge,
            code=vulnerability["code"]
        )

        patch = generate_patch(prompt)
        patch = patch.replace("```python", "")
        patch = patch.replace("```", "")
        patch = patch.strip()

        print("\n" + "=" * 50)
        print("VULNERABILITY")
        print("=" * 50)

        print(vulnerability)

        print("\n" + "=" * 50)
        print("GENERATED PATCH")
        print("=" * 50)

        print(patch)
        # validate the patch
        validation_result = validate_patch(
            vulnerability["vulnerability"],
            patch
        )

        print("\n" + "=" * 50)
        print("VALIDATION RESULT")
        print("=" * 50)

        print(validation_result)


if __name__ == "__main__":
    main()