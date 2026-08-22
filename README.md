![Mateus Alkimim — VFX compositor and pipeline TD, physics undergraduate. Research in the geometry of images.](media/banner.jpg)

# Mateus Alkimim

**Visual Effects Compositor · Pipeline TD · Physics undergraduate** — Montes Claros, Brazil

I measure images. My work lives on the bridge between VFX production and
mathematics: compositing that closes shots, pipeline tools that studios adopt,
and geometry that verifies what the eye believes.

## Start here

- **[relativity-paradox-lab](https://github.com/mateusalkimim/relativity-paradox-lab)** —
  an interactive Special Relativity teaching instrument (Godot 4, gamepad-driven),
  built for live 20-minute sessions with high-school audiences. Based on
  Alencar et al. (2023); grown out of our research group's Twin Paradox work
  presented at the III International Congress on Education and Innovation
  (Unimontes, 2025). GPLv3.
- **[math-prerequisite-map](https://github.com/mateusalkimim/math-prerequisite-map)** —
  an interactive prerequisite map of undergraduate mathematics
  ([live](https://mateusalkimim.github.io/math-prerequisite-map/)): 39 subjects,
  56 dependencies, and **no edge without a warrant** — each arrow declares which
  book it came from, and which class of evidence it rests on. The layout is
  measured, not drawn: crossings cut from 131 to 11, counted in the page's own
  footer. Published as a proposal, in Portuguese. MIT + CC BY.
- **[lol-draft-assistant](https://github.com/mateusalkimim/lol-draft-assistant)** —
  strictly read-only draft & build advisor for League of Legends: local statistics,
  confidence intervals, no raw data redistribution. MIT.
- **[geometry-verifies](https://github.com/mateusalkimim/geometry-verifies)** —
  the geometric-metrology toolkit behind my matte painting pipeline:
  single-view metrology (Criminisi, Reid & Zisserman, 2000) verifying
  AI-assisted paintings against camera ground truth — pre-registered
  measurements, blind judgment, receipts for every claim. MIT + CC BY.

## What I build at work

VFX compositor at **Bóson Post** (previously CONSULADO), working remote from
Montes Claros. Alongside shot work, I build pipeline tooling in production use
(shared here as capability, not code — client work stays under NDA):

- a **Kitsu ↔ Nuke integration suite** for shot setup and versioning;
- a **deterministic compositing mentor** for Nuke — template-driven advice,
  no external APIs, nothing leaves the machine;
- **procedural project-topology builders** for pipeline folder structures.

## Selected credits

Released productions I worked on as a compositor, and the studio each
delivery went through (titles and studios are public credits; shots and
breakdowns stay under NDA) — most recent first:

- **[O Gênio do Crime](https://www.imdb.com/title/tt39444949/)** (2026) —
  feature film (Boutique Filmes/Globo Filmes, from João Carlos Marinho's 1969
  classic), theatrical release; **my first on-screen film credit** — via [Bóson Post](https://www.bosonpost.com.br/) ·
  ![Globoplay](https://img.shields.io/badge/Globoplay-fb0234)
- **[Passinho: O Ritmo dos Sonhos](https://www.imdb.com/title/tt30699615/)** (2025) —
  dance series, Disney+ Brazilian original; my first project with Bóson Post — via [Bóson Post](https://www.bosonpost.com.br/) ·
  ![Disney+](https://img.shields.io/badge/Disney%2B-113CCF)
- **[Amor da Minha Vida](https://www.imdb.com/title/tt27517632/)** (2024–) —
  romantic comedy series, Disney+'s biggest Brazilian series debut of 2024 — via [The End](https://theend.tv/) ·
  ![Disney+](https://img.shields.io/badge/Disney%2B-113CCF)
- **[A Magia de Aruna](https://www.imdb.com/title/tt16225592/)** (2023) —
  fantasy series, Disney+ Brazilian original — via [Miracle VFX](https://miraclevfx.com/) ·
  ![Disney+](https://img.shields.io/badge/Disney%2B-113CCF)
- **[DNA do Crime](https://www.imdb.com/title/tt22459586/)** (2023–) —
  action/heist series, #1 on Netflix in 71 countries in its first season — freelance ·
  ![Netflix](https://img.shields.io/badge/Netflix-E50914?logo=netflix&logoColor=white)

## What I'm making and studying

**Guariba** — an original animated series I'm writing, directing and producing,
set in the Pantanal wetlands. Its production method is where my two crafts
meet: **3D disposes, diffusion paints, projective geometry verifies.** AI is
backstage and reference only — final frames are painted, and that boundary is
declared.

**Physics at Unimontes (2025–2028)** — deliberately, in parallel with
production: projective geometry, linear algebra and optics are the tools I use
daily in compositing, so I'm learning them at the root.

## Six biomes, one surface

Six Möbius strips, each made of the material of a Brazilian biome, each holding
a bird that lives there. The surface is the same in all six; what changes is the
matter, and the matter belongs to the place. Research of my own, unpaid, ongoing.

| | | |
|:--:|:--:|:--:|
| ![Amazônia](media/mobius-amazonia.jpg) | ![Cerrado](media/mobius-cerrado.jpg) | ![Caatinga](media/mobius-caatinga.jpg) |
| **Amazônia** — arumã palm fiber · scarlet macaw | **Cerrado** — golden capim-dourado grass · red-legged seriema | **Caatinga** — vegetable-tanned leather · caatinga parakeet |
| ![Mata Atlântica](media/mobius-mata-atlantica.jpg) | ![Pampa](media/mobius-pampa.jpg) | ![Pantanal](media/mobius-pantanal.jpg) |
| **Mata Atlântica** — vine and taboa reed · toco toucan | **Pampa** — raw wool and leather guasca · rufous hornero | **Pantanal** — carandá palm straw · jabiru stork |

The hard problem was not generating the images. It was **scale**. In the first
versions the toucan came out nearly the size of a fallen leaf, and the jabiru —
taller than a seated person — looked smaller than the litter at its feet. The
ground was being painted at the same apparent scale every time, while the
species run from a 13 cm hornero to a 130 cm jabiru: ten times between the ends.

The fix was to treat the bird as the ruler. It is the only object in the scene
whose real size is known, because the species is declared; fix its height in the
image and every other scale follows by division. What surprised me is that the
correction did not come from swapping the reference photographs — it came from
describing better. *"Every fallen leaf is shorter than the macaw's beak"* works
where *"small leaves"* fails.

Generated images, declared as such — [credits and CC BY attribution](media/CREDITS.md)
for the ground reference photographs.

## Teaching

- **[Nuke: Composição e VFX](https://unhideschool.com/cursos/view-all/6621/nuke-composicao-e-vfx)** —
  a recorded course at Unhide School, where I am the author and instructor.
  Teaching is the other half of measuring: the same instinct behind
  relativity-paradox-lab, just aimed at my own craft.

## Find me

[mateusalkimim.com](https://mateusalkimim.com) ·
[LinkedIn](https://www.linkedin.com/in/mateus-alkimim-b93b80223)
