from helpers import retrieve_transcript_podcast


def test_function(episode_1_file):
    expected = [
        "0:01  ",
        "When I was a kid, apples were garbage. They were called Red Delicious and "
        "they were red. They were not delicious. They looked beautiful, but then you "
        "bite into it, and almost always it would be mushy and mealy, just nasty.",
        "",
        "0:15  ",
        "It was a really bad time to be an apple eater. It was also a really bad time " "to be an apple grower.",
        "",
        "0:21  ",
        "Everybody really just about literally everybody was growing Red Delicious.",
        "",
        "0:24",
        "This is Dennis courtier. He's the owner of Pepin heights orchard in Lake " "City, Minnesota.",
        "",
        "0:30",
        "We were going broke. You know, we were being asked to deliver goods for " "below the cost of production.",
        "",
        "0:36",
        "If courtier tried to raise his prices. Some other farmer who was growing the "
        "exact same Red Delicious apples would say to buyers, Hey, I'll sell them to "
        "you for less because Red Delicious apples were this ubiquitous, "
        "interchangeable thing they were commodity and making commodities. Whether "
        "it's cheap socks or metal screws or Red Delicious apples is a terrible "
        "business to be in. Hello and welcome to Planet money. I'm Jacob Goldstein.",
        "",
        "1:00",
        "I'm Dan Charles. I cover food and farming for NPR. Today on the show how we "
        "got from merely nasty apples to apples, you actually want to eat apples that "
        "tastes delicious. Yeah,",
        "",
        "1:10",
        "there was a guy who discovered a delicious miracle Apple, but discovering " "that Apple was not enough.",
        "",
        "1:19",
        "Support for planet money. And this message comes from Dropbox maker of "
        "Dropbox for Business. The average person uses two devices to share at work "
        "to collaborate regularly. Dropbox for Business gives you access to your "
        "team's files wherever you work, computer, phone, laptop, or from any web "
        "browser, so that you can stay productive on the go wherever you are. Plus, "
        "you get all the space your team needs. And unlimited deletion, recovery and "
        "version history. Learn more@dropbox.com slash NPR.",
        "",
        "1:51",
        "The guy who discovered the miracle Apple, that one apple, his name is David "
        "Bedford. And when he was growing up, he loved fruit, but he hated apples "
        "because all he ever knew were Red Delicious. But then he went off to college "
        "and one day for the first time in his life. He tasted a really good apple.",
        "",
        "2:07",
        "Someone brought a bushel of yellow apples down from Michigan and they were "
        "fresh and they weren't mealy. They didn't have a tough, Naugahyde like skin. "
        "They were crisp and juicy, and I was amazed.",
        "",
        "2:20",
        "So David Bedford thinks to himself, why not make more amazing apples? Why "
        "not have amazing apples in the grocery store? He becomes an apple breeder. "
        "he devotes his professional life to creating those delicious apples. But",
        "",
        "2:34",
        "this is a tough thing to devote your life to inventing a better Apple is "
        "really hard. For one thing, you want a new Apple, it's gonna take a long "
        "time. You know, you find a couple promising apples, you crossbreed them, you "
        "collect the offspring, you get the seeds, you put them in the ground, and "
        "then you gotta wait. You gotta wait for an apple tree to grow up out of the "
        "ground. It takes five years or more. Finally the tree grows up, starts "
        "producing apples, you pick one, you taste it, and it sucks. That's actually",
        "",
        "3:02",
        "what happens 99.99% of the time. I went to visit David Bedford At his trial "
        "orchard at the University of Minnesota and he walked me out to the orchard. "
        "And I see rows and rows of little apple trees up the hillsides and down the "
        "hillsides. He'd like them all to be great, but he knows that they won't be",
        "",
        "3:21",
        "if you look around you here, what we see around us here is probably five to "
        "6000 trees. That's not even enough really to have one that will be a winner.",
        "",
        "3:33",
        "You're a you're a you're a tough Judge of apple trees.",
        "",
        "3:36",
        "Wow. You know, we've got a lot of responsibility here. We're trying to save "
        "the world from media grapples, and we can't let our guard down.",
        "",
        "3:44",
        "And there's only one way that David Bedford can tell whether a tree is "
        "great, mediocre worth keeping. He doesn't have a chemical test. He can't "
        "tell just by looking at them. He has to walk the rose tree by tree, taking "
        "an apple from each one and tasting. How many apples Do you bite into in a "
        "day when you're going through like",
        "",
        "4:03",
        "an average day at the peak of the season, you'd probably be five to 600 "
        "apples. Sooner or later, somebody has to eat it. That's the ultimate "
        "determination is the mouth and the and the tongue in the brain. And so you "
        "have to take a bite and you have to decide there is a",
        "",
        "4:21",
        "trick to tasting 500 apples a day. Bedford bites into the apple chews for a "
        "few seconds and this is the trick doesn't swallow it.",
        "",
        "4:31",
        "No great effort expended. They just opened the mouth and many jack the ball "
        "was dropping on the ground dropping underground. Yeah,",
        "",
        "4:37",
        "he didn't even spit it out. He just kind of lets it fall out like like a two "
        "year old who suddenly decides Hey, I don't want to eat this thing that's in "
        "my mouth.",
        "",
        "4:45",
        "This trick this technique. This is how he found the miracle apple. It was "
        "years ago back in the early 1980s. David Bedford is walking down the trees "
        "one by one bite, spit, bite, spit and he comes to the One Tree tree number "
        "1711. He picks an apple, he takes a bite.",
        "",
        "5:05",
        "There was this moment of confusion maybe oh my goodness, what is this? This "
        "is not a Red Delicious texture. This is not even a good Apple texture. This "
        "is something beyond the two things that came to my mind number one was "
        "watermelon, the way the watermelon will kind of break in your mouth, and "
        "then did you squeeze out of it. And the other thing was Asian pears, that "
        "real Christmas of an Asian pear. But I'd sorted that out enough to say, I "
        "don't know what this is, but it's good. You know, I like it. It was sweet.",
        "",
        "5:39",
        "It was crisp. So they called it honey crisp, and honey crisp would "
        "eventually change the apple business. But it took a long time for that to "
        "happen.",
        "",
        "5:47",
        "Because think about this moment. David Bedford has a new Apple in his hand, "
        "something different, maybe better than all the apples in the store. He tells "
        "Apple growers about this new discovery, the apple that's so much better than "
        "the mealy Red Delicious that everyone's eating. He says, I got it. I got it. "
        "Try this.",
        "",
        "6:03",
        "And the growers. They don't want they would Bedford's amazing new Apple. "
        "They don't want it because the grocery stores don't want it. Back then the "
        "produce section was still pretty boring. You know, you went in you want to "
        "let us there's iceberg. That's it. You want kale, there's no kale. You want "
        "apples? Yeah, they got apples.",
        "",
        "6:21",
        "I remember a produce market are telling me when I first got into the "
        "business, he said Why are you guys trying to make more apples? We don't need "
        "that. He said we have a red one. We have a yellow one. And we have a green "
        "one. That's all we need.",
        "",
        "6:35",
        "This is a classic problem for an inventor. You come up with something new, "
        "something incredible. But nobody really wants it. Nobody even knows about "
        "it. Bedford probably needed a marketing team a big advertising push. He "
        "didn't have any of that all he had was this one guy.",
        "",
        "6:50",
        "That guy was Dennis courtier. courtier is the apple grower from the "
        "beginning of the show was getting killed trying to grow Red Delicious. "
        "Cartier used to come by Bedford's orchard every so often he'd say, Hey, you "
        "know you have anything good. You have anything different. One time courtier "
        "came by and Bedford took him to tree 1711 Bedford took him to that "
        "honeycrisp tree and said here, try one of these courts here took a bite and "
        "thought these could be the apples I've been waiting for.",
        "",
        "7:16",
        "They were that damn good. And that damn difference.",
        "",
        "7:20",
        "courtier makes a big bet. He starts planning lots of honeycrisp trees. He "
        "doesn't know if it's gonna work, doesn't know if people are gonna want these "
        "apples. But if they do, he could finally start making a decent profit "
        "because instead of growing the same apples as everybody else, he'll be the "
        "only guy growing honeycrisp at least for a while. He has a head start on "
        "every other Apple grower.",
        "",
        "7:39",
        "Of course, this being the apple business, he's going to have to wait a long "
        "time to figure out whether his bet will pay off.",
        "",
        "7:45",
        "Yeah, he plants the trees. He waits for him to grow up they get bigger. And "
        "finally, by the time the trees are starting to produce apples, the "
        "supermarket's are ready for they have gone",
        "",
        "7:55",
        "beyond Red Delicious. Finally, there are other apples that are starting to " "show up on the shelves. And",
        "",
        "8:00",
        "when the honeycrisp finally get to the store, they do great",
        "",
        "8:04",
        "we had retailers telling us that it is still true that honey crisp had "
        "elevated apples to a different level within their grocery stores. The point "
        "that honey crisp is in many cases, the top dollar grossing matches to Apple.",
        "",
        "8:20",
        "They were the top grossing item in the whole store. You know,",
        "",
        "8:24",
        "not every week, not every store, not every part of the season. But when the "
        "air is at their peak, we have retailers who sell more dollars worth of our "
        "honeycrisp every week than they sell two liter bottles of Coca Cola. That "
        "changes things.",
        "",
        "8:38",
        "grocery stores are dying to get quartiers product, he's finally selling his "
        "apples at a profit. He's doing great making money. But before long, he sees "
        "other people planting honeycrisp trees. And he knows that pretty soon, there "
        "will be tons of farmers competing against him to sell honey crisp, he'll be "
        "back in that Red Delicious world where he can't make a profit. honey crisp "
        "will just be this delicious commodity courtier realized. And this was really "
        "the final step in this story that he needed to do more than find a delicious "
        "apple. He needed to figure out a way to keep that delicious apple to himself "
        "and maybe just a few selected other farmers.",
        "",
        "9:15",
        "I remember the specific discussions in which a number of us it's like, well, "
        "what if, what if, what if? What if we did this? What if we did that?",
        "",
        "9:25",
        "What if when we find the next great Apple, a small group of us could control "
        "the supply of it. Make sure we grow enough to keep the supermarket's happy, "
        "not too many. So the price doesn't crash make sure the apples handled well. "
        "So that still good so shoppers still want to buy it.",
        "",
        "9:41",
        "And you might be able to do this with a patent right you can patent an "
        "apple. In fact, Bedford and the University of Minnesota had patented the "
        "honeycrisp but they let anybody who wanted to plant it farmers just had to "
        "pay a small royalty. And anyway, more importantly, a patent lasts for 20 "
        "years which in a business where it takes five years. More just to grow a "
        "tree is not that long. By the time honey crisp was really taken off its "
        "patent was expiring",
        "",
        "10:06",
        "then courtier and his friends looked around and they saw something "
        "interesting. A clever Australian company had gone beyond patents. They had "
        "gotten a trademark on the name Pink Lady for their apples. That's Pink Lady "
        "with a little tm for trademark. Unlike a patent, a trademark never expires, "
        "you give an apple a name, you trademark that name. And then you get to "
        "decide forever who gets to grow and who gets to sell apples under that name.",
        "",
        "10:32",
        "cartoonist friends wanted to do that, but they needed a new Apple. About 10 "
        "years ago, they found it they found it at that same orchard run by David "
        "Bedford at the University of Minnesota and courtier. This time, he talked to "
        "Bedford and the university into trademarking that Apple. They call it sweet "
        "Tango. This is one T, SW E, ta, N, g. o. Tm, only 45 farmers are allowed to "
        "grow it.",
        "",
        "10:58",
        "We have just shy of a million trees in the ground, and it's going quite "
        "well. It's a great apple. We grow more and sell more of them every year. And "
        "you know, we're trying to figure out how quickly we can ramp it up.",
        "",
        "11:11",
        "If you're an apple grower and you are not part of the sweet Tango growing "
        "club, well go find another club there are a lot of so called club apples now "
        "being grown arriving in the grocery stores and",
        "",
        "11:22",
        "each one has a name more ridiculous than the last. Let's do a few of",
        "",
        "11:27",
        "them. Envy Cosmic Crisp jazz Kanzi, Lady Alice,",
        "",
        "11:31",
        "opal Pacific rose pin yada Ruby frost snap dragon. Yeah, exactly, exactly.",
        "",
        "11:39",
        "And that is not even the end of",
        "",
        "11:40",
        "the list. One little detail. It's only the name that's trademarked. So even "
        "if you're not in the club, you can grow the apple, you just can't use the "
        "name. Pro tip. If you see Pink Lady and Crips pink in the same store, just "
        "buy whichever one's cheaper because they're the same apple. All these apples "
        "with their ridiculous names are brands. Each Apple is a brand and you could "
        "imagine a future where saying, Hey, can you pick me up some apples? Sounds "
        "as ridiculous as saying, Hey, can you pick me up a six pack of cola. You "
        "don't say cola. You say Coke or Pepsi? The brand is the thing.",
        "",
        "12:16",
        "Tim burns used to run the promotional campaign for the sweet Tango apple. "
        "And he says apples now will be like every other item in the grocery store. "
        "They will have their own brands, they will have their own marketing teams, "
        "their own advertising blitzes, it is going to be a world of managed brands "
        "just like the soup aisle or the potato chip aisle, or any other aisle. This "
        "is what it's going to be going forward.",
        "",
        "12:40",
        "There's something a little sad about this. Even apples, you know, this basic "
        "natural thing are now in the world of brands and advertising and marketing.",
        "",
        "12:51",
        "But all that is driving people to create and sell really good apples. So if "
        "you really like apples, and you're willing to pay for a really great "
        "delicious new Apple, you can now find them. And you know what? If you don't "
        "want to pay more, you can still get rid delicious.",
        "",
        "13:10",
        "You can always email us at Planet money@npr.org. You can tweet at us at "
        "planet money. You can tweet at me at Jacob Goldstein in Charles",
        "",
        "13:18",
        "Are you on Twitter? I am at NPR Dan Charles. Our story today",
        "",
        "13:21",
        "was produced by Jess Jang and Neda Wilson. And finally, if you're looking "
        "for another great podcast, check out snap judgment with Glenn Washington. "
        "It's an hour long show of real stories about real people. You can find it on "
        "the NPR one. I'm Jacob Goldstein.",
        "",
        "13:37",
        "And I'm Dan Charles. Thanks for listening.",
        "",
        "Transcribed by https://otter.ai",
        "",
    ]

    assert retrieve_transcript_podcast(episode_1_file) == expected
