"""
Generate refashioned versions of Summa Theologica Part I, Q27-Q43
(Treatise on the Trinity)
"""

import json
import os

BUILD_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(BUILD_DIR, "summa_p1_refashioned_part3.json")

data = [
  # ========== Q27: The Procession of the Divine Persons ==========
  {
    "index": "27.0",
    "refashioned": "Having established what belongs to God's unified essence, we turn to the Trinity of persons. The persons are distinguished by relations of origin, so we begin with procession itself: (1) Is there procession in God? (2) Can any such procession be called generation? (3) Is there a second procession beyond generation? (4) Can that second procession also be called generation? (5) Are there more than two processions?"
  },
  {
    "index": "27.1a",
    "refashioned": "Procession usually implies movement outward -- something leaving its source. God, being absolutely simple and self-contained, has nothing external in that sense. So in what way can there be procession in God?\n\nThe key is distinguishing external from internal procession. When a cause produces an external effect -- heat radiating outward from a fire -- the effect is separate from the source. But intellectual activity stays within the agent. When you understand something, the concept you form does not leave your mind; it arises within it. The 'word of the heart' proceeds from your knowledge yet remains in you.\n\nThis is how procession works in God. It is not an outward movement or an external effect. It is an interior emanation, like a word proceeding from a speaker yet remaining within the speaker. The Word proceeds from the Father and stays perfectly one with Him. This is what Catholic theology means by divine procession: not departure, but an intelligible emanation within God's own being."
  },
  {
    "index": "27.1b",
    "refashioned": "The objection that procession requires separation misunderstands the kind of procession at work. In external procession, what goes out is necessarily distinct from its source. But in interior intellectual procession, the opposite is true: the more perfectly something is understood, the more closely the concept is united with the mind that forms it. Since God's understanding is infinitely perfect, the Word that proceeds from Him is perfectly one with its source, with no diversity whatsoever.\n\nNor does this conflict with God being the first principle. An architect contains the plan of a house within his art; if the architect were the first principle, the art would be included in that first principle. God is like an architect whose creative design is internal to Himself."
  },
  {
    "index": "27.2a",
    "refashioned": "Can this procession of the Word in God properly be called generation -- a begetting?\n\nGeneration in its broadest sense just means coming into existence. But in living things, generation has a stricter meaning: a living being originates from a conjoined living principle, and what proceeds comes forth as a likeness of the same nature. A hair growing from a body is not properly 'begotten'; only what proceeds by way of likeness in the same specific nature counts -- like a human from a human.\n\nThe procession of the Word in God meets every requirement of generation in this strict sense. It proceeds by an intellectual act, which is a vital operation. It comes from a conjoined principle (the Father's own intellect). It proceeds by way of likeness, since the concept of the intellect is a likeness of what is understood. And it exists in the same nature, since in God understanding and existence are identical. Therefore the procession of the Word is genuine generation, and the Word proceeding is properly called the Son."
  },
  {
    "index": "27.2b",
    "refashioned": "The difference from human thought is crucial. In us, the act of understanding is not identical with the substance of the intellect, so the concept we form is not the same nature as its source. In God, the act of understanding is the divine substance itself. Therefore the Word that proceeds is fully subsistent in the same divine nature, and is properly called begotten -- the Son.\n\nAs for the objection that whatever is generated receives derived existence and so cannot be self-subsistent: not everything that comes from another exists in a subject. The whole substance of created being comes from God, yet there is no pre-existing subject that receives it. Similarly, what is generated in God receives divine existence from the Father, but not as something received into matter. The Son's existence is the divine existence itself, shared without division."
  },
  {
    "index": "27.3",
    "refashioned": "Is the procession of the Word the only procession in God, or is there another?\n\nThere are two, because the internal acts of an intellectual nature are two: understanding and willing. The procession of the Word corresponds to the act of understanding. But the will also operates within the agent: when we love something, the beloved becomes present in the lover through that act of love. So beyond the procession of the Word, there is a second procession -- the procession of Love.\n\nThese two cannot collapse into one, even though in God will and intellect are identical in being. The nature of love requires that it proceed from something already conceived: you cannot love what you have not first understood. So there is an intrinsic order -- the Word comes first in the order of intelligibility, and Love follows from it. This distinction of order is enough to make them genuinely two processions, not one."
  },
  {
    "index": "27.4",
    "refashioned": "The procession of Love is not generation. Here is why.\n\nThe intellect is actualized by its object residing within it as a likeness. When you understand something, you form a concept that is a likeness of the thing understood. That is why intellectual procession is properly called generation -- every generator produces its own likeness.\n\nThe will works differently. The will is actualized not by a likeness of the object residing in it, but by an inclination toward the object. Love is not a copy of the beloved; it is a movement toward the beloved. So what proceeds by way of love does not proceed as a likeness, and therefore does not proceed as begotten.\n\nInstead, what proceeds by love proceeds as 'spirit' -- a term that captures vital movement and impulse. That is why the third person is called the Holy Spirit: the name expresses the dynamic, impulsive character of love, as when we say someone is 'moved' or 'inspired' by love."
  },
  {
    "index": "27.5",
    "refashioned": "There are exactly two processions in God, not more. Internal processions can only arise from actions that remain within the agent. In an intellectual nature, those actions are understanding and willing -- and only those. Sensation might seem to be internal, but it depends on an external stimulus and belongs to the bodily order, not the purely intellectual.\n\nPower is not a third internal action; power is the principle by which an agent acts on something external, so it gives rise to the procession of creatures, not of divine persons. Goodness belongs to the essence, not to a distinct operation. And unlike human beings who understand and love through multiple successive acts, God understands all things by one simple act and wills all things by one act. So there is one perfect Word and one perfect Love -- not an infinite chain of words from words or loves from loves."
  },

  # ========== Q28: The Divine Relations ==========
  {
    "index": "28.0",
    "refashioned": "With procession established, we examine the divine relations: (1) Are there real relations in God? (2) Are these relations identical with the divine essence? (3) Are they really distinct from each other? (4) How many are there?"
  },
  {
    "index": "28.1a",
    "refashioned": "Relations in God are real, not merely logical constructions.\n\nMost categories -- quantity, quality, and so on -- describe something inherent in a subject. Relation is unique: its entire nature consists in referring to something else. Sometimes this reference exists only in the mind, as when reason compares 'man' to 'animal' as species to genus. But sometimes things are by their very nature ordered to each other, and in that case the relation is real -- as a heavy object is really ordered toward the center of gravity.\n\nNow, when something proceeds from a principle of the same nature, both the source and what proceeds share the same order of being, and their mutual reference is real. The divine processions are precisely this: the Son proceeds from the Father within the identity of the same divine nature. Therefore the relations between them -- paternity and filiation, spiration and procession -- are real relations, not merely constructs of theological reasoning.\n\nWithout real relations, the Father would not really be Father, nor the Son really Son. That would be the Sabellian heresy: one person wearing different masks."
  },
  {
    "index": "28.1b",
    "refashioned": "Several clarifications. First, God's relations to creatures are not real in God (creatures depend on God, not the reverse), so there is no parallel between creaturely relations and internal divine relations. Second, the relations that follow the operation of the intellect -- between the Word and its source -- are real, not merely logical, because the intellect and the Word are real things really related through the act of understanding. The relations within the mind's activity are different from the relations the mind observes between already-understood objects. Paternity and filiation in God fall into the former category: they are real."
  },
  {
    "index": "28.2a",
    "refashioned": "Relation in God is really identical with the divine essence, though they differ in how we think about them.\n\nIn creatures, accidents have an existence that inheres in a subject. Relation is special among accidents because its formal content is not 'something in a subject' but 'reference to another.' Still, as an accident, it does inhere in a subject. Transfer this to God, where there are no accidents: whatever exists in God has the existence of the divine essence itself. So insofar as relation has being, it is the divine essence. But insofar as relation means 'reference to another,' it does not describe the essence as such -- it points toward the opposite term.\n\nGilbert de la Porree got this wrong by treating the divine relations as something external or 'assistant' to the essence. That was condemned. The truth is that relation in God is the divine essence in its very being, yet carries a distinct intelligible content -- the reference to another -- that the word 'essence' does not express. Essence and relation are one reality understood under two aspects."
  },
  {
    "index": "28.2b",
    "refashioned": "When Augustine says that relational terms are not predicated 'of the substance,' he means they are not predicated in the mode of substance -- not that they exist as something separate from it. The divine perfection contains more than any single name can express. 'Wisdom' does not exhaust God's reality; neither does 'relation.' But that does not mean there is something in God besides relation in reality -- only in our multiple names for what is ultimately one.\n\nNor does the relational character of these terms make the divine essence imperfect, as if God's reality were merely relational. The essence comprehends within itself the perfection of every genus. Relational names capture one genuine aspect of that inexhaustible perfection."
  },
  {
    "index": "28.3",
    "refashioned": "The divine relations are really distinct from each other, even though each is identical with the divine essence.\n\nThis seems contradictory: how can two things both be identical with a third thing yet distinct from each other? The answer lies in relative opposition. Things that are identical with the same thing in every respect -- both really and logically -- are identical with each other. But paternity and filiation, while each identical with the divine essence in being, carry opposite relational meanings: one says 'source of' and the other says 'derived from.' This relative opposition is what makes them really distinct.\n\nAttributes like goodness and power do not involve mutual opposition, so they are not really distinct from each other in God. But fatherhood and sonship are inherently opposed as correlatives. Without this real distinction of opposed relations, there would be no real Trinity -- just one person under different descriptions, which is exactly the Sabellian error that the doctrine of the Trinity rejects."
  },
  {
    "index": "28.4a",
    "refashioned": "There are exactly four real relations in God: paternity, filiation, spiration, and procession.\n\nReal relations in God can only be based on the two internal processions (since God's relations to creatures are not real in Him). Each procession generates two opposed relations: the relation of the principle to what proceeds, and the relation of what proceeds to its principle.\n\nFrom the procession of the Word (generation): paternity (the Father's relation as begetting principle) and filiation (the Son's relation as begotten). From the procession of Love: spiration (the relation of the principle from which Love proceeds) and procession (the relation of the one who proceeds as Love).\n\nThe procession of Love has no proper name of its own, and neither do its associated relations. 'Spiration' and 'procession' are borrowed from the processes themselves rather than being names that express the relational content as precisely as 'paternity' and 'filiation' do."
  },
  {
    "index": "28.4b",
    "refashioned": "Why is there no real relation between God's intellect and its object, or between God's will and its object? Because in God, the knower and the known are identical, as are the willer and the willed. A thing cannot have a real relation to itself. But the relation between the Word and its source is different: the Word proceeds by an intelligible act, so the relation is between the one producing and what is produced -- and that is real.\n\nAs for the suggestion that intelligible relations multiply infinitely (since you can understand that you understand, ad infinitum): in us, each new act of reflection is a separate act. In God, all understanding is one single act, so no infinite multiplication follows. The ideas in God's mind are eternal but are distinguished only logically, not by real relations. And equality and likeness among the persons are logical relations, not additional real ones."
  },

  # ========== Q29: The Divine Persons ==========
  {
    "index": "29.0",
    "refashioned": "With processions and relations established, we turn to the persons themselves -- first considered in general, then individually. Four questions arise: (1) What is the definition of 'person'? (2) How does 'person' relate to essence, subsistence, and hypostasis? (3) Can the word 'person' properly be applied to God? (4) What does it signify when applied to Him?"
  },
  {
    "index": "29.1a",
    "refashioned": "Boethius defined 'person' as 'an individual substance of a rational nature.' Every word earns its place.\n\nSubstance is individuated by itself -- unlike accidents, which are individuated by the subjects they inhere in. (This particular whiteness is 'this' because it exists in this particular thing.) So individuals in the genus of substance deserve a special name: 'hypostasis,' or first substance.\n\nBut among substances, rational ones stand out further. They have dominion over their own actions. They do not merely act by nature; they act for themselves. Actions belong to singulars, and rational singulars command their own actions in a way that rocks, plants, and even animals do not. This is why the individuals of rational nature receive yet another special name: 'person.'\n\n'Individual substance' places person in the genus of substance as a singular. 'Rational nature' restricts it to the intellectual order. The definition is precise and complete."
  },
  {
    "index": "29.1b",
    "refashioned": "To the objection that singulars cannot be defined: we are not defining this or that particular person but what it is to be a person in general -- the general idea of singularity. To the objection that 'individual substance' is redundant if substance already means first substance, or contradictory if it means second substance: substance here is taken in a general sense (covering both first and second), and 'individual' restricts it to first substance. The word 'individual' also excludes what is assumed into a higher unity -- as Christ's human nature is not a person because it is assumed by the Word.\n\nAs for why 'nature' rather than 'essence': nature originally meant the intrinsic principle of generation and movement, and by extension came to mean the form that completes a thing's essence. Since person means the singular in a determinate genus, 'nature' -- which points to the specific form -- fits better than 'essence,' which is more generic. Finally, the separated soul is not a person because it is naturally a part of the composite human being, retaining its orientation toward reunion with the body."
  },
  {
    "index": "29.2a",
    "refashioned": "How does 'person' relate to the technical terms 'hypostasis,' 'subsistence,' and 'essence'?\n\nSubstance has two senses. In one sense, it means the quiddity or essence -- what the definition expresses. In another, it means the concrete individual that subsists in a genus. This concrete individual can be named three ways, each highlighting a different aspect. Insofar as it exists in itself and not in another, it is called a 'subsistence.' Insofar as it underlies a common nature (as this particular man underlies human nature), it is called 'a thing of nature.' Insofar as it underlies accidents, it is called a 'hypostasis' or 'substance.'\n\nAll three names apply to individuals across every genus of substance. 'Person' is the special case: it is what these three names mean when restricted to the genus of rational substances. So person, hypostasis, subsistence, and essence are not synonyms, but they overlap in predictable ways."
  },
  {
    "index": "29.2b",
    "refashioned": "The Greeks use 'hypostasis' where we would say 'person' in the context of rational beings. When we say 'three subsistences' in God, we mean what the Greeks call 'three hypostases.' The Latin 'substance' was avoided in the plural because it can also mean essence, and saying 'three substances' might suggest three essences.\n\nEssence, properly, is what the definition expresses -- the common form, not the individual matter. So essence, hypostasis, and person are not identical in things composed of matter and form: essence covers the common nature, while hypostasis and person add the individualizing principles. In God, of course, there is no matter, so the distinctions work differently -- but the conceptual framework still applies."
  },
  {
    "index": "29.3a",
    "refashioned": "Can the word 'person' properly be applied to God?\n\nYes. 'Person' signifies what is most perfect in all of nature: a subsistent individual of a rational nature. Self-mastery, self-knowledge, self-possession -- these are the highest perfections we know. Since every perfection must be attributed to God in a supereminent way, the name 'person' applies to God preeminently.\n\nThe objection that 'person' is not found in Scripture misses the point. Scripture affirms everything the word signifies -- supreme self-subsistence, perfect intelligence. If we could speak of God only in the exact words of Scripture, we could never discuss God in any language but the original Hebrew and Greek. The pressure of refuting heresies made it necessary to coin new terms to express ancient truths. The Apostle warns against 'profane novelties of words,' not against every new term that faithfully captures revealed truth."
  },
  {
    "index": "29.3b",
    "refashioned": "The word 'person' originally comes from the masks worn in theatrical performances -- personae, through which actors 'sounded through' (personando). But its meaning evolved. Because famous characters were represented by these masks, 'person' came to signify anyone of high dignity. Then it was extended to every subsistent individual of rational nature. Since the dignity of the divine nature exceeds every other dignity, the word 'person' belongs to God preeminently.\n\nAs for 'hypostasis': Jerome warned that 'poison lurks in this word' not because the concept is wrong, but because Latin-speaking heretics exploited the confusion between 'hypostasis' (which the Greeks used for 'person') and 'substance' (which Latins often took to mean 'essence'). The word itself, properly understood, applies to God -- it signifies subsistence.\n\nRichard of St. Victor refined Boethius's definition for the divine case: a person in God is 'the incommunicable existence of the divine nature.' This captures the divine context better, since God is not individuated by matter but by the incommunicability of each relational existence."
  },
  {
    "index": "29.4a",
    "refashioned": "Does the word 'person,' when applied to God, signify relation or substance?\n\nThis is a harder question than it looks. 'Person' is predicated in the plural of the three (unlike essential terms), yet by itself it does not obviously refer to another (unlike relational terms like 'Father'). Some thinkers concluded that 'person' is purely an essential term, only given a relational sense by ecclesiastical convention. But that cannot be right: if 'person' by its own meaning expressed only essence, then saying 'three persons' would give heretics more ammunition, not less.\n\nOthers said it signifies both essence and relation. Among these, some said it signifies essence directly and relation indirectly; others said the reverse. The latter come closer to the truth."
  },
  {
    "index": "29.4b",
    "refashioned": "The key insight is that a word can carry different content depending on the nature to which it is applied. 'Person' in general means an individual subsistent in a rational nature. What makes someone individual is whatever distinguishes them within their nature. In human nature, this flesh, these bones, this soul -- the individualizing principles. In God, the only distinction is relational: the relations of origin.\n\nSince relation in God is not an accident inhering in a subject but the divine essence itself, a divine relation subsists. The divine paternity is God the Father. So 'divine person' signifies a relation as subsisting -- relation expressed in the mode of a substance. It signifies relation directly (because relation is what distinguishes persons in God) and essence indirectly (because the essence is what the relation subsists in). Before the heretical attacks forced precision, no one thought carefully about this. Afterward, it became clear that 'person' carries relational signification not just by convention but by the logic of its own meaning when applied to God."
  },
  {
    "index": "29.4c",
    "refashioned": "When Augustine says the Father is 'person in regard to Himself,' he means 'person' is not predicated of the Father as pointing to the Son the way 'Father' does. It signifies relation, but in the mode of a substance -- a subsistent hypostasis -- not in the mode of an explicit reference to another.\n\nWhen asked 'Three what?' and answering 'Three persons,' the 'what' refers to the suppositum (the concrete individual), not to the essence as such. And the fact that 'person' means different things concretely in God versus in humans does not make it equivocal any more than 'animal' becomes equivocal because horses and donkeys differ. The term is analogous -- as all language about God and creatures must be."
  },

  # ========== Q30: The Plurality of Persons in God ==========
  {
    "index": "30.0",
    "refashioned": "We now consider the plurality of persons: (1) Are there several persons in God? (2) How many? (3) What do numerical terms signify in God? (4) Can the term 'person' be common to all three?"
  },
  {
    "index": "30.1",
    "refashioned": "There are several persons in God. The argument is straightforward. 'Person' in God signifies a relation as subsisting in the divine nature. There are several real relations in God. Therefore there are several subsisting realities in the divine nature -- which is to say, several persons.\n\nThis does not mean several essences. The definition of 'person' includes 'substance' not in the sense of essence but of suppositum -- the concrete individual. The Greeks say 'three hypostases' rather than 'three substances' to avoid confusion.\n\nNor does plurality of persons compromise divine simplicity. God's unity and simplicity exclude every plurality of absolute things -- but not plurality of relations. Relations do not add composition to what they are predicated of. And numerical plurality in God is not like parts composing a whole: the Father is not one-third of the Trinity. Each person possesses the entire divine magnitude."
  },
  {
    "index": "30.2a",
    "refashioned": "There are exactly three persons in God -- not two, not four, not more.\n\nThe divine persons are subsisting relations, and real distinction among them comes only from relative opposition. Two opposed relations yield two persons. Non-opposed relations can belong to the same person.\n\nPaternity and filiation are opposed: the one who begets and the one who is begotten. So they constitute two persons -- the Father and the Son.\n\nNow the other two relations: spiration (the principle of the procession of Love) and procession (Love proceeding). Procession cannot belong to the Father or the Son, because the procession of Love follows from the procession of the Word, not the other way around. Spiration, however, is not opposed to either paternity or filiation. So spiration belongs to both the Father and the Son jointly. That leaves procession as the distinguishing relation of a third person: the Holy Spirit, who proceeds by way of Love.\n\nThree persons. No more, no fewer."
  },
  {
    "index": "30.2b",
    "refashioned": "Though there are four relations, only three of them constitute distinct persons. Spiration is a real relation but not a 'personal property,' because it belongs to two persons, not one. The three personal properties that actually constitute persons are paternity (the Father), filiation (the Son), and procession (the Holy Spirit).\n\nThe Holy Spirit does not produce a further divine person because the Father and the Holy Spirit share one and the same goodness. The goodness belongs to the Holy Spirit as received from another; it belongs to the Father as the principle of communication. The relative opposition between the Holy Spirit and any hypothetical further person simply does not exist, so no further procession occurs.\n\nAs for the objection that three persons imply measurement: when number applies to things numbered in God, each person possesses the same full magnitude as the whole Trinity. One is not a part of three."
  },
  {
    "index": "30.3a",
    "refashioned": "Do numerical terms in God signify something real?\n\nThe answer requires distinguishing two kinds of plurality. One is quantitative plurality -- the kind that comes from dividing a continuous magnitude, producing number as a species of quantity. This exists only in material things and has no place in God. The other is transcendental plurality -- the formal distinction that arises whenever things are divided by different forms or natures. This kind of 'many' is not a quantity but a feature of being itself.\n\nWhen we say 'three persons,' we are not applying mathematical number to God. We are using transcendental multitude: each person is signified as undivided in itself and distinct from the others. The numeral adds to the reality it names only a negation of division. 'One essence' means the essence undivided. 'One person' means the person undivided. 'Three persons' means those persons, each undivided in itself. Number here is a way of affirming distinction, not of counting parts."
  },
  {
    "index": "30.3b",
    "refashioned": "'One' does not exclude multitude; it excludes division. 'Multitude' does not remove unity; it affirms that each of its members is undivided. These are not purely negative terms -- they do signify something real (the persons themselves), while adding a negation of division. Just as 'white' signifies a real color while excluding blackness, number in God signifies real persons while negating their division."
  },
  {
    "index": "30.4",
    "refashioned": "Can the term 'person' be common to the three divine persons?\n\nYes, but in a specific sense. It is not common the way an essence is common (shared as one reality), nor the way a genus or species is common (a universal predicated of many). 'Person' is common by a community of idea: each divine person subsists distinctly in the divine nature, and 'person' names this shared mode of being -- distinct, incommunicable subsistence.\n\nThis is like the way 'some man' indicates the mode of singular existence without specifying which singular. In human affairs, 'person' signifies not the nature itself but the reality subsisting in that nature. In God, each person subsists distinctly from the others in the same divine nature. That shared pattern of incommunicable subsistence is what makes 'person' genuinely common to all three, without making it a genus, a species, or a universal."
  },

  # ========== Q31: Unity and Plurality in God ==========
  {
    "index": "31.0",
    "refashioned": "We now address what belongs to unity or plurality in God: (1) Can we speak of 'Trinity'? (2) Is the Son 'other than' the Father? (3) Can the exclusive word 'alone' be joined to essential terms? (4) Can it be joined to personal terms?"
  },
  {
    "index": "31.1",
    "refashioned": "The name 'Trinity' is proper to God. It signifies the determinate number of persons -- making explicit what 'plurality' leaves vague.\n\nThe word does not signify the essence directly (the Father alone is not the Trinity), nor a particular relation. Etymologically it might suggest 'trine-unity' (the one essence of three persons), but strictly it means the number of persons sharing one essence.\n\n'Trinity' is not a collective noun the way 'people' is. A collective implies the weakest kind of unity -- a group held together by order. In God there is unity of order and unity of essence. Nor does 'Trinity' imply inequality the way 'triplicity' does. And 'Trinity is trine' cannot be said, because that would multiply the Trinity by itself, implying nine realities -- which is absurd."
  },
  {
    "index": "31.2a",
    "refashioned": "Is the Son 'other than' the Father? This requires linguistic precision, because Trinitarian theology is an exercise in exact language where the wrong word leads to heresy.\n\nTo avoid the error of Arius (who divided the essence), we must not say the persons are 'diverse' or 'different,' since those words imply distinction of essence. We may say 'distinct,' because distinction can be purely relational. We avoid 'separation' and 'division' (which imply parts), 'disparity' (which implies unequal quality), and 'alien' (which implies strangeness).\n\nTo avoid the error of Sabellius (who collapsed the persons into one), we must not say God is 'singular' or 'solitary,' since those deny plurality of persons.\n\nThe precise formulation: the Son is 'another person' than the Father (alius -- a different 'who'), but not 'another thing' (aliud -- a different 'what'). In the masculine, 'other' refers to the suppositum and correctly affirms personal distinction. In the neuter, 'other' would refer to the essence and wrongly imply essential difference."
  },
  {
    "index": "31.2b",
    "refashioned": "'Other' (in the masculine) refers to the suppositum -- the concrete individual -- and that is sufficient where the substance is distinct as hypostasis. 'Diverse' implies distinction of form, and there is only one form in God. 'Alien' means extraneous and dissimilar, which is far stronger than 'other.'\n\nThe grammatical distinction matters: neuter gender is formless and expresses the common essence; masculine and feminine are formed and express the determinate suppositum. So when we ask 'Who is the Father?' the answer names a person. When we ask 'What is the Father?' the answer describes the essence. Father and Son are 'one thing' (unum -- neuter) but not 'one person' (unus -- masculine). They are 'another person' (alius) but not 'another thing' (aliud)."
  },
  {
    "index": "31.3a",
    "refashioned": "Can we say 'God alone is eternal' or 'God alone is wise'? It depends on how 'alone' functions.\n\nTaken as a categorematic term (describing the subject absolutely), 'alone' would mean 'solitary' -- which is false of God, since there are three persons. But taken as a syncategorematic term (modifying the relation between subject and predicate), 'alone' means 'no one else shares this predicate.' In that sense, 'God alone is eternal' is perfectly true: nothing besides God is eternal.\n\nSo 'alone' can be joined to essential terms in God when it functions to exclude creatures from the predicate, not when it implies God's internal solitude."
  },
  {
    "index": "31.3b",
    "refashioned": "God would be alone even if angels and saints were with Him, if there were no plurality of persons within Him. The presence of creatures does not remove divine solitude; only the internal society of the three persons does.\n\nThe adverb 'only' can modify either the subject or the predicate. 'Only Socrates runs' excludes other runners. 'Socrates only runs' excludes other activities. So 'the Father is God alone' is problematic unless carefully qualified -- it could be read as denying divinity to the Son and Spirit. But 'God alone creates' is fine, because it excludes creatures from the creative act. And critically, what is true of God as a whole cannot always be distributed to individual persons with the exclusive term attached. 'God alone creates' does not entail 'the Father alone creates,' just as 'man alone is a rational animal' does not entail 'Socrates alone is a rational animal.'"
  },
  {
    "index": "31.4",
    "refashioned": "Can we say 'the Father alone is God'? It depends entirely on how the statement is parsed.\n\nIf 'alone' means the Father is solitary, it is false. If 'alone' excludes others from the subject -- meaning 'He who, with no other, is the Father, is God' -- it is true but trivially so. If 'alone' excludes others from the predicate in the masculine sense (no other person is God), it is false, because the Son and Spirit are also God. If it excludes in the neuter sense (no other thing is God), it is true, because the Son is another person but not another thing.\n\nWhen Scripture says 'Thee, the only true God,' Augustine takes this as referring to the whole Trinity, not exclusively to the Father. Or if it refers to the Father's person, the other persons are not excluded because of the unity of essence. The bottom line: exclusive terms attached to personal names require careful handling. They should be interpreted charitably when found in authoritative texts, not pressed into service for heretical conclusions."
  },

  # ========== Q32: The Knowledge of the Divine Persons ==========
  {
    "index": "32.0",
    "refashioned": "How do we know the divine persons? (1) Can the Trinity be known by natural reason? (2) Are there 'notions' in God? (3) How many notions are there? (4) Can we hold differing opinions about them?"
  },
  {
    "index": "32.1a",
    "refashioned": "Can natural reason -- unaided by revelation -- discover the Trinity?\n\nSome point to philosophical precedents. Aristotle invoked the number three in speaking of divine greatness. Augustine found echoes of the Word in Platonic writings. Trismegistus spoke of the Monad begetting a Monad.\n\nOthers argue that probable or even necessary arguments exist for every truth, including the Trinity. Richard of St. Victor claimed as much. Arguments from God's infinite goodness (which must communicate itself infinitely) and from the need for partnership in possessing good have been proposed. Augustine himself used the procession of word and love within the human mind as an image of the Trinity.\n\nBut against this stands the testimony of the great theologians: Hilary says no one should think to reach the mystery of divine generation by human reason alone. Ambrose says the mind fails and the voice falls silent before it. The Trinity is distinguished by generation and procession -- and these are precisely what human understanding cannot grasp on its own."
  },
  {
    "index": "32.1b",
    "refashioned": "Natural reason cannot attain the Trinity. Here is why.\n\nWe know God through creatures, as effects point to their cause. But the creative power of God belongs to the whole Trinity equally -- it pertains to the unity of essence, not the distinction of persons. So from creation we can know what belongs to God's unity (that He exists, that He is one, that He is good), but not what belongs to the distinction of persons.\n\nAttempting to prove the Trinity by natural reason actually damages the faith in two ways. First, it undermines the dignity of faith, which consists precisely in believing invisible things that exceed reason. Second, it invites ridicule from unbelievers, who will conclude that Christians base their faith on weak arguments and believe for no better reasons.\n\nThe proper approach: with those who accept revelation, argue from Scripture. With those who accept nothing of revelation, show that faith's claims are not impossible -- but do not pretend to demonstrate them."
  },
  {
    "index": "32.1c",
    "refashioned": "The philosophers did not actually discover the Trinity. When Aristotle invoked the number three, he was noting that ancient peoples used it in worship because of some perfection in threeness -- not asserting three persons in God. The Platonists spoke of a Word, but meant the divine idea or exemplar, not a begotten person. Trismegistus's 'Monad begetting a Monad' referred to the production of the world, not the generation of the Son.\n\nArguments from God's goodness or from the human mind can confirm the Trinity once it is already accepted on faith, the way a scientific theory can be confirmed by showing its results match observation. But they cannot prove it independently, any more than one astronomical model proves there is no other model that fits the data.\n\nWhy then was the Trinity revealed at all, if reason cannot reach it? Two reasons. First, for a correct understanding of creation: knowing that God made all things by His Word prevents the error that creation was necessary, and knowing that Love proceeds in God shows that creation flows from goodness, not need. Second, for understanding salvation, accomplished by the incarnate Son and the gift of the Holy Spirit."
  },
  {
    "index": "32.2a",
    "refashioned": "Are there 'notions' in God -- abstract properties by which we identify and distinguish the persons?\n\nSome say there should be no notions, since God is supremely simple and anything said of God concerns either the unity of essence or the trinity of persons. Notions seem to fall into neither category.\n\nBut we need them. When someone asks 'By what are the three persons one?' we answer: by the essence. When they ask 'By what are they three?' we need abstract terms like paternity and filiation to answer. The essence is the 'what'; the person is the 'who'; the notion is the 'whereby.'"
  },
  {
    "index": "32.2b",
    "refashioned": "Some thinkers tried to eliminate notions by treating abstract terms as shorthand for concrete ones -- 'paternity' just means 'the Father.' But abstract and concrete names serve different purposes even in God, where both express the same simple reality: abstract names express simplicity, concrete names express subsistence.\n\nThere is also a technical reason notions are indispensable. The Father is related to two persons -- the Son and the Holy Spirit -- by two distinct relations (paternity and spiration), not one. If the Father's relation to both were a single relation, then the Son and the Holy Spirit would be related back to the Father by a single relation, and since relations are what multiply persons, they would not be two persons but one. So the Father must have multiple relational properties, and we need abstract terms to distinguish them."
  },
  {
    "index": "32.2c",
    "refashioned": "Though notions are not mentioned in Scripture by name, they are contained implicitly in the persons that Scripture does name, as the abstract is contained in the concrete. And though notions cannot be predicated of essential or personal acts (we do not say 'paternity creates' or 'paternity begets'), essential attributes that do not imply action -- like eternity and immensity -- can be predicated of them. We can say 'paternity is eternal' because that simply removes a creaturely limitation."
  },
  {
    "index": "32.3a",
    "refashioned": "There are five notions in God.\n\nNotions are the proper ideas by which we identify each divine person. Persons can be known either as the source of another or as proceeding from another. The Father is known: (1) as from no one -- 'innascibility'; (2) as source of the Son -- 'paternity'; (3) as co-source of the Holy Spirit -- 'common spiration.' The Son is known: (4) as begotten from the Father -- 'filiation'; and He also shares common spiration with the Father. The Holy Spirit is known: (5) as proceeding from Father and Son -- 'procession.'\n\nOf these five, four are relations (innascibility is not a relation in the strict sense, since it does not refer to another but negates being from another). Four are properties belonging to one person only (common spiration is not a property, since it belongs to two persons). Three are personal notions that actually constitute the persons: paternity, filiation, and procession."
  },
  {
    "index": "32.3b",
    "refashioned": "The multiple notions belonging to one person (for instance, the Father has innascibility, paternity, and common spiration) do not compose that person out of parts. Since they are not mutually opposed by relative opposition, they do not differ in reality. But they differ in concept and cannot be predicated of each other: spiration is not paternity, just as knowledge is not power, even though in God both are one reality.\n\nNo sixth notion is needed for the Holy Spirit's not being a principle of further procession, because this is not a mark of dignity (the way the Father's being from no one is). And the Son and Spirit do not share a single notion of 'proceeding from the Father,' because they proceed in different ways (generation vs. spiration), and a notion must be based on something specific."
  },
  {
    "index": "32.4",
    "refashioned": "Can theologians hold differing opinions about the notions? Yes -- within limits.\n\nSome truths are directly articles of faith (the Trinity, the Incarnation). A false opinion about these is heresy. Other truths are indirectly matters of faith: denying them entails consequences that contradict articles of faith. Before the entailment is recognized, holding a wrong view is not heretical. Once the Church has determined the consequences, it becomes so.\n\nThe notions themselves are not articles of faith. So differing opinions about them are permissible -- provided no one knowingly holds a view that leads to consequences against the faith."
  },

  # ========== Q33: The Person of the Father ==========
  {
    "index": "33.0",
    "refashioned": "We now consider the persons individually, starting with the Father: (1) Is the Father a 'principle'? (2) Is 'Father' His proper name? (3) Is 'Father' said personally before essentially? (4) Does unbegottenness belong to the Father alone?"
  },
  {
    "index": "33.1",
    "refashioned": "The Father is properly called a 'principle' -- meaning simply 'that from which another proceeds.' The Greeks use 'cause' and 'principle' interchangeably for the divine persons, but the Latin tradition prefers 'principle' because 'cause' can imply priority and dependency. A principle need not be prior to or greater than what proceeds from it; it only needs to be that whence something originates.\n\nSince the Son proceeds from the Father, the Father is a principle. 'Principle' is used here not of the essence (which is common) but of the person, signifying a relation of origin."
  },
  {
    "index": "33.2",
    "refashioned": "'Father' is the proper name of the first person. Not 'generator' or 'begetter,' but 'Father.' Why? Because 'Father' names the relation rather than the act. Generation is an act that arrives at a terminus; fatherhood is the permanent relation that constitutes the person. The name of a person should point to what constitutes the person, and that is the subsisting relation -- paternity.\n\nYes, 'father' is used more broadly in Scripture (we call God 'Father' of creation, and of adopted children). But the primary and proper sense of 'Father' as applied to God is the personal relation to the Son -- the relation of origin within the Trinity."
  },
  {
    "index": "33.3a",
    "refashioned": "Is 'Father' said of God personally (as a Trinitarian title) before it is said essentially (as Creator and Lord of all)?\n\nSome things have the same name applied to them for independent reasons. But when one application depends on the other, priority belongs to the one that is independent. The Father's paternity in relation to the Son does not depend on God's fatherhood of creatures; but God's fatherhood of creatures (by creation or adoption) is modeled on, and named after, the eternal generation of the Son.\n\nSo 'Father' as a personal name of the first person of the Trinity is prior in meaning to 'Father' as an essential name for God's relationship to creatures."
  },
  {
    "index": "33.3b",
    "refashioned": "Among creatures, generation in the common sense could theoretically be prior to generation in the strict sense. But in God there is no common generation; there is only the unique intellectual generation of the Word. Since the Word's generation is the prototype from which all other 'fatherhood' language derives, the personal sense of 'Father' is absolutely prior.\n\nPaul makes this explicit: 'From whom all fatherhood in heaven and earth is named' (Ephesians 3:15). Creaturely fatherhood is a shadow of the divine original, not the other way around."
  },
  {
    "index": "33.4a",
    "refashioned": "Does it belong to the Father alone to be unbegotten?\n\nYes. 'Unbegotten' can be taken in a privative sense (not begotten, but of a nature that could be) or in a negative sense (simply not begotten). In the negative sense, it applies to the Father and the Holy Spirit, since neither is begotten. But in the strict sense that theologians intend -- as a personal property that distinguishes the Father from the other persons -- 'unbegotten' means 'not from another by way of generation, where generation is relevant to one's nature.' Since the Holy Spirit proceeds by way of love (spiration), not by generation, unbegottenness as a distinguishing mark singles out the Father alone.\n\nInnascibility -- the property of being from no one at all -- captures something more than merely 'not begotten.' It captures the Father's unique position as the one divine person who has no origin whatsoever."
  },
  {
    "index": "33.4b",
    "refashioned": "Unbegottenness is not the same as common spiration (the Father's role as co-source of the Holy Spirit with the Son). The Father has both, but they differ conceptually. Innascibility (being from no one) is a notion of the Father alone, while common spiration is shared with the Son.\n\nInnascibility is technically not a relation, since it does not point to another term. It is more like a negation: 'not from another.' But it functions as a notion because it identifies the Father by capturing something distinctive about His position in the Trinity."
  },

  # ========== Q34: The Person of the Son ==========
  {
    "index": "34.0",
    "refashioned": "We now consider the Son, who is also called the Word. Three questions: (1) Is 'Word' said of God in a personal sense? (2) Is it the proper name of the Son? (3) Does the name 'Word' imply relation to creatures?"
  },
  {
    "index": "34.1a",
    "refashioned": "Is 'Word' a personal name in God -- that is, does it name a distinct person, not just an attribute of the essence?\n\nThe word 'Word' (Logos) can mean three things: the spoken word, the internal concept, and the thing conceived. The spoken word is merely a sign. The thing conceived is what the word represents, not the word itself. The internal concept -- the intelligible form proceeding from the mind's act of understanding -- is what 'word' most properly means.\n\nIn God, 'Word' taken in its proper sense signifies something that proceeds from another: the concept proceeds from the one conceiving. This is a personal name, because what proceeds in God by intellectual emanation is a person. It refers to the Son."
  },
  {
    "index": "34.1b",
    "refashioned": "Origen held that 'Word' signifies not the Son's person but the Father's communicative activity -- making the Son known, as a spoken word makes a thought known. But this is inadequate. A spoken word is secondary; the inner word is primary. And the inner word in God is not a quality or an activity but a subsistent person.\n\nThe key distinction: the word that exists within the mind is not a tool for expression; it is the very act of intelligence taking form. In God, this inner Word is the Son."
  },
  {
    "index": "34.2a",
    "refashioned": "Is 'Word' the proper name of the Son specifically, or could it apply to other persons?\n\n'Word' implies two things: procession by an act of intellect, and a representational relation to what is known. In God, only the Son proceeds by way of intellectual emanation. The Holy Spirit proceeds by way of love, which does not proceed as a likeness of its object but as an impulse toward it. So 'Word' is proper to the Son.\n\nThis does not reduce the Son to mere knowledge. The Word in God is 'knowledge with love,' as Augustine puts it -- a living word that breathes forth love. But the mode of procession is intellectual, and that is what the name 'Word' captures."
  },
  {
    "index": "34.2b",
    "refashioned": "Anselm defined a word as a 'likeness of the thing thought.' The Holy Spirit, though sharing the divine nature fully, does not proceed as a likeness in the same way. Love does not proceed by assimilation but by attraction and impulse. So while the Spirit is fully God, the name 'Word' does not belong to Him.\n\nThe Son, as Word, expresses everything the Father knows -- which is everything, including Himself, all creatures, and the Holy Spirit. The Word is not limited to self-knowledge but is the comprehensive expression of the Father's infinite understanding."
  },
  {
    "index": "34.3",
    "refashioned": "Does the name 'Word' imply any relation to creatures?\n\nYes, but indirectly. The Word primarily expresses the Father -- as a concept primarily represents what the mind understands. But the Father, in knowing Himself, knows all things (since all things preexist in Him as their cause). So the Word, in expressing the Father, also expresses all creatures.\n\nThe Word's relation to creatures is not one of production (the Word does not 'make' creatures by being spoken) but of representation: the Word contains the knowledge of all things that the Father can make. Whether those creatures actually exist or not, the Word expresses them. This is why Scripture says 'all things were made through Him' -- through the Word, the Father's creative knowledge is articulated."
  },

  # ========== Q35: Of the Image ==========
  {
    "index": "35.0",
    "refashioned": "Is the Son an 'Image'? Two questions: (1) Is 'Image' said personally in God? (2) Is it proper to the Son?"
  },
  {
    "index": "35.1",
    "refashioned": "'Image' is a personal name in God, properly belonging to the Son.\n\nAn image requires two things: it must proceed from another, and it must be a likeness of that other in the same specific nature (or at least in the form that characterizes the species). A photograph of a man is not an image in this strict sense -- it reproduces the external appearance but not the nature. A son born of a father is an image in the strict sense: same human nature, proceeding from the father.\n\nThe Son proceeds from the Father by generation, and in proceeding receives the same divine nature. So the Son is the Image of the Father -- not in the loose sense of resemblance, but in the strict sense of a likeness that proceeds from its exemplar in identity of nature."
  },
  {
    "index": "35.2",
    "refashioned": "Is 'Image' proper to the Son, or does it also apply to the Holy Spirit?\n\nThe Holy Spirit is like the Father (sharing the same divine nature), but the concept of 'image' requires proceeding as a likeness. The Son proceeds by way of the intellect -- an intellectual word is precisely a likeness of the object understood. The Holy Spirit proceeds by way of love, which is not a likeness of its object but an impulse toward it.\n\nSo 'Image' belongs to the Son alone. The Holy Spirit is 'like' the Father in nature but does not proceed as a likeness. When creatures are called 'images of God,' they bear the image imperfectly and by participation; the Son alone is the perfect Image, identical in nature with the Father."
  },

  # ========== Q36: The Person of the Holy Ghost ==========
  {
    "index": "36.0",
    "refashioned": "We turn to the Holy Spirit, who is also called Love and Gift. Four questions about the name 'Holy Spirit': (1) Is this a proper personal name? (2) Does the Holy Spirit proceed from both the Father and the Son? (3) Does He proceed from the Father through the Son? (4) Are the Father and Son one principle of the Holy Spirit?"
  },
  {
    "index": "36.1a",
    "refashioned": "Is 'Holy Spirit' a proper name for one divine person, or a general term for divinity?\n\nBoth 'holy' and 'spirit' can be applied to God generally. The Father is holy; the Son is spirit. But when joined together as a compound name, 'Holy Spirit' functions as the proper designation of the third person. This is because the third person, who proceeds as Love, has no naturally fitting proper name the way 'Father' and 'Son' do. (Love's procession, unlike generation, has no ready-made vocabulary in any language.) So the name 'Holy Spirit,' which by its components suggests both immateriality (spirit) and the sanctifying impulse (holiness), was appropriated by usage to designate the third person specifically."
  },
  {
    "index": "36.1b",
    "refashioned": "When Scripture says 'the Spirit of the Lord is upon me,' it sometimes refers to the Father, sometimes to the Son, and sometimes to the Holy Spirit specifically. Context determines meaning. But the compound proper name 'the Holy Spirit' designates the third person.\n\nThe name also captures something about the Holy Spirit's nature: both Father and Son 'spirate' (breathe forth) the Spirit, and what is breathed in common can be named by what is common to both -- holiness and spirituality."
  },
  {
    "index": "36.2a",
    "refashioned": "Does the Holy Spirit proceed from the Son as well as from the Father?\n\nYes. This is the key point of difference between Western and Eastern Trinitarian theology, but the Western position is well-grounded.\n\nThe argument is structural. If the Holy Spirit did not proceed from the Son, there would be no relative opposition between them, and therefore no real distinction. Wherever there is no relative opposition in God, there is identity. Without proceeding from the Son, the Spirit's relation to the Son would not be one of opposition (origin vs. originated) but merely one of... nothing distinguishing. The Spirit and the Son would be the same person. Since they are not the same person, the Spirit must proceed from the Son."
  },
  {
    "index": "36.2b",
    "refashioned": "The order of the processions confirms this. The procession of love follows from the procession of the word: you cannot love what you have not first known. So just as all love proceeds from a concept, the Holy Spirit (who proceeds as Love) proceeds from the Son (who is the Word). The Son's generation logically precedes the Spirit's procession, and this precedence is not merely logical but constitutive: the Son is, together with the Father, the principle from which the Spirit proceeds."
  },
  {
    "index": "36.2c",
    "refashioned": "Some Eastern fathers seem to deny that the Spirit proceeds from the Son. But careful reading shows they denied only that the Spirit proceeds from the Son as from a first or independent principle. The Father is the unoriginate source; the Son's role as co-spirator derives from the Father. Greek theology and Latin theology converge on the substance of the claim even when the emphasis differs.\n\nScripture supports the double procession: Jesus says 'He will receive of mine' (John 16:14), and the Spirit is called 'the Spirit of the Son' (Galatians 4:6). These would be meaningless if there were no relation of origin between the Son and the Spirit."
  },
  {
    "index": "36.3a",
    "refashioned": "Does the Holy Spirit proceed from the Father 'through' the Son?\n\nYes. The Father is the first principle who begets the Son; the Son, having received everything from the Father (including the power of spiration), joins with the Father in spirating the Holy Spirit. 'Through the Son' does not mean the Son is a mere instrument or intermediate channel. It means the Father's spirative power flows to the Spirit through the Son because the Son possesses that same power by generation from the Father."
  },
  {
    "index": "36.3b",
    "refashioned": "The preposition 'through' does not imply that the Son is a secondary or subordinate cause. In the Trinity, 'through' expresses order of origin: the Father's authority as first principle is communicated to the Son, and both together are one principle of the Spirit. The Son spirates because the Father gave Him everything, including the power to spirate. So 'from the Father through the Son' is fully compatible with 'from the Father and the Son,' and Eastern and Western formulations express the same reality from different angles."
  },
  {
    "index": "36.4a",
    "refashioned": "Are the Father and Son one principle of the Holy Spirit, or two?\n\nOne principle. The act of spirating the Holy Spirit belongs to the Father and Son not by virtue of their personal properties (which distinguish them) but by virtue of the one divine nature they share. The spirative power is one; the act of spiration is one. What is one in principle constitutes one principle.\n\nThis is why we say 'the Father and the Son spirate the Holy Spirit' (plural subject, singular action), not 'the Father spirates and the Son spirates' as though these were two separate acts."
  },
  {
    "index": "36.4b",
    "refashioned": "If someone objects that two persons acting together are two principles, the answer is that principlehood here depends not on the persons as such but on the common power. In creatures, two humans pulling a rope are two agents because each has their own separate strength. But the Father and Son share numerically one spirative power. So they are one principle, not two.\n\nThis is analogous to how 'the three persons create' constitutes one creative principle, not three, because the creative power is the one divine essence."
  },
  {
    "index": "36.4c",
    "refashioned": "We do not say 'the Father and Son are one Spirator' (using a noun) but 'they are one spirating' (using an adjective), because the adjectival form attaches to the form -- the shared power -- while the noun form could suggest a single personal identity. The Father and Son are distinct persons who exercise one shared act. The language must reflect both the personal distinction and the unity of action."
  },

  # ========== Q37: The Name of the Holy Ghost -- Love ==========
  {
    "index": "37.0",
    "refashioned": "The Holy Spirit is also called Love. Two questions: (1) Is 'Love' a proper name of the Holy Spirit? (2) Do the Father and Son love each other by the Holy Spirit?"
  },
  {
    "index": "37.1a",
    "refashioned": "Is 'Love' a proper personal name of the Holy Spirit, or does it refer to the divine essence in general?\n\nLove in God can be taken essentially (as an attribute of the divine nature -- God is love) or personally (as designating the person who proceeds by way of love). The Holy Spirit proceeds as love: the will's impulse toward the good, flowing from the intellectual conception of that good.\n\nJust as 'Word' captures the mode of the Son's procession (intellectual emanation), 'Love' captures the mode of the Spirit's procession (volitional impulse). Taken personally, Love is the proper name of the Holy Spirit. Taken essentially, it applies to the whole Trinity."
  },
  {
    "index": "37.1b",
    "refashioned": "The key to understanding this is Augustine's distinction. Essential love is the act of willing that belongs to God's nature. Personal Love is the person who proceeds by that act. They are not two different loves; the personal Love proceeds from the essential act of loving, just as the personal Word proceeds from the essential act of understanding.\n\nSo when Scripture says 'God is love,' it speaks of the essence. When it says 'the love of God is poured into our hearts by the Holy Spirit,' it points to the person."
  },
  {
    "index": "37.1c",
    "refashioned": "Love, as a personal name, captures something distinctive about how the third person proceeds. The Son proceeds as a likeness (word, image); the Holy Spirit proceeds as an impulse or inclination (love, gift). This is not to say the Spirit lacks likeness to the Father -- He shares the same nature -- but that His mode of proceeding is characterized by the movement of the will toward the good, not by the representation of the known."
  },
  {
    "index": "37.2a",
    "refashioned": "Do the Father and Son love each other 'by' the Holy Spirit?\n\nThis question is tricky. If it means the Holy Spirit is the formal cause or essential principle by which the Father and Son love, the answer is no. The act of love belongs to the divine essence and is common to all three persons. The Father does not need the Holy Spirit in order to love.\n\nBut if it means the Father and Son express or manifest their mutual love in the breathing forth of the Holy Spirit, the answer is yes. The Holy Spirit proceeds as the Love between Father and Son -- not as an instrument they use to love, but as the subsistent expression of the love they share."
  },
  {
    "index": "37.2b",
    "refashioned": "When we say 'the Father loves the Son by the Holy Spirit,' the 'by' does not indicate efficient or formal causality. It indicates a relationship of origin: the Holy Spirit is the Love that proceeds from the Father's love for the Son. The Father loves essentially (by His nature), and the Holy Spirit is the personal term of that essential love -- the subsistent Love breathed forth.\n\nSo the sentence is true if read as: 'The Father, loving the Son, spirates the Holy Spirit who is Love.' It is false if read as: 'The Father could not love the Son without the Holy Spirit as His means of loving.'"
  },
  {
    "index": "37.2c",
    "refashioned": "This also applies to the Father's love of Himself and of creatures. The Father loves Himself and all things by the essential love that is His nature. But the Holy Spirit proceeds as the expression of that love. We can say the Father and Son love each other and love us 'by' the Holy Spirit in the sense that the Spirit is the proceeding Love that flows from their mutual love and extends to creation."
  },

  # ========== Q38: The Name of the Holy Ghost -- Gift ==========
  {
    "index": "38.0",
    "refashioned": "The Holy Spirit is also called 'Gift.' Two questions: (1) Can 'Gift' be a personal name? (2) Is it proper to the Holy Spirit?"
  },
  {
    "index": "38.1a",
    "refashioned": "A gift, by definition, is something given freely -- not in exchange, not owed, but out of sheer generosity. The root of free giving is love: we give to someone because we wish them well. So love is the first gift, the gift that makes all other gifts possible.\n\nThe Holy Spirit proceeds as Love. Therefore the Holy Spirit proceeds as the first Gift. 'Gift' can be a personal name because it signifies a person who proceeds in the manner of love and is thereby the originating gift through which all other gifts flow."
  },
  {
    "index": "38.1b",
    "refashioned": "The Gift exists as giveable from eternity -- the Holy Spirit is eternally related to the persons as one who can be given -- but is actually given in time when God bestows grace on creatures. The distinction between being a gift (the eternal aptitude) and being given (the temporal act) matters: the Holy Spirit is eternally Gift, but is given to creatures at specific moments in the economy of salvation.\n\nGift does not imply subordination. A gift proceeds from the giver and is distinct from the giver, but in God this procession carries no diminishment. The Holy Spirit is given freely, and in being given, bestows the fullness of divine love."
  },
  {
    "index": "38.2",
    "refashioned": "'Gift' is the proper name of the Holy Spirit.\n\nThe reasoning follows the same pattern as 'Love.' A gift in the fullest sense is an unreturnable, gratuitous giving. The reason for giving freely is love. The Holy Spirit proceeds as Love. Therefore the Holy Spirit proceeds as the first Gift -- the one through which all particular gifts are distributed.\n\nAugustine puts it clearly: 'As being born is, for the Son, to be from the Father, so for the Holy Spirit, to be the Gift of God is to proceed from Father and Son.' The Spirit's personal identity is constituted by proceeding as Love, and 'Gift' names the same reality from the side of its communicability to creatures."
  },

  # ========== Q39: Persons in Relation to the Essence ==========
  {
    "index": "39.0",
    "refashioned": "How do the persons relate to the divine essence? Eight questions: (1) Is the essence identical with the person? (2) Should we say the three persons are 'of one essence'? (3) Should essential names be singular or plural? (4-5) Can notional terms be predicated of essential names? (6) Can personal names be predicated of essential names? (7) Can essential attributes be appropriated to particular persons? (8) Which attributes belong to which person?"
  },
  {
    "index": "39.1",
    "refashioned": "In God, the essence is really identical with each person. The divine essence is the divine existence itself, and each person is that same existence subsisting in a particular relational mode. The Father is not 'composed of' essence plus paternity, as if these were separable components. The essence is paternity in the Father and filiation in the Son.\n\nBut while the essence is identical with each person in reality, they differ in how we conceive them. 'Essence' signifies the common nature in the mode of a form. 'Person' signifies the distinct subsistence. We can say 'the essence is the Father,' but we cannot say 'the essence generates' (because generating is a personal act, not an essential one). The real identity with the conceptual distinction is what makes Trinitarian language work."
  },
  {
    "index": "39.2a",
    "refashioned": "Should we say the three persons are 'of one essence'?\n\nYes, but the preposition matters. We say the three persons are of one essence (de una essentia) or from one essence (ex una essentia) to indicate that they share a common nature. We do not say 'one essence of three persons' in a way that would make the essence merely collective.\n\nThe Council of Constantinople condemned saying the Son is 'from a different substance' than the Father. The proper formulas -- 'consubstantial,' 'of one essence' -- express the identity of nature among the persons."
  },
  {
    "index": "39.2b",
    "refashioned": "The prepositions 'of' and 'from' do not imply that the essence is prior to or separate from the persons -- as if the persons were carved out of a pre-existing block of divinity. They signify that the essence is the common form in which each person subsists. We avoid saying the essence 'begets' or 'is begotten,' because these are personal acts. The essence is what the persons share; the relations are what distinguish them."
  },
  {
    "index": "39.3a",
    "refashioned": "Should essential names be predicated of the persons in the singular or the plural? 'God,' 'wise,' 'good' -- do we say the Father is God and the Son is God (two statements, one God each) or the Father and Son are Gods?\n\nEssential names are always singular. We say 'the Father is God, the Son is God, the Holy Spirit is God' -- and 'these three are one God,' never 'three Gods.' This is because the form signified by 'God' is one -- the divine essence. Multiple subjects sharing one form take the singular: three men who share one culture can be called 'one culture group,' and three persons sharing one divinity are one God."
  },
  {
    "index": "39.3b",
    "refashioned": "Personal names, by contrast, are properly plural. We say 'three persons,' not 'one person who is Father, Son, and Spirit.' The form signified by personal names -- the subsisting relation -- is really distinct in each person. Where the form is one, the name is singular; where the forms are really distinct, the name is plural.\n\nSo 'God' is singular because the essence is one. 'Person' is plural because the relations are really distinct."
  },
  {
    "index": "39.4a",
    "refashioned": "Can we say 'God begets God'? Can notional (personal) terms be predicated of essential names taken concretely?\n\nYes. 'God begets God' is true: the Father (who is God) begets the Son (who is God). The concrete term 'God' stands for a suppositum -- a concrete individual -- and the Father is that individual. When we say 'God begets,' we mean 'the person who is God, the Father, begets.'\n\nBut we cannot say 'the essence begets,' because the abstract term 'essence' does not stand for a suppositum but for a form. And forms do not perform personal acts. The concrete name 'God' and the abstract name 'essence' differ in their mode of signification even though they refer to the same reality."
  },
  {
    "index": "39.4b",
    "refashioned": "The rule is: concrete essential names (God, the Almighty) can serve as subjects or predicates of notional propositions, because they stand for the persons. Abstract essential names (the essence, the divinity, wisdom) cannot, because they signify the common form and do not stand for any particular person. So 'God begets God' is fine, but 'the divine essence begets the divine essence' is not. The first is a statement about persons; the second would absurdly make the essence act as an agent."
  },
  {
    "index": "39.5a",
    "refashioned": "Can notional terms be predicated of essential names taken in the abstract? Can we say 'the essence is the Father'?\n\nYes, by virtue of real identity. The divine essence is really identical with the person of the Father. So 'the essence is the Father' is true in the sense of 'the reality that is the essence is the same reality that is the Father.' But it does not follow that the essence generates or is generated, because those are acts, and the essence as such does not act -- persons act."
  },
  {
    "index": "39.5b",
    "refashioned": "The identity statements ('the essence is the Father,' 'paternity is the essence') are true because in God there is no real distinction between essence and relation. But this identity does not license interchanging predicates freely. What is true of the essence under the formality of essence cannot be transferred to the person under the formality of person, and vice versa. 'The essence is common to the three persons' does not entail 'the Father is common to the three persons.'"
  },
  {
    "index": "39.6",
    "refashioned": "Can the persons be predicated of the essential names? Can we say 'God is three persons' or 'God is the Trinity'?\n\nYes. The concrete term 'God' stands for the three persons (since each person is God), so 'God is the three persons' and 'God is the Trinity' are both true. What cannot be said is that the essence is three persons, because the abstract term 'essence' signifies the form, and the form is one, not three."
  },
  {
    "index": "39.7",
    "refashioned": "Can essential attributes be 'appropriated' to particular persons -- that is, can we assign power to the Father, wisdom to the Son, and goodness to the Holy Spirit, even though all three share all essential attributes equally?\n\nYes. Appropriation does not mean exclusive possession. It means using common attributes to illuminate personal properties. Power is appropriated to the Father because He is the unoriginate principle; wisdom to the Son because He proceeds as the Word (an intellectual emanation); goodness to the Holy Spirit because He proceeds as Love (and love's object is the good).\n\nAppropriation helps us understand the persons by analogy. It does not divide the essence."
  },
  {
    "index": "39.8a",
    "refashioned": "Which attributes are appropriated to which person?\n\nAugustine appropriated differently depending on context. To the Father: eternity, unity, and power. To the Son: beauty (or species), truth, and wisdom. To the Holy Spirit: goodness, joy (or use), and love.\n\nThe logic: The Father, as unoriginate principle, is fittingly associated with eternity (no beginning), unity (the source from which distinction arises), and power (the principle of action). The Son, proceeding as Word, is associated with beauty (the splendor of intelligible form), truth (the correspondence between concept and reality), and wisdom (knowledge in its fullness). The Holy Spirit, proceeding as Love, is associated with goodness (the object of love), joy (the rest of love in its object), and love itself."
  },
  {
    "index": "39.8b",
    "refashioned": "Hilary offers a slightly different appropriation: eternity in the Father, beauty in the Image (the Son), and enjoyment in the Gift (the Holy Spirit). These map to the same logic from a different angle.\n\nThe point of appropriation is pedagogical. We cannot directly see the personal distinctions in God; they are known only by revelation. But by connecting essential attributes we can grasp (power, wisdom, love) to particular persons, we build conceptual bridges to the invisible relations. The bridges are real correspondences, not arbitrary assignments -- power really does resonate with the notion of an unoriginate principle, wisdom with an intellectual procession, love with a volitional one."
  },

  # ========== Q40: Persons as Compared to Relations or Properties ==========
  {
    "index": "40.0",
    "refashioned": "How do the persons relate to their properties? Four questions: (1) Are relation and person the same? (2) Are the persons distinguished by relations? (3) Do the relations remain if we mentally abstract them from the persons? (4) Do relations presuppose the personal acts, or vice versa?"
  },
  {
    "index": "40.1a",
    "refashioned": "In God, each person is identical with the relation that constitutes it. The Father is paternity; the Son is filiation; the Holy Spirit is procession. This follows from divine simplicity: there can be no real composition in God, so the person cannot be one thing and the relation another.\n\nBut we need to distinguish personal relations (which constitute persons) from other notions. Innascibility is a notion of the Father but does not constitute Him as a person -- it merely negates origin. Common spiration belongs to both Father and Son and so cannot constitute either one individually. Only the three 'personal properties' -- paternity, filiation, and procession -- are subsisting relations that are the persons."
  },
  {
    "index": "40.1b",
    "refashioned": "Some thinkers held that the persons are constituted not by relations but by their origins (the acts of generating and spirating). On this view, paternity is something the Father 'has' rather than something the Father 'is.' But this creates a problem: if the person exists before the relation, then the person is constituted by something absolute, and the distinction between persons would be absolute rather than relational. That leads either to a plurality of essences (Arianism) or to no real distinction at all.\n\nThe better view: the person and the relation are identical in reality, though we conceive them under different aspects. When we say 'the Father,' we think of the person. When we say 'paternity,' we think of the constitutive relation. Same reality, different conceptual angles."
  },
  {
    "index": "40.2a",
    "refashioned": "Are the persons distinguished by relations of origin?\n\nYes, and only by relations of origin. In God there is no matter, no accidents, no composition of any kind. The only distinction available is relational -- specifically, the opposition between 'origin' and 'originated.' Paternity and filiation are opposed as principle and what proceeds from the principle. This relative opposition is what makes the Father and Son genuinely two persons sharing one essence."
  },
  {
    "index": "40.2b",
    "refashioned": "The distinction between persons cannot come from absolute properties (like wisdom or goodness), because these belong to the one essence and are shared equally. Nor can it come from anything extrinsic. It can only come from relations, and specifically from relations that involve opposition. Non-opposed relations (like common spiration, which is shared by Father and Son) do not distinguish the persons who share them.\n\nSo the entire Trinitarian structure stands on relational opposition: who originates from whom."
  },
  {
    "index": "40.3a",
    "refashioned": "If we mentally strip away the personal relations, is there anything left of the persons?\n\nIf we abstract the relations entirely, nothing remains but the undifferentiated divine essence. There is no 'bare person' underneath the relation. The relation is what makes the person a distinct person.\n\nBut if we abstract the relations only from their role as relations (their reference to another) while retaining their role as constitutive principles, then we can still conceive the persons as distinct hypostases -- we just lose the explicit referential aspect."
  },
  {
    "index": "40.3b",
    "refashioned": "The distinction of persons depends entirely on the relations. Remove the relations, and you remove the persons -- what remains is simply the one divine essence. This confirms that persons in God are constituted by subsisting relations and nothing else."
  },
  {
    "index": "40.3c",
    "refashioned": "Some objected that if the hypostases depend on relations, then divine hypostases are not 'absolute' the way created hypostases are. The answer is that in creatures, hypostases are distinguished by matter or individual features. In God, they are distinguished by relations. This does not make the divine hypostases less real -- it makes them differently constituted, as befits a nature that is absolutely simple."
  },
  {
    "index": "40.4",
    "refashioned": "Which comes first in our understanding: the personal acts (generating, spirating) or the personal properties (paternity, spiration)?\n\nLogically, the relation-as-constituting-the-person is prior to the notional act. The Father must be the Father before He can generate, since generation is an act of a person, and the person is constituted by paternity. But paternity as a relation-referring-to-the-Son is logically posterior to generation, since the reference to the Son presupposes the Son's existence, which comes from the act of generation.\n\nSo there is a logical order: (1) the Father is constituted as Father by paternity considered as a form, (2) the Father generates, (3) the Son comes to be, (4) and paternity and filiation refer to each other as correlatives. In reality, all of this is one eternal, simple act -- the ordering is purely in how we understand it."
  },

  # ========== Q41: Persons in Reference to the Notional Acts ==========
  {
    "index": "41.0",
    "refashioned": "We now consider the persons in relation to the notional acts (generating, being generated, spirating, being spirated). Six questions: (1) Should notional acts be attributed to persons? (2) Are these acts necessary or voluntary? (3) Does a person proceed from nothing or from something? (4) Is there a power in God corresponding to these acts? (5) What does that power mean? (6) Can one notional act terminate in more than one person?"
  },
  {
    "index": "41.1",
    "refashioned": "Notional acts should be attributed to the persons. Wherever real distinction exists, we can identify what distinguishes. The divine persons are distinguished by relations of origin, and origin implies acts -- the Father generates, the Son is generated, Father and Son together spirate, the Holy Spirit is spirated. These are the notional acts.\n\nThe objection that every action in God reduces to the essence misses the point. Notional acts are not actions like creating (which is essential and common to all three persons). They are the internal acts by which the persons originate from one another. They do not add anything to the substance but express the relational distinctions that are the persons themselves."
  },
  {
    "index": "41.2a",
    "refashioned": "Are the notional acts necessary or voluntary? In other words, does the Father generate the Son by choice, or by nature?\n\nBy nature -- not by an act of will that could have gone otherwise. If generation depended on the Father's free choice, the Son's existence would be contingent, and the Son would be a creature. But the Son shares the Father's nature fully and necessarily.\n\nThis does not mean the Father generates unwillingly. The will accompanies generation in the sense that the Father wills what He does by nature. But the will is not the principle of generation. Nature is. Just as God's self-knowledge is natural (not chosen), so the Word's procession from that self-knowledge is natural."
  },
  {
    "index": "41.2b",
    "refashioned": "What about the Holy Spirit -- does He proceed by will? Yes, in the sense that the Holy Spirit proceeds as Love, and love belongs to the will. But this does not make the procession voluntary in the sense of optional. The will here operates naturally (as nature inclines it), not freely (as deliberation directs it). Just as we naturally will our own happiness without choosing to, the Father and Son naturally spirate the Holy Spirit through their essential love.\n\nThe distinction between 'natural will' and 'free will' is critical. The Spirit's procession is from the will acting naturally. It is not contingent and could not have failed to occur."
  },
  {
    "index": "41.3a",
    "refashioned": "Does a divine person proceed from nothing, or from something?\n\nFrom something -- specifically, from the divine substance. The Son is 'from the substance of the Father,' meaning He receives the same divine nature by generation. He is not made from nothing (that would make Him a creature) nor from pre-existing matter (there is no matter in God).\n\nThe 'from' here indicates consubstantiality, not causation in the creaturely sense. The Son is from the Father's substance the way light is from the sun -- same nature, no diminishment, no separation."
  },
  {
    "index": "41.3b",
    "refashioned": "When we say the Son is begotten 'of the substance of the Father,' we mean the divine substance is communicated from Father to Son in generation. We do not mean a portion is detached or a new substance is created. The entire divine substance, undivided, is shared.\n\nThis is why the creed says 'God from God, Light from Light.' The preposition indicates origin of person, not division of essence."
  },
  {
    "index": "41.3c",
    "refashioned": "The same applies to the Holy Spirit. He proceeds from the substance of the Father and the Son. Though we do not say He is 'begotten from' their substance (since His procession is not generation), He does receive the same divine nature through spiration. Every divine procession is a communication of the one undivided substance."
  },
  {
    "index": "41.4",
    "refashioned": "Is there a power in God with respect to the notional acts? Can we say the Father has the 'power to generate'?\n\nYes. Power simply means the principle of an act. Since the Father really does generate, there must be in Him a principle of generation -- and that is what we mean by power. This power is not an added attribute but the divine essence itself, as it is the principle of the notional act.\n\nThe power to generate is the divine nature as possessed by the Father in the mode of paternity. It is the same essence that is the power of the Son to be generated and the power of Father and Son to spirate."
  },
  {
    "index": "41.5a",
    "refashioned": "What exactly does the 'power to generate' signify? Does it signify the relation (paternity), the essence, or both?\n\nPower signifies a principle of action. In God, the principle of generation is the divine nature as possessed by the Father. So the power to generate signifies the divine essence directly (as the root of the act) and the relation indirectly (as the mode in which the essence is possessed by the one who generates).\n\nWe cannot say the power to generate is paternity itself, because paternity is a relation, and a relation is not a principle of action in the strict sense. But we can say it is the divine nature as exercised by the Father."
  },
  {
    "index": "41.5b",
    "refashioned": "The Father and the Son have the same power (the same divine nature), but in different relational modes. The Father has the power as 'giving' -- He can generate. The Son has the same power as 'receiving' -- He is generated. This is why the Son cannot Himself generate a further Son: not because He lacks power, but because the same power exists in Him in the mode of filiation, not paternity."
  },
  {
    "index": "41.6",
    "refashioned": "Can one notional act terminate in more than one person? Can the Father beget two Sons?\n\nNo. There is only one perfect act of divine generation, producing one perfect Word. The reason goes back to the simplicity of God's understanding: God understands all things by one act. Since the Word proceeds from this one act, there can be only one Word. If there were two sons, either the Father's intellectual act would be divided (impossible) or one of the sons would be redundant.\n\nSimilarly, there is only one procession of Love, producing one Holy Spirit. The perfection and simplicity of God's willing means there cannot be multiple proceeding Loves."
  },

  # ========== Q42: Equality and Likeness Among the Divine Persons ==========
  {
    "index": "42.0",
    "refashioned": "We now compare the persons to one another in equality and likeness. Six questions: (1) Is there equality among the divine persons? (2) Is the person proceeding co-eternal with the principle? (3) Is there an order of nature? (4) Is the Son equal to the Father in greatness? (5) Is the Son in the Father and the Father in the Son? (6) Is the Son equal to the Father in power?"
  },
  {
    "index": "42.1a",
    "refashioned": "The divine persons are equal to one another. Equality means the negation of greater or less. If the persons were unequal, they would differ in their 'quantity' -- and quantity in God means nothing but the perfection of the divine nature. Unequal persons would have different natures, and three persons with different natures would not be one God.\n\nSince the three persons share one and the same divine nature in its full perfection, none exceeds or falls short of another. They are equal."
  },
  {
    "index": "42.1b",
    "refashioned": "The relevant kind of equality is not about physical size (God has no body) but about 'virtual quantity' -- the perfection and power of a nature. This is measured by the form itself: in spiritual beings, 'greater' means 'more perfect.' Since the divine nature is infinitely perfect and is entirely shared by each person, none is greater or lesser.\n\nEquality goes beyond mere likeness. Things can be alike while participating in a form to different degrees (a lukewarm and a hot thing are both warm, hence alike, but not equal in warmth). The divine persons do not merely share the divine nature to varying degrees -- they possess it identically and fully. So they are not only like but equal."
  },
  {
    "index": "42.2a",
    "refashioned": "Is the Son co-eternal with the Father? Arius listed twelve models of generation, each of which implied that what is generated is later than, or less than, its source. His conclusion: the Son came after the Father.\n\nBut every model Arius cited was drawn from imperfect, creaturely generation -- material change, temporal succession, inequality. None applies to God."
  },
  {
    "index": "42.2b",
    "refashioned": "The Son is co-eternal with the Father. Three factors could make an effect posterior to its principle: the agent's free choice of timing, the agent's initial imperfection (needing time to mature), or the successive character of the action. None applies to divine generation.\n\nThe Father generates by nature, not by free choice, so there is no chosen delay. The Father's nature was always perfectly actual, so there is no growth toward readiness. And the act of generation is not successive -- it does not unfold in stages through time. It is instantaneous and eternal.\n\nTherefore the Son has existed whenever the Father has existed. The Son is co-eternal with the Father, and so is the Holy Spirit with both."
  },
  {
    "index": "42.2c",
    "refashioned": "No single creaturely analogy perfectly captures divine generation. We must gather insights from many: the coeternal nature of light and its splendor, the impassibility of a word born from the intellect, the consubstantiality implied by the name 'Son.' Of all analogies, the procession of the word from the intellect comes closest, since an intellectual word is not posterior to its source (except in an intellect that transitions from potentiality to act, which does not apply to God).\n\nThe Son is 'ever being born' and 'ever born' -- 'ever' captures eternity's permanence, 'born' captures the perfection of the generation. There was never a time when the Son was not. Arius's 'there was when He was not' is refuted by the eternal completeness of divine generation."
  },
  {
    "index": "42.3",
    "refashioned": "Is there an order of nature among the divine persons?\n\nYes, but it is an order of origin, not of priority. 'Order of nature' here does not mean one person is prior in nature to another, but that one is from another. The Father is the principle of the Son, and the Father and Son are the principle of the Holy Spirit. This establishes an order: not 'before and after,' but 'from whom and toward whom.'\n\nAugustine captures it precisely: 'Not whereby one is prior to another, but whereby one is from another.' The order is real -- it is not invented by our minds -- but it carries no implication of superiority, inferiority, or temporal sequence."
  },
  {
    "index": "42.4a",
    "refashioned": "Is the Son equal to the Father in greatness -- that is, in the perfection of the divine nature?\n\nYes. The very nature of filiation requires it. Paternity and filiation are defined by the fact that the offspring attains the same nature as the parent. In creatures, a child may start imperfect and grow toward equality, or a defect in generation may prevent full equality. But in God there is no potentiality, no growth, no defect. The Son receives the Father's nature fully and perfectly from all eternity.\n\nAs Hilary says: remove bodily weakness, the beginning of conception, the process of growth -- and every son, by natural generation, is the father's equal, because he possesses the same nature."
  },
  {
    "index": "42.4b",
    "refashioned": "When Scripture says 'the Father is greater than I,' it speaks of Christ's human nature, in which He is less than the Father. In His divine nature, He is equal. Athanasius: 'Equal to the Father in His Godhead; less than the Father in humanity.'\n\nThe objection that the Father has paternity and the Son does not -- so the Son lacks something -- confuses substance with relation. Paternity is the Father's dignity, but it is the same essence that, in the Son, is filiation. The same dignity exists in both, under different relational modes. It is like the same road viewed from two directions: the road from Athens to Thebes and from Thebes to Athens is one road, but the journey differs in direction.\n\nAnd though the Father has three notions while the Son has two, notions are not parts that add up. All the persons together are not greater than one, because the whole perfection of the divine nature exists in each."
  },
  {
    "index": "42.5",
    "refashioned": "Are the Son in the Father and the Father in the Son?\n\nYes, in three ways. By essence: the Father communicates His own essence to the Son without change, so the Father's essence is in the Son, and therefore the Father Himself is in the Son. And since the Son is His own essence, He Himself is in the Father. By relation: each correlative implies the other in its very concept -- paternity implies filiation and vice versa, so each is conceptually 'in' the other. By origin: the Word proceeds from the intellect yet remains within the speaker; the Son goes forth from the Father yet remains within Him.\n\nNo creaturely model of 'being in' captures this perfectly. The closest is the way something exists in its originating principle -- except that in creatures, the originated and the origin differ in nature, while in God they do not."
  },
  {
    "index": "42.6",
    "refashioned": "Is the Son equal to the Father in power?\n\nYes. Power follows from the perfection of nature. Since the Son possesses the same nature as the Father in its full perfection, He possesses the same power. Whatever the Father can do, the Son can do 'in like manner' (John 5:19).\n\nBut 'in like manner' does not mean 'in the same relational mode.' The same power that is 'begetting' in the Father is 'being begotten' in the Son. The Son cannot beget a Son -- not because He lacks power, but because the power exists in Him as filiation, not paternity. Generation is a relation, not an absolute capacity. So the Son has the same omnipotence as the Father, but exercised under a different relational aspect.\n\nWhen Scripture says the Son 'cannot do anything of Himself,' it means the Son's power is derived from the Father by origin -- not that it is lesser. The Son acts of Himself (per se) but not from Himself (a se)."
  },

  # ========== Q43: The Mission of the Divine Persons ==========
  {
    "index": "43.0",
    "refashioned": "Finally, the mission of the divine persons -- how the persons are 'sent' into the world. Eight questions: (1) Can a divine person be sent? (2) Is mission eternal or temporal? (3) What is invisible mission? (4) Can the Father be sent? (5) Can the Son be sent invisibly? (6) Is invisible mission to all who have grace? (7) Is the Holy Spirit sent visibly? (8) Can a person send Himself?"
  },
  {
    "index": "43.1",
    "refashioned": "Can a divine person be 'sent'? Sending seems to imply inferiority (the sent is less than the sender), separation (what is sent departs from the sender), and a change of location (arriving somewhere new). None of these applies to God in the ordinary sense.\n\nBut mission in God means two things: a relation of origin (the one sent proceeds from the sender) and a new mode of presence (the one sent begins to exist somewhere in a new way). The Son is sent by the Father into the world not because He was absent before, but because He begins to be present in a new way -- through the Incarnation, or through the gift of grace.\n\nThis mission does not imply inferiority, because divine procession is according to equality of nature. It does not imply separation, because the Son does not cease to exist where He was. It does not imply local movement, because the divine person was already everywhere."
  },
  {
    "index": "43.2",
    "refashioned": "Mission is temporal, not eternal. The terms used for divine origins fall on a spectrum. Some express only the relation to the principle: 'procession,' 'going forth.' Some express the eternal term: 'generation,' 'spiration' -- these are exclusively eternal, because the terminus of the Son's generation is the divine nature, which is eternal. Others express a temporal term: 'mission' and 'giving' -- because to be sent or given implies a new mode of existence in a creature, and that is temporal.\n\nSo 'the Son proceeds from the Father' can be eternal. 'The Son is sent by the Father' is always temporal -- it refers to the visible mission of the Incarnation or the invisible mission of grace. Mission includes the eternal procession but adds a temporal effect."
  },
  {
    "index": "43.3a",
    "refashioned": "The invisible mission of a divine person occurs through the gift of sanctifying grace.\n\nGod is present in all things by essence, power, and presence -- as the cause is present in every effect that participates in its goodness. But beyond this universal mode, there is a special presence in rational creatures who, by knowledge and love, actually attain to God Himself. When a person knows and loves God in the way that sanctifying grace makes possible, God is not merely the sustaining cause of their being but the object of their direct experience.\n\nThis special indwelling -- God present as the known is in the knower and the beloved in the lover -- occurs only through sanctifying grace. The divine person is 'sent' in the sense of beginning to dwell in someone in this new, intimate way."
  },
  {
    "index": "43.3b",
    "refashioned": "The divine person Himself is given, not merely His effects. Sanctifying grace enables the rational creature to possess and enjoy the divine person directly. The Spirit is not a distant cause whose gifts arrive like packages from afar; the Spirit Himself dwells in the soul through the gift of grace.\n\nThe gifts of grace (prophecy, miracles, tongues) manifest the Spirit's presence but are not the basis of the invisible mission. Only sanctifying grace constitutes the new mode of divine indwelling that we call 'being sent.'"
  },
  {
    "index": "43.4",
    "refashioned": "Can the Father be sent? No. Mission requires procession from another, and the Father proceeds from no one. He is the unoriginate source. The Son can be sent (He proceeds from the Father). The Holy Spirit can be sent (He proceeds from both). The Father dwells in us by grace just as the Son and Spirit do, but He is not described as 'sent,' because there is no one from whom He comes.\n\nThe Father gives Himself freely to be enjoyed by the creature, but 'giving' in this context does not imply 'being sent,' which requires origin from another."
  },
  {
    "index": "43.5a",
    "refashioned": "Can the Son be sent invisibly -- not just in the visible mission of the Incarnation, but through interior grace?\n\nYes. Both the Son and the Holy Spirit can be invisibly sent, because both dwell in the soul by grace and both proceed from another. The Father dwells in us too, but since He does not proceed from another, He is not sent.\n\nThe Son's invisible mission corresponds to the intellectual illumination that grace brings. The Spirit's invisible mission corresponds to the kindling of love. Scripture says: 'The Son is sent whenever He is known and perceived by anyone' -- that is, when someone receives the intellectual illumination of faith and wisdom through sanctifying grace."
  },
  {
    "index": "43.5b",
    "refashioned": "Though all gifts of grace are attributed to the Holy Spirit (who is Love and the first Gift), some gifts are specifically appropriated to the Son -- those that belong to the intellect, since the Son proceeds as the Word. So the Son is sent according to intellectual illumination, and the Spirit is sent according to the kindling of charity.\n\nBut the Son's Word is not bare knowledge; it is 'knowledge with love.' And the Spirit's love is not blind; it flows from knowledge. So neither mission occurs without the other. Where the Son illuminates, the Spirit kindles; where the Spirit kindles, the Son illuminates. The two invisible missions are distinct in their formal character but inseparable in their occurrence."
  },
  {
    "index": "43.6",
    "refashioned": "Is the invisible mission directed to everyone who participates in grace?\n\nYes. The invisible mission occurs wherever there is both the indwelling of grace and a new beginning of that indwelling -- either the first reception of grace or a significant advance in it. This includes the Old Testament patriarchs and prophets (the Spirit was given to them, even if the visible signs came later at Pentecost).\n\nThe invisible mission occurs with every significant growth in grace -- not with every incremental increase (which would make mission continuous and trivial), but with proficiency in new acts or states: the fervor that leads to martyrdom, the grace to work miracles, the impulse to radical generosity. Even the blessed receive the invisible mission at the beginning of their beatitude, and it extends further through ever-deeper revelation of divine mysteries."
  },
  {
    "index": "43.7a",
    "refashioned": "Is the Holy Spirit sent visibly? Yes -- but differently from the Son's visible mission.\n\nThe Son was sent visibly by assuming human nature into the unity of His person. The Incarnation was a permanent, personal union. The Holy Spirit's visible missions were different: the dove at Christ's baptism, the tongues of fire at Pentecost, the breath on the apostles. These were visible signs created for the occasion, not personal unions. The Holy Spirit did not become a dove or become fire.\n\nHuman nature requires being led to invisible truths through visible things. So God manifested the invisible missions through visible signs. The Son's visible mission showed Him as the author of sanctification; the Spirit's visible mission showed the Spirit as the sign and gift of sanctification."
  },
  {
    "index": "43.7b",
    "refashioned": "Because the Son assumed human nature permanently, what is said of that nature can be said of the Son -- including being 'less than the Father.' The Holy Spirit, having not assumed any visible creature into personal union, cannot be called less than the Father on that basis.\n\nThe visible missions of the Spirit were not prophetic visions (which exist in the imagination) nor sacramental signs (which use pre-existing things symbolically). They were specially created visible phenomena that appeared, served their signifying purpose, and passed away.\n\nThe visible mission of the Spirit was not directed to all who received grace. It was directed to specific persons at foundational moments: Christ at His baptism (signifying His authority to give grace), the apostles at Pentecost (signifying their teaching office). The visible mission manifests the invisible one but is not required for every instance of it. The Old Testament fathers received the invisible mission of grace but not the visible mission of the Spirit, because the Son's visible mission had to come first -- the Spirit manifests the Son, as the Son manifests the Father."
  },
  {
    "index": "43.8",
    "refashioned": "Can a divine person send Himself? In a sense, yes.\n\nIf 'sending' means designating the eternal principle from whom the person proceeds, then only the Father sends the Son, and only the Father and Son send the Spirit. The Son does not send Himself in this sense, because He does not proceed from Himself.\n\nBut if 'sending' means being the principle of the temporal effect that constitutes the mission -- the grace, the indwelling, the new mode of presence -- then the whole Trinity sends, because the whole Trinity causes the effects of grace. In this sense, the Son sends Himself and the Spirit sends Himself, because each person, together with the others, causes the grace through which the mission is accomplished.\n\nThis does not mean a human being can 'send' the Holy Spirit, because humans cannot cause the effect of sanctifying grace. Only God can do that."
  }
]

# Write output
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Written {len(data)} refashioned entries to {OUTPUT_PATH}")
