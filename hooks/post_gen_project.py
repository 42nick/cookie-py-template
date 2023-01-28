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

        # create directoriy and folders
        vsc_path.mkdir(parents=True, exist_ok=True)
        vsc_setting_path.touch(exist_ok=True)
        vsc_extension_path.touch(exist_ok=True)

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
                        "recommendations": [
                            "ms-python.python",
                            "ms-python.vscode-pylance",
                            "KevinRose.vsc-python-indent",
                            "njpwerner.autodocstring"
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
