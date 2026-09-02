#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assembles the repaired/completed "She Survived: Now Name Her." Twine HTML."""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "source" / "original.html"
OUT = ROOT / "She Survived - Now Name Her.html"

with open(ROOT / "build" / "css.txt", encoding="utf-8") as f:
    CSS = f.read()
with open(ROOT / "build" / "js.txt", encoding="utf-8") as f:
    JS = f.read()

# ---------------------------------------------------------------------------
# Passage list: (name, tags, content)
# ---------------------------------------------------------------------------
P = []

def add(name, tags, content):
    P.append((name, tags, content.strip("\n")))

# ============================== OPENING =====================================

add("Start", "opening", """
(set: $Earth to 0)
(set: $Fire to 0)
(set: $Water to 0)
(set: $Night to 0)
(set: $Warm to 0)
(set: $Bold to 0)
(set: $Creative to 0)
(set: $Unusual to 0)
(set: $Grounded to 0)
(set: $Sophisticated to 0)
(set: $Wild to 0)
(set: $MumArchetype to "")
(set: $ChildName to "")
(set: $LoveNames to (a:))
(set: $MaybeNames to (a:))
(set: $NopeNames to (a:))
(set: $WTFNames to (a:))
(set: $Bracket to (a:))
(set: $NextRoundResults to (a:))
(set: $Finalists to (a:))
(set: $WildcardUsed to false)
(set: $WildcardName to "")
(set: $WildcardSource to "")
(set: $CustomFirst to "")
(set: $CustomMiddle to "")
(set: $CustomSurname to "")
(set: $CustomFullName to "")
(set: $HelpVibe to "")
(set: $FinalReason to "")
(set: $WinnerName to "")
(set: $FinalHeadline to "")
(set: $ResultHeading to "")
(set: $CandidateInfo to (datamap:
"Zaira Maree Rivers", (datamap: "pron", "ZY-rah", "vibe", "Bright and a little unstoppable. Never stays where life dumped her."),
"Rhea Kristal Sinclair", (datamap: "pron", "REE-ah", "vibe", "Runs the room without ever raising her voice."),
"Zora Kristal Forest", (datamap: "pron", "ZOR-ah", "vibe", "Dawn energy with feral edges."),
"Marlowe Rae Quinn", (datamap: "pron", "MAR-loh", "vibe", "Sees everything. Explains nothing."),
"Zaria Rae Sterling", (datamap: "pron", "ZAR-ee-ah", "vibe", "Polished. Still has bite."),
"Nadia Rae Winter", (datamap: "pron", "NAH-dee-ah", "vibe", "Hope with a cold front behind it."),
"Zelia Rae Morrow", (datamap: "pron", "ZEE-lee-ah", "vibe", "Quietly memorable. Grows on you."),
"Vesper Kristal Wilde", (datamap: "pron", "VESS-per", "vibe", "Arrives late. Changes the whole room."),
"Kaia Rae Morrow", (datamap: "pron", "KY-ah", "vibe", "Warm, wild, and not explaining herself."),
"Thea Rae Osmond", (datamap: "pron", "THEE-ah", "vibe", "Lets everyone else finally see clearly."),
"Juno Kristal Hale", (datamap: "pron", "JOO-noh", "vibe", "Ends arguments just by walking in."),
"Romy Maree Calder", (datamap: "pron", "ROH-mee", "vibe", "Sounds soft. Is not remotely soft.")
))

# SHE SURVIVED: NOW NAME HER

From the ashes she rose.

Not brand new.
Not magically fixed.
Just a little more herself than she used to be.

There were great decisions.
There were questionable decisions.
There were balls dropped.
There were probably a few launched into another postcode.

There were definitely opinions.

Fair.

You are not being asked to rewrite history or pretend Mum has suddenly become a normal, punctual adult with a functioning sense of direction.

That ship sailed years ago.

She still gets wildly excited about fairies.
She will absolutely stop to admire a suspiciously beautiful stick.
She can leave "with plenty of time" and still arrive late.

And if she says:

"I know where I'm going..."

check Google Maps immediately.

You've known all the strange little bits that have always been me — so what name actually feels like Mum?

Roast the names.
Reject them dramatically.
Suggest something completely cooked.

But when it counts, give me your real answer.

[[BEGIN THE FAMILY RESEARCH->WhoAreYou]]
""")

add("WhoAreYou", "opening", """
# WHICH OFFSPRING ARE YOU?

WHICH OFFSPRING ARE YOU?
Choose carefully.

This may be the most authority Mum has ever voluntarily handed you.

[[Connor->ConnorStart]]

[[Grace->GraceStart]]

[[Hunter->HunterStart]]

[[Avs->AvsStart]]

[[Harry->HarryStart]]

No, you cannot select your sibling and sabotage their data.
""")

add("ConnorStart", "opening", """
(set: $ChildName to "Connor")
# CONNOR HAS ENTERED THE CHAT
Peacekeeping privileges are temporarily suspended.
Today, you are encouraged to have an opinion.
A real one.
Terrifying, I know.
[[Begin Question 1->Question1]]
""")

add("GraceStart", "opening", """
(set: $ChildName to "Grace")
# GRACE HAS ENTERED THE CHAT
Excellent.
Someone with standards.
Please try not to turn this into a full performance review of Mum.
Actually... no promises.
[[Begin Question 1->Question1]]
""")

add("HunterStart", "opening", """
(set: $ChildName to "Hunter")
# HUNTER HAS ENTERED THE CHAT
Congratulations on recently becoming An Adult™.
House. Bills. Relationship. Opinions.
Still no authority over Mum, unfortunately.
[[Use your new adult powers wisely->Question1]]
""")

add("AvsStart", "opening", """
(set: $ChildName to "Avs")
# AVS HAS ENTERED THE CHAT
Mini-Mum detected.
This could be extremely useful.
Or extremely dangerous.
Probably both.
[[Proceed with caution->Question1]]
""")

add("HarryStart", "opening", """
(set: $ChildName to "Harry")
# HARRY HAS ENTERED THE CHAT
You have been selected for classified naming operations.
Your mission:
Judge Mum.
Try not to enjoy the power too much.
[[Begin mission->Question1]]
""")

# ============================== QUESTIONS 1-7 ================================

add("Question1", "interrogation", """
# QUESTION 1 / 7
## If Mum were an element, she'd be...
(link: "🔥 FIRE")[
(set: $Fire to $Fire + 2)
(set: $Bold to $Bold + 1)
(set: $Wild to $Wild + 1)
(go-to: "Question2")
]
(link: "🌊 WATER")[
(set: $Water to $Water + 2)
(set: $Warm to $Warm + 1)
(set: $Creative to $Creative + 1)
(go-to: "Question2")
]
(link: "🌿 EARTH")[
(set: $Earth to $Earth + 2)
(set: $Grounded to $Grounded + 2)
(go-to: "Question2")
]
(link: "🌬 AIR")[
(set: $Creative to $Creative + 2)
(set: $Unusual to $Unusual + 1)
(go-to: "Question2")
]
(link: "⚡ WHATEVER LIGHTNING COUNTS AS")[
(set: $Bold to $Bold + 2)
(set: $Wild to $Wild + 2)
(set: $Unusual to $Unusual + 1)
(go-to: "Question2")
]
---
*Choose carefully. The algorithm is already making assumptions.*
""")

