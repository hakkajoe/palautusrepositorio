from urllib import request
from project import Project
import tomlkit


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        toml_data = tomlkit.parse(content)

        poetry_data = toml_data.get("tool").get("poetry")

        name = poetry_data.get("name")
        description = poetry_data.get("description")
        license = poetry_data.get("license")
        authors = poetry_data.get("authors")


        dependencies = []
        dev_dependencies = []

        poetry_dependencies = poetry_data.get("dependencies")
        for dep_name, dep_version in poetry_dependencies.items():
            dependencies.append(f"{dep_name}")

        dev_dependencies_data = poetry_data.get("group").get("dev").get("dependencies")
        for dev_dep_name, dev_dep_version in dev_dependencies_data.items():
            dev_dependencies.append(f"{dev_dep_name}")

        result = f"Name: {name}\nDescription: {description}\nLicense: {license}\n\nAuthors:"
        for author in authors:
            result += f"\n- {author}"

        result += "\n\nDependencies:"
        for dep in dependencies:
            result += f"\n- {dep}"

        result += "\n\nDevelopment dependencies:"
        for dev_dep in dev_dependencies:
            result += f"\n- {dev_dep}"

        return result


        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies)
