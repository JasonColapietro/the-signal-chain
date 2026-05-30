# Chapter 23 - Echo and Delay: Tape, Analog, and Digital

The first thing you hear on so many great records is not a note. It is the *ghost* of one. A guitar strikes a single chord and a fraction of a heartbeat later the sound comes back, slightly darker, slightly softer, a phantom standing just behind the player's shoulder. In a Memphis storefront studio in the summer of 1954, that ghost arrived by way of two tape machines wired together, and it turned an ordinary acoustic strum into something that seemed to bounce off the walls of a much larger, more dangerous room. The room did not exist. The echo invented it. That trick — capturing a sound, holding it for a measured instant, and handing it back — is the oldest piece of true signal processing in the electric guitarist's arsenal, older than fuzz, older than the wah, nearly as old as the electric guitar itself. And of all the things we do to a guitar signal, delay may be the one that most directly conjures *space*: the suggestion that the music is happening somewhere with size, depth, and air.

This chapter follows the repeat from the spinning reels of tape echo through the warm dark fade of bucket-brigade analog and into the glassy precision of the first digital units. Along the way it is worth holding one idea in your head, because it unlocks everything else: a delay is not a sound so much as a *rhythm*. The instant you choose how long to wait before the echo returns, you have made a musical decision — about feel, about groove, about whether the guitar slaps you in the chest or floats off into the rafters.

## The Spinning Reel: Tape Echo and Its Mojo

Before there were pedals there were tape machines, and the principle could not be simpler. Record a signal onto a moving loop of magnetic tape with one head, then read it back a moment later with a second head positioned a little farther along the tape's path. The gap between writing and reading — the physical distance between the record head and the playback head, divided by the speed the tape is travelling — *is* the delay time. Speed the tape up and the heads sit closer in time, so the echo tightens. Slow it down and the repeat stretches lazily behind the note. Feed some of that played-back signal back into the record head and it re-records, repeats again, and again, each pass a little quieter and a little duller until it dissolves. That feedback loop is the heart of every echo box ever built.

The machine that defined the sound for guitarists was the **Echoplex**, introduced by Market Electronics and sold under the Maestro name beginning in the early 1960s. Its genius was a moving record head on a sliding carriage: drag a lever and you physically changed the head spacing, sweeping the delay time from a tight slap to a long trailing wash without stopping the tape. By the time the solid-state **Echoplex EP-3** arrived around 1970, the unit had become a fixture on professional stages and in countless studios. And here the story takes on a wrinkle of genuine gear lore that happens, this time, to be true. The EP-3's input ran through a simple solid-state preamp stage, and that stage had a sound — a subtle treble lift and a thickening of the midrange that players noticed even with the echo switched off entirely. Guitarists from Eddie Van Halen to Jimmy Page are commonly cited as running an EP-3 in the chain partly as an always-on preamp, a tone-sweetener masquerading as an echo unit. That "EP-3 preamp mojo" is real enough that boutique builders now sell standalone pedals that clone just the preamp stage, no echo attached. It is one of the few pieces of tone mythology that survives contact with an oscilloscope.

Tape echo's character comes from its imperfections. Tape cannot store every frequency equally; the highs roll off a little more with each repeat, so the echoes grow progressively darker, a quality engineers call the *high-frequency loss* of successive generations. The tape itself never moves at a perfectly constant speed — tiny variations in the motor and the mechanical drag produce **wow and flutter**, a gentle wavering of pitch that smears each repeat just slightly out of tune with the original. Far from a flaw, this is the warmth people chase. The repeats sound *alive*, breathing, never quite mechanical.

