#!/usr/bin/env python3
"""Write FUALL Draw.io breakdown notes into column 8 of the Foundations CSV."""

import csv

INPUT = '/Users/jt/Top/Projects/FU/FUALL/drafts/csv/Foundations - Foundations.csv'
OUTPUT = '/Users/jt/Top/Projects/FU/FUALL/drafts/csv/Foundations - Foundations.csv'

TARGET_COL = 8  # First empty column

# Notes keyed by row number (1-indexed, row 1 = header)
HEADER_LABEL = "FUALL Draw.io breakdown"

NOTES = {
    3: """Examples of the pattern — see existing Notes column for the full civilizational cycles list (Ibn Khaldun, Spengler, Toynbee, Turchin, Strauss & Howe, Glubb, Dalio).

Column 4 contains an alternate draft of the telephone metaphor that was developed into Row 4's final version. Column 6 contains the "Athens had it, Renaissance recovered it, Enlightenment built on it" passage — this language was cut from the rework but the cadence is strong; consider recovering for another article.""",

    4: """The telephone metaphor is imperfect in one important way: in the game, mutations are random. In civilizational transmission, mutations can be random (honest misunderstanding), motivated (power-seeking, simplification for convenience), or structural (each generation's shortcuts become the next generation's starting point).

Michael Tomasello, The Cultural Origins of Human Cognition (1999): cumulative culture requires each generation to faithfully transmit AND improve. Failure at either step breaks "the ratchet." This is the formal version of the telephone problem.

"The original phrase is itself imperfect and in need of an update" — this is what makes the problem harder than mere preservation. Pure conservation would be difficult enough. But the phrase also needs to get better. Which means you need people capable of both receiving it accurately AND improving it — which requires the very wisdom the transmission is trying to produce. A bootstrapping problem.""",

    5: """Grand temples and their construction timescales:
- Great Pyramid of Giza (c. 2560 BCE) — ~20 years to build, still standing after 4,500 years
- Parthenon, Athens (447–432 BCE) — 15 years
- Angkor Wat, Cambodia (early 12th century) — ~30 years
- Chartres Cathedral, France (1194–1220) — 26 years
- Notre-Dame de Paris (1163–1345) — 182 years
- Cologne Cathedral (1248–1880) — 632 years
- Sagrada Família, Barcelona (1882–ongoing) — 140+ years and counting
- Borobudur, Java (c. 750–842 CE) — ~75 years

These are investment signals. Civilizations don't spend generations building structures unless they consider the ideas those structures represent to be foundational. The temples themselves are transmission devices — their permanence is the message: "this matters enough to outlast us."

The stories and rituals that accompany them serve the same function. The Eleusinian Mysteries lasted ~2,000 years. The Catholic Mass has been performed continuously for ~1,700 years. Confucian rites persist after 2,500 years. The durability of ritual often exceeds the durability of understanding — which is the problem.""",

    6: """"Symbols defended long after understanding lost" — this is the master pattern:
- Cargo cults: after WWII, Pacific Islanders built imitation airstrips hoping planes would return. Perfect preservation of form, zero access to function. Feynman used this as his metaphor for bad science ("Cargo Cult Science," 1974 Caltech commencement).
- Chesterton's Fence (The Thing, 1929): "Don't ever take a fence down until you know the reason it was put up." The conservative principle. But also: sometimes the reason is genuinely forgotten, and defending the fence becomes the obstacle.
- "Often the very institutions built to preserve understanding become vessels for its corruption" — the Catholic Church preserving Greek texts while suppressing their application. Universities preserving the word "Academy" while gutting its function. Political parties preserving the word "liberal" while practicing illiberalism.

Column 4 contains a draft connecting this directly to Paideia and the Sophists — material that was developed into Rows 7-8 in the final version.""",

    7: """Sophists: Protagoras, Gorgias, Hippias, Prodicus were the major figures. Not uniformly bad — Protagoras's "man is the measure of all things" is a serious philosophical position. But the commercial model selected for persuasion skill over truth-seeking. The corruption wasn't in charging fees per se but in what the fees optimized for.

Socrates's trial: 399 BCE. Charges: impiety (asebeia) and corrupting the youth. Convicted by jury of 501 Athenian citizens. Vote was close — roughly 280 to 221. Refused to flee (see Crito). Drank hemlock. See Plato's Apology, Crito, Phaedo for the trial, the argument against escape, and the death scene respectively.

Akademos/Hekademos: mythological Attic hero. The grove (Akademia) was about a mile northwest of Athens. Plato began teaching there c. 387 BCE. The Academy continued in various forms for nearly 900 years until Justinian I closed it in 529 CE — itself an act of a Christian emperor suppressing pagan philosophy. The referent killed by institutional power.

Hoi eleutheroi (οἱ ἐλεύθεροι): Aristotle, Politics. The "free arts" — skills befitting a free person, as opposed to banausic (mechanical/servile) arts. The distinction was explicitly political: you need these capacities to participate in self-governance. A person without them is free in name only.

"Signaling theory of education" — Bryan Caplan, The Case Against Education (2018): argues that much of modern education's value is signaling (proving you can sit through 4 years of compliance) rather than human capital formation (actually learning useful things). This is the quantitative version of the sophistry critique.

See existing Notes column for structural evidence: journals behind paywalls, Aaron Swartz, tuition inflation, textbook prices, artificial scarcity.

Column 2 (Original) contains an older version that led with Reason rather than the Socrates story — the structural pivot to leading with the historical narrative was a significant improvement.""",

    8: """Werner Jaeger, Paideia: The Ideals of Greek Culture (1933–1945, 3 volumes) — the definitive modern treatment. Argues Paideia was the Greeks' central contribution to civilization, not democracy or philosophy in the narrow sense, but the concept of deliberate human formation.

Latin equivalent: humanitas (Cicero, Aulus Gellius). German: Bildung — cultural self-formation through education and experience. Each carries similar connotations; each has degraded in its own language.

"Credentials without substance" — current stats: average US student debt ~$37,000 (2024). Tuition has risen ~1,200% since 1980, adjusted for inflation. Meanwhile employer surveys consistently show graduates lack critical thinking and communication skills — the very things the liberal arts were supposed to provide.

See existing Notes column for Academy etymology and Paideia/Confucius comparison.

Column 6 contains an extended draft connecting Paideia to Plato's Academy and the liberal arts tradition. Material was incorporated into the final Rework but the longer version has useful detail about Aristotle's specific curriculum.""",

    9: """Linguistic/philosophical background for "terms as vessels":
- Saussure's distinction between signifier (the word) and signified (the concept). The relationship is arbitrary and conventional — which is why it can drift.
- Wittgenstein's language games — meaning is use, and use changes across communities and time.
- Korzybski: "the map is not the territory" (Science and Sanity, 1933). Words are maps of concepts, not the concepts themselves.
- The Sapir-Whorf hypothesis (weak form): language shapes thought. If the terms degrade, the thinking degrades with them.

"Liberal Arts to worthless degree" — the original seven: grammar, logic, rhetoric (trivium) + arithmetic, geometry, music, astronomy (quadrivium). Codified by Martianus Capella (5th century) and Cassiodorus (6th century). These were the prerequisites for all further study — you learned these first because without them you couldn't learn anything else properly. Now they're electives at best.

"Never built a mass wisdom program" — mass literacy is recent (global literacy rate was ~12% in 1820, ~86% in 2015). Mass media is ~100 years old. Post-scarcity information is ~25 years old. The building blocks for mass wisdom transmission exist for the first time in history. We have the infrastructure; we lack the content and the institution.

See existing Notes column for Dawkins meme irony.""",

    10: """The three questions and their philosophical lineages:
- "Why is there something rather than nothing?" — Leibniz, Principles of Nature and Grace (1714). Though versions appear in pre-Socratic philosophy (Parmenides: "what is, is; what is not, is not").
- "What is the right way to live?" — Socrates in the Republic: "We are discussing no small matter, but how we ought to live." Also the central question of Confucius's Analects, the Bhagavad Gita, and arguably every religious text.
- "How do we come to know?" — the domain of epistemology. Plato's Theaetetus. Descartes' Meditations (1641). Hume's problem of induction. Kant's three Critiques map loosely onto these three questions.

"Every serious question comes from trying to answer them" — example chain: Why is healthcare expensive? → What do we owe each other? → How should we structure society? → What is the right way to live? → What is goodness? → Why are we here? Every "why" chain terminates at a fundamental question.

See existing Notes column for the humility disclaimer ("Much of what follows is not new...").""",

    11: """Socrates quote: Plato, Apology 21d. The Oracle at Delphi (Pythia) declared no one wiser. His investigation — testing the claim against politicians, poets, and craftsmen — is the narrative arc of the Apology. Each group believed they knew; Socrates found they didn't but also didn't know they didn't. His only advantage was knowing.

Epictetus quote: Discourses, Book II, Chapter 17. Epictetus (c. 50–135 CE) was born a slave, studied under Musonius Rufus, freed, taught in Nicopolis. His Discourses were transcribed by his student Arrian — themselves a transmission across generations, surviving only because someone wrote them down. The full text is available on this site.

"Fight our own minds to get there" — relevant cognitive science: confirmation bias, motivated reasoning, the Dunning-Kruger effect (Kruger & Dunning, 1999 — people with low competence systematically overestimate their ability; Socrates identified the pattern 2,400 years earlier), the backfire effect (Nyhan & Reifler, 2010 — correcting a false belief can paradoxically strengthen it). Epistemic humility is not natural; it is trained. Which is why the Academy matters.

"A civilization that abandons such questions does not become practical. It becomes shallow." — Compare with Chesterton: "The madman is not the man who has lost his reason. The madman is the man who has lost everything except his reason." (Orthodoxy, 1908). A civilization that keeps its technical capacity but loses its fundamental orientation is not sane — it is efficient at nothing in particular.""",

    12: """The cross-cultural list unpacked:

Concepts:
- Zhi (知/智): Confucian. One of the five constant virtues (alongside Ren, Li, Yi, Xin). "To know what you know and what you do not know — that is true wisdom" (Analects 2.17). Deep practical wisdom — not abstract knowledge but insight that enables ethical action.
- Sophia (Σοφία): Greek. Root of "philosophy." Personified in Proverbs 8:22–31 as present at creation. Hagia Sophia (537 CE) = "Holy Wisdom." The building itself is a civilizational statement: the highest aspiration is wisdom.
- Geist: German. Hegel, Phenomenology of Spirit (1807). Not easily translated — spirit, mind, collective consciousness of an era. "The Geist fades" describes the erosion in one phrase.

Personifications:
- Maat (𓁦): Egyptian. Goddess/principle of truth, justice, cosmic order. The 42 negative confessions. The weighing of the heart. Foundational to Egyptian civilization for ~3,000 years.
- Saraswati (सरस्वती): Hindu goddess of knowledge, music, arts, wisdom. Depicted with a veena, a book, and a rosary — art, knowledge, and devotion unified in one figure.
- Athena (Ἀθηνᾶ): Greek goddess of wisdom and strategic warfare (not chaotic violence — that's Ares). Born fully formed from Zeus's head. Athens named itself after her — the city is literally named for wisdom.

People:
- Socrates (470–399 BCE), Buddha (Siddhartha Gautama, c. 563–483 BCE), Confucius (Kong Qiu, 551–479 BCE). Three independent civilizations produced foundational wisdom-seekers within roughly the same century. Karl Jaspers called this the Axial Age (The Origin and Goal of History, 1949) — the period when humanity first became conscious of itself as a whole.

Philia: Aristotle, Nicomachean Ethics, Books VIII–IX. Distinguishes friendships of utility, pleasure, and virtue. Philosophy = philia + sophia = the sustained commitment to wisdom. See also Row 17 notes on the corruption of philia as a suffix.

"Wisdom is the integration of these three capacities" — this formulation is the core claim of the entire project. Traditions that held all three together (Rta, arguably Tao in its pre-Confucian/pre-Laozi form) maintained the integration. Traditions that specialized in one branch (Laozi's Dao → Reality, Confucian Dao → Right, Stoic Logos → Reason) achieved depth at the cost of wholeness. The erosion pattern at the civilizational level mirrors the specialization pattern at the philosophical level.""",

    13: """Tools of Reason with origins:
- Logic: Aristotle's Organon (4th century BCE). Syllogistic reasoning. Later: Stoic logic, medieval logic, Boolean algebra (Boole, 1847), predicate logic (Frege, 1879), modal logic (Kripke, 1959).
- Epistemology: "How do we know what we know?" Plato's Theaetetus. Descartes' Meditations (1641). Hume's problem of induction. Gettier problems (1963) — showing justified true belief isn't quite sufficient.
- Hypothesis and experiment: Francis Bacon, Novum Organum (1620). The inductive method. The empirical turn that launched modern science.
- Falsifiability: Karl Popper, The Logic of Scientific Discovery (1934/1959). A claim is scientific only if it could in principle be shown false. This was itself an update to the toolkit — the method improving itself.
- Discourse: See the 3D's of Discourse article on this site (Deliberation, Dialogue, Debate). Civil discourse is itself a tool of Reason — the means by which reasoning happens between people rather than just within one mind.

"The methods themselves must be examined" — Thomas Kuhn, The Structure of Scientific Revolutions (1962). Paradigm shifts. Also Lakatos (research programmes), Feyerabend (Against Method — arguing no single method governs all scientific progress), Bayesian epistemology.

Aquinas's distinction (Summa Theologica): discursive reasoning (ratio) = step-by-step, human; intuitive understanding (intellectus) = immediate, divine. The human mode is sequential and effortful. This is not a deficiency — it is the distinctly human way of knowing. But its cost is why it erodes.

Column 4 note about "a word bad psychologists corrupted" — this refers to the suffix -philia being pathologized. Connects to the philia discussion in Row 12 (Wisdom) and the fuller aside in Row 17's existing notes.

See also Row 22 existing Notes column: "Reason's methods extend far beyond the hard science laboratory..." — this material about social science needing philosophy was considered for the Reason section but works better as a supporting note.""",

    14: """"Starting with Aristotle's Natural Philosophy" — Physics, De Caelo, De Generatione et Corruptione, Meteorologica. Aristotle established systematic empirical observation even though he got many specifics wrong (geocentrism, spontaneous generation). The practice mattered more than the conclusions.

The mythological-to-mechanistic progression:
- Thales of Miletus (c. 624–546 BCE): first to seek natural rather than supernatural explanations. "The primary substance is water." Wrong, but asking the right kind of question.
- Poseidon → tides → lunar gravity (Newton, Principia, 1687)
- Apollo → the sun → nuclear fusion (Bethe, 1939)
- "Spirits" of disease → germ theory (Pasteur, Koch, 1860s–1880s)
Each case: the observation was real, the personification was imprecise, the mechanism was discoverable. The myth was clever, just data-poor.

"Every advance complicates what we ought to do":
- Gravity → cosmology → we are cosmically insignificant. Existential reckoning.
- The atom → nuclear energy → Hiroshima and clean energy. Same knowledge, opposite applications.
- The genome → CRISPR (Doudna & Charpentier, 2012) → gene therapy AND designer babies AND eugenics concerns.
- AI (current) → the most powerful information technology ever built, trained on the collective output of human civilization. Who controls it? Toward what ends? With what accountability? These are Right questions forced into urgency by Reality advances.

Rta (ऋत), the Vedic concept of cosmic order, is arguably the oldest attempt at what this section describes — the claim that there IS an underlying order to reality, prior to the gods themselves. Our exploration of Reality is the attempt to map what Rta asserts exists.""",

    15: """The two-layer distinction:

Laws (codified Right at a point in time):
- Nomos (νόμος): Greek. Law, custom, convention. The nomos/physis debate (convention vs nature) was central to Sophistic and Socratic philosophy — are laws natural or made up?
- Li (禮): Confucian ritual propriety. Governs the five relationships (ruler-subject, parent-child, husband-wife, elder-younger, friend-friend). Analects Book XII.
- Shari'a (شريعة): "the path to water." Islamic law from Quran, Hadith, ijma (consensus), qiyas (analogy).
- Halakha (הלכה): "the way to walk." Jewish law from Torah and Talmud.

Principles by which laws are judged and updated:
- Dikaiosyne (δικαιοσύνη): Greek justice. Aristotle NE Book V: "complete virtue in relation to our fellow humans." The Republic is structured entirely around defining it.
- Yi (義): Confucian righteousness. The moral judgment that sits above Li. One of the five constant virtues.
- Adl (عدل): Islamic justice/equity. One of the 99 names of God (Al-Adl). The principle by which Shari'a is evaluated.
- Tzedek (צדק): Hebrew justice. "Justice, justice shall you pursue" (Deuteronomy 16:20 — repetition deliberate). Root of tzedakah.

Every tradition built both — the code AND the concept that sits above the code and judges whether the code is still right. The code is the snapshot; the principle is the living capacity to revise it.

Dharma (धर्म) straddles both layers — it is simultaneously the prescribed duty AND the principle of rightness by which that duty is assessed. This may be why it resists clean categorization.

"Right is not merely ethics in the academic sense" — academic ethics has largely become a spectator sport: analyzing trolley problems rather than asking whether a civilization is on track. Applied ethics (bioethics, AI ethics) is closer but still tends to be reactive. Right as used here is closer to what the Greeks meant by politike — the art of steering the polis.""",

    16: """The compounding cycle:
- Francis Bacon, Novum Organum (1620): "Knowledge is power" — the first explicit statement that understanding reality gives practical capacity.
- Condorcet, Sketch for a Historical Picture of the Progress of the Human Mind (1795): reason + science + rights = compounding human welfare. Written while hiding from the Terror. He believed in the cycle even as the Revolution devoured its own.
- D.M. Berwick: "Not all change is improvement, but all improvement is change." The progressive-conservative tension in one sentence.

"Wisdom can be recovered" — the Renaissance as proof of concept: Greek and Roman texts preserved by Islamic scholars (House of Wisdom, Baghdad, 8th–13th centuries; translation schools of Córdoba and Toledo) were reintroduced to Europe in the 12th–15th centuries. Wisdom tied to truth survives even centuries of neglect — if the texts survive. This is one reason the web app exists: digital text doesn't burn.

"The full relationship between the three is richer than captured in this summary" — intentional understatement. Reality informs Right (what's possible constrains what's desirable). Right directs Reason (values determine what questions we prioritize). Reason checks Right (logic tests whether our values are internally consistent). Each pair has a bidirectional relationship, and all three interact simultaneously. The articles on Power and Paideia develop these dynamics further.""",

    17: """See existing Notes column for the philia aside (paraphilia corruption). Consider whether this note belongs here or in Row 12 (Wisdom), since philia is introduced in the article at the Wisdom section.

"Remove the rot in the Temples, and a bit more" — the "bit more" encompasses: political spectrums (how we talk about aiming), power (what prevents good ideas from winning), and economic questions (post-scarcity, AI, displacement costs). These are addressed in the follow-up articles.

"That is the problem. That is the inheritance. That is the work." — three beats that function as a commitment. The problem (erosion). The inheritance (the tradition of people who fought it before). The work (what we do now).""",

    18: """The three follow-ups address the three major gaps this article leaves open:
- Erosion: The mechanism. WHY does the cycle fail? Pathos/Mythos/Ethos/Logos as modes of engaging with truth, each with its own decay pattern. The demand side (Sneaky Candy). The supply side (institutional failure).
- Power: The obstacle. Why can't good ideas just win? Because ideas need power to become reality, and power corrupts the process. The 4 domains (Physical, Resources, Social, Ideational) and the cascade when the ideational domain weakens.
- Paideia: The solution. What institutions do we need? The 6 educational functions every civilization requires (Academy, Guilds, Laboratory, News, Agora, Temple), how all are currently failing, and what rebuilding looks like. The Grandfather Principle.

These three plus this Foundations article form the core chain. Everything else — political spectrums, specific policy questions, breakdowns of current events — branches from them."""
}


def main():
    with open(INPUT, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        rows = list(reader)

    # Set header for column 8
    while len(headers) <= TARGET_COL:
        headers.append('')
    headers[TARGET_COL] = HEADER_LABEL

    # Write notes into column 8
    for row_num, note_text in NOTES.items():
        row_idx = row_num - 2  # row 2 = index 0
        if 0 <= row_idx < len(rows):
            while len(rows[row_idx]) <= TARGET_COL:
                rows[row_idx].append('')
            rows[row_idx][TARGET_COL] = note_text.strip()

    # Pad all rows to same length
    max_cols = max(len(headers), max(len(r) for r in rows))
    while len(headers) < max_cols:
        headers.append('')
    for r in rows:
        while len(r) < max_cols:
            r.append('')

    with open(OUTPUT, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(headers)
        for r in rows:
            writer.writerow(r)

    print(f"Written {len(NOTES)} notes to column {TARGET_COL} ({HEADER_LABEL})")
    print(f"Output: {OUTPUT}")


if __name__ == '__main__':
    main()
