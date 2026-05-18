"""
ASCII PIXEL GAME — STREET FIGHTER II  ROUND 3
Animasi pertarungan RYU vs ZANGIEF selama 30 detik.
Jalankan: python street_fighter_ascii.py
"""

import time
import os
import sys

CLEAR = "\033[2J\033[H"
RED     = "\033[91m"
YELLOW  = "\033[93m"
WHITE   = "\033[97m"
GRAY    = "\033[90m"
RESET   = "\033[0m"
BOLD    = "\033[1m"

FRAMES = [
    # 0 — Round Start
    (RED, """
    ╔══════════════════════════════════╗
    ║   STREET FIGHTER II   ROUND 3    ║
    ╚══════════════════════════════════╝
    RYU  [████████████████████] ZANGIEF
    RYU  [██████████████░░░░░░] ZANGIEF

    ┌────────────────────────────────┐
    │                                │
    │      o/         _o_            │
    │      |       _<( )>_           │
    │      /\\       / | \\          │
    │                                │
    └────────────────────────────────┘
         RYU           ZANGIEF

    ════════════════════════════════════
       *** ROUND 3 — FIGHT! ***"""),

    # 1 — Ryu walking forward
    (RED, """
    ╔══════════════════════════════════╗
    ║   STREET FIGHTER II   ROUND 3    ║
    ╚══════════════════════════════════╝
    RYU  [████████████████████] ZANGIEF
    RYU  [██████████████░░░░░░] ZANGIEF

    ┌────────────────────────────────┐
    │                                │
    │        o/       _o_            │
    │       /|>    _<( )>_           │
    │        |\\      / | \\         │
    │                                │
    └────────────────────────────────┘
       RYU mendekat...

    ════════════════════════════════════
    SCORE: 00000  TIME: 098"""),

    # 2 — Zangief jalan
    (RED, """
    ╔══════════════════════════════════╗
    ║   STREET FIGHTER II   ROUND 3    ║
    ╚══════════════════════════════════╝
    RYU  [████████████████████] ZANGIEF
    RYU  [██████████████░░░░░░] ZANGIEF

    ┌────────────────────────────────┐
    │                                │
    │          o/     _o_            │
    │         /|>  _<( )>_           │
    │          |\\  </  |\\          │
    │                                │
    └────────────────────────────────┘
       ZANGIEF siap bergulat!

    ════════════════════════════════════
    SCORE: 00000  TIME: 096"""),

    # 3 — Ryu charging
    (RED, """
    ╔══════════════════════════════════╗
    ║   STREET FIGHTER II   ROUND 3    ║
    ╚══════════════════════════════════╝
    RYU  [████████████████████] ZANGIEF
    RYU  [██████████████░░░░░░] ZANGIEF

    ┌────────────────────────────────┐
    │                                │
    │         _o      _o_            │
    │        (|>    _<( )>_          │
    │        /\\      / | \\         │
    │                                │
    └────────────────────────────────┘
       RYU: "HADOOOO..."  (charging)

    ════════════════════════════════════
    SCORE: 00000  TIME: 094"""),

    # 4 — Hadouken lepas
    (YELLOW, """
    ╔══════════════════════════════════╗
    ║   STREET FIGHTER II   ROUND 3    ║
    ╚══════════════════════════════════╝
    RYU  [████████████████████] ZANGIEF
    RYU  [██████████████░░░░░░] ZANGIEF

    ┌────────────────────────────────┐
    │                                │
    │        o>  ===(O)===  _o_      │
    │       /|>             / \\     │
    │       / \\                     │
    │                                │
    └────────────────────────────────┘
       RYU: "HADOUKEN!!!"

    ════════════════════════════════════
    SCORE: 00200  TIME: 092"""),

    # 5 — Hadouken mendekati Zangief
    (YELLOW, """
    ╔══════════════════════════════════╗
    ║   STREET FIGHTER II   ROUND 3    ║
    ╚══════════════════════════════════╝
    RYU  [████████████████████] ZANGIEF
    RYU  [██████████████░░░░░░] ZANGIEF

    ┌────────────────────────────────┐
    │                                │
    │        o>        ===(O)=  _o_  │
    │       /|>              _<(!)>_ │
    │       / \\               / | \\│
    │                                │
    └────────────────────────────────┘
       ZANGIEF: "NYET!!!"  (siap lompat)

    ════════════════════════════════════
    SCORE: 00200  TIME: 090"""),

    # 6 — HIT!
    (RED, """
    ╔══════════════════════════════════╗
    ║   STREET FIGHTER II   ROUND 3   ║
    ╚══════════════════════════════════╝
    RYU  [████████████████████] ZANGIEF
    RYU  [██████████████░░░░░░] ZANGIEF  -200HP

    ┌────────────────────────────────┐
    │                                │
    │        o>          *BOOM!*     │
    │       /|>           x_x        │
    │       / \\          /| \\      │
    │                                │
    └────────────────────────────────┘
       *** HIT! ZANGIEF -200HP ***

    ════════════════════════════════════
    SCORE: 00800  TIME: 088"""),

    # 7 — Zangief RAGE
    (RED, """
    ╔══════════════════════════════════╗
    ║   STREET FIGHTER II   ROUND 3    ║
    ╚══════════════════════════════════╝
    RYU  [████████████████████] ZANGIEF
    RYU  [██████████████░░░░░░] ZANGIEF

    ┌────────────────────────────────┐
    │                                │
    │        o/        >O<           │
    │        |>     _<( ! )>_        │
    │        /\\      / | \\         │
    │                                │
    └────────────────────────────────┘
       ZANGIEF: "GRRAAAH!!!" (RAGE)

    ════════════════════════════════════
    SCORE: 00800  TIME: 086"""),

    # 8 — Zangief lari
    (RED, """
    ╔══════════════════════════════════╗
    ║   STREET FIGHTER II   ROUND 3    ║
    ╚══════════════════════════════════╝
    RYU  [████████████████████] ZANGIEF
    RYU  [██████████████░░░░░░] ZANGIEF

    ┌────────────────────────────────┐
    │                                │
    │        o/      _O_             │
    │        |>   _<( )>_            │
    │        /\\   </  |>            │
    │                                │
    └────────────────────────────────┘
       ZANGIEF maju cepat!

    ════════════════════════════════════
    SCORE: 00800  TIME: 084"""),

    # 9 — Grab attempt
    (RED, """
    ╔══════════════════════════════════╗
    ║   STREET FIGHTER II   ROUND 3    ║
    ╚══════════════════════════════════╝
    RYU  [████████████████████] ZANGIEF
    RYU  [██████████████░░░░░░] ZANGIEF

    ┌────────────────────────────────┐
    │                                │
    │       o/   <>_O_               │
    │       |>  _<( )>_              │
    │       /\\   / | \\             │
    │                                │
    └────────────────────────────────┘
       ZANGIEF mencoba GRAB!

    ════════════════════════════════════
    SCORE: 00800  TIME: 082"""),

    # 10 — Ryu dodge
    (YELLOW, """
    ╔══════════════════════════════════╗
    ║   STREET FIGHTER II   ROUND 3    ║
    ╚══════════════════════════════════╝
    RYU  [████████████████████] ZANGIEF
    RYU  [██████████████░░░░░░] ZANGIEF

    ┌────────────────────────────────┐
    │                                │
    │      _o     _O_                │
    │      |>  _<( )>_ (GRAB MISS!)  │
    │      |    / | \\               │
    │                                │
    └────────────────────────────────┘
       RYU dodge! ZANGIEF meleset!

    ════════════════════════════════════
    SCORE: 01200  TIME: 080"""),

    # 11 — SHORYUKEN!
    (YELLOW, """
    ╔══════════════════════════════════╗
    ║   STREET FIGHTER II   ROUND 3    ║
    ╚══════════════════════════════════╝
    RYU  [████████████████████] ZANGIEF
    RYU  [██████████████░░░░░░] ZANGIEF

    ┌────────────────────────────────┐
    │          /o\\   _O_            │
    │         //|\\  (XXX)           │
    │           |    / \\            │
    │          / \\                  │
    │   RYU: "SHORYUKEN!!!"          │
    └────────────────────────────────┘
       *** SHORYUKEN!!! UPPERCUT! ***

    ════════════════════════════════════
    SCORE: 02400  TIME: 078"""),

    # 12 — Zangief terpental
    (RED, """
    ╔══════════════════════════════════╗
    ║   STREET FIGHTER II   ROUND 3    ║
    ╚══════════════════════════════════╝
    RYU  [████████████████████] ZANGIEF
    RYU  [████████░░░░░░░░░░░░] ZANGIEF  -500HP!

    ┌────────────────────────────────┐
    │                   x_x          │
    │        o/        /|\\          │
    │        |>        ZANGIEF DOWN! │
    │        /\\                     │
    │   *** CRITICAL HIT! -500HP *** │
    └────────────────────────────────┘
       ZANGIEF JATUH!

    ════════════════════════════════════
    SCORE: 04200  TIME: 076"""),

    # 13 — Zangief bangun
    (RED, """
    ╔══════════════════════════════════╗
    ║   STREET FIGHTER II   ROUND 3    ║
    ╚══════════════════════════════════╝
    RYU  [████████████████████] ZANGIEF
    RYU  [████████░░░░░░░░░░░░] ZANGIEF

    ┌────────────────────────────────┐
    │                                │
    │        o/        _/o           │
    │        |>        |>            │
    │        /\\       /  (bangun...)│
    │                                │
    └────────────────────────────────┘
       ZANGIEF bangkit perlahan...

    ════════════════════════════════════
    SCORE: 04200  TIME: 074"""),

    # 14 — SUPER COMBO
    (YELLOW, """
    ╔══════════════════════════════════╗
    ║   STREET FIGHTER II   ROUND 3    ║
    ╚══════════════════════════════════╝
    RYU  [████████████████████] ZANGIEF
    RYU  [████████░░░░░░░░░░░░] ZANGIEF
    *** SUPER COMBO READY! ***

    ┌────────────────────────────────┐
    │                                │
    │        o/      ★ _O_ ★        │
    │        |>    _<(!!!)>_         │
    │        /\\     / | \\          │
    │   *** SPINNING PILEDRIVER!! ***│
    └────────────────────────────────┘
       ZANGIEF: "FINAL ATOMIC BUSTER!"

    ════════════════════════════════════
    SCORE: 04200  TIME: 072"""),

    # 15 — Zangief menangkap Ryu
    (RED, """
    ╔══════════════════════════════════╗
    ║   STREET FIGHTER II   ROUND 3    ║
    ╚══════════════════════════════════╝
    RYU  [████████████████████] ZANGIEF
    RYU  [██░░░░░░░░░░░░░░░░░░] ZANGIEF  -700HP!!

    ┌────────────────────────────────┐
    │                                │
    │        _O_                     │
    │     _<(RYU)>_  <- CAUGHT!      │
    │      / | \\                    │
    │   SPINNING PILEDRIVER!!!       │
    └────────────────────────────────┘
       *** CRITICAL!!! RYU -700HP ***

    ════════════════════════════════════
    SCORE: 04200  TIME: 068"""),

    # 16 — RYU DOWN
    (RED, """
    ╔══════════════════════════════════╗
    ║   STREET FIGHTER II   ROUND 3    ║
    ╚══════════════════════════════════╝
    RYU  [██░░░░░░░░░░░░░░░░░░] ZANGIEF
    RYU  [████████░░░░░░░░░░░░] ZANGIEF

    ┌────────────────────────────────┐
    │  x_x                           │
    │  /|\\  <- RYU DOWN!    _O_     │
    │   |                _<( )>_     │
    │  / \\               / | \\     │
    │   ZANGIEF MENANG??             │
    └────────────────────────────────┘
       RYU terjatuh keras...

    ════════════════════════════════════
    SCORE: 04200  TIME: 064"""),

    # 17 — Ryu bangkit (dramatic)
    (YELLOW, """
    ╔══════════════════════════════════╗
    ║   STREET FIGHTER II   ROUND 3    ║
    ╚══════════════════════════════════╝
    RYU  [██░░░░░░░░░░░░░░░░░░] ZANGIEF
    RYU  [████████░░░░░░░░░░░░] ZANGIEF

    ┌────────────────────────────────┐
    │                                │
    │       _/o          _O_         │
    │       |>        _<( )>_        │
    │      /  (ryu...)  / | \\       │
    │   "...not yet."                │
    └────────────────────────────────┘
       RYU bangkit dengan susah payah!

    ════════════════════════════════════
    SCORE: 04200  TIME: 060"""),

    # 18 — Final charge
    (YELLOW, """
    ╔══════════════════════════════════╗
    ║   STREET FIGHTER II   ROUND 3    ║
    ╚══════════════════════════════════╝
    RYU  [██░░░░░░░░░░░░░░░░░░] ZANGIEF
    RYU  [████████░░░░░░░░░░░░] ZANGIEF

    ┌────────────────────────────────┐
    │                                │
    │       _o           _O_         │
    │      (|>        _<( )>_        │
    │      /\\          / | \\       │
    │   RYU charging SUPER HADOUKEN! │
    └────────────────────────────────┘
       "...METSU... HADOUKEN!!!"

    ════════════════════════════════════
    SCORE: 04200  TIME: 056"""),

    # 19 — SUPER HADOUKEN BESAR
    (YELLOW, """
    ╔══════════════════════════════════╗
    ║   STREET FIGHTER II   ROUND 3    ║
    ╚══════════════════════════════════╝
    RYU  [██░░░░░░░░░░░░░░░░░░] ZANGIEF
    RYU  [████████░░░░░░░░░░░░] ZANGIEF

    ┌────────────────────────────────┐
    │                                │
    │  o>  ===((((O))))===   _O_     │
    │ /|>                 _<( )>_    │
    │ / \\                 / | \\    │
    │  METSU HADOUKEN!!!!!           │
    └────────────────────────────────┘
       *** SUPER ART!!! ***

    ════════════════════════════════════
    SCORE: 08800  TIME: 052"""),

    # 20 — IMPACT BESAR
    (RED, """
    ╔══════════════════════════════════╗
    ║   STREET FIGHTER II   ROUND 3    ║
    ╚══════════════════════════════════╝
    RYU  [██░░░░░░░░░░░░░░░░░░] ZANGIEF
    RYU  [░░░░░░░░░░░░░░░░░░░░] ZANGIEF  KO!

    ┌────────────────────────────────┐
    │         * * * BOOM! * * *      │
    │  o>      \\  |  /   X_X        │
    │ /|>       \\ | /   /|\\        │
    │ / \\        \\|/    /  \\      │
    │   *** SUPER CRITICAL HIT!! *** │
    └────────────────────────────────┘
       ZANGIEF HP = 0 !!!!

    ════════════════════════════════════
    SCORE: 12400  TIME: 048"""),

    # 21 — K.O. screen
    (RED, """
    ╔══════════════════════════════════╗
    ║   STREET FIGHTER II   ROUND 3    ║
    ╚══════════════════════════════════╝
    RYU  [██░░░░░░░░░░░░░░░░░░] ZANGIEF
    RYU  [░░░░░░░░░░░░░░░░░░░░] ZANGIEF

    ┌────────────────────────────────┐
    │                                │
    │       o/            x___x      │
    │       |            /|   |\\    │
    │       /\\           / \\  /\\  │
    │                                │
    │        *** K . O . !!! ***     │
    └────────────────────────────────┘
       ZANGIEF is DOWN!!!

    ════════════════════════════════════
    SCORE: 12400  TIME: 044"""),

    # 22 — RYU WINS
    (YELLOW, """
    ╔══════════════════════════════════╗
    ║   STREET FIGHTER II   ROUND 3    ║
    ╚══════════════════════════════════╝
    RYU  [██░░░░░░░░░░░░░░░░░░] ZANGIEF
    RYU  [░░░░░░░░░░░░░░░░░░░░] ZANGIEF

    ┌────────────────────────────────┐
    │                                │
    │      \\o/    WINNER!!!         │
    │       |                        │
    │      / \\   "The answer lies   │
    │             in the heart of    │
    │             battle!"           │
    └────────────────────────────────┘
          ★ RYU WINS!!! ★

    ════════════════════════════════════
    PERFECT SCORE: 12400 + BONUS 5000"""),

    # 23 — RESULT SCREEN
    (WHITE, """
    ╔══════════════════════════════════╗
    ║        BATTLE RESULTS            ║
    ╚══════════════════════════════════╝

    ┌────────────────────────────────┐
    │   FIGHTER   : RYU              │
    │   ROUND WON : ★ ★             │
    │   HIT COUNT : 024              │
    │   COMBO MAX : 8 HIT!!!         │
    │   BONUS     : +5000            │
    │   FINAL SCORE: 17400           │
    │                                │
    │   ACHIEVEMENTS:                │
    │   [] SHORYUKEN MASTER          │
    │   [] METSU HADOUKEN            │
    │   [] PERFECT DODGE             │
    └────────────────────────────────┘

    ════════════════════════════════════
       CONTINUE? INSERT COIN..."""),
]

