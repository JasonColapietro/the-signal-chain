# Chapter 19 - The Uni-Vibe: Rotary Dreams

Listen to the opening seconds of "Machine Gun" from the *Band of Gypsys* record, taped on the first night of 1970 at the Fillmore East, and before Jimi Hendrix plays a single note in anger you can already hear the room breathing. The guitar isn't doing anything dramatic yet -- a held chord, a couple of probing notes -- but the sound itself is alive, swelling and receding, the high frequencies drifting in and out of focus like heat shimmering off summer asphalt. It is not tremolo, which would simply turn the volume up and down. It is not a wah, which sweeps a single resonant peak. It is something stranger and wetter, a seasick, throbbing motion that makes the whole tone seem to rotate in space. That motion is the sound of a small, heavy, oddly built box from Japan called the Uni-Vibe, and it was supposed to sound like something else entirely.

## A Failed Imitation

The story begins with envy. By the mid-1960s every organ player worth hearing was running a **Hammond organ** through a **Leslie rotary speaker cabinet**, a wonderful and absurd piece of furniture in which an actual horn and an actual rotating drum-baffle spun around inside the cabinet, hurling the sound physically through the air. As the speakers rotated, they threw the sound at the listener and then away again, and the laws of physics did the rest: a Doppler pitch-shift as the source moved toward and away from you, an amplitude swell as it faced you and turned aside, and a thicket of phase cancellations as the direct and reflected waves collided in the room. The result was that lush, three-dimensional, swirling shimmer you hear under every great soul ballad and psychedelic organ break. Guitarists wanted it desperately, but a Leslie was the size of a refrigerator, weighed as much as one, and was a nightmare to mic and move.

So the race was on to fake it in a box. In Japan, the **Honey** company -- soon to be reorganized into the firm best remembered as **Shin-ei** -- set an engineer named **Fumio Mieda** to the task. Mieda was the same restless designer behind a clutch of early Japanese effects, and his brief was simple in theory: build a small electronic device that reproduced the rotary swirl of a Leslie. The result, sold around 1968, was the **Uni-Vibe**, distributed in the United States under the **Univox** badge (the importer Unicord) and elsewhere variously as the Shin-ei or Jax. The earliest units came as a two-piece set: a chrome-faced main box and a separate rocker **expression pedal** that controlled the speed of the effect, so the player could ride the swirl from a slow drift to a frantic flutter with the foot, exactly as an organist could switch a Leslie between its slow "chorale" and fast "tremolo" speeds.

Here is the beautiful accident at the center of this chapter: it did not sound like a Leslie. Not really. A Leslie's defining trick is genuine Doppler pitch modulation -- the note actually goes sharp and flat as the speaker spins -- and the Uni-Vibe's circuit produced comparatively little of that. What it produced instead was a deep, watery, asymmetrical *phase* sweep with a pronounced throb, narrower and more hypnotic than a Leslie and, to many ears, far more interesting on a guitar. The imitation failed upward. It became its own thing, a sound no rotating speaker had ever quite made, and within two years it would be bolted to the front of the most famous guitar rigs on earth.

## How It Works: Photocells in the Dark

Open a vintage Uni-Vibe and the heart of it looks almost comically simple, even crude, which is part of why people fell in love with it and part of why it is so hard to copy. Inside sits a tiny incandescent **lamp**, and clustered around that lamp, staring at it, are four light-dependent resistors -- **photocells**, also called LDRs. A low-frequency oscillator, the **LFO**, makes the lamp pulse: brighter, dimmer, brighter, dimmer, at whatever rate the speed control dictates. As the lamp's glow rises and falls, the resistance of each photocell rises and falls with it, and those changing resistances are wired into four **all-pass filter** stages -- phase-shift stages -- in the audio path.

