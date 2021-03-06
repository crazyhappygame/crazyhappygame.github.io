from jinja2 import Template
# >>> template = Template('Hello {{ name }}!')
# >>> template.render(name='John Doe')

template = '''    <div class="col-md-4 col-sm-6 portfolio-item">
                    <div>
                        <img src="img/games/jigsaw_puzzles.png" class="img-responsive" alt="">
                    </div>
                    <div class="portfolio-caption">
                        <a href="http://www.onet.pl">
                            <img src="img/google-play-badge.png" class="img-responsive center-block" alt="">
                        </a>
                        <h4>+</h4>
                        <a href="http://www.onet.pl">
                            <img src="img/ms-badge.png" class="img-responsive center-block" alt="">
                        </a>
                        <h3>Jigsaw Puzzle</h3>
                        <!-- <p class="text-muted">Website Design</p> -->
                    </div>
                </div>'''

template2 = '''   {% for game in games %}
                <div class="col-xs-6 col-sm-4 col-md-3 portfolio-item">
                    <div>
                        <img src="img/games/{{ game["image"] }}" class="img-responsive" alt="">
                    </div>
                    <div class="portfolio-caption">
                        <div class="row">{% for store in game["stores"] %}
                            <div class="col-xs-6 portfolio-item">
                                <a href="{{ store["link"] }}">
                                    <img src="{{ store["badge"] }}" class="img-responsive center-block" alt="">
                                </a>
                            </div>{% endfor %}
                        </div>
                        <h4>{{ game["name"] }}</h4>
                    </div>
                </div>
                {% endfor %}
                '''


def get_stores(stores):
    def get_store(store, col_class):
        return f"""<div class="portfolio-caption">
               <a href = "{store["link"]}" >
                    <img src = "{store["badge"]}" class = "img-responsive center-block" alt = "" >
                </a >
            </div >"""

    if len(stores) == 1:
        return get_store(stores[0], "")
    assert len(stores) == 2
    return "\n".join(get_store(store, "col-xs-6") for store in stores)


def get_template_item(game):
    return f"""
        <div class="col-xs-6 col-sm-4 col-md-3 portfolio-item">
            <a href = "{game["stores"][0]["link"]}" >
                <div class="portfolio-caption">
                    <h4>{game["name"]}</h4>
                </div>
                <div class="portfolio-caption">
                    <img src="img/games/{game["image"]}" class="img-responsive" alt="">
                </div>
                {get_stores(game["stores"])}
            </a>
        </div>"""


def get_template_items(games):
    return "\n".join([get_template_item(game) for game in games])


def googleLink(id):
    return 'https://play.google.com/store/apps/details?id=com.crazyhappygame.{id}&pcampaignid=MKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1'.format(id=id)


def getGoogleStore(id):
    return {
        "badge": "img/google-play-badge.png",
        "link": googleLink(id)
    }


def msLink(id):
    return 'https://www.microsoft.com/store/apps/{id}?ocid=badge'.format(id=id)


def getMsStore(id):
    return {
        "badge": "img/ms-badge.png",
        "link": msLink(id)
    }


games = [
    {
        "name": "DotPoly",
        "image": "dotpoly.png",
        "stores": [getGoogleStore("dotpoly")]
    },
    {
        "name": "DotToDot",
        "image": "dottodot.png",
        "stores": [getGoogleStore("dottodot")]
    },
    {
        "name": "Mahjong",
        "image": "mahjong.png",
        "stores": [getGoogleStore("mahjong")]
    },
    {
        "name": "Planet Draw",
        "image": "planet_draw.png",
        "stores": [getGoogleStore("planetdraw")]
    },

    {
        "name": "Jigsaw Puzzle",
        "image": "jigsaw_puzzle.png",
        "stores": [getGoogleStore("jigsawpuzzle"), getMsStore("9nblggh4tpj1")]
    },
    {
        "name": "Coloring Book",
        "image": "coloring_book.png",
        "stores": [getGoogleStore("coloringpagespuzzleforkids"), getMsStore("9nblggh4m297")]
    },
    {
        "name": "ABC Puzzle",
        "image": "puzzle_animals.png",
        "stores": [getGoogleStore("letterjigsawpuzzlesforkids"), getMsStore("9nblggh4nxmn")]
    },
    {
        "name": "Puzzle/Memo",
        "image": "bee_pack.png",
        "stores": [getGoogleStore("kidspuzzlebeepack"), getMsStore("9nblggh3vrtd")]
    },
    {
        "name": "Christmas Tree",
        "image": "christmas_tree.png",
        "stores": [getGoogleStore("christmastree")]
    },
    # {
    #     "name": "Smart Draw",
    #     "image": "smart_draw.png",
    #     "stores": [getGoogleStore("smartdraw")]
    # },
    {
        "name": "Kids Puzzle Bee",
        "image": "bee.png",
        "stores": [getGoogleStore("kidspuzzlebee")]
    },
    {
        "name": "Cats Puzzle",
        "image": "puzzle_animals2.png",
        "stores": [getGoogleStore("catsandmicejigsawpuzzlesforkids")]
    }
]
t = Template(template2)
# print(t.render(games=games))
print(get_template_items(games))