add("Question2", "interrogation", """
QUESTION 2 / 7

Mum exists most naturally at...

(link: "🌅 SUNRISE")[
(set: $Warm to $Warm + 1)
(set: $Grounded to $Grounded + 1)
(set: $Creative to $Creative + 1)
(go-to: "Question3")
]

(link: "☀️ MASSIVE SUNNY DAY")[
(set: $Warm to $Warm + 2)
(set: $Fire to $Fire + 1)
(go-to: "Question3")
]

(link: "🌇 SUNSET")[
(set: $Creative to $Creative + 2)
(set: $Warm to $Warm + 1)
(set: $Night to $Night + 1)
(go-to: "Question3")
]

(link: "🌙 MIDNIGHT")[
(set: $Night to $Night + 2)
(set: $Sophisticated to $Sophisticated + 1)
(set: $Wild to $Wild + 1)
(go-to: "Question3")
]

(link: "🕒 3:07AM MAKING QUESTIONABLE DECISIONS")[
(set: $Wild to $Wild + 3)
(set: $Unusual to $Unusual + 2)
(go-to: "Question3")
]

---

Pick honestly. Mum denies all allegations.
""")

add("Question3", "interrogation", """
QUESTION 3 / 7

Pick Mum's natural habitat

(link: "🌊 BEACH")[
(set: $Water to $Water + 2)
(set: $Warm to $Warm + 1)
(set: $Wild to $Wild + 1)
(go-to: "Question4")
]

(link: "🌲 FOREST")[
(set: $Earth to $Earth + 2)
(set: $Grounded to $Grounded + 1)
(set: $Night to $Night + 1)
(go-to: "Question4")
]

(link: "🏙 CITY AT NIGHT")[
(set: $Night to $Night + 2)
(set: $Sophisticated to $Sophisticated + 2)
(go-to: "Question4")
]

(link: "🏔 MOUNTAINS")[
(set: $Earth to $Earth + 1)
(set: $Bold to $Bold + 2)
(set: $Grounded to $Grounded + 1)
(go-to: "Question4")
]

(link: "🚧 SOMEWHERE SHE PROBABLY WASN'T MEANT TO BE")[
(set: $Wild to $Wild + 3)
(set: $Unusual to $Unusual + 2)
(set: $Bold to $Bold + 1)
(go-to: "Question4")
]

---

Mum's legal team has requested silence.
""")

add("Question4", "interrogation", """
QUESTION 4 / 7 Choose Mum's uniform

(link: "👖 DENIM + BARE FEET")[ (set: $Earth to $Earth + 2) (set: $Grounded to $Grounded + 1) (go-to: "Question5") ]

(link: "🖤 BLACK EVERYTHING")[ (set: $Night to $Night + 2) (set: $Sophisticated to $Sophisticated + 1) (go-to: "Question5") ]

(link: "✨ SOMETHING UNNECESSARILY DRAMATIC")[ (set: $Creative to $Creative + 2) (set: $Unusual to $Unusual + 1) (set: $Bold to $Bold + 1) (go-to: "Question5") ]

(link: "🧥 LEATHER + BOOTS")[ (set: $Bold to $Bold + 2) (set: $Fire to $Fire + 1) (go-to: "Question5") ]

(link: "🤷 WHATEVER WAS CLEAN")[ (set: $Wild to $Wild + 1) (set: $Grounded to $Grounded + 1) (set: $Warm to $Warm + 1) (go-to: "Question5") ]

Fashion analysis complete. Conclusions remain questionable.
""")

add("Question5", "interrogation", """
QUESTION 5 / 7 Mum's strongest energy is...

(link: "❤️ WARM")[ (set: $Warm to $Warm + 3) (go-to: "Question6") ]

(link: "🔥 FIERCE")[ (set: $Fire to $Fire + 2) (set: $Bold to $Bold + 2) (go-to: "Question6") ]

(link: "🧠 CLEVER")[ (set: $Sophisticated to $Sophisticated + 2) (set: $Creative to $Creative + 1) (go-to: "Question6") ]

(link: "😈 MISCHIEVOUS")[ (set: $Wild to $Wild + 2) (set: $Unusual to $Unusual + 1) (go-to: "Question6") ]

(link: "🌿 GROUNDED")[ (set: $Earth to $Earth + 2) (set: $Grounded to $Grounded + 2) (go-to: "Question6") ]

(link: "🌀 COMPLETELY IMPOSSIBLE TO CATEGORISE")[ (set: $Unusual to $Unusual + 3) (set: $Creative to $Creative + 2) (set: $Wild to $Wild + 1) (go-to: "Question6") ]

Excellent. Nothing has been clarified.
""")

add("Question6", "interrogation", """
QUESTION 6 / 7 Pick Mum an animal

Spiritually. Not legally. Calm down.

(link: "🐺 WOLF")[ (set: $Earth to $Earth + 1) (set: $Night to $Night + 1) (set: $Bold to $Bold + 2) (go-to: "Question7") ]

(link: "🦊 FOX")[ (set: $Creative to $Creative + 1) (set: $Wild to $Wild + 2) (set: $Sophisticated to $Sophisticated + 1) (go-to: "Question7") ]

(link: "🐦‍⬛ RAVEN")[ (set: $Night to $Night + 2) (set: $Creative to $Creative + 2) (go-to: "Question7") ]

(link: "🐆 BIG CAT")[ (set: $Fire to $Fire + 1) (set: $Bold to $Bold + 2) (set: $Sophisticated to $Sophisticated + 1) (go-to: "Question7") ]

(link: "🦅 EAGLE")[ (set: $Bold to $Bold + 2) (set: $Grounded to $Grounded + 1) (go-to: "Question7") ]

(link: "🦝 FERAL BIN-CHICKEN ENERGY")[ (set: $Wild to $Wild + 3) (set: $Unusual to $Unusual + 2) (go-to: "Question7") ]

Wildlife authorities have declined to comment.
""")

add("Question7", "interrogation", """
QUESTION 7 / 7 Someone meets Mum for the first time. What should they think?

(link: "SHE'S INTERESTING")[ (set: $Creative to $Creative + 2) (set: $Unusual to $Unusual + 1) (go-to: "ArchetypeReveal") ]

(link: "SHE'S STRONG")[ (set: $Bold to $Bold + 2) (set: $Grounded to $Grounded + 1) (go-to: "ArchetypeReveal") ]

(link: "SHE'S BEAUTIFUL")[ (set: $Warm to $Warm + 1) (set: $Sophisticated to $Sophisticated + 2) (go-to: "ArchetypeReveal") ]

(link: "SHE'S DEFINITELY DIFFERENT")[ (set: $Unusual to $Unusual + 3) (go-to: "ArchetypeReveal") ]

(link: "I PROBABLY SHOULDN'T UNDERESTIMATE HER")[ (set: $Bold to $Bold + 2) (set: $Sophisticated to $Sophisticated + 1) (set: $Wild to $Wild + 1) (go-to: "ArchetypeReveal") ]

(link: "ALL OF THE ABOVE, OBVIOUSLY")[ (set: $Warm to $Warm + 1) (set: $Bold to $Bold + 1) (set: $Creative to $Creative + 1) (set: $Unusual to $Unusual + 1) (set: $Grounded to $Grounded + 1) (set: $Sophisticated to $Sophisticated + 1) (set: $Wild to $Wild + 1) (go-to: "ArchetypeReveal") ]

Final answer locked. Mum is now being statistically judged.
""")