That phrase "all-pass filter" is worth unpacking, because it is the whole secret. An all-pass filter does something sneaky: it lets every frequency through at full volume -- it does not cut treble or bass -- but it *delays* each frequency by a different amount, shifting its phase. When you take that phase-shifted copy and mix it back against the original dry signal, the frequencies that come out exactly upside-down (180 degrees out of phase) cancel, carving deep notches in the spectrum. Sweep those notches up and down the frequency range and you have a **phaser**. So the Uni-Vibe is, in its bones, a four-stage phaser -- one of the very first ever built for guitar.

But two details make it sing rather than merely sweep. First, the four photocells do not respond in lockstep. Real photocells of that era were inconsistent parts with their own slightly different "lag" -- the small delay between the light changing and the resistance catching up. Mieda's circuit also fed the filter stages at deliberately staggered, unequal frequency points rather than spacing them evenly the way a textbook phaser does. The upshot is a *staggered, asymmetrical* sweep: the notches don't march in a tidy parade, they lurch and pulse, the motion lopsided and organic, leaning harder one way than the other. That asymmetry is the throb, the seasick lilt, the thing your ear reads as "alive." Second, the lamp itself smooths the motion. An incandescent filament cannot turn on and off instantly; it glows and fades with a gentle, rounded curve. So the modulation is never a hard mechanical chop but a soft, tidal swell -- closer to breathing than to clockwork.

A switch on the unit selects **Chorus** or **Vibrato** mode, though neither word means quite what a modern pedal buyer expects. In **Chorus** mode the phase-shifted signal is blended with the dry signal -- that mix is where the cancellation notches form, and it is the famous swirling Uni-Vibe sound, the one on all the records. In **Vibrato** mode the dry signal is removed entirely and you hear only the wet, modulated path; with no dry reference to cancel against, the result is a genuine warbling pitch-and-phase wobble, more pronounced and disorienting, less commonly used. The Speed control (and the expression pedal that overrides it) sets the LFO rate; an Intensity or Volume control sets how deep and how loud the effect sits. There is no separate "width" or "depth" knob carving the sweep -- the depth is baked into the circuit, which is exactly why every real one sounds so consistent and so good.

## Phase Modulation Versus True Chorus

It is worth pausing on a distinction that confuses even experienced players, because the Uni-Vibe sits right on the fault line between two whole families of effect. **Phase modulation**, what the Uni-Vibe does, works by mixing a signal against a *phase-shifted copy of itself* and sweeping the cancellation notches. No time delay in the modern sense is involved; the "movement" is the notches sliding through the harmonic content of your note. The frequencies that get notched out are mathematically related to the spacing of the filter stages, so a phaser tends to interact with the **harmonic series** of whatever you play -- the natural ladder of overtones (the octave, the fifth above that, the next octave, the major third, and on up) that rings above any fundamental pitch. When a notch sweeps through your second or third harmonic, you hear that overtone duck and swell, which is why sustained, harmonically rich notes seem to come alive under a vibe in a way that staccato playing does not.

**True chorus**, by contrast -- the sound of an early-1980s analog chorus pedal -- uses a short **time delay** (a few milliseconds) whose length is wobbled by an LFO. Wobbling the delay time stretches and compresses the waveform, which produces real **pitch modulation** (small, continuous sharp-and-flat detuning), and mixing that detuned, delayed copy against the dry signal gives the impression of two instruments playing not quite in unison. That detuning is precisely the thing a spinning Leslie does and the thing the Uni-Vibe largely *doesn't*. So the irony compounds: the box built to imitate a Leslie achieves its magic through phase cancellation, while the effect we now call "chorus" -- which actually does reproduce the Leslie's Doppler detuning -- came along years later. The Uni-Vibe's "Chorus" switch is a historical misnomer that stuck. What your ear loves about it is not detuning at all but the staggered, throbbing sweep of those four lopsided notches.

