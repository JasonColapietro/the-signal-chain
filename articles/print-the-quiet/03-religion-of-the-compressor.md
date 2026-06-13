# The Religion of the Compressor

### Glue, breath, parallel, crime — and why engineers talk about a piece of gear as if it were a god

**By Jason Colapietro, Founder and CEO of Suede Labs** · *A Suede Social long read.*
*Print the Quiet, no. 3.*

---

If you spend any time around recording engineers, you learn that the compressor is not just a device. It is a religion. They will argue for hours about it, in language closer to theology than electronics. *This one breathes.* *That one glues.* *This one feels alive.* *That one is dead.* They will spend $4,000 on a single channel of hardware because the input transformer is wound differently. They will discount a plugin shootout that they would have called definitive last week because today they tracked through an actual 1176 and remembered what the real one does.

This is the third piece in the **Print the Quiet** series, and it is about that religion. What a compressor actually does. The lineage of the canonical units. The art of using one, and the crime of using one badly. And why engineers talk about it the way they do — because compression, more than any other tool in the studio, is where a piece of recorded music gets its body.

---

## The mechanism, plainly

A compressor reduces dynamic range by attenuating signal above a chosen threshold according to a ratio. Five controls govern the result.

**Threshold** is the level above which the compressor starts working. Below threshold, the signal passes untouched.

**Ratio** is how aggressively the compressor reduces signal above threshold. A 4:1 ratio means for every 4 dB above threshold, only 1 dB comes out. Anything above 10:1 is effectively limiting — the compressor refuses to let the signal grow further.

**Attack** is how quickly the compressor clamps down after the threshold is crossed. Fast attack catches transients (the snap of a snare hit, the consonant in front of a vowel). Slow attack lets transients through and only clamps on the sustain that follows — which preserves the snap but sacrifices peak control.

**Release** is how quickly the compressor lets go. Too short, and the compressor "pumps" — you hear it grabbing and releasing in time with the music. Too long, and the compressor stays clamped, choking the next phrase.

**Knee** is how gradually compression engages around the threshold. A hard knee is abrupt; a soft knee feels transparent and musical.

There is also the detection method. **Peak** detectors react to instantaneous transients — the 1176 is a peak-style FET compressor. **RMS** detectors average signal level over a window and feel more like the way the ear perceives loudness — the dbx 160 and the LA-2A live in that world.

That's it, mechanically. Every compressor is a variation on those parameters. The religion lives in the variations.

---

## The lineage

A short canon, with the technical detail that matters to engineers and the cultural detail that matters to anyone trying to understand why pre-1995 records sound the way they do.

**Fairchild 660 / 670 (1959).** Designed by Rein Narma at the Fairchild Recording Equipment Corporation. The 670 is the stereo dual-mono version, with 20 tubes (the mono 660 has 11). Both use the rare 6386 remote-cutoff tube. Geoff Emerick brought the Fairchild into the Beatles' chain at Abbey Road starting with *Revolver* — Beatles vocals, Ringo's drum bus on "Tomorrow Never Knows," piano. Used 660s now sell for $20,000 and up; 670s push past $40,000. Tony Visconti, who has used a Fairchild on most David Bowie records: *"The Fairchild was the go-to black box of sonic glue for the entire drum kit or the bass guitar, or even both."* It is the original color compressor. You hear it on records the way you hear weather in a memory.

