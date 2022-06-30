import click
import dbf
from pathlib import Path
from sqlite_utils import Database


@click.command()
@click.version_option()
@click.argument("dbf_paths", type=click.Path(exists=True), nargs=-1, required=True)
@click.argument("sqlite_db", nargs=1)
@click.option("--table", help="Table name to use (only valid for single files)")
@click.option("-v", "--verbose", help="Show what's going on", is_flag=True)
def cli(dbf_paths, sqlite_db, table, verbose):
    """
    Convert DBF files (dBase, FoxPro etc) to SQLite

    https://github.com/simonw/dbf-to-sqlite
    """
    if table and len(dbf_paths) > 1:
        raise click.ClickException("--table only works with a single DBF file")
    db = Database(sqlite_db)
    for path in dbf_paths:
        table_name = table if table else Path(path).stem
        if verbose:
            click.echo('Loading {} into table "{}"'.format(path, table_name))
        dbf_table = dbf.Table(str(path))
        dbf_table.open()
        columns = dbf_table.field_names
        db[table_name].insert_all(dict(zip(columns, list(row))) for row in dbf_table)
        dbf_table.close()
    db.vacuum()
