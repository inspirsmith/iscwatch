import typer

from iscwatch.scrape import iter_advisories

app = typer.Typer()

@app.command()
def show():
    """Show all Intel Security Center Advisories"""
    for one_advisory in iter_advisories():
        print(one_advisory)

@app.command()
def hello():
    print("Hello, world.")
# @app.command()
# def catalog(dir: Union[str, None] = None):
#     """Create a catalog of security advisories from Intel home page."""
#     pattern = r"intel-sa-([0-9]{5}).html"
#     if result := requests.get(ADVISORY_HOME_PAGE):
#         advisory_ids = re.findall(pattern, result.text)
#         for one_id in advisory_ids:
#             advisory_url = f"{ADVISORY_ID_PAGE}{one_id}.html"
#             if result := requests.get(advisory_url):
#                 with open(f"{one_id}.html", "wb") as file:
#                     rich.print(f"writing: {one_id}.html")
#                     file.write(result.content)
#                 time.sleep(5)


# @app.command()
# def check(
#     update: Annotated[
#         bool, typer.Option(help="Update database with results of check.")
#     ] = False
# ):
#     """
#     Check security center homepage for new advisories.
#     """
#     res = requests.get(ADVISORY_HOME_PAGE)
#     soup = bs4.BeautifulSoup(res.text)

#     advisory_table = soup.find("table")
#     if type(advisory_table) is bs4.element.Tag:
#         advisories = []
#         for tr in advisory_table.find_all("tr", class_="data"):
#             tr_data = []
#             for td in tr.find_all("td"):
#                 if td.text:
#                     tr_data.append(td.text)
#                 if a := td.find("a"):
#                     tr_data.append(a["href"])
#             if len(tr_data) == 5:
#                 advisories.append(Advisory(*tr_data))

#             tr_data = []


# @app.command()
# def count():
#     print("count")


if __name__ == "__main__":
    app()