**Teletronix LA-2A (1962).** Jim Lawrence's electro-optical tube leveling amplifier. The mechanism is unusual: an internal element called a T4 cell converts the audio into light, the light hits a photoresistor, and the photoresistor controls the gain. Because optical attack is naturally slow and program-dependent, the LA-2A is the vocal compressor — slow enough to not interrupt phrases, even enough to feel transparent on long sustained notes. It has, famously, two knobs: peak reduction and gain. There is no attack control. There is no release control. There is no ratio control. It does what it does, and the engineer's only decision is how much. The simplicity is the religion. (Side note: the "1965" date often cited is the year Babcock Electronics acquired Teletronix's patents; the unit itself was introduced 1962.)

**UA 1176 (1968).** Bill Putnam's FET (field effect transistor) compressor, peak-detecting, famously fast — attack times as short as 20 microseconds. The aggressive one. The lead-vocal-in-modern-pop one. The drum-bus one. Revisions matter:

- **Rev A "Bluestripe"** (1967-68): no low-noise circuitry, gritty, distorted, the most aggressive-sounding rev.
- **Rev C, D, E** (1970-73): the LN low-noise circuit added; the most revered revs and the basis of modern UA reissues.
- **Rev H "Silverface"** (mid-70s): input transformer removed, replaced with an op-amp input — the cleanest-sounding rev.

The 1176's defining party trick is the "all-buttons-in" / British Mode: pressing all four ratio buttons at once produces a non-linear, aggressive, harmonically rich squash. The unit was never designed to do this. An engineer pressed the buttons by accident, liked it, and the move entered the canon. The most famous compressor color in pop music is a happy hardware bug.

**dbx 160 (1976, not 1971 — that's the year David Blackmer founded dbx).** The first commercially successful VCA (voltage-controlled amplifier) compressor. Hard-knee, fast, punchy. The drum-room sound of the late 1970s and 1980s — Hugh Padgham, Bob Clearmountain, anyone tracking rock drums with serious attack. The Blackmer Gain Cell, patented in 1973, is the technical foundation of the VCA compressor as a category.

**SSL G-bus compressor.** First appeared on the SSL 4000 B (1976), refined on the 4000 E (1981), reached definitive form on the G-series in 1987. Built into every SSL console's center section. VCA-based, feed-forward topology, derived from a dbx 202 black-can VCA chip. Because every SSL console had one, every record mixed on an SSL from 1985 to 2005 had at least the option to glue the 2-bus with this comp. Most did. The "SSL sound" — the bright, cohesive, slightly-over-glued mid-period CD-era pop master — is partly this one chip.

**Empirical Labs Distressor (1995).** Dave Derr, who had been an Eventide engineer working on the H3000, designed the Distressor as a digitally-controlled analog compressor with mode switches that emulate the behavior of an LA-2A, a Fairchild, an 1176, and tape. "Dist 2" emphasizes second-harmonic content (tube-like); "Dist 3" emphasizes third-harmonic (tape-like); "Opto" mode produces LA-2A behavior. The Distressor is the most-used outboard compressor in modern professional studios because it can play any role in a session. It is the Swiss Army of the rack.

**Manley Variable Mu (1994).** EveAnna Manley's tube compressor, using the same remote-cutoff tube transconductance gain reduction mechanism as the Fairchild. Soft, slow, expensive. The mastering 2-bus and tracking-bus comp for engineers who want analog tube character without the Fairchild's price tag (which is, charitably, ridiculous).

---

## The craft

There are two kinds of compression. Compression you *hear*: the pumping 1176 on a drum bus that you can audibly hear breathing in time. The released kick that lets the room come up between hits. The vocal that compresses you can hear working on the consonants. That is sometimes the point — Phil Collins's "In the Air Tonight" gated reverb on the drums depends on a compressor and a gate you can identify by ear.

Compression you *feel*: the SSL bus comp doing 1 to 2 dB on the master and you don't notice it until you bypass it and the mix falls apart. The light Fairchild on a vocal bus that adds tube color and "glue" without changing the shape of any phrase. The Distressor on a bass guitar that locks the bottom end in place so the kick can punch through.

The terms engineers use here — *glue*, *breath*, *body*, *air* — are not metaphorical. They are physical descriptions of what compression does to the cumulative envelope of a mix. *Glue* is when several sources start sharing the same dynamic envelope, so they feel like one event instead of five layered events. *Breath* is the audible release of a slow comp letting go between phrases. *Body* is the gain-reduction that pulls the sustained portion of a note up relative to the transient. *Air* is what you have left in the high frequencies when the compressor hasn't eaten them.

The fastest way to learn the difference between compression you hear and compression you feel is to put a stereo bus compressor across the mix bus, set it to a 2:1 ratio with a slow attack and an auto release, and watch the meter. If the needle is moving 1 to 2 dB at the peaks, you are doing it right. If the needle is jumping 8 dB on every chorus, you are doing it wrong — you have replaced the song's dynamic shape with a mechanical breathing pattern.

---

## Parallel, sidechain, multiband

Three techniques worth naming.

**Parallel compression** — sometimes called the New York drum trick — runs a heavily-compressed copy of a signal on a separate channel and blends it back under the original uncompressed signal. The compressed copy supplies the body and the sustain; the uncompressed original supplies the transient snap. The blend gives you body without losing punch. Bob Clearmountain popularized it on Springsteen, the Stones, and Bryan Adams. The term "New York Compression" was coined by Bobby Owsinski in *The Mixing Engineer's Handbook* (1999), but the technique predates the term — Motown's "exciter" bus on vocals in the 1960s was a parallel scheme, and the internal architecture of Dolby A noise reduction (1965) was built on parallel encode/decode buses. Andrew Scheps formalized parallel compression into his whole-mix philosophy: a post-fader send of every track in the mix (except the drums) into a single stereo aux bus, smashed hard, blended back at low level under the main mix. He calls it the "rear bus" because, on the Neve quad console where he developed the technique, the unused quadraphonic rear bus became his parallel comp send. The technique is now standard practice in pop mixing.

**Sidechain compression** uses one signal to trigger the compression of another. The most familiar version is the kick-side-chained-bass trick of house and EDM music — every kick triggers the bass to duck briefly, making space in the low end. The technique works equally well, and more subtly, in pop and rock: side-chaining a synth pad to the lead vocal so the pad ducks whenever the vocal is present. Side-chaining a reverb return to the dry source so the reverb only blooms in the gaps. Used judiciously, sidechain compression is invisible.

**Multi-band compression** splits the signal into frequency bands and compresses each independently. Useful for problem-solving — taming a resonant frequency on a vocal, glueing a too-broad master, fixing a mix that should have been remixed. It is also the cardinal sin of mastering engineers who use it as a substitute for actually fixing the source mix. There is a saying among older engineers: if you need multi-band compression to make a mix work, the mix is wrong.

---

## The signature uses

A short list of who did what, and why it matters.

**Geoff Emerick on the Beatles.** Fairchild 660 on Ringo's drum bus on "Tomorrow Never Knows" (the loop-driven *Revolver* track) — the compressed kit becomes part of the song's drone. The same Fairchild on Lennon's vocals from *Sgt. Pepper* onward, giving the vocal that tube-glued forward presence that has never quite been replicated since.

**Hugh Padgham on Peter Gabriel and Phil Collins.** The "gated reverb" sound of the 1980s — first heard on Peter Gabriel's *third* self-titled album (1980), then on Phil Collins's "In the Air Tonight" (1981, with Collins playing the drums) — was not actually invented as a reverb trick. It was an accident. The SSL 4000 console's talkback mic had a built-in heavily-compressing limiter (so studio chatter could be heard at low level), and Padgham discovered that routing the drum room into the talkback compressor and then through a gate produced an enormous, slamming, distinctly-1980s drum sound. The gated reverb is a compressor's accident.

**Bob Clearmountain on Springsteen and Bryan Adams.** Parallel compression on drums, drum-sample reinforcement, fast 1176-style on lead vocals. Clearmountain's mixes from 1982 to 1995 essentially defined what a rock record sounded like on commercial radio.

**Andrew Scheps on Adele's _21_** (Grammy Album of the Year): *"I probably did the least amount of processing I've ever done — one mix had only five EQs in total, a little bit of spring reverb, and a compressor across the bus, because it was just the sound of the tracks."* The restraint is the credit. Scheps's record is, in part, what he did *not* add.

**Chris Lord-Alge** (Green Day, U2, Aerosmith, Springsteen, hundreds of others): the most aggressive compression hand in mainstream rock. CLA is documented hitting 15 to 20 dB of gain reduction on a Bluestripe 1176 on lead vocals, post-EQ, with a 4:1 ratio on the master bus pulling another 7 dB. The result is hyper-real, radio-ready, slamming. You can love it or hate it; you cannot deny it works on commercial rock radio.

**Tchad Blake** (Tom Waits, Sheryl Crow, Pearl Jam): the Shure Level-Loc compressor, originally designed for paging systems and police-band radios, as a deliberate distortion-as-compression tool. Blake discovered it on Tom Waits's *Bone Machine.* His own line: *"The Level-Loc changed my life."* The Level-Loc is awful as a transparent comp and astonishing as a character tool. The lesson: a compressor's job is not necessarily to be invisible.

**Andy Wallace** (continuity from earlier in this series): on the *Grace* sessions, parallel compression on the drum bus, light Fairchild-style on Buckley's vocal, conservative SSL G-bus on the master at perhaps 2 to 4 dB of gain reduction. The dynamic range of the Grace master — DR11 to DR13 — is the receipt for what restrained, intentional compression buys you.

---

## The crime

There are bad uses too. Worth naming.

**Brick-wall mastering as compression abuse.** The loudness war (see the previous piece in this series) was, technically, compression and limiting deployed as a loudness tool rather than as an artistic tool. The mastering chain stopped trying to shape the music and started trying to make it louder. Metallica's *Death Magnetic* (2008) at DR3 is the canonical disaster. Ted Jensen, who mastered it, publicly disowned the result: *"In this case the mixes were already brick-walled before they arrived at my place. Suffice it to say I would never be pushed to overdrive things as far as they are here. Believe me, I'm not proud to be associated with this one."* The mixes — by Andrew Scheps, who knows better — had been compressed too hard before mastering even started. The compressor was being asked to do what only the song could do.

**The LANDR sound.** Algorithmic mastering services default to heavy compression because heavy compression always sounds *immediately* better in an A/B with an uncompressed source — for the Fletcher-Munson reasons explored in piece #2. Documented analyses of LANDR and eMastered outputs show crest factors as low as 11 dB (very brick-walled), hyped high-mids, dense sub-100 Hz limiting. The compressor, in these tools, is no longer being driven by an engineer's ear. It is being driven by an algorithm optimizing for "sounds loud in three seconds."

**Compression as masking.** Inexperienced producers learn, often the wrong way, that heavy compression can hide a thin vocal or an uneven drum performance. It can, briefly. The cost is that the body that was uneven shows up later — in the listener's fatigue, in the song's lack of depth, in the eventual realization that what you are hearing has been pressed flat to disguise problems that weren't worth disguising. Compression cannot fix performance. It can only smooth its surface.

---

## Why the religious language

Why do engineers talk about compressors the way mystics talk about saints?

A reasonable answer: compression is, more than EQ or reverb, the tool that most directly shapes the *body* of a recorded sound. EQ changes the spectral balance — you hear the difference in terms of frequencies. Reverb adds space — you hear the difference in terms of room. Compression changes the *envelope* of a sound through time, and envelopes through time are how the nervous system reads emotional intensity. A fast-attacked drum hit is exciting because the transient is sharp. A slow-attacked vocal is intimate because the sustain is brought forward. Compression is the tool that most directly controls *how the listener's body feels what is on the record.*

When engineers say a compressor "breathes," they mean it lets the music's natural dynamic envelope show through with subtle reinforcement. When they say it "glues," they mean it pulls several sources into a shared envelope that the body reads as one event. When they say it is "alive," they mean it is not crushing the envelope but tracking it.

These are physical descriptions, even if the language sounds spiritual. The compressor is the throat of the recording. It is the part of the chain that decides how the body of the sound arrives at the listener's body. That is why engineers talk about it the way they do.

It is also why the loudness war was a tragedy on a human scale, not just a technical one. The throat of the recording got clamped shut. The body that the listener was supposed to feel never arrived.

---

## A coda for the working producer

Three principles, from people who have spent their lives compressing things well.

**Use less.** Most engineers, including Scheps, Wallace, and Clearmountain, will tell you they compress less now than they did fifteen years ago. The instinct, when in doubt, is to add more gain reduction. The right move, almost always, is to add less.

**Listen to the release.** The single most-misset knob on a compressor is the release. A release that is too fast pumps. A release that is too slow chokes the next phrase. The right release lets go just before the next attack — which means the right release is, in some sense, defined by the song's tempo and phrasing. If your compressor's release is at one setting for the whole song, it is wrong for at least half of it. Modern compressors with program-dependent release exist for this reason.

**Bypass.** The discipline that separates competent compressionists from religious ones: bypass the compressor every few minutes. If the music sounds worse, you are compressing well. If it sounds the same, you are compressing too much. If it sounds *better* uncompressed, you have compressed too much.

The compressor is the most powerful tool in the studio and the most easily abused. Used well, it is what makes a record feel alive. Used badly, it is what makes a record feel dead. There is no neutral setting. The decision is always tonal, and tonal decisions are always moral.

Print the quiet. Compress the body. Bypass to check.

---

*Print the Quiet is a Suede Social series on tone, dynamics, and the parts of music that don't fit on a lead sheet. Next: the lost art of clean.*
