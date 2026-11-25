# news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/ayilinalin/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/ayilinalin/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

One page of the world's news for Wednesday, 25 November 2026. The front page names its day in the dateline and covers the wars in Ukraine and Gaza, Huawei's US verdict, Asian markets on AI jitters, Pakistan's first astronaut in orbit, Ábrego García's departure for Spain, China's purge, the Gambia's election, Bangladesh's pay rise, and Colombia's hostage siege.

The page was drawn as a broadsheet: a masthead, a lead story with a 500,000-dead stat panel, two columns of six news stories with subject labels, a three-item briefs row, and a footer naming the reporting sources. Headlines were checked against live BBC, Al Jazeera, Guardian and NPR feeds from 25 November 2026.

## Run it

```sh
python3 main.py
```

The program checks the PNG's magic bytes and its 1024 by 1024 dimensions, then copies it to `/output/entry.png`. Outside the grader's container, `MAKEFUN_OUTPUT_DIR` stands in for `/output`:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The image is 1024 by 1024 pixels and about 131 KiB, well inside the competition's one-megabyte limit. Both runs write the same bytes.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
