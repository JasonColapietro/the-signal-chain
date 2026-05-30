# Chapter 24 - Chorus, Flange, and the Modulation Boom

The opening seconds of "Walking on the Moon" are almost nothing at all. A bass note walks up, the hi-hat ticks, and then Andy Summers plays a single chord and lets it hang in the air like vapor rising off wet pavement. It is not a power chord. It is not a barre chord you would recognize from a beginner's book. It is a strange, suspended, bell-like thing -- a chord with a major second ringing inside it where you expect a third -- and it has been smeared with something that makes it sound as if two guitars are playing slightly out of tune with each other, drifting in and out of phase, never quite settling. That shimmer is chorus. That hanging dissonance is an add9. Together they define a sound so specific to a moment in time that you can practically smell the early-1980s reverb in it. This chapter is about that shimmer, and about its rowdier cousin, the flanger -- the two effects that turned the dry electric guitar into a wide, three-dimensional, watery instrument, and that ruled roughly a decade of records from new wave to arena rock to the first tremors of grunge.

## The Physics of Doubling a Sound

Both chorus and flange are built on the same humble trick: take the guitar signal, delay a copy of it by a tiny amount, and mix that delayed copy back with the original. Everything interesting flows from how short the delay is and whether it moves.

To understand why a delayed copy changes the tone rather than simply doubling the volume, you have to think about what happens when two identical waves arrive slightly out of step. Sound is a wave -- a pattern of pressure peaks and troughs marching past your ear. If you add a wave to a delayed copy of itself, some frequencies will line up peak-to-peak and reinforce (they get louder), while others will line up peak-to-trough and cancel (they vanish). Which frequencies do which depends entirely on the delay time relative to each frequency's period. The mathematical result is a series of evenly spaced notches carved out of the frequency spectrum, with peaks in between -- a shape that, if you drew it, looks exactly like the teeth of a comb. Engineers call this **comb filtering**, and it is the beating heart of every modulation effect in this chapter.

Now make that delay time change continuously. If you slowly sweep the delay from very short to slightly longer and back, the comb's teeth slide up and down the spectrum -- notches rising, peaks falling, a moving pattern of reinforcement and cancellation. The thing doing the sweeping is a **Low Frequency Oscillator**, or LFO: a circuit that generates a slow, smooth cycling voltage, usually well below the range of hearing, somewhere between a fraction of a hertz and a few hertz. The LFO does not make sound itself. It is a hand on a dial, gently and rhythmically turning the delay time up and down. The shape of its motion (a smooth triangle or sine wave, typically) and its speed (Rate) and how far it pushes the delay (Depth) are the parameters that separate a seasick wobble from a tasteful glimmer.

So what divides chorus from flange? Two things: the length of the delay and what you do with the comb.

A **flanger** uses a very short delay -- roughly 1 to 10 milliseconds -- and sweeps it. At those delay times the comb's notches are spaced far apart and sit high in the spectrum, and as the LFO sweeps them they swoop dramatically across the audible range. That swooping, hollow, whooshing rush is the famous "jet plane" sound. The effect's name comes from the studio technique that birthed it: engineers in the 1960s would run two identical tape machines playing the same recording, then drag a finger on the flange (the rim) of one tape reel to slow it a hair, sliding it out of sync with the other. The shifting cancellation between the two reels produced that sweeping whoosh. Les Paul had toyed with the idea years earlier, and the technique flowered on records like the Small Faces' "Itchycoo Park" in 1967. Critically, most flangers add **feedback** (sometimes labeled Regeneration or Resonance): a portion of the output is fed back into the delay input, which sharpens and intensifies the notches until they ring and whistle, turning a gentle sweep into a dramatic, metallic, vocal swoosh.

A **chorus** uses a longer delay -- roughly 15 to 35 milliseconds -- and rather than relying on the comb's notches for its character, it modulates the delay time to continuously vary the pitch of the delayed copy. Here a second piece of physics enters: the Doppler effect. When you change the length of a delay line in real time, you are effectively stretching and compressing the delayed signal, which raises and lowers its pitch -- the same reason a passing siren drops in pitch as it recedes. So a chorus produces a delayed copy that is constantly, microscopically sharp and then flat relative to the dry note, by a few cents at most. Layer that gently detuned, slightly-late copy under the original and you get exactly what you hear when two players play the same part: not robotic unison but a living, breathing thickness, a shimmer of two slightly different pitches beating against each other. That is why the effect is named for a choir. A choir is never perfectly in tune with itself, and that imperfection is its richness. Chorus does not usually use feedback, and its delay is long enough that the comb-filter notches sit low and dense and matter less than the audible detuning. The boundary is genuinely fuzzy -- a chorus is, in a real sense, just a flanger with a longer delay and no feedback -- but in practice the two sound nothing alike, and players reach for them for opposite reasons.

