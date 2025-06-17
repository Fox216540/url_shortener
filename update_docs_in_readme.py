import yaml

with open('docs.yaml', 'r') as f:
    yml_data = yaml.safe_load(f)

formatted = yaml.dump(yml_data, sort_keys=False)

with open('README.md', 'r') as f:
    readme = f.read()

start_tag = '<!-- DOCS_START -->'
end_tag = '<!-- DOCS_END -->'

before = readme.split(start_tag)[0]
after = readme.split(end_tag)[1]

new_readme = f"{before}{start_tag}\n```yaml\n{formatted}```\n{end_tag}{after}"

with open('README.md', 'w') as f:
    f.write(new_readme)
