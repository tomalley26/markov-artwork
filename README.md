# markov-artwork

## Title: Stephanie Shih’s Ceramics as Markovian Collage, or, “Hmart Haul”

For this system, I was inspired by the upcoming Bowdoin College Museum of Art exhibition Without Apology: Asian American Selves, Memories, Futures. While looking into the artists featured in this exhibition, I came across the work of Taiwanese-American artist Stephanie Shih. Shih creates ceramic sculptures of popular ‘Asian-American’ grocery items that LA art gallery Sebastian Gladstone describes as “products that will hardly feel foreign to a Western viewer, and yet one that East and Southeast Asian viewers will recognize as uniquely their own.” As a biracial (Chinese/white) Asian American, I was struck with the nostalgia and familiarity I felt while exploring her work. Commonplace grocery store items such as chili-garlic sauce, bok choy, and Kikkoman soy sauce have stocked my family’s pantry for years, recalled in my earliest memories and eventually woven into the fabric of my childhood throughout countless family meals. The trompe l’oeil of Shih’s sculptures sparked a flashback to my constructions of Asian American nostalgia, evoking tastes, smells, and memories of watching my family cook in our kitchen or bring me along on monthly pilgrimages to the local Asian grocery stores. Speaking on how the Asian-American diaspora cannot feel totally at home in either Asian countries or the United States due to language barriers and cultural differences, Shih remarks that “there isn’t a place where we can go and feel like, there is where I belong. I like to think of Asian-America as more of an emotional place that exists in our conversations and in our shared memories. To me, that is why nostalgia and memory are so hard to separate from community.” In my Markovian collages, I attempt to construct these emotional-imaginative spaces where Asian American memories of nostalgic items collide and overlap, sometimes in a whimsical or illogical order due to the Markov matrix probabilities. The vertical length of the collages is reminiscent of Chinese hanging scroll artwork, and my choice to include eight ‘tiles’ is a nod to the luck that the number eight connotes in Chinese culture. Combining these traditional inspirations with the modern medium of computer generated art situates my work outside of any particular era and encourages the viewer to experience it through the lens of their own spectrum of familiarity or nostalgia. 

The pseudo “randomness” of the Markovian system reflects how seemingly unrelated events have contributed to facets of Asian-American culture. Sebastian Gladstone states: “​the cultural significance of some groceries—like Libby’s Vienna Sausages for Filipino meatloaf, Spam for Korean army stew, and Heinz ketchup for Japanese spaghetti—is rooted in histories of colonization and U.S. military presence in Asia.” For me, relating ketchup to spaghetti seems like a random Markovian transition, yet its significance spans decades of modern history. As Asian America is inherently multicultural, the diaspora has established its culture through a linking of many nations, identities, and customs. 

Having recently returned from three months of living in Taiwan, and being a Computer Science & Asian Studies double major, I’m excited to create a project that combines these two interests for the first time.

Working on this project challenged me to reframe the purpose of computer science in my mind. In previous classes or internships, coding has been an efficient way to complete an assignment or create a tool. Interrogating my own assumption that computer science is always used for practical purposes was the first challenge I encountered. While starting this class, I began to consider the usefulness of using computer science for art, music, or just for fun. My comfort zone in computer science usually does not involve creating anything visually appealing or interesting. The furthest I’ve gone is in my experience with UI design during an internship, but creating artwork is a totally new goal. Thinking about how to find and use new tools for creating artwork was another challenge I encountered. I wanted to go beyond the classic medium of drawing or painting, and researched different methods of collaging instead. Additionally, I was challenged by the new concept of Markov chains and how I could implement them for my artwork in a meaningful way. Becoming more comfortable with this new concept and understanding at least one way of implementing it in code was another notable challenge. For my next steps, I hope to learn about different ways that computers can generate information or art besides Markov chains, and delve further into the role of AI in creating artwork as well.

I believe that my system is not completely creative, but has certain aspects of approaching creativity. The main creativity of the program lies in the transition matrix, which is pre-defined but still able to produce different or seemingly random results. In terms of my own involvement in the system, I think this project is highly P-Creative, since combining art and computer science, or even combining my majors of Computer Science and Asian Studies, is something new for me. I also think it has elements of combinatorial creativity due to my use of another artist’s pre-existing work and combining it with the artistic method of collage. The reaction that my system generates through the art it produces is somewhat exploratory for me, since I am attempting to create not just a visual work but also an emotional-imaginative space for the viewer. The nostalgia (or lack thereof) of the viewer is an integral part of my artwork. Overall, I believe the system I programmed is not entirely creative, but the ways in which it interacts with my artistic process and the experience of the viewer has certain elements of creativity.

## Documentation and Setup:

- [ ] Install dependencies
This program relies on Pillow (PIL) for image handling, numpy for implementing the Markov chain, and random for generating random numbers. Check the import statements on lines 1-3 in test.py to see if the dependencies have been installed correctly.

    Pillow installation:
    https://pillow.readthedocs.io/en/stable/installation.html

    numpy installation:
    https://numpy.org/install/

    random: If you don’t already have the python random module installed, I installed the vscode-random extension.

- [ ] Clone repository locally from GitHub:
    https://github.com/tomalley26/markov-artwork

- [ ] In test.py (path: markov-artwork/test.py), navigate to line 56:
`img = Image.open("/Users/tomalley/markov-artwork/assets/" + motif + ".png")`
and change `/Users/tomalley/markov-artwork/images/` to `Users/<Your username here>/markov-artwork/images/`, or change the path name to whatever location you have cloned the repository to. This change will allow the program to access the assets folder, containing the necessary images for creating the collage.

- [ ] Run test.py to display the collage. The output should be similar to: 
 `Here's the combination: ['rice', 'cake', 'salmon', 'fishhead', 'lindt']
3`
Where the combination array contains the names of the motifs in the collage, and the following number (0, 1, 2, or 3) is the value of the “coin” variable. The collage will output in a new window on your desktop.
