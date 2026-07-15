import re

VARIABLE_PATTERN = re.compile(
    r"\{([a-zA-Z_][a-zA-Z0-9_]*)\}"
)

def replace_variables(text, variables):
    def replace(match):
        key = match.group(1)
        return str(
            variables.get(
                key,
                match.group(0)
            )
        )
    return VARIABLE_PATTERN.sub(
        replace,
        text
    )

def create_structure(base, structure, variables):
    for name, content in structure.items():
        name = replace_variables(
            name,
            variables
        )

        path = base / name

        if isinstance(content, dict):
            path.mkdir(
                parents=True,
                exist_ok=True
            )

            create_structure(
                path,
                content,
                variables
            )
        else:
            content = replace_variables(
                content,
                variables
            )
            path.write_text(
                content,
                encoding="utf-8"
            )