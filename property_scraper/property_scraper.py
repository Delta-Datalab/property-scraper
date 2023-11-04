from src.extract import Extract
import click

@click.command()
@click.argument('url')
def main(url):
    extract = Extract()
    extract.download_data(url)

if __name__ == '__main__':
    main()