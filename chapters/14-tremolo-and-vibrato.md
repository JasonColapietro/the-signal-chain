# Chapter 14 - Tremolo and Vibrato: The First Modulation

A teenager in a Memphis bedroom in 1962 flips a chrome switch on the face of a small brown amplifier, and the room begins to breathe. He hasn't touched a string yet. The amp is simply idling, its tubes warm, and already the silence has a pulse to it — a faint, rhythmic swelling in the hiss, like a heartbeat heard through a wall. He strikes a single open E, lets it ring, and the note doesn't just sustain; it gulps. Loud, soft, loud, soft, a steady throb that turns one plain note into a procession of notes, each a little ghost of the last. He has done nothing clever. He has only flipped a switch. But the guitar has stopped being a guitar that makes sounds and become a guitar that makes *time*, and somewhere in that swelling and fading he hears the surf, the desert highway, the slow drip of a Louisiana swamp he has never seen. This is the first effect most players ever met — not a stompbox bought and bolted to a pedalboard, but a circuit already living inside the amplifier, waiting behind a switch labeled, with a confidence that would confuse guitarists for the next sixty years, **Vibrato**.

## The Great Naming Confusion

Let us settle the vocabulary before we go a single sentence further, because the manufacturers got it backward and never fully owned up to it. There are two distinct effects here, and they do genuinely different things to the sound.

**Tremolo** is a periodic change in *volume*. The pitch never moves. The amplitude — the loudness — rises and falls at a regular rate, so a held note pulses: on, off, on, off, or more gently, swell and dip. Think of rapidly turning your guitar's volume knob up and down with a metronome. That is tremolo, and it is, despite the label, what almost every vintage Fender amp actually produces.

**Vibrato** is a periodic change in *pitch*. The volume stays put while the note bends slightly sharp and flat around its center, the way an opera singer or a violinist makes a held tone shimmer, the way a blues player wiggles a fretted note with the fretting hand. The wobble is in the frequency, not the volume.

Here is the crime. Leo Fender, building the **Tremolux** in 1955 and the larger **Vibrolux** soon after, slapped the wrong words on the wrong things and then doubled down. Most famously, the amp Fender called the Vibrolux, and the front-panel circuit Fender labeled "Vibrato" on countless blackface and silverface amps, is in fact *tremolo* — volume pulsing, pitch dead steady. Meanwhile the genuine pitch-shifting *vibrato* that Fender did build — into the Vibroverb and a few others, and most ambitiously into the bridge-mounted **synchronized tremolo** on the 1954 Stratocaster — got tangled up too, because the Stratocaster's pitch-bending whammy bar is, by the strict definition, a *vibrato* unit but was christened "tremolo" on the patent. So the bar that changes pitch was called tremolo, and the circuit that changes volume was called vibrato, and Leo, a radio repairman by trade and no musician, seems never to have grasped or much cared about the distinction. Gibson, to their credit, generally got it right, calling their amp circuits "Vibrato" only when there was pitch movement involved and "Tremolo" when there wasn't, though their consistency wavered too. The upshot: when a vintage Fender says "Vibrato" on the panel, your ears are almost certainly hearing tremolo. When you yank the silver bar on a Strat, you are producing vibrato that the headstock decal insists on calling tremolo. The words are a coin landed on its edge. Throughout this chapter I will use them correctly — tremolo for volume, vibrato for pitch — and trust you to translate the front panels.

## How the Throb Is Made

The earliest amplifier tremolo, appearing on Gibson and Fender amps in the late 1940s and very early 1950s, worked by the most direct method imaginable: it wiggled the tube's operating point. Inside a vacuum tube, a small negative voltage on the control grid — the **bias** — sets how much the tube amplifies. Push that bias voltage up and down with a slow oscillator and the tube's gain rises and falls in sympathy, so the whole signal passing through gets louder and softer. This is **bias tremolo**, and it has a particular character: because you are modulating a power or phase-inverter tube near the end of the chain, the effect interacts with how hard the amp is working. At the loudest part of each cycle the tube can edge toward breakup, so the pulse isn't a clean on/off — it has a slightly ragged, lurching, almost seasick swell, smooth at the top and gummy at the bottom. Brownface Fenders and many tweed-era circuits used variations of this. The low-frequency oscillator itself, the **LFO**, was typically built from a single triode wired as a phase-shift oscillator, producing a roughly sinusoidal control voltage whose speed you set with the Speed knob and whose depth you set with the Intensity knob.

