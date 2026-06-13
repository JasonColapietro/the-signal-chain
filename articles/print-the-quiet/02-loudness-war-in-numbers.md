# The Loudness War, in Numbers

### How the masters got crushed, who tried to stop it, and whether the streaming era actually ended it

**By Jason Colapietro, Founder and CEO of Suede Labs** · *A Suede Social long read.*
*Print the Quiet, no. 2.*

---

The first piece in this series argued, through Jeff Buckley's *Hallelujah,* that tone is a value system — a set of decisions about what to leave in and what to take out. The deepest single decision in modern record-making is the one a mastering engineer makes about how loud to print the master. That decision, made wrong about a million times between 1994 and 2010, took the dynamics out of pop music. This is the piece that explains, in numbers, what happened.

---

## What loudness actually means

Three measurements get used in this conversation. They are different, and the difference matters.

**Peak** is the instantaneous maximum sample value of the audio file. A peak meter reads the tallest spike. On a CD or a 16-bit WAV, peak maxes out at 0 dBFS (decibels relative to full scale). One sample at 0 dBFS, or above the digital ceiling for a true-peak meter, can produce audible clipping if the playback chain reconstructs the wave between samples.

**RMS** (root mean square) is a moving average of signal power over some window — typically 300 ms. It tells you, roughly, how much sustained energy is in the signal. Two different songs can hit the same peak but have wildly different RMS levels. The one with the higher RMS sounds louder.

**LUFS** (Loudness Units relative to Full Scale, defined in the ITU-R BS.1770 standard) is the modern measurement. It applies K-weighting — a filter that approximates the ear's frequency response — and gates out silent passages before averaging across the whole program. The result is a single number that correlates with perceived loudness across different program material in a way RMS does not. Spotify, Apple Music, YouTube, and Tidal all use LUFS for normalization.

A useful intuition: a record at -18 LUFS sounds quiet. A record at -14 LUFS sounds normal. A record at -10 LUFS sounds aggressive. A record at -6 LUFS sounds, on first listen, exciting, and on tenth listen, exhausting.

**Dynamic range** (DR, the score reported by the TT Dynamic Range Meter and the Dynamic Range Database) is loosely the difference between peak and average. A record with DR12 has 12 dB of breathing room between its quiet moments and its loud ones. A record with DR4 is essentially flatlined — its average level is almost touching its peak the whole time. Higher DR is, by most measures, healthier sound.

---

## The war, in numbers

The shift began in earnest in the mid-1990s and accelerated through the 2000s. Pre-CD-era pop and rock — late-70s through mid-80s — generally sat in the DR12 to DR14 range. By the late 1990s, average pop had moved to roughly DR8 to DR10. By the 2008 peak, mainstream releases were routinely landing at DR4 to DR6. In LUFS terms, the average integrated loudness of pop and rock masters shifted from around -18 to -20 LUFS in the early CD era to roughly -7 to -6 LUFS at the peak of the war. That is a swing of more than 10 dB — and in perceptual terms, each 3 dB doubles the apparent power.

The technical enabler arrived in 1994: the **Waves L1 Ultramaximizer**, the first mass-produced digital brick-wall limiter with look-ahead. The L2 in 1999 made the workflow routine. Sound on Sound's later assessment was succinct: "for some, the sound of the 1990s and the 2000s was the L1 and L2." Suddenly any mastering engineer with a Pro Tools rig could shave the peaks off a master and raise its apparent loudness without producing audible clipping. The temptation was nearly irresistible. Labels heard the louder masters in A/B comparisons and assumed louder was better. The psychoacoustics agreed with them — the Fletcher-Munson equal-loudness contours, first measured in 1933 and refined into ISO 226, describe how the ear's frequency sensitivity is non-flat and *changes with level*. At higher SPL the ear hears more bass and more air. So the same EQ balance appears subjectively fuller at higher loudness, in a five-second comparison. This is the technical engine of the loudness war: a louder master wins every quick A/B by default, regardless of how it actually sounds over thirty minutes.

The cost was paid by the music. Dynamics are emotional information. A song that gets quieter and then louder is telling you something about its emotional shape. Crush the master to a flat wall and that information goes missing. The quiet verse and the loud chorus sit at the same perceived volume. Every drum hit lands with the same force, because the kick that should hit hardest has been clamped down to the level of the snare ghost notes. The listener's nervous system, which is built to read dynamic change as meaning, gets nothing to read.

---

## The three canonical disasters