The other expressive variable is rate, and it matters more than almost anything. A **slow LFO** -- the sweep taking several seconds to complete a full cycle -- gives that oceanic, barely-there drift, the sound of a chord very slowly turning over in the light. It rewards patience and sustain. A **fast LFO** pushes toward a nervous, propeller-like flutter, almost a tremolo at the top end, tense and agitated. Because the original came with a foot pedal for speed, the instrument is really a *performance* of motion: you can sit on a held chord and slowly open the speed up, letting the swirl accelerate as the emotion rises, then pull it back. Hendrix understood this immediately. The pedal was not a set-and-forget effect; it was a third hand.

## The Tone, Described

Plug a **Stratocaster** into a vintage Uni-Vibe in Chorus mode, set the speed slow, and the first thing you notice is that nothing is harsh. The notches live mostly in the midrange and lower treble -- call it the region from roughly 800 Hz up past 2 kHz -- so as they sweep they take the bite off the upper mids and then give it back, over and over, a soft hand passing across the face of the tone. On a clean single-coil neck pickup the effect is liquid and underwater, glassy highs pooling and draining. Push the same signal through an overdriven amp and the character transforms: distortion adds a dense forest of harmonics for the notches to chew on, so the swirl becomes thicker, more turbulent, almost vocal, with a hollow "wow" in the middle of every sustained note as a notch passes through. There is a faint, grainy texture to a real vibe, too, a slightly lo-fi, compressed quality from those simple photocells and the modest circuit around them, and that grain is part of the charm -- it sounds like an old film looks, warm and slightly worn.

What the vibe loves above all is held information. A single bent note, allowed to ring, becomes a small drama as the sweep crawls across its overtones. A fat barre chord turns into a slowly rotating cathedral window of sound. Staccato funk chops, by contrast, give the effect almost nothing to work with -- the notes are gone before a notch can travel anywhere -- which is why the vibe is the patron saint of the slow blues, the spacey ballad, and the long psychedelic plateau, and why it rarely shows up on a fast, percussive part. To dial it in, you start slow and shallow, find the speed where the throb matches the breath of the song, and then you stop touching the knobs and start playing long.

## Case Study: Hendrix and the Star-Spangled Sky

Jimi Hendrix is the reason the Uni-Vibe is a legend rather than a footnote. By 1969 he was running one in front of his **Marshall** stacks alongside his **Fuzz Face** and **wah**, and the combination defined the back end of his short career. The most quoted example is "Machine Gun," whether the *Band of Gypsys* version or the Woodstock readings: the Uni-Vibe in Chorus mode at a slow-to-medium speed, smearing his sustained, feeding-back lines into something that genuinely evokes the disorientation and dread the song is about, the swirl turning every held note into a wail that will not sit still. Hendrix worked the speed pedal as a dynamic device, letting the rate breathe with the intensity of his improvisation.

Listen, too, underneath the famous Woodstock "Star-Spangled Banner." Amid the dive-bombs and the napalm shrieks of feedback there is a watery, rotating quality to many of the held tones that is pure vibe, the effect lending an eerie, heat-haze instability to a melody everyone in America could hum. The lore around Hendrix's exact settings is thick and largely unverifiable -- he was famously indifferent to documenting knob positions, and his rigs changed constantly -- so treat any precise "Jimi used X" claim with healthy skepticism. What is not in doubt is the role: the Uni-Vibe was his color for hugeness and unease, the sound he reached for when a note needed to feel like it was happening to you rather than merely at you.

Here is an original phrase in the spirit of that approach -- a slow, sustained bend that gives the sweep room to move. Set the vibe to Chorus, speed slow, into a thick, sustaining overdrive.

```
Slow blues feel, roughly 60 BPM -- let everything ring
e|----------------------------------------------------|
B|----------------------(8)~~~~~~~~~~~~~~~~~~~~~~~~~~~|
G|--7b9-----7b9r7-------5----7~~~~~~~~~~~~~~~~~~~~~~~~|
D|----------------------------------------------------|
A|----------------------------------------------------|
E|----------------------------------------------------|
```
*Example 19.1 -- a sustained G-string bend held under a slow Chorus-mode vibe.*