The second great method is **optical**, or photocell, tremolo, and it is the one most associated with the classic blackface Fender sound of the 1960s. Here the LFO doesn't touch the tubes at all. Instead it drives a small neon lamp or incandescent bulb that brightens and dims, and that pulsing light shines on a **light-dependent resistor** (an LDR, or photocell) sitting across the signal path. As the lamp glows brighter the photocell's resistance drops and more signal bleeds to ground; as the lamp fades the resistance rises and the signal returns. The whole assembly — lamp plus photocell sealed together in a little light-tight tube — was nicknamed the "roach" or optocoupler. Because the photocell responds with a slight lag and a gentle curve rather than switching instantly, optical tremolo has a famously smooth, rounded, almost vocal swell. It is the sound of a Fender Twin or Deluxe Reverb idling: a soft, even, hypnotic pulse with none of the lurch of bias tremolo. The trade-off is a tiny loss of overall volume when the circuit is engaged, since the photocell is always shunting at least a little signal away — flip the tremolo off on a blackface amp and you'll often hear the rig get a hair louder.

And then there is the strange and gorgeous third path: **harmonic tremolo**, found on a small run of Fender "brownface" amps from roughly 1959 to 1963 — certain Twin, Pro, Super, and Concert models. This is the connoisseur's tremolo, the one that sends collectors into reverie. Instead of simply raising and lowering the whole signal's volume, the harmonic circuit splits the signal into two frequency bands — a low-pass path carrying the bass and a high-pass path carrying the treble — and modulates them *out of phase* with each other. As the lows swell, the highs dip, and vice versa. The effect is that the tone color shifts back and forth as much as the volume does, the way a wah pedal parked and rocking slowly might sound, producing a watery, phasey, almost three-dimensional pulse that seems to move not just in loudness but in space. Whether the brownface circuit is a "true" frequency-splitting filter modulation or something closer to a bias tremolo with a phase-shift quirk has been argued endlessly by amp techs and clone-builders; the most rigorous teardowns describe it as a genuine two-band, out-of-phase modulation, and that is the explanation that best matches what your ears hear. Either way the sound is unmistakable, lusher and more liquid than any plain volume tremolo, and modern pedal makers have spent decades trying to bottle it.

True pitch **vibrato** in an amplifier is rarer and harder, because changing pitch electronically in 1960 meant changing the *time* it took the signal to pass through — a tiny, modulated delay. Some designs achieved a mild vibrato by frequency-modulating an oscillator stage; the effect was subtle and never became the dominant amp feature that tremolo did. The most musically important pitch vibrato of the era didn't come from the amp at all. It came from the player's hand and from that bridge-mounted bar on the Stratocaster, where pressing down slacks all six strings at once and lifting tightens them, sweeping the whole chord sharp and flat — the genuine article, mislabeled or not.

## Why It Sounds the Way It Does, and How to Make It Groove

A pulse is not yet music. A clock ticks at a steady rate and we ignore it. The reason tremolo became a beloved musical effect rather than a novelty is that guitarists learned to *lock its rate to the song* — to treat the throb not as decoration laid over the music but as a rhythmic voice inside it. To do that you need a working idea of **rhythmic subdivision**: the way a single beat divides into smaller equal parts.

Count a moderate groove: one, two, three, four. Each of those numbers is a **quarter note**. Split each beat cleanly in half and you get **eighth notes** — one-and, two-and, three-and, four-and — twice as many pulses, twice as fast. Split each beat into three equal parts instead and you get **triplets** — one-trip-let, two-trip-let — a rolling, loping, three-against-the-beat feel that is the secret heartbeat of the blues and of a thousand slow soul ballads. Now: set your tremolo's Speed knob so that one full swell-and-dip cycle of the effect lands exactly on each of those subdivisions. If one tremolo cycle equals one quarter note, the amp pulses once per beat — a slow, looming throb. Speed it up so one cycle equals an eighth note and the pulse doubles, becoming a propulsive chop. Tune it to triplets and the guitar starts to gallop. The numbers are simple: if the song is at 120 beats per minute, a quarter-note tremolo runs at 2 cycles per second (120 divided by 60); eighth notes at that tempo want 4 cycles per second; triplets want 6. Match the LFO to one of those and the steady throb stops fighting the drummer and starts *grooving with* him. Mismatch it — let the tremolo drift at some unrelated speed — and the effect smears into seasickness, a wobble that pulls against the beat and makes the whole track feel slightly drunk. Sometimes, gloriously, that is exactly what you want; "Crimson and Clover" floats precisely because its tremolo isn't rigidly locked. But when you want power, you lock it, and a single chord held under a hard eighth-note tremolo can drive a song harder than a busy strumming hand ever could, because the listener's body feels the regularity and starts to move to it.

Let's hear the first one. A simple chord stab, held and chopped into hard eighth notes by the tremolo, the way countless 1960s records used a parked chord as a rhythm engine.

