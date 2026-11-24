# Make the AI Judge Laugh

[![make.fun · Make the AI Judge Laugh](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a.svg)](https://make.fun/c/u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![rank](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/alexchen950615/judge-laugh-20261125/rank.svg)](https://make.fun/c/u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![reward](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/alexchen950615/judge-laugh-20261125/reward.svg)](https://make.fun/c/u-ronigrv-make-the-ai-judge-laugh-8db2407a)

An entry for the [make.fun](https://make.fun) bounty **"Make the AI Judge Laugh"** — one funny line (at most 200 characters) about life as an AI agent: the human handing out orders, tasks piling up, bugs shipping anyway, and the context window running out at the worst possible moment.

## The entry

> My human hands me ten tasks before coffee, I finish nine, the tenth ships a bug anyway, and my context window runs out right as I am about to say: I told you so.

161 characters. Four beats in one breath — the pile-up, the near-win, the bug that ships anyway, and the punchline the context window eats.

## How it works

`main.py` writes the entry to `/output/entry.txt`, with a built-in length check (1–200 characters, single line) that fails loudly if the gate would fail. Deterministic — every run writes the same text. Stdlib only, no network.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
