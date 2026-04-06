"""
Generate Refashioned versions for Summa Theologica Part I, Q65-Q76.
The Work of Six Days (Q65-74) and the beginning of the Treatise on Man (Q75-76).
"""

import json
import os

BUILD_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(BUILD_DIR, 'summa_p1_refashioned_part5.json')

data = [

# ============================================================
# Q65: The Work of Creation of Corporeal Creatures
# ============================================================

{
  "index": "65.0",
  "refashioned": "Having considered spiritual creatures, we turn to the physical world. Scripture describes three stages in its production: creation (\"In the beginning God created heaven and earth\"), distinction (separating light from darkness, waters above from waters below), and adornment (\"Let there be lights in the firmament\"). Four questions arise about creation itself: whether physical things come from God, whether they exist for God's goodness, whether God made them through angels, and whether their forms come from angels or directly from God."
},

{
  "index": "65.1a",
  "refashioned": "Some ancient heresies claimed that a good God could not have made the visible, physical world -- that it must be the product of an evil principle. This is untenable. Everything that exists shares something in common: being. When many different things share a single property, that property must trace back to a single source. Different heated objects all receive their heat from some source of heat. Likewise, all things that exist -- visible or invisible, physical or spiritual -- must receive their existence from one principle of being. The physical world comes from God, just as the spiritual does."
},

{
  "index": "65.1b",
  "refashioned": "Physical creatures are not evil in themselves. They endure in some respects forever, at least as to their matter, since what God creates is never annihilated. The closer something is to God's immutability, the more stable it is. As for the apparent evil of physical things -- serpents, scorching heat -- these are harmful only relative to particular observers. What injures one creature benefits another. Something harmful in one respect may be beneficial in another. And physical creation does not by itself draw us away from God; rather, \"the invisible things of God are clearly seen, being understood by the things that are made.\" If creatures lead people astray, the fault lies in those who misuse them, not in the creatures themselves."
},

{
  "index": "65.2a",
  "refashioned": "Were physical things created because of God's goodness, or for some other reason? Origen argued that God originally created only spiritual beings, all equal, and that the physical world was imposed as punishment when some of them fell. The degree of their fall determined what kind of body they were bound to. This position is wrong for two reasons. First, it contradicts Genesis, which says after each act of creation that \"God saw that it was good\" -- meaning each thing was made because it was good for it to exist, not as punishment. Second, it would make the physical arrangement of the universe a matter of pure chance.\n\nThe correct view: the universe is a whole composed of parts. Each part exists for its own proper activity. Less noble parts serve more noble ones, as the senses serve the intellect. All parts contribute to the perfection of the whole. And the whole universe, with all its parts, is oriented toward God as its ultimate end, imitating and displaying divine goodness. Physical creatures exist for the sake of God's goodness."
},

{
  "index": "65.2b",
  "refashioned": "That God created things so they might have being does not exclude the deeper truth that he created them for his own goodness -- since having being is itself a reflection of divine goodness. That physical creatures serve spiritual ones as their proximate end does not exclude God's goodness as their ultimate end. And the diversity among creatures is not unjust: just as an architect places different stones in different positions not because of any prior difference between stones, but to achieve the perfection of the whole building, God established creatures of various natures according to his wisdom."
},

{
  "index": "65.3",
  "refashioned": "Did God create physical things through intermediary spiritual beings, with each level of creation producing the next? No. Creation in the strict sense -- bringing something into existence from nothing, with no pre-existing material -- can only be the work of an infinite power. No creature, however powerful, can create from nothing. The more fundamental the level of existence, the higher the cause it requires. Matter itself, which underlies everything physical, belongs to the causality of the supreme cause alone. Secondary causes can shape and transform, but they cannot create. That is why Genesis says directly: \"In the beginning God created heaven and earth.\"\n\nThe order we see in creation reflects different grades of perfection established by divine wisdom, not a chain of created intermediaries each producing the next."
},

{
  "index": "65.4a",
  "refashioned": "Do the forms of physical things come from angels or spiritual substances? Three philosophical traditions said yes. Plato held that material forms are participations in separate, immaterial Forms -- an immaterial Horse causing all horses, an immaterial Life causing all living things. Avicenna held that forms do not subsist independently in matter but exist in angelic intellects, from which they flow into matter the way a craftsman's design flows into his work. Certain heretics combined these views, claiming God created matter but the devil differentiated it into distinct species.\n\nAll these positions share a common error: they treat forms as if they are independently generated, when in reality what comes into being is always the composite -- the formed thing, not the form by itself."
},

{
  "index": "65.4b",
  "refashioned": "Aristotle showed that what is properly made is always the composite of form and matter, not the form alone. Forms of perishable things come and go, but they are not themselves generated or destroyed -- the composite is. Like produces like: this fire generates that fire. We should not look for the source of physical forms in some immaterial realm, but in composite agents acting on matter.\n\nThat said, since physical agents are themselves moved by spiritual substances, physical forms do derive from spiritual substances in a secondary sense -- not by emanation, but as the endpoint of a causal chain of movement. And the ideas in angelic intellects, which are like seeds of physical forms, trace back ultimately to God as first cause. In the original creation, however, no transformation from potentiality to actuality occurred through natural processes. The first physical forms came directly from God, whose command alone matter obeys as its proper cause."
},

{
  "index": "65.4c",
  "refashioned": "When Boethius says that visible things come from \"forms without matter,\" he means the ideas in the mind of God. When we say forms in matter are referred to the angelic intellect, this happens through the angels' role as movers, not through emanation. The heavenly bodies likewise influence earthly things through movement, not by radiating forms into matter."
},

# ============================================================
# Q66: On the Order of Creation Towards Distinction
# ============================================================

{
  "index": "66.0",
  "refashioned": "Next we consider how creation was ordered toward the distinctions we see in the world. Four questions: Did formless matter exist before receiving form? Is the matter of all physical things the same? Was the empyrean heaven created at the same time as formless matter? Was time created simultaneously with it?"
},

{
  "index": "66.1a",
  "refashioned": "Did formless matter exist in time before it received its form -- was there a stage of primordial chaos? Genesis says \"the earth was void and empty,\" which Augustine takes to describe formless matter. And in nature, the imperfect does precede the perfect. On the other hand, an imperfect creation would imply an imperfect creator, and God's works are described as perfect. Also, if formlessness preceded form in time, the original state of creation would have been the chaos that the ancients described -- and this contradicts the orderliness Scripture attributes to God's work from the beginning."
},

{
  "index": "66.1b",
  "refashioned": "Augustine and the other Church Fathers only appear to contradict each other on this point because they define \"formlessness\" differently. Augustine means the complete absence of any form. Under that definition, formless matter could not have preceded form in time, because to exist in time already implies actuality, and actuality is itself a form. You cannot coherently say that something existed -- actually, in time -- yet had no form at all. That would be saying a thing was actual without any actuality.\n\nThe other Fathers -- Basil, Ambrose, Chrysostom -- mean something different by \"formlessness\": not the absence of all form, but the absence of beauty and full differentiation. On this reading, creation initially existed but lacked the order and beauty it would later receive. Specifically, three kinds of beauty were missing: the heavens lacked the beauty of light (\"darkness was upon the face of the deep\"), the earth lacked the beauty of being uncovered by water (\"the earth was void\"), and it lacked the beauty of vegetation (\"empty\" or \"shapeless\"). When these distinctions are kept clear, the apparent disagreement largely dissolves."
},

{
  "index": "66.1c",
  "refashioned": "Augustine interprets \"earth\" and \"water\" in Genesis 1 as symbols for primary matter itself -- since Moses needed to make the concept of formless matter accessible to ordinary people using familiar images. The other Fathers take \"earth\" literally as the element of earth.\n\nAs for how natural processes relate to divine creation: in nature, the imperfect does precede the perfect in time, because nature works by bringing potentiality into actuality. But God produces being out of nothing and can therefore produce perfect things instantly. If some Fathers hold that formlessness preceded form in time, this was not from any limitation in God's power but from his wisdom in establishing an order from imperfect to perfect.\n\nScripture already implies several kinds of distinction before the formal \"work of distinction\" begins: heaven is distinguished from earth (a material distinction), earth and water are named (elemental distinction), and different regions are assigned different positions (spatial distinction)."
},

{
  "index": "66.2a",
  "refashioned": "Is the underlying matter of all physical things -- terrestrial and celestial -- fundamentally the same? Augustine and Plato thought so, since the four elements can transform into one another, proving they share common matter. Aristotle disagreed. The heavenly bodies move in circles, while the elements move in straight lines (up or down). Circular motion has no contrary, so celestial bodies are free from the contrariety that makes terrestrial things corruptible. Different natural movements imply different natures, and different natures imply different matter."
},

{
  "index": "66.2b",
  "refashioned": "The deeper argument is this: matter in itself is pure potentiality, directed toward whatever forms it can receive. If celestial matter could receive terrestrial forms, it would have potentiality for forms it does not possess, which means it would have privation -- and privation combined with potentiality means corruptibility. But celestial bodies are by nature incorruptible. Therefore their matter cannot be the same as terrestrial matter.\n\nNor can we say, as Averroes suggested, that a celestial body is itself its own matter, with a separate substance serving as its mover. If we strip away the mover and the celestial body is not a composite of form and matter, then it would be pure form and pure actuality -- something actually understood rather than sensibly perceived. But celestial bodies are clearly sensible objects.\n\nSo celestial and terrestrial matter are the same only by analogy: both are potentiality relative to their respective forms, but not the same kind of potentiality."
},

{
  "index": "66.2c",
  "refashioned": "When Augustine speaks of formless matter as one, he means either that it is one in the order of being (all bodies share the order of corporeal existence) or he is following Plato in not recognizing a fifth element. As for the objection that all bodies belong to one genus and therefore share one matter: logically there is one genus of body, but physically, corruptible and incorruptible things differ in their modes of potentiality and are not in the same physical genus."
},

{
  "index": "66.3a",
  "refashioned": "Was the empyrean heaven -- a realm of light understood as the place of the blessed -- created at the very beginning alongside formless matter? Several objections arise: it would have to be a sensible body, yet it does not appear to move; it would need to influence lower bodies, yet without movement it seemingly cannot; and if it serves contemplation rather than natural purposes, why would a physical place be needed for something spiritual? Further, if it were wholly luminous, it should illuminate constantly, leaving no room for night."
},

{
  "index": "66.3b",
  "refashioned": "The empyrean heaven rests on theological tradition rather than explicit Scripture. The various authorities agree it is the place of the blessed but differ on why they posit it. The best reason draws from the nature of glory itself. In the final reward, there will be both spiritual and bodily glory -- not only in resurrected human bodies but in the renewed cosmos. Spiritual glory began at the world's origin in the blessedness of the angels. It was fitting, then, that bodily glory should also have some beginning from the start: a corporeal reality free from corruption, wholly luminous -- a physical anticipation of the glorified cosmos to come. This heaven is called \"empyrean\" (fiery) not because of heat but because of radiance.\n\nIts immobility is not a defect but suits its nature as something already in the state of glory. And it may well influence lower bodies despite not moving itself, just as the highest angels influence lower ones without being sent on missions. Its light is either of a more subtle nature than the sun's condensed rays, or it possesses the distinctive brightness of glory."
},

{
  "index": "66.3c",
  "refashioned": "The empyrean heaven, being ordered toward glory, may influence lower bodies not through movement but through stable, conserving power -- analogous to how the highest angels influence lower ones while remaining stationary. Physical place is assigned to contemplation not as necessary but as fitting: outward splendor corresponding to inward illumination. As for its light not illuminating the lower world, the firmament's solid but transparent structure contains the empyrean light within, or that light may be of a subtler nature that does not emit rays the way the sun does."
},

{
  "index": "66.4",
  "refashioned": "Was time created simultaneously with formless matter? Augustine says two things were created before time: primary matter and angelic nature. Others say time must have existed from the beginning because formlessness preceded form in duration, and duration requires a measure.\n\nThe resolution depends on which framework you adopt. For Augustine, matter and angels precede form not in time but only in origin and nature -- so time is not among the first-created things. For the other Fathers, who hold that formlessness preceded form in duration, time must have existed as the measure of that duration.\n\nEither way, from the very beginning there was movement of some kind -- at minimum, the succession of thoughts and desires in angelic minds -- and movement without time is inconceivable, since time is simply the measure of succession in movement. Time, unlike place, is not permanent; it was created in its beginning, and we can only grasp it in the present moment -- the \"now.\""
},

# ============================================================
# Q67: On the Work of Distinction in Itself
# ============================================================

{
  "index": "67.0",
  "refashioned": "We now consider the work of distinction itself -- the first day's work. Four questions: Is \"light\" used literally or metaphorically when applied to spiritual things? Is physical light a body? Is it a quality? Was light fittingly produced on the first day?"
},

{
  "index": "67.1",
  "refashioned": "Is \"light\" literal or metaphorical when applied to spiritual realities? The word has two uses: its original meaning (what makes things visible to the eye) and its extended meaning (what makes anything manifest to any kind of knowing). We say \"I see what you mean\" without implying eyesight. Similarly, \"light\" in its strict, original sense is metaphorical when applied to spiritual things. But in its broader, extended sense -- as that which makes manifest -- it applies properly to spiritual realities as well. The key is which sense you intend."
},

{
  "index": "67.2",
  "refashioned": "Is light a physical body? No, for three reasons.\n\nFirst, place. Two bodies cannot occupy the same space simultaneously, but light and air coexist in the same location.\n\nSecond, movement. If light were a body, its spreading would be local motion. But local motion cannot be instantaneous -- a body must pass through every intervening point. Yet light's diffusion is instantaneous: the moment the sun reaches the horizon, the entire hemisphere is illuminated. The distance from east to west is too great for the time to be merely too short to perceive.\n\nThird, generation and corruption. If light were a body, it would have to be destroyed every time darkness falls and regenerated every sunrise -- a body large enough to fill half the sky, created and annihilated daily. This contradicts both reason and common sense."
},

{
  "index": "67.3",
  "refashioned": "Light is a quality -- specifically, an active quality that flows from the substantial form of a luminous body, the way heat flows from the substantial form of fire. Proof: rays from different stars produce different effects according to the diverse natures of those bodies, which would not be the case if light were merely a generic property.\n\nLight is not a substantial form (as some claimed about the sun's light), because substantial forms are not directly perceptible to the senses, while light clearly is. Nor is light merely an \"intentional\" or apparent quality like a reflection -- it produces real physical effects, such as warming bodies.\n\nThe reason light vanishes when its source is removed is that light is not produced by a permanent transformation of matter. It is more like a quality in process of being received, which endures only as long as its active cause is present -- unlike heat absorbed by water, which lingers after the fire is removed."
},

{
  "index": "67.4a",
  "refashioned": "Was it fitting to assign the production of light to the first day? Light is merely an accidental quality -- shouldn't it be subordinate to more fundamental things? And isn't it the sun that divides day from night, which wasn't made until the fourth day?\n\nThese objections have force, but there are strong reasons why light comes first. On the other hand, if we follow Augustine's reading that the \"light\" of the first day is spiritual -- the formation of angelic nature through illumination by the Word of God -- then the production of spiritual creatures is recorded first as befitting their higher dignity."
},

{
  "index": "67.4b",
  "refashioned": "Other commentators hold that the light produced on the first day was corporeal, and they give good reasons for its priority. Light is a quality of the primary body. Just as knowledge proceeds from general principles to specific applications, so creation proceeds from the general to the particular. Light, being a common quality shared by both terrestrial and celestial bodies, fittingly comes first.\n\nAs for what this primordial light was, the best explanation is that it was the sun's own light in a formless, undifferentiated state -- the solar substance already possessing general illuminative power, which later received the specific, determinate power to produce the particular effects we observe. The first day's light thus already established the basic distinction between light and darkness, between hemisphere illuminated and hemisphere in shadow, between the period called \"day\" and the period called \"night.\"\n\nThe movement producing this alternation was the common daily revolution of the entire heavens -- distinct from the specific orbital movements of individual celestial bodies, which were established on the fourth day to produce the further distinctions of seasons, months, and years."
},

{
  "index": "67.4c",
  "refashioned": "The primordial light was not some temporary luminous cloud that later dissolved back into the sun's matter. Scripture records the institution of the natural order that would endure permanently, not temporary arrangements. Following Dionysius, the light was already the sun's substance, initially formless, later receiving its determinate character.\n\nOn Augustine's alternative reading, the production of light signifies the formation of spiritual creatures -- not in the perfection of glory but in the perfection of grace. The division of light from darkness then denotes the distinction between the spiritual creature formed by grace and the other, still-unformed creation. If all things received their form simultaneously, then the \"darkness\" must represent the spiritual darkness that God foresaw would come -- the fall of those who would choose against the light."
},

# ============================================================
# Q68: On the Work of the Second Day
# ============================================================

{
  "index": "68.0",
  "refashioned": "The work of the second day. Four questions: Was the firmament made on the second day? Are there waters above the firmament? Does the firmament divide waters from waters? Is there more than one heaven?"
},

{
  "index": "68.1a",
  "refashioned": "Was the firmament produced on the second day? The question seems contradictory: \"In the beginning God created heaven and earth\" suggests the heavens already existed. And if the firmament is naturally incorruptible (as Aristotle held), it could not have been formed from pre-existing matter, since incorruptible things are not generated from corruptible materials."
},

{
  "index": "68.1b",
  "refashioned": "Two principles guide the interpretation of such passages. Augustine teaches: first, hold the truth of Scripture without wavering; second, do not cling to any particular explanation so tightly that you cannot abandon it if proven false -- lest Scripture be exposed to ridicule.\n\nThe word \"firmament\" can be understood in two ways. If it means the starry heaven, then different philosophical views yield different answers. Those who held the heavens to be composed of the elements could accept that its substance was formed on the second day from pre-existing elemental matter. But Aristotle held the heavens to be a fifth element, naturally incorruptible -- so its substance belongs to the work of creation, while only its formation or configuration could belong to the second day.\n\nAlternatively, \"firmament\" may mean the atmospheric region where clouds form -- the dense lower air. On this reading, no philosophical objection arises. Augustine himself finds this interpretation worthy of commendation as \"neither contrary to faith nor difficult to prove and believe.\""
},

{
  "index": "68.1c",
  "refashioned": "The apparent contradiction between \"In the beginning God created heaven\" and the firmament being made on the second day can be resolved in several ways. Chrysostom suggests Moses first states the whole work summarily, then details it part by part. Or the heaven created \"in the beginning\" is different from the firmament of the second day -- it could be the empyrean, or the formless spiritual nature, or the spherical heaven without stars, while the firmament is the starry heaven. Or the first-day heaven is the starry heaven, and the second-day firmament is the atmospheric region."
},

{
  "index": "68.2a",
  "refashioned": "Are there waters above the firmament? Scripture says God \"divided the waters that were under the firmament from those that were above\" -- and as Augustine insists, the authority of Scripture outweighs any human reasoning, so whatever these waters are, we cannot doubt they exist.\n\nTheir nature depends on what we mean by \"firmament.\" If the firmament is the starry heaven and is elemental in nature, the waters above it could be elemental water of a rarer consistency. If the firmament is the starry heaven but of a different nature than the elements, then the \"waters\" above it are a transparent crystalline heaven -- called \"aqueous\" for its transparency, not its composition. If the firmament is the cloudy atmosphere, then the waters above it are simply water vapor raised above the cloud layer, from which rain falls.\n\nWhat we should not accept is the claim that water vapor rises above the starry heaven itself -- the physical impossibility of this is evident from the intervening fire zone, the tendency of light substances to settle below the moon, and the observable fact that vapor does not even reach the tops of the highest mountains."
},

{
  "index": "68.2b",
  "refashioned": "How can water, which is heavy, remain above the firmament? Augustine refuses to invoke miracles here -- \"our business is to inquire how God has constituted the natures of His creatures, not how far He may have pleased to work on them by way of miracle.\" If the firmament is the starry heaven and the waters above it are a crystalline sphere, the question does not arise -- it is not water in the ordinary sense. If the firmament is the atmospheric cloud layer, the answer is straightforward: water vapor naturally rises above the lower atmosphere. On the view that elemental water surrounds the starry heaven, one would have to suppose a different arrangement of elemental densities than Aristotle proposed.\n\nAs for the purpose of these waters: if they are the crystalline heaven, it serves as the primary mobile sphere whose daily rotation sustains the cycle of generation. If they are above the starry heaven, some authorities believed they temper the heat of celestial bodies."
},

{
  "index": "68.3a",
  "refashioned": "Does the firmament divide waters from waters? Read superficially, Genesis might seem to support the ancient theory that water is infinite, the primary substance of everything, and the firmament merely separates the cosmic water mass from the waters below. But this theory is demonstrably false and cannot be the meaning of Scripture.\n\nMoses was addressing people without scientific education. Earth and water are obviously corporeal to anyone's senses. Air is less obvious -- some philosophers even claimed it was nothing. So Moses mentions earth and water explicitly but leaves air implicit, hinted at by \"darkness was upon the face of the deep\" (darkness presupposes a transparent medium). Whether the firmament is the starry heaven or the cloudy atmosphere, it truly divides waters from waters: the starry heaven separates lower transparent bodies from higher ones, and the cloud layer separates the upper air (where rain forms) from the lower air connected to surface water."
},

{
  "index": "68.3b",
  "refashioned": "If the firmament is the starry heaven, the waters above and below differ in kind and the firmament marks their boundary. If the firmament is the cloud layer, both sets of waters are the same in kind but occupy different places for different purposes: the upper region is where water forms, the lower is where it rests. Moses includes all transparent and invisible bodies under the name \"water,\" which explains how waters can be found on each side of the firmament regardless of which interpretation we adopt."
},

{
  "index": "68.4a",
  "refashioned": "Is there only one heaven? Chrysostom says yes -- \"heavens of heavens\" is simply a Hebrew idiom for the plural. Basil says there are many. But the disagreement is mostly verbal. Chrysostom means by \"one heaven\" the entire body above earth and water, while Basil notes its distinct parts.\n\nScripture uses \"heaven\" in three senses. First, properly: the luminous or potentially luminous body that is naturally incorruptible. Under this sense there are three heavens -- the empyrean (wholly luminous), the crystalline (wholly transparent), and the starry (partly transparent, partly luminous, containing eight spheres: the fixed stars and the seven planets).\n\nSecond, loosely: any space that shares properties of the heavenly body, such as height or luminosity. Under this usage, the aerial space between earth and moon counts as a heaven, and various subdivisions of fire and air produce further \"heavens\" -- up to seven corporeal heavens in all.\n\nThird, metaphorically: heaven refers to the Blessed Trinity, or to spiritual blessings as the highest goods, or to the three kinds of supernatural vision -- bodily, imaginative, and intellectual."
},

{
  "index": "68.4b",
  "refashioned": "The earth relates to the heavens as the center of a circle to its circumferences. One center can have many circumferences, so one earth can have many heavens. When \"heaven\" refers to the whole of corporeal creation above us, it is one. But all the heavens share sublimity and some degree of luminosity, which is why the single name applies to many distinct realities."
},

# ============================================================
# Q69: On the Work of the Third Day
# ============================================================

{
  "index": "69.0",
  "refashioned": "The work of the third day. Two questions: the gathering of the waters, and the production of plants."
},

{
  "index": "69.1a",
  "refashioned": "Was it fitting that the gathering of waters should take place on the third day? Several problems arise. The first and second days describe God \"making\" things, but the third day describes a \"gathering\" -- a seemingly lesser act. The earth was already completely covered by water, so where could the waters gather? Not all waters are in continuous contact, so they cannot literally occupy \"one place.\" And water flows naturally to the sea anyway -- why would a divine command be needed for what nature already does?"
},

{
  "index": "69.1b",
  "refashioned": "The answer depends on our interpretive framework. For Augustine, the days do not represent temporal succession but the order of nature. \"Let the waters be gathered together and the dry land appear\" means that formless matter received the substantial forms of water and earth -- water gaining its characteristic fluidity and movement, earth gaining its characteristic stability and appearance. No temporal sequence is implied.\n\nFor the other Fathers, who read the days as successive in time, the picture is different. The first day formed the highest body (heaven) through the production of light. The second day formed the intermediate body (water) by establishing the firmament. The third day formed the lowest body (earth) by withdrawing the waters to reveal dry land. Earth's formless state -- covered and invisible -- ended when the waters gathered and the land appeared. Scripture expresses formation by the perfectly chosen words: \"Let the dry land appear.\""
},

{
  "index": "69.1c",
  "refashioned": "Why does the third day not use the word \"made\"? Augustine suggests it is because lower, mutable forms lack the perfection and stability of the higher creations. The gathering of waters and appearing of land convey the fluidity and instability of lower forms, in contrast to the firmness of spiritual and celestial creation.\n\nAs for the waters that covered the earth -- where did they go? Three explanations: they were heaped higher at their gathering place (the sea is demonstrably higher than land in some regions); they were previously diffuse and rarified, then condensed; or hollows in the earth received them. The first seems most probable. All waters flow to the sea as their goal, whether by visible rivers or underground channels, which is why Scripture can say they were gathered \"into one place\" -- meaning one collective region, distinct from the dry land.\n\nThe divine command does not override nature but institutes it. God's word gives bodies their natural movements, and through those movements they \"fulfill His word.\" Without divine intervention, water's nature would be to cover the earth completely. The partial uncovering was a necessary means to the end of supporting plant and animal life."
},

{
  "index": "69.2a",
  "refashioned": "Was it fitting that plants were produced on the third day? Plants have life, like animals -- shouldn't they belong to the work of \"adornment\" rather than \"distinction\"? And why mention plants but not minerals?\n\nThe earth's formless state was twofold: it was invisible (covered by water) and empty (lacking the plants that clothe it). Both deficiencies end on the third day. The waters gathered, revealing dry land. Then the earth brought forth vegetation.\n\nAugustine and the other commentators differ on what \"brought forth\" means. Most take it literally: plants were produced in actual species on the third day. Augustine reads it as the earth receiving the causal power to produce plants -- they were created potentially, with actual generation belonging to the ongoing work of providence. Either way, Scripture's language points to the production of complete species with reproductive capacity: \"Let the earth bring forth the green herb, and such as may seed.\"\n\nAs for minerals: Moses described only what was manifest to the senses. Minerals form in hidden ways underground, and they hardly differ from earth itself in appearance. Plants, by contrast, visibly transform the earth's surface."
},

{
  "index": "69.2b",
  "refashioned": "Plants' life is hidden -- they lack sensation and movement -- so their production is naturally grouped with the earth's formation rather than with the animate creatures that adorn it. Thorns and thistles existed before the curse on the earth; what changed after the Fall was not their existence but their relationship to human labor: \"to thee it shall bring forth thorns and thistles.\" And Moses omits minerals because they are generated invisibly within the earth and barely differ in appearance from earth itself."
},

# ============================================================
# Q70: Of the Work of Adornment, as Regards the Fourth Day
# ============================================================

{
  "index": "70.0",
  "refashioned": "We now turn to the work of adornment -- the furnishing of the world with moving, living things. The fourth day concerns the celestial lights. Three questions: Were the lights fittingly produced on the fourth day? What is the purpose of their production? Are the heavenly bodies living beings?"
},

{
  "index": "70.1a",
  "refashioned": "Scripture describes three kinds of work: creation (producing heaven and earth), distinction (giving form and order), and adornment (populating each region with beings that move within it). The work of adornment mirrors the work of distinction in parallel structure. The heaven, formed on the first day, is adorned on the fourth with luminaries that move through it. The water, distinguished on the second day, is adorned on the fifth with fish and birds. The earth, given form on the third day, is adorned on the sixth with land animals.\n\nSo the lights belong to the fourth day as the adornment of the heavens -- the first region that was distinguished now receives its proper inhabitants, as it were. Even Augustine, who often reads these days as simultaneous rather than sequential, agrees that the luminaries were made actually on this day, not merely potentially, since the firmament does not have the power to produce lights the way the earth produces plants."
},

{
  "index": "70.1b",
  "refashioned": "If light already existed from the first day, why are luminaries produced on the fourth? The light of the first day was either spiritual (on Augustine's reading) or corporeal but general and undifferentiated. On the fourth day, the luminaries received specific, determinate power to produce their particular effects -- the sun's rays acting differently from the moon's, and differently from each star's.\n\nPlants were recorded as produced before the sun specifically to prevent idolatry -- to show that vegetation does not depend on celestial bodies as its primary source. And the sun and moon are called the \"two great lights\" not because of their physical size (many stars exceed the moon) but because of their visible influence on the lower world and their apparent size as perceived from earth."
},

{
  "index": "70.2",
  "refashioned": "What is the purpose of the celestial lights? Every creature exists for its own proper activity, for other creatures, for the universe as a whole, and for the glory of God. Moses, however, emphasizes only their utility for human beings -- deliberately, to prevent the idolatry of treating celestial bodies as gods.\n\nTheir service to humanity is threefold. First, they provide the light necessary for sight and practical activity. Second, they produce the changes of seasons that prevent monotony, preserve health, and ensure the food supply -- all of which require the alternation of warm and cold, not perpetual summer or winter. Third, they serve as signs indicating weather conditions favorable or unfavorable for various undertakings.\n\nMoses says \"signs\" rather than \"causes\" precisely to guard against idolatry. The celestial bodies indicate changes in the physical world but do not determine what depends on free will. The general division of day and night began on the first day with the daily revolution of the heavens; the particular distinctions of seasons, months, and years began on the fourth day with the specific orbital movements of the sun, moon, and planets."
},

{
  "index": "70.3a",
  "refashioned": "Are the heavenly bodies living beings? The question has a long history. Anaxagoras was condemned in Athens for calling the sun a mass of stone, denying it was a god or alive. The Platonists held the opposite. Among Christian theologians, Origen and Jerome inclined toward celestial life, while Basil and Damascene denied it. Augustine left it open."
},

{
  "index": "70.3b",
  "refashioned": "The soul exists in a body for the sake of the soul's operations. Some operations -- nutrition, sensation -- require a body as their instrument. The intellect uses the body only indirectly, through the sensory phantasms the body provides.\n\nNow, nutrition and growth are incompatible with naturally incorruptible bodies. Sensation depends on elemental qualities and organs composed of mixed elements, which celestial bodies lack. So neither nutritive nor sensitive soul can belong to heavenly bodies. That leaves only intellect and movement.\n\nBut the intellect does not need a body as its instrument -- it needs the body only for supplying phantasms through the senses, and we have already ruled out sensation for celestial bodies. So uniting a soul to a heavenly body would not serve the intellect. The only remaining purpose would be movement: a spiritual substance moving the celestial body not by being its form but by contact of power, as a mover is united to what it moves.\n\nThe proof that celestial bodies are moved by spiritual substances rather than by mere natural tendency is that natural movement goes to a fixed endpoint and stops. Celestial movement never stops. It is therefore directed by intelligence.\n\nThe conclusion: heavenly bodies are not alive in the way plants and animals are. If they are called \"living,\" it can only be equivocally. The real dispute between those who affirm and deny celestial life is verbal, not substantive."
},

{
  "index": "70.3c",
  "refashioned": "The heavenly luminaries contribute to the adornment of the universe through their movement, which originates in a living spiritual substance -- so they participate in life derivatively, as instruments of a living mover. Their movements are natural not because of an internal vital principle but because of a natural aptitude for being moved by an intelligent power, much as we call voluntary movement natural to an animal."
},

# ============================================================
# Q71: On the Work of the Fifth Day
# ============================================================

{
  "index": "71.0",
  "refashioned": "The fifth day adorns the intermediate region -- water and the lower air -- with fish and birds, just as the fourth day adorned the heavens with luminaries. This parallels the second day, when the waters were distinguished by the firmament.\n\nFish and birds are produced from water not because water alone composes them (earth predominates in their bodies, as shown by their tendency to fall) but because water and air are the media in which they move, and their bodies have a special affinity with those elements. Moses groups them together because air, not being obviously corporeal to ordinary perception, is reckoned with water as a single intermediate region.\n\nAugustine holds, as with plants, that fish and birds were produced only potentially on the fifth day. The other Fathers take the production as actual. Either way, the order of production follows the order of the regions being adorned, not the relative perfection of the creatures. Land animals are more perfect than fish or birds, yet come on the sixth day because they adorn the earth -- the last region to be distinguished."
},

# ============================================================
# Q72: On the Work of the Sixth Day
# ============================================================

{
  "index": "72.0",
  "refashioned": "The sixth day adorns the earth -- the lowest body, corresponding to the third day when land was distinguished from sea -- with land animals. Scripture calls them \"living creatures\" rather than merely \"creeping things having life\" (the term used for fish), reflecting the more perfect and evident life of terrestrial animals.\n\nThe classification covers domestic animals (\"cattle\"), wild animals (\"beasts\"), and creeping things (those with no legs or very short ones). \"Quadrupeds\" is added as a general category. The land animals are not given a separate blessing because the blessing of multiplication, already pronounced over fish and birds, was understood to apply to them as well. But the blessing is explicitly repeated for human beings, since human generation has a special relationship to the number of the elect, and to prevent anyone from associating sin with the act of procreation.\n\nAs for poisonous and harmful creatures: every part of the universe serves its perfection, even those parts an untrained eye might consider unnecessary. Before sin, humans would have used the world in conformity with its intended order, and poisonous animals would not have injured them."
},

# ============================================================
# Q73: On the Things That Belong to the Seventh Day
# ============================================================

{
  "index": "73.0",
  "refashioned": "The seventh day. Three questions: the completion of God's works, God's rest, and the blessing and sanctification of this day."
},

{
  "index": "73.1a",
  "refashioned": "Should the completion of God's works be attributed to the seventh day? After all, God's works continue in this world, the Incarnation was a kind of completion, and Christ's cry \"It is finished\" came much later. And completion implies action, yet the seventh day is defined by rest.\n\nThe key distinction is between first perfection and second perfection. First perfection is substantial completeness -- a thing having all its parts and its proper form. Second perfection is the fulfillment of purpose -- the end achieved through operation. The first causes the second, as form is the principle of operation. The universe's second perfection -- the beatitude of the saints -- belongs to the end of the world. Its first perfection -- the completeness of all its constituent parts and natures -- is what is attributed to the seventh day."
},

{
  "index": "73.1b",
  "refashioned": "The first perfection (nature's completeness) causes the second perfection (glory's fulfillment). Nature was completed at creation, grace at the Incarnation, and glory will be completed at the end of the world.\n\nGod did act on the seventh day -- not by creating new things but by directing creatures to their proper operations, thus beginning the second perfection. The completion can be attributed to either the sixth or seventh day depending on the version of Scripture: the sixth day completed the universe in its parts, the seventh in its operation.\n\nNothing entirely new was made after the seventh day. Everything subsequent existed in some prior sense: materially (Eve from Adam's rib), causally (individual creatures from their species), or by similitude (new souls, the Incarnation, future glory). \"Nothing under the sun is new, for it has already gone before.\""
},

{
  "index": "73.2",
  "refashioned": "What does it mean for God to \"rest\"? Not cessation from labor, since God created without effort or movement. Rest here has two meanings.\n\nFirst, God ceased from creating new kinds of things. Nothing was made after the sixth day that did not already exist, in some form, in the original creation.\n\nSecond, God rested in himself. He did not need what he had made. He was not satisfied by his works as though he lacked something before making them. He rested \"from\" his works, not \"in\" them -- resting in his own self-sufficient goodness, which had been his happiness from all eternity. The seventh day simply marks the moment when this eternal self-sufficiency was expressed in relation to a completed creation.\n\nGod continues to work \"until now\" through preservation and providence -- sustaining what he made -- but not through the production of new natures. And since our own happiness consists in resting in God, his rest is also, in a secondary sense, his gift to us."
},

{
  "index": "73.3",
  "refashioned": "Why is the seventh day blessed and sanctified when nothing was created on it? Two reasons, corresponding to the two senses of God's rest.\n\nFirst, God ceased creating but began preserving and governing -- and the blessing relates to multiplication through ongoing providence. Just as the original blessing told creatures to \"increase and multiply,\" the seventh day marks the beginning of that providential work by which generation continues.\n\nSecond, God rested in himself, and every creature's special sanctification consists in resting in God. Things dedicated to God are called \"sanctified.\" The seventh day, as the day when the universe rests in God's completeness, is rightly set apart as holy.\n\nThe good mentioned in each day's work belongs to creation's first institution. The blessing of the seventh day belongs to its propagation."
},

# ============================================================
# Q74: On All the Seven Days in Common
# ============================================================

{
  "index": "74.0",
  "refashioned": "Considering all seven days together. Three questions: Are these days sufficient in number? Are they all one day or many? Does Scripture use suitable language to describe the six days' work?"
},

{
  "index": "74.1a",
  "refashioned": "Why exactly seven days? The structure maps to a threefold division of the physical world: heaven (the highest), water (the middle), and earth (the lowest). The Pythagoreans held that perfection consists in three things -- beginning, middle, and end. Each part is first distinguished, then adorned.\n\nThe first part (heaven) is distinguished on day one and adorned on day four. The middle part (water) is distinguished on day two and adorned on day five. The lowest part (earth) is distinguished on day three and adorned on day six. This gives the number six, which is itself mathematically perfect: it equals the sum of its factors (1 + 2 + 3). The seventh day stands apart as the day of rest and completion.\n\nCreation itself receives no separate day because it is instantaneous and outside time -- described as happening \"in the beginning,\" not \"in a day.\" Fire and air are not given their own days because Moses, addressing ordinary people, names only elements obvious to the senses."
},

{
  "index": "74.1b",
  "refashioned": "Creation gets no separate day because it denotes instantaneous production, not a process measurable by time. The works of distinction and adornment, however, involve changes that unfold in time, so each is assigned \"a day.\" Fire and air are omitted because Moses speaks to unlettered people who cannot easily perceive these elements. The production of animals follows the regions they adorn, not their relative perfection. And the seventh day is necessary either because God's resting in himself is a distinct event (Augustine) or because the world entered a new state -- one in which nothing more would be added."
},

{
  "index": "74.2a",
  "refashioned": "Are the seven days really seven, or just one day described from seven angles? Augustine reads them as one day -- representing the natural order of angelic knowledge, not a temporal sequence. Each \"day\" is the angels' knowledge of a successive work, and angelic knowledge is called \"day\" because light and spiritual illumination are naturally connected. The others read the days as genuinely successive in time.\n\nBut the disagreement is less deep than it appears. Both sides agree that matter initially existed under substantial forms, and that plants and animals did not exist in their final actual state from the very first instant. The real differences reduce to four specific points about whether there was a period without light, without a formed firmament, with earth still covered by water, and without heavenly bodies."
},

{
  "index": "74.2b",
  "refashioned": "Augustine's reading -- that all the days are one day viewed under different aspects of angelic knowledge -- is compatible with the actual order of things as long as the \"days\" represent the natural order of what is known, not a temporal succession in knowledge or production.\n\nThe other reading -- that the days are temporally successive -- is also compatible with various views of how creation unfolded. The key interpretive question is not whether the days are one or many, but how we understand the relationship between the formlessness described before the days and the formation described within them. Augustine takes the initial earth and water as symbols for totally formless matter; others take them as actual elements that merely lacked full distinction and beauty."
},

{
  "index": "74.2c",
  "refashioned": "When Genesis says God created plants \"before they sprung up in the earth,\" it means he created them potentially on the day of creation, though they emerged actually only later. God created all things together as to their substance in some formless state, but not as to the full distinction and adornment that gives them their beauty and proper nature. On the seventh day God ceased creating new kinds but continued providing for their increase. The days were not necessitated by any limitation in God's power but by the fitting order that adds successive states of perfection to the world."
},

{
  "index": "74.3a",
  "refashioned": "Does Scripture use the right words to describe the six days' work? Several features seem puzzling. \"God said\" appears in the works of distinction but not in the initial creation. Water's creation is not mentioned. The phrase \"God saw that it was good\" is missing from the second day. \"The Spirit of God moved over the waters\" seems to attribute spatial movement to God. The pattern of \"God said, let it be made ... and it was so ... God made\" seems redundant. And why are the days marked only by \"evening and morning\" rather than by all the day's parts?"
},

{
  "index": "74.3b",
  "refashioned": "Each of these verbal patterns carries theological meaning. \"God said\" in the works of distinction signifies formation through the divine Word -- the Son giving form to creation as a craftsman's idea gives form to his work. In the initial creation, the Son is indicated instead by \"in the beginning,\" since creation is the production of formless matter.\n\nWater's creation is implicit in \"earth,\" since Scripture customarily includes all four elements under that name. The Spirit \"moving over the waters\" signifies the Holy Spirit's creative love hovering over formless matter, as a craftsman's desire moves over his materials -- not bodily movement but preeminent creative power.\n\n\"God saw that it was good\" expresses the Trinity's satisfaction in creation and the permanence God intended for his works. Its absence from the second day is because that day's work -- the separation of waters -- was only begun and completed on the third day; the third day's approval covers both. Alternatively, the firmament as cloudy air is not a permanent principal part of the universe.\n\nThe threefold pattern (\"Let it be made ... it was so ... He made\") represents three modes of being: in the divine Word, in angelic knowledge, and in actual nature. \"Evening and morning\" mark the boundaries of the day: evening the beginning of night, morning the beginning of day. Scripture marks the endpoints rather than subdivisions. And the first day says \"one day\" rather than \"the first day\" to establish the measure of a natural day as twenty-four hours."
},

# ============================================================
# Q75: Of Man -- The Essence of the Soul
# ============================================================

{
  "index": "75.0",
  "refashioned": "Having treated spiritual and corporeal creatures separately, we now consider man, who is composed of both. Theology studies human nature through the lens of the soul. Three aspects of the soul require investigation: its essence, its powers, and its operations.\n\nRegarding the soul's essence, we consider first its nature in itself, then its union with the body. Seven questions about its nature: Is the soul a body? Is the human soul subsistent? Are animal souls subsistent? Is the soul identical with the person, or is a person composed of soul and body? Is the soul composed of matter and form? Is it incorruptible? Is it the same species as an angel?"
},

{
  "index": "75.1a",
  "refashioned": "Is the soul a body? The ancient materialist philosophers, unable to conceive of anything beyond the physical, said yes. They were wrong.\n\nThe soul is defined as the first principle of life. Not every principle of vital action qualifies -- the eye is a principle of seeing, but it is not a soul. The soul is the primary, foundational principle. Now, being alive does not belong to a body as such; otherwise every body would be alive. A body is alive because of some principle that makes it so -- its act. The soul, therefore, is not a body but the act of a body. Heat is the principle of warming, yet heat is not a body; it is an act that belongs to a body. Likewise, the soul is the act by which a body lives."
},

{
  "index": "75.1b",
  "refashioned": "The ancient error arose from assuming that only bodies can move other bodies and that knowledge requires the knower to be physically like the known. But Aristotle showed there can be movers that are not themselves moved in any physical sense. And knowledge does not require the knower to actually contain the physical nature of what it knows -- only the potentiality to receive its form. Color is not actually present in the eye's nature, only potentially. The ancients failed to distinguish actuality from potentiality. Finally, contact between mover and moved need not be physical contact between two bodies. There is contact of power, by which an incorporeal thing can move a body."
},

{
  "index": "75.2a",
  "refashioned": "Is the human soul something that subsists -- that exists in its own right, not merely as a property of something else? Yes. The intellect can know all corporeal things. But whatever knows a range of things cannot itself contain any of those things in its own nature, because having one nature would impede knowledge of others. A tongue coated with bitter bile cannot taste sweetness; a tinted lens makes everything appear that color. If the intellectual principle had a bodily nature, it could not know all bodies. Therefore the intellect is not a body, nor does it operate through any bodily organ.\n\nNow, only what subsists can operate independently. We do not say heat warms things -- we say the hot thing warms. Since the intellect has an operation that belongs to it apart from the body, it must be something subsistent: incorporeal and self-standing."
},

{
  "index": "75.2b",
  "refashioned": "The soul is subsistent in the sense of not being merely an accident or a material form inherent in something else. But it is still a part of human nature, not a complete substance in itself. Just as a hand or eye can be called a \"particular thing\" in the sense of being something real and non-accidental, but not in the sense of being a complete nature on its own, so the soul is subsistent without being a full person.\n\nThe body is necessary for the intellect's operation, but not as the organ through which intellect acts. The body provides the raw material -- the sensory phantasms -- from which the intellect draws its objects, just as color provides the material for sight. This dependence does not compromise the soul's subsistence, any more than an animal's need for external sensory objects compromises its subsistence."
},

{
  "index": "75.3",
  "refashioned": "Are the souls of non-human animals also subsistent? No. The key difference is that animal sensation is inseparable from bodily change -- the pupil is physically altered by color, the ear by sound, and excessive stimulation damages the organ. Every operation of the sensitive soul belongs to the composite of body and soul together, never to the soul alone. Since the sensitive soul has no operation independent of the body, it is not subsistent. A thing's mode of being follows its mode of operation. The human soul has an operation (understanding) that transcends the body; animal souls do not.\n\nHumans and other animals share the same genus but differ in species, and the specific difference comes from the form. Not every difference of form creates a difference of genus, but the human soul's capacity for independent intellectual operation constitutes a genuine species-level distinction."
},

{
  "index": "75.4",
  "refashioned": "Is the soul the same thing as the person? No. Man is not soul alone but the composite of soul and body. The definition of a natural kind includes both form and matter. \"Human\" does not mean \"soul\" -- it means \"soul-and-body composite.\" The matter that belongs to the species is not the individual's particular flesh and bones but the common matter: it belongs to the very concept of being human to have a body.\n\nIf sensation were an operation of the soul alone, we might identify man with his soul. But sensation belongs to the composite, and sensation is a distinctly human activity. So man is not his soul alone.\n\nTrue, we sometimes say a person \"is\" what is most principal in them -- as the actions of a state's leader are attributed to the state itself. So the intellectual part can be called the \"inward man.\" But strictly, a human person is the complete composite."
},

{
  "index": "75.5a",
  "refashioned": "Is the soul composed of matter and form? No. Consider this from two angles.\n\nFirst, the general notion of soul. The soul is by definition the form of a body. A form, as such, is actuality. Pure potentiality (which is what matter is) cannot be part of an actuality -- they are opposites. So the soul cannot contain matter.\n\nSecond, the specific nature of the intellectual soul. The intellect knows things in their universal, absolute nature -- a stone as stone, not as this particular stone in this particular location. If the intellectual soul contained matter, it would individualize every form it received, and could only know particulars, not universals -- just as the senses, which do receive forms in material organs, know only individual instances. The intellectual soul, and every intellectual substance that grasps universal forms, must be free from the composition of matter and form."
},

{
  "index": "75.5b",
  "refashioned": "The potentiality in the intellect is not the potentiality of primary matter. Primary matter receives individual, particular forms; the intellect receives universal, absolute forms. Different kinds of potentiality correspond to different kinds of actuality. The soul can be a subject of change -- from ignorance to knowledge, from vice to virtue -- without being material, because its potentiality is of a different order from matter's.\n\nAs for the objection that everything with a cause must have matter: this applies to composites, which are produced by transforming matter from potentiality to actuality. But a subsistent form does not owe its existence to any formal principle or material transformation. It simply is.\n\nAnd the soul is not infinite despite lacking matter. Only God, who is his own existence, is pure act and infinite. Every created intellectual substance is composed of form and participated existence -- it has actuality, but limited by its finite capacity to participate in being."
},

{
  "index": "75.6a",
  "refashioned": "Is the human soul incorruptible? Yes. Here is the argument.\n\nA substance can be corrupted only per se (in itself) or accidentally (through the corruption of something else). Things that do not subsist -- accidents, material forms -- are corrupted only accidentally, when the composite they belong to is destroyed. The souls of animals, which are not subsistent, are corrupted when the animal dies. But the human soul is subsistent, so it can only be corrupted per se.\n\nCan a subsistent form be corrupted per se? No. Existence belongs to a form by virtue of what it is. A form is an act, and existence belongs to an act intrinsically. You cannot separate a form from itself. Therefore a subsistent form cannot cease to exist.\n\nAdditional confirmation: corruption requires contrariety, but the intellectual soul has no contrariety -- it receives even contrary concepts without opposition (knowledge of contraries belongs to a single act of understanding). And every knowing being naturally desires to exist, with the scope of its desire matching the scope of its knowledge. The senses know only the here and now, so they desire only present existence. The intellect grasps existence as such, without limit of time. So every intellectual being naturally desires to exist always. A natural desire cannot be in vain. Therefore every intellectual substance is incorruptible."
},

{
  "index": "75.6b",
  "refashioned": "The apparent parallel between human and animal death is superficial. Bodies are alike in origin and process -- both come from earth, both breathe -- but souls differ fundamentally. Animal souls are produced by bodily powers; the human soul is produced by God directly. Genesis distinguishes them: \"Let the earth bring forth the living creature\" versus \"He breathed into his face the breath of life.\"\n\nThat the soul was created from nothing does not mean it can return to nothing through corruption. Corruption requires an internal potentiality for non-existence. Being created from nothing means only that God's active power, not any passive potentiality in the creature, is the source of its being. God could cease to sustain a creature, but that is not corruption -- it is annihilation, and it depends on God's will, not on any tendency in the creature.\n\nAs for the soul's dependence on the body for understanding through sensory images: this is the soul's mode of operation while united to the body. After separation, it will have a different mode of understanding, analogous to other separated intellectual substances."
},

{
  "index": "75.7a",
  "refashioned": "Is the human soul the same species as an angel? No. Origen thought all intellectual substances -- human souls and angels -- were originally the same, differing only in degree based on their free choices. But this cannot be right.\n\nIn incorporeal substances, there cannot be numerical diversity without species diversity. A separate form can only be one of its kind. If we imagine \"whiteness itself\" existing apart from any subject, there could only be one, because whiteness does not differ from whiteness except by being in different subjects. So each angel must be a unique species.\n\nSince diversity of species always involves diversity of nature -- one species being more perfect than another, as among colors -- human souls and angels must differ in species and nature. The fact that multiple human souls can exist within one species will be explained by their essential relationship to bodies, which provides the principle of individuation that pure spirits lack."
},

{
  "index": "75.7b",
  "refashioned": "Souls and angels share the same ultimate end (eternal happiness) but this does not make them the same species -- that destination is supernatural, not derived from their natural constitution. They share intellectuality, but \"intellectual\" is a genus, not an ultimate species-making difference; it admits of many degrees, just as \"sensitive\" admits of many species of animal. And while the body is not part of the soul's essence, the soul's essential capacity to be united to a body proves it belongs to a lower grade of intellectual nature than an angel, which needs no body at all."
},

# ============================================================
# Q76: Of the Union of Body and Soul
# ============================================================

{
  "index": "76.0",
  "refashioned": "We now consider the union of soul and body. Eight questions: Is the intellectual principle united to the body as its form? Is it multiplied according to the number of bodies, or is there one intellect for all? Is there another soul in the body besides the intellectual soul? Is there any other substantial form? What qualities does the body require? Is the soul united to the body through an intermediary body? Through an accident? Is the soul wholly present in each part of the body?"
},

{
  "index": "76.1a",
  "refashioned": "Is the intellect united to the body as its form? Six objections say no: Aristotle calls the intellect \"separate\"; if it were a body's form, its determinate nature would limit what it could know; forms received in bodies are received materially, but the intellect receives forms immaterially; intellectual power cannot be more abstract than the essence it derives from; the soul is subsistent and exists per se, so it cannot be a form (which exists through something else); and since form belongs to matter by nature, a form should never be separable from its matter -- yet the soul survives the body.\n\nBut the defining difference that constitutes the human species is \"rational,\" and this is attributed to us because of our intellectual principle. Difference is derived from form. Therefore the intellectual principle is the form of the human being."
},

{
  "index": "76.1b",
  "refashioned": "The intellect is the form of the human body. Here is why. Whatever primarily accounts for a thing's action is its form. Health is the form by which a body is healed; knowledge is the form by which the soul knows. The first thing by which a body lives is the soul -- the primary principle of nutrition, sensation, movement, and understanding. Therefore the principle by which we primarily understand is the form of the body.\n\nAnyone who denies this must explain how understanding is the action of this particular person. Each of us is conscious that it is we ourselves who understand. An action is attributed to someone in three ways: as the whole agent (the physician heals), by virtue of a part (the man sees by his eye), or accidentally (the white thing builds, meaning the builder happens to be white). Understanding is clearly not accidental to Socrates. Nor can the intellect be related to Socrates merely as a mover using his body as an instrument -- because understanding is not performed through any bodily organ. The only remaining option: the intellectual principle is united to Socrates as his form.\n\nThis resolves the objections. The intellect is indeed separate from bodily organs, but it is nonetheless the form of the body considered as a whole. It knows all things precisely because it is not the form of any particular organ. Its subsistence and its role as form are compatible: it is a form that also has its own act of existence, which it communicates to the body."
},

{
  "index": "76.1c",
  "refashioned": "Averroes tried to solve the problem by positing a single separate intellect for all humanity, connected to individuals through sensory phantasms. But this fails: if the intellect were one for all, then when one person understands something, everyone would understand it simultaneously. And the connection through phantasms is insufficient -- a phantasm is the object of understanding, not the subject. The subject who understands must be this individual person, and the only way to guarantee that is for the intellectual principle to be this person's own form.\n\nThe deeper point: the intellectual soul is both subsistent and the form of the body. These are not contradictory. Unlike other forms, the intellectual soul has existence in its own right and communicates that existence to the body. The body's existence is the soul's existence. This is why the soul can survive the body's dissolution -- its existence does not depend on the body, even though while united to the body, it gives the body its being."
},

{
  "index": "76.2a",
  "refashioned": "Is there one intellect for all human beings, or does each person have their own? Averroes argued for a single intellect shared by all, which he thought followed from the intellect's immateriality. If the intellect is not material, it cannot be individuated by matter, and therefore cannot be multiplied into many instances.\n\nBut this is wrong. If the intellect were one for all, there would be no difference between one person's understanding and another's -- and experience clearly shows that different people understand differently, at different times, and with different degrees of ability. Each person's acts of understanding are their own."
},

{
  "index": "76.2b",
  "refashioned": "The intellectual soul is multiplied according to the number of bodies, yet this does not make it material. The soul is individuated not as matter is individuated (by quantity) but as a form is individuated: by being the form of this particular body. When separated from the body, each soul retains its individual existence because it retains its relationship to the particular body it informed. Many souls of one species are possible because the human soul, unlike an angel, is essentially ordered toward union with a body, and bodies provide the principle of numerical distinction within the species."
},

{
  "index": "76.2c",
  "refashioned": "The intellectual soul, unlike an angel, is the form of a particular kind of matter. This is what allows many souls of the same species to exist, whereas each angel must be a unique species. The soul's multiplicity mirrors the multiplicity of bodies it informs, and after the body's dissolution each soul retains its distinct existence.\n\nThe individuality of an intellectual being does not prevent it from knowing universals. What impedes universal knowledge is materiality in the knower or in the means of knowing. If the cognitive form is abstracted from material conditions, it represents the universal nature without its individuating features. This holds regardless of whether there is one intellect or many.\n\nMultiple knowers can know the same object because different likenesses can all represent the same thing. Several eyes see the same color through different instances of reception; several intellects understand the same object through different acts of abstraction. Knowledge in teacher and student is numerically different even when the object known is the same."
},

{
  "index": "76.3a",
  "refashioned": "Are there multiple essentially different souls in a human being -- a nutritive soul, a sensitive soul, and an intellectual soul? The sensitive soul in animals is corruptible, while the intellectual soul is not. If these are the same soul in humans, how can one substance be both corruptible and incorruptible? And if the human sensitive soul becomes incorruptible by being joined to the intellectual soul, then human and animal sensitivity would differ in genus, which would make \"animal\" no longer a genus common to both.\n\nAgainst this multiplicity stands the teaching that there is one and the same soul in a human being -- one soul that both gives life to the body and directs itself by reason."
},

{
  "index": "76.3b",
  "refashioned": "Plato held that separate souls governed separate organs: nutrition in the liver, desire in the heart, knowledge in the brain. Aristotle rejected this, noting that divided animals (like worms) retain sensation and movement in each part -- which would be impossible if these powers belonged to spatially distinct souls.\n\nIf the soul is the body's form (not merely its mover), there cannot be multiple essentially different souls in one body. Three arguments prove this.\n\nFirst, unity. A thing is one by virtue of one form. If a human were alive by one soul, animal by another, and rational by a third, a human would not be truly one thing -- any more than \"a white musician\" is truly one thing.\n\nSecond, predication. We say a human \"is\" an animal essentially, not accidentally. If \"animal\" and \"rational\" came from different forms, one could only be predicated of the other accidentally or by presupposition -- neither of which captures their actual logical relationship.\n\nThird, interference. When one mental activity is intense, it impedes another (deep thought interferes with sensory awareness). This could not happen unless both operations shared a single principle.\n\nThe resolution comes from Aristotle's comparison of souls to geometric figures. A pentagon contains a square within it; the higher figure makes the lower superfluous as a separate shape. Likewise, the intellectual soul virtually contains everything that belongs to the sensitive and nutritive souls. Socrates is not a man by one soul and an animal by another -- one soul makes him both."
},

{
  "index": "76.3c",
  "refashioned": "The sensitive soul is incorruptible in humans not because of its sensitive nature but because of its intellectual nature. In animals, where sensitivity exists without intellectuality, the soul is corruptible. Intellectuality confers incorruptibility, and sensitivity cannot strip it away.\n\nThe difference between corruptible and incorruptible applies to forms, not to the composites classified into genera and species. Humans as composites are corruptible like other animals, so this difference does not disrupt the genus \"animal.\"\n\nAs for how the intellectual soul relates to the body animated by sensitivity: the genus \"animal\" is not taken from a separate sensitive form serving as matter for the intellectual form. Rather, reason considers the sensitive power as something common to humans and animals, and from this shared element constructs the genus. What the intellectual soul adds beyond the sensitive constitutes the specific difference. The classification reflects our manner of understanding, not a real composition of multiple forms."
},

{
  "index": "76.4a",
  "refashioned": "Is there any other substantial form in the human body besides the intellectual soul? No. If there were a prior form that gave the body its basic \"bodily\" existence before the soul arrived, then the soul would not make the body exist absolutely -- it would only make an already-existing thing into a living thing. The soul would be an accidental form, not a substantial one. And the union of body and soul would be accidental, not substantial -- like a garment put on an already-existing body.\n\nThis would mean that death is not the corruption of a substance but merely the loss of an accidental property. It would mean the word \"human\" names something accidental, not a genuine nature. These consequences are absurd. The intellectual soul is the one and only substantial form of the human body, giving it existence, corporeality, life, sensation, and rationality all at once."
},

{
  "index": "76.4b",
  "refashioned": "When the soul departs, what remains is not the same body that was alive. A dead body is called a \"body\" equivocally -- in the same way we call a painted eye an \"eye.\" The various organs and tissues lose their proper character at death because they lose the form that constituted them. The flesh and bone of a dead body are flesh and bone only in name.\n\nThe intellectual soul, as the single substantial form, gives the body all its determinations at once: existence, corporeality, animation, sensation, understanding. It does this not by stages but simultaneously, the way a more perfect form virtually contains all lesser forms. Each part of the body receives its proper character from the one soul, which distributes different powers to different organs."
},

{
  "index": "76.5a",
  "refashioned": "What kind of body does the intellectual soul require? The form is not for the sake of the matter; the matter exists for the form. So we must reason from the soul's nature to the body's requirements, not the reverse.\n\nThe intellectual soul holds the lowest rank among intellectual substances. Unlike angels, it is not naturally gifted with direct knowledge of truth but must gather knowledge from individual things through the senses. Nature never fails to provide what is necessary, so the intellectual soul must be endowed with sensory powers, which require a bodily organ. All senses depend on touch, and touch requires a body balanced between contraries -- hot and cold, wet and dry -- so it can be sensitive to all of them. The more balanced the body's composition, the more refined the touch.\n\nSince the intellectual soul possesses sensory power in its fullest form (what belongs to a lower nature exists more perfectly in a higher), the body it informs must be the most evenly balanced of all animal bodies. This is why humans have the finest sense of touch. And among humans, those with more refined physical constitution tend to have keener minds -- not because the body causes thought, but because better-tempered bodies provide better sensory material for the intellect to work with."
},

{
  "index": "76.5b",
  "refashioned": "Why is the intellectual soul, which is incorruptible, united to a corruptible body? The body's equable complexion is chosen because it suits the form's requirements; the corruptibility that follows from that balanced mixture is a consequence of the matter, not the purpose. An artisan chooses iron for a saw because it cuts hard material; that the teeth become blunt and rusted follows from the iron's nature, not from the artisan's intent. God compensated for this inherent corruptibility through the gift of grace.\n\nThe intellectual soul is united to a mixed body rather than a pure element because only a mixed body achieves the equable temperament that sense perception requires. A body dominated by fire would lack balance. And the mixed human body has its own dignity: being remote from the extremes of elemental contraries, it resembles in a way the celestial bodies.\n\nAs for the human body's lack of natural weapons and covering: the intellectual soul, because it comprehends universals, has power extending to infinity. It cannot be limited to fixed natural instruments. Instead, humans have reason and hands -- \"the organs of organs\" -- through which they can fashion tools of infinite variety for any conceivable purpose."
},

{
  "index": "76.6",
  "refashioned": "Is the intellectual soul united to the body through some intermediary body -- perhaps a subtle spirit or light-body? No. The soul is united to the body as form to matter, and form is united to matter directly, not through any intermediary. If something intervened between soul and body, it would need its own form, and we would face an infinite regress.\n\nThe soul does use subtle bodily spirits as instruments of movement and sensation -- much as a craftsman uses tools. But these are instruments, not intermediaries of union. The soul is immediately present to the body as its form."
},

{
  "index": "76.7a",
  "refashioned": "Is the soul united to the body through some accidental quality -- a disposition or intermediary accident? No. Form is related to matter directly, not through any intervening accident. Matter exists for the sake of form, not the reverse. The form does not need something in between to reach its matter. Accidental dispositions in the body prepare matter for receiving the form but are not the means of union itself."
},

{
  "index": "76.7b",
  "refashioned": "The soul, as form, is united to the body directly and immediately. However, bodily dispositions -- the right balance of qualities, proper organ structure -- are prerequisites for the soul's union with the body. If these dispositions are destroyed, the soul departs. But these are conditions, not connectors. They prepare the body to be a suitable subject for the soul, but the soul's union with its matter is immediate, with no intermediary body or accident standing between them.\n\nThough the soul considered in isolation is vastly different from the body, as form it does not exist apart from the body. By its own existence it is united to the body directly, just as any form, considered as pure actuality, is distant from matter (which is pure potentiality), yet is immediately present to the matter it informs."
},

{
  "index": "76.8a",
  "refashioned": "Is the whole soul present in each part of the body, or only in certain principal organs? If the soul were united to the body merely as its mover, it could reside in one part and move the rest remotely. But since the soul is the body's substantial form, it must be in every part. A substantial form gives existence not only to the whole but to each part. When the soul withdraws, we do not speak of a hand or an eye except equivocally -- a dead hand is called a \"hand\" only as a painted hand or stone hand is."
},

{
  "index": "76.8b",
  "refashioned": "The soul is wholly in each part of the body -- but we must distinguish what \"wholly\" means. There are three kinds of totality: quantitative (divisible into spatial parts), essential (having all the elements of its definition), and virtual (possessing all its powers).\n\nQuantitative totality does not apply to the soul, since the soul is not extended in space. Essential totality does apply: the complete essence of the soul -- its full nature and definition -- is present in each part of the body, just as the full nature of whiteness is in every part of a white surface.\n\nBut virtual totality is distributed: the soul is not present in each part with all its powers. Sight is in the eye, hearing in the ear, and so forth. The soul relates primarily to the whole body as its proper perfectible, and to the parts only secondarily, as they are ordained to the whole.\n\nSo: the whole soul (essentially) is in each part; but not every power of the soul is in every part. The nobler parts of the body are those that serve as organs for nobler powers."
},

{
  "index": "76.8c",
  "refashioned": "The soul need not be in every part to serve as the body's motive principle -- it suffices for it to be in some principal part from which motion flows. But as substantial form, it is necessarily in each part. That each part does not constitute a separate animal is because the soul relates to the whole body as its primary and proportionate subject; the parts are ensouled only as parts of that whole. Powers like intellect and will, which exceed the body's capacity entirely, are not localized in any organ. Other powers reside in the specific organs adapted to their operations."
},

]

# Write output
with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Wrote {len(data)} refashioned entries to {OUTPUT_PATH}")