```
Tempo: 120 bpm. Tremolo RATE set to eighth notes (4 cycles/sec).
Hold each chord; the AMP does the rhythm. Let ring throughout.

e|--0---------------0---------------|
B|--1---------------1---------------|
G|--0---------------0---------------|
D|--2---------------2---------------|
A|--3---------------3---------------|
E|----------------------------------|
   C  . . . . . .   C  . . . . . .
   (each dot = one tremolo pulse, two pulses per beat)

Tremolo on a held C major chord — the amp pulses the rhythm.
```
*Strike the C major chord once and hold it; the eighth-note tremolo carves it into a pulsing pad. Dial Intensity high for a near-staccato chop, Speed to taste against a click. Optical (blackface) tremolo gives the smoothest swell; bias tremolo adds lurch.*

Notice what the theory bought us. That single C chord — root C, the major third E, the perfect fifth G — never changes. The harmony is static. Yet the passage has rhythm, drive, and motion, all of it supplied by the amplifier's volume oscillation rather than by the fretting hand. This is the deepest lesson of tremolo: it lets *time* become an instrument. You can stand on one chord for eight bars and the song still moves, because the throb is doing the work a strumming arm would otherwise do.

Now the triplet feel — the swampy, rolling pulse, three subdivisions per beat, the texture of bayou rock and slow Southern grooves.

```
Tempo: ~88 bpm, swampy. Tremolo RATE set to TRIPLETS (3 cycles/beat).
Low, dark chords. Neck pickup, amp just starting to break up.

e|----------------------------------|
B|----------------------------------|
G|----------------------------------|
D|--7-----------------5-------------|
A|--7-----------------5-------------|
E|--5-----------------3-------------|
   D5                 C5
   |  |  |  |  |  |    |  |  |  |  |  |
   (each | = one triplet tremolo pulse)

Open-voiced power chords under a galloping triplet tremolo.
```
*Two open-voiced power chords (root and fifth only — no third, so they read as neither major nor minor) ride a triplet tremolo that turns each held chord into a galloping, three-per-beat throb. Roll the amp's Intensity to about three-quarters for a deep, swallowing pulse. This is the swamp: dark, wet, hypnotic.*

These are **power chords** — written D5 and C5 — built from just the root and the perfect fifth, the interval whose frequencies sit in the tidy ratio of 3 to 2 and ring with an open, hollow stability. Because there's no third (the note that would make a chord sound happy-major or sad-minor), a power chord is harmonically neutral, all muscle and no mood, which is exactly why it sits so well under heavy modulation: the ear isn't distracted by the chord's emotional color and gives itself over to the *rhythm* of the tremolo instead. Triplet tremolo over open fifths is the engine of a whole strain of swamp rock.

## Three Players, Three Pulses

**Tommy James and the Shondells, "Crimson and Clover" (1968).** The most famous tremolo on any pop record arrives not at the start of the song but at its hypnotic, fading end, where Tommy James's voice and guitar dissolve into a deep, slow, watery pulse on the repeated title phrase. The legend, which James has recounted in interviews over the years, is that the effect was achieved partly by running vocals and guitar through a tremolo — commonly cited as an amp's tremolo circuit — set to a luxuriant, slowish rate, producing that famous underwater wobble on the words "crimson and clover, over and over." The pulse is deliberately *not* locked tight to the beat; it floats just loose enough to feel dreamlike rather than mechanical, which is the whole point. The tremolo here isn't driving the groove; it's dissolving the song into color, turning a simple two-word refrain into a slowly breathing wash. It is the sound of psychedelia learning that an effect could be a feeling.

**Creedence Clearwater Revival, "Born on the Bayou" (1969), from *Bayou Country*.** John Fogerty opens this song with one of the great tremolo statements in rock: a dark, swelling, reverb-soaked figure that conjures heat and water and dread before he sings a word. The lore, repeated across gear circles and broadly consistent with Fogerty's own descriptions of his rig, places him with a Rickenbacker through a **Kustom** amplifier whose built-in tremolo supplied that thick, throbbing pulse, drenched in spring reverb. Whatever the exact box, the *technique* is textbook swamp tremolo: a relatively slow rate, deep intensity, dark tone, low strings, the pulse swelling each held note so the riff seems to rise out of the mud and sink back into it. Fogerty's genius was to treat the tremolo as atmosphere and rhythm at once — the throb is both the humidity hanging in the air and the pulse that makes your head nod. Set a bridge-into-neck tone roll-off, a slow-to-moderate tremolo with high intensity, a good slap of reverb, and you are most of the way to the bayou.

**Bo Diddley, "Bo Diddley" (1955).** Before the others, before psychedelia, there was the pulse. Bo Diddley's tremolo is the foundation stone of the entire effect's place in rock and roll. Playing his rectangular Gretsch through a tremolo — the effect built into his amplifier, set fast and deep — Diddley fused the amplifier's throb with his own relentless, syncopated strumming to create the rhythm now known the world over as the **Bo Diddley beat**, that "shave-and-a-haircut" clave pattern that powered "Bo Diddley," "Who Do You Love," and an entire lineage of songs that followed. Crucially, Diddley's tremolo is *fast* — a shimmering, almost machine-gun flutter rather than a slow swell — and he plays it not as a special effect but as a permanent texture, a maraca-like shimmer riding on top of the beat. He understood before almost anyone that an effect could become an identity. The throb wasn't decorating his sound; it *was* his sound, as recognizable as a fingerprint.