Bend the G string up a whole step (7 to the pitch of 9) and just hold it; the Uni-Vibe's notches crawl across the bent note's overtones so the pitch seems to shimmer and rotate even while your finger is still. The slower you take it, the more the swirl tells the story.

## Case Study: Robin Trower and the Bridge of Sighs

If Hendrix made the Uni-Vibe famous, **Robin Trower** made it architectural. On his 1974 album *Bridge of Sighs*, and above all the title track, the vibe is not an ornament but the foundation of the entire sound. Trower, a Stratocaster player steeped in Hendrix's vocabulary, built "Bridge of Sighs" on a slow, doom-laden riff drenched in a Uni-Vibe set to a luxuriantly slow speed, so the whole track seems suspended underwater, every chord and bend rotating with glacial, hypnotic patience. Pair that with a thick, fuzzy overdrive and a cavernous reverb and you get one of the most atmospheric guitar tones ever committed to tape -- heavy and weightless at once.

What Trower understood, and what the recording teaches, is that the vibe rewards *space*. He plays slowly. He lets notes hang. He leaves gaps so the swirl has room to do its work, and he keeps the speed slow enough that you feel the throb as a pulse rather than a flutter. His exact rig has been discussed for decades and the broad strokes are well established -- Strat, vintage Uni-Vibe, Marshall amplification, fuzz -- while the precise settings, as ever, are best described as commonly cited rather than documented.

This second example is a chordal bed in that vein: simple triads and a sustained voicing, left to ring so the sweep can rotate the whole harmony at once. Note the **add9** chord, a major chord with the ninth (the second scale degree, an octave up) added on top, which adds a glassy, unresolved shimmer that the vibe loves because it gives the notches an extra overtone to play with.

```
Very slow, roughly 56 BPM -- let chords ring full
e|--0-----------0-----------0-------------------------|
B|--3-----------1-----------0-------------------------|
G|--0-----------0-----------4-------------------------|
D|--2-----------2-----------2-------------------------|
A|--3-----------0-----------2-------------------------|
E|--------------------------0-------------------------|
```
*Example 19.2 -- Cadd9 / Am(add9) / E-ish color, each shape struck once and left to bloom.*

Strike each shape once and let it bloom; with the Uni-Vibe in Chorus at a slow speed, the held chord slowly turns in the light, the added ninth shimmering as a notch sweeps across it. Keep your pick hand still and let the box move the sound.

## Case Study: Gilmour and the Breathing Floyd

**David Gilmour** carried the Uni-Vibe into a third aesthetic entirely: not the blues-rock fury of Hendrix or the doom of Trower, but the wide, clean, spacious ache of **Pink Floyd**. On *The Dark Side of the Moon*, the gently rocking guitar figure of "Breathe (In the Air)" floats on a slow modulation widely associated with a Uni-Vibe-type effect, the clean, lap-steel-inflected tone swelling and receding with a slowness that perfectly matches the song's title and its meditation on the passing of a life. (Gilmour's modulation choices across his career are debated by gearheads -- he has used various rotary, vibe, and chorus units, and which specific box appears on which track is not always settled, so the honest statement is that "Breathe" lives in unmistakably Uni-Vibe territory even where the exact unit is contested.)

The lesson of Gilmour's use is that the vibe is not only a dirty effect. On a clean, compressed signal with plenty of reverb, a slow vibe becomes a kind of weather -- atmosphere rather than incident. It widens a simple part and makes stillness feel like motion. Where Trower used it to make heaviness hover, Gilmour used it to make calm shimmer.

