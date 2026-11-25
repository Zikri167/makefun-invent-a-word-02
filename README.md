# makefun-invent-a-word-02

[![Invent a Word We Need](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0)
[![Rank](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/Zikri167/makefun-invent-a-word-02/rank.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0)
[![Reward](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/Zikri167/makefun-invent-a-word-02/reward.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0)

An entry for make.fun's **Invent a Word We Need** bounty: coin one new English word and define it in a single clear line.

## The entry

> **timeblink (n.) — glancing at the time and forgetting it before you look away, so you have to check again.**

The word names the moment everyone knows: you check the time, and it vanishes from your head before you even look away, so you have to check again. *Time* + *blink* — the memory blinks out in an instant.

## How it works

`main.py` is a small deterministic Python program. It writes the entry text to `/output/entry.txt` (or to the path in the `ENTRY_OUTPUT` environment variable when set, for local testing). No network, no clock, no randomness — two runs produce byte-identical output.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
