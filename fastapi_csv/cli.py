"""
Simple command line interface that starts an API by calling `fastapi-csv`.
"""

import typer
import uvicorn

from .applications import FastAPI_CSV


typer_app = typer.Typer()


@typer_app.command()
def main(
    csv_path: str = typer.Argument(..., help="Path to the CSV file"),
    host: str = typer.Option("127.0.0.1", help="IP to run the API on"),
    port: int = typer.Option(8000, help="Port to run the API on"),
):
    """
    🏗️ Create APIs from CSV files within seconds, using fastapi.
    
    Just pass along a CSV file and this command will start a fastapi
    instance with auto-generated endpoints & query parameters to access the data.
    """
    typer.echo(f"🏗️ Creating API from CSV file: {csv_path}")
    app = FastAPI_CSV(csv_path)
    typer.echo("🦄 Starting with uvicorn...")
    typer.echo(
        "💡 Check out the API docs at "
        + typer.style(f"http://{host}:{port}/docs", bold=True)
    )
    typer.echo("-" * 80)
    uvicorn.run(app, host=host, port=port)