add("ArchetypeReveal", "interrogation", """
ANALYSING MUM...

Reviewing questionable evidence...

Consulting absolutely no qualified professionals...

Checking whether "feral" is a recognised personality type...

Ignoring several red flags...

(if: $Earth >= 5 and $Fire >= 4)[ (set: $MumArchetype to "ROOTED MENACE")

ROOTED MENACE 🌿🔥

Grounded. Warm. Stubborn.

Just dangerous enough to keep things interesting.

Apparently Mum is equal parts tree roots and bad ideas. ]

(else-if: $Water >= 5 and $Wild >= 4)[ (set: $MumArchetype to "FERAL MERMAID")

FERAL MERMAID 🌊😈

Flowing. Emotional. Adaptable.

Occasionally operating without appropriate adult supervision.

Can probably be returned to the ocean if found wandering. ]

(else-if: $Night >= 5 and $Sophisticated >= 4)[ (set: $MumArchetype to "MIDNIGHT CEO")

MIDNIGHT CEO 🌙🖤

Calm face.

Questionable thoughts.

Strong likelihood of knowing significantly more than she is admitting. ]

(else-if: $Creative >= 5 and $Wild >= 4)[ (set: $MumArchetype to "ART DEPARTMENT INCIDENT")

ART DEPARTMENT INCIDENT 🎨⚠️

Creative. Unpredictable.

Statistically unlikely to follow instructions.

May disappear briefly after noticing a particularly beautiful stick. ]

(else-if: $Warm >= 5 and $Bold >= 4)[ (set: $MumArchetype to "SUNSHINE WITH TEETH")

SUNSHINE WITH TEETH ☀️🦷

Warm enough to pull people in.

Fierce enough to make them reconsider several previous decisions.

Looks friendly.

Read the fine print. ]

(else-if: $Earth >= 5 and $Night >= 4)[ (set: $MumArchetype to "FOREST AFTER DARK")

FOREST AFTER DARK 🌲🌙

Grounded. Quiet. Slightly wild.

Would ideally live somewhere beautiful where nobody can find her.

Unfortunately she also cannot find herself because she is lost again. ]

(else-if: $Bold >= 5 and $Unusual >= 4)[ (set: $MumArchetype to "LIMITED EDITION")

LIMITED EDITION ⚡✨

Not everybody's cup of tea.

Fortunately Mum has never displayed any particular interest in being tea.

One of one. Returns not accepted. ]

(else-if: $Creative >= 5 and $Sophisticated >= 4)[ (set: $MumArchetype to "CLEVER BUT MAKE IT WEIRD")

CLEVER BUT MAKE IT WEIRD 🧠✨

Smart enough to know better.

Creative enough to do something else anyway.

Could probably make a fairy house out of roadside debris before arriving 40 minutes late. ]

(else-if: $Wild >= 5 and $Night >= 4)[ (set: $MumArchetype to "NOCTURNAL PROBLEM")

NOCTURNAL PROBLEM 🌙🚨

Technically functioning.

Spiritually unsupervised.

Nothing productive has ever started with:

"So I had an idea at 2am..." ]

(else-if: $Grounded >= 5 and $Warm >= 4)[ (set: $MumArchetype to "BAREFOOT ORACLE")

BAREFOOT ORACLE 🌿✨

Warm. Grounded. Weirdly observant.

Will give excellent advice while holding a rock she found three hours ago and now considers emotionally significant. ]

(else-if: $Fire >= 5 and $Wild >= 4)[ (set: $MumArchetype to "CONTROLLED BURN")

CONTROLLED BURN 🔥😈

Mostly controlled.

Technically.

Bright, fierce and capable of clearing out whatever no longer needs to be there.

Protective eyewear recommended. ]

(else:)[ (set: $MumArchetype to "CLASSIFICATION FAILED")

CLASSIFICATION FAILED 🌀

The results are annoyingly inconclusive.

Apparently Mum contains too many conflicting settings to fit neatly into one category.

Which, frankly...

feels suspiciously accurate. ]

THE IMPORTANT BIT

That's the personality sorted. Sort of.

But personality isn't the whole file. Time to open the rest of it.

[[KEEP DIGGING->Question8]]
""")

# ============================== QUESTIONS 8-17 ================================

add("Question8", "interrogation", """
QUESTION 8 / 10

The family group chat goes off. Mum's reply lands...

(link: "📵 Four hours later, like the conversation never happened")[ (go-to: "Question9") ]

(link: "🔊 As a voice note. A long one. With background noise.")[ (go-to: "Question9") ]

(link: "😂 One emoji. No context. You're supposed to just know.")[ (go-to: "Question9") ]

(link: "📖 A full paragraph, mid-thought, no greeting, fully formed opinions")[ (go-to: "Question9") ]

Message read. Meaning unclear. Business as usual.
""")

add("Question9", "interrogation", """
QUESTION 9 / 10

You get in the car. Mum's already driving. What's the situation?

(link: "🔊 Bass loud enough to renegotiate your organs")[ (go-to: "Question10") ]

(link: "🎧 The same three songs she's had on repeat since approximately 2014")[ (go-to: "Question10") ]

(link: "🎶 Something you've never heard of and will never be able to find again")[ (go-to: "Question10") ]

(link: "🤫 Total silence. She's mid-thought. Do not interrupt.")[ (go-to: "Question10") ]

Volume analysis complete. Hearing damage waivers recommended.
""")

add("Question10", "interrogation", """
QUESTION 10 / 10

Back when something went properly wrong, what usually happened?

(link: "📞 Someone was already calling Mum before you'd finished explaining")[ (go-to: "Question11") ]

(link: "🧩 She found the one weird angle nobody else had thought of")[ (go-to: "Question11") ]

(link: "🛠 She fixed it, then quietly made sure everyone else was okay too")[ (go-to: "Question11") ]

(link: "🙃 It landed in her lap anyway. It always did.")[ (go-to: "Question11") ]

Filed under: reasons people still have her number.
""")

add("Question11", "interrogation", """
QUESTION 11 / 10 (yes, the numbering gave up. so did she.)

A form needs to be filled out today. What actually happens?

(link: "⚡ Done in four minutes flat, somehow better than the instructions asked for")[ (go-to: "Question12") ]

(link: "🔬 Becomes a full research project with sub-questions")[ (go-to: "Question12") ]

(link: "🕚 Discovered again at 11:58pm, deadline intact through sheer will")[ (go-to: "Question12") ]

(link: "📤 Handed to somebody else within thirty seconds of arriving")[ (go-to: "Question12") ]

Bureaucracy: defeated, avoided, or ignored. Never neutral.
""")

add("Question12", "interrogation", """
QUESTION 12

Someone at pickup, a party or a queue tries to make small talk about the weather. Mum's move?

(link: "🚪 Polite exit strategy, already deployed before they finish the sentence")[ (go-to: "Question13") ]

(link: "😐 The stare. The one that ends conversations without a single word.")[ (go-to: "Question13") ]

(link: "📱 Sudden, extremely convincing phone emergency")[ (go-to: "Question13") ]

(link: "😅 Accidentally engages properly, immediately regrets it")[ (go-to: "Question13") ]

Small talk: survived. Barely. Under protest.
""")

add("Question13", "interrogation", """
QUESTION 13

Mum starts "just one small project." Where does it actually end up?

(link: "📦 Exactly where it was supposed to. Suspicious.")[ (go-to: "Question14") ]

(link: "🏗 A full renovation nobody signed off on")[ (go-to: "Question14") ]

(link: "🗂 Fourteen tabs and three brand new hobbies deep")[ (go-to: "Question14") ]

(link: "🌀 Nobody knows. Including her. Especially her.")[ (go-to: "Question14") ]

Scope creep. A way of life.
""")

add("Question14", "interrogation", """
QUESTION 14

Mum spots something and calls it "magic." What is it actually?

(link: "🐛 A bug. A genuinely unremarkable bug.")[ (go-to: "Question15") ]

(link: "🪨 A rock. Now emotionally significant. No further explanation offered.")[ (go-to: "Question15") ]

(link: "☁️ A cloud shaped like something only she can see")[ (go-to: "Question15") ]

(link: "✨ Nothing you can identify, and she won't clarify")[ (go-to: "Question15") ]

The fairy sighting rate remains statistically alarming.
""")

