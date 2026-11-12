"""``uv run gesture <command>``: the gesture generator's tools (notes/gesture_plan.md).

    uv run gesture build-library [--speakers 1_wayne 4_lawrence 9_miranda] [--out ...]
    uv run gesture report [--library ...]
    uv run gesture analyze [--library ...]
    uv run gesture generate --reply speech/runs/<session>/turn_01 [--random-baseline]
    uv run gesture render --dir logs/gesture/replies/<name> [--push] [--obs-delay-steps 2]
    uv run gesture check --dirs logs/gesture/replies/*
    uv run gesture conversation --sessions speech/runs/<session> [...] [--max-minutes 10]
    uv run gesture serve                                   # for the speech loop (step 6)
    uv run gesture replay --session speech/runs/<session>  # conversation + render + check
    uv run gesture live                                    # K1 gesturing live in a MuJoCo window (step 7)
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import tyro

from booster_mjlab.gesture.analysis import AnalysisCfg, run
from booster_mjlab.gesture.generate import (
    CheckCfg,
    ConversationCfg,
    GenCfg,
    RenderCfg,
    ReplayCfg,
    check,
    conversation,
    generate,
    render,
    replay,
)
from booster_mjlab.gesture.live import LiveCfg, live
from booster_mjlab.gesture.serve import ServeCfg, serve
from booster_mjlab.gesture.library import LibraryCfg, build, report


@dataclass
class Report:
    library: Path = LibraryCfg.out


def main() -> None:
    cmd = tyro.extras.subcommand_cli_from_dict({
        "build-library": LibraryCfg,
        "report": Report,
        "analyze": AnalysisCfg,
        "generate": GenCfg,
        "render": RenderCfg,
        "check": CheckCfg,
        "conversation": ConversationCfg,
        "serve": ServeCfg,
        "replay": ReplayCfg,
        "live": LiveCfg,
    })
    if isinstance(cmd, LibraryCfg):
        build(cmd)
    elif isinstance(cmd, Report):
        report(cmd.library)
    elif isinstance(cmd, GenCfg):
        generate(cmd)
    elif isinstance(cmd, RenderCfg):
        render(cmd)
    elif isinstance(cmd, CheckCfg):
        check(cmd)
    elif isinstance(cmd, ConversationCfg):
        conversation(cmd)
    elif isinstance(cmd, ServeCfg):
        serve(cmd)
    elif isinstance(cmd, ReplayCfg):
        replay(cmd)
    elif isinstance(cmd, LiveCfg):
        live(cmd)
    else:
        run(cmd)


if __name__ == "__main__":
    main()