Floyd's harmony here leans on **modal** color. "Breathe" rocks gently between an E minor and an A major sonority, and that pairing -- a minor i chord moving to a *major* IV -- is the signature of the **Dorian mode**, the minor scale with a raised sixth degree. (A mode is simply a scale built by starting on a different note of a parent scale; Dorian is the second mode, brighter than the natural minor because of that raised sixth, which is exactly the note that turns the IV chord major.) That raised sixth gives the song its bittersweet, hovering quality, neither fully dark nor fully resolved -- a perfect harmonic match for the suspended, rotating motion of the vibe.

Here is a Hendrix-style rhythm figure to close the examples -- the kind of soulful chordal comping where the vibe sweeps through ringing extensions. It uses the famous **7#9** voicing, the "Hendrix chord," a dominant seventh with a sharpened ninth on top; the clash between its major third and that raised-ninth (which sounds like a minor third an octave up) is the gritty, bluesy crunch under so much of Jimi's rhythm work.

```
Slow funk-soul feel, roughly 72 BPM -- lay back behind the beat
e|----------------------------------------------------|
B|--6--6----------8---8-------------------------------|
G|--7--7----------9---9-------------------------------|
D|--6--6----------7---7-------------------------------|
A|--7--7----------x---x-------------------------------|
E|--0--0----------------------------------------------|
```
*Example 19.3 -- the E7#9 "Hendrix chord," then the upper grip sliding up two frets for color.*

Catch the E7#9 with a light, percussive stroke, let it ring just long enough for the Uni-Vibe to begin its sweep, then move the upper grip up two frets and back; the slow swirl turns a stock rhythm figure into something that breathes. Dig in lightly -- the vibe and the amp's natural compression do the rest.

## What Endured

The original Uni-Vibe was discontinued in the early 1970s, and for years it was the stuff of dusty rumor, hoarded by collectors who knew that nothing else sounded quite like it. The reasons were exactly the things that made it special and the things that made it hard to reproduce: those inconsistent photocells, the staggered filter stages, the gentle lag of an incandescent bulb glowing in the dark. Cheaper imitations used simpler LFO chips and even, symmetrical phasing, and they always sounded too tidy -- a phaser pretending to be a vibe. The good modern recreations are the ones that went back and honored the lopsided original: a real lamp, real photocells, staggered stages, the asymmetry preserved.

What the Uni-Vibe proved, and what makes it belong at the heart of any history of effects, is that the most beloved sounds are often beautiful failures. Mieda set out to bottle a refrigerator-sized spinning speaker and instead built something the spinning speaker could never do -- a throbbing, watery, four-cornered swirl that turned held notes into living things. It failed to be a Leslie and succeeded at being itself, and three of the greatest guitarists of the era heard that immediately and built whole songs on top of it. Rotary dreams, dreamed wrong, and all the better for it.

> **Listen For**
> - **Jimi Hendrix, "Machine Gun"** (*Band of Gypsys*, 1970): the Uni-Vibe in Chorus mode swelling under every sustained, feeding-back line -- listen to how the held notes refuse to sit still, the swirl turning them into wails. Compare the Woodstock "Star-Spangled Banner" (*Woodstock* recordings) for the same watery instability under the melody.
> - **Robin Trower, "Bridge of Sighs"** (*Bridge of Sighs*, 1974): the deepest, slowest vibe on record -- focus on how the spaces between the notes let the swirl rotate the whole tone, and how slowly the throb pulses.
> - **Pink Floyd, "Breathe (In the Air)"** (*The Dark Side of the Moon*, 1973): clean, spacious, slow modulation in unmistakable Uni-Vibe territory -- hear how the gentle sweep makes a calm, near-static part feel like it is breathing, and notice the minor-to-major-IV Dorian color underneath.
> - **A/B test for your ear:** put on any of these, then a true analog *chorus* track from the early 1980s. The chorus detunes (you hear two slightly out-of-tune guitars); the vibe sweeps notches (you hear one guitar rotating in space). Once you can tell them apart, you understand the whole chapter.