add("Question15", "interrogation", """
QUESTION 15

Mum actually decides to focus today. What happens?

(link: "🎯 Finished before anyone realises she's started")[ (go-to: "Question16") ]

(link: "📋 Terrifyingly organised. For exactly one day.")[ (go-to: "Question16") ]

(link: "👥 The whole household gets quietly recruited")[ (go-to: "Question16") ]

(link: "🏆 Done better than anyone actually asked for")[ (go-to: "Question16") ]

Focused Mum is a limited-time event. Enjoy responsibly.
""")

add("Question16", "interrogation", """
QUESTION 16

If Mum had to describe herself on a work form, she'd probably write...

(link: "“Prefers not to explain.”")[ (go-to: "Question17") ]

(link: "“Difficult to categorise.”")[ (go-to: "Question17") ]

(link: "“Results may vary.”")[ (go-to: "Question17") ]

(link: "“Ask my kids.”")[ (go-to: "Question17") ]

HR has no follow-up questions. HR is too afraid.
""")

add("Question17", "interrogation", """
QUESTION 17 / LAST ONE

Which version of Mum are you most likely to get on any given day?

(link: "⚙️ Hyper-focused and weirdly efficient")[ (go-to: "The Interrogation Is Over") ]

(link: "🌪 Creative tornado with twelve tabs open in her brain")[ (go-to: "The Interrogation Is Over") ]

(link: "🤐 Quiet, antisocial, and absolutely not available for small talk")[ (go-to: "The Interrogation Is Over") ]

(link: "🎰 Somehow all three before lunch")[ (go-to: "The Interrogation Is Over") ]

Final answer locked. There is no version 18. We checked.
""")

add("The Interrogation Is Over", "interrogation", """
THE INTERROGATION IS OVER

Okay. Enough questions.

You have now provided a completely unqualified psychological assessment of your mother.

Thank you for your service.

Before you go in, a few things worth keeping in the back of your head — not rules, just vibes:

A good name should feel strong, like she's finally stepped into herself.

It can be beautiful, with a little bit of danger underneath.

It should be unusual enough to remember, without sounding invented.

And if it's right, it should feel like it was somehow always supposed to be her name.

Now we get to the reason you're actually here.

NAME HER.

Some of these names are real contenders.

Some are wildcards.

Some may be here purely so Mum can determine whether you should ever be trusted with an important decision again.

Do not overthink it.

Do not be polite.

If you hate one, kill it.

If you love one, defend it.

And if something unexpectedly feels like her...

pay attention.

[[ENTER THE NAME PIT->Name Pit]]
""")

# ============================== THE NAME PIT ================================

add("Name Pit", "namepit", """
<div class="stage-namepit">

THE NAME PIT

Welcome to the part where feelings get hurt.

You're going to see full names, one at a time.

Your job is not to analyse them like you're naming a pharmaceutical company.

Just react.

Pick your gut response:

LOVE IT
Yep. Keep her alive.

MAYBE
Not sold, but she can stay for another round.

NOPE
Absolutely not. Remove it from my sight.

WHAT THE FUCK IS THAT?
Special category. Self-explanatory.

There are real contenders in here.

There are wildcards.

There may also be a couple of sacrificial names included purely for scientific purposes.

Twelve names. No mercy. Ready?

[[THROW ME A NAME->ZairaMareeRivers]]

</div>
""")

add("ZairaMareeRivers", "namepit", """
<div class="stage-namepit">
<span class="tag">NAME 1 OF 12</span>

# ZAIRA MAREE RIVERS
<p class="pron">Zaira — ZY-rah</p>

Bright, radiant, a little uncommon without trying too hard.

Maree — a thread back to where she came from.

Rivers — movement, change, and absolutely no intention of staying where life dumped her.

Gut reaction. No committee meeting.

(link: "🔥 OH SHIT… THIS COULD BE HER")[ (set: $LoveNames to $LoveNames + (a: "Zaira Maree Rivers")) (go-to: "RheaKristalSinclair") ]

(link: "👀 I'M LISTENING…")[ (set: $MaybeNames to $MaybeNames + (a: "Zaira Maree Rivers")) (go-to: "RheaKristalSinclair") ]

(link: "🪦 BURY IT WITH DIGNITY")[ (set: $NopeNames to $NopeNames + (a: "Zaira Maree Rivers")) (go-to: "RheaKristalSinclair") ]

(link: "🚨 WHO LET THIS NAME IN HERE?")[ (set: $WTFNames to $WTFNames + (a: "Zaira Maree Rivers")) (go-to: "RheaKristalSinclair") ]

</div>
""")

add("RheaKristalSinclair", "namepit", """
<div class="stage-namepit">
<span class="tag">NAME 2 OF 12</span>

# RHEA KRISTAL SINCLAIR
<p class="pron">Rhea — REE-ah</p>

Titan queen, mother of gods, the one who actually ran things while everyone else took the credit.

Kristal — the piece that came with her. Not left behind, just recut.

Sinclair — sharp, composed, faintly dangerous in a blazer.

Looks like she chairs the meeting. Also looks like she caused the meeting.

(link: "👑 OKAY, QUEEN")[ (set: $LoveNames to $LoveNames + (a: "Rhea Kristal Sinclair")) (go-to: "ZoraKristalForest") ]

(link: "🤏 CLOSE, BUT NOT QUITE")[ (set: $MaybeNames to $MaybeNames + (a: "Rhea Kristal Sinclair")) (go-to: "ZoraKristalForest") ]

(link: "🚫 DEMOTED IMMEDIATELY")[ (set: $NopeNames to $NopeNames + (a: "Rhea Kristal Sinclair")) (go-to: "ZoraKristalForest") ]

(link: "🤨 WHO APPROVED THIS?")[ (set: $WTFNames to $WTFNames + (a: "Rhea Kristal Sinclair")) (go-to: "ZoraKristalForest") ]

</div>
""")

add("ZoraKristalForest", "namepit", """
<div class="stage-namepit">
<span class="tag">NAME 3 OF 12</span>

# ZORA KRISTAL FOREST
<p class="pron">Zora — ZOR-ah</p>

Dawn, light, beginning again — but without sounding like she was named by a motivational poster.

Kristal — the piece that stayed. Same woman, different chapter.

Forest — grounded, wild, slightly feral, and definitely not built for neat little boxes.

Immediate verdict:

(link: "⚡ WAIT… WHY DOES THIS ACTUALLY WORK?")[ (set: $LoveNames to $LoveNames + (a: "Zora Kristal Forest")) (go-to: "MarloweRaeQuinn") ]

(link: "🧐 DON'T HATE IT. SUSPICIOUS.")[ (set: $MaybeNames to $MaybeNames + (a: "Zora Kristal Forest")) (go-to: "MarloweRaeQuinn") ]

(link: "🌲 RETURN IT TO THE FOREST")[ (set: $NopeNames to $NopeNames + (a: "Zora Kristal Forest")) (go-to: "MarloweRaeQuinn") ]

(link: "🚫 ABSOLUTELY NOT MY MOTHER")[ (set: $WTFNames to $WTFNames + (a: "Zora Kristal Forest")) (go-to: "MarloweRaeQuinn") ]

</div>
""")

