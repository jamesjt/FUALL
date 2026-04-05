"""
Generate refashioned (modernized) versions of Summa Theologica Part I, Q14-Q26.
Outputs a JSON array of {index, refashioned} objects.
"""
import json

data = [
    # =========================================================================
    # Q14: OF GOD'S KNOWLEDGE (16 Articles)
    # =========================================================================
    {
        "index": "14.0",
        "refashioned": "Having examined what God is in himself, we turn to what God does -- beginning with what happens inside God (knowing and willing) before addressing what flows outward (creating). Since understanding is a form of life, knowledge leads naturally to questions about divine life, truth, and the ideas in God's mind. Sixteen questions about divine knowledge follow: whether God knows, how he knows himself, whether he grasps other things, whether his knowledge is step-by-step or all-at-once, whether it causes things to exist, and how it relates to evil, individuals, infinity, the future, and change."
    },
    {
        "index": "14.1",
        "refashioned": "God possesses knowledge in the highest possible degree. The key insight is that what separates knowing beings from non-knowing ones is range: a rock can only be a rock, but a mind can become, in a sense, anything it understands. The more immaterial something is, the wider its cognitive reach. Plants, locked in matter, know nothing. Animal senses, partially freed from matter, know something. The human intellect, further freed, knows more. God, who is utterly immaterial and purely actual, therefore knows most of all.\n\nThis does not mean knowledge in God works the way it works in us. In us, knowledge is a quality we acquire -- a habit moving from potential to actual. In God, there is no potentiality. His knowledge is not something added to his being; it is his being. And because knowledge adapts to the knower's mode of existence, divine knowledge does not split into universal and particular, or potential and actual, the way ours does. It operates on an entirely different plane."
    },
    {
        "index": "14.2a",
        "refashioned": "God knows himself perfectly, and he does so through himself -- not through some external representation. In any act of understanding, the object known must be present in the knower. When we understand something, our intellect is informed by an intelligible likeness of the thing. But this means our intellect starts in potentiality and is actualized by what it receives.\n\nGod has no potentiality. His intellect and its object are identical. He does not need to receive a likeness of himself because he already is the very intelligible content that would inform such understanding. His mind, the act of his mind, and the object of his mind are one and the same thing. So God knows himself through himself, without mediation."
    },
    {
        "index": "14.2b",
        "refashioned": "The objection that a knower must 'return to itself' to know itself -- implying motion God cannot have -- rests on a metaphor. 'Returning to one's essence' simply means subsisting in oneself rather than depending on something external. God supremely subsists in himself, so he supremely 'returns to himself.'\n\nThe objection that understanding involves being moved or perfected by something else also fails. Our intellect is perfected by what it receives only because it starts in potentiality. God's intellect, which is never in potentiality, does not need to be perfected by any object. It is its own perfection.\n\nFinally, the claim that we only know ourselves by first knowing other things reflects a limitation of our passive intellect, which must be activated by external objects before it can reflect. God, as pure act in both existence and intelligibility, needs no such activation."
    },
    {
        "index": "14.3",
        "refashioned": "God comprehends himself fully. To comprehend something means to know it as perfectly as it can be known. A theorem is comprehended when you grasp its demonstration, not when you merely find it plausible. God's power to know is as great as his actuality in being -- both are infinite and identical. So he knows himself as completely as he is knowable, which is perfect comprehension.\n\nThis does not make God 'finite to himself.' Comprehension here does not mean containment by something external. It means nothing about him is hidden from his own knowledge. God is not bounded by his intellect as if his intellect were something separate; rather, his intellect and his being are one."
    },
    {
        "index": "14.4",
        "refashioned": "God's act of understanding is identical with his substance. If it were something separate, then something other than God would be the perfection of God's nature -- his substance would stand to his intellect as potentiality to act, which is impossible in a being of pure actuality.\n\nThe logic is straightforward: understanding, unlike building or heating, does not pass outward to an external product. It stays in the knower as the knower's own perfection. Just as existence follows on form, understanding follows on the intelligible content present in the mind. In God, there is no form distinct from his existence, no intelligible content distinct from his essence. Therefore his understanding is his essence is his existence.\n\nThe result: in God, the knower, the known, the means of knowing, and the act of knowing are all one. When we say God understands, we are not adding multiplicity to his nature."
    },
    {
        "index": "14.5a",
        "refashioned": "God necessarily knows things other than himself. He understands himself perfectly, and perfect self-knowledge includes knowing the full extent of one's own power. Since God's power extends to everything that exists or could exist -- he is the first cause of all things -- knowing his own power means knowing everything his power reaches.\n\nMoreover, since God's existence is identical with his understanding, whatever effects pre-exist in him as their cause must exist in him in an intelligible way. Everything that is in another exists according to the mode of that in which it is. So all things exist in God according to the mode of understanding.\n\nGod does not know other things by looking outside himself. He sees them in himself, since his essence contains the likeness of everything. He knows himself through his own essence; he knows everything else through that same essence, because it is the template from which all things derive."
    },
    {
        "index": "14.5b",
        "refashioned": "When Augustine says God 'sees nothing outside himself,' this does not mean God is ignorant of the external world. It means that what exists outside God is known by God within himself -- in his own essence, which contains the likeness of all things.\n\nNor does knowing other things make something external the 'perfection' of God's intellect. A stone is not literally in the soul; its image is. The things God knows are in his intellect through his essence, which already contains their likenesses. No external perfection is added.\n\nAnd God's intellectual act is not specified by anything outside himself. It is specified by the primary object understood -- his own essence -- in which all other things are comprehended. So his act of understanding remains entirely self-determined."
    },
    {
        "index": "14.6a",
        "refashioned": "Does God know things merely in general, or does he know each thing in its specific, individual distinctness?\n\nSome argued that since God knows other things through himself as their universal cause, he can only know them in a general way -- as beings, not as the particular kinds of beings they are. Just as fire, if it knew itself, would know heat but not the specific things that happen to be hot.\n\nBut this cannot be right. Merely general knowledge is imperfect knowledge. Our own minds start with vague, general impressions and become more perfect as they grasp specifics. If God's knowledge of things beyond himself were only general, his intellect would be imperfect -- and so would his being, since in God these are identical."
    },
    {
        "index": "14.6b",
        "refashioned": "God knows all things with proper, specific knowledge -- not just as beings in general, but as distinct from one another. The reason is that God's essence is not related to the essences of creatures the way a generic concept relates to its species (like 'animal' to 'horse' and 'human'). It is related as a perfect act to imperfect acts. Knowing the number six means you implicitly know three; knowing a human means you implicitly know what an animal is.\n\nGod's essence contains every perfection found in any creature, and more. Since each creature's proper nature is a particular degree of participation in divine perfection, God could not know his own essence perfectly unless he knew every way it can be participated in. He therefore knows each thing according to its own distinct nature.\n\nAnalogies like 'a center knowing all its radii' or 'light knowing all colors' capture part of this -- universal causality -- but miss the crucial point. Light does not cause the differences between colors; those come from the medium. But God causes not just what creatures share in common (being) but also what distinguishes them from one another. Every form, every specification, every individuating principle pre-exists in God's perfection. So he knows each thing specifically, not just generically."
    },
    {
        "index": "14.6c",
        "refashioned": "The objection that knowing things 'as they are in the knower' limits God to knowing things only in their divine mode misreads the phrase. The eye does not know a stone according to the stone's existence in the eye; through the image in the eye, it knows the stone as it exists in reality. God knows things in himself, but by that very fact knows them in their own natures -- and more perfectly than they know themselves.\n\nThe objection that the created essence cannot reveal the divine essence (so neither should the reverse hold) confuses the direction of the relationship. The imperfect cannot reveal the perfect, but the perfect can reveal the imperfect. The divine essence, as the unlimited perfection that all creatures partially imitate, can serve as the proper concept of each thing according to the specific way that thing participates in it."
    },
    {
        "index": "14.7",
        "refashioned": "God's knowledge is not discursive -- he does not reason from one thing to another the way we do. Our thinking has two kinds of movement: sequential (first understanding one thing, then turning to another) and inferential (arriving at conclusions through premises).\n\nNeither applies to God. He sees all things simultaneously in one act, because he sees them all in one thing -- himself. There is no sequence. And he sees effects in their cause without needing to derive them step by step, because he does not discover his effects; he already knows them by knowing himself as their source. Discursive reasoning is the movement from the known to the unknown. In God, nothing is unknown."
    },
    {
        "index": "14.8",
        "refashioned": "God's knowledge is the cause of things, not the other way around. For us, knowledge is caused by the objects we know -- reality shapes our understanding. But God's relationship to the world resembles an architect's relationship to a building: the design in the architect's mind causes the building, not vice versa.\n\nHowever, knowledge alone does not produce things. An architect can conceive many houses he never builds. What makes knowledge productive is will. God knows all possibilities, but only those he wills to exist actually come into being. This is why divine creative knowledge is called 'knowledge of approbation' -- knowledge joined with will.\n\nNatural things therefore stand midway between God's knowledge and ours. God's knowledge is prior to things and measures them (as the architect's blueprint measures the building). Things are prior to our knowledge and measure it (as the finished building informs the visitor's understanding)."
    },
    {
        "index": "14.9",
        "refashioned": "God knows things that do not actually exist. Whatever can be made, thought, or said -- by any creature, or by God himself -- is known to God, even if it never becomes actual.\n\nThere is, however, a distinction. Some non-actual things were actual in the past or will be in the future. God knows all of these through what is called 'knowledge of vision,' because his eternal present encompasses all of time simultaneously. Eternity does not move through moments; it comprehends them all at once. What is past or future to us is present to God's gaze.\n\nOther things are merely possible -- within God's power or a creature's power, but never actually realized at any point in time. God knows these too, through what is called 'knowledge of simple intelligence.' He knows them as real possibilities, not as actualities.\n\nSince God's knowledge joined with his will causes things, not everything God knows must exist. Only what he wills to be, or permits to be, actually occurs."
    },
    {
        "index": "14.10",
        "refashioned": "God knows evil, though evil has no positive reality of its own. Evil is the privation of good -- it exists only as an absence or deficiency in something that should be otherwise. Darkness is known through light, and evil is known through good. To know any good thing perfectly, you must know what could corrupt or diminish it. Since God knows all good things perfectly, he necessarily knows the evils that oppose them.\n\nThis does not mean evil exists in God or that God causes evil. He knows evil not through evil itself (as if evil were a positive content in his mind) but through the good things to which evil is opposed. And knowing something through its opposite is not imperfect knowledge when the thing in question has no independent reality of its own. Evil by its very nature is a privation -- it can only be defined and understood through the good it negates."
    },
    {
        "index": "14.11a",
        "refashioned": "God knows individual, singular things -- not just universals. Some argued that since immateriality is what makes knowledge possible, and since singular things are individuated by matter, an immaterial intellect like God's could only grasp universals. But this misunderstands the relationship between God's intellect and matter.\n\nOur intellect knows only universals because it abstracts from material conditions -- it strips away individuality to reach the general concept. But God's intellect is not immaterial through abstraction. It is immaterial by its very nature, and as the cause of all things including matter, it is the source of both universal forms and individual instances.\n\nEarlier attempts to explain how God knows individuals failed. Saying he knows them 'through universal causes' is insufficient -- universal causes do not determine what makes Socrates this particular man rather than another. Saying he 'applies' universal knowledge to particular cases just pushes the question back, since applying knowledge to a particular already presupposes knowing that particular.\n\nThe real answer: God's knowledge extends as far as his causality. Since his creative power reaches not just to forms (the source of universals) but to matter (the principle of individuation), his knowledge reaches to individuals. His essence, as the productive principle of all things, is sufficient to know everything he makes -- not just in general, but in full particularity."
    },
    {
        "index": "14.11b",
        "refashioned": "Our intellect cannot grasp singulars because the intelligible content it works with is abstracted from individualizing conditions. But the intelligible content in God's intellect -- his own essence -- is not immaterial through abstraction. It is the source of everything that makes things what they are, including what makes them individual. So God knows both universals and singulars through his simple intellect.\n\nAnd while matter in its bare potentiality seems utterly unlike God (who is pure act), even matter, insofar as it has being at all, retains some likeness to the divine being."
    },
    {
        "index": "14.12a",
        "refashioned": "God can know infinite things. Since he knows not only what is actual but what is possible -- for himself and for all creatures -- and since possibilities are infinite, his knowledge must extend to infinity.\n\nThe objection that infinity means 'always more to count' and therefore cannot be grasped is based on a model of sequential counting. God does not enumerate things one by one. He knows everything simultaneously, in a single act. The infinity that defeats step-by-step measurement does not defeat all-at-once comprehension.\n\nThe key is the mode of the knowing form. A sense image represents only one individual. A human concept represents a species and thus implicitly covers infinite possible individuals -- but only generically, not distinctly. God's essence, as the sufficient likeness of everything that is or can be, represents all things including their distinguishing features. So his knowledge extends to infinite things as individually distinct."
    },
    {
        "index": "14.12b",
        "refashioned": "The objection that infinity cannot be 'traversed' conflates traversal (sequential passage through parts) with comprehension (complete grasp). God does not traverse the infinite; he comprehends it, because nothing falls outside his knowledge.\n\nThe objection that knowledge must 'measure' what it knows, and infinity cannot be measured, confuses quantitative measurement with the knowledge of essence and truth. God's knowledge measures things not by counting them but by knowing their nature. Even an actually infinite number of things (were such to exist) would have determinate, finite natures -- and therefore be fully knowable to God."
    },
    {
        "index": "14.13a",
        "refashioned": "God knows future contingent events -- things that could go either way and have not yet happened. This is one of the most contested points in philosophical theology, and Aquinas's answer turns on a careful distinction about perspective.\n\nA contingent event can be considered in two ways. Considered in its cause, it is genuinely undetermined -- the cause could produce this outcome or that. No certain knowledge of it is possible from this vantage point; only conjecture. But considered as it actually occurs in itself, it is no longer contingent in that moment -- it is determined, and can be known with certainty. (When you see someone sitting, you know with certainty they are sitting, even though their sitting was a free act.)\n\nGod's knowledge is measured by eternity, which is not a very long stretch of time but a simultaneous whole that encompasses all of time. Everything that happens at any moment in time is present to God's eternal gaze as actually occurring. He sees contingent events not in their causes (where they would be uncertain) but in their actual occurrence (where they are determinate). He sees the whole timeline the way someone on a hilltop sees every traveler on the road at once, while the traveler on the road can only see what is in front of him.\n\nSo contingent events are genuinely contingent relative to their created causes. But they are infallibly known by God, because he sees them as present in their actuality."
    },
    {
        "index": "14.13b",
        "refashioned": "The objection that a necessary cause must have a necessary effect misses the role of secondary causes. A seed's growth is contingent (it might fail) even though the sun that powers it is necessary. Likewise, things known by God may be contingent relative to their proximate causes, even though God's knowledge (the first cause) is necessary.\n\nThe deeper puzzle concerns the conditional statement: 'If God knew X would happen, then X will happen.' The antecedent is necessary (God's eternal knowledge does not change). Does the consequent therefore become necessary -- destroying all contingency?\n\nThe solution: when the antecedent involves an act of knowing, the consequent must be understood as it exists under that knowledge, not as it is in itself. 'If God knew X, then X will happen' is true where X is understood as present to God's eternal vision. As actually present, it necessarily is what it is (everything that is, while it is, necessarily is). But this does not make it absolutely necessary -- it remains contingent in its own nature and causes.\n\nThis parallels how something material (a stone) can be known immaterially -- the stone as known is immaterial, though the stone in itself remains material. Likewise, a contingent event as known by God is necessarily known, but as it exists in itself, it remains contingent."
    },
    {
        "index": "14.14",
        "refashioned": "God knows propositions -- statements that predicate one thing of another -- even though his intellect does not compose and divide the way ours does. Our minds know things one feature at a time and must assemble them into judgments ('Socrates is wise'). God knows every feature of every thing simultaneously by grasping its full essence in a single act.\n\nJust as God knows material things immaterially and composite things simply, he knows propositional truths non-propositionally. His one act of understanding his own essence suffices to represent all that can be true of any thing -- including every proposition that could be formed about it."
    },
    {
        "index": "14.15a",
        "refashioned": "God's knowledge does not change. Since his knowledge is identical with his substance, and his substance is utterly immutable, his knowledge must be equally unchanging.\n\nThe appearance of change -- 'God knew Christ would be born, but now does not know Christ will be born' -- dissolves once we recognize that God does not know propositional truths through sequential propositions the way we do. He knows in a single eternal act that Christ is born at a particular point in time. The proposition 'Christ will be born' was true before that time and false after, but God's knowledge of the event itself never shifts. He knows without change that the same event is future relative to one moment and past relative to another."
    },
    {
        "index": "14.15b",
        "refashioned": "Relational terms like 'Lord' and 'Creator' change as creatures change -- God becomes 'Lord of Israel' when Israel exists. But knowledge and love are different: they denote relations as the objects stand in God, not as they are in themselves. Since created things exist in God invariably (even as they change in themselves), knowledge and love are predicated of God without variation.\n\nThe objection that God 'could know more than he knows' (since he could make things he has not made) is misplaced. God already knows everything he could make -- through his knowledge of simple intelligence. The scope of his knowledge does not expand or contract with the scope of his creation."
    },
    {
        "index": "14.16",
        "refashioned": "God has both speculative and practical knowledge. Knowledge is speculative when it concerns what cannot be acted upon, when it considers an operable thing only in its general principles, or when it is not directed toward action. It is practical when it is ordered to operation.\n\nGod knows himself speculatively, since he is not something to be produced or acted upon. He knows things he has created (or could create) both speculatively -- grasping their natures and principles -- and practically, insofar as his knowledge directed their production. Things he can make but never does make, he knows speculatively but not practically. Even evil falls under his practical knowledge in a derivative sense, since he permits, directs, or counteracts it -- much as diseases fall under a physician's practical knowledge.\n\nSince God knows all other things by knowing himself, his speculative self-knowledge contains within it both speculative and practical knowledge of everything else."
    },

    # =========================================================================
    # Q15: OF IDEAS (3 Articles)
    # =========================================================================
    {
        "index": "15.0",
        "refashioned": "Having examined God's knowledge, we now consider the ideas in God's mind -- the patterns or blueprints by which things are made and known. Three questions: whether such ideas exist, whether there are many of them, and whether there are ideas of everything God knows."
    },
    {
        "index": "15.1",
        "refashioned": "There must be ideas in the divine mind. An 'idea' is simply the form of a thing existing apart from the thing itself -- serving either as a blueprint for producing it, or as a principle for knowing it.\n\nAnything produced by intelligence rather than chance requires a pre-existing plan. An architect must have the form of the house in mind before building it. Since the world was made by God acting through intellect (not by accident), there must be a form in the divine mind to whose likeness the world was made. That is what we mean by a divine idea.\n\nThis is not Plato's theory of self-subsisting Ideas floating in a separate realm. The ideas exist in God's intellect, not apart from it. And since God's essence is the productive principle of all things, the idea in God is ultimately identical with his essence -- not as God is in himself, but as his essence relates to and can be imitated by creatures."
    },
    {
        "index": "15.2a",
        "refashioned": "Are there many ideas in God, or just one? Several objections push toward unity: God's essence is one, his wisdom is one, and multiplying ideas seems to multiply eternal things (which would make temporal creatures the cause of something eternal).\n\nAgainst this, Augustine insists that each thing was created according to its own proper idea -- implying distinct ideas for distinct things."
    },
    {
        "index": "15.2b",
        "refashioned": "There must be many ideas in God. The ultimate purpose of creation is not a single creature but the order of the whole universe -- and you cannot conceive a whole without conceiving its parts. A builder cannot design a house without ideas of its individual components.\n\nThis does not compromise divine simplicity. The many ideas are not many images informing God's intellect (which would introduce real multiplicity). They are many things understood by one intellect through one essence. God knows his own essence perfectly, which means he knows every way it can be participated in by creatures. Each distinct way of participating in the divine perfection corresponds to a distinct idea. The plurality is in what is understood, not in the medium of understanding.\n\nThe relations that multiply ideas are not real relations in God (those belong only to the Trinitarian persons). They are relations of reason -- the divine intellect comparing its own essence to the many things that can imitate it."
    },
    {
        "index": "15.2c",
        "refashioned": "God's essence is called an 'idea' not as it is in itself but as it is the pattern of this or that particular thing. So there are many ideas because many patterns are understood through one essence.\n\nThe distinction between wisdom (by which God understands) and idea (what God understands) matters here. God understands many things by one act of wisdom. But he also understands that he understands them -- grasping the distinct patterns. It is this reflexive awareness that constitutes the plurality of ideas."
    },
    {
        "index": "15.3",
        "refashioned": "Are there ideas of everything God knows? Ideas serve two roles: as exemplars (blueprints for making) and as types (principles for knowing). As exemplars, ideas extend to everything God actually makes. As types, they extend more broadly -- to everything God knows in its specific nature, including things that never come to exist.\n\nSome limits apply. Evil has no idea in God, because evil is not a positive nature but a privation. God knows evil through the type of the good it negates. Primary matter has an idea only in conjunction with form, since matter cannot exist or be known by itself. Genera have no separate idea from species (since genera only exist in species). But individual things do fall under divine ideas, because God's providence extends to individuals, not just species -- contrary to what Plato supposed."
    },

    # =========================================================================
    # Q16: OF TRUTH (8 Articles)
    # =========================================================================
    {
        "index": "16.0",
        "refashioned": "Since knowledge concerns what is true, we now examine truth itself. Eight questions: where truth resides, how it relates to being and goodness, whether God is truth, whether truth is one or many, and whether it is eternal and immutable."
    },
    {
        "index": "16.1a",
        "refashioned": "Does truth reside in things or in the mind? Augustine offered definitions suggesting truth is in things ('That is true which is'). Aristotle placed it in the intellect ('The true and the false reside not in things, but in the intellect'). Which is right?"
    },
    {
        "index": "16.1b",
        "refashioned": "Truth resides primarily in the intellect and secondarily in things. Here is the reasoning:\n\nGoodness is the goal of appetite -- it resides in the desirable thing itself. Truth is the goal of intellect -- it resides in the knowing mind. Knowledge works by drawing the known into the knower, while appetite works by moving the desirer toward the desired. So the endpoint of knowledge (truth) is in the knower, just as the endpoint of desire (goodness) is in the thing desired.\n\nBut truth in the mind spills over onto things. A thing is called 'true' insofar as it conforms to an intellect on which it depends. Artifacts are 'true' when they match the designer's blueprint. Natural things are 'true' when they match their exemplar in the divine mind. 'A true stone' is one that fully possesses the nature proper to stone, as preconceived by God.\n\nSo truth is first and foremost the mind's conformity to reality. But things are called true by extension, insofar as they conform to the mind that designed them. The classic definition -- 'truth is the equation of thought and thing' -- captures both directions."
    },
    {
        "index": "16.1c",
        "refashioned": "Augustine's definition ('that is true which is') describes the truth of things, not of intellect. The ancient philosophers, who denied that natural forms came from any designing intelligence, were forced to ground all truth in conformity to the human mind -- leading to relativism. But if we recognize that things are true primarily by conforming to the divine intellect, these problems dissolve.\n\nThe objection that 'a thing is true because it exists, so truth must be in things rather than in minds' confuses the cause of truth with truth itself. A thing's existence causes truth in the intellect, but that does not make the thing itself the primary seat of truth -- just as medicine causes health in the animal without health residing primarily in the medicine."
    },
    {
        "index": "16.2",
        "refashioned": "Truth resides properly in the intellect's act of judging -- composing and dividing (affirming and denying) -- not in simple apprehension. Sight grasps a color, and it grasps it truly. The intellect grasps what a thing is, and grasps it truly. But neither the sense nor the intellect at that stage knows that it grasps truly. Truth as known -- truth as a conscious achievement -- requires the intellect to judge that reality matches its apprehension. This happens only when the intellect affirms or denies something about a subject.\n\nSo truth can be in the senses and in simple understanding the way truth is in any true thing. But truth as explicitly known and affirmed resides in the intellect's act of judgment."
    },
    {
        "index": "16.3",
        "refashioned": "True and being are convertible -- they cover the same territory but differ in meaning. Everything that exists is in principle knowable, and everything knowable is in some sense true. Just as 'good' adds to being the notion of desirability, 'true' adds to being the notion of relation to an intellect.\n\nEven non-being falls under truth in a derivative way: the intellect can make non-being an object of thought, and it is true that non-being is not. But truth is grounded in being, since what is not has no truth of its own apart from the mind that apprehends it."
    },
    {
        "index": "16.4",
        "refashioned": "Truth is logically prior to goodness, for two reasons. First, truth relates to being more directly: truth concerns being simply and immediately, while goodness concerns being insofar as it is desirable (which adds a further qualification). Second, knowledge naturally precedes desire -- you must apprehend something before you can want it.\n\nThe sequence is: first being, then truth (being as related to intellect), then goodness (being as related to appetite). But in the order of things desired, good is the more universal category, since truth itself is a good of the intellect."
    },
    {
        "index": "16.5",
        "refashioned": "God is truth itself. Truth in its fullest sense is the conformity of an intellect to reality. In God, this conformity is absolute: his being is not merely conformed to his intellect -- it is the very act of his intellect. His understanding is the measure and cause of every other being and every other intellect. He is his own existence and his own act of understanding. So truth is not merely in him; he is truth itself, the sovereign and first truth.\n\nEven the truth of our proposition 'someone sins' is ultimately from God -- insofar as all intellectual apprehension derives from him. But it does not follow that the sin itself is from God. That would be a fallacy of accident: the truth of the statement comes from God, but the act described in the statement does not."
    },
    {
        "index": "16.6",
        "refashioned": "Is there one truth or many? Both, depending on what we mean.\n\nIf we are talking about truth as it exists in created intellects, there are many truths -- as many as there are acts of knowing. Just as one face produces many reflections in a mirror, the one divine truth is reflected in many created minds.\n\nBut if we are talking about truth as it exists in things -- the conformity of things to the divine intellect that designed them -- then all things are true by one primary truth. Each thing is true insofar as it conforms to its exemplar in God's mind, and there is only one divine mind."
    },
    {
        "index": "16.7",
        "refashioned": "Created truth is not eternal. Truth resides in intellects. If no intellect is eternal, no truth is eternal. Only the divine intellect is eternal, so only the truth in the divine intellect is eternal -- and that truth is God himself.\n\nThe truths of mathematics ('two plus three equals five') or geometry ('the nature of a circle') are eternal only as they exist in God's mind. The objection that 'it was always true that what exists now would exist' is answerable: that proposition was true only insofar as its future being was contained in an eternal cause, namely God."
    },
    {
        "index": "16.8a",
        "refashioned": "Is truth immutable? Truth in the divine intellect is absolutely immutable, because God's intellect never changes and nothing escapes it. Truth in our intellects is mutable -- not because truth itself moves, but because our minds shift from truth to falsity. We change our opinions while reality stays the same, or reality changes while we keep our old opinions.\n\nBut the truth by which natural things are called true -- their conformity to the divine intellect -- is wholly immutable, since the divine standard never shifts."
    },
    {
        "index": "16.8b",
        "refashioned": "The proposition 'Socrates sits' is true with two kinds of truth simultaneously: the truth of the thing (it is a meaningful expression, as designed by the divine intellect) and the truth of signification (it accurately represents a fact). When Socrates stands up, the first truth remains (the proposition is still a well-formed expression) but the second changes (it no longer matches reality).\n\nSo truth does change in a sense -- not that truth disappears entirely, but that particular truths come and go as reality shifts. The sitting of Socrates is a different state of affairs before, during, and after -- and the truth of propositions about it varies accordingly."
    },

    # =========================================================================
    # Q17: CONCERNING FALSITY (4 Articles)
    # =========================================================================
    {
        "index": "17.0",
        "refashioned": "We now examine falsity. Four questions: whether falsity exists in things, in the senses, in the intellect, and how true and false are opposed."
    },
    {
        "index": "17.1a",
        "refashioned": "Does falsity exist in things? Things cannot be false in relation to the divine intellect -- everything that happens proceeds from God's design (except voluntary deviations, which are sins -- and scripture calls these 'untruths'). But things can be called false relative to our intellect in two ways. First, by misrepresentation: we call something false when a word or thought misrepresents it. Second, by natural tendency to mislead: things that naturally produce false impressions are called false -- fool's gold, sugar-coated poison, deceptive appearances. This second kind is the more proper sense. We do not call everything false that resembles something else; only when the resemblance naturally tends to produce a false judgment in most cases."
    },
    {
        "index": "17.1b",
        "refashioned": "Things do not actively deceive -- they only display their own nature. But they can occasion falsity by bearing a misleading likeness to other things. A thing is false not because it exists (insofar as it exists, it is true relative to the divine intellect) but because it falls short of what our intellect expects. An actor playing Hector is a true actor and a false Hector -- in things that are, there is always some degree of 'is not,' and in that gap, falsity finds its foothold."
    },
    {
        "index": "17.2",
        "refashioned": "The senses can be false, but only in limited ways. A sense is never wrong about its proper object: sight does not err about color (except when the organ is impaired -- a sick tongue tastes sweet as bitter). But the senses do err about common sensibles (size, shape, motion) and incidental objects (identifying a figure in the distance as a particular person).\n\nFalsity is more properly attributed to imagination than to the senses, since imagination can represent absent things as present -- producing illusions, dream experiences, and the like. The senses always report accurately what they receive; the error lies in how this information is interpreted and combined."
    },
    {
        "index": "17.3",
        "refashioned": "The intellect, like the senses, is infallible regarding its proper object: the essence or 'what-it-is' of a thing. You cannot be wrong about what a human being is while you genuinely grasp human nature. But the intellect can err in its judgments -- when it attributes to a thing something that does not belong to it, or denies something that does. This is the domain of composition and division (affirmation and denial), and here falsity properly resides.\n\nFalsity can creep into even simple apprehension, but only accidentally -- when the intellect mingles judgment into its grasp of an essence, such as applying the wrong definition to a thing, or constructing a self-contradictory definition ('a rational four-footed animal'). Regarding genuinely simple essences grasped on their own terms, the intellect is either right or draws a blank."
    },
    {
        "index": "17.4",
        "refashioned": "True and false are contraries, not mere contradictories (presence vs. absence). Falsity is not nothing -- it is a positive misapprehension, something asserted that does not match reality. Just as blindness is not merely 'not-seeing' but the absence of sight in a being that should see, falsity is not merely 'not-truth' but a distortion in a faculty that aims at truth.\n\nSince true and good are universal and convertible with being, every falsity is founded in some truth (as every evil is founded in some good). A false opinion about God is still an opinion -- something real and true as an act of thought -- even though its content is false. In God himself there is no falsity, since his intellect cannot err. But in our apprehension of God, the false opinion is genuinely contrary to the true one."
    },

    # =========================================================================
    # Q18: THE LIFE OF GOD (4 Articles)
    # =========================================================================
    {
        "index": "18.0",
        "refashioned": "Since understanding belongs to living beings, we now consider divine life. Four questions: what it means to live, what life is, whether life properly belongs to God, and whether all things are life in God."
    },
    {
        "index": "18.1a",
        "refashioned": "Life belongs to things that move themselves. We recognize an animal as alive when it moves on its own; when it stops moving of its own accord, we pronounce it dead. Extending this principle: anything that determines itself to movement or operation of any kind -- whether physical motion, growth, sensation, or thought -- is properly called living. Things that cannot initiate their own operations are not alive, except metaphorically.\n\nThis includes 'movement' in a broad sense. Understanding and willing are not physical motions, but they are self-initiated activities of a being in act -- and they count as life at the highest level."
    },
    {
        "index": "18.1b",
        "refashioned": "When Aristotle calls motion 'the life of natural bodies,' he speaks by analogy, not literally. Heavy objects falling and rivers flowing are moved by external principles (gravity, terrain), not by internal self-determination. Plants are the lowest genuinely living things -- they move themselves in growth and decay. 'Living waters' (flowing springs vs. stagnant ponds) merely look alive; the motion comes from an external source."
    },
    {
        "index": "18.2",
        "refashioned": "Life is not an operation but a mode of being. When we say something 'lives,' we mean it has a nature that can initiate its own operations -- not that it is currently performing any particular operation. 'Living' is an essential predicate, not an accidental one. A sleeping animal is still alive.\n\nBut we often use 'life' loosely for the operations themselves. We speak of the 'active life' versus the 'contemplative life,' the 'life of virtue,' the 'life of self-indulgence.' In this extended sense, whatever a person organizes their whole existence around becomes their 'life.' And this is how 'knowing God' can be called 'eternal life' -- it is the operation around which the ultimate mode of existence is organized."
    },
    {
        "index": "18.3a",
        "refashioned": "Does life properly belong to God? The objection: life requires self-movement, and God is the 'unmoved mover.' So how can God live?\n\nAnother objection: life requires a principle of life (a soul), but God has no principle -- he is underived."
    },
    {
        "index": "18.3b",
        "refashioned": "Life belongs to God in the highest possible degree. The argument proceeds by degrees of self-determination:\n\nPlants move themselves, but only in executing growth -- the form and goal of their movement are fixed by nature. Animals are more alive: they acquire the forms that guide their movement through sensation, giving them more self-determination. But animals still cannot set their own goals; instinct does that. Rational beings are more alive still: they can know the relationship between ends and means, set their own goals, and direct themselves accordingly. The intellect commands the senses, which command the body -- ascending layers of self-governance.\n\nBut even human intellects are not fully self-determining. Our first principles are given to us by nature, and our ultimate end (happiness) is willed necessarily, not chosen. We are partly moved by what we are.\n\nGod alone is wholly self-determining. His act of understanding is his very nature. He is not determined by anything external -- not by received principles, not by a nature he did not choose. His intellectual activity simply is his being. Therefore God has life in the most perfect and complete degree: entirely self-originating, entirely in act, entirely without dependence."
    },
    {
        "index": "18.3c",
        "refashioned": "The objection about movement confuses two kinds of action. Actions that pass outward (heating, cutting) perfect the thing acted upon. Actions that remain within the agent (understanding, willing) perfect the agent itself. When we say 'God moves himself,' we mean the second kind -- his understanding and willing are his own internal perfection, not a transition from potential to actual.\n\nGod has no principle of life because he is his own life. He does not need a soul to animate him, because his existence just is understanding, and understanding just is living. Life in our world requires vegetative powers because corruptible bodies need nourishment and reproduction. Incorruptible beings have no such requirement."
    },
    {
        "index": "18.4a",
        "refashioned": "Are all things life in God? Since God's living just is his understanding, and since his intellect, its object, and its act are all identical, whatever exists in God as understood is the divine life itself. All things made by God exist in him as things understood. Therefore all things in God are the divine life.\n\nThis does not mean all things in God are movement. Things exist in God in two senses: as sustained by his power (in which sense they retain their own natures) and as known by him (in which sense they exist according to the mode of the divine essence, which is life)."
    },
    {
        "index": "18.4b",
        "refashioned": "Things as they exist in the divine mind have a nobler mode of being (uncreated, intelligible) than they have in themselves (created, material). But this does not mean the divine idea of a horse is more truly a horse than an actual horse -- because being a horse involves being material, which the idea is not. The idea has a higher being, but the concrete thing more fully realizes the specific nature.\n\nEvil things, though known by God, are not 'life in God.' Evil is known through the types of good, not through its own positive presence in the divine mind. Things that never come to exist can be called life in God only insofar as 'life' means 'understood' -- they are grasped by the divine intellect -- but not insofar as life implies the principle of actual creation."
    },

    # =========================================================================
    # Q19: THE WILL OF GOD (12 Articles)
    # =========================================================================
    {
        "index": "19.0",
        "refashioned": "We now turn from God's knowledge to God's will. Twelve questions follow: whether God has a will, what he wills, whether he wills necessarily, whether his will causes things, whether his will has a cause, whether it is always fulfilled, whether it changes, whether it imposes necessity on things, whether God wills evil, whether God has free will, and how the 'signs' of God's will relate to his actual will."
    },
    {
        "index": "19.1",
        "refashioned": "God has a will, because will follows naturally from intellect. Every natural thing tends toward its proper form and rests in it when possessed. In knowing beings, this tendency extends to things apprehended by the intellect: the mind grasps something as good, and the will inclines toward it. Wherever there is intellect, there is will. Since God has intellect, he has will. And since his intellect is identical with his being, so is his will.\n\nGod's will is not an appetite striving for what it lacks (which would imply imperfection). Will includes not just desire for what is absent but love and delight in what is possessed. God's will rests in his own goodness, which he already fully possesses. And since the object of God's will is his own goodness (which is his own essence), his will is not moved by anything external. It moves itself -- or rather, it simply is the divine being's orientation toward its own infinite good."
    },
    {
        "index": "19.2",
        "refashioned": "God wills things other than himself. Every being that is in act and possesses some good naturally tends to communicate that good to others, as far as possible. Fire spreads heat; every agent in act produces its likeness. Since God possesses goodness in the most perfect way, his will to communicate that goodness is strongest of all.\n\nGod wills himself as the end and other things as ordered to that end. He wills his own goodness for its own sake and wills that other things exist as participants in it. Other things are willed not as if God needs them -- his goodness is entirely self-sufficient -- but because it befits the divine goodness to be shared.\n\nThis does not introduce multiplicity into God's will. Just as his intellect is one while understanding many things through one essence, his will is one while willing many things through one goodness."
    },
    {
        "index": "19.3a",
        "refashioned": "God necessarily wills his own goodness -- it is the proper object of his will, just as happiness is necessarily willed by us. But he does not necessarily will anything else.\n\nThe distinction is between absolute necessity and conditional necessity. A thing is absolutely necessary when denying it would be contradictory (like 'a whole is greater than its part'). God's will has a necessary relation to his own goodness: he cannot not will it. But things apart from God are not necessary for his goodness -- his perfection is complete without them. They are like a horse for a journey you could make on foot: useful but not indispensable.\n\nSo God wills other things freely, not out of necessity. However, once he does will something, it becomes conditionally necessary -- his will cannot change, so what he wills he cannot then un-will. His freedom lies in the initial willing, not in instability after the fact."
    },
    {
        "index": "19.3b",
        "refashioned": "That God wills from eternity does not make his willing necessary -- only conditionally so (given that he wills it, it must be). That he necessarily wills his own goodness does not force him to will other things, because his goodness does not depend on them. That his nature includes whatever he wills does not make that willing necessary, because willing other things is voluntary, not contrary to his nature.\n\nThe deepest point: God's not necessarily willing something does not make his will imperfect or contingent. The deficiency, if any, lies in the thing willed (which does not require the divine goodness to depend on it), not in the divine will itself. And the will's self-determination does not require an external cause to tip the balance -- God's will, unlike a naturally indifferent cause, determines itself."
    },
    {
        "index": "19.4a",
        "refashioned": "God's will is the cause of things. He does not create by necessity of nature (the way fire necessarily heats) but by intellect and will.\n\nThree arguments establish this. First, the order of causes: natural agents must have their ends predetermined by some intelligence. The arrow flies toward the target because the archer aimed it. Since God is first in the order of causes, he must act by intellect and will, not by blind nature.\n\nSecond, the character of natural agents: a natural agent, being determinate in nature, always produces the same kind of effect. But God, whose being is infinite and undetermined, produces the vast diversity of creation. This requires will choosing among possibilities, not nature mechanically producing one outcome.\n\nThird, the relation of effects to their cause: effects pre-exist in their cause according to the cause's mode of being. Since God's mode of being is intellectual, his effects pre-exist in him intellectually. They proceed from him through the inclination of will to actualize what his intellect conceives."
    },
    {
        "index": "19.4b",
        "refashioned": "The objection that God acts 'by his essence, not by choice' (like the sun shining) confuses the issue. God's essence is his intellect and will. So acting from his essence means acting through intellect and will.\n\nAugustine's statement 'Because God is good, we exist' does not mean God creates by nature rather than will. It means his goodness is the reason his will chose to create -- goodness is the motive, will is the mode.\n\nKnowledge and will are not competing causes. In us too, knowledge directs and will commands the same act. In God, these are one."
    },
    {
        "index": "19.5a",
        "refashioned": "Nothing external causes God's will. This does not mean God acts irrationally. He wills means for the sake of ends -- but since he grasps end and means in a single eternal act (not sequentially), willing the end does not cause willing the means. Instead, he wills the ordering of means to end. He wills this to be for the sake of that, but does not will this because of that.\n\nThe analogy is to understanding: if you grasp premises and conclusion simultaneously (seeing the conclusion in the premises), the understanding of the premises does not cause the understanding of the conclusion. You simply see that the premises entail the conclusion."
    },
    {
        "index": "19.5b",
        "refashioned": "That God's will has no cause does not destroy natural science. God wills effects to proceed from definite causes, preserving the order of the universe. So it is perfectly rational to investigate secondary causes -- just mistaken to treat them as primary, independent of God's will.\n\nNor does it mean everything depends solely on divine whim. Only the first, most fundamental features of creation depend directly on God's will alone (why there are rational beings at all). Everything else follows from the ordering of causes that God willed into existence."
    },
    {
        "index": "19.6a",
        "refashioned": "God's will is always fulfilled, because it is the universal cause of all things. A particular cause can be blocked by another particular cause -- but nothing can escape the order of the universal cause, under which all particular causes are included. Whatever seems to depart from God's will in one respect falls back into it in another: the sinner who defies God's moral will is caught by God's just will when punished.\n\nThe objection from Paul's 'God wills all to be saved' requires careful handling (see the reply below). The objection that God could will more good than exists confuses knowing all good with willing all good. The objection that secondary causes can block God's will only works for a first cause that is not truly universal -- and God's will is universal, encompassing all causes within it."
    },
    {
        "index": "19.6b",
        "refashioned": "'God wills all to be saved' can be understood in three ways: as applying only to those who are in fact saved; as applying to all classes of people (some from every group) but not every individual; or -- the most nuanced reading -- as expressing God's antecedent will versus his consequent will.\n\nThe antecedent/consequent distinction works like this: a judge, considered simply, wills all people to live. But when a particular person turns out to be a murderer, the judge wills his execution. The antecedent will considers things in the abstract; the consequent will considers all relevant circumstances. What God wills consequently (all things considered) always happens. What he wills antecedently (abstractly) may not.\n\nThis is like saying 'a merchant wants to keep his cargo' (antecedent) but 'throws it overboard in a storm' (consequent). The consequent will is the operative one."
    },
    {
        "index": "19.7a",
        "refashioned": "God's will is entirely unchangeable. Changing one's will requires either new information or a change in one's situation -- discovering that something previously thought bad is actually good, or finding that circumstances have shifted. Since God's knowledge is complete and his nature immutable, neither condition can arise.\n\nThe key distinction: willing that things change is not the same as changing one's will. You can decide in advance to build something and later tear it down -- one unchanging plan that includes both construction and destruction at their appointed times. God can will a thing for a season and its opposite for another season without his will ever shifting."
    },
    {
        "index": "19.7b",
        "refashioned": "When scripture says 'God repented,' it speaks metaphorically -- by analogy with human behavior. A person who destroys what they made appears to repent. God destroyed humanity in the flood without any change of will, since that destruction was always part of his plan.\n\nWhen God declares 'I will destroy this nation' and then relents when they repent, this is not a change of will either. God's consequent will always included the conditional: if they repent, they will be spared. He announced what would happen according to the secondary order of causes, but his higher will already encompassed the possibility of reprieve."
    },
    {
        "index": "19.8",
        "refashioned": "God's will imposes necessity on some things but not all. Some have tried to explain this through secondary causes: necessary causes produce necessary effects, contingent causes produce contingent effects. But this is insufficient. No secondary cause can ultimately block God's will, and the distribution of necessary versus contingent causes cannot be independent of God's intention.\n\nThe real explanation is God's own will. Because his will is perfectly efficacious, it determines not just what happens but how it happens. God wills some things to happen necessarily (the laws of mathematics, the motions of celestial bodies) and other things to happen contingently (free human choices). He achieves the latter by attaching contingent causes to contingent effects -- not because the contingent cause forces his hand, but because he designed the system to include contingency. The world contains both necessity and freedom because God willed it to contain both."
    },
    {
        "index": "19.9a",
        "refashioned": "God does not will evil. Evil, as the privation of good, is never an object of appetite in itself -- it is only encountered as a side effect of pursuing some good. The lion wills food, not the death of the stag as such. The sinner wills pleasure, not the moral disorder as such.\n\nGod wills no good more than his own goodness. He therefore never wills the evil of sin, which is directly opposed to right ordering toward the divine good. But the evil of natural defect or punishment he does will, by willing the goods to which these evils are attached: he wills justice, and punishment is attached to justice; he wills the natural order, and natural decay is part of that order.\n\nGod neither wills evil to exist nor wills evil not to exist. He wills to permit evil -- and permission is itself a good, because it preserves the freedom and natural order that make the universe what it is."
    },
    {
        "index": "19.9b",
        "refashioned": "Some argued that while God does not will evil, he wills 'that evil should exist' because evil serves the greater good. But this is wrong. Evil is not ordered to good by its own nature -- only accidentally. The tyrant did not intend to showcase the martyrs' patience. Good outcomes from evil are beside the sinner's intention. So we cannot say God positively wills the existence of evil; he permits it, and good sometimes results from that permission incidentally.\n\nThe logical point: 'God wills evil to exist' and 'God wills evil not to exist' are both affirmative statements -- they are not contradictory opposites. The real situation is that God neither wills evil's existence nor wills its non-existence. He wills to permit it. That is the precise position."
    },
    {
        "index": "19.10",
        "refashioned": "God has free will. Free will operates in the domain where necessity does not apply. God necessarily wills his own goodness (just as we necessarily will happiness), so there is no freedom there. But regarding everything else -- things he does not will by necessity -- God freely chooses. He can will a thing to exist or not exist, without either choice being compelled.\n\nThe objection that free will implies the ability to sin confuses freedom with defect. Freedom is the power to choose among options compatible with one's nature. Since evil contradicts the divine goodness by which God wills all things, willing evil is not a live option for God -- not because his freedom is limited, but because evil is not a genuine alternative for an infinitely good being. We ourselves can will to sit or not sit without sin; God can will a universe to exist or not exist without deficiency."
    },
    {
        "index": "19.11",
        "refashioned": "There is a difference between what God actually wills (the will of good pleasure) and what we call God's will by metaphor (the will of expression or sign). Just as punishment is called 'God's anger' not because God feels angry but because punishment is what anger produces in us, so precepts and prohibitions are called 'God's will' not because the precept itself is what God inwardly wills, but because issuing precepts is how we normally express our will.\n\nThis matters because scripture speaks of God 'willing' things that do not always come to pass (commands that are disobeyed). The will of good pleasure always succeeds. The will of expression indicates what God asks of us, but its fulfillment depends partly on creaturely response."
    },
    {
        "index": "19.12a",
        "refashioned": "Five signs of divine will are traditionally distinguished: operation (what God directly does), permission (what he allows without directly causing), precept (what he commands), prohibition (what he forbids), and counsel (what he recommends without commanding).\n\nOperation and permission concern the present: God either acts or allows. Precept, prohibition, and counsel concern the future: God directs rational creatures toward good (through commands for what is necessary and counsel for what is beneficial) and away from evil (through prohibition).\n\nA person reveals their will directly by acting or by not preventing action, and indirectly by directing others -- through binding commands, through forbidding, or through persuasive recommendation. The same framework applies, by analogy, to God."
    },
    {
        "index": "19.12b",
        "refashioned": "These five signs overlap: the same thing can be the subject of precept, operation, and counsel simultaneously. This is not redundant; it simply reflects different modes of manifesting the same underlying will.\n\nThe signs apply differently to different kinds of creatures. Rational creatures, who are masters of their own acts, receive precepts, counsels, and prohibitions. Other creatures, which act only as moved by God, fall under operation and permission alone. And evil is addressed by a single sign (prohibition) while good requires two (precept and counsel), because good admits of degrees -- what is minimally required versus what is optimally pursued."
    },

    # =========================================================================
    # Q20: GOD'S LOVE (4 Articles)
    # =========================================================================
    {
        "index": "20.0",
        "refashioned": "We now consider what flows from God's will: first love, then justice and mercy. Four questions about divine love: whether love exists in God, whether he loves all things, whether he loves some more than others, and whether he loves better things more."
    },
    {
        "index": "20.1a",
        "refashioned": "Love exists in God. Love is the most fundamental act of will -- more basic than joy, desire, or hope. You can only desire what you love, rejoice in what you love, or hate what opposes what you love. Love regards good universally, whether present or absent. Every other movement of the will presupposes it as root and origin.\n\nSince God has will, he must have love. And it is love properly speaking, not merely metaphorical love. In us, love in the sensitive appetite comes with bodily changes (passion). Love in the intellective appetite (will) does not. God's love is of this latter kind: real love without passion. 'God rejoices by an operation that is one and simple,' as Aristotle says."
    },
    {
        "index": "20.1b",
        "refashioned": "The objection that love is a passion and therefore unworthy of God confuses two levels of appetite. Passion belongs to the sensitive appetite and involves bodily change. But love, joy, and delight, considered as acts of the intellective will, are not passions at all. The bodily element is stripped away; only the formal element -- willing good to another, delighting in what is possessed -- remains. These can be properly attributed to God.\n\nThe objection that love is a 'uniting force' and therefore implies composition in God is also resolved. Love unites by willing good to another and by drawing the lover toward the beloved. God wills good to others (uniting by benevolence) and draws all things to himself as their end (uniting by final causality). Neither operation introduces composition into the divine nature."
    },
    {
        "index": "20.2a",
        "refashioned": "God loves all existing things. Every existing thing, insofar as it exists, is good -- existence itself is a good. Since God's will is the cause of all things, every creature has existence and goodness only because God willed good to it. And to will good to something is precisely what love is.\n\nBut there is a profound difference between divine love and human love. Our love is a response to goodness we discover in things -- we are moved by what is already good. God's love is the cause of goodness in things -- his willing makes them good. Our love follows goodness; God's love creates it."
    },
    {
        "index": "20.2b",
        "refashioned": "God even loves sinners insofar as they exist, since existence itself comes from him and is good. But insofar as they are sinners, they fall short of being -- sin is a privation, not a positive nature. Under that aspect, they are hated by God: not with passion, but in the sense that their deficiency is opposed to the good he wills.\n\nGod's love for irrational creatures is not friendship (which requires the capacity for mutual love and shared life) but something more like the love of a designer for his design -- ordering all things toward rational creatures and ultimately toward himself. This is not because God needs creatures but because of his goodness and the service they render to those who can share in his life."
    },
    {
        "index": "20.3",
        "refashioned": "God loves some things more than others. The act of his will is always the same in intensity (since it is one, simple, and eternal), but he wills greater goods to some things than to others. Since loving something means willing good to it, and since God wills more good to some creatures, he loves them more.\n\nThis is not arbitrary favoritism. God's love is the cause of goodness in things. No creature would be better than another unless God willed greater good for it. The hierarchy of creation -- rocks, plants, animals, humans, angels -- exists because God loved some things into higher levels of being."
    },
    {
        "index": "20.4a",
        "refashioned": "Does God always love better things more? Yes, necessarily -- because the very reason something is better is that God wills greater good for it. God's love is not responsive to pre-existing rank; it establishes rank. A thing is noble precisely because and to the extent that God wills good to it.\n\nThe apparent counterexamples dissolve on examination: God loved Christ more than all humanity (giving him the highest name and glory), not less. Angels are naturally superior to humans, but God assumed human nature in Christ -- not because he loves humanity more than angels in general, but because human need was greater (a doctor gives costly treatment to the sick, not to the healthy)."
    },
    {
        "index": "20.4b",
        "refashioned": "The case of Peter and John illustrates the nuance. Peter may have loved Christ more ardently; John may have been loved more intimately by Christ. Different gifts reflect different aspects of divine love -- neither simply 'more' nor 'less.'\n\nThe penitent versus the innocent: all else being equal, innocence is nobler. But the penitent who rises more humble and fervent may end up with more grace than the innocent who coasts. And grace freely given is a greater gift to one who deserved punishment than to one who did not.\n\nThe predestined sinner versus the currently just person: goodness must be measured at the time God's gift arrives. At the moment of final salvation, the predestined person receives the greater good. But at other moments, the currently just person may be better. God's love accounts for the whole arc of a life, not any single snapshot."
    },

    # =========================================================================
    # Q21: THE JUSTICE AND MERCY OF GOD (4 Articles)
    # =========================================================================
    {
        "index": "21.0",
        "refashioned": "After love, we consider God's justice and mercy. Four questions: whether justice belongs to God, whether his justice can be called truth, whether mercy belongs to him, and whether both justice and mercy appear in all his works."
    },
    {
        "index": "21.1a",
        "refashioned": "Justice belongs to God, but not the kind that governs transactions between equals (commutative justice -- buying, selling, exchanging). God owes nothing in that sense, since no one gave to him first. What belongs to God is distributive justice: the kind a ruler exercises in giving each subject what their role and nature require.\n\nThe order of the universe -- in both natural effects and voluntary actions -- displays this divine justice. God gives each existing thing what is proper to its nature and condition, preserving the proper order and powers of each."
    },
    {
        "index": "21.1b",
        "refashioned": "God can be just even though he is 'no one's debtor' in the ordinary sense. There is a twofold debt. First, God owes it to himself that his wisdom and goodness be expressed in creation -- that things fulfill what he designed them to be. Second, each creature is owed what its nature requires (hands for a human, service from animals). The second debt derives from the first: what is due to creatures is due because God's own wisdom ordained it so.\n\nGod is therefore a debtor to himself and, derivatively, to the order he established -- but never to creatures as an inferior owing to a superior. 'When you punish the wicked, it is just because it fits their deserts. When you spare the wicked, it is also just because it befits your goodness,' as Anselm says.\n\nVirtues connected to passion (temperance, fortitude) apply to God only metaphorically. But virtues of giving and ordering (justice, liberality, magnificence) apply properly, since they reside in the will, not the sensitive appetite."
    },
    {
        "index": "21.2",
        "refashioned": "God's justice can rightly be called truth. When the mind is the measure and rule of things (as an architect's blueprint measures the building), truth consists in the thing matching the mind. Works of justice are measured by law, and God's law is his own wisdom. So when God establishes things in the order that conforms to his wisdom, that is simultaneously justice (right ordering) and truth (conformity of reality to the divine standard).\n\nThis is not 'truth' in the sense of social honesty (saying what you mean). It is truth in the metaphysical sense: reality matching its intended design."
    },
    {
        "index": "21.3",
        "refashioned": "Mercy belongs to God in its effect, though not as an emotion. The word 'mercy' (misericordia) literally means 'a heart grieved by another's misery.' God does not grieve. But the effect of mercy -- removing misery, supplying what is lacking, healing deficiency -- belongs to God supremely, since he is the primary source of all perfection and goodness.\n\nMercy, justice, liberality, and goodness all describe the same divine act of communicating perfections, but under different aspects. Goodness: perfections are shared. Justice: they are proportioned to each thing's nature. Liberality: they are given without self-interest. Mercy: they remedy defect and remove misery.\n\nMercy does not contradict justice. A person who pays double what is owed does not violate justice -- they exceed it. God acts mercifully by doing more than justice strictly requires. 'Mercy exalts itself above judgment.'"
    },
    {
        "index": "21.4a",
        "refashioned": "Both mercy and justice appear in every work of God. Justice appears because God can do nothing that contradicts his own wisdom and goodness, and whatever he does in creation follows the proper order and proportion he established. Mercy appears because that order ultimately traces back to nothing but the free generosity of the divine will.\n\nThe logic: nothing is due to a creature except on account of something prior, which is due on account of something prior still, and so on. Follow the chain to its origin and you reach something that depends on nothing but God's gratuitous goodness. Every act of divine justice therefore rests on a foundation of mercy. Mercy is the root; justice is the structure built upon it.\n\nGod gives more than strict proportion requires. The gap between what creatures deserve and what divine goodness confers is always filled by mercy."
    },
    {
        "index": "21.4b",
        "refashioned": "Even damnation contains mercy: God punishes less than is deserved. Even justification contains justice: God forgives sin in response to love he himself infused. The conversion of Jews displays justice (fulfilling promises made to their ancestors); the conversion of Gentiles displays mercy (extending grace beyond any prior covenant). Both are present in both.\n\nThe suffering of the just in this world also displays both: justice, because lesser faults are cleansed; mercy, because affliction detaches them from earthly things and draws them toward God.\n\nEven creation -- which presupposes nothing at all in the created thing -- displays both. Justice: things are produced in accordance with divine wisdom. Mercy: things are brought from non-existence to existence, a gratuitous gift of being."
    },

    # =========================================================================
    # Q22: THE PROVIDENCE OF GOD (4 Articles)
    # =========================================================================
    {
        "index": "22.0",
        "refashioned": "Having considered what belongs to God's will taken absolutely, we now address providence -- the plan by which God orders all things to their end. Then predestination (the ordering of rational creatures to salvation). Four questions: whether providence belongs to God, whether it covers everything, whether it is immediate, and whether it imposes necessity."
    },
    {
        "index": "22.1a",
        "refashioned": "Providence properly belongs to God. Everything good in creation -- not just the existence of things, but their ordering toward an end -- is caused by God. Since God acts through intellect, the plan for this ordering must pre-exist in his mind. That plan is what we call providence: the type of the order of things toward their end, existing in the divine mind.\n\nProvidence is the chief part of prudence. Prudence involves remembering the past, understanding the present, and providing for the future. In God, all three collapse into a single eternal act. He does not deliberate (deliberation implies uncertainty), but he does command and direct -- which is what prudence fundamentally is."
    },
    {
        "index": "22.1b",
        "refashioned": "Two aspects of providence must be distinguished: the plan itself (the 'reason of order,' which is eternal) and the execution of the plan (governance, which unfolds in time).\n\nThe objection that prudence involves counsel (and God does not take counsel) is resolved: in God, the certainty of knowledge serves where inquiry serves in us. The 'counsel of his will' means not deliberation but the rational ordering that in us would be the product of deliberation.\n\nProvidence involves both intellect and will, but this does not make God composite. In God, intellect and will are identical with his essence."
    },
    {
        "index": "22.2a",
        "refashioned": "Everything is subject to divine providence -- without exception. Some ancient thinkers denied providence entirely (attributing everything to material chance), or limited it to incorruptible things (the heavens), or extended it only to species (not individuals), or restricted it to human affairs.\n\nBut since God is the cause of all being, and since every agent acts for an end, everything that has being in any way must be directed to an end by God. And since God's knowledge extends to every particular and every individual, his providence must extend equally far. Even apparently chance events are 'chance' only relative to their proximate causes; relative to the universal divine plan, nothing is unplanned."
    },
    {
        "index": "22.2b",
        "refashioned": "The problem of evil: if God provides for everything, why does evil exist? Because providence does not mean preventing all evil at all costs. A wise governor permits lesser evils to secure greater goods. If God prevented all evil, many goods would be lost -- lions would not eat if lambs could not die; patience would not exist if injustice did not.\n\nChance is not eliminated by providence. Events are 'by chance' relative to their particular causes. A man digging a field finds treasure by chance (he was not looking for it), but not by chance relative to the man who buried it. Relative to the universal cause, nothing is by chance -- but relative to secondary causes, contingency remains real.\n\nHuman freedom is not eliminated either. Being 'left in the hand of one's own counsel' is itself part of divine providence. God provides for humans precisely by giving them the capacity for self-governance through reason."
    },
    {
        "index": "22.3",
        "refashioned": "God provides for all things immediately -- in the sense that every creature's ordering exists in his mind directly. But the execution of his plan often runs through secondary causes. A king plans the whole campaign but delegates execution to generals, who delegate to captains.\n\nGod's use of intermediaries is not due to any deficiency. It reflects the abundance of his goodness: he communicates to creatures not just existence but the dignity of being causes themselves. Removing secondary causation would remove a great good from the universe.\n\nSo God has immediate providence over all things (the plan is his alone, down to the last detail) while governing through a hierarchy of causes. Even the lowliest creature is directly intended in the divine plan, though its actual production may involve a long chain of intermediate causes."
    },
    {
        "index": "22.4",
        "refashioned": "Divine providence does not impose necessity on all things. Providence has assigned contingent causes to some effects and necessary causes to others. The reason is not that God's will is deficient, but that he willed the universe to contain both necessary and contingent features -- this makes for a more complete and ordered whole.\n\nSo things happen contingently not despite providence but because of it. The order of divine providence requires that some things be contingent. A universe of pure necessity would be an impoverished universe.\n\nThe intermediary causes that God uses can sometimes fail (a plant fails to grow, a free agent chooses poorly). This does not mean providence failed -- it means the plan included contingency as a genuine feature of reality."
    },

    # =========================================================================
    # Q23: PREDESTINATION (8 Articles)
    # =========================================================================
    {
        "index": "23.0",
        "refashioned": "Providence applied specifically to the salvation of rational creatures is called predestination. Eight questions: what predestination is, what it places in the predestined, whether it implies certainty, its relation to election, whether merits cause it, the certainty of its number, whether it can be aided by prayer, and its relation to reprobation."
    },
    {
        "index": "23.1a",
        "refashioned": "Predestination is properly attributed to God. Since God's providence directs all things to their end, and since some rational creatures are directed to eternal life (which exceeds the natural capacity of any creature), this directing must be planned in advance in the divine mind. That advance plan is predestination.\n\nJust as providence is the plan of ordering things to their end, predestination is the specific plan of ordering certain rational beings to the supernatural end of eternal life. It is a part of providence, not a separate thing."
    },
    {
        "index": "23.1b",
        "refashioned": "Predestination does not place anything in the predestined person. It exists in God as his plan, not in the creature as a received quality. The effects of predestination -- grace and glory -- are in the creature, but predestination itself is an act of the divine intellect and will, ordering someone to salvation from eternity.\n\nPredestination differs from foreknowledge: foreknowledge extends to good and evil, but predestination concerns only the good (the directing to salvation). It is an active plan, not passive observation."
    },
    {
        "index": "23.2",
        "refashioned": "Predestination implies certainty. Since divine providence infallibly achieves its purposes (nothing escapes the universal cause), and predestination is a part of providence, its fulfillment is certain. Those whom God has predestined to eternal life will certainly attain it.\n\nBut this certainty does not impose necessity. Predestination is carried out through contingent secondary causes -- including free human choices. The certainty is on God's side (his plan cannot fail), not on the side of the secondary causes (which retain their contingent character). A predestined person could, considered in themselves, fail -- but considered under divine providence, they will not."
    },
    {
        "index": "23.3",
        "refashioned": "Does God reprobate anyone? If predestination is part of providence, and providence permits some things to fail for the sake of a greater good, then yes: God permits some rational creatures to fall short of eternal life. This is reprobation.\n\nReprobation is not symmetrical with predestination. Predestination is the cause of both present grace and future glory. Reprobation is not the cause of present fault (sin comes from the free will of the creature), but it is the cause of the future penalty. God does not cause anyone to sin; he permits sin and ordains punishment.\n\nWhy God predestines some and reprobates others cannot be traced to any cause in the creatures themselves. It is a matter of the divine will, which assigns different roles for the sake of the order and beauty of the whole -- just as a builder does not place every stone in the same position."
    },
    {
        "index": "23.4",
        "refashioned": "The predestined are chosen by God. Election implies selection, and since predestination involves directing particular individuals to glory, it presupposes an act of choosing. And since will presupposes knowledge, election presupposes foreknowledge. But in God, these are not temporally sequential -- he knows, chooses, and plans in one eternal act.\n\nPredestination is not the same as election. Election is the choosing; predestination is the entire plan that follows from the choosing (including the ordering of grace and glory). But election is a necessary component of predestination."
    },
    {
        "index": "23.5a",
        "refashioned": "Are anyone's merits the cause of their predestination? No -- not the merits that predestination itself produces (that would be circular), nor merits in a prior life (there is no such thing in this framework), nor foreseen future merits (since even those merits are effects of predestination, flowing from the grace that predestination arranges).\n\nWe can say that God pre-ordained some to glory on account of merits -- but those very merits were also pre-ordained by God. At the foundation, the plan traces back to the divine goodness alone."
    },
    {
        "index": "23.5b",
        "refashioned": "Within the execution of predestination, there is order and causality: later effects can depend on earlier ones, and merit can be the reason for glory. God wills to give glory because of merit, and merit because of grace. But the whole arrangement as a whole has no cause except the divine goodness.\n\nThis is not arbitrary. Justice governs the internal ordering: glory follows merit, mercy precedes merit with grace. But why this particular set of persons rather than another -- why Jacob and not Esau -- traces to nothing in the creatures themselves, only to God's will communicating his goodness."
    },
    {
        "index": "23.5c",
        "refashioned": "Some argued that the reason God elects some and not others lies in foreseen merits -- God predestines those whom he foresees will respond well. But this reverses the order. Grace is the cause of good response, not the other way around. The very capacity to merit is itself a gift of predestination.\n\nOthers suggested God pre-ordains to glory based on merit, and to merit based on grace -- assigning cause at each step. But they could assign no cause for why grace is given to one and not another. So the question remains: why this person? And the only answer is the divine will, which distributes its goodness freely.\n\nThis parallels a craftsman choosing some stones for the foundation and others for the walls. The choice is not based on differences in the stones (all are equal in raw material) but on the craftsman's purpose for the whole structure."
    },
    {
        "index": "23.6",
        "refashioned": "The number of the predestined is certain to God. It is known not merely in general ('some will be saved') but in particular ('these specific individuals will be saved'). The number is fixed and will neither increase nor decrease.\n\nSome described this number as 'formally certain but materially uncertain' (meaning: the count is fixed, but who fills the slots is not). But this is wrong. God knows exactly who is predestined, down to the individual. The number is certain in both respects.\n\nThe claim sometimes made that the number of predestined was set to replace the fallen angels is probable but not definitive. What is clear is that the number is part of the providential plan for the whole universe."
    },
    {
        "index": "23.7a",
        "refashioned": "Can prayer and good works help bring about predestination? Yes -- as secondary causes executing the divine plan, not as causes of the plan itself. Predestination includes both the end (glory) and the means (prayer, good works, grace). When people pray for the salvation of others, they are acting as instruments of a predestination already decreed."
    },
    {
        "index": "23.7b",
        "refashioned": "The objection that prayer is useless if predestination is certain confuses the certainty of the plan with the superfluity of means. A military victory may be certain in the general's plan, but the soldiers' actions are still necessary to execute it. Predestination is fulfilled through secondary causes, not despite them.\n\nThe objection that predestination cannot be aided because nothing is greater than the eternal fails to distinguish the plan from its execution. The eternal plan is not aided (it is complete in God from eternity). But the temporal execution proceeds through creaturely acts -- and these genuinely contribute to the outcome, even though the outcome is divinely certain."
    },
    {
        "index": "23.7c",
        "refashioned": "The conclusion is that the execution of predestination includes the prayers of the saints as genuine instrumental causes. This is not a contradiction: the plan is certain, and prayer is part of what makes it certain. Remove the prayer, and the plan would have been different. But the plan was never going to be different, because the plan always included the prayer."
    },
    {
        "index": "23.8a",
        "refashioned": "Can the predestined be damned, or the reprobate saved? Taken absolutely (considering only their own nature and free will): yes, the predestined can fail and the reprobate can succeed. Taken under the condition of divine predestination: no. The two are compatible because predestination operates through contingent causes. The contingent cause retains its natural capacity for either outcome, while the providential arrangement ensures one outcome actually occurs.\n\nThis is like a runner who can lose (naturally) but will win (given divine arrangement). The capacity to lose is real; the actuality of winning is certain."
    },
    {
        "index": "23.8b",
        "refashioned": "The number of predestined does not increase through prayer (as if prayer could add someone to a fixed list). Rather, prayer is itself part of the predestination of those who were always on the list. The execution unfolds through secondary causes, prayer included, but the plan itself is immutable.\n\nSimilarly, saying 'the predestined person can be damned, considered in themselves' does not mean predestination can fail. It means the person's nature does not of itself guarantee salvation. But predestination never relies on nature alone; it operates through grace, which is precisely what nature alone cannot provide."
    },

    # =========================================================================
    # Q24: THE BOOK OF LIFE (3 Articles)
    # =========================================================================
    {
        "index": "24.0",
        "refashioned": "The concept of the 'book of life' -- a metaphor for God's knowledge of who will attain eternal life -- is connected to predestination. Three questions: what the book of life is, whose life it concerns, and whether anyone can be blotted out of it."
    },
    {
        "index": "24.1",
        "refashioned": "The 'book of life' is a metaphor for God's knowledge of those who will attain eternal life. Just as a list of soldiers enrolled for battle is called a book of the living, God's knowledge of those destined for the 'battle' of eternal life is called the book of life.\n\nSince God knows all things in his own essence, this 'book' is not a separate record but an aspect of divine knowledge -- specifically, the knowledge of who will ultimately be saved. It relates to predestination as knowledge relates to the plan it informs."
    },
    {
        "index": "24.2",
        "refashioned": "The book of life concerns only those who will attain eternal life -- not all living things, and not even all rational creatures, but those who will in fact reach their supernatural end. Some are inscribed absolutely (those predestined to glory), others are said to be inscribed in a qualified sense (those who have present grace but may ultimately fall away).\n\nThe distinction between being inscribed absolutely and in a qualified sense tracks the difference between predestination (which is certain) and present justice (which can be lost)."
    },
    {
        "index": "24.3",
        "refashioned": "Can anyone be blotted out of the book of life? Not in the absolute sense -- God's knowledge of who is predestined never changes. But in the qualified sense: someone in a state of grace (and thus 'written' in the book according to present justice) can fall from grace. They are 'blotted out' not from God's eternal knowledge but from the current status that gave them a place in the metaphorical book.\n\nThe erasure is not in God's knowledge (which never errs and never changes) but in the thing known. A person's state changes; God's knowledge of their state was always accurate, including his knowledge that they would eventually fall."
    },

    # =========================================================================
    # Q25: THE POWER OF GOD (6 Articles)
    # =========================================================================
    {
        "index": "25.0",
        "refashioned": "After considering what belongs to God's will and intellect, we turn to divine power -- the principle by which God produces external effects. Six questions: whether there is power in God, whether it is infinite, whether God is omnipotent, whether he can make the past not to have happened, whether he can do what he does not do, and whether he can do better than he does."
    },
    {
        "index": "25.1",
        "refashioned": "Active power belongs to God in the highest degree. Power is the principle of action on something else, and God, as the first cause of all things, is supremely an agent. Unlike created things, whose power is distinct from their being (and therefore limited), God's power is identical with his being and essence. Since his being is infinite, his power is infinite.\n\nThe objection that power implies potentiality (and God is pure act) confuses passive and active potency. Passive potency (the capacity to receive something) is indeed excluded from God. But active potency (the capacity to produce something) is not a deficiency -- it is perfection. God's power is pure active potency without any admixture of passivity."
    },
    {
        "index": "25.2",
        "refashioned": "God's power is infinite. This follows from the infinity of his essence. In any agent, the more perfectly it possesses the form by which it acts, the greater its power of acting. Since God's form (his essence) is infinite (as established in Q7), his power is infinite.\n\nAn infinite effect does not result from this, because God wills to produce finite effects. The infinity is in the power, not necessarily in what the power produces. A sculptor with unlimited skill can still choose to carve a small figurine."
    },
    {
        "index": "25.3a",
        "refashioned": "God is omnipotent -- he can do all things that are possible. But 'possible' must be understood correctly. It does not mean 'whatever can be imagined, no matter how self-contradictory.' The absolutely possible is whatever does not involve a contradiction in terms. God can do everything that is absolutely possible; he cannot do what is self-contradictory, because a self-contradiction is not a coherent 'thing' at all."
    },
    {
        "index": "25.3b",
        "refashioned": "A square circle is not something God fails to create; it is nothing. The words are strung together, but they do not describe any possible reality. 'God cannot make a square circle' does not limit God's power, because there is no power-deficiency involved -- only a pseudo-task that does not correspond to anything.\n\nOmnipotence means: every consistently describable state of affairs is within God's power. Whatever involves being, he can cause. Whatever involves non-being disguised as being (contradictions), he 'cannot' do -- but this 'cannot' reflects the incoherence of the request, not any deficiency in God."
    },
    {
        "index": "25.3c",
        "refashioned": "The common formula 'God can do all things' should be understood as: God can do whatever is possible, and something is possible if it does not involve contradiction. This is not circular (defining omnipotence by possibility and possibility by omnipotence) if we define possibility independently, in terms of the compatibility of subject and predicate.\n\nAristotle was wrong to say God cannot undo what is done (that was not about divine power but about the logic of past facts -- see the next article)."
    },
    {
        "index": "25.4",
        "refashioned": "Can God make the past not to have happened? No, because 'the past not having happened' is a contradiction. If something happened, it is true that it happened, and making that truth false would be making a contradiction true. This does not limit God's power; it is simply not a possible thing to do, for the same reason a square circle is not a possible thing to make.\n\nSome say God could in principle undo the past (since his power is greater than nature) but chooses not to. But this is confused. It is not a matter of choosing -- the task is incoherent. It is like asking whether God is strong enough to overthrow the law of non-contradiction. The question does not describe a feat of power; it describes a failure of meaning.\n\nThis is compatible with God's ability to restore what was lost (healing, resurrection, forgiveness). Restoring the future is not the same as undoing the past."
    },
    {
        "index": "25.5a",
        "refashioned": "Can God do things he does not actually do? Yes. If God could only do what he actually does, his power would be limited to what exists, and everything that exists would exist by necessity. But God acts by will, not by necessity of nature. He freely chose among possibilities. Therefore there are things possible to God that he has not done and will not do.\n\nGod could make more things or different things, or add features to existing things. The existing order is not the only possible one; it is the one God freely chose."
    },
    {
        "index": "25.5b",
        "refashioned": "The objection that God 'must do everything his power and goodness and wisdom require' is answered by distinguishing between the absolute power of God (what he can do) and his ordained power (what he has in fact decreed). His ordained power always operates within his wisdom and justice. His absolute power exceeds what he has actually chosen to do.\n\nNothing limits God's power except contradiction. His wisdom and justice do not limit his power -- they govern its exercise. What God actually does is always wise and just, but wise and just alternatives existed that he did not choose."
    },
    {
        "index": "25.6a",
        "refashioned": "Can God do better than he does? In one sense, yes: God can always bestow more goodness on any particular thing. He could make a better universe, or make any creature more perfect than it is. His power is not exhausted by what he has produced.\n\nBut in another sense, no: the universe as God made it cannot be improved while remaining the same universe. If you change the proportions, you change the whole. A four-stringed instrument cannot sound better by tightening one string beyond its proper tuning. Each thing in the universe is as good as it needs to be for the order of the whole; making one part better without adjusting everything else would disrupt the harmony."
    },
    {
        "index": "25.6b",
        "refashioned": "God cannot make something better than the humanity of Christ (which is united to God) or better than the beatific vision of the blessed (which is the enjoyment of God himself). These are already at the absolute summit of created goodness by virtue of their direct union with the infinite divine nature.\n\nBut for everything else, God could always produce something better. There is no ceiling on possible perfection short of God himself. Each thing he makes is good, but he could always make a better one -- though the 'better' version would be a different thing, not an improved version of the same thing.\n\nThe key distinction: God always gives things their due goodness (justice), and always more than their strict due (mercy). He does what he does wisely and well. But the claim that he 'could not do better' would limit his infinite power, which is false."
    },

    # =========================================================================
    # Q26: THE DIVINE BEATITUDE (4 Articles)
    # =========================================================================
    {
        "index": "26.0",
        "refashioned": "We conclude the treatment of the divine essence with beatitude -- God's perfect happiness. Four questions: whether beatitude belongs to God, what makes God beatified, whether he alone is essentially blessed, and whether all other beatitude is contained in his."
    },
    {
        "index": "26.1",
        "refashioned": "Beatitude belongs to God in the highest degree. Beatitude is the perfect good of an intellectual nature -- the state of having everything one wants and wanting nothing one lacks. Every intellectual being desires beatitude, and the more perfect the intellect, the more perfectly it can possess it.\n\nGod's intellect is the most perfect of all. He comprehends himself fully, his will rests in perfect satisfaction in his own goodness, and his being is entirely self-sufficient. Therefore he is not merely 'happy' in some qualified sense -- he is beatitude itself. Everything that anyone could ever desire in any form of happiness is found in God in a supereminent way: the joy of knowledge (he knows all things), the delight of possession (he possesses all perfections), the satisfaction of will (his will rests in infinite goodness)."
    },
    {
        "index": "26.2",
        "refashioned": "God is called blessed primarily on account of his intellect. Beatitude is the perfect operation of the highest faculty, and the highest faculty is intellect. What makes God blessed is his perfect understanding -- specifically, his perfect understanding of himself.\n\nThis does not exclude will from beatitude (delight in the good possessed is part of happiness). But the primary constituent of beatitude is the intellectual act that grasps the perfect good. Will's delight accompanies and completes beatitude but does not constitute it.\n\nSo when we ask 'what makes God happy?' the answer is: his perfect knowledge of his own infinite perfection. The will's satisfaction follows from this as a natural consequence."
    },
    {
        "index": "26.3",
        "refashioned": "God alone is essentially blessed -- blessed by his very nature, not by participation in something beyond himself. Every creature that attains beatitude does so by participation: its happiness consists in receiving something it did not have by nature (the beatific vision, the supernatural union with God). Creatures are made happy; God simply is happy.\n\nNo creature has a natural right to beatitude, since beatitude exceeds the capacity of any created nature. Angels and humans can be beatified, but only by grace -- a gift that elevates them beyond their natural powers. God needs no such elevation. His nature is his beatitude."
    },
    {
        "index": "26.4",
        "refashioned": "All beatitude is contained in God's beatitude. Whatever genuine happiness exists anywhere -- the contemplative joy of the philosopher, the delight of friendship, the satisfaction of desire fulfilled -- exists in God in a more perfect form.\n\nGod's contemplation is the perfect and unbroken knowledge of himself and all things. His delight is the perfect rest of will in infinite goodness. His friendship (if we may call it that) is the mutual love within the Trinity and the providential love he extends to creatures. Every form of happiness that any creature experiences is a faint echo of what exists in God completely.\n\nSo divine beatitude is not one species of happiness alongside others. It is the source and fullness of all happiness -- the ocean of which every creature's joy is a droplet."
    },
]

output_path = r"D:\Projects\Websites\Git\FUALL\content\books\build\summa_p1_refashioned_part2.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Wrote {len(data)} entries to {output_path}")
