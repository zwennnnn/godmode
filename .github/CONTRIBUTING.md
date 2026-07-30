# Contributing to godmode

> Thank you for your interest in contributing to godmode — the weighted-scoring technology decision engine.

godmode is a curated knowledge base of 117+ technologies from [roadmap.sh](https://roadmap.sh), organized across 17 roadmaps. Every contribution makes the engine smarter for everyone.

---

## Ways to contribute

| Contribution type | Difficulty | Impact |
|------------------|-----------|--------|
| **Fix a typo / broken link** in a tech `.md` | Easy | Low |
| **Update scoring matrix** with 2026 data | Easy | Medium |
| **Add a new technology** (run `scripts/research.py --interactive`) | Medium | High |
| **Add a new roadmap category** | Hard | Very high |
| **Improve the scoring algorithm** in `decision-engine.md` | Hard | High |
| **Add eval / tests** for `scripts/score.py` | Medium | High |
| **Improve documentation / examples** | Easy | Medium |
| **Translate tech MDs** to other languages | Medium | High |
| **Report bugs** in scoring / validation | Easy | Medium |

---

## Quick start

```bash
# 1. Fork the repo
# 2. Clone your fork
git clone https://github.com/<your-fork>/godmode
cd godmode

# 3. Create a branch
git checkout -b add-<tech>-to-<roadmap>

# 4. Make your change (edit or add a tech MD)

# 5. Validate
python scripts/validate-md.py roadmaps/<category>/<tech>.md

# 6. Test the scoring engine
python scripts/score.py --roadmap <category> --stage mvp-speed

# 7. Commit + push
git add -A
git commit -m "Add <tech> to <category> roadmap"
git push origin add-<tech>-to-<roadmap>

# 8. Open a PR
gh pr create --title "Add <tech> to <category>" --body "..."
```

---

## Adding a new technology

Use the scaffolder — don't write the MD by hand:

```bash
python scripts/research.py --interactive
# Prompts:
#   - Tech name
#   - Roadmap folder
#   - Source URLs (comma-separated)
#   - Tags
#   - 7 scoring criteria (maturity, community, learning_curve, performance, cost, dx, production_readiness)
#   - One-liner + When-to-use + When-not + Why-it-matters + alternatives
# Writes a valid MD to roadmaps/<category>/<slug>.md.
```

After generating:
1. Fill in TODO evidence notes in the scoring matrix.
2. Run `python scripts/validate-md.py <file>.md` — must report OK.
3. Run `python scripts/score.py --roadmap <category> --stage mvp-speed` — verify the score.
4. Commit + PR.

---

## Contributing guidelines

### Required
- **Every tech MD must follow** [`templates/tech-md.md`](../templates/tech-md.md) — frontmatter + sections.
- **Sources must be dated** (YYYY-MM) and current (preferably 2025–2026).
- **Scoring must have evidence** — never an unbacked number.
- **Pass the validator** — `python scripts/validate-md.py <file>.md` must be OK before PR.

### Style
- **English only** for all `.md` files (per `rules.md`).
- **Bias toward evidence over opinion** — link sources, quote benchmarks.
- **Update `last-updated`** in frontmatter when you change the file.
- **Update `godmode.md`** Progress Tracker if you add a whole category.

### Don't
- ❌ Don't modify `rules.md` — it's the user's, untouched.
- ❌ Don't invent scoring numbers.
- ❌ Don't include marketing claims without sources.
- ❌ Don't add a tech to a roadmap without at least 3 sources (1 official + 2 third-party).
- ❌ Don't skip the validator.

---

## Adding a new roadmap category

1. **Discuss first** — open an issue with your proposal.
2. **If approved**:
   - Create `roadmaps/<your-category>/README.md` (copy from `templates/roadmap-index.md`).
   - Add 5–10 starter techs (use `scripts/research.py`).
   - Update `godmode.md` Progress Tracker + add to `SKILL.md` coverage list.
   - Run full validation.
3. **Submit PR** with category proposal + 5+ techs.

---

## Reporting bugs

Found a scoring inconsistency? A wrong "When NOT to use"? A broken source link?

- **Open an issue** at [github.com/zwennnnn/godmode/issues](https://github.com/zwennnnn/godmode/issues).
- Include: tech name, file path, what's wrong, what it should be.
- Tag with: `bug` / `scoring` / `docs` / `data`.

---

## Code of conduct

- **Be kind** — we're all here to make better tech decisions.
- **Be evidence-based** — cite sources, not opinions.
- **Be patient** — maintainers are volunteers.
- **Be open** — assume good faith; ask questions.

---

## Maintainers

- [zwennnnn](https://github.com/zwennnnn) — creator, lead maintainer.

See [CONTRIBUTORS.md](../CONTRIBUTORS.md) for the full list of contributors.

---

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](../LICENSE).

Thanks for making godmode better! 🚀