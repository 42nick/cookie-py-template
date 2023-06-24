from pathlib import Path
from textwrap import dedent


def create_vsc_folder():
    print("create_vscode_folder.py")
    create_vsc_folder = "{{cookiecutter.additional_vsc_settings}}" == "y"
    if create_vsc_folder:
        # initialize the paths
        vsc_path = Path(".vscode")
        vsc_setting_path = vsc_path.joinpath("settings.json")
        vsc_extension_path = vsc_path.joinpath("extensions.json")
        vsc_launch_path = vsc_path.joinpath("launch.json")

        # create directoriy and folders
        vsc_path.mkdir(parents=True, exist_ok=True)
        vsc_setting_path.touch(exist_ok=True)
        vsc_extension_path.touch(exist_ok=True)
        vsc_launch_path.touch(exist_ok=True)

        # fill settings.json with default settings
        with open(vsc_setting_path, "w") as f:
            f.write(
                dedent(
                    """\
                    {
                        /* --------------------------------- python --------------------------------- */
                        "python.terminal.activateEnvironment": true,
                        "[python]": {
                            "editor.codeActionsOnSave": {
                                "editor.formatOnSave": true,
                                "source.organizeImports": true
                            },
                        },
                        "python.analysis.completeFunctionParens": true,
                        "python.analysis.autoImportCompletions": true,
                        "python.analysis.autoImportUserSymbols": true,
                        "python.formatting.provider": "black",
                    }                    
                    """
                )
            )

        # fill extensions.json with default extensions
        with open(vsc_extension_path, "w") as f:
            f.write(
                dedent(
                    """\
                    {
                        // Installed extension can be listed with `code --list-extensions`.
                        "recommendations": [
                            "ms-python.python",
                            "ms-python.vscode-pylance",
                            "ms-python.isort",
                            "KevinRose.vsc-python-indent",
                            "njpwerner.autodocstring"
                        ]
                    }                    
                    """
                )
            )

        # fill launch.json to properly debug python code and the tests
        with open(vsc_launch_path, "w") as f:
            f.write(
                dedent(
                    """\
                    {
                        // Use IntelliSense to learn about possible attributes.
                        // Hover to view descriptions of existing attributes.
                        // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
                        "version": "0.2.0",
                        "configurations": [
                            {
                                "name": "Pytest - Debugging",
                                "type": "python",
                                "request": "launch",
                                "program": "${file}",
                                "purpose": [
                                    "debug-test"
                                ],
                                "console": "integratedTerminal",
                                "justMyCode": false,
                                "env": {
                                    "PYTEST_ADDOPTS": "--no-cov"
                                }
                            },
                            {
                                "name": "Python: Current File",
                                "type": "python",
                                "request": "launch",
                                "program": "${file}",
                                "console": "integratedTerminal",
                                "justMyCode": true
                            },
                        ]
                    }               
                    """
                )
            )

def create_sonarcloud_settings():
    if "{{cookiecutter.sonarcloud}}" == "y":
        sonar_cloud_settings_path = Path(".sonarcloud.properties")
        with open(sonar_cloud_settings_path, "w") as f:
            sonarcloud_organization = input("Enter your sonarcloud organization: ")
            
            f.write(
                dedent(
                    f"""\
                    sonar.projectKey={{cookiecutter.project_slug}}
                    sonar.organization={sonarcloud_organization}
                    sonar.python.coverage.reportPaths=reports/coverage.xml
                    """
                )
            )
def main():
    
    create_vsc_folder()
    create_sonarcloud_settings()

if __name__ == "__main__":
    main()
