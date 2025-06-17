import yaml

with open("docs.yaml", "r") as f:
    spec = yaml.safe_load(f)

info = spec.get("info", {})
paths = spec.get("paths", {})

md = f"# 📘 API Documentation\n\n"
md += f"**Title:** {info.get('title', 'N/A')}\n\n"
md += f"**Version:** {info.get('version', 'N/A')}\n\n"
md += f"**Description:** {info.get('description', '')}\n\n"
md += f"---\n\n"

for path, methods in paths.items():
    for method, details in methods.items():
        summary = details.get("summary", "")
        description = details.get("description", "")
        parameters = details.get("parameters", [])
        request_body = details.get("requestBody", {})
        responses = details.get("responses", {})

        md += f"## `{method.upper()} {path}`\n\n"
        md += f"**Summary:** {summary}\n\n"
        if description:
            md += f"**Description:** {description}\n\n"

        # Параметры
        if parameters:
            md += "**Parameters:**\n\n"
            md += "| Name | In | Type | Required | Description |\n"
            md += "|------|----|------|----------|-------------|\n"
            for p in parameters:
                name = p.get("name", "")
                location = p.get("in", "")
                ptype = p.get("schema", {}).get("type", "")
                required = p.get("required", False)
                desc = p.get("description", "")
                md += f"| {name} | {location} | {ptype} | {required} | {desc} |\n"
            md += "\n"

        # Request body
        if request_body:
            md += "**Request Body:**\n\n"
            content = request_body.get("content", {})
            for mime, c in content.items():
                example = c.get("example") or (c.get("examples") or {}).get("default", {}).get("value")
                md += f"Content-Type: `{mime}`\n\n"
                if example:
                    md += "```json\n" + yaml.dump(example, sort_keys=False) + "```\n\n"

        # Responses
        if responses:
            md += "**Responses:**\n\n"
            for code, resp in responses.items():
                desc = resp.get("description", "")
                md += f"- **{code}**: {desc}\n"
                content = resp.get("content", {})
                for mime, c in content.items():
                    example = c.get("example") or (c.get("examples") or {}).get("default", {}).get("value")
                    if example:
                        md += f"\nContent-Type: `{mime}`\n\n"
                        md += "```json\n" + yaml.dump(example, sort_keys=False) + "```\n\n"

        md += "---\n\n"

# Обновление README
with open("README.md", "r") as f:
    content = f.read()

start_tag = "<!-- DOCS_START -->"
end_tag = "<!-- DOCS_END -->"

before = content.split(start_tag)[0]
after = content.split(end_tag)[1]

new_readme = f"{before}{start_tag}\n{md}\n{end_tag}{after}"

with open("README.md", "w") as f:
    f.write(new_readme)