The other monument of tape echo is the **Roland RE-201 Space Echo**, launched in 1974. Rather than a single sliding head, the RE-201 used a loop of tape running past three fixed playback heads, selectable in combination by a rotary knob, plus a built-in spring reverb. Choosing different head combinations gave you not just longer or shorter echoes but *patterns* of echoes — multiple rhythmic taps layered together. Crank its "Intensity" control (Roland's word for feedback) past a certain point and the repeats stop decaying and start *building*, each one louder than the last until the whole machine erupts into runaway howling oscillation. That **self-oscillation** — a delay feeding itself until it screams — became an instrument in its own right, a sound you can ride like a theremin by nudging the rate knob while it wails.

Earlier and stranger than either was the Italian-made **Binson Echorec**, which stored its signal not on tape but on a rotating *magnetic drum* or disc — essentially a steel platter the recording was written onto, read by a small array of playback heads spaced around its circumference. The drum was mechanically robust where tape was fragile, and the multiple heads let you tap out complex multi-repeat rhythms with a clarity tape struggled to match. Pink Floyd's **David Gilmour** built some of the most cavernous guitar landscapes ever recorded around the Echorec, using its drum-driven repeats to turn single notes into slow, pulsing architecture. We will come back to him.

## How a Delay Actually Works

Strip away the technology and every delay does three jobs. It captures the signal. It holds that copy for a chosen length of time — the **delay time**, measured in milliseconds. And it plays the copy back, usually mixed underneath the dry original, while optionally feeding a portion of the output back into the input to create additional, decaying repeats. Three controls govern the result, and they appear in some form on nearly every delay ever made.

*Delay time* sets how long you wait. *Feedback* (sometimes labeled repeats, regeneration, or intensity) sets how many echoes you get: at zero you hear a single repeat, and as you turn it up the repeats multiply, each quieter than the last, until at the extreme the loop sustains itself indefinitely and oscillates. *Mix* (or level, or blend) sets how loud the echoes sit relative to your dry signal — a whisper behind the note, an equal partner, or a wash that swallows the original whole.

What separates the technologies is *how* they hold that copy and what they do to it while they hold it. Tape, as we saw, stores it physically on magnetic medium and darkens it with each pass. The next great idea stored it electronically. The **bucket-brigade device**, or BBD, is a chip containing a long chain of tiny capacitors. The audio signal is passed from one capacitor to the next, step by step, in time with a clock — like a fire brigade passing buckets of water hand to hand down a line. The more buckets in the chain and the slower the clock ticks, the longer it takes a sample to reach the end, and that travel time is your delay. Crucially, the signal stays *analog* the whole way; it is never converted into numbers. Each hand-off loses a little fidelity, so analog delays sound warm and dark, the repeats softening into a pillowy blur. And because BBD chips held a limited number of buckets, analog delays were typically short — a few hundred milliseconds at most before the sound degraded into murk.

The classic analog pedals are beloved precisely for that murk. The **Boss DM-2**, released in 1981, delivers up to roughly 300 milliseconds of delay with repeats that decay into a soft, rounded darkness, sitting politely behind the dry note rather than competing with it. The **Electro-Harmonix Deluxe Memory Man**, with its longer delay range and built-in modulation that adds a seasick chorus-like waver to the repeats, became the secret weapon behind some of the most famous guitar textures of the late 1970s and beyond. Analog repeats *recede*. They get out of the way. That dark decay is forgiving in a way the next technology, at first, was not.

Digital delay arrived in earnest in the early 1980s and worked on an entirely different principle. The incoming analog signal is sampled — measured thousands of times a second and converted into a stream of binary numbers — stored in memory chips, then converted back to analog on the way out. Because numbers do not degrade, the repeats came back *crisp*, bright, and near-identical to the original, with delay times stretching to seconds rather than milliseconds. Units like the Boss DD-2 (1983) and rack processors from companies like Lexicon and TC Electronic offered clean, long, pristine echoes that tape and BBD simply could not. To some ears the early digital repeats were *too* clean — clinical, even cold, missing the breathing imperfection that made tape feel human. To others, that pristine clarity was the whole point: a repeat that sat in perfect rhythmic lockstep, bright enough to ring out distinctly through a dense mix. Modern digital units now happily *emulate* tape's wow and flutter and BBD's dark decay, so a player today can have any of these flavors in one box. But the underlying lesson holds: tape darkens and wavers, analog darkens and softens, early digital clarifies and extends.

## Delay Time as Rhythm: The Math That Makes It Musical

Here is the idea that turns a delay from a special effect into a compositional tool. Because the echo returns after a fixed number of milliseconds, and because music moves in beats, the relationship between your delay time and the song's tempo determines whether the echo *grooves* or *fights*. Get the math right and the repeats lock into the pulse like a second guitarist. Get it wrong and they wash into a muddy blur that drags against the band.

Start with the single most useful number in all of delay. To find the length of one quarter note in milliseconds, divide 60,000 by the tempo in beats per minute:

**60000 / BPM = milliseconds per quarter note**

The logic is plain once you see it. There are 60,000 milliseconds in a minute, and at, say, 120 BPM there are 120 beats in that minute, so each beat — each quarter note — lasts 60000 / 120 = 500 milliseconds. Set your delay to 500 ms at 120 BPM and every echo lands squarely on the next beat. Halve it to 250 ms and the repeats fall on the eighth notes. This is *quarter-note* and *eighth-note* delay, the rhythmic backbone of countless arrangements.

But the most addictive rhythmic delay setting of all is the **dotted eighth**. In music notation a dot after a note adds half its value again, so a dotted eighth note equals an eighth plus a sixteenth — three sixteenths in total, or three-quarters the length of a quarter note. The formula follows directly:

**dotted-eighth delay = (60000 / BPM) x 0.75**

At 120 BPM that is 500 x 0.75 = 375 milliseconds. The magic of the dotted eighth is what happens when you play steady eighth notes against a dotted-eighth echo: the repeats fall *between* your picked notes, in the gaps, weaving a galloping sixteenth-note tapestry out of a part you are playing far more slowly. The guitar and its own shadow interlock into a pattern neither could produce alone. This is the engine behind the chiming, cascading arpeggios that define a whole school of atmospheric rock guitar, and we will hear it shortly. For *slapback* — the short, percussive single echo of rockabilly — you ignore the tempo math entirely and work by feel, setting the delay short, roughly 80 to 150 milliseconds, with the feedback turned all the way down so you get exactly one tight repeat snapping right behind the note.

## The Tone of a Repeat

Listen closely to a great tape slapback and what you hear is a doubling that thickens without smearing. At around 100 milliseconds the repeat is too fast to register as a separate event yet too slow to phase against the original — it sits in that perceptual seam where the ear reads it as one fatter, more urgent note with a hard percussive edge on its tail. The slight high-frequency rolloff of the tape keeps that edge from getting brittle; the repeat is duller than the dry note, so it reinforces the attack without adding harshness. Roll the delay shorter still and you approach the territory where the copy starts to comb-filter against the original, hollowing out frequencies and producing a metallic, flange-like coloration. Slapback lives just on the safe side of that line.

A long, multi-repeat tape or drum echo paints an entirely different picture. Here the repeats are slow enough to be heard as distinct events, and as each one darkens and detunes a fraction from the wow and flutter, they pile into a soft cumulative haze — a low-midrange cloud that hangs in the 200 to 800 Hz region, behind and beneath the dry signal, suggesting a great stone room without the boxy honk of an actual reverb. Push the feedback toward self-oscillation and that haze blooms into a sustained drone you can pitch-bend by riding the delay-time control, the repeats smearing into one continuous tone. Analog BBD delay sits between these worlds: darker and rounder than tape, with repeats that fall away quickly into a warm pillow, never bright enough to clutter the top end, ideal for thickening a rhythm part or adding depth to a lead without anyone in the audience consciously hearing "an echo." Crisp digital, by contrast, returns every repeat with its treble intact, each echo a bright, distinct ring — glorious for rhythmic dotted-eighth work where you *want* to hear every tap articulate cleanly, less forgiving when you simply want atmosphere, because nothing gets out of the way.

## Case Studies in the Craft of the Echo

### Scotty Moore, Elvis Presley, and the Birth of Slapback

The sound that launched rock and roll guitar was, in large part, the sound of tape echo. At Sun Studio in Memphis, producer Sam Phillips ran his recordings through a tape delay setup — two Ampex machines feeding one into the other — to produce a tight, exciting slapback he splashed across vocals and guitars alike. On the 1954 sides that introduced Elvis Presley to the world, **Scotty Moore**'s guitar work on tracks like "That's All Right" and "Mystery Train" rides that slap: a hollowbody guitar, clean and bright, every note shadowed by a single percussive repeat a fraction behind it, giving the part a nervous forward momentum that no dry signal could match. Moore later made the Echoplex part of his own rig, but the foundational sound was Phillips's studio slap. The delay is short — in the slapback range, a single repeat with no feedback tail — and its effect is rhythmic and propulsive rather than spacious. It does not create a room; it creates *urgency*. That tight doubling became the defining guitar texture of rockabilly and a permanent fixture in the country and roots-rock vocabulary.

### Brian Setzer and the Slapback Revival

Three decades later, **Brian Setzer** of the Stray Cats picked up the same torch and made slapback his signature, swinging it into the 1980s and beyond with ferocious energy. Setzer's rig centered on a **Gretsch** hollowbody — famously a 1959 6120 — typically into a Fender Bassman-style amp, with tape echo (and later faithful digital emulations of it) supplying the slap. On the 1981 Stray Cats material and across his big-band records of the 1990s, the delay sits in the classic rockabilly window, short enough to read as a single thickening repeat, fast enough to drive the rhythm. What Setzer adds to Moore's template is aggression and precision: hard hybrid picking, snapping the strings against the frets, every staccato note kicking out a crisp shadow. Below is an original slapback figure in his idiom — a bright, swung shuffle over an open-position chord shape, the kind of thing that wants a hollowbody, clean amp headroom, and a short single repeat.

*Feel:* swung sixteenths, brisk shuffle, ~150 BPM. Delay ~120 ms, feedback at zero (one repeat), mix moderate.

```
e|------------------------------------------------|
B|------------------------------------------------|
G|------0--------0------0h2p0-----------0---0-----|
D|----2-------2------------------2---2-------2----|
A|-3-------3-------3----------3-------------------|
E|------------------------------------------------|
```

*Slapback in action:* keep it clean and bright, pick close to the bridge, and let the single short repeat double each note into a percussive snap — the echo should sound like a tight handclap a hair behind the string.

### David Gilmour and the Architecture of Long Delay

If Scotty Moore used echo to push, **David Gilmour** used it to *expand*. Across Pink Floyd's catalog — and nowhere more famously than the solos on tracks like "Time," "Dogs," and the live "Comfortably Numb" — Gilmour deployed long, rhythmically tuned delays to make a single guitar fill a vast acoustic space. In the early years he leaned heavily on the **Binson Echorec**, whose drum-and-multiple-head design let him stack repeats into pulsing patterns, the foundation of the hypnotic intro textures on pieces like "One of These Days," where a single bass-and-guitar figure is multiplied by the Echorec into a churning, mechanical groove. As his rig grew, Gilmour layered multiple delay units at once and was an early adopter of tempo-locked rhythmic delay — famously using a repeat tuned to the dotted eighth so that his held, vocal-like bends would echo back in the gaps and reinforce the song's pulse. His feedback settings are typically moderate, several audible repeats rather than a runaway oscillation, the echoes darkening as they fade so the original note always sings out clearly on top.

There is real music theory underneath Gilmour's spaciousness. His lead vocabulary leans on the **minor pentatonic** scale — the five-note pattern (root, flat third, fourth, fifth, flat seventh) that is the bedrock of blues and rock soloing — but he constantly resolves his long, bending phrases onto **chord tones**, the specific notes (root, third, fifth) of whatever chord the band is sitting on underneath him. That is why his slow, echoing bends sound so *settled* and inevitable rather than merely bluesy: he bends up to a target note that is consonant with the harmony and lets the delay carry it, so the repeat sustains a note that already belongs. The echo does not just add space; it *holds the resolution* in the air. The following original phrase shows the idea — a slow bend up to a chord tone, allowed to ring, with a long delay multiplying it into a fading column of sound.

*Feel:* slow, spacious, ~63 BPM (think a stately rock ballad). Delay ~475 ms (quarter note at this tempo), feedback for 3–4 repeats, mix high.

```
e|----------------------------------------------------|
B|--15b17~~~~~-----------15------13-------------------|
G|-----------------14b16-------16b14-----14~~~~~------|
D|----------------------------------------------------|
A|----------------------------------------------------|
E|----------------------------------------------------|
```

*Long delay as architecture:* play sparsely and let silence do the work — each bent target note (here landing on chord tones) blooms, repeats, and decays into the next phrase, so one guitar implies a cathedral. A touch of modulation on the repeats deepens the sense of space.

### The Edge and the Dotted-Eighth Cascade

No discussion of rhythmic delay can omit **The Edge** of U2, who built an entire guitar identity on the dotted-eighth repeat and whom a later chapter explores in full detail. The essential principle is the one we worked out above: by playing a sparse pattern of clean, chiming notes and setting a delay to three-quarters of a quarter note, locked to the song's tempo, the echoes fall precisely into the spaces between the played notes. On the 1984 track "Pride (In the Name of Love)" and across the *War* and *The Unforgettable Fire* era, this produces the illusion of a guitarist playing a rapid, intricate sixteenth-note part while in fact striking far fewer notes — the machine fills in the rest, and the player's right hand stays relaxed and rhythmic. It is the cleanest demonstration in all of rock that delay is rhythm. The Edge typically favored bright, articulate repeats so each tap rings distinctly, often two delays at once for additional rhythmic complexity, with the dry guitar kept clean and compressed so every note has a uniform, bell-like attack for the echo to copy.

The trick only works if the played notes and the echoes interlock cleanly, which means understanding exactly where the repeats land. Picture a single bar of four beats divided into sixteen sixteenth-note slots. You pluck a note on slot 1. A dotted-eighth delay (three sixteenths long) returns it on slot 4. If you pluck again on slot 7, its echo lands on slot 10, and so on. The played notes (P) and their echoes (e) tile the bar like this:

```
slot:   1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
play:   P  .  .  e  .  .  P  .  .  e  .  .  P  .  .  e
```

Here is an original pattern built on that grid — a clean arpeggiated figure where what you *play* is simple but what you *hear* is a dense, rolling cascade.

*Feel:* bright and driving, ~120 BPM. Dotted-eighth delay = 375 ms; feedback moderate (the repeats should be clearly audible but fading); mix near equal with the dry signal.

```
e|--0-----------0-----------0-----------|
B|-------0-----------0-----------0------|
G|----------1-----------1-----------1---|
D|--------------------------------------|
A|--------------------------------------|
E|--------------------------------------|
```

*The dotted-eighth cascade:* play these three notes cleanly and evenly, let them ring (do not mute), and the delay drops a repeat into every gap, so a slow arpeggio blossoms into a fast, shimmering wash. Dial the delay time to exactly three-quarters of one beat at your tempo, or the echoes will smear instead of interlocking. Keep the amp clean and add a little compression so every note feeds the delay at the same level.

## A Closing Word on Space

What unites the spinning tape, the rotating drum, the brigade of buckets, and the stream of digital samples is that each one lets a guitarist play *with the past* — to set a note loose and have it answer itself, to converse with a sound that is already gone. Used short and dry, it is rhythm and muscle, the slap that drives a rockabilly shuffle. Used long and lush, it is architecture, the air that turns a single sustained bend into a room you could walk through. The technology shapes the color — darker and wavering from tape, rounder and softer from analog, brighter and cleaner from digital — but the musical decision is always the same one, the one you make the instant you choose how long to wait: how far behind you do you want your own shadow to stand?

> **Listen For**
> - **Elvis Presley / Scotty Moore, "Mystery Train" and "That's All Right" (1954-55):** the tight, single-repeat tape slapback off Sam Phillips's machines — hear how the short echo doubles each guitar note into a percussive snap and drives the rhythm forward without ever sounding spacious.
> - **Stray Cats, "Stray Cat Strut" and "Rock This Town" (1981):** Brian Setzer's hollowbody slapback — focus on the snap a hair behind each staccato note and how the clean, bright tone keeps the repeat crisp rather than muddy.
> - **Pink Floyd, "One of These Days" (1971):** the Binson Echorec turning a single repeated figure into a churning, multi-tap mechanical groove — listen to the rhythmic pattern the multiple heads stack up.
> - **Pink Floyd, "Time" solo, *The Dark Side of the Moon* (1973):** David Gilmour's long, rhythmically tuned delay — notice how each bent note lands on a chord tone and the echoes hold that resolution in the air as the phrase fades.
> - **U2, "Pride (In the Name of Love)" (1984):** the dotted-eighth cascade — try to separate the notes The Edge actually picks from the echoes the delay fills in between them; the dense sixteenth-note shimmer is mostly the machine.