GAME_OVER = f"""
{BOLD}{YELLOW}
    ╔══════════════════════════════════════╗
    ║    *** GAME OVER — INSERT COIN ***   ║
    ║                                      ║
    ║       ★  RYU  CHAMPION!  ★          ║
    ║                                      ║
    ║    FINAL SCORE :  17400              ║
    ║    MAX COMBO   :  8 HIT              ║
    ║    TIME LEFT   :  000                ║
    ║                                      ║
    ║       [ PRESS START ]                ║
    ╚══════════════════════════════════════╝
{RESET}"""

def draw_bar(elapsed, total=30.0, width=38):
    filled = int((elapsed / total) * width)
    bar = "█" * filled + "░" * (width - filled)
    pct = int((elapsed / total) * 100)
    return f"  [{bar}] {pct}%  {elapsed:.1f}s / {total:.0f}s"

def run():
    total = 30.0
    n = len(FRAMES)
    match_num = 1

    try:
        while True:
            start = time.time()

            # --- FIGHT loop ---
            while True:
                elapsed = time.time() - start
                if elapsed >= total:
                    break

                fi = min(int((elapsed / total) * n), n - 1)
                color, frame = FRAMES[fi]

                header = (
                    f"{BOLD}{RED}  [ STREET FIGHTER II — ROUND 3 ]"
                    f"  MATCH #{match_num}{RESET}\n"
                    f"{GRAY}{draw_bar(elapsed)}{RESET}\n"
                )
                print(CLEAR + header + color + BOLD + frame + RESET)
                time.sleep(0.12)

            # --- GAME OVER sebentar lalu mulai ulang ---
            print(CLEAR + GAME_OVER)
            time.sleep(2.5)
            match_num += 1

    except KeyboardInterrupt:
        print(CLEAR + f"\n{YELLOW}  [Pertarungan dihentikan! Total match: {match_num}]{RESET}\n")
        sys.exit(0)

if __name__ == "__main__":
    print(f"{BOLD}{RED}")
    print("  ╔══════════════════════════════════╗")
    print("  ║   STREET FIGHTER II — ROUND 3    ║")
    print("  ║   RYU  vs  ZANGIEF               ║")
    print("  ║   Durasi : 30 detik              ║")
    print("  ║   Ctrl+C untuk keluar            ║")
    print("  ╚══════════════════════════════════╝")
    print(f"{RESET}")
    time.sleep(1.5)
    run()
