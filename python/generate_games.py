from jinja2 import Template
# >>> template = Template('Hello {{ name }}!')
# >>> template.render(name='John Doe')

template='''    <div class="col-md-4 col-sm-6 portfolio-item">
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

template2='''   {% for game in games %}
                <div class="col-md-4 col-sm-6 portfolio-item">
                    <div>
                    	<img src="img/games/{{ game["image"] }}" class="img-responsive" alt="">
                    </div>
                    <div class="portfolio-caption">{% for store in game["stores"] %}
                        <a href="{{ store["link"] }}">
                    		<img src="{{ store["badge"] }}" class="img-responsive center-block" alt="">
                    	</a>{{ "<h4>+</h4>" if not loop.last }}{% endfor %}
                    	<h3>{{ game["name"] }}</h3>
                    </div>
                </div>
                {% endfor %}
                '''


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
	"name": "Jigsaw Puzzle",
	"image": "jigsaw_puzzle.png",
	"stores": [getGoogleStore("jigsawpuzzle"), getMsStore("9nblggh4tpj1")]},
	{
	"name": "Coloring Book",
	"image": "coloring_book.png",
	"stores": [getGoogleStore("coloringpagespuzzleforkids"), getMsStore("9nblggh4m297")]},
	{
	"name": "ABC Puzzle",
	"image": "puzzle_animals.png",
	"stores": [getGoogleStore("letterjigsawpuzzlesforkids"), getMsStore("9nblggh4nxmn")]},
	{
	"name": "Puzzle/Memo/Flower",
	"image": "bee_pack.png",
	"stores": [getGoogleStore("kidspuzzlebeepack"), getMsStore("9nblggh3vrtd")]},
	{
	"name": "Planet Draw",
	"image": "planet_draw.png",
	"stores": [getGoogleStore("planetdraw")]},
	{
	"name": "Christmas Tree",
	"image": "christmas_tree.png",
	"stores": [getGoogleStore("christmastree")]},
	{
	"name": "Smart Draw",
	"image": "smart_draw.png",
	"stores": [getGoogleStore("smartdraw")]},
	{
	"name": "Kids Puzzle Bee",
	"image": "bee.png",
	"stores": [getGoogleStore("kidspuzzlebee")]},
	{
	"name": "Cats Puzzle",
	"image": "puzzle_animals2.png",
	"stores": [getGoogleStore("catsandmicejigsawpuzzlesforkids")]}
]
t = Template(template2)
print(t.render(games=games))