And a fourth, because no chapter on this effect is complete without it: **the Smiths, "How Soon Is Now?" (1984).** Johnny Marr's intro is the most ambitious tremolo on any record, and it is a masterclass in locking rate to tempo. Marr and producer John Porter, by Marr's own accounts in numerous interviews, built that shivering, jittering shimmer by running a slide-guitar figure through *multiple* amplifiers each fitted with tremolo, then painstakingly syncing the tremolo rates together — tuning each amp's Speed until the pulses lined up into one tight, hard, fast tremolo locked precisely to the track. The result trembles like nothing before it: a vast, metallic, anxious shudder that is unmistakably the sound of that song from its first second. Where Diddley's tremolo shimmers and Fogerty's swells, Marr's *vibrates*, fast and locked and relentless, proof that the oldest amplifier effect still had radical new sounds left in it three decades after Leo mislabeled the switch.

## A Single Line, Pulsing

The last example strips everything away: one note at a time, a melodic riff sent through tremolo so each pitch flickers as it sounds. This is the surf-and-spaghetti-western texture, the lonesome single-string line that flickers like heat haze.

```
Tempo: ~100 bpm. Tremolo RATE eighth notes, moderate intensity.
Neck pickup, lots of reverb. Let each note breathe and flicker.

e|------------------------------------------|
B|------------------------------------------|
G|------------------------------------------|
D|---------------------5~-------------------|
A|--3----5----7----5-------3----0-----------|
E|------------------------------------------|
   A    B    C#   B   D    A    open A~
   minor-pentatonic-flavored line over A

A single tremolo'd melody — amp flicker plus finger vibrato (~).
```
*A slow, vocal single-note melody drawn from the A minor pentatonic shape; the eighth-note tremolo makes each sustained note flutter and the held notes (marked ~ for finger vibrato) shimmer twice over — amp tremolo on the volume, hand vibrato on the pitch. Set Speed against the click, Intensity to roughly half so the notes flicker without fully chopping out.*

That melody is built from the **minor pentatonic scale**, the five-note pattern (root, flat third, fourth, fifth, flat seventh — here A, C, D, E, G) that is the mother tongue of blues and rock lead playing. Drop in the flat fifth between the fourth and fifth and you'd have the full **blues scale**; leave it out and you have the clean, plaintive pentatonic that suits a single tremolo'd line so well, because the scale's wide, gapped intervals give each flickering note room to be heard as its own event. Note the two layers of wobble in that last example: the *amplitude* flickering from the amp's tremolo and the *pitch* shimmering from the fretting hand's true vibrato (the ~ marks). Stacking real hand vibrato on top of amp tremolo is the oldest trick for making a held note feel alive in two dimensions at once — pitch and volume both breathing — and it is precisely the distinction the front-panel labels never managed to keep straight.

There is a reason this humble effect outlasted so many flashier ones. Tremolo asks almost nothing of the player — flip a switch, set two knobs — yet it changes the most fundamental thing about a note after pitch itself: how it lives and dies in time. It taught guitarists that the air between notes could pulse, that a single chord could groove, that an amplifier was not merely a thing that got loud but a collaborator that could keep time. Every modern modulation effect — the phasers and the choruses and the auto-panners — descends from that little neon lamp glowing on a photocell, or that power tube being gently throttled twice a second, making the room breathe before a string is even struck.

> **Listen For**
>
> - **Bo Diddley, "Bo Diddley" (1955):** a *fast*, deep tremolo flutter riding the maraca-like clave beat — hear how the amp's pulse becomes part of the rhythm itself, not an effect on top of it.
> - **Creedence Clearwater Revival, "Born on the Bayou" (1969):** the dark, slow, reverb-drenched swelling figure of the intro — feel the pulse swell and sink on each held note, atmosphere and groove fused.
> - **Tommy James and the Shondells, "Crimson and Clover" (1968):** the famous *loosely* synced, underwater tremolo on the fading "over and over" outro — notice it floats just off the beat, dreamlike rather than locked.
> - **The Smiths, "How Soon Is Now?" (1984):** Johnny Marr's intro — multiple tremolos painstakingly synced into one fast, hard, tightly locked shudder; the gold standard for matching tremolo *rate to tempo*.
> - **Any blackface Fender at idle (e.g. a Deluxe Reverb demo):** flip the "Vibrato" switch with no playing — that smooth, rounded optical pulse in the hum is the photocell breathing, and remember: the label says vibrato, but your ears are hearing tremolo.