**Metallica, *Death Magnetic* (2008).** The textbook case. Mastered by Ted Jensen at Sterling Sound; the Dynamic Range Database lists the CD master at **DR3**, against *Master of Puppets* at DR12. Audible clipping on the snare and the cymbals. Fans noticed within hours of release that the *Guitar Hero III* DLC version, which used a less-compressed pre-master sourced from the multitracks, sounded objectively better than the retail CD — reportedly about 10 dB quieter and noticeably more dynamic. The petition asking Metallica to remix the album passed 13,000 signatures inside weeks. Ted Jensen posted publicly to a Metallica forum: *"In this case the mixes were already brick walled before they arrived at my place. Suffice it to say I would never be pushed to overdrive things as far as they are here. Believe me I'm not proud to be associated with this one."* It is the rarest of mastering documents — the engineer disowning his own master. Andrew Scheps, asked years later, put it more bluntly: *"My line is that the loudness war is over because I won. And that was the record that did it."*

**Rush, *Vapor Trails* (2002).** Original master = **DR5**. The 2013 David Bottrill remix and remaster = DR7. Geddy Lee, on record about the original: *"We overcooked it. The mixes were really loud and brash. The mastering job was harsh and distorted."* Alex Lifeson: *"It was a contest, and it was mastered too high, and it crackles, and it spits, and it just crushes everything."* The remix was not a touch-up. It was a confession.

**Red Hot Chili Peppers, *Californication* (1999).** **DR4**. Distortion audible on the slide solo of "Otherside" and on the snare across the record. Mastered by Vlado Meller at Rick Rubin's request. The 2012 180-gram vinyl reissue, cut by Chris Bellman at Bernie Grundman Mastering from less-compressed sources, is the listenable version of the same record. A whole separate master, on a different medium, exists because the original master is — let's be plain — broken.

For contrast, the triumphs of the same era and earlier. Donald Fagen's *The Nightfly* (1982), recorded on 3M's 32-track digital system and mastered by Bob Ludwig, sits at high dynamic range and is still the audiophile reference for clarity. Pink Floyd's *Wish You Were Here* original CD and the 2011/2025 remasters sit at DR11 to DR13. The Steely Dan catalog and the original Beatles masters routinely score DR12 to DR14. *Grace* — the Buckley album from the previous piece — sits in roughly the same band on the original 1994 CD; the 2004 Legacy remaster compressed it noticeably and is, audibly, the worse master.

---

## Bob Katz and the K-system

The serious technical counter-proposal came in 2000. **Bob Katz**, mastering engineer at Digital Domain, presented "An Integrated Approach to Metering, Monitoring, and Level Practices" at the 109th AES Convention in Los Angeles. The paper proposed the **K-system**: three loudness scales (K-12 for broadcast, K-14 for pop and rock, K-20 for classical and film) calibrated to a standard monitoring level of 83 dB SPL. The idea was that if labels and engineers agreed on a reference loudness and consumer playback systems delivered consistent volume, the incentive to brick-wall masters for competitive loudness would evaporate.

It did not get adopted. Labels had no incentive while the war was still profitable, and there was no consumer-side playback standard to enforce it. The K-system became a religious document — cited by every mastering engineer who took the problem seriously, ignored by most of the industry. Katz himself kept the faith. **Ian Shepherd**, the British mastering engineer, founded **Dynamic Range Day** in 2010 as an annual advocacy event. The argument was being made, persistently, that the war was a self-inflicted wound and that the music was the casualty.

---

## What streaming actually changed

The reset that the K-system could not impose, the streaming platforms imposed by accident. Around 2014, Spotify, iTunes, YouTube, and the others rolled out loudness normalization. Today's targets:

- **Spotify**: -14 LUFS integrated. Quiet tracks get turned up; loud tracks get turned down.
- **Apple Music** (Sound Check): about -16 LUFS. Apple only turns *down* loud tracks; it does not boost quiet ones.
- **YouTube**: -14 LUFS. Turns down loud tracks; does not boost quiet ones; never limits.
- **Tidal**: -14 LUFS, album-normalized by default since the 2019 update influenced by Eelco Grimm's research.
- **Amazon Music, Deezer**: roughly -14 to -15 LUFS.

The mechanism is simple. A -7 LUFS brick-walled master gets turned down 7 dB by Spotify to hit -14. A -14 LUFS dynamic master plays through untouched. To the listener, both arrive at roughly the same average level. But the brick-walled master has already had its dynamics removed at the source; the dynamic master plays back with its breath intact. *On the listener's speakers, after normalization, the dynamic master sounds louder and more alive.* The incentive flipped. For the first time in twenty years, mastering loud was the worse strategy.

Bob Katz declared the war won in early 2014. *"The debilitating loudness war has finally been won. The last battle will be over by mid-2014."* He was, on his own terms, right. The pure incentive to brick-wall is gone.

Ian Shepherd has argued, persistently, that this is the wrong question. The platforms normalize, yes — but most chart releases *still arrive at mastering already brick-walled* by the producers and mixers, before the mastering engineer even sees the file. The normalized playback of a hot master is not the same as a dynamic master normalized to the same level. The dynamic information has to have been preserved at the source for the listener's ear to receive it. A -14 LUFS playback of a -7 LUFS source still sounds crushed; it just sounds crushed at a lower volume. The war as a *practice* persists even if the war as an *incentive* has ended.

The honest answer in 2026 is that both are right. The incentive has flipped. The practice is changing slowly. Average DR of new pop releases sits around DR8 to DR10 — better than the DR4-6 trough of 2008, still well below the DR12-14 baseline of the analog era. The trend is upward. We are not back to *The Nightfly,* but we are also not living in 2008.

---

## The engineers, on the record

The mastering community has been remarkably consistent about this since the early 2000s. **Bob Ludwig**, who retired in 2023 after fifty years and roughly twelve thousand mastered albums, recalled the *Chinese Democracy* sessions of 2008 in which he supplied three masters at different loudness levels and the band chose the most dynamic one: *"Fan and press backlash against the recent heavily compressed recordings finally set the context for someone to take a stand and return to putting music and dynamics above sheer level."* He named the war as the central technical fight of his career.

**Emily Lazar**, of The Lodge, who has mastered records for David Bowie and Foo Fighters and won the Best Engineered Album Grammy: *"The loudness wars are the bane of my daily existence."*

**Howie Weinberg**, formerly of Masterdisk: *"I like nice loud files, but I don't want them crushed. There is a happy medium."*

**Andrew Scheps**, who mixed *Death Magnetic* and watched his work get crushed at the mastering stage: said in 2023 that his mixes "have gotten much quieter over the last 5-10 years." This is, in mixer-speak, an enormous statement. Scheps was famous for hot rock mixes. The reset has reached him.

**Mandy Parnell**, of Black Saloon Studios, has built a practice around mastering for dynamics on analog chains — Sigur Rós, Björk, The xx, Aphex Twin. Her records do not crush, and they do not need to.

---

## Vinyl, and the strange new vinyl problem

The vinyl revival was supposed to be the loudness war's natural antagonist. Vinyl has physical limits: the stylus has to track the groove without skipping; RIAA pre-emphasis boosts highs in cutting and rolls them off in playback; low bass eats groove width. A brick-walled digital master cannot be cut directly to vinyl without compromising stylus tracking and inner-groove distortion. The industry standard was, for decades, to cut vinyl from a separate, more dynamic master.

That separate master is increasingly being skipped. Headphonesty's April 2025 reporting documented a pattern of cheap modern vinyl pressings cut directly from the loud digital retail master. The buyer pays for the vinyl premium, and gets, sonically, the same compressed master they could have streamed for free. The loudness war has migrated, by negligence, onto the medium that was supposed to defeat it.

Audiophile labels — Mobile Fidelity, Analogue Productions, ECM, the better reissue programs — still cut vinyl properly from less-compressed sources. The mainstream catalog often does not. This is worth checking, if you care, before paying $40 for a record.

---

## The AI question

A note on what the war looks like in 2026. AI music-generation systems (Suno, Udio, the new wave) trained on commercial pop have learned, by absorption, to output already-mastered audio at brick-wall loudness. The training data taught them that this is what a finished track sounds like. There is no separate "mix" or "master" stage; the model produces a finished-sounding artifact. Third-party AI mastering services (LANDR, eMastered) further compress this output by default. The result is that AI-generated tracks are, on average, even more dynamics-flattened than human-made commercial pop.

This is a small thing and a large thing. It is small because individual AI tracks rarely get listened to at the depth where the loss of dynamics matters. It is large because the systems are training the next generation of listeners to accept compressed audio as the baseline. If your reference for "what music sounds like" is AI-generated content, you will not notice when a human record is given the same treatment, because you will not have heard the alternative.

---

## What this means for a Suede Social reader

A short coda for anyone making records.

If you are a producer, master quieter than your instinct tells you to. -14 LUFS integrated is the streaming target. Anything quieter is fine; the platform will turn it up. Anything louder will be turned down, and the dynamics you destroyed to be louder will not be restored.

If you are a label or an artist, ask your mastering engineer for two masters: a streaming master at -14 LUFS with dynamics intact, and a vinyl master cut from a less-compressed source. If the engineer cannot tell you the LUFS or the DR of what they're delivering, get a different engineer.

If you are a listener, the easiest test is this. Take a record you love that was made before 1990 and a current chart record. Play them at the same volume on the same speakers. Listen to the quiet moments. The old record will have moments that are quieter than the chart record's quiet moments. Those quiet moments are the dynamics that the modern record gave up to be louder. They are also, almost always, where the song's emotional information lives.

The war is mostly over. The damage is partly reversible. The recipe is in every Bob Katz paper, in every Bob Ludwig master from 1976 to 2023, in every Andy Wallace mix that left room for the breath. *Hallelujah,* in 1994, had room for the breath. That is why it still sounds alive.

Print the quiet. Master the quiet too.

---

*Print the Quiet is a Suede Social series on tone, dynamics, and the parts of music that don't fit on a lead sheet. Next: the religion of the compressor.*