add("MarloweRaeQuinn", "namepit", """
<div class="stage-namepit">
<span class="tag">NAME 4 OF 12</span>

# MARLOWE RAE QUINN
<p class="pron">Marlowe — MAR-loh</p>

Old surname turned first name. Narrator energy — the one who sees everything and says just enough.

Rae — clean, quick, no ceremony required.

Quinn — sharp-edged, faintly unbothered, refuses to be background noise.

Sounds like someone who'd solve the case and leave without explaining how.

(link: "🕶️ SHE'S GOT A WHOLE BACKSTORY NOW")[ (set: $LoveNames to $LoveNames + (a: "Marlowe Rae Quinn")) (go-to: "ZariaRaeSterling") ]

(link: "🤷 COULD GO EITHER WAY")[ (set: $MaybeNames to $MaybeNames + (a: "Marlowe Rae Quinn")) (go-to: "ZariaRaeSterling") ]

(link: "📁 CASE CLOSED. REJECTED.")[ (set: $NopeNames to $NopeNames + (a: "Marlowe Rae Quinn")) (go-to: "ZariaRaeSterling") ]

(link: "🚔 THIS ISN'T EVEN A NAME")[ (set: $WTFNames to $WTFNames + (a: "Marlowe Rae Quinn")) (go-to: "ZariaRaeSterling") ]

</div>
""")

add("ZariaRaeSterling", "namepit", """
<div class="stage-namepit">
<span class="tag">NAME 5 OF 12</span>

# ZARIA RAE STERLING
<p class="pron">Zaria — ZAR-ee-ah</p>

Bright, striking, feminine without being soft around the edges.

Rae — clean, simple, gives the name some air.

Sterling — strong, polished, valuable — but still has a bit of bite to it.

First instinct only:

(link: "✨ OKAY… SHE'S GOT SOMETHING")[ (set: $LoveNames to $LoveNames + (a: "Zaria Rae Sterling")) (go-to: "NadiaRaeWinter") ]

(link: "👀 NOT SOLD, BUT DON'T KILL HER YET")[ (set: $MaybeNames to $MaybeNames + (a: "Zaria Rae Sterling")) (go-to: "NadiaRaeWinter") ]

(link: "🪓 CUT HER FROM THE LINE-UP")[ (set: $NopeNames to $NopeNames + (a: "Zaria Rae Sterling")) (go-to: "NadiaRaeWinter") ]

(link: "🚪 NOPE. ESCORT HER OUT.")[ (set: $WTFNames to $WTFNames + (a: "Zaria Rae Sterling")) (go-to: "NadiaRaeWinter") ]

</div>
""")

add("NadiaRaeWinter", "namepit", """
<div class="stage-namepit">
<span class="tag">NAME 6 OF 12</span>

# NADIA RAE WINTER
<p class="pron">Nadia — NAH-dee-ah</p>

Means "hope," which is either extremely on the nose or extremely funny depending on the week.

Rae — light, doesn't need decoration.

Winter — cold enough to mean business, still capable of something beautiful falling out of the sky.

Elegant. Also fully capable of shutting a room down with one look.

(link: "❄️ SHE COULD ACTUALLY PULL THIS OFF")[ (set: $LoveNames to $LoveNames + (a: "Nadia Rae Winter")) (go-to: "ZeliaRaeMorrow") ]

(link: "🤔 UNDECIDED. ASK AGAIN LATER.")[ (set: $MaybeNames to $MaybeNames + (a: "Nadia Rae Winter")) (go-to: "ZeliaRaeMorrow") ]

(link: "🥶 COLD. NEXT.")[ (set: $NopeNames to $NopeNames + (a: "Nadia Rae Winter")) (go-to: "ZeliaRaeMorrow") ]

(link: "😵 ABSOLUTELY NOT. WHO IS THIS.")[ (set: $WTFNames to $WTFNames + (a: "Nadia Rae Winter")) (go-to: "ZeliaRaeMorrow") ]

</div>
""")

add("ZeliaRaeMorrow", "namepit", """
<div class="stage-namepit">
<span class="tag">NAME 7 OF 12</span>

# ZELIA RAE MORROW
<p class="pron">Zelia — ZEE-lee-ah</p>

Bright, unusual, feminine, and memorable without sounding like it escaped from a fantasy novel.

Rae — short, clean, keeps the whole name light on its feet.

Morrow — tomorrow, next chapter, what comes after.

Gut check:

(link: "⚡ OHHH… HOLD UP")[ (set: $LoveNames to $LoveNames + (a: "Zelia Rae Morrow")) (go-to: "VesperKristalWilde") ]

(link: "👀 KEEP HER AROUND")[ (set: $MaybeNames to $MaybeNames + (a: "Zelia Rae Morrow")) (go-to: "VesperKristalWilde") ]

(link: "🪦 NOT DEADLY, JUST NOT HER")[ (set: $NopeNames to $NopeNames + (a: "Zelia Rae Morrow")) (go-to: "VesperKristalWilde") ]

(link: "🚪 GET HER OUT OF HERE")[ (set: $WTFNames to $WTFNames + (a: "Zelia Rae Morrow")) (go-to: "VesperKristalWilde") ]

</div>
""")

add("VesperKristalWilde", "namepit", """
<div class="stage-namepit">
<span class="tag">NAME 8 OF 12</span>

# VESPER KRISTAL WILDE
<p class="pron">Vesper — VESS-per</p>

Evening star. The moment the sky changes and everyone finally stops talking.

Kristal — carried across, unchanged underneath the new name.

Wilde — yes, like that. Sharp, a little theatrical, entirely on purpose.

Sounds like a woman who arrives fashionably late and never apologises for it.

(link: "🌆 OKAY THAT'S ACTUALLY KIND OF ICONIC")[ (set: $LoveNames to $LoveNames + (a: "Vesper Kristal Wilde")) (go-to: "KaiaRaeMorrow") ]

(link: "🧐 SUSPICIOUSLY GOOD. WATCHING CLOSELY.")[ (set: $MaybeNames to $MaybeNames + (a: "Vesper Kristal Wilde")) (go-to: "KaiaRaeMorrow") ]

(link: "🌫️ FADE TO BLACK ON THIS ONE")[ (set: $NopeNames to $NopeNames + (a: "Vesper Kristal Wilde")) (go-to: "KaiaRaeMorrow") ]

(link: "🚫 WHO GAVE HER A STAGE NAME")[ (set: $WTFNames to $WTFNames + (a: "Vesper Kristal Wilde")) (go-to: "KaiaRaeMorrow") ]

</div>
""")

add("KaiaRaeMorrow", "namepit", """
<div class="stage-namepit">
<span class="tag">NAME 9 OF 12</span>

# KAIA RAE MORROW
<p class="pron">Kaia — KY-ah</p>

Warm, free, slightly wild. Unusual enough to stand out without needing an explanation every time you introduce yourself.

Rae — short, bright, uncomplicated.

Morrow — what comes next. Not erasing the past — just refusing to live there.

Immediate reaction:

(link: "🔥 FUCK… SHE MIGHT ACTUALLY BE SOMETHING")[ (set: $LoveNames to $LoveNames + (a: "Kaia Rae Morrow")) (go-to: "TheaRaeOsmond") ]

(link: "👀 ALRIGHT KAIA, DON'T GET COMFORTABLE")[ (set: $MaybeNames to $MaybeNames + (a: "Kaia Rae Morrow")) (go-to: "TheaRaeOsmond") ]

(link: "🫠 I SEE IT. I JUST DON'T WANT IT.")[ (set: $NopeNames to $NopeNames + (a: "Kaia Rae Morrow")) (go-to: "TheaRaeOsmond") ]

(link: "🚪 THANKS FOR COMING. LEAVE.")[ (set: $WTFNames to $WTFNames + (a: "Kaia Rae Morrow")) (go-to: "TheaRaeOsmond") ]

</div>
""")

add("TheaRaeOsmond", "namepit", """
<div class="stage-namepit">
<span class="tag">NAME 10 OF 12</span>

# THEA RAE OSMOND
<p class="pron">Thea — THEE-ah</p>

Goddess of light and sight — the one who lets everyone else actually see what's in front of them.

Rae — quiet, doesn't need backup.

Osmond — a bit unexpected, slightly old-school, oddly hard to forget.

Sounds respectable right up until you find out what she's actually been doing.

(link: "💡 OH THAT'S ANNOYINGLY GOOD")[ (set: $LoveNames to $LoveNames + (a: "Thea Rae Osmond")) (go-to: "JunoKristalHale") ]

(link: "🤨 SUSPICIOUS LEVELS OF FINE")[ (set: $MaybeNames to $MaybeNames + (a: "Thea Rae Osmond")) (go-to: "JunoKristalHale") ]

(link: "🕯️ LIGHTS OUT ON THIS ONE")[ (set: $NopeNames to $NopeNames + (a: "Thea Rae Osmond")) (go-to: "JunoKristalHale") ]

(link: "🚨 WHO INVITED HER")[ (set: $WTFNames to $WTFNames + (a: "Thea Rae Osmond")) (go-to: "JunoKristalHale") ]

</div>
""")

add("JunoKristalHale", "namepit", """
<div class="stage-namepit">
<span class="tag">NAME 11 OF 12</span>

# JUNO KRISTAL HALE
<p class="pron">Juno — JOO-noh</p>

Queen of the gods. Ran the whole operation and was permanently unimpressed by everyone in it.

Kristal — the one piece nobody voted to remove.

Hale — sturdy, capable, built to outlast whatever comes next.

The kind of name that ends arguments just by entering the room.

(link: "👑 SHE WOULD RULE, HONESTLY")[ (set: $LoveNames to $LoveNames + (a: "Juno Kristal Hale")) (go-to: "RomyMareeCalder") ]

(link: "🤷 JURY'S STILL OUT")[ (set: $MaybeNames to $MaybeNames + (a: "Juno Kristal Hale")) (go-to: "RomyMareeCalder") ]

(link: "⚰️ OVERTHROWN. NEXT.")[ (set: $NopeNames to $NopeNames + (a: "Juno Kristal Hale")) (go-to: "RomyMareeCalder") ]

(link: "🚫 ABSOLUTELY NOT MY MOTHER'S ENERGY")[ (set: $WTFNames to $WTFNames + (a: "Juno Kristal Hale")) (go-to: "RomyMareeCalder") ]

</div>
""")

add("RomyMareeCalder", "namepit", """
<div class="stage-namepit">
<span class="tag">NAME 12 OF 12 — LAST ONE</span>

# ROMY MAREE CALDER
<p class="pron">Romy — ROH-mee</p>

Warm, a little retro, impossible to say without sounding fond of her.

Maree — the same thread that's followed her the whole way through.

Calder — the sculptor who made things move for a living. Fitting, for someone who was never going to sit still.

Sounds soft. Is absolutely not soft.

(link: "🥹 OKAY WAIT I ACTUALLY LOVE THIS")[ (set: $LoveNames to $LoveNames + (a: "Romy Maree Calder")) (go-to: "CasualtyReport") ]

(link: "🧐 GROWING ON ME, SUSPICIOUSLY")[ (set: $MaybeNames to $MaybeNames + (a: "Romy Maree Calder")) (go-to: "CasualtyReport") ]

(link: "👋 THANKS, NEXT")[ (set: $NopeNames to $NopeNames + (a: "Romy Maree Calder")) (go-to: "CasualtyReport") ]

(link: "🚫 WHO EVEN IS SHE")[ (set: $WTFNames to $WTFNames + (a: "Romy Maree Calder")) (go-to: "CasualtyReport") ]

</div>
""")

# ============================== TOURNAMENT ================================

add("CasualtyReport", "knockout", """
<div class="stage-knockout">
<span class="tag">CASUALTY REPORT</span>

# THE CASUALTY REPORT

Twelve names went into the pit. Several have been lost in the line of duty.

**LOVED**

(if: $LoveNames's length is 0)[Nobody. Not one. Devastating.]
(else:)[<div class="card">(for: each _n, ...$LoveNames)[_n<br>]</div>]

**MAYBE (survived on a technicality)**

(if: $MaybeNames's length is 0)[Nobody sat on the fence. Bold of you.]
(else:)[<div class="card">(for: each _n, ...$MaybeNames)[_n<br>]</div>]

**SENT DIRECTLY TO HELL**

(if: ($NopeNames's length + $WTFNames's length) is 0)[Nobody. You loved everyone. Suspicious.]
(else:)[<div class="card">(for: each _n, ...$NopeNames)[_n<br>](for: each _n, ...$WTFNames)[_n<br>]</div>]

Rest in pieces. We are not revisiting them.

[[SEE WHO'S LEFT STANDING->Survivors]]
</div>
""")

add("Survivors", "knockout", """
<div class="stage-knockout">
(set: $Bracket to $LoveNames + $MaybeNames)
(set: $NextRoundResults to (a:))
(if: $Bracket's length is 0)[

# EVERYONE'S DEAD

All twelve. Every single one.

This is either impressively decisive or deeply concerning. Possibly both.

There is no bracket. There is no field. There is only you, and what you're about to do next.

[[FINE. WE'LL DO THIS THE HARD WAY->NobodySurvived]]

](else-if: $Bracket's length <= 3)[
(set: $Finalists to $Bracket)

# NOT ENOUGH FOR A BRACKET

Not enough carnage here for a proper knockout. These names go straight through to the final round.

<div class="card">(for: each _n, ...$Bracket)[_n<br>]</div>

[[STRAIGHT TO THE WILDCARD->WildcardResurrection]]

](else:)[

# THE SURVIVORS

(print: $Bracket's length) names made it out of the pit alive-ish. That's too many for a clean final round.

Time for a bracket.

TWO NAMES ENTER. ONE MUM LEAVES.

[[BEGIN THE KNOCKOUT->HeadToHead]]
]
</div>
""")

add("HeadToHead", "knockout", """
<div class="stage-knockout">
<span class="tag">HEAD TO HEAD</span>
(set: _first to $Bracket's 1st)
(set: _second to $Bracket's 2nd)
(set: _firstInfo to $CandidateInfo's (_first))
(set: _secondInfo to $CandidateInfo's (_second))

# TWO NAMES ENTER. ONE MUM LEAVES.

<div class="card">**(print: _first)**<br><span class="pron">(print: _firstInfo's pron)</span></div>

<p class="vs">VERSUS</p>

<div class="card">**(print: _second)**<br><span class="pron">(print: _secondInfo's pron)</span></div>

(link: "👉 KEEP " + _first)[
(set: $NextRoundResults to $NextRoundResults + (a: _first))
(if: $Bracket's length > 2)[(set: $Bracket to (subarray: $Bracket, 3, $Bracket's length))](else:)[(set: $Bracket to (a:))]
(if: $Bracket's length is 1)[(set: $NextRoundResults to $NextRoundResults + (a: $Bracket's 1st))(set: $Bracket to (a:))]
(if: $Bracket's length is 0)[(go-to: "RoundComplete")](else:)[(go-to: "HeadToHead")]
]

(link: "👉 KEEP " + _second)[
(set: $NextRoundResults to $NextRoundResults + (a: _second))
(if: $Bracket's length > 2)[(set: $Bracket to (subarray: $Bracket, 3, $Bracket's length))](else:)[(set: $Bracket to (a:))]
(if: $Bracket's length is 1)[(set: $NextRoundResults to $NextRoundResults + (a: $Bracket's 1st))(set: $Bracket to (a:))]
(if: $Bracket's length is 0)[(go-to: "RoundComplete")](else:)[(go-to: "HeadToHead")]
]
</div>
""")

add("RoundComplete", "knockout", """
<div class="stage-knockout">
(if: $NextRoundResults's length <= 3)[
(set: $Finalists to $NextRoundResults)

# THAT ROUND'S DONE

(print: $Finalists's length) name(s) still standing:

<div class="card">(for: each _n, ...$Finalists)[_n<br>]</div>

[[ON TO THE WILDCARD->WildcardResurrection]]

](else:)[

# ROUND COMPLETE

(print: $NextRoundResults's length) still standing. Not low enough yet. Another round.

<div class="card">(for: each _n, ...$NextRoundResults)[_n<br>]</div>

(link: "NEXT ROUND")[
(set: $Bracket to $NextRoundResults)
(set: $NextRoundResults to (a:))
(go-to: "HeadToHead")
]
]
</div>
""")

add("NobodySurvived", "knockout", """
<div class="stage-knockout">
# NOBODY SURVIVED

Every single name got a Nope or a WTF. Impressive work.

Since you hated everyone equally, you don't get a vote between finalists. You get exactly one move: fix it yourself.

(link: "🪦 RESCUE ONE FROM THE GRAVE")[ (go-to: "WildcardRescue") ]

(link: "✍️ NAME HER YOURSELF")[ (go-to: "WildcardInvent") ]
</div>
""")

# ============================== WILDCARD ================================

add("WildcardResurrection", "knockout", """
<div class="stage-knockout">
# THE WILDCARD

Here's who's still standing:

<div class="card">(for: each _n, ...$Finalists)[_n<br>]</div>

You get ONE wildcard. Use it to rescue a name from the pile of shame, or name her yourself. Or don't — the survivors can speak for themselves.

(link: "🪦 RESCUE ONE FROM THE GRAVE")[ (go-to: "WildcardRescue") ]

(link: "✍️ NAME HER YOURSELF")[ (go-to: "WildcardInvent") ]

(link: "🙅 NAH, THE SURVIVORS SPEAK FOR THEMSELVES")[ (go-to: "FinalThree") ]
</div>
""")

add("WildcardRescue", "knockout", """
<div class="stage-knockout">
(set: _pool to $NopeNames + $WTFNames)
(if: _pool's length is 0)[

# NOTHING TO RESCUE

Nobody actually died in the pit. There's no grave to dig up.

[[FINE, I'LL WRITE ONE MYSELF->WildcardInvent]]

](else:)[

# THE GRAVE

Pick one name to drag back from the dead.

(for: each _n, ..._pool)[(link: _n)[ (set: $Finalists to $Finalists + (a: _n)) (set: $WildcardUsed to true) (set: $WildcardName to _n) (set: $WildcardSource to "rescued") (go-to: "FinalThree") ]]
]
</div>
""")

add("WildcardInvent", "knockout", """
<div class="stage-knockout">
# NAME HER YOURSELF

You've known Mum longer than this game has.

First name:

(input-box: bind $CustomFirst, "e.g. Nadia", 1)

Middle name (optional):

(input-box: bind $CustomMiddle, "optional", 1)

Surname (optional):

(input-box: bind $CustomSurname, "optional", 1)

Stuck? (link: "NEED INSPIRATION?")[ (go-to: "NameHelp") ]

(link: "THAT'S HER")[
(if: $CustomFirst is "")[
(replace: ?wildwarning)[Nice try. She needs at least a first name.]
](else:)[
(set: _full to $CustomFirst)
(if: $CustomMiddle is not "")[(set: _full to _full + " " + $CustomMiddle)]
(if: $CustomSurname is not "")[(set: _full to _full + " " + $CustomSurname)]
(set: $CustomFullName to _full)
(set: $Finalists to $Finalists + (a: $CustomFullName))
(set: $WildcardUsed to true)
(set: $WildcardName to $CustomFullName)
(set: $WildcardSource to "invented")
(go-to: "FinalThree")
]
]

|wildwarning>[]
</div>
""")

add("NameHelp", "knockout", """
<div class="stage-knockout">
# NAME EMERGENCY 🚨

Your imagination has apparently left the building.

Pick a vibe and the machine will throw you a few ideas.

(link: "🌿 EARTHY")[ (set: $HelpVibe to "Earthy") (go-to: "NameHelpResults") ]

(link: "🔥 BOLD")[ (set: $HelpVibe to "Bold") (go-to: "NameHelpResults") ]

(link: "🌙 DARK")[ (set: $HelpVibe to "Dark") (go-to: "NameHelpResults") ]

(link: "✨ WEIRD BUT GOOD")[ (set: $HelpVibe to "Weird") (go-to: "NameHelpResults") ]

(link: "💎 GROWN-UP")[ (set: $HelpVibe to "Grown") (go-to: "NameHelpResults") ]

(link: "🌊 FLOWING")[ (set: $HelpVibe to "Flowing") (go-to: "NameHelpResults") ]

(link: "🎲 SURPRISE ME")[ (set: $HelpVibe to "Surprise") (go-to: "NameHelpResults") ]

We cannot promise taste. Only options.
</div>
""")

add("NameHelpResults", "knockout", """
<div class="stage-knockout">
# HERE. HAVE SOME NAMES.

(if: $HelpVibe is "Earthy")[Sienna. Mara. Willow. Rowan.]
(else-if: $HelpVibe is "Bold")[Zora. Maeve. Rhea. Juno.]
(else-if: $HelpVibe is "Dark")[Vesper. Maren. Raine. Thea.]
(else-if: $HelpVibe is "Weird")[Lyra. Vega. Riva. Marlowe.]
(else-if: $HelpVibe is "Grown")[Vera. Nadia. Romy. Sasha.]
(else-if: $HelpVibe is "Flowing")[Zaira. Maren. Mira. Kaia.]
(else:)[Zaira. Rae. Lyra. Mara.]

Steal one. Change one. Mash two together. Or ignore the lot because apparently you know better.

[[BACK TO NAMING MUM->WildcardInvent]]
</div>
""")

# ============================== FINAL THREE / VOTE / RESULT ================================

add("FinalThree", "finalvote", """
<div class="stage-finalvote">
(if: $Finalists's length is 1)[(set: $FinalHeadline to "THE ONLY ONE LEFT STANDING")]
(else-if: $Finalists's length is 2)[(set: $FinalHeadline to "THE FINAL TWO")]
(else-if: $Finalists's length is 3)[(set: $FinalHeadline to "THE FINAL THREE")]
(else:)[(set: $FinalHeadline to "THE FINAL FEW")]

# (print: $FinalHeadline)

(for: each _n, ...$Finalists)[
<div class="card">

**(print: _n)**

(if: _n is $WildcardName and $WildcardSource is "invented")[
<span class="pron">however you want to say it — you made her up</span>

She's here because nobody else was going to do it, apparently.
](else:)[
(set: _info to $CandidateInfo's (_n))
<span class="pron">(print: _info's pron)</span>

(print: _info's vibe)

(if: _n is $WildcardName and $WildcardSource is "rescued")[Executed once. Resurrected out of spite, or love. Hard to tell with this family.]
(else-if: $LoveNames contains _n)[The votes were in before you'd finished reading it.]
(else-if: $MaybeNames contains _n)[Nobody hated it enough to kill it. That's basically a victory around here.]
(else:)[Survived a bracket. Nobody expected that either.]
]
</div>
]

Curious whether any of these line up with anything real? (link: "🔢 NUMEROLOGY CHECK (OPTIONAL)")[ (go-to: "NumerologyHook") ]

[[NAME THE WOMAN->FinalVoteSpeech]]
</div>
""")

