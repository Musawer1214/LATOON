# -*- coding: utf-8 -*-
"""Can Machines Think? script v1 (2026-10-18). Single source for script.json, script_en.md and dub/*.json.
Each line: id, chapter, EN text, visual note (language-neutral), claim ids (FACTCHECK.md), UR, PS.
Numbers in UR/PS are digits on purpose (STYLE_GUIDE: figures may stay digits; easier to read aloud)."""

CHAPTERS = [
    ("C0", "Cold Open", "0:00"),
    ("C1", "The Question He Refused (1950)", None),
    ("C2", "The Countess's Objection (1843)", None),
    ("C3", "Move 37 (1997-2016)", None),
    ("C4", "The Room (1980)", None),
    ("C5", "A Board Inside the Machine (2022-2023)", None),
    ("C6", "The Test Is Passed (2025-2026)", None),
    ("C7", "Thinking Is Not Feeling", None),
    ("C8", "What Would Change Your Mind?", None),
]

# pause after line (s): default 0.5; chapter end 1.4; weighty 1.0
L = [{'id': 'C0-01',
  'ch': 'C0',
  'pause': 0.4,
  'en': 'Imagine your phone buzzes. Two chats open side by side. One is a real person, a student in Lahore. The other is a machine. You have five minutes to find the human.',
  'vis': 'HOOK_PRE motion in frame 1: Map Warm paper desk, a phone (2D, semi-real, soft shadow) slides in; screen splits into two chat panes with abstract message bubbles (no '
         "readable text), labels 'A' / 'B'; a 5:00 countdown ring draws on. Camera pushes into the split.",
  'layer': '2D',
  'src': [],
  'ur': 'سوچیں آپ کا فون بجتا ہے۔ دو chats ساتھ ساتھ کھلتی ہیں۔ ایک میں اصلی انسان ہے، لاہور کا ایک student۔ دوسری میں ایک machine۔ آپ کے پاس پانچ منٹ ہیں، انسان کو پہچانیں۔',
  'ps': 'فرض کړئ ستاسو فون بجیږي۔ دوه chats څنګ په څنګ پرانستل شي۔ په یو کښې ریښتینے انسان دے، د لاهور یو student۔ په بل کښې یوه machine۔ تاسو سره پنځه منټه دي، انسان پیدا کړئ۔'},
 {'id': 'C0-02',
  'ch': 'C0',
  'en': 'In 2025, researchers in San Diego ran this game for real, with hundreds of people. An AI told to play a shy young person who uses slang was picked as the human '
        'seventy-three percent of the time.',
  'vis': "Camera pulls back from the phone onto a canvas grid of many small phone icons (hundreds of games); one pane glows with a SIGNAL RED persona tag 'PERSONA'; big numeral "
         "'73%' counts up (Inter Black). Source tag: Jones & Bergen, PNAS 2026.",
  'layer': '2D',
  'src': ['F1', 'F2'],
  'ur': '2025 میں San Diego کے researchers نے یہ کھیل سچ مچ کھیلا، سینکڑوں لوگوں کے ساتھ۔ ایک AI، جسے slang بولنے والا شرمیلا نوجوان بننے کو کہا گیا، 73 فیصد بار انسان سمجھا گیا۔',
  'ps': 'په 2025 کښې د San Diego researchers دا لوبه په ریښتیا وکړه، د سلګونو خلقو سره۔ یو AI، چې ورته ووئیلے شو د slang ویونکي شرمیندوکي ځوان په شان شي، په 73 فیصده کښې انسان '
        'وګڼلے شو۔'},
 {'id': 'C0-03',
  'ch': 'C0',
  'pause': 0.9,
  'en': 'Seventy-three percent. More often than the real humans it was up against.',
  'vis': "Two bars draw on side by side: 'AI 73%' vs 'HUMAN 27%' (the human witness's share in those games); 50% chance line as a dashed INK2 rule. Hold.",
  'layer': '2D',
  'src': ['F2'],
  'ur': '73 فیصد۔ ان اصلی انسانوں سے بھی زیادہ جن کے مقابلے میں یہ تھا۔',
  'ps': '73 فیصده۔ د هغه ریښتینو انسانانو نه هم زیات چې ورسره یې مقابله وه۔'},
 {'id': 'C0-04',
  'ch': 'C0',
  'pause': 0.8,
  'en': 'So, does it think? The man who invented this test would not have answered you. He called that question "too meaningless to deserve discussion."',
  'vis': 'Match cut: the dashed 50% line becomes a typewriter line on a 1950 journal page (Mind, Vol. LIX) as a paper prop; credited archival portrait of Alan Turing (Commons, '
         "licence at build) fades in at left; quote card in Cormorant: 'too meaningless to deserve discussion' + tag 'Turing, Mind, 1950'.",
  'layer': 'photo+2D',
  'src': ['T3'],
  'ur': 'تو کیا یہ سوچتی ہے؟ جس شخص نے یہ test بنایا، وہ آپ کو جواب ہی نہ دیتا۔ اس نے اس سوال کو کہا تھا: اتنا بے معنی کہ بحث کے لائق ہی نہیں۔',
  'ps': 'نو آیا دا سوچ کوي؟ چا چې دا test جوړ کړو، هغه به تاسو ته جواب هم نه وو درکړے۔ هغه دې سوال ته ووئیل: دومره بې معنې چې د بحث قابل نه دے۔'},
 {'id': 'C0-05',
  'ch': 'C0',
  'pause': 1.4,
  'en': 'Today: the long argument over that question, from 1843 to now, and what it would actually take to know.',
  'vis': 'Fast four-beat strip across one wide canvas, camera gliding left to right: Lovelace portrait (PD) / Kasparov at the board (licensed) / ink cutaway of a sealed room / an '
         "8x8 Othello board whose discs flip on their own. Pull out to wide; TITLE CARD 'CAN MACHINES THINK?' (Playfair caps) with BRASS 'BIG QUESTIONS' badge. Bed hit.",
  'layer': 'photo+2D',
  'src': [],
  'ur': 'آج: اس سوال پر لمبی بحث، 1843 سے آج تک، اور یہ کہ جاننے کے لیے اصل میں کیا چاہیے۔',
  'ps': 'نن: په دې سوال اوږده بحث، د 1843 نه تر نن پورې، او دا چې د پوهیدو دپاره په اصل کښې څه پکار دي۔'},
 {'id': 'C1-01',
  'ch': 'C1',
  'en': 'Manchester, 1950. Alan Turing, by then programming the Manchester computer, publishes a paper in the journal Mind. Its first line: "I propose to consider the question, '
        '\'Can machines think?\'"',
  'vis': "Chapter tag '1950'. Credited archival photo of the Manchester computer (Ferranti Mark 1 / Manchester Mark 1; Commons or Univ. of Manchester, licence at build) with slow "
         'Parallax push; the Mind title page as a paper card slides in; first line types on in Nimbus Mono (quoted, English term text).',
  'layer': 'photo+2D',
  'src': ['T1', 'T9'],
  'ur': 'Manchester، 1950۔ Alan Turing، جو تب Manchester computer پر کام کر رہے تھے، journal Mind میں ایک paper چھاپتے ہیں۔ پہلی line: میں یہ سوال اٹھانا چاہتا ہوں، کیا machines '
        'سوچ سکتی ہیں؟',
  'ps': 'Manchester، 1950۔ Alan Turing، چې هغه وخت یې په Manchester computer کار کولو، په journal Mind کښې یو paper چاپوي۔ اوله line: زه غواړم دا سوال راپورته کړم، آیا machines '
        'سوچ کولے شي؟'},
 {'id': 'C1-02',
  'ch': 'C1',
  'en': 'Then he refuses to define the words. If "think" means whatever people commonly mean by it, he wrote, the answer would have to come from something like a Gallup poll. '
        '"But this is absurd."',
  'vis': "The words 'MACHINE' and 'THINK' lift off the page; a 1950s-style poll ballot box (2D, BRASS) draws on and fills with tick slips, then a SIGNAL RED line strikes through "
         "it ('absurd' beat).",
  'layer': '2D',
  'src': ['T2'],
  'ur': 'پھر وہ لفظوں کی definition دینے سے انکار کر دیتے ہیں۔ لکھا، اگر سوچنے کا مطلب وہی ہے جو عام لوگ لیتے ہیں، تو جواب کسی Gallup poll سے نکالنا پڑے گا۔ اور یہ تو فضول بات '
        'ہے۔',
  'ps': 'بیا هغه د لفظونو definition ورکولو نه انکار کوي۔ ولیکل، که د سوچ مطلب هغه وي چې عام خلق یې اخلي، نو جواب به د Gallup poll نه راباسو۔ او دا خو بې کاره خبره ده۔'},
 {'id': 'C1-03',
  'ch': 'C1',
  'en': 'He swaps the question for a game. An interrogator types questions to two hidden players and must tell which is which. First a man and a woman; then Turing asks, what if '
        'a machine takes one seat?',
  'vis': "ONE CANVAS: Manim 3D cutaway of three rooms (ThreeDScene, slow orbit), connected by a teleprinter line; labels 'A', 'B', 'C' (Turing's own letters). Camera zooms into "
         'room A; a figure silhouette dissolves into a small machine cabinet (ink, semi-real, no robot).',
  'layer': '3D',
  'src': ['T4'],
  'ur': 'وہ سوال کی جگہ ایک کھیل رکھ دیتے ہیں۔ ایک سوال کرنے والا دو چھپے کھلاڑیوں سے type کر کے سوال پوچھتا ہے اور اسے بتانا ہے کون کون ہے۔ پہلے ایک مرد اور ایک عورت؛ پھر Turing '
        'پوچھتے ہیں، اگر ایک کرسی پر machine بیٹھ جائے تو؟',
  'ps': 'هغه د سوال پر ځائے یوه لوبه کیږدي۔ یو پوښتونکے د دوو پټو لوبغاړو نه په type سوالونه کوي او باید ووائي څوک څوک دے۔ اول یو سړے او یوه ښځه؛ بیا Turing تپوس کوي، که په یوه '
        'چوکۍ machine کیني نو بیا؟'},
 {'id': 'C1-04',
  'ch': 'C1',
  'en': 'He called it the imitation game; we call it the Turing test. And he bet that in about fifty years, an average interrogator would have no more than a seventy percent '
        'chance of spotting the machine after five minutes.',
  'vis': "Label swap on the rooms: 'IMITATION GAME' -> 'TURING TEST'. A timeline ruler draws on along the canvas floor: '1950' ... '2000'; two stamps pop softly at 2000: '70%' "
         "and '5 MIN'. Camera follows the ruler right.",
  'layer': '3D+2D',
  'src': ['T3'],
  'ur': 'انہوں نے اسے imitation game کہا؛ ہم اسے Turing test کہتے ہیں۔ اور شرط لگائی کہ تقریباً پچاس سال میں، پانچ منٹ کے بعد ایک عام سوال کرنے والے کا machine پہچاننے کا chance '
        '70 فیصد سے زیادہ نہیں ہوگا۔',
  'ps': 'هغه دې ته imitation game ووئیل؛ مونږ ورته Turing test وایو۔ او شرط یې وتړله چې تقریباً په پنځوس کالو کښې، د پنځه منټو نه پس به د عام پوښتونکي د machine پیژندلو chance د '
        '70 فیصده نه زیات نه وي۔'},
 {'id': 'C1-05',
  'ch': 'C1',
  'en': 'Notice: he didn\'t bet that machines would think. He bet that by the end of the century, people would talk of machines thinking "without expecting to be contradicted." A '
        'prediction about machines, and about us.',
  'vis': "Zoom out from the '2000' stamp: the ruler bends into a speech balloon over a crowd silhouette (warm umber ink); quote card 'without expecting to be contradicted' "
         '(Cormorant). A small mirror icon: machine on one side, people on the other.',
  'layer': '2D',
  'src': ['T3'],
  'ur': 'غور کریں: انہوں نے یہ شرط نہیں لگائی کہ machines سوچیں گی۔ شرط یہ تھی کہ صدی کے آخر تک لوگ machines کے سوچنے کی بات کریں گے اور کوئی ٹوکے گا نہیں۔ یہ machines کے بارے '
        'میں بھی پیشگوئی ہے، اور ہمارے بارے میں بھی۔',
  'ps': 'غور وکړئ: هغه دا شرط نه وه تړلې چې machines به سوچ کوي۔ شرط دا وه چې د صدۍ تر آخره به خلق د machines د سوچ خبره کوي او هیڅوک به یې نه ټوکي۔ دا د machines په باره کښې هم '
        'وړاندوینه ده، او زمونږ په باره کښې هم۔'},
 {'id': 'C1-06',
  'ch': 'C1',
  'en': 'He even noted that we already run this test on each other: the viva voce, the spoken exam that finds out whether someone really understands, or has "learnt it parrot '
        'fashion."',
  'vis': "Cut on the canvas to an exam room (2D semi-real, warm light): examiner and student at a desk, label 'VIVA VOCE'; a small ink parrot perches on the student's notes on "
         "'parrot fashion'.",
  'layer': '2D',
  'src': ['T5'],
  'ur': 'انہوں نے یہ بھی لکھا کہ یہ test ہم ایک دوسرے پر پہلے سے کرتے ہیں: viva voce، وہ زبانی امتحان جو بتاتا ہے کہ کسی کو سچ میں سمجھ آئی ہے، یا اس نے طوطے کی طرح رٹ لیا ہے۔',
  'ps': 'هغه دا هم ولیکل چې دا test مونږ مخکښې نه په یو بل کوو: viva voce، هغه زباني امتحان چې ښائي یو څوک په ریښتیا پوهه دے، که یې د طوطي غوندې یاد کړي دي۔'},
 {'id': 'C1-07',
  'ch': 'C1',
  'en': "If you've sat a viva in Peshawar or Lahore, you know the move: the examiner digs until it's clear which one you are. We even have a word for learning parrot fashion: "
        'ratta. Keep that word in mind.',
  'vis': "Small map inset of Pakistan (LAND GREEN, accurate outline) with two dots: Peshawar, Lahore. Back to the exam room: the examiner's question marks stack up. On 'ratta' "
         "the label 'RATTA' (Latin letters) stamps on the parrot's notebook; it stays pinned at a canvas corner as a callback object.",
  'layer': '2D',
  'src': ['L1'],
  'ur': 'اگر آپ نے پشاور یا لاہور میں viva دیا ہے، تو آپ جانتے ہیں: examiner کریدتا رہتا ہے جب تک صاف نہ ہو جائے کہ آپ کون سے والے ہیں۔ طوطے کی طرح یاد کرنے کا ہمارے پاس لفظ بھی '
        'ہے: رٹا۔ یہ لفظ یاد رکھیں۔',
  'ps': 'که تاسو په پېښور یا لاهور کښې viva ورکړې وي، نو تاسو ته معلومه ده: examiner کنستل کوي تر هغې چې صفا شي تاسو کوم یئ۔ د طوطي غوندې یادولو دپاره زمونږ سره لفظ هم شته: رټا۔ '
        'دا لفظ یاد ساتئ۔'},
 {'id': 'C1-08',
  'ch': 'C1',
  'pause': 1.4,
  'en': 'But first, Turing had to answer an objection written a hundred and seven years earlier.',
  'vis': "The timeline ruler rewinds leftward fast past '1900' and stops at '1843' (re-hook). Pages flutter.",
  'layer': '2D',
  'src': ['T6', 'T8'],
  'ur': 'لیکن پہلے Turing کو ایک اعتراض کا جواب دینا تھا، جو 107 سال پہلے لکھا گیا تھا۔',
  'ps': 'خو مخکښې Turing له یو اعتراض ته جواب ورکول وو، چې 107 کاله مخکښې لیکلے شوے وو۔'},
 {'id': 'C2-01',
  'ch': 'C2',
  'en': "London, 1843. Ada Lovelace publishes long notes on Charles Babbage's Analytical Engine, a steam-powered computer he designed but never completed.",
  'vis': "Chapter tag '1843'. Lovelace portrait (Chalon c.1840, public domain) as a credited photo card; Manim 3D: a brass-and-gear column of the Analytical Engine (accurate to "
         'the Science Museum trial piece; credited photo of the trial piece beside it, licence at build), slow orbit, the unbuilt part drawn as dashed ink outline.',
  'layer': 'photo+3D',
  'src': ['T6', 'T7'],
  'ur': 'لندن، 1843۔ Ada Lovelace، Charles Babbage کے Analytical Engine پر لمبے notes چھاپتی ہیں۔ یہ بھاپ سے چلنے والا computer تھا، جس کا design تو بنا مگر وہ کبھی مکمل نہیں '
        'ہوا۔',
  'ps': 'لندن، 1843۔ Ada Lovelace د Charles Babbage د Analytical Engine په باره کښې اوږده notes چاپوي۔ دا د بړاس په زور چلیدونکے computer وو، design یې جوړ شو خو هیڅکله پوره نه '
        'شو۔'},
 {'id': 'C2-02',
  'ch': 'C2',
  'en': 'Her notes are famous for showing how such a machine could be programmed. And in them she warned: "The Analytical Engine has no pretensions whatever to originate '
        'anything. It can do whatever we know how to order it to perform."',
  'vis': 'Her Note G table (Bernoulli numbers diagram, public domain scan) slides in as a paper card; camera pushes in; then the quote card in Cormorant with source tag '
         "'Lovelace, Note G, 1843'.",
  'layer': 'photo+2D',
  'src': ['T6', 'T7'],
  'ur': 'یہ notes اس لیے مشہور ہیں کہ ان میں دکھایا گیا کہ ایسی machine کو program کیسے کیا جا سکتا ہے۔ اور انہی میں انہوں نے خبردار کیا: Analytical Engine خود سے کچھ نیا پیدا '
        'کرنے کا کوئی دعویٰ نہیں رکھتا۔ یہ وہی کر سکتا ہے جس کا حکم دینا ہمیں آتا ہو۔',
  'ps': 'دا notes ځکه مشهور دي چې پکښې ښودلې شوي چې داسې machine څنګه program کیدے شي۔ او په همدې کښې هغې خبردارے ورکړو: Analytical Engine پخپله د څه نوي پیدا کولو هیڅ دعوه نه '
        'لري۔ دا هغه څه کولے شي چې مونږ ته یې د حکم ورکولو طریقه معلومه وي۔'},
 {'id': 'C2-03',
  'ch': 'C2',
  'en': 'It is the oldest objection in this debate, and it still sounds right: a machine only does what it is told.',
  'vis': "The quote shrinks into a small card pinned on the canvas as 'OBJECTION 1843'; an arrow from 'ORDERS IN' to 'ACTIONS OUT' draws through the engine; a question mark "
         'hovers between.',
  'layer': '2D',
  'src': [],
  'ur': 'یہ اس بحث کا سب سے پرانا اعتراض ہے، اور آج بھی ٹھیک لگتا ہے: machine بس وہی کرتی ہے جو اسے کہا جائے۔',
  'ps': 'دا د دې بحث تر ټولو زوړ اعتراض دے، او نن هم سم ښکاري: machine صرف هغه کوي چې ورته ووئیلے شي۔'},
 {'id': 'C2-04',
  'ch': 'C2',
  'en': 'Turing\'s first answer is disarmingly honest. "Machines take me by surprise with great frequency," he wrote, mostly because he never calculated carefully enough to know '
        'what they would do.',
  'vis': "Back to Turing's desk (2D semi-real, warm lamp): a scribbled sum with a hurried assumption circled; the machine cabinet answers with an unexpected number; small chime.",
  'layer': '2D',
  'src': ['T6'],
  'ur': 'Turing کا پہلا جواب بڑا سیدھا سچا ہے۔ انہوں نے لکھا، machines مجھے اکثر حیران کر دیتی ہیں، زیادہ تر اس لیے کہ میں کبھی اتنا دھیان سے حساب ہی نہیں لگاتا کہ پتا ہو وہ کیا '
        'کریں گی۔',
  'ps': 'د Turing اول جواب ډیر ساده او رښتونے دے۔ هغه ولیکل، machines ما اکثر حیرانوي، زیاتره ځکه چې زه هیڅکله دومره په غور حساب نه کوم چې معلومه وي هغوي به څه کوي۔'},
 {'id': 'C2-05',
  'ch': 'C2',
  'en': 'His deeper answer was a different machine: not a programmed adult mind but something like a child\'s, "a notebook as one buys it from the stationer\'s": little '
        'mechanism, lots of blank sheets. Then teach it.',
  'vis': "A fresh school notebook (2D, real paper texture) opens: a few printed lines at the top ('mechanism'), many blank pages; pages begin filling with handwriting as the "
         "camera pulls back ('teach it').",
  'layer': '2D',
  'src': ['T10'],
  'ur': 'ان کا گہرا جواب ایک الگ machine تھی: بڑے کا program کیا ہوا ذہن نہیں، بلکہ بچے جیسا کچھ، جیسے stationery کی دکان سے لی نئی کاپی: mechanism تھوڑا، خالی صفحے بہت۔ پھر اسے '
        'پڑھائیں۔',
  'ps': 'د هغه ژور جواب بله machine وه: د لوی سړي program شوے ذهن نه، بلکې د ماشوم په شان یو څه، لکه د stationery د دوکان نه نوې کاپي: mechanism لږ، خالي پاڼې ډیرې۔ بیا ورته سبق '
        'ورکړئ۔'},
 {'id': 'C2-06',
  'ch': 'C2',
  'pause': 1.4,
  'en': 'A machine that learns, instead of only following orders. For decades, that stayed an idea. Then machines started beating us at our own games.',
  'vis': 'The filled notebook closes and becomes a chessboard (match cut, page edge -> board edge). Re-hook.',
  'layer': '2D',
  'src': ['T10'],
  'ur': 'ایسی machine جو سیکھے، صرف حکم نہ مانے۔ کئی دہائیوں تک یہ بس ایک خیال رہا۔ پھر machines ہمیں ہمارے ہی کھیلوں میں ہرانے لگیں۔',
  'ps': 'داسې machine چې زده کړه کوي، نه یوازې حکم مني۔ د لسیزو پورې دا یو خیال پاتې شو۔ بیا machines مونږ په خپلو لوبو کښې ماتول شروع کړل۔'},
 {'id': 'C3-01',
  'ch': 'C3',
  'en': "New York, 1997. IBM's Deep Blue beats world chess champion Garry Kasparov in a six-game match, by force: two hundred million positions every second, steered by "
        'evaluations its team built in. Lovelace would not have been surprised.',
  'vis': "Chapter tag '1997'. Credited photo of a Deep Blue cabinet (Computer History Museum photo on Commons, licence at build) and Kasparov at the board (licensed); Manim 3D: a "
         "chess position whose search tree fans out explosively in BRASS lines; counter '200,000,000 / s'; the tree collapses into a hand-built book 'EVALUATION'; the 'OBJECTION "
         "1843' card glints in its corner. Source tag: IBM.",
  'layer': 'photo+3D',
  'src': ['G1'],
  'ur': 'New York، 1997۔ IBM کا Deep Blue، chess کے world champion Garry Kasparov کو چھ games کے match میں طاقت کے زور پر ہرا دیتا ہے: ہر سیکنڈ میں 20 کروڑ positions، اس '
        'evaluation کے سہارے جو اس کی team نے اندر ڈالی تھی۔ Lovelace کو اس پر حیرت نہ ہوتی۔',
  'ps': 'New York، 1997۔ د IBM Deep Blue د chess world champion Garry Kasparov د شپږو games په match کښې د طاقت په زور ماتوي: هر سیکنډ کښې 20 کروړه positions، د هغه evaluation په '
        'مرسته چې د هغې team پکښې اچولې وه۔ Lovelace به پرې حیرانه نه وه۔'},
 {'id': 'C3-02',
  'ch': 'C3',
  'en': "Seoul, March 2016. DeepMind's AlphaGo plays Lee Sedol, one of the greatest Go players of his era. AlphaGo was not handed a strategy. It learned from thousands of expert "
        'games, then by playing against itself.',
  'vis': "Chapter beat '2016'. Credited photo of Lee Sedol (Commons, licence at build); Manim 3D 19x19 Go board, slow orbit; two ghost boards play each other (self-play) in faint "
         'loops.',
  'layer': 'photo+3D',
  'src': ['G2'],
  'ur': 'Seoul، مارچ 2016۔ DeepMind کا AlphaGo، اپنے دور کے عظیم ترین Go کھلاڑیوں میں سے ایک، Lee Sedol سے کھیلتا ہے۔ AlphaGo کو کوئی strategy نہیں دی گئی۔ اس نے ماہروں کی ہزاروں '
        'games سے سیکھا، پھر خود سے کھیل کر۔',
  'ps': 'Seoul، مارچ 2016۔ د DeepMind AlphaGo د خپل دور د Go د تر ټولو لویو لوبغاړو نه یو، Lee Sedol سره لوبه کوي۔ AlphaGo ته هیڅ strategy نه وه ورکړې شوې۔ هغه د ماهرانو د زرګونو '
        'games نه زده کړل، بیا یې د ځان سره لوبې وکړې۔'},
 {'id': 'C3-03',
  'ch': 'C3',
  'en': 'In game two it played move 37, a move DeepMind puts at a one in ten thousand chance of being played. It helped win the game. AlphaGo took the match, four games to one.',
  'vis': "Camera dives to one intersection; a single black stone lands with a soft click; label 'MOVE 37' and '1 in 10,000'. Scoreboard '4-1'. Source tag: DeepMind.",
  'layer': '3D',
  'src': ['G2'],
  'ur': 'دوسری game میں اس نے move 37 کھیلی، ایسی چال جس کے کھیلے جانے کا chance، DeepMind کے مطابق، دس ہزار میں ایک تھا۔ اسی نے game جتوانے میں مدد دی۔ AlphaGo نے match چار ایک '
        'سے جیتا۔',
  'ps': 'په دویمه game کښې یې move 37 وکړه، داسې چل چې د DeepMind په وینا یې د کیدو chance په لسو زرو کښې یو وو۔ همدې په ګټلو کښې مرسته وکړه۔ AlphaGo match څلور یو وګټلو۔'},
 {'id': 'C3-04',
  'ch': 'C3',
  'pause': 1.0,
  'en': 'Lee Sedol said he had thought AlphaGo was "merely a machine." "But when I saw this move, I changed my mind. Surely, AlphaGo is creative."',
  'vis': 'Quiet hold: Lee Sedol photo card, his quote in Cormorant (via DeepMind). No motion except a slow push.',
  'layer': 'photo',
  'src': ['G2'],
  'ur': 'Lee Sedol نے کہا: میرا خیال تھا AlphaGo صرف ایک machine ہے۔ لیکن یہ چال دیکھ کر میری رائے بدل گئی۔ یقیناً AlphaGo creative ہے۔',
  'ps': 'Lee Sedol ووئیل: ما ګڼل AlphaGo یوازې یوه machine ده۔ خو دا چل مې چې ولیدو، رائے مې بدله شوه۔ یقیناً AlphaGo creative دے۔'},
 {'id': 'C3-05',
  'ch': 'C3',
  'pause': 1.4,
  'en': "So here was a machine that did something nobody had ordered, and surprised a master. Lovelace's objection was cracking. But a sharper one was waiting: surprise is not "
        'understanding. In 1980, a philosopher built a room to prove it.',
  'vis': "The 'OBJECTION 1843' card cracks along an ink line; the crack becomes the outline of a door (match cut) -> a sealed room drawn in ink. Re-hook.",
  'layer': '2D',
  'src': ['S1'],
  'ur': 'تو یہ ایسی machine تھی جس نے وہ کیا جس کا کسی نے حکم نہیں دیا تھا، اور ایک استاد کو حیران کر دیا۔ Lovelace کا اعتراض ٹوٹ رہا تھا۔ مگر ایک اور تیز اعتراض انتظار میں تھا: '
        'حیران کرنا، سمجھنا نہیں ہے۔ 1980 میں ایک philosopher نے یہ ثابت کرنے کے لیے ایک کمرہ بنایا۔',
  'ps': 'نو دا داسې machine وه چې هغه یې وکړل چې چا یې حکم نه وو ورکړے، او یو استاد یې حیران کړو۔ د Lovelace اعتراض ماتیدو۔ خو یو بل تیز اعتراض انتظار کښې وو: حیرانول، پوهیدل نه '
        'دي۔ په 1980 کښې یو philosopher د دې ثابتولو دپاره یوه کوټه جوړه کړه۔'},
 {'id': 'C4-01',
  'ch': 'C4',
  'en': 'John Searle, at Berkeley, asks you to imagine him locked in a room. He does not read a word of Chinese. To him, in his words, it is "just so many meaningless squiggles."',
  'vis': "Chapter tag '1980'. Credited photo of John Searle (Commons, licence at build). Manim 3D cutaway of the room (ThreeDScene, warm lamp, paper texture), a figure at a desk; "
         'Chinese characters float as INK shapes with no meaning attached.',
  'layer': 'photo+3D',
  'src': ['S1'],
  'ur': 'Berkeley کے John Searle کہتے ہیں، سوچیں میں ایک کمرے میں بند ہوں۔ مجھے Chinese کا ایک لفظ نہیں آتا۔ ان کے لفظوں میں، میرے لیے یہ بس بے معنی لکیریں ہیں۔',
  'ps': 'د Berkeley John Searle وائي، فرض کړئ زه په یوه کوټه کښې بند یم۔ په Chinese کښې یو لفظ هم نه پوهیږم۔ د هغه په لفظونو، زما دپاره دا صرف بې معنې کرښې دي۔'},
 {'id': 'C4-02',
  'ch': 'C4',
  'en': 'Slips of Chinese writing come in under the door. He has a rulebook in English: when you see these shapes, send back those shapes. He follows it perfectly, and to the '
        "people outside, his answers are indistinguishable from a native speaker's.",
  'vis': "Slips slide under the door; a thick 'RULEBOOK' opens; INK arrows map shape -> shape; slips go back out. Camera pulls outside: two readers nod (silhouettes). Equal-sign "
         "icon between 'ROOM' and 'NATIVE SPEAKER'.",
  'layer': '3D+2D',
  'src': ['S2'],
  'ur': 'دروازے کے نیچے سے Chinese لکھی پرچیاں اندر آتی ہیں۔ ان کے پاس English میں ایک rulebook ہے: یہ شکلیں دیکھو، تو وہ شکلیں واپس بھیجو۔ وہ اس پر بالکل ٹھیک چلتے ہیں، اور باہر '
        'والوں کے لیے ان کے جواب کسی Chinese کے جوابوں جیسے ہی ہیں۔',
  'ps': 'د دروازې لاندې نه د Chinese لیک پرچې دننه راځي۔ د هغه سره په English کښې یو rulebook دے: دا شکلونه چې ووینې، هغه شکلونه واپس ولیږه۔ هغه پرې بالکل سم عمل کوي، او د بهر '
        'خلقو دپاره یې جوابونه د یو Chinese د جوابونو په شان دي۔'},
 {'id': 'C4-03',
  'ch': 'C4',
  'en': 'Yet inside the room, nothing understands Chinese. Searle\'s conclusion: running the right program is not enough for understanding. In his words, a program has "only a '
        'syntax but no semantics."',
  'vis': "Inside: the figure shrugs; two labels draw on and separate: 'SYNTAX' (shapes, TEAL) and 'SEMANTICS' (meaning, SIGNAL RED), the second one empty. Source tag: Searle, BBS "
         '1980.',
  'layer': '3D+2D',
  'src': ['S2'],
  'ur': 'پھر بھی کمرے کے اندر Chinese کوئی نہیں سمجھتا۔ Searle کا نتیجہ: صحیح program چلا دینا سمجھ کے لیے کافی نہیں۔ ان کے لفظوں میں، program کے پاس صرف syntax ہے، semantics '
        'نہیں۔',
  'ps': 'بیا هم د کوټې دننه هیڅوک په Chinese نه پوهیږي۔ د Searle نتیجه: صحیح program چلول د پوهې دپاره کافي نه دي۔ د هغه په لفظونو، د program سره صرف syntax دے، semantics نشته۔'},
 {'id': 'C4-04',
  'ch': 'C4',
  'pause': 0.9,
  'en': 'Remember ratta? The Chinese Room is the perfect ratta: every answer right, and none of it understood.',
  'vis': "Callback: the pinned 'RATTA' notebook flies in from its corner and lands on the room's desk; every slip gets a tick mark, the 'SEMANTICS' box stays empty.",
  'layer': '2D',
  'src': ['L1'],
  'ur': 'رٹا یاد ہے؟ Chinese Room مکمل رٹا ہے: ہر جواب صحیح، اور سمجھ کچھ بھی نہیں۔',
  'ps': 'رټا مو یاد ده؟ Chinese Room پوره رټا ده: هر جواب صحیح، او پوهه هیڅ نه۔'},
 {'id': 'C4-05',
  'ch': 'C4',
  'en': "The most famous comeback is the systems reply. The man doesn't understand, but he is only one part. The whole system, man plus rulebook plus paper, understands.",
  'vis': "Camera pulls out to show the whole room as one box labelled 'SYSTEM'; dotted outline around man + book + paper.",
  'layer': '3D',
  'src': ['S3'],
  'ur': 'اس کا سب سے مشہور جواب systems reply ہے۔ آدمی نہیں سمجھتا، مگر وہ صرف ایک حصہ ہے۔ پورا system، یعنی آدمی، rulebook اور کاغذ مل کر، سمجھتا ہے۔',
  'ps': 'د دې تر ټولو مشهور جواب systems reply دے۔ سړے نه پوهیږي، خو هغه صرف یوه برخه ده۔ ټول system، یعنې سړے، rulebook او کاغذ یو ځائے، پوهیږي۔'},
 {'id': 'C4-06',
  'ch': 'C4',
  'en': "Searle's answer: fine. Let him memorise the rulebook and do everything in his head. Now he is the whole system. And he still understands nothing.",
  'vis': "The room walls fold away; the rulebook pages stream into the figure's head; he stands outdoors on bare paper ground. The 'SEMANTICS' box is still empty.",
  'layer': '3D',
  'src': ['S3'],
  'ur': 'Searle کا جواب: ٹھیک ہے۔ وہ پوری rulebook یاد کر لے اور سب کچھ ذہن میں کرے۔ اب وہ خود پورا system ہے۔ اور پھر بھی کچھ نہیں سمجھتا۔',
  'ps': 'د Searle جواب: سمه ده۔ هغه دې ټول rulebook یاد کړي او هر څه دې په ذهن کښې وکړي۔ اوس هغه پخپله ټول system دے۔ او بیا هم په هیڅ نه پوهیږي۔'},
 {'id': 'C4-07',
  'ch': 'C4',
  'pause': 1.0,
  'en': 'So who understands Chinese here: the man, the book, or nobody at all? Philosophers have argued about it for more than forty years.',
  'vis': "Three cards side by side: 'MAN' / 'BOOK' / 'NOBODY'; a slow pulse on each in turn (viewer prompt). Year counter '1980 -> 2026'.",
  'layer': '2D',
  'src': ['S1'],
  'ur': 'تو یہاں Chinese کون سمجھتا ہے: آدمی، کتاب، یا کوئی بھی نہیں؟ philosophers چالیس سال سے زیادہ اس پر بحث کر رہے ہیں۔',
  'ps': 'نو دلته په Chinese څوک پوهیږي: سړے، کتاب، که هیڅوک نه؟ philosophers د څلویښتو کالو نه زیات په دې بحث کوي۔'},
 {'id': 'C4-08',
  'ch': 'C4',
  'en': 'And one twist people forget. Searle never said machines can\'t think. "We are precisely such machines," he wrote. His claim was that the brain\'s biology has the causal '
        'powers that matter, and a program alone does not. A simulated rainstorm, he pointed out, leaves nobody drenched.',
  'vis': "A semi-real anatomical brain (accurate, warm shading, OXBLOOD/SAGE) appears beside the room; label 'BIOLOGY' on the brain, 'PROGRAM' on the rulebook; quote card 'We are "
         "precisely such machines.' On 'simulated rainstorm': a monitor with a rain simulation, the room around it dry.",
  'layer': '2D',
  'src': ['S4', 'S5'],
  'ur': 'اور ایک بات جو لوگ بھول جاتے ہیں۔ Searle نے کبھی نہیں کہا کہ machines سوچ نہیں سکتیں۔ لکھا، ہم خود ایسی ہی machines ہیں۔ ان کا دعویٰ تھا کہ اصل طاقت دماغ کی biology میں '
        'ہے، صرف program میں نہیں۔ انہوں نے کہا، بارش کی simulation کسی کو گیلا نہیں کرتی۔',
  'ps': 'او یوه خبره چې خلق یې هیروي۔ Searle هیڅکله نه دي ووئیلي چې machines سوچ نه شي کولے۔ ولیکل، مونږ پخپله همداسې machines یو۔ د هغه دعوه وه چې اصل طاقت د دماغ په biology کښې '
        'دے، یوازې په program کښې نه۔ هغه ووئیل، د باران simulation هیڅوک نه لمدوي۔'},
 {'id': 'C4-09',
  'ch': 'C4',
  'pause': 1.4,
  'en': 'Simulate a monsoon over Lahore all day long; Lahore stays dry.',
  'vis': "Our local illustration of Searle's point (not his example): the monitor's rain simulation is over a stylised Lahore skyline (Badshahi Mosque silhouette, accurate); "
         'camera pulls back to a real, dry Lahore street outside the window (credited photo). Soft rain SFX inside the monitor only.',
  'layer': '2D',
  'src': ['L2'],
  'ur': 'سارا دن لاہور پر monsoon کی simulation چلائیں، لاہور سوکھا ہی رہے گا۔',
  'ps': 'ټوله ورځ په لاهور د monsoon simulation وچلوئ، لاهور به وچ پاتې وي۔'},
 {'id': 'C5-01',
  'ch': 'C5',
  'en': "Searle's rulebook was something a person could read. Today's language models have no rulebook anyone wrote, only billions of learned numbers, tuned to predict the next "
        'piece of text.',
  'vis': 'Re-hook. The readable rulebook dissolves into a dense wall of tiny numbers (Nimbus Mono, INK2) that scrolls past the camera; counter ticking into the billions (e.g. '
         "GPT-3: '175,000,000,000', small source tag); a single 'NEXT TOKEN ->' arrow at the end.",
  'layer': '2D',
  'src': ['M1'],
  'ur': 'Searle کی rulebook ایسی تھی جو انسان پڑھ سکے۔ آج کے language models کی کوئی rulebook کسی نے نہیں لکھی، بس اربوں سیکھے ہوئے numbers ہیں، text کا اگلا ٹکڑا guess کرنے کے '
        'لیے۔',
  'ps': 'د Searle rulebook داسې وو چې انسان یې لوستلے شي۔ د نن language models هیڅ rulebook چا نه دے لیکلے، یوازې اربونه زده کړي numbers دي، د text د راتلونکې ټکړې guess کولو '
        'دپاره۔'},
 {'id': 'C5-02',
  'ch': 'C5',
  'en': 'So does anything like understanding grow inside? In 2022, researchers at Harvard, MIT and Northeastern tested it in a tiny world. They trained a GPT-style model on move '
        'lists from the board game Othello, twenty million games. It never saw a board. Nobody told it the rules.',
  'vis': "Chapter tag '2022'. A long ticker tape of move codes ('C4 D3 E6 ...', English/alphanumeric) feeds into a small model block; counters '20,000,000 games'. No board "
         'visible yet: deliberately absent.',
  'layer': '2D',
  'src': ['M2'],
  'ur': 'تو کیا اندر سمجھ جیسی کوئی چیز اگتی ہے؟ 2022 میں Harvard، MIT اور Northeastern کے researchers نے ایک ننھی سی دنیا میں یہ جانچا۔ انہوں نے ایک GPT جیسے model کو board game '
        'Othello کی چالوں کی lists پر train کیا، 2 کروڑ games۔ اس نے کبھی board نہیں دیکھا۔ کسی نے rules نہیں بتائے۔',
  'ps': 'نو آیا دننه د پوهې په شان څه راټوکیږي؟ په 2022 کښې د Harvard، MIT او Northeastern researchers دا په یوه وړه دنیا کښې وازمویل۔ هغوي یو GPT غوندې model د board game '
        'Othello د چلونو په lists train کړو، 2 کروړه games۔ هغه هیڅکله board نه وو لیدلے۔ چا ورته rules نه وو ښودلي۔'},
 {'id': 'C5-03',
  'ch': 'C5',
  'en': 'It learned to propose legal moves almost perfectly. Trained on the big set, its top choice was illegal about once in ten thousand.',
  'vis': "Stream of predicted moves with tiny green ticks; one red cross in a sea of ticks; stamp '0.01%' with source tag 'Li et al., ICLR 2023'.",
  'layer': '2D',
  'src': ['M2'],
  'ur': 'اس نے تقریباً بالکل ٹھیک جائز چالیں بتانا سیکھ لیا۔ بڑے data پر train ہو کر، اس کی پہلی پسند دس ہزار میں تقریباً ایک بار ہی غلط ہوتی تھی۔',
  'ps': 'هغه تقریباً بالکل سم جائز چلونه ښودل زده کړل۔ په لوی data باندې train شوے، د هغه اول انتخاب په لسو زرو کښې تقریباً یو ځل ناجائز وو۔'},
 {'id': 'C5-04',
  'ch': 'C5',
  'en': "Then they looked inside. With small probes, they could read the board out of the model's internal activity, square by square: a picture of a game it had never been "
        'shown.',
  'vis': 'Manim 3D: the model block becomes translucent layers; a probe (thin BRASS needle) reads one layer; above it an 8x8 Othello board assembles square by square from the '
         'activity (the board finally appears). Slow orbit.',
  'layer': '3D',
  'src': ['M2'],
  'ur': 'پھر انہوں نے اندر جھانکا۔ چھوٹے probes سے وہ model کے اندر کی activity میں سے board پڑھ سکتے تھے، خانہ بہ خانہ: اس game کی تصویر جو اسے کبھی دکھائی ہی نہیں گئی تھی۔',
  'ps': 'بیا یې دننه وکتل۔ په وړو probes یې د model د دننه activity نه board لوستلے شو، خانه په خانه: د هغې game تصویر چې هیڅکله نه وه ورښودلې شوې۔'},
 {'id': 'C5-05',
  'ch': 'C5',
  'pause': 0.9,
  'en': 'Then the decisive step. They edited that inner picture, flipping a disc inside the model, and its next moves changed to fit the edited board. The map was not decoration. '
        'The model was using it.',
  'vis': "One disc on the inner board flips (soft chime); the 'legal moves' highlights on the board rearrange to match; label 'INTERVENTION'. Hold the wide payoff shot.",
  'layer': '3D',
  'src': ['M2'],
  'ur': 'پھر فیصلہ کن قدم۔ انہوں نے اس اندر کی تصویر کو بدلا، model کے اندر ایک disc پلٹ دی، اور اس کی اگلی چالیں بدلے ہوئے board کے حساب سے بدل گئیں۔ یہ نقشہ سجاوٹ نہیں تھا۔ '
        'model اسے استعمال کر رہا تھا۔',
  'ps': 'بیا فیصله کن قدم۔ هغوي هغه دننه تصویر بدل کړو، د model دننه یې یوه disc واړوله، او د هغې راتلونکي چلونه د بدل شوي board مطابق بدل شول۔ دا نقشه سینګار نه وه۔ model ترې '
        'کار اخستو۔'},
 {'id': 'C5-06',
  'ch': 'C5',
  'en': 'That is real evidence of an inner model of a world. But it is a toy world. And big language models can also fail in surprising ways.',
  'vis': "Pull out: the Othello board becomes a tiny tile on a huge world map outline (scale contrast, 'TOY WORLD' label).",
  'layer': '2D',
  'src': ['M2'],
  'ur': 'یہ اندر دنیا کے ایک model کا اصلی ثبوت ہے۔ مگر یہ کھلونا دنیا ہے۔ اور بڑے language models حیران کن طریقوں سے fail بھی ہوتے ہیں۔',
  'ps': 'دا د دننه یوې دنیا د model ریښتینے ثبوت دے۔ خو دا د لوبو دنیا ده۔ او لوی language models په حیرانوونکو طریقو fail هم کیږي۔'},
 {'id': 'C5-07',
  'ch': 'C5',
  'en': 'In 2023, researchers asked GPT-4 questions like "Who is Tom Cruise\'s mother?" It got those right seventy-nine percent of the time. Flip them around, "Who is Mary Lee '
        'Pfeiffer\'s son?", and it dropped to thirty-three. Same fact, other direction: the reversal curse.',
  'vis': "Two arrows between two name cards 'TOM CRUISE' <-> 'MARY LEE PFEIFFER' (text cards only, no photos of private persons): forward arrow '79%', reverse arrow '33%' "
         "(thinner, SIGNAL RED). Label 'REVERSAL CURSE'. Source tag: Berglund et al. 2023.",
  'layer': '2D',
  'src': ['M4'],
  'ur': '2023 میں researchers نے GPT-4 سے ایسے سوال پوچھے، Tom Cruise کی ماں کون ہے؟ ایسے سوال اس نے 79 فیصد صحیح کیے۔ انہیں الٹا کریں، Mary Lee Pfeiffer کا بیٹا کون ہے؟ تو یہ 33 '
        'فیصد پر آ گیا۔ وہی بات، الٹی طرف سے: reversal curse۔',
  'ps': 'په 2023 کښې researchers د GPT-4 نه داسې سوالونه وکړل، د Tom Cruise مور څوک ده؟ داسې سوالونه یې په 79 فیصده کښې صحیح کړل۔ الټا یې کړئ، د Mary Lee Pfeiffer زوے څوک دے؟ نو '
        '33 فیصده ته راښکته شو۔ هم هغه خبره، د بل طرف نه: reversal curse۔'},
 {'id': 'C5-08',
  'ch': 'C5',
  'pause': 1.4,
  'en': 'So: a map of the world inside, or a very good parrot? So far, some of both, depending on what you test. If a machine plays by a map in its head, does it understand the '
        "game? Tell us where you'd draw the line.",
  'vis': "Split canvas: left the inner Othello map, right the 'RATTA' parrot; a drawn line hovers between them, moving left and right (viewer prompt); settles in the middle.",
  'layer': '2D',
  'src': ['M2', 'M4'],
  'ur': 'تو اندر دنیا کا نقشہ ہے یا ایک بہت اچھا طوطا؟ اب تک، دونوں کچھ کچھ، یہ اس پر ہے کہ آپ test کیا کرتے ہیں۔ اگر machine اپنے اندر کے نقشے سے کھیلے، تو کیا وہ game سمجھتی '
        'ہے؟ بتائیں، آپ لکیر کہاں کھینچیں گے۔',
  'ps': 'نو دننه د دنیا نقشه ده که یو ډیر ښه طوطی؟ تر اوسه، دواړه څه ناڅه، دا په دې ده چې تاسو څه test کوئ۔ که machine د خپلې دننه نقشې نه لوبه کوي، نو آیا په game پوهیږي؟ ووایئ، '
        'تاسو به کرښه چرته کاږئ۔'},
 {'id': 'C6-01',
  'ch': 'C6',
  'en': 'Back to that seventy-three percent. The study, by Cameron Jones and Benjamin Bergen, was peer-reviewed and published in PNAS in 2026.',
  'vis': "Chapter tag '2026'. Return to the opening phone canvas (callback); PNAS paper title card (text only; PNAS figure only if its licence allows, check at build). Source "
         'tag.',
  'layer': '2D',
  'src': ['F1'],
  'ur': 'واپس اسی 73 فیصد پر۔ یہ study، Cameron Jones اور Benjamin Bergen کی، peer-review کے بعد 2026 میں PNAS میں چھپی۔',
  'ps': 'بیرته هغه 73 فیصدو ته۔ دا study، د Cameron Jones او Benjamin Bergen، د peer-review نه پس په 2026 کښې په PNAS کښې چاپ شوه۔'},
 {'id': 'C6-02',
  'ch': 'C6',
  'en': "It used Turing's three-way setup: each interrogator chatted with a human and a machine at once, for five minutes, then picked the human. Two separate groups took part: "
        'university students, and paid volunteers online.',
  'vis': "The 1950 three-room 3D model from C1 reappears and morphs into a modern split-screen chat (match cut across 75 years); '5 MIN' timer; two group icons 'STUDENTS' / "
         "'ONLINE'.",
  'layer': '3D+2D',
  'src': ['F1'],
  'ur': 'اس میں Turing کا تین طرفہ طریقہ استعمال ہوا: ہر سوال کرنے والا ایک ساتھ ایک انسان اور ایک machine سے پانچ منٹ chat کرتا، پھر انسان چنتا۔ دو الگ گروپوں نے حصہ لیا: '
        'university students، اور online پیسوں پر حصہ لینے والے لوگ۔',
  'ps': 'پکښې د Turing درې طرفه طریقه استعمال شوه: هر پوښتونکي یو ځائے د یو انسان او یوې machine سره پنځه منټه chat کوله، بیا یې انسان غوره کولو۔ دوه جدا ګروپونو برخه واخستله: '
        'university students، او online په پیسو شریک شوي خلق۔'},
 {'id': 'C6-03',
  'ch': 'C6',
  'en': 'With the persona, GPT-4.5 was picked as the human seventy-three percent of the time, and LLaMa 3.1 fifty-six. Without it, the same models fell to thirty-six and '
        'thirty-eight. ELIZA, a 1960s rule-based chatbot added as a check, got twenty-three.',
  'vis': 'Bar chart builds bar by bar on one canvas (Inter numerals): GPT-4.5 PERSONA 73 / LLaMa-3.1 PERSONA 56 / GPT-4.5 NO PERSONA 36 / LLaMa-3.1 NO PERSONA 38 / ELIZA 23 '
         '(ELIZA bar small and quiet, no character art) ; dashed 50% chance line. Camera zooms to each bar as named, then out.',
  'layer': '2D',
  'src': ['F2', 'F3'],
  'ur': 'persona کے ساتھ GPT-4.5 کو 73 فیصد بار انسان چنا گیا، اور LLaMa 3.1 کو 56 فیصد۔ اس کے بغیر یہی models 36 اور 38 پر آ گئے۔ ELIZA، 1960 کی دہائی کا rules والا chatbot، جو '
        'check کے لیے رکھا گیا، 23 پر رہا۔',
  'ps': 'د persona سره GPT-4.5 په 73 فیصده کښې انسان وګڼلے شو، او LLaMa 3.1 په 56 کښې۔ بې له دې همدا models 36 او 38 ته راښکته شول۔ ELIZA، د 1960 لسیزې د rules والا chatbot، چې د '
        'check دپاره ساتلے شوے وو، په 23 پاتې شو۔'},
 {'id': 'C6-04',
  'ch': 'C6',
  'en': 'When they stretched the games to fifteen minutes, it held. GPT-5, with the same persona, was picked fifty-nine percent of the time.',
  'vis': "Timer ring stretches '5 MIN' -> '15 MIN'; a new bar 'GPT-5 PERSONA 59' joins, still above the 50% line.",
  'layer': '2D',
  'src': ['F4'],
  'ur': 'جب games کو پندرہ منٹ تک بڑھایا گیا، نتیجہ وہی رہا۔ GPT-5 اسی persona کے ساتھ 59 فیصد بار چنا گیا۔',
  'ps': 'کله چې games پنځلس منټو ته اوږدې کړې شوې، نتیجه هم هغه وه۔ GPT-5 د همدې persona سره په 59 فیصده کښې غوره شو۔'},
 {'id': 'C6-05',
  'ch': 'C6',
  'en': "So Turing's bet came true, about twenty-five years late. His line was seventy percent accuracy for the interrogator. Here, people facing the best model did worse than a "
        'coin toss.',
  'vis': "The 1950 ruler returns: '2000' stamp slides to '2025'; a '70%' threshold line vs. 'INTERROGATOR ACCURACY 27%' (vs GPT-4.5 persona); a coin flips once.",
  'layer': '2D',
  'src': ['T3', 'F2'],
  'ur': 'یوں Turing کی شرط سچ ثابت ہوئی، تقریباً 25 سال دیر سے۔ ان کی حد تھی سوال کرنے والے کی 70 فیصد درستی۔ یہاں سب سے اچھے model کے سامنے لوگ سکہ اچھالنے سے بھی برا کر رہے '
        'تھے۔',
  'ps': 'داسې د Turing شرط رښتیا شوه، تقریباً 25 کاله ناوخته۔ د هغه حد د پوښتونکي 70 فیصده درستي وه۔ دلته د تر ټولو ښه model مخې ته خلقو د سکې اچولو نه هم بد کار وکړو۔'},
 {'id': 'C6-06',
  'ch': 'C6',
  'en': 'But look at how people decided. The most common strategy was small talk; only twelve percent tested knowledge or reasoning, the things Turing imagined. And the reason '
        'given most often was linguistic style: a typo, a casual tone, the feel of the writing.',
  'vis': "Horizontal bars: 'SMALL TALK 61%' long, 'KNOWLEDGE & REASONING 12%' short; then reason chips float up: 'TYPO', 'TONE', 'STYLE' (English labels). Source tag: PNAS 2026, "
         'Fig. 4-5.',
  'layer': '2D',
  'src': ['F5'],
  'ur': 'لیکن دیکھیں لوگوں نے فیصلہ کیسے کیا۔ سب سے عام طریقہ گپ شپ تھا؛ صرف 12 فیصد نے علم یا reasoning کو جانچا، جن کا Turing نے سوچا تھا۔ اور سب سے زیادہ دی گئی وجہ تھی لکھنے '
        'کا انداز: کوئی typo، بے تکلف لہجہ، تحریر کا احساس۔',
  'ps': 'خو وګورئ چې خلقو فیصله څنګه وکړه۔ تر ټولو عامه طریقه ګپ شپ وه؛ صرف 12 فیصده علم یا reasoning وازمویلو، د کومو چې Turing سوچ کړے وو۔ او تر ټولو زیاته ورکړې شوې وجه د '
        'لیکلو انداز وو: یو typo، بې تکلفه لهجه، د لیک احساس۔'},
 {'id': 'C6-07',
  'ch': 'C6',
  'pause': 1.0,
  'en': 'Ghalib has a line that fits this almost too well: "They say Ghalib\'s way of saying things is something else." He meant his poetry. The judges did the same thing: they '
        'chose by the manner of speaking.',
  'vis': 'THE THOUGHT: quiet card on PAPER2, Ghalib portrait (public domain, credited); the original Urdu line in Noto Nastaliq Urdu, large: «کہتے ہیں کہ غالبؔ کا ہے اندازِ بیاں '
         "اور» with the English meaning beneath in Cormorant; tag 'Mirza Ghalib (1797-1869), via Rekhta'. Slow push, bed only.",
  'layer': 'photo+2D',
  'src': ['Q1'],
  'ur': 'غالب کا ایک مصرع اس پر کچھ زیادہ ہی ٹھیک بیٹھتا ہے: کہتے ہیں کہ غالبؔ کا ہے اندازِ بیاں اور۔ ان کی مراد اپنی شاعری تھی۔ judges نے بھی یہی کیا: بات کرنے کے انداز سے چنا۔',
  'ps': 'د غالب یو مصرع په دې ډیره برابره ده: کہتے ہیں کہ غالبؔ کا ہے اندازِ بیاں اور، یعنې د غالب انداز بل شان دے۔ مراد یې خپله شاعري وه۔ judges هم همداسې وکړل: د خبرو د انداز '
        'نه یې غوره کړل۔'},
 {'id': 'C6-08',
  'ch': 'C6',
  'pause': 1.4,
  'en': "The authors' careful conclusion: the test may now measure humanlikeness more than intelligence. It shows a machine can stand in for a person in a short chat; not what, "
        'if anything, is going on inside.',
  'vis': "The chat window shrinks into a closed box with a keyhole; label 'HUMANLIKE?' on the box, 'INSIDE?' at the keyhole. Re-hook into the next chapter.",
  'layer': '2D',
  'src': ['F6'],
  'ur': 'مصنفین کا محتاط نتیجہ: یہ test شاید اب ذہانت سے زیادہ انسان جیسا لگنا ناپتا ہے۔ یہ بتاتا ہے کہ machine ایک چھوٹی chat میں انسان کی جگہ لے سکتی ہے؛ یہ نہیں کہ اندر کیا ہو '
        'رہا ہے، اگر کچھ ہو رہا ہے۔',
  'ps': 'د لیکوالانو محتاطه نتیجه: دا test شاید اوس د ذهانت نه زیات انسان ته ورته والے اندازه کوي۔ دا ښائي چې machine په لنډه chat کښې د انسان ځائے نیولے شي؛ دا نه چې دننه څه '
        'کیږي، که څه کیږي۔'},
 {'id': 'C7-01',
  'ch': 'C7',
  'en': 'And inside is where the hardest question lives. Thinking is one thing. Experiencing, there being something it feels like to be you, is another. Turing saw that objection '
        'coming too.',
  'vis': "Camera goes through the keyhole into a dim NIGHT-umber space (the one deep-dark chapter); two labels: 'THINKING' (BRASS) and 'EXPERIENCE' (LAMP glow, no neon).",
  'layer': '2D',
  'src': ['T11'],
  'ur': 'اور اندر ہی سب سے مشکل سوال رہتا ہے۔ سوچنا ایک بات ہے۔ محسوس کرنا، یعنی آپ ہونے کا کوئی احساس ہونا، دوسری بات۔ Turing نے یہ اعتراض بھی پہلے سے بھانپ لیا تھا۔',
  'ps': 'او دننه تر ټولو ګران سوال اوسیږي۔ سوچ کول یوه خبره ده۔ احساس کول، یعنې ستاسو د کیدو یو احساس موجود وي، بله خبره ده۔ Turing دا اعتراض هم مخکښې لیدلے وو۔'},
 {'id': 'C7-02',
  'ch': 'C7',
  'pause': 1.0,
  'en': "In 1949, Professor Jefferson argued that no machine equals a brain until it writes a sonnet because of thoughts and emotions felt. Turing's reply: taken to the extreme, "
        'the only way to be sure anything thinks is to be it, and that would apply to other people too. So, he wrote, we keep "the polite convention that everyone thinks."',
  'vis': "A sonnet page (Shakespeare's 'Shall I compare thee', quoted in Turing's viva example) as a paper card; two silhouettes face each other, each with a closed thought "
         "bubble; quote card 'the polite convention that everyone thinks'.",
  'layer': '2D',
  'src': ['T11'],
  'ur': '1949 میں Professor Jefferson نے کہا کہ کوئی machine دماغ کے برابر نہیں جب تک وہ محسوس کیے ہوئے خیالوں اور جذبات کی وجہ سے sonnet نہ لکھے۔ Turing کا جواب: اسے آخری حد تک '
        'لے جائیں تو یقین کا واحد طریقہ ہے خود وہی ہونا، اور یہ بات دوسرے انسانوں پر بھی لاگو ہوگی۔ اس لیے، انہوں نے لکھا، ہم یہ شائستہ رواج رکھتے ہیں کہ سب سوچتے ہیں۔',
  'ps': 'په 1949 کښې Professor Jefferson ووئیل چې هیڅ machine د دماغ برابره نه ده تر هغې چې د محسوس شوو خیالونو او جذباتو په وجه sonnet ونه لیکي۔ د Turing جواب: که دا آخري حد ته '
        'یوسئ نو د یقین یوازینۍ لار دا ده چې ته پخپله هماغه یې، او دا به په نورو انسانانو هم لاګو وي۔ ځکه، هغه ولیکل، مونږ دا مؤدب رواج ساتو چې هر څوک سوچ کوي۔'},
 {'id': 'C7-03',
  'ch': 'C7',
  'en': 'In 2023, nineteen researchers, including the AI pioneer Yoshua Bengio, tried to do better than a polite convention.',
  'vis': "Chapter beat '2023'. A grid of 19 small author name cards (text only) fills in; 'Bengio' highlighted; report title card 'Consciousness in Artificial Intelligence' "
         '(arXiv 2308.08708).',
  'layer': '2D',
  'src': ['B1'],
  'ur': '2023 میں 19 researchers نے، جن میں AI کے بانیوں میں سے Yoshua Bengio بھی تھے، شائستہ رواج سے بہتر کچھ کرنے کی کوشش کی۔',
  'ps': 'په 2023 کښې 19 researchers، چې پکښې د AI د بنسټ ایښودونکو نه Yoshua Bengio هم وو، د مؤدب رواج نه د ښه کار کوشش وکړو۔'},
 {'id': 'C7-04',
  'ch': 'C7',
  'en': 'They took leading scientific theories of consciousness, such as global workspace theory, and turned them into "indicator properties": concrete features you could check '
        'for in a real AI system.',
  'vis': "Theory cards ('GLOBAL WORKSPACE', 'RECURRENT PROCESSING', 'HIGHER-ORDER', 'PREDICTIVE PROCESSING', 'ATTENTION SCHEMA') each drop a checkbox onto a clipboard titled "
         "'INDICATORS'.",
  'layer': '2D',
  'src': ['B1'],
  'ur': 'انہوں نے consciousness کی بڑی scientific theories لیں، جیسے global workspace theory، اور انہیں indicator properties میں بدلا: ایسی ٹھوس خصوصیات جو کسی اصلی AI system میں '
        'چیک کی جا سکیں۔',
  'ps': 'هغوي د consciousness لویې scientific theories واخستې، لکه global workspace theory، او په indicator properties یې بدلې کړې: داسې ټینګې ځانګړتیاوې چې په یو ریښتیني AI '
        'system کښې چیک کیدے شي۔'},
 {'id': 'C7-05',
  'ch': 'C7',
  'en': 'Their 2023 analysis suggested no current AI systems were conscious, and also found no obvious technical barriers to building systems that meet the indicators. Their '
        'warning: meeting them still would not prove a system is conscious.',
  'vis': "Clipboard checks against a few AI system icons (generic blocks, no logos): boxes mostly empty, stamp 'NO CURRENT SYSTEM (2023)'; then a second stamp 'NO OBVIOUS "
         "BARRIER'; then a small INK2 footnote card 'not proof'.",
  'layer': '2D',
  'src': ['B2'],
  'ur': '2023 میں ان کے تجزیے کے مطابق اس وقت کا کوئی AI system conscious نہیں تھا، اور یہ indicators پورے کرنے والے systems بنانے میں کوئی واضح technical رکاوٹ بھی نہیں ملی۔ ان '
        'کی تنبیہ: یہ پورے ہونا بھی ثبوت نہیں کہ system conscious ہے۔',
  'ps': 'په 2023 کښې د هغوي د تجزیې مطابق د هغه وخت هیڅ AI system conscious نه وو، او د داسې systems په جوړولو کښې چې دا indicators پوره کړي، هیڅ واضح technical خنډ هم ونه موندلے '
        'شو۔ د هغوي خبردارے: د دې پوره کیدل هم ثبوت نه دے چې system conscious دے۔'},
 {'id': 'C7-06',
  'ch': 'C7',
  'en': 'Even that method rests on a bet, a mainstream but disputed one: that consciousness comes from the right computations, whatever the machine is made of. Supporters of '
        'integrated information theory argue a digital computer is unlikely to be conscious, whatever program it runs.',
  'vis': "Two-pan balance scale (2D, BRASS): left pan 'COMPUTATION' (a circuit pattern drawn in ink, no glow), right pan 'SUBSTRATE' (brain tissue texture); right pan labelled "
         "'IIT'. The scale tips back and forth.",
  'layer': '2D',
  'src': ['B3'],
  'ur': 'یہ طریقہ بھی ایک شرط پر کھڑا ہے، عام مگر متنازع: کہ consciousness صحیح computations سے آتی ہے، machine چاہے کسی بھی چیز کی بنی ہو۔ integrated information theory کے حامی '
        'کہتے ہیں کہ digital computer کا conscious ہونا مشکل ہے، چاہے کوئی بھی program چلائے۔',
  'ps': 'دا طریقه هم په یوه شرط ولاړه ده، عامه خو اختلافي: چې consciousness د صحیح computations نه راځي، machine که د هر شي نه جوړه وي۔ د integrated information theory حامیان '
        'وائي چې د digital computer conscious کیدل ګران دي، که هر program چلوي۔'},
 {'id': 'C7-07',
  'ch': 'C7',
  'pause': 1.4,
  'en': 'Notice the shape of that fight. Is it the pattern that matters, or the stuff it runs on? It is Turing against Searle all over again, now argued over real machines.',
  'vis': "The balance scale's pans fade into the Turing photo card (left) and the Searle photo card (right) from earlier chapters; wide hold.",
  'layer': 'photo+2D',
  'src': ['B3', 'S4'],
  'ur': 'اس لڑائی کی شکل دیکھیں۔ اہم pattern ہے، یا وہ مادہ جس پر وہ چلتا ہے؟ یہ پھر سے Turing بمقابلہ Searle ہے، اب اصلی machines کے سامنے۔',
  'ps': 'د دې جنګ شکل وګورئ۔ اهم pattern دے، که هغه مواد چې پرې چلیږي؟ دا بیا هم Turing د Searle په مقابل کښې دے، اوس د ریښتینو machines مخې ته۔'},
 {'id': 'C8-01',
  'ch': 'C8',
  'en': 'So, can machines think? Here is what we can honestly say today.',
  'vis': 'Back on Map Warm paper; the whole story canvas visible in one wide shot (rooms, engine, Go board, Chinese room, Othello board, bar chart) as the camera settles.',
  'layer': '2D',
  'src': [],
  'ur': 'تو کیا machines سوچ سکتی ہیں؟ آج ہم ایمانداری سے یہ کہہ سکتے ہیں۔',
  'ps': 'نو آیا machines سوچ کولے شي؟ نن مونږ په ایمانداري دا ویلے شو۔'},
 {'id': 'C8-02',
  'ch': 'C8',
  'en': "By Turing's test, some already pass. Inside, at least some models build working maps of their world. On new ground, they can still fail in surprising ways. And is anyone "
        'home? A careful 2023 attempt to check found no current system that qualifies.',
  'vis': "Camera visits four zones of the wide canvas in turn, each getting a stamp: bar chart 'PASSES', Othello map 'INNER MAP', reversal arrows 'FAILS', keyhole box 'OPEN'.",
  'layer': '2D',
  'src': ['F1', 'M2', 'M4', 'B2'],
  'ur': 'Turing کے test پر کچھ pass ہو چکی ہیں۔ اندر، کم از کم کچھ models اپنی دنیا کے کام کرنے والے نقشے بناتے ہیں۔ نئی جگہ پر اب بھی حیران کن طریقوں سے fail ہو سکتے ہیں۔ اور '
        'کیا اندر کوئی ہے؟ 2023 کی ایک محتاط کوشش کو اس وقت کا کوئی system اس قابل نہیں ملا۔',
  'ps': 'د Turing په test کښې ځینې pass شوې دي۔ دننه، لږ تر لږه ځینې models د خپلې دنیا کار کوونکې نقشې جوړوي۔ په نوي ځائے اوس هم په حیرانوونکو طریقو fail کیدے شي۔ او آیا دننه '
        'څوک شته؟ د 2023 یو محتاط کوشش د هغه وخت هیڅ system د دې قابل ونه موندلو۔'},
 {'id': 'C8-03',
  'ch': 'C8',
  'en': 'Maybe the question Turing called meaningless was really three questions. Can it behave like us? Does it model the world? Is anyone home? We now have experiments for the '
        'first two. The third is still wide open.',
  'vis': "Three cards draw on: 'BEHAVES LIKE US?' (tick, experiment icon), 'MODELS THE WORLD?' (tick, probe icon), 'ANYONE HOME?' (open question mark, LAMP warm).",
  'layer': '2D',
  'src': ['T3', 'F1', 'M2', 'B2'],
  'ur': 'شاید جسے Turing نے بے معنی سوال کہا، وہ اصل میں تین سوال تھے۔ کیا یہ ہماری طرح برتاؤ کر سکتی ہے؟ کیا یہ دنیا کا model بناتی ہے؟ کیا اندر کوئی ہے؟ پہلے دو کے لیے اب تجربے '
        'موجود ہیں۔ تیسرا اب بھی پوری طرح کھلا ہے۔',
  'ps': 'شاید هغه سوال چې Turing بې معنې ووئیلو، په اصل کښې درې سوالونه وو۔ آیا زمونږ په شان رویه کولے شي؟ آیا د دنیا model جوړوي؟ آیا دننه څوک شته؟ د اولو دوو دپاره اوس تجربې '
        'شته۔ دریم اوس هم پوره خلاص دے۔'},
 {'id': 'C8-04',
  'ch': 'C8',
  'pause': 1.0,
  'en': 'Turing ended his paper with a line that still fits: "We can only see a short distance ahead, but we can see plenty there that needs to be done."',
  'vis': "The Mind paper's last page as a paper card; the line types on in Cormorant; camera drifts slowly forward into blank paper (the open road).",
  'layer': 'photo+2D',
  'src': ['T12'],
  'ur': 'Turing نے اپنا paper ایک ایسی line پر ختم کیا جو آج بھی ٹھیک بیٹھتی ہے: ہم آگے تھوڑا ہی دیکھ سکتے ہیں، مگر اتنا ضرور دیکھ سکتے ہیں کہ کرنے کو بہت کچھ پڑا ہے۔',
  'ps': 'Turing خپل paper په داسې line ختم کړو چې نن هم برابره ده: مونږ مخکښې لږ لیدلے شو، خو دومره ضرور وینو چې د کولو ډیر کارونه پاتې دي۔'},
 {'id': 'C8-05',
  'ch': 'C8',
  'pause': 2.0,
  'en': 'So here is our question for you. What would a machine have to do to change your mind?',
  'vis': "The two chat panes from the cold open return, empty, cursor blinking (bookend). Then END CARD (shown, never spoken): Neuron star, L A T O O N, 'Voyaging the Unseen'; "
         'lower two-thirds clear for Studio end-screen elements (next: Big Questions / Enigma), ~15-20 s bed.',
  'layer': '2D',
  'src': [],
  'ur': 'تو ہمارا سوال آپ سے یہ ہے۔ کسی machine کو کیا کرنا پڑے گا کہ آپ کی رائے بدل جائے؟',
  'ps': 'نو زمونږ سوال ستاسو نه دا دے۔ یوې machine به څه کول وي چې ستاسو رائے بدله شي؟'}]