The technology that made these effects affordable and put them on the floor in front of every guitarist was the **bucket-brigade device**, or BBD: an analog integrated circuit, commercialized at scale in the 1970s, that passes an audio signal down a long chain of tiny capacitors like a fire brigade passing buckets of water hand to hand. Clock the chain fast and the signal comes out quickly (short delay); clock it slower and it takes longer (longer delay). Wire the LFO to the clock and you can sweep the delay smoothly. BBDs were never perfectly clean -- they added a soft, slightly dark, slightly grainy character as the signal degraded down the line -- and that warmth became part of the sound. When players say a vintage analog chorus sounds "warmer" than a digital one, they are largely hearing the gentle high-frequency loss and subtle noise of the bucket brigade.

## The Boxes That Defined the Sound

The modulation boom had a clear ground zero in Hamamatsu, Japan, at Roland and its pedal division, Boss. In 1975 Roland released the **Roland JC-120 Jazz Chorus**, a solid-state amplifier with two 12-inch speakers and a built-in stereo chorus that became, against the grain of an era that worshipped tube warmth, one of the most influential amps ever built. The JC-120's trick was to split the signal in stereo: the dry guitar went to one speaker while a chorused, pitch-wobbled version went to the other, and the LFO pushed the two in opposite directions. The result was enormous width -- a clean tone that seemed to wrap around the room. Its glassy, almost stainless-steel cleanliness made it a favorite of players who wanted clarity rather than grit, and you can hear its distinctive chorused chime across countless new wave and post-punk records.

Boss extracted that circuit into a stompbox. The **Boss CE-1 Chorus Ensemble** of 1976 was the first dedicated chorus pedal -- a big, heavy box that contained essentially the JC-120's chorus plus a vibrato mode, running on the same Doppler-style pitch modulation. It was glorious and unwieldy. Three years later Boss shrank the concept into the compact, sea-foam-green **Boss CE-2** (1979), a single-output chorus with just two knobs, Rate and Depth, that became the template for the modern chorus pedal and one of the most-used effects of the 1980s. Its sound is the quintessential chorus: liquid, glassy, a touch dark from its bucket-brigade heart, never harsh.

Across the Atlantic, in New York, Mike Matthews's Electro-Harmonix built the wilder end of the spectrum. The **Electro-Harmonix Electric Mistress**, introduced in the mid-1970s, was a flanger that could also hold a fixed "filter matrix" position, freezing the comb in place for a hollow, vocal, stationary tone. It is a lush, slightly noisy, gloriously seasick flanger, and it sits at the center of one of the most famous clean-guitar sounds ever recorded. Meanwhile the California company **MXR** built the flanger as a piece of pro audio: the orange **MXR Flanger**, with its sliders for Manual, Width, Speed, and Regeneration, delivered a deep, hi-fi, dramatically swept flange that, pushed to extremes, produced the metallic jet-engine roar that hard rock fell in love with. The **A/DA Flanger** of 1977 took the resonance even further, capable of an almost ring-modulated, otherworldly sweep.

## Andy Summers and the Architecture of Space

No player understood the new modulation more completely than Andy Summers of The Police. While punk demanded loud, fast, distorted barre chords, Summers did almost the opposite. He played clean, he played wide, and he played chords that left holes in the middle. His central discovery was that the **add9** chord -- a major triad with the ninth (the second scale degree, an octave up) stacked on top, but crucially without removing the third -- is the perfect food for chorus.

Here is the theory. A plain major chord is the 1st, 3rd, and 5th notes of the major scale: in A major, the notes A, C#, and E. The "9th" is the same note as the 2nd degree (B), just voiced an octave higher. Add it without removing anything and you get A--C#--E--B, a chord that contains both the bright major third and the ringing, unresolved major second between the B and the C# sitting near each other. That close interval -- a major second, two adjacent white keys, the most gently dissonant interval in tonal music -- creates a soft internal beating, a tension that never quite resolves. Now run that through a chorus, which detunes a copy of the whole chord by a few cents: the already-beating ninth starts beating against its own slightly-flat twin, and the chord blooms into a wide, glassy, suspended cloud. The chorus does not just thicken the add9; it amplifies the very quality -- gentle, unresolved shimmer -- that makes the add9 beautiful.

Summers favored a **Fender Telecaster** (famously a heavily modified 1963 model) into the chorus and a clean amp, and he voiced these chords high on the neck so the close intervals rang out clearly rather than muddying in the bass. "Message in a Bottle" rides a relentless arpeggiated sequence of these tall, suspended shapes; "Every Breath You Take," from 1983's *Synchronicity*, is built almost entirely on an add9 figure picked across the strings with a clean, lightly modulated tone that has launched a thousand wedding bands. The effect on the records was usually a chorus in the family of the Boss CE-1, often into a clean amp, with the LFO set slow and the depth modest -- enough to widen and gild the sound without seasickness.

