import click
import subprocess
from pytestreport.reporter import generate_report_pytest


@click.group()
def cli():
    """Command-line interface for generating test reports."""
    pass


@click.command()
@click.argument("output_format")
def new(output_format: str, module_path: str = None):
    """_summary_

    Args:
        output_format (_type_): _description_
    """
    command = f"""pytest --cov={module_path} --cov-report={output_format}:covarge_report.{output_format}"""
    
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    
    if result.returncode == 0:
        generate_report_pytest(prefix=module_path, output_file=f"report.{output_format}")
        click.echo("Test report generated successfully!")
    else:
        click.echo("Failed to generate test report.")
    

cli.add_command(new)

if __name__ ==  "__main__":
    cli()