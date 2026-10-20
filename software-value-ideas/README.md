# Software value ideas (October 2026)

Idea-generation work on value opportunities in software after the 2026 AI sell-off: a 10-slide summary deck plus 10-slide deep dives on the top three ideas. Prices are as of the **19 October 2026 close**. For discussion only; not investment advice.

## Decks (private claude.ai artifacts)

| Deck | Link |
|---|---|
| Software at a discount (summary, 10 slides) | https://claude.ai/artifact/4SYRtGuPPXp8Y6LbHgSsGp |
| Adobe deep dive | https://claude.ai/artifact/WUZY5Tw9WGiWNcsjdLbZQG |
| Intuit deep dive | https://claude.ai/artifact/X7gWG82MGis5o1DtesSpjb |
| GoDaddy deep dive | https://claude.ai/artifact/3VzZXfxLDoDCKHWM9GMhM9 |

## Method

- **Owner FCF** = free cash flow minus stock-based comp. Hurdle: an owner FCF yield of at least 7%.
- **Growth priced in**: the perpetual growth rate implied by a Gordon reverse DCF at a 9.5% discount rate: `g = (R·EV − OFCF) / (EV + OFCF)`.
- **Durability score (0–4)**, one point each for:
  - owning the system of record or data;
  - regulatory or trust lock-in;
  - pricing that AI agents can't shrink;
  - distribution to ship AI first.
- **Scenarios**: a multiple of next-year owner FCF per share. Bear, base and bull are weighted 25/50/25 for the probability-weighted value.

## Conclusions at the 19 Oct close

| Idea | Price | Owner FCF yield | Growth priced in | Bear / Base / Bull | Size |
|---|---|---|---|---|---|
| Adobe (ADBE) | $247 | 8.9% | 0.6% | $165 / $340 / $465 | Full |
| Intuit (INTU) | $326 | 7.6% | 1.8% | $210 / $400 / $525 | Half; add below $300 |
| GoDaddy (GDDY) | $107 | 10.4% | 0.8% | $60 / $140 / $205 | Half (leverage) |

- **On deck:** FactSet (buy below ~$250) and Salesforce (buy below ~$195).
- **Value traps:** HubSpot, monday.com, Dropbox, Gartner, Fair Isaac and Gen Digital.

## Layout

- `research/`: source notes behind every number, with links.
- `model/`: valuation scripts.
  - `final.py` holds the scenario values at 6 Oct prices.
  - `refresh.py` re-bases the price-driven metrics to 19 Oct.
- `gen/`: slide generators.
  - `idea.py` and `ideas.json` build the three idea pages.
  - `rest.py` builds the on-deck, traps and risks slides.
  - `screen.py` builds the scatter.
  - `adbe.py`, `intu.py` and `gddy.py` build the deep dives, using `deep.py`.
  - Hand-written slides: `cover`, `summary` and `setup` in the main deck, and the scatter host embedded in `screen.html`.
- `decks/<name>/project/`: the published Slides-artifact sources (`deck.json` and one HTML file per slide).
- `tools/`:
  - `lint.py` checks the allowed tags, properties and minimum font sizes.
  - `render.cjs` renders each slide at 1920×1080 with Playwright and flags overflow and wrapped footers.

Regenerate from this folder:

```sh
python3 gen/adbe.py && python3 gen/intu.py && python3 gen/gddy.py
python3 gen/idea.py gen/ideas.json decks/main/project/slides && python3 gen/rest.py
python3 tools/lint.py decks/main
node tools/render.cjs decks/main /tmp/render-main
```

## Data caveats

- Finance data sites (SEC EDGAR, Yahoo and others) could not be fetched directly from the build environment. Figures come from web-search results and are cross-checked where possible.
- For Intuit's 19 Oct close, Benzinga shows $325.62 and Morningstar shows $322.41 shortly after the close. The decks use $326.
- The screen scatter uses 19 Oct prices for the five names in the decks and 6 Oct prices for the rest. The traps slide uses 6 Oct multiples.