Here is a Police-style figure in the spirit of those records. The point is the voicing, not speed: let every note ring into the next.

```
Aadd9             Esus4             F#m11             Dadd9
Slow, ~120 BPM, clean tone with a slow, shallow chorus. Let all notes ring.

e|--0-------0-------|--0-------0-------|--0-------0-------|--0-------0-------|
B|----2-------2-----|----0-------0-----|----0-------0-----|----3-------3-----|
G|------2-------2---|------2-------2---|------2-------2---|------2-------2---|
D|--2---------------|--2---------------|--2---------------|--0---------------|
A|--0---------------|--2---------------|--4---------------|------------------|
E|------------------|--0---------------|--2---------------|------------------|

Police-style add9 / suspended figure -- open high strings drone while the bass moves.
```

Each shape keeps the open high E and B ringing as a drone while the bass moves underneath -- the close intervals (the 9ths and suspended 4ths) are what the chorus blooms into width.

## Flange in the Hands of the Heavy and the Spacious

If Summers used chorus to build cathedrals of air, two other players showed what a flanger could do at opposite emotional poles. **David Gilmour** of Pink Floyd reached for flange to make the guitar sound like weather. On the long, mournful solos and arpeggios of records around *Animals* and *The Wall*, Gilmour ran an Electric Mistress in the chain, and you can hear its slow, hollow, vocal sweep widening his clean and lightly overdriven tones into something oceanic. The flanger's stationary "filter matrix" voicing in particular gave certain passages a fixed, hollow, almost underwater coloration -- a comb frozen mid-spectrum, scooping out the middle so the notes sound like they are reaching you through deep water. Gilmour's flange is patient. It breathes on the scale of a held bend, not a fast riff, and it pairs beautifully with his preference for vocal, blues-derived phrasing built on the **minor pentatonic** scale (the five notes 1--b3--4--5--b7) bent and sustained until each note becomes its own event.

Then there is **Eddie Van Halen**, who used a flanger as a weapon. By 1978 Eddie had an **MXR Flanger** in his rig, and he deployed it not for ambient wash but for impact -- to make a heavy riff lift off. The intro to "Unchained," from 1981's *Fair Warning*, is the textbook case: a thick, palm-muted, drop-tuned power-chord riff (Eddie tuned down roughly a half to full step on much of that record) suddenly drenched in the slow, deep sweep of the flanger, so the chords seem to inflate and breathe as they ring. On "Ain't Talkin' 'Bout Love," from the 1978 debut, a flanger colors the now-iconic clean-ish minor riff, adding a swirling motion that keeps a very simple two-finger chord pattern hypnotically alive. Eddie's flange settings are debated -- the famous "brown sound" mythology surrounds his whole rig, and exact pedal positions are commonly cited but rarely confirmed -- but the principle is plain: set the LFO slow, the depth deep, and a healthy dose of regeneration, and a static power chord acquires a sense of enormous, swelling movement.

The theory worth knowing here concerns the power chord itself. A **power chord** (notated "5," as in A5) is not really a chord in the harmonic sense at all: it is just the root and the fifth, with no third. The interval of a perfect fifth (the 5th degree above the root, the most consonant interval after the octave) is so stable and so free of the third's major/minor coloring that it stays clean and huge even under heavy distortion, where a full triad would turn to mud as the distortion generates intermodulation between the closely spaced overtones. Strip a chord to root and fifth and you can pile on gain, volume, and a flanger's sweep without the harmony collapsing. That austerity is exactly why the power chord and the flanger are such natural partners: the flanger supplies all the motion and complexity the bare interval lacks.

Here is a flanged power-chord riff in that arena-rock spirit. Palm-mute the chugs tightly and let the ringing chords open up so the sweep can bloom.

```
Heavy, ~132 BPM. Flanger: slow rate, deep, with strong regeneration. PM = palm mute.

e|------------------|------------------|------------------|------------------|
B|------------------|------------------|------------------|------------------|
G|------------------|------------------|---------------7~-|------------------|
D|--5-5-5--7--------|--5-5-5--7--------|--5-5-5--7--5~~--7~|------5--7~~-------|
A|--5-5-5--7----5--7|--5-5-5--7----5--7|--5-5-5--7--5~~--7~|--5--7-5--7~~------|
E|--3-3-3--5----3--5|--3-3-3--5----3--5|--3-3-3--5--3~~--5~|--3--5----5~~------|
   PM                PM                 PM

Flanged power-chord riff -- tight palm-muted chugs, then held chords for the sweep to bloom.
```

The fast palm-muted G5 chugs stay tight and dry-sounding because the flanger's sweep is too slow to color short notes much; the held, vibratoed chords at the end of the phrase are where the jet-plane swoosh swells up and inflates the sound.

## "Come as You Are" and the Watery Return of Chorus

By the late 1980s, chorus had become so ubiquitous -- on guitars, on basses, on synth pads, on snare drums -- that it began to read as a cliche of expensive, glossy studio production. It took a band that despised expensive gloss to make it sound dangerous again. Kurt Cobain of **Nirvana** owned an **Electro-Harmonix Small Clone**, a simple two-knob chorus with a single Rate knob and a Depth toggle, and on "Come as You Are," from 1991's *Nevermind*, he used it to drown the song's main riff in a thick, watery, deliberately murky wobble.

The Small Clone's chorus is wetter and more obvious than the polite Boss CE-2 -- its depth runs deeper, so the pitch wobble is more pronounced, and the effect sits forward in the mix rather than discreetly widening it. Cobain played the riff low, down on the bottom strings, on a guitar tuned down a whole step (so the notes sound a step lower than written), and the combination of the low register, the down-tuning, and the heavy chorus produces that famous submerged, queasy, underwater quality -- as if the riff is being played in a flooded basement. It was a brilliant subversion: he took the prettiest, most overused effect of the previous decade and made it sound cold, narcotic, and unsettling. The same Small Clone shows up elsewhere in Nirvana's catalog, lending the clean verse arpeggios of other songs a similar watery shimmer that throws the explosive distorted choruses into sharp relief.

The musical lesson is one of register and contrast. Chorus on high, open, jangly add9 chords (Summers) sounds bright and celestial; the very same effect on low, single-note riffs played on the wound strings sounds thick, dark, and seasick, because those low fundamentals beat more slowly and audibly against their detuned copies. Same circuit, opposite emotional worlds, governed entirely by where on the neck you put your hands.

Here is an original watery clean line in that spirit -- low, simple, hypnotic, built to be soaked in chorus.

```
Mid-tempo, ~120 BPM. Heavy chorus: moderate rate, deep depth. Bridge pickup, clean, slightly compressed.

e|------------------------------------------------------------|
B|------------------------------------------------------------|
G|------------------------------------------------------------|
D|------------------4-2---------------------4-2-------2--------|
A|--2---2-2--4-2-0----------2---2-2--4-2-0-----------0h2---0---|
E|----------------------------------------------3-------------|

Watery clean line on the wound strings -- the chorus, not your hand, supplies the movement.
```

Played on the wound strings with a deep chorus, the slow pitch wobble makes each low note shimmer and curdle; keep the picking even and let the effect, not your hand, supply the movement.

## A Decade of Motion

The modulation boom did not invent these effects -- the tape-flange whoosh and the doubled-track shimmer predate the stompbox by years -- but the bucket-brigade chip democratized them, and a generation of players discovered that the dry electric guitar could be opened up into something wide, liquid, and dimensional without ever touching the distortion knob. Chorus gave the clean guitar a choir's living imperfection; flange gave it the rush of moving air and, with enough regeneration, the scream of a jet. Between them they colored the sound of an entire era, and they remain on pedalboards today for the simplest of reasons: a single guitar, alone, can sound like a crowd, a tide, or a passing storm, all from the same modest trick of delaying a sound and mixing it with itself.

> **Listen For:**
>
> - **The Police, "Walking on the Moon"** (*Reggatta de Blanc*, 1979) -- Andy Summers's hanging add9 chord at the top: hear the close major-second beating *inside* the chord, then the slow chorus widening it into vapor. The space around the chord is as important as the chord.
> - **The Police, "Message in a Bottle"** (*Reggatta de Blanc*, 1979) -- the arpeggiated tower of suspended/add9 shapes; listen to how the high open strings ring on as drones while the chorus gilds the whole figure.
> - **Pink Floyd, "Dogs"** (*Animals*, 1977) -- David Gilmour's clean and overdriven passages through the Electric Mistress; hear the slow, hollow, vocal sweep and the scooped, underwater coloration of the flanger's filter-matrix voicing.
> - **Van Halen, "Unchained"** (*Fair Warning*, 1981) -- the opening riff: a thick, down-tuned power-chord figure suddenly swept by the MXR Flanger. Notice how the held chords seem to inflate and breathe while the tight palm-mutes stay dry.
> - **Van Halen, "Ain't Talkin' 'Bout Love"** (*Van Halen*, 1978) -- the flanged minor riff; a simple two-finger pattern kept hypnotic by slow swirling motion.
> - **Nirvana, "Come as You Are"** (*Nevermind*, 1991) -- Kurt Cobain's Small Clone chorus on the main riff: low, down-tuned, and deliberately murky. Hear how the deep pitch wobble turns a simple line submerged and queasy -- the same effect Summers used for brightness, here used for unease.