add("NumerologyHook", "finalvote", """
<div class="stage-finalvote">
# NUMEROLOGY: A PLACEHOLDER, NOT A PROPHECY

Here's the honest version: there's a real numerology target for Mum's eventual legal name, and it's supposed to land on the number 8.

Calculating that properly needs her actual full birth details, and this game isn't going to guess at those or invent numbers just to sound clever.

So consider this a marked spot for later — a proper numerology pass on the real shortlist, done properly, outside of a kids' phone game.

Gut feeling first. Maths later. That was always the deal.

[[BACK TO THE FINALISTS->FinalThree]]
</div>
""")

add("FinalVoteSpeech", "finalvote", """
<div class="stage-finalvote">
# ALRIGHT, CHILDREN.

You have known her your whole life.

You have judged her personality.

Insulted several perfectly innocent names.

Killed others without trial.

And somehow we are still trusting you.

NAME THE WOMAN.

[[I'M READY->FinalVoteChoice]]
</div>
""")

add("FinalVoteChoice", "finalvote", """
<div class="stage-finalvote">
# THE VOTE

Pick one. There's no take-backs button. There is, however, a Play Again button, so the stakes are moderate.

(for: each _n, ...$Finalists)[(link: _n)[ (set: $WinnerName to _n) (go-to: "FinalReason") ]]
</div>
""")

add("FinalReason", "finalvote", """
<div class="stage-finalvote">
# WHY THIS ONE?

Optional. Roast, explanation, heartfelt essay, or "dunno, it just suits you" all accepted.

(input-box: bind $FinalReason, "type your reason (or don't)", 4)

(link: "LOCK IT IN 🔒")[
(if: $FinalReason is "")[(set: $FinalReason to "No reason supplied. Apparently vibes were sufficient.")]
(go-to: "Result")
]
</div>
""")

add("Result", "result", """
<div class="stage-result">
(if: $ChildName is "Connor")[(set: $ResultHeading to "CONNOR'S FINAL RULING")]
(else-if: $ChildName is "Grace")[(set: $ResultHeading to "GRACE'S VERDICT")]
(else-if: $ChildName is "Hunter")[(set: $ResultHeading to "HUNTER HAS DECIDED")]
(else-if: $ChildName is "Avs")[(set: $ResultHeading to "AVS HAS SPOKEN")]
(else-if: $ChildName is "Harry")[(set: $ResultHeading to "HARRY HAS SPOKEN")]
(else:)[(set: $ResultHeading to "THE VERDICT")]

# (print: $ResultHeading)

## (print: $WinnerName)

(if: $WildcardUsed and $WinnerName is $WildcardName)[
(if: $WildcardSource is "invented")[This one wasn't even in the pit. (print: $ChildName) made her up from scratch.]
(else:)[This one was rescued from the Nope pile using the game's one wildcard.]
](else-if: $WildcardUsed)[
The wildcard, (print: $WildcardName), got used but didn't win in the end. Democracy, etc.
]

**Why:** (print: $FinalReason)

Mum's archetype for the record: **(print: $MumArchetype)**

(either: "CERTAINTY LEVEL: Extremely.", "CERTAINTY LEVEL: Ask again in six months.", "CERTAINTY LEVEL: Higher than expected, honestly.", "CERTAINTY LEVEL: Somewhere between “obviously” and “we'll see”.")

---

Want to save this so Mum can compare it against the other four verdicts?

<textarea class="resultbox" readonly>(print: $ResultHeading) — Winner: (print: $WinnerName). Reason: (print: $FinalReason). Mum's archetype: (print: $MumArchetype).</textarea>

<button class="copybtn" onclick="copyResultText(this)">COPY RESULT</button>

Or just screenshot this screen. That works too.

[[PLAY AGAIN->Start]]
</div>
""")

print(f"Prepared {len(P)} total passages")

# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------
names = [p[0] for p in P]
name_set = set(names)
errors = []

dupes = set(n for n in names if names.count(n) > 1)
if dupes:
    errors.append(f"DUPLICATE PASSAGE NAMES: {dupes}")

for name, tags, content in P:
    if not content.strip():
        errors.append(f"EMPTY PASSAGE: {name}")
    if len(content.strip()) < 5:
        errors.append(f"SUSPICIOUSLY SHORT PASSAGE: {name}")

link_pattern = re.compile(r'\[\[(?:[^\]|]*?->)?([^\]|]+?)\]\]')
goto_pattern = re.compile(r'\(go-?to:\s*"([^"]+)"\)')

all_targets = {}
for name, tags, content in P:
    targets = set(link_pattern.findall(content)) | set(goto_pattern.findall(content))
    all_targets[name] = targets
    for t in targets:
        if t not in name_set:
            errors.append(f"BROKEN LINK in '{name}' -> '{t}' (no such passage)")

# reachability check from Start
from collections import deque
reachable = set()
q = deque(["Start"])
while q:
    cur = q.popleft()
    if cur in reachable:
        continue
    reachable.add(cur)
    for t in all_targets.get(cur, ()):
        if t not in reachable:
            q.append(t)

orphans = name_set - reachable
if orphans:
    errors.append(f"UNREACHABLE FROM START: {orphans}")

forbidden = ["Sabine", "Astrid", "Veya", "Zara"]
for name, tags, content in P:
    for f in forbidden:
        if re.search(r'\b' + re.escape(f) + r'\b', content) and f != "Zara":
            errors.append(f"FORBIDDEN NAME '{f}' found in passage '{name}'")
        if f == "Zara" and re.search(r'\bZara\b', content):
            errors.append(f"FORBIDDEN NAME '{f}' found in passage '{name}'")

for name, tags, content in P:
    o, c = content.count("("), content.count(")")
    if o != c:
        errors.append(f"PAREN MISMATCH in '{name}': {o} open vs {c} close")
    o2, c2 = content.count("["), content.count("]")
    if o2 != c2:
        errors.append(f"BRACKET MISMATCH in '{name}': {o2} open vs {c2} close")

if errors:
    print("\n".join(errors))
    print(f"\n{len(errors)} VALIDATION ISSUE(S) FOUND")
else:
    print("VALIDATION CLEAN: no broken links, no empty passages, no orphans, no forbidden names, brackets balanced")

# ---------------------------------------------------------------------------
# Assemble final HTML
# ---------------------------------------------------------------------------
with open(SRC, encoding="utf-8") as f:
    original = f.read()

m = re.search(r'<tw-storydata\b[^>]*>', original)
storydata_open_original = m.group(0)
head = original[:m.start()]
tail = original[original.index("</tw-storydata>") + len("</tw-storydata>"):]

# rebuild the opening tag, keep same attrs, same ifid, bump nothing else
storydata_open = storydata_open_original  # unchanged: startnode=1 still valid (Start keeps pid 1)

pid_lookup = {name: str(i + 1) for i, (name, tags, content) in enumerate(P)}

parts = [storydata_open]
parts.append(f'<style role="stylesheet" id="twine-user-stylesheet" type="text/twine-css">{CSS}</style>')
parts.append(f'<script role="script" id="twine-user-script" type="text/twine-javascript">{JS}</script>')

cols = 6
for i, (name, tags, content) in enumerate(P):
    pid = pid_lookup[name]
    x = 100 + (i % cols) * 220
    y = 100 + (i // cols) * 160
    esc_name = html.escape(name, quote=True)
    esc_tags = html.escape(tags, quote=True)
    esc_content = html.escape(content, quote=True)
    parts.append(
        f'<tw-passagedata pid="{pid}" name="{esc_name}" tags="{esc_tags}" '
        f'position="{x},{y}" size="100,100">{esc_content}</tw-passagedata>'
    )
parts.append('</tw-storydata>')

final_html = head + "".join(parts) + tail

with open(OUT, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"\nWrote {OUT} ({len(final_html)} bytes)")
