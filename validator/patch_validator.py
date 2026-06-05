def validate_patch(
    vulnerability_type,
    patched_code
):

    result = {
        "valid": False,
        "reason": ""
    }

    if vulnerability_type == "SQL Injection":

        if "+" not in patched_code:

            result["valid"] = True
            result["reason"] = (
                "No string concatenation detected."
            )

    elif vulnerability_type == "Command Injection":

        if (
            "os.system" not in patched_code
            and "shell=True" not in patched_code
        ):

            result["valid"] = True
            result["reason"] = (
                "Dangerous command execution removed."
            )

    elif vulnerability_type == "Hardcoded Credential":

        if "os.getenv" in patched_code:

            result["valid"] = True
            result["reason"] = (
                "Credential moved to environment variable."
            )

    return result

if __name__ == "__main__":

    patch = '''
API_KEY = os.getenv("API_KEY")
'''

    print(
        validate_patch(
            "Hardcoded Credential",
            patch
        )
    )