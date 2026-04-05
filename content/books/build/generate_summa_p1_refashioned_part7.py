"""
Generate refashioned versions of Summa Theologica Part I, Q90-Q102.
The creation and original state of man.
"""

import json

data = [
    # ── Q90: Of the First Production of Man's Soul ──
    {
        "index": "90.0",
        "refashioned": "Having covered creation in general, we turn to the creation of humanity specifically. Four topics: (1) the production of man himself, (2) the purpose of that production, (3) the first man's condition, and (4) his dwelling place. On the production of man, three sub-topics: the soul, the body, and the woman. On the soul, four questions: Was it made, or part of God's substance? Was it created from nothing? Was it made directly by God or through angels? Was it made before the body?"
    },
    {
        "index": "90.1",
        "refashioned": "The human soul is not a piece of God. This claim sounds flattering, but it falls apart immediately. The soul sometimes lacks understanding. It acquires knowledge gradually from external things. It has multiple distinct powers. None of this is compatible with the divine nature, which is pure actuality, receives nothing from outside itself, and admits no internal variety.\n\nThe error has deep roots. Early thinkers, unable to conceive of anything beyond the physical, assumed God was a body and the soul was made of the same stuff. The Manichaeans thought God was light and the soul a trapped fragment of it. Later thinkers who recognized incorporeal realities still made the mistake of treating the soul as part of a single cosmic soul, unable to distinguish different levels of spiritual existence.\n\nAll these views have already been refuted. The soul is not God's substance. When Genesis says God \"breathed\" life into man, this is not literal exhalation but the act of making a spirit. And though the soul is a simple form, it is not pure act like God; it has existence only by participation, not by its own essence. God and the human mind are genuinely diverse, not different versions of the same thing."
    },
    {
        "index": "90.2",
        "refashioned": "The rational soul can only come into existence through creation, not through any natural process of generation. Here is why: the way something is made must correspond to the way it exists. Only substances that subsist in their own right are truly \"made\" in the full sense. Non-subsistent forms (like whiteness or shape) do not come into being on their own; they come into being only when the composite thing they belong to is produced.\n\nThe rational soul is different from other forms because it subsists independently. It is not merely the form of a body in the way heat is a quality of fire. Because it subsists, it can properly be said to exist and therefore to be made. And since it cannot be made from pre-existing matter (whether physical, which would make it a body, or spiritual, which would mean one spiritual substance morphing into another), it can only exist through creation from nothing.\n\nThis does not apply to other forms. The rational soul is unique in being both a form and a subsistent being."
    },
    {
        "index": "90.3",
        "refashioned": "God produces rational souls directly, without angelic intermediaries. The reasoning is straightforward: the soul can only come into existence through creation, and only God can create. Every secondary cause works by transforming something that already exists, but creation means producing something from nothing. Since the rational soul cannot be produced by transforming pre-existing matter, no created power, however elevated, can produce it. Angels can rearrange and transform existing material, but they cannot create from nothing. Therefore, every rational soul is the immediate work of God."
    },
    {
        "index": "90.4a",
        "refashioned": "Was the soul created before the body? Origen thought all souls were created simultaneously with the angels, before any bodies existed, because he believed all spiritual substances are naturally equal and only differ by merit. Augustine tentatively suggested the soul of the first man might have been created with the angels and then later joined to the body by its own will, but he explicitly declined to assert this.\n\nThe answer depends on what the soul is. If the soul were a complete being that merely administers the body from outside, pre-existence would be conceivable. But the soul is the body's form and naturally a part of human nature. A soul without a body is an incomplete human nature. God created the first things in their complete natural state. Therefore, it would have been unfitting for the soul to be created without the body.\n\nThe soul was not made before the body. It was created together with it, as its natural completion."
    },
    {
        "index": "90.4b",
        "refashioned": "If the soul were a complete species on its own, it could have been created separately. But as the form of the body, it was necessarily created in the body, not apart from it. The fact that the soul survives the body's death does not prove it existed before the body; death is a defect that came later, not part of the original design."
    },
    # ── Q91: The Production of the First Man's Body ──
    {
        "index": "91.0",
        "refashioned": "Four questions about the first human body: (1) What was it made from? (2) Who made it? (3) Was it well-designed? (4) How does Scripture describe its production?"
    },
    {
        "index": "91.1a",
        "refashioned": "The human body was fittingly made from earth. God is simply perfect, containing all things within Himself as effects pre-exist in their cause. Angels reflect this perfection by knowing all natural things. Humans reflect it in a lower way: by being composed of all things. The rational soul belongs to the genus of spiritual substances. The body's balanced temperament resembles the stability of celestial bodies. And the body contains all four elements in their very substance.\n\nThe higher elements, fire and air, dominate in power (life requires heat and moisture), but the lower elements, earth and water, dominate in quantity, because the less powerful elements must be present in greater proportion to maintain equilibrium. Earth and water mixed together are called \"slime\" or \"clay.\" This is why man is called a \"little world\": every level of creation is represented in him."
    },
    {
        "index": "91.1b",
        "refashioned": "Why not make the body from nothing, to show God's power more dramatically? Because God's power was already shown in creating matter from nothing; the body itself was fittingly composed of all four elements so man would have something in common with every level of physical creation. Why not from a celestial substance? Because celestial matter is impassible and cannot form the sense organs the rational soul needs. Why not mainly from the nobler elements, fire and air? Because if they dominated in quantity as well as power, they would overwhelm the mixture and destroy the equilibrium the sense of touch requires. Touch is the foundation of all the other senses, and its organ must be a balanced mean between the qualities it perceives."
    },
    {
        "index": "91.2a",
        "refashioned": "The first human body was produced directly by God, not through any created intermediary. Forms in matter are only produced when one composite generates another composite of the same kind. No pre-existing human body existed to generate the first one. Angels cannot create new forms from scratch; they can only work with what already exists, using something like a seed. God alone, being absolutely immaterial, can produce form in matter without needing a preceding material form. Since there was no prior human body to serve as a template for natural generation, God alone could have formed the first one.\n\nThis does not mean angels played no role at all. God may have used them as ministers in subsidiary tasks, just as they will assist at the resurrection by gathering dust. But the actual formation of the first human body required divine creative power."
    },
    {
        "index": "91.2b",
        "refashioned": "The claim that celestial bodies could have produced man is too ambitious. Perfect animals cannot arise from celestial influence alone. Even the Philosopher's dictum that \"man and the sun beget man\" only means celestial power cooperates with natural generation, not that it replaces it. The production of a human body from earth is not a natural change driven by celestial motion; it is a supernatural act of divine power, like raising the dead."
    },
    {
        "index": "91.3a",
        "refashioned": "The human body is excellently designed, not in an absolute sense, but relative to its purpose: serving as the instrument of a rational soul. Every artist designs for the intended function, not for abstract perfection. A saw is made of iron, not glass, even though glass is more beautiful. God fashioned the human body as the best possible instrument for rational life. Any apparent deficiencies are necessary trade-offs required by the body's material conditions.\n\nThe body's immediate purpose is the rational soul and its operations. Matter exists for the sake of form, and instruments exist for the sake of the agent who uses them. The human body is shaped to serve thought, not the other way around."
    },
    {
        "index": "91.3b",
        "refashioned": "Why do some animals have sharper senses or faster movement? Because the human body is optimized for a different priority: the most balanced temperament of any animal, which is what touch (the foundation of all senses) requires. Man has the largest brain relative to body size, both for the interior cognitive powers that support intellectual activity and to cool the considerable heart-heat required for upright posture. That large, moist brain weakens smell, which requires dryness. Similar trade-offs explain why some animals see or hear more acutely.\n\nWhy no natural armor, claws, or thick hide? These come from an excess of the earthy element, which would upset human temperament. Instead, man has reason and hands, which Aristotle calls \"the instrument of instruments.\" Through these, man can fashion an unlimited variety of tools, weapons, and clothing, something far more powerful than any fixed biological equipment. A rational nature capable of conceiving infinite solutions needs an instrument capable of infinite adaptation.\n\nWhy upright posture? Four reasons. First, human senses serve knowledge, not just survival. An upright face can freely survey heaven and earth, gathering the raw material for understanding. Second, the brain, where interior cognitive activity occurs, is elevated above the other organs. Third, if man were prone, the hands would be locked into the role of forefeet, losing their universal utility. Fourth, a prone posture would require a protruding mouth with thick, hard lips and tongue, making speech, reason's proper instrument, impossible.\n\nMan's orientation is also significant: his head faces the heavens, his feet face the earth. Plants are inverted (roots as mouth, pointing down). Animals are horizontal. Man alone is properly aligned between the higher and lower worlds."
    },
    {
        "index": "91.4",
        "refashioned": "Does Scripture's account of creating man fit the theology? Yes, on every count. The special language (\"Let us make man\") signals not that God needed help, but that human creation received special deliberation, reflecting the plurality of divine Persons whose image is most clearly expressed in man. The \"breathing\" of life into the face is not a separate act from making the body; it explains what makes the body alive. The soul is the form of the body, and the face is mentioned because that is where vital operations are most visible through the senses.\n\nBody and soul were not produced sequentially. It would be unfitting for God to make a body without a soul or a soul without a body, since each is only a part of human nature, and the body depends on the soul rather than the reverse. The mention of \"male and female\" alongside \"the image of God\" does not mean the image resides in sex; it means the image (which is in the mind, where there is no sexual distinction) belongs to both sexes equally."
    },
    # ── Q92: The Production of the Woman ──
    {
        "index": "92.0",
        "refashioned": "Four questions about the creation of woman: (1) Should woman have been made in the original creation? (2) Should she have been made from man? (3) From his rib specifically? (4) Was she made directly by God?"
    },
    {
        "index": "92.1a",
        "refashioned": "Woman was necessary, but specifically as a partner in generation, not as a general helper. For any other kind of work, another man would have been more efficient. The distinction between male and female follows from the logic of living things.\n\nIn the simplest organisms, reproductive power is built into every individual. In plants, male and female functions are permanently united. In perfect animals, the active and passive generative powers are separated into male and female because animal life has higher activities than reproduction. The sexes need not be permanently joined; they unite only for the act of generation. In humans, the separation is even more pronounced because human life is ordered to something higher still: intellectual activity. The female was therefore produced separately from the male, though they are united in the flesh for generation."
    },
    {
        "index": "92.1b",
        "refashioned": "Aristotle's claim that the female is a \"defective male\" applies only at the level of individual generation, where the male seed aims to produce a male likeness and sometimes fails due to material factors. At the level of nature's universal intention, which depends on God, woman is not defective at all but is deliberately included for the work of generation.\n\nAs for subjection: there are two kinds. Servile subjection, where the superior exploits the subject for his own benefit, only began after sin. But ordered governance, where the more capable direct others for the common good, would have existed even in innocence. Any community requires leadership, and natural differences in judgment would have made some kind of governance necessary. Inequality is not inherently a punishment.\n\nThe objection that God should not have made woman because He foresaw she would occasion sin proves too much. If God removed everything that would become an occasion of sin, the universe would be imperfect. The common good is not sacrificed to prevent individual evil."
    },
    {
        "index": "92.2",
        "refashioned": "It was fitting that woman be made from man rather than independently. Four reasons. First, it gave the first man a dignity parallel to God's: as God is the principle of the whole universe, the first man was the principle of the whole human race. Second, it deepened the bond between man and woman. Knowing she came from him, man would love her more closely and cleave to her, as Genesis says. This was especially important for humans, who unlike other animals live together for life. Third, human marriage serves not only reproduction but domestic partnership, where each has a distinct role. The woman coming from man as her principle reflects this ordered partnership. Fourth, there is a sacramental dimension: the Church originates from Christ, as woman originated from man.\n\nThe objection that male and female should share the same material origin (both from earth) misses the point. Nature works from determinate matter in determinate ways. Divine power, being infinite, can produce the same species from any matter."
    },
    {
        "index": "92.3",
        "refashioned": "Why from the rib specifically? To symbolize the social union of man and woman. She was not made from his head, because she should not dominate him. She was not made from his feet, because she should not be treated with contempt as a slave. She was made from his side, signifying partnership. There is also a sacramental meaning: from the side of Christ on the cross flowed blood and water, the sacraments on which the Church was established.\n\nAs for the physics: the rib was not simply stretched. Additional matter was created or converted by divine power, analogous to how Christ multiplied loaves by transforming nourishment, not by stretching bread. The rib belonged to Adam's perfection not as an individual but as the principle of the human race, much as seed belongs to the perfection of the one who generates. Its removal caused no pain because pain belongs to the fallen state."
    },
    {
        "index": "92.4",
        "refashioned": "Woman was formed directly by God. In natural generation, an individual of a species is produced from determinate matter by the specific power of that species. Human beings are naturally generated from human seed. Producing a human being from anything other than the normal material (whether from earth for the man or from a rib for the woman) exceeds the capacity of any created power. Only the Author of nature can produce effects outside nature's ordinary course. Angels may have assisted in subsidiary ways, but the actual formation was God's direct work."
    },
    # ── Q93: The End or Term of the Production of Man ──
    {
        "index": "93.0",
        "refashioned": "The purpose of human creation is that man is made \"to the image and likeness of God.\" Nine questions: (1) Is God's image in man? (2) In irrational creatures? (3) More in angels than in man? (4) In every person? (5) Does the image reflect the Trinity or just the divine essence? (6) Is it in the mind only? (7) In the soul's acts or its powers? (8) Only in relation to God as its object? (9) How do \"image\" and \"likeness\" differ?"
    },
    {
        "index": "93.1",
        "refashioned": "There is an image of God in man, but an imperfect one. An image requires two things: likeness and derivation. An egg resembles another egg but is not its image, because it was not copied from it. A reflection in a mirror is an image because it is derived from the original. Equality is not required for an image to exist, though a perfect image would lack nothing found in the original.\n\nMan has a genuine likeness to God, derived from God as exemplar. But the likeness is not one of equality; the exemplar infinitely exceeds the copy. This is why Scripture says man was made \"to\" God's likeness, with the preposition signaling approach from a distance. The image is not in man's bodily shape but in his spiritual nature. Whereas Christ is simply \"the Image\" of the Father (being of identical nature), man is \"to the image\" (being of an analogous, not identical, nature)."
    },
    {
        "index": "93.2",
        "refashioned": "The image of God is found only in intellectual creatures, not in animals or inanimate things. A generic resemblance or a shared accidental quality is not enough for an image; what is needed is likeness in species, or at least in the defining characteristic. Things resemble God in three ascending degrees: by existing, by living, and by understanding. Only the last approaches close enough to count as an image.\n\nAll creatures participate in some likeness to God, but only intellectual creatures have the specific likeness that constitutes an image. A worm may come from a man but is not his image, because the resemblance is too generic. Similarly, the beauty of the whole universe does not make the universe an image of God in the relevant sense. The image is found where God's defining characteristic, intellect, is specifically imitated."
    },
    {
        "index": "93.3",
        "refashioned": "Angels bear God's image more perfectly than humans do, because the image consists primarily in intellectual nature, and angelic intellect is superior to human intellect.\n\nThere are secondary respects in which man resembles God more than angels do: man proceeds from man as God proceeds from God; the whole soul is in the whole body as God is present to the whole world. But these secondary resemblances only count as aspects of the divine image if the primary likeness (intellectual nature) is already present. Otherwise even animals would qualify. Since the primary criterion is intellectual nature, and angels excel in this, angels are more to God's image absolutely speaking, even though man surpasses angels in certain secondary respects."
    },
    {
        "index": "93.4",
        "refashioned": "The image of God exists in every human being, because every person has an intellectual nature. But the image operates at three levels. First, every person has the natural capacity to understand and love God; this is the image of creation, shared by all. Second, those who actually know and love God through grace possess the image of re-creation, found only in the just. Third, those who know and love God perfectly possess the image of glory, found only in the blessed.\n\nBoth men and women bear the image equally. Genesis says \"to the image of God He created him; male and female He created them\" precisely to show the image belongs to both sexes, since it resides in the mind, where there is no sexual distinction."
    },
    {
        "index": "93.5a",
        "refashioned": "Does the image of God in man reflect the Trinity of Persons, or only the divine essence? Some argue it must reflect only the unity of essence, since what the image imitates (eternity, intelligence, free will, goodness) belongs to the one divine nature, not to the distinction of Persons. Others worry that if the image reflected the Trinity, we could know the Trinity by natural reason alone, which is false.\n\nAgainst this, Hilary argues that the very plurality of Persons is confirmed by the fact that man is made \"to the image of God\" using plural language."
    },
    {
        "index": "93.5b",
        "refashioned": "The image reflects both the divine nature and the Trinity. The distinction of divine Persons follows from the divine nature (being distinguished by relations of origin that are suited to that nature). So imitating the divine nature does not exclude representing the Persons; in fact, one follows from the other.\n\nThe objection that this would make the Trinity knowable by natural reason fails because the image in us is deeply imperfect. As Augustine says, we see the trinity within ourselves but only believe the Trinity in God. The gap between our interior life of thought and love and the divine processions is vast enough that the image does not deliver demonstrative knowledge of the Trinity."
    },
    {
        "index": "93.6a",
        "refashioned": "Is the image of God found in the whole person or only in the mind? Paul says \"the man\" is God's image. Genesis ties the image to the creation of male and female. Shape seems relevant to images. And there are trinities in sense experience and imagination, not just in intellect.\n\nAgainst these, Paul also says renewal \"according to the image\" consists in putting on the new man in the spirit of the mind. The image belongs to the mind specifically."
    },
    {
        "index": "93.6b",
        "refashioned": "The image of God is in the mind alone. In other creatures, and in the non-rational parts of the human being, we find only a \"trace\" of God, not an image. The difference: an image represents by likeness in species; a trace represents the way an effect points to a cause without reaching specific likeness (footprints trace an animal, ashes trace a fire).\n\nRational creatures achieve a representation of species because they imitate God not only in being and living but in understanding. Other creatures show only traces of the intellect that created them. Similarly, in rational creatures we find a procession of word from intellect and love from will that mirrors, however imperfectly, the procession of the Word from the Father and Love from both. In non-rational creatures, we find only traces of these processions: their finite nature points to a principle, their species points to a designing word, their ordered purpose points to the maker's love. In the human body and senses, the likeness to God is by trace. In the mind, it is by image."
    },
    {
        "index": "93.6c",
        "refashioned": "The image of God is not in every part of man but is impressed on his mind, as a coin bears the image of a king without every part of the coin being the image. The distinction of male and female does not constitute the image; Scripture mentions both sexes immediately after mentioning the image precisely to show the image belongs to both, since it is in the mind where there is no sexual distinction.\n\nThe human body's upright shape does not contain the image but represents it by way of trace, pointing toward the image in the soul. And the trinities found in sensory and imaginary vision fall short of the divine image because their components are external or adventitious to the soul, unlike the mind's own acts of understanding and love, which more closely mirror the divine processions."
    },
    {
        "index": "93.7a",
        "refashioned": "The image of the Trinity is found primarily in the soul's acts, not just in its powers or habits. The divine Persons are distinguished by the procession of Word from Speaker and Love from both. In us, a word cannot exist without actual thought. Therefore the image is most fully present when we actually think and from that thinking produce an interior word, and from both break forth into love.\n\nPowers and habits are the principles from which acts flow. Since acts virtually exist in their principles, the image can be considered secondarily as existing in the powers, and even more in the habits. But the primary locus is the act itself."
    },
    {
        "index": "93.7b",
        "refashioned": "Augustine's trinities of mind-knowledge-love and memory-understanding-will both point to the image, with the latter being more precise because it distinguishes functions more clearly. The key insight is that the image resides most fully in actual thought and actual love, not merely in the habitual retention of knowledge. Memory, understanding, and will as Augustine uses them are not three separate powers but three aspects of the mind's activity.\n\nThe objection that an act does not always remain (while the image should be permanent) is handled by noting that even when not actively thinking, the soul always remembers, understands, and loves itself habitually. The image exists permanently in the habits and powers as principles, and fully when those principles are activated."
    },
    {
        "index": "93.8a",
        "refashioned": "The image of God in the soul is most properly found when the mind turns toward God, not when it contemplates any random object. Different objects produce specifically different words and loves in the mind. The Word of God is born of God's self-knowledge, and divine Love proceeds from God's self-love. So the truest image in us is the word born of knowing God and the love proceeding from that knowledge.\n\nThis does not mean the image disappears when we think about other things. The mind's capacity to turn toward God is itself a permanent natural feature. And when the mind knows itself, it indirectly mirrors God, since self-knowledge is a stepping stone to knowing the God who made it. But the image is most fully realized in direct knowledge and love of God.\n\nKnowledge of temporal things, while it involves trinitarian structure (species, vision, intention), does not constitute the image properly, because such knowledge is adventitious and directed at objects beneath the mind. The image requires the mind to engage with what is above it."
    },
    {
        "index": "93.8b",
        "refashioned": "For the image to hold, what proceeds must be a word of God proceeding from knowledge of God. A mere trinity of cognitive elements about any object is not enough.\n\nThe knowledge that constitutes the image can be either natural (the mind's innate capacity to know God through reason) or gracious. Even when the image is \"obsolete\" in those without reason's use, \"obscured\" in sinners, or \"clear\" in the just, it never fully vanishes because the natural aptitude to know God always remains.\n\nIn the beatific vision, even temporal things will be seen in God and through God's unchangeable truth. At that point, the contemplation of all things will belong to the image, because everything will be known through the divine Word."
    },
    {
        "index": "93.9a",
        "refashioned": "\"Likeness\" and \"image\" are not redundant terms. Likeness is broader than image: wherever there is an image there is likeness, but not vice versa. The two can be distinguished in two ways.\n\nFirst, likeness as a preamble to image. Here likeness covers the more general features (incorruptibility of the soul, for instance) while the image proper is found specifically in the intellectual nature. In this sense, the mind is to God's image, while the body and lower faculties bear God's likeness as a trace.\n\nSecond, likeness as the perfection of image. Here likeness signifies how well the image succeeds. An image is \"like\" its original when the representation is good and \"unlike\" when it falls short. In this sense, likeness adds a qualitative dimension: specifically, likeness of power and virtue. The image gives you the structure (intellect, will, self-movement); the likeness of virtue tells you how well that structure is being used."
    },
    {
        "index": "93.9b",
        "refashioned": "Likeness is not distinct from image in the general sense (since every image involves likeness) but in the specific sense: either as falling short of the image (covering features too general to constitute the image proper) or as perfecting it (indicating the quality of the image's realization). The soul's essence belongs to the image insofar as it represents the divine essence in intellectual nature, not in generic features like simplicity or indissolubility. Natural seeds of virtue in the soul can ground a natural \"likeness,\" and the two terms can apply to different aspects of the same reality. Love of the word (knowledge loved) belongs to image; love of virtue belongs to likeness."
    },
    # ── Q94: Of the State and Condition of the First Man as Regards His Intellect ──
    {
        "index": "94.0",
        "refashioned": "We now consider the first man's condition, starting with his intellect. Four questions: (1) Did he see God's essence? (2) Could he see angels directly? (3) Did he possess all knowledge? (4) Could he be deceived?"
    },
    {
        "index": "94.1a",
        "refashioned": "The first man did not see God in His essence. The proof is simple: anyone who sees God's essence possesses beatitude, and no one possessing beatitude can willingly turn away from God, because beatitude is what everyone necessarily desires. Since Adam sinned, he could not have been seeing God's essence.\n\nBut Adam knew God more perfectly than we do now, in a way midway between our current knowledge and the beatific vision. We know God through sensible creatures, and our engagement with the sensible world distracts us from purely intelligible contemplation. In Adam, the lower powers were perfectly subject to reason, and reason was not dragged down by sensory preoccupation. He could contemplate God's intelligible effects clearly and steadily, receiving a kind of direct illumination from the First Truth. His knowledge was not the beatific vision, but it was far clearer than anything we achieve in our present distracted condition."
    },
    {
        "index": "94.1b",
        "refashioned": "Adam was happy in paradise, but not with the final happiness of seeing God's essence. He had a natural perfection and integrity that constituted a genuine, if incomplete, blessedness. His good will was well-ordered precisely because it did not desire the final reward before the time of merit had been completed. He knew God without the obscurity caused by sin (where sensory preoccupation clouds intellectual vision) but not without the inherent limitation of knowing God through creatures rather than directly."
    },
    {
        "index": "94.2a",
        "refashioned": "Could Adam see angels in their essence? No, and for a principled reason. The human soul, even in the state of innocence, was adapted to govern the body and therefore naturally understood by turning to images derived from sense experience. This mode of knowing proceeds in three stages: the soul turns from external things to concentrate on itself, then rises toward association with higher intelligences, then ascends toward God.\n\nThe first stage yields genuine self-knowledge. But the second stage does not yield direct knowledge of angels, because angelic understanding operates on entirely different principles than ours. Knowing how we ourselves think does not tell us what it is like to think as an angel does. The third stage falls even shorter of knowing God directly.\n\nAdam knew the angels better than we do, because his intellectual life was clearer and less obstructed. But \"better\" does not mean \"directly.\" He had a more excellent apprehension of intelligible realities, but the gap between human and angelic cognition remained."
    },
    {
        "index": "94.2b",
        "refashioned": "Innocence did not change the soul's fundamental nature or mode of operation. The state of innocence differs from our current state not by giving the soul a different kind of existence but by removing corruption while preserving natural integrity. The soul still understood by turning to sense-derived images. Adam's limitation in knowing angels was not because his body weighed down his soul (as ours does now) but because the soul's natural cognitive object simply falls short of angelic reality. We have both obstacles; Adam had only the second."
    },
    {
        "index": "94.3",
        "refashioned": "Adam possessed knowledge of everything humans have a natural aptitude to know, plus the supernatural truths necessary for directing human life. The reasoning: perfection precedes imperfection in the natural order, as act precedes potentiality. God created things not only for themselves but as principles of other things. Since Adam was to be the father and teacher of the entire human race, he needed comprehensive knowledge from the start.\n\nThis included everything virtually contained in self-evident principles (the full range of natural knowledge) and enough revealed truth to direct human life toward its supernatural end. What he did not know were things that exceed human capacity and are unnecessary for life's direction: other people's private thoughts, future contingent events, trivial individual facts.\n\nThis knowledge came through divinely infused species, but it was not different in kind from natural knowledge, just as miraculously given eyes are not different from natural ones. Adam would have advanced in natural knowledge, not by learning new truths but by experiencing practically what he already knew theoretically. In supernatural knowledge, he would have advanced through further revelation."
    },
    {
        "index": "94.4a",
        "refashioned": "Could Adam have been deceived? No. As long as the state of innocence persisted, it was impossible for the human intellect to assent to falsehood. Truth is the good of the intellect; falsehood is its evil. In a state where no evil could exist (because sin was absent), no false judgment could exist either.\n\nThe deeper reason is structural. The rectitude of the original state meant the soul was subject to God, and the lower faculties were subject to reason. Deception in the intellect never comes from the intellect itself (which, regarding its proper object, is always true) but from interference by lower faculties like imagination. When reason's natural judgment is free and undistorted, we are not deceived by phantasms, as we see from the fact that waking people are not fooled by dream-images. In the state of innocence, reason was fully free.\n\nSome argued Adam could have been deceived in matters beyond his knowledge, as long as he did not firmly assent. But this is inconsistent with the integrity of the original state. Even a tentative entertaining of falsehood would be an evil of the intellect, incompatible with a condition where no evil existed."
    },
    {
        "index": "94.4b",
        "refashioned": "The woman was deceived before she sinned outwardly, but not before she had already sinned inwardly through pride. She could not have believed the serpent unless she had already given in to the love of her own power. As for the serpent speaking, she may have thought it had received this ability supernaturally, not naturally.\n\nIf something false had been presented to Adam's senses or imagination, his reason would have judged correctly. He was not accountable for what might occur during sleep, since reason is not operative then. If someone had told him something false about future events or secret thoughts, he would not have believed it was true but might have considered it possible, which is not a false opinion. In every case, either reason would have corrected the error, or divine guidance would have prevented it. After he had already sinned in his heart, that guidance was forfeit."
    },
    # ── Q95: Of Things Pertaining to the First Man's Will ──
    {
        "index": "95.0",
        "refashioned": "Two topics under the first man's will: (1) grace and righteousness, (2) dominion over other things. On grace and righteousness, four questions: (1) Was man created in grace? (2) Did he have passions? (3) Did he have all virtues? (4) Were his actions less meritorious than ours?"
    },
    {
        "index": "95.1a",
        "refashioned": "The first man was created in grace, not in a state of mere nature. The argument is structural. The rectitude of the original state consisted in reason being subject to God, the lower powers subject to reason, and the body subject to the soul. The first subjection was the cause of the other two. When reason lost its subjection to God through sin, the lower powers immediately rebelled against reason, as Augustine notes: they \"felt the impulse of disobedience in the flesh, as though it were a punishment corresponding to their own disobedience.\"\n\nNow, the subjection of the lower powers to reason was clearly not natural; otherwise it would have survived sin (natural gifts remained even in fallen angels). Therefore the primary subjection of reason to God, which caused it, was also not natural but supernatural, a gift of grace. An effect cannot exceed its cause. If the loss of grace dissolved the lower powers' obedience, then grace must have been what sustained it. Therefore man was created with grace from the first moment."
    },
    {
        "index": "95.1b",
        "refashioned": "Paul's contrast between Adam as \"living soul\" and Christ as \"life-giving spirit\" refers to the body's mode of life, not the soul's spiritual condition. Adam had spiritual life in his soul (grace) but not the glorified spiritual body that Christ inaugurates. Augustine clarifies that Adam possessed the Holy Spirit to some degree, though not in the way the faithful do now, who are admitted to eternal happiness directly after death.\n\nThe objection that God wanted to show what free will could do before grace was given misunderstands Augustine's point: God showed what free will could do before being confirmed in grace, not before receiving grace at all. And while man was created in grace, it was by virtue of that grace, not the nature in which he was created, that he could advance by merit."
    },
    {
        "index": "95.2",
        "refashioned": "Adam had passions in the state of innocence, but only certain kinds and in a distinctive way. He had no passions directed toward present or imminent evil (like fear or sorrow), because no evil was present or threatening. He had no burning concupiscence for goods not yet possessed. But he did have passions directed toward present good (joy and love) and future good expected at the proper time (measured desire and hope).\n\nThe crucial difference: in our current state, passions often run ahead of reason or resist it, because the sensory appetite is not fully subject to rational control. In Adam, the lower appetite was entirely governed by reason. Passions arose only as consequences of rational judgment, never as disruptions of it. This was not the absence of passion but its perfect ordering. As Aristotle notes, virtue does not eliminate desire; the temperate person desires what is appropriate, in the appropriate way."
    },
    {
        "index": "95.3a",
        "refashioned": "Adam possessed all the virtues, but in a nuanced way. The rectitude of the original state required that reason be subject to God and the lower powers to reason. Virtues are precisely the perfections that accomplish this ordering. So Adam necessarily had every virtue.\n\nBut a distinction is needed. Virtues that involve no inherent imperfection (like charity and justice) existed fully, both as habits and in act. Virtues that imply imperfection compatible with innocence also existed in both habit and act: faith (of things not yet seen) and hope (of beatitude not yet possessed), since Adam did not yet have the beatific vision.\n\nVirtues that imply imperfection incompatible with innocence existed only as dispositions, not in act. Penance (sorrow for sin committed) and mercy (sorrow for another's suffering) could not be exercised where there was no sin or suffering. But Adam was so disposed that he would have repented if there had been cause, and would have helped anyone in need if need had existed. Think of how a virtuous person would feel ashamed if they did something wrong, even though they never do. The disposition is real; only the occasion is absent."
    },
    {
        "index": "95.3b",
        "refashioned": "Temperance and fortitude do not essentially require excessive passions to subdue; they are per se competent to moderate passions of any intensity. In innocence, they operated on well-ordered passions rather than disordered ones.\n\nPassions regarding evil in another (like hating the demons' malice) were compatible with innocence. So virtues related to such passions could exist fully. Passions regarding evil in the same subject (like sorrow over one's own suffering) were incompatible with innocence, so virtues exclusively related to these existed only as habits.\n\nAdam had perseverance as a virtue (the habitual choice to continue in good) but not perseverance as an uninterrupted fact (since he eventually fell). Faith existed because the perfection of innocence did not include the beatific vision."
    },
    {
        "index": "95.4",
        "refashioned": "Were Adam's actions less meritorious than ours? Merit can be measured two ways: by its root (grace and charity) and by the degree of the action itself (either absolutely or proportionally).\n\nBy the root of grace, Adam's works were more meritorious. His grace met no obstacle in human nature and would have been more copious. Absolutely, his works were also greater because his virtue was greater. But proportionally, our works may merit more, because a small deed done with great difficulty exceeds our capacity more dramatically than a great deed done easily exceeds the capacity of someone strong.\n\nThe bottom line: Adam's advantage was absolute; ours is relative. We need grace for more things (remission of sin, support in weakness) but not more grace. Difficulty and struggle increase proportional merit and can satisfy for sin, but they do not prove our actions are simply more meritorious. Adam had no interior impulse toward evil, so he could resist temptation more easily, even without grace."
    },
    # ── Q96: Of the Mastership Belonging to Man in the State of Innocence ──
    {
        "index": "96.0",
        "refashioned": "Four questions about human dominion in the state of innocence: (1) Was man master over the animals? (2) Over all creatures? (3) Were all people equal? (4) Would some have governed others?"
    },
    {
        "index": "96.1a",
        "refashioned": "Before sin, all animals were subject to man. Three arguments. First, natural order: the imperfect exists for the use of the perfect. Plants use earth, animals use plants, and man uses both. Dominion over animals is the natural culmination of this hierarchy. Second, divine providence: God governs inferior things through superior ones. Man, made in God's image, is the natural governor of animals. Third, the gap between human and animal cognition: animals have particular instinctive prudence regarding specific situations, while man has universal practical reason covering all situations. Whatever is partial is naturally subject to what is universal.\n\nBefore sin, man had not forfeited this natural authority through disobedience. As punishment for disobeying God, creatures that should have been subject to man disobeyed him in turn. The disorder we see now, animals fleeing or attacking humans, is the consequence, not the original condition."
    },
    {
        "index": "96.1b",
        "refashioned": "Angels may have helped gather animals to Adam for naming, not because man lacked authority but because angels naturally have greater power over certain material tasks. Predatory animals were always predatory (sin did not change animal nature) but remained subject to man's governance nonetheless, much as domesticated predators today serve human purposes. Lions did not eat grass before the Fall.\n\nIn innocence, man had no bodily need of animals (no need for clothing, transport, or animal food) but used them for knowledge, studying their natures. Animals would have obeyed man voluntarily through their natural participation in instinctive prudence, as domestic animals obey their human masters now."
    },
    {
        "index": "96.2",
        "refashioned": "Man's dominion over creation corresponded to his dominion over himself. He contains all levels of reality: reason (shared with angels), sensation (shared with animals), vegetative life (shared with plants), and material body (shared with inanimate things).\n\nOver angels, man had no authority, since reason is not their master but their peer or inferior. Over animals, man ruled by command, since the sensitive powers obey reason to some degree. Over plants and inanimate things, man ruled not by commanding but by using, since vegetative processes and material nature do not obey commands but can be employed without hindrance. Man had no power to alter the course of celestial bodies; that belongs to God alone."
    },
    {
        "index": "96.3",
        "refashioned": "Perfect equality would not have existed even in innocence. At minimum, there would have been diversity of sex (required for generation) and age (since children would be born over time). Beyond these, free will would have produced differences in virtue and knowledge, since people would have applied themselves to varying degrees. Even bodies would have differed in robustness, beauty, and size, since the human body was still subject to natural laws and influenced by climate, nutrition, and other factors.\n\nBut none of these inequalities would have involved defect or fault. The differences would have been in degree of perfection, not between perfection and imperfection. Order requires inequality; as Augustine says, order arranges equal and unequal things in their proper place. The beauty of ordered diversity was part of God's design, not a punishment."
    },
    {
        "index": "96.4",
        "refashioned": "There are two kinds of authority. The first is servile: one person uses another for his own benefit. This kind of dominion only began after sin and is inherently grievous, since no one willingly yields what should be his own. In innocence, this kind of mastership could not have existed.\n\nThe second is governance for the common good: directing free people toward their own welfare and the welfare of the community. This kind of authority would have existed even in innocence, for two reasons. First, man is naturally social, and any social group requires someone to attend to the common good. Many individuals, left to themselves, pursue many different ends; one person looking after the common interest is essential to organized life. Second, differences in knowledge and virtue would have existed, and it would have been wasteful for these advantages not to benefit others.\n\nAs Augustine says, just men command not through love of domination but through the service of counsel. Leadership in innocence would have been an act of service, not exploitation."
    },
    # ── Q97: Of the Preservation of the Individual in the Primitive State ──
    {
        "index": "97.0",
        "refashioned": "Four questions about the first man's bodily condition: (1) Was he immortal? (2) Was he impassible? (3) Did he need food? (4) Would the tree of life have given immortality?"
    },
    {
        "index": "97.1",
        "refashioned": "Man in the state of innocence was immortal, but not by nature. His body was not intrinsically incorruptible like an angel (which has no matter) or a celestial body (whose matter admits only one form). Rather, God gave the soul a supernatural power to preserve the body from all corruption, so long as the soul remained subject to God.\n\nThis makes theological sense: the rational soul surpasses the capacity of corporeal matter, so it was fitting that it received a power surpassing what matter could naturally sustain. When that supernatural gift was forfeited through sin, the body's natural corruptibility reasserted itself. Death entered through sin, not through nature.\n\nThis immortality was different from the immortality of glory promised as a reward. The original immortality was conditional, maintained by supernatural grace as long as obedience continued. The promised immortality of glory is permanent and absolute."
    },
    {
        "index": "97.2",
        "refashioned": "\"Passion\" has two senses. In the broad sense, any change counts (including sensation and sleep). In the strict sense, passion means being altered away from your natural disposition. Adam was passible in the broad sense (he could sense, sleep, and undergo natural processes) but impassible in the strict sense. No change contrary to his natural well-being could affect him, just as no corruption leading to death could occur. He could control passion as he could avoid death, so long as he refrained from sin.\n\nHis body was protected from external harm partly by his own reason (avoiding dangerous situations) and partly by divine providence, which ensured nothing harmful came upon him unexpectedly. The removal of the rib for Eve's creation was not a natural deterioration but was analogous to seminal emission: material provided for the generation of the species, not a loss to the individual."
    },
    {
        "index": "97.3",
        "refashioned": "Adam needed food. His immortality was not intrinsic but sustained by a supernatural power in the soul. Natural heat still consumed the body's moisture, and food was needed to replace what was lost. In the primitive state, man had an animal life requiring nourishment; after the resurrection, he will have a spiritual life needing none.\n\nThe distinction maps onto the soul's dual identity. As \"soul\" (what it shares with other living things), it gives animal life to the body, which requires the vegetative functions of nutrition, growth, and generation. As \"spirit\" (what is unique to it), it will eventually communicate immortality, impassibility, and glory to the body. In innocence, the first mode applied. After resurrection, the second.\n\nNot eating would have been sinful, since God commanded Adam to eat from every tree except the forbidden one. Digestion would have produced waste, which God would have disposed in a way fitting to the state."
    },
    {
        "index": "97.4",
        "refashioned": "The tree of life was a real cause of extended life but not of absolute immortality. The body faced two threats. First, natural heat consuming moisture, remedied by ordinary food from the other trees. Second, the gradual weakening of the body's assimilative power over time (the same process that causes aging: added nutrients progressively dilute the original vital force, as water added to wine eventually overwhelms the wine's character).\n\nThe tree of life addressed this second threat by strengthening the body's vital force against this progressive weakening. But its power was finite. It could preserve the body for a definite period, not forever. After that period elapsed, man would either need to eat from it again or be transferred to the spiritual life.\n\nSo the tree of life was genuinely medicinal but not a source of natural immortality. The soul's supernatural power of preservation remained the primary cause; the tree was a bodily supplement against one specific mode of decay."
    },
    # ── Q98: Of the Preservation of the Species ──
    {
        "index": "98.0",
        "refashioned": "Two questions about reproduction in the state of innocence: (1) Would generation have occurred? (2) Would it have been through sexual union?"
    },
    {
        "index": "98.2a",
        "refashioned": "Generation in the state of innocence would have been through sexual union, not through some alternative angelic or spiritual process. Some early thinkers, troubled by the nature of concupiscence, imagined the human race would have multiplied by divine power alone, without sex. But this is unreasonable. What is natural to man by virtue of his animal life was neither acquired nor lost through sin. Sexual generation is natural to man as an animal, as the design of the body makes obvious. These organs would not have been purposeless before the Fall.\n\nTwo elements must be distinguished. The first is the natural union of male and female, with active and passive generative principles. This belongs to the order of nature and would have existed in innocence. The second is the disordered excess of concupiscence that currently accompanies the act. This is a consequence of the lower powers' rebellion against reason and would not have existed in innocence, when the sensory appetite was fully subject to rational control.\n\nAs Augustine says, the reproductive organs would have been moved by the will like any other limb, without ardent or disordered incentive, with calmness of soul and body."
    },
    {
        "index": "98.2b",
        "refashioned": "The comparison to angels fails: in paradise, man was angel-like in mind but still animal in body. Only after the resurrection will both soul and body be spiritualized. Our first parents did not have intercourse in paradise, either because they were expelled too soon after Eve's creation or because they awaited a specific divine command about timing.\n\nThe claim that sexual union makes man beast-like is precisely backward. What makes sexual behavior bestial is the absence of rational control over concupiscence, not the act itself. In innocence, reason would not have diminished sensory pleasure (indeed, Augustine notes that with purer nature and greater bodily sensitivity, pleasure would have been greater) but would have prevented concupiscence from dominating. A sober person enjoys food no less than a glutton; the difference is that the glutton's appetite controls him.\n\nVirginal integrity would not have been compromised by intercourse in that state. As Augustine says, the union would have been one of deliberate action, not lustful desire, and conception and birth would have been free of the distortions that accompany them now."
    },
    # ── Q99: Of the Condition of the Offspring as to the Body ──
    {
        "index": "99.0",
        "refashioned": "Two questions about children's bodies in the state of innocence: (1) Would infants have had full physical strength from birth? (2) Would all children have been male?"
    },
    {
        "index": "99.1",
        "refashioned": "Children in the state of innocence would not have had full adult physical strength at birth, but they would not have had the helplessness we observe in infants now. Where revelation is silent, we must follow the natural order, and it is natural for human infants to lack strength because of the brain's large size and high moisture content, which impedes the nerves that control movement.\n\nThe original righteousness meant the body could not do anything contrary to the well-ordered will. But a well-ordered will desires only what is appropriate to its stage of life. An infant's will would not desire to perform adult actions. So children would have had enough strength for age-appropriate activities (nursing and the like) but not for everything an adult can do.\n\nThe weakness of infancy is natural and follows from birth, unlike the weakness of old age, which leads to corruption. Since man in innocence was born but not subject to corruption, infantile limitations would have existed but senile decline would not."
    },
    {
        "index": "99.2",
        "refashioned": "Both sexes would have been born in the state of innocence. Diversity of sex belongs to the perfection of human nature, just as different grades of being belong to the perfection of the universe.\n\nAristotle's claim that the female is a \"misbegotten male\" refers only to the individual case, where the male seed aims to produce a male likeness. At the level of universal nature, the generation of females is fully intended. The cause of female births is not defect or failure but natural variation: climatic conditions, celestial influences, and even the parents' own will. In innocence, where the body was more subject to the soul, parents might have been able to determine the sex of their children by will alone.\n\nSince all children would have been born to live animal lives requiring food and generation, all would have needed to reproduce, not just the first couple. This implies roughly equal numbers of males and females."
    },
    # ── Q100: Of the Condition of the Offspring as Regards Righteousness ──
    {
        "index": "100.0",
        "refashioned": "Two questions about children's moral condition: (1) Would they have been born righteous? (2) Would they have been born confirmed in righteousness, unable to sin?"
    },
    {
        "index": "100.1",
        "refashioned": "Children in the state of innocence would have been born in a state of original righteousness, including sanctifying grace. Original righteousness was not an individual trait of Adam's but an endowment of the entire human nature, a gift pertaining to the species. This is clear from the fact that original sin, its opposite, is transmitted precisely as a condition of the nature. If the corruption passes through nature, so would the righteousness have.\n\nThis grace would not have been natural in the sense of being transmitted through biological generation. Rather, God would have conferred it directly on each soul at the moment of its creation, just as the rational soul itself is not transmitted by the parents but infused by God when the body is ready to receive it. The mechanism is parallel: nature provides the body; God provides the soul and its grace."
    },
    {
        "index": "100.2",
        "refashioned": "Children would not have been born confirmed in righteousness. Confirmation in righteousness comes only through the beatific vision: once a rational creature sees God as He is, it cannot turn away, because God is the essence of goodness and nothing is desired except under the aspect of good. But Adam had not yet attained the beatific vision. Had he attained it, his animal life (and with it, the capacity for generation) would have ceased, replaced by the spiritual life. So no children could have been born to parents who were already confirmed.\n\nThis means children, like their parents, could have sinned by their own free will. They would not have inherited the necessity of sinning (as we inherit original sin's effects), but neither would they have been guaranteed sinlessness. Their preservation from sin would have depended on divine providence and their own choices, not on an irrevocable state.\n\nThe angel analogy does not apply: angelic free will becomes fixed after its first choice, while human free will remains changeable throughout mortal life."
    },
    # ── Q101: Of the Condition of the Offspring as Regards Knowledge ──
    {
        "index": "101.0",
        "refashioned": "Two questions about children's knowledge in the state of innocence: (1) Would they have been born with perfect knowledge? (2) Would they have had full use of reason from birth?"
    },
    {
        "index": "101.1",
        "refashioned": "Children would not have been born with perfect knowledge. The soul naturally acquires knowledge through the senses; that is why it is united to a body in the first place. If the soul were fully equipped with knowledge at creation, the body would serve no cognitive purpose, which contradicts the soul-body union's rationale.\n\nAdam's comprehensive knowledge was a special endowment for his unique role as father and teacher of the human race, not a feature of human nature as such. His children would have inherited the natural and gracious features of the species but not his individual privileges. They would have acquired knowledge over time through experience and learning, but more easily and without the obstacles we face.\n\nThis would not have constituted ignorance. Ignorance is the absence of knowledge that should be present at a given time. Children would have possessed whatever knowledge was appropriate to their stage of development. They would have had sufficient knowledge of universal moral principles to act rightly, and this natural moral knowledge would have been more complete than what we possess by nature now."
    },
    {
        "index": "101.2",
        "refashioned": "Children would not have had full use of reason at birth, because the use of reason depends on the sensitive powers, which depend on bodily organs, and in infants the brain's high moisture content impedes neural function. This is a natural condition, not a punishment for sin.\n\nHowever, children in innocence would have had more use of reason than infants do now, relative to the activities appropriate to their age. The general principle holds: nature proceeds from imperfect to perfect, and even in innocence, human development would have followed this trajectory. Some animals can walk at birth, but this reflects simpler neural requirements, not greater perfection. The most complex organisms need the most development time."
    },
    # ── Q102: Of Man's Abode, Which is Paradise ──
    {
        "index": "102.0",
        "refashioned": "Four questions about paradise: (1) Was it a physical place? (2) Was it suited to human habitation? (3) Why was man placed there? (4) Was man created there?"
    },
    {
        "index": "102.1a",
        "refashioned": "Paradise was a real, physical place. Augustine identifies three positions: purely corporeal, purely spiritual, or both. The strongest view is both. Scripture narrates events in paradise as history (the planting of trees, the formation of Eve, the rivers), and historical narrative demands a real location.\n\nParadise was a garden in the east, situated in the most excellent part of the earth. The \"east\" carries symbolic weight (it is the \"right hand\" of the heavens, the nobler side), but the place itself was genuinely physical. The tree of life was a real tree whose fruit had life-preserving power, though it also carried spiritual significance. The tree of knowledge of good and evil was equally real, named for what would result from eating it."
    },
    {
        "index": "102.1b",
        "refashioned": "The claim that paradise reached to the moon should not be taken literally. It may mean figuratively that its atmosphere had the constant, temperate quality associated with celestial bodies. The rivers of paradise may have flowed underground for some distance before emerging at their known sources, a common phenomenon in geography.\n\nThe reason no explorer has found paradise is that it is cut off from the habitable world by impassable barriers: mountains, seas, or extreme climate. Its inaccessibility does not disprove its existence."
    },
    {
        "index": "102.2a",
        "refashioned": "Paradise was perfectly suited to man's original state. The human body could be corrupted in two ways: internally by aging (loss of moisture, weakening of vital force) and externally by hostile environmental conditions. Paradise addressed both. Its temperate, pure atmosphere protected against external corruption. Its trees, including the tree of life, provided nourishment against internal decay.\n\nWhy not the empyrean heaven, where angels dwell? Because the empyrean suits angelic nature (purely spiritual, governing all corporeal creation from above) and the state of beatitude (maximally stable). Man's nature is not purely spiritual, and his original state was not yet beatitude. Paradise suited man as he was: embodied, immortal by grace, and on the way toward beatitude rather than already possessing it."
    },
    {
        "index": "102.2b",
        "refashioned": "The empyrean heaven fits the angel's nature directly and serves as the abode of beatitude. It would have been man's final destination but not his starting point. Paradise was adapted to man as a composite of soul and body, providing what the body needed (temperate conditions) precisely because the soul's preserving power worked through bodily conditions.\n\nNo irrational animal naturally inhabited paradise, though God brought animals there for Adam to study and name, and the serpent entered through diabolical agency. Paradise did not become useless after man's expulsion; it demonstrated God's original generosity and what man lost through sin."
    },
    {
        "index": "102.3",
        "refashioned": "Man was placed in paradise \"to dress it and keep it.\" This can be read two ways. First, God worked in man and kept him: sanctifying him (since without God's ongoing work, man falls into darkness) and preserving him from corruption and evil. Second, man cultivated and guarded paradise, but this cultivation would have been pleasant, not laborious. Before sin, work was a form of knowledge and delight, not toil. And \"keeping\" paradise meant keeping it for himself by not sinning, not guarding it against external trespassers.\n\nParadise was for man's benefit, not the reverse. Man was not created to serve the garden; the garden was created to serve man."
    },
    {
        "index": "102.4",
        "refashioned": "Man was not created in paradise but was created outside it and then placed there by God. This arrangement makes a theological point: the incorruptibility of man's original state was not natural to him but was a supernatural gift. By creating man outside paradise and then transferring him there, God made clear that the blessed condition was His doing, not something inherent in human nature.\n\nAngels, by contrast, were created in their proper abode (the empyrean heaven) because that place suits their nature directly. For man, paradise suited his supernatural endowment, not his bare nature. Woman was made in paradise not because of her own dignity but because of the dignity of the material from which she was formed (Adam's rib, which was already in paradise). Similarly, children would have been born in paradise because their parents were already there."
    }
]

import json
import os

output_path = os.path.join(os.path.dirname(__file__), 'summa_p1_refashioned_part7.json')
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Wrote {len(data)} entries to {output_path}")
