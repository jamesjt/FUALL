// ── Agora: local discussion notes ──
// Each entry renders as a .doc-content element in the main pane.
// No Google Sheet fetch. Content is authored directly here.

const agoraEntries = [
    {
        title: 'The Hermosillo. 4/22/26',
        date: 'April 22, 2026',
        location: 'The Hermosillo on York',
        participants: ['T', 'L', 'S', 'J'],
        sections: [
            {
                heading: '1. China: 50 Years of Transformation',
                claim: 'In 50 years, China has improved well-being for more people, faster, than any nation in history.',
                verdict: 'Substantially true. Overwhelming on material well-being; qualified on political freedom and environment.',
                justification: [
                    { type: 'prose', text: 'Compressing gains of that magnitude into two generations across a population north of a billion is without historical parallel. No other nation has moved so many people so far so fast on the measurable axes of food, shelter, health, income, and education.' },
                    { type: 'prose', text: 'The qualifications are real but do not overturn the claim:' },
                    { type: 'bullets', items: [
                        'Air pollution cost ~1.8 years of average life expectancy in 2024 (AQLI), down from ~3.3 years in 2013. The fastest national air-quality improvement ever recorded, but still 5–6× WHO guidelines in the industrial north.',
                        'Civic freedoms have contracted sharply relative to the 1990s–2010s reformist peak. Tighter censorship, Hong Kong crackdown, mass detention of Uyghurs in Xinjiang (an estimated 1M+ held in "re-education" camps, 2017–2020), civil-society and lawyer arrests. Still vastly more permissive than under Mao, where private enterprise, independent religion, and free movement were effectively banned.',
                        'Xinjiang and Tibet live under intensive ethnic surveillance. Checkpoints, DNA collection, mosque closures, restrictions on religious and linguistic practice.'
                    ]}
                ],
                subsectionsCollapsible: true,
                subsections: [
                    {
                        title: 'Well-being of the average citizen',
                        claimRelation: 'supports',
                        summary: 'Average Chinese well-being improved dramatically.',
                        bullets: [
                            { label: 'World Bank. Lifting 800 million people out of poverty', url: 'https://www.worldbank.org/en/news/press-release/2022/04/01/lifting-800-million-people-out-of-poverty-new-report-looks-at-lessons-from-china-s-experience', relation: 'supports', note: '~800M lifted out of extreme poverty since 1978' },
                            { label: 'World Bank. Life expectancy, China', url: 'https://data.worldbank.org/indicator/SP.DYN.LE00.IN?locations=CN', relation: 'supports', note: 'Life expectancy rose 12 years (66 → 78)' },
                            { label: 'World Bank. Infant mortality rate, China', url: 'https://data.worldbank.org/indicator/SP.DYN.IMRT.IN?locations=CN', relation: 'supports', note: 'Infant mortality ~10% of what it was' },
                            { label: 'World Bank / WHO. Maternal mortality ratio, China', url: 'https://data.worldbank.org/indicator/SH.STA.MMRT?locations=CN', relation: 'supports', note: 'Maternal mortality ~25% of what it was' },
                            { label: 'UNDP. Human Development Report (China)', url: 'https://hdr.undp.org/data-center/specific-country-data#/countries/CHN', relation: 'supports', note: 'Human Development Index 0.43 → 0.79' },
                            { label: 'World Bank. Adult literacy rate, China', url: 'https://data.worldbank.org/indicator/SE.ADT.LITR.ZS?locations=CN', relation: 'supports', note: 'Literacy 66% → 97%' },
                            { label: 'Our World in Data. China', url: 'https://ourworldindata.org/country/china', relation: 'supports', note: 'Nutrition, clean water, sanitation, schooling years. All rose in parallel' }
                        ]
                    },
                    {
                        title: 'Upward mobility beyond poverty',
                        claimRelation: 'supports',
                        summary: 'Poverty exit is only half the story. It also brought people into a middle class at a scale no prior society matched.',
                        bullets: [
                            { label: 'China Leadership Monitor. China\'s middle-income class', url: 'https://www.prcleader.org/post/china-s-middle-income-class-macroeconomic-growth-and-common-prosperity', relation: 'supports', note: 'Middle-income class grew from 10M (2002) to 336M (2023). The largest class formation ever recorded' },
                            { label: 'Yicai Global. China\'s higher education enrollment rate exceeds 60%', url: 'https://www.yicaiglobal.com/news/chinas-higher-education-enrollment-rate-exceeds-60', relation: 'supports', note: 'Post-secondary enrollment: 0.26% (1949) → 60.2% (2023)' },
                            { label: 'SCMP. China\'s college graduates hit record high', url: 'https://www.scmp.com/economy/economic-indicators/article/3244076/chinas-college-graduates-hit-record-high-1179-million-2024-adding-job-market-pressure', relation: 'supports', note: 'University graduates 1.45M (2002) → 11.79M (2024)' },
                            { label: 'IZA DP 12804. Rising Intergenerational Income Persistence in China (Fan, Yi, Zhang)', url: 'https://docs.iza.org/dp12804.pdf', relation: 'qualifies', note: 'Intergenerational mobility: high for post-Mao cohort, narrowing for those born after ~1980' },
                            { label: 'NBER. Demystifying the Chinese Housing Boom (Fang, Gu, Xiong, Zhou)', url: 'https://www.nber.org/papers/w21112', relation: 'qualifies', note: 'Home ownership ~90% (among the world\'s highest). Credit-fueled, post-2021 correction risk' }
                        ]
                    },
                    {
                        title: 'Infrastructure, urbanization, & automation',
                        claimRelation: 'supports',
                        bullets: [
                            { label: 'Wikipedia. Urbanization in China', url: 'https://en.wikipedia.org/wiki/Urbanization_in_China', relation: 'supports', note: 'Urbanization 18% (1978) → 66% (2023)' },
                            { label: 'Wikipedia. Expressways of China', url: 'https://en.wikipedia.org/wiki/Expressways_of_China', relation: 'supports', note: 'Expressway network ~190,700 km (end of 2024). Roughly 2.4× the US Interstate system (~78,680 km); surpassed it in 2011' },
                            { label: 'Wikipedia. High-speed rail in China (Track network)', url: 'https://en.wikipedia.org/wiki/High-speed_rail_in_China#Track_network', relation: 'supports', note: '~45,000 km of operating high-speed rail by end-2023. Roughly two-thirds of the world\'s total' },
                            { label: 'WSJ', url: 'https://www.youtube.com/watch?v=MCBdcNA_FsI', relation: 'supports', note: 'Video: China\'s dark factories. So automated they don\'t need lights (WSJ tour of Zeekr EV plant)' },
                            { label: 'Kalil 4.0', url: 'https://www.youtube.com/watch?v=ZfyCGNhYwxY', relation: 'supports', note: 'Video: Xiaomi\'s 100% automated "dark factory". 10M phones per year, minimal humans' },
                            { label: 'Quicktron Robotics', url: 'https://www.youtube.com/watch?v=9lzxF1oOWgM', relation: 'supports', note: 'Video: Alibaba\'s Cainiao fulfillment center running 1000+ autonomous mobile robots' },
                            { label: 'Wikipedia. List of busiest container ports', url: 'https://en.wikipedia.org/wiki/List_of_busiest_container_ports', relation: 'supports', note: '7 of the 10 busiest container ports are in China (including Hong Kong); Shanghai #1 since 2010' }
                        ]
                    },
                    {
                        title: 'Energy',
                        claimRelation: 'supports',
                        bullets: [
                            { label: 'World Bank. Access to electricity, China', url: 'https://data.worldbank.org/indicator/EG.ELC.ACCS.ZS?locations=CN', relation: 'supports', note: '~60% electrification (1980) → 100% (~2015). Every modern well-being metric. Refrigeration, education, safe water pumps. Depends on this.' },
                            { label: 'Carbon Brief. China added more solar panels in 2023 than US did in its entire history', url: 'https://www.carbonbrief.org/daily-brief/china-added-more-solar-panels-in-2023-than-us-did-in-its-entire-history/', relation: 'supports', note: 'China added 217 GW of solar in 2023. More than the total US solar fleet (~175 GW) built over the prior two decades' },
                            { label: 'Ember. Global Electricity Review', url: 'https://ember-climate.org/insights/research/global-electricity-review-2024/', relation: 'context', note: 'China now accounts for ~60% of new global renewable capacity additions. Shifting the energy mix away from coal improves air quality, which directly affects lifespan.' },
                            { label: 'World Nuclear Association. China', url: 'https://world-nuclear.org/information-library/country-profiles/countries-a-f/china-nuclear-power', relation: 'context', note: '55+ reactors operating, 20+ under construction. Long-run energy security protects future well-being.' }
                        ]
                    },
                    {
                        title: 'Information & digital',
                        claimRelation: 'supports',
                        bullets: [
                            { label: 'CNNIC. Statistical Reports', url: 'https://www.cnnic.com.cn/IDR/ReportDownloads/', relation: 'supports', note: 'Internet users: ~620k (1997) → 1.09+ billion (2023). Financial services, education, and commerce now reach hundreds of millions who had no access at all.' },
                            { label: 'Brookings. The digital yuan and digital payments', url: 'https://www.brookings.edu/articles/the-future-of-money-and-the-digital-yuan/', relation: 'supports', note: 'Alipay + WeChat Pay process $40T+ annually. Financial inclusion at a scale no developing economy has matched.' },
                            { label: 'ITU. Digital Development Dashboard', url: 'https://www.itu.int/en/ITU-D/Statistics/Pages/stat/default.aspx', relation: 'context', note: '3.8M+ 5G base stations. 60% of the global total. Infrastructure for the next generation of services.' }
                        ]
                    },
                ]
            },
            {
                heading: '2. Has War and Violence Really Declined?',
                claim: 'Since WWII, global deaths from violence have declined substantially.',
                verdict: 'Substantially true. The post-WWII period had the lowest per-capita rate of violent death in any comparable interval on record; qualified by regional unevenness and a partial 2020s reversal.',
                justification: [
                    { type: 'prose', text: 'Per-capita deaths from interstate war, civil conflict, homicide, and mass atrocity all fell sharply from their first-half-of-the-20th-century peaks. The drop is most dramatic on the war-and-genocide axis: combatants died at ~240,000/year on average from 1800–1945 vs. ~40,000/year since 1989 (OWID, UCDP).' },
                    { type: 'prose', text: 'The qualifications are real but do not overturn the claim:' },
                    { type: 'bullets', items: [
                        'Homicide trends are uneven by region. Africa and the Americas remain 2–3× the current global average, and Latin American rates swing significantly decade to decade.',
                        'The 2020s reversed part of the recent gain. Conflict deaths in 2023 hit ~170,700 (SIPRI), the highest since 2019, though still small relative to mid-20th-century baselines.',
                        'Most post-WWII atrocity deaths concentrate in Mao\'s regime and late Stalinism. Strip those outliers and the per-year decline relative to 1915–1945 grows to ~15–30×.'
                    ]}
                ],
                subsectionsCollapsible: true,
                subsections: [
                    {
                        title: 'Overall violent death trend since WWII',
                        claimRelation: 'supports',
                        summary: 'Global violent deaths per capita fell dramatically from WWII peaks to the 2010s, the least violent period per capita in recorded history.',
                        bullets: [
                            { label: 'Our World in Data. War and Peace', url: 'https://ourworldindata.org/war-and-peace', relation: 'supports', note: '"Fewer people died in conflicts in recent decades than in most of the 20th century". Though the article flags a recent uptick in the Middle East, Africa, and Europe' }
                        ]
                    },
                    {
                        title: 'Homicide trends. WWII era vs. 2010–2020, by region',
                        claimRelation: 'supports',
                        summary: 'The data gap is a bit problematic as systematic global and regional homicide tracking only begins ~1990. The WWII-era to 2010–2020 comparison is cleanest for Europe and the US. Where more historical data exists, the dominant pattern is decline or decline-then-partial-reversal.',
                        bullets: [
                            { label: 'Wikipedia. Homicide (Eisner long-run series)', url: 'https://en.wikipedia.org/wiki/Homicide', relation: 'supports', note: 'Europe. Long-term decline: 20th-century Western European average ~1.4/100k (Eisner). Today Western Europe ~0.5–1.5/100k; wider Europe/Central Asia region ~3/100k (Eastern Europe higher)' },
                            { label: 'Disaster Center. US FBI UCR compilation', url: 'https://www.disastercenter.com/crime/uscrime.htm', relation: 'supports', note: 'US. Peak-and-decline cycle: 5.1/100k (1960) → 10/100k (1990 peak) → 4.8 (2010) → 5.0 (2019). Roughly stable 1960 vs. 2010s' },
                            { label: 'Wikipedia. Gun violence in the United States', url: 'https://en.wikipedia.org/wiki/Gun_violence_in_the_United_States', relation: 'supports', note: 'US. 1990s peak and decline: "After 1993, gun violence in the United States began a period of dramatic decline." Gun homicide 7/100k (1993) → 3.6 (2013)' },
                            { label: 'Brookings. Why did U.S. homicides spike in 2020?', url: 'https://www.brookings.edu/articles/why-did-u-s-homicides-spike-in-2020-and-then-decline-rapidly-in-2023-and-2024/', relation: 'supports', note: 'US. COVID bump then reversal: 2020 surge of almost 30% in the average city; "in 2023 they began to fall rapidly"' },
                            { label: 'Wikipedia. Crime in Japan', url: 'https://en.wikipedia.org/wiki/Crime_in_Japan', relation: 'supports', note: 'East Asia (Japan). Sustained decline: 1.1/100k (1989, earliest verified) → 0.78/100k (2024); "murders at postwar low." Pre-1989 data not cleanly sourced' },
                            { label: 'Wikipedia. Crime in South Africa', url: 'https://en.wikipedia.org/wiki/Crime_in_South_Africa', relation: 'qualifies', note: 'Africa (South Africa). Major decline then partial reversal: 67/100k (1994) → 34 (2009) → 44 (2023). Pre-1994 regional data patchy' },
                            { label: 'Wikipedia. Crime in Latin America', url: 'https://en.wikipedia.org/wiki/Crime_in_Latin_America', relation: 'qualifies', note: 'Latin America. Mixed, volatile, no pre-1990 baseline: Mexico 19.4 (2011) → 25 (2017); El Salvador 106 (2012) → 1.9 (2024); Colombia 24.4 (2016)' },
                            { label: 'Wikipedia. Crime in Australia', url: 'https://en.wikipedia.org/wiki/Crime_in_Australia', relation: 'supports', note: 'Oceania (Australia). Low and stable: ~0.87/100k (2017–2020), stable since the data series began in 1989' },
                            { label: 'Wikipedia. List of countries by intentional homicide rate (UNODC global)', url: 'https://en.wikipedia.org/wiki/List_of_countries_by_intentional_homicide_rate', relation: 'context', note: 'Global average (post-1990 only, no pre-1990 systematic data): 6.9/100k (2010) → 6.2 (2012) → 6.1 (2017) → 5.6 (2022)' }
                        ]
                    },
                    {
                        title: 'Battle deaths. War and civil conflict',
                        claimRelation: 'supports',
                        summary: 'Battle deaths per capita collapsed after WWII. Post-1970s–80s wars peaked around 300,000 annual deaths; fell to much lower levels in the 1990s and stayed below those peaks for two decades.',
                        bullets: [
                            { label: 'Our World in Data. War and Peace', url: 'https://ourworldindata.org/war-and-peace', relation: 'supports', note: '"Conflict deaths surged again in the 1970s and 1980s... peaked at 300,000 deaths annually. They fell to much lower levels in the 1990s and have stayed below previous peaks in the decades since"' }
                        ]
                    },
                    {
                        title: 'Mass atrocities. Pre-WWII era vs. post-WWII',
                        claimRelation: 'supports',
                        summary: 'Atrocities by aggregate death toll pre- and post-WWII look comparable. But ~70–80% of the post-WWII total is concentrated in Mao\'s regime alone (Great Leap Forward + Cultural Revolution) and late Stalinism. Strip those and post-WWII drops to ~6–10M cumulative across 80 years, a 15–30× per-year decline.',
                        bullets: [
                            { label: 'Our World in Data. War and Peace', url: 'https://ourworldindata.org/war-and-peace', relation: 'supports', note: 'Framing: "Fewer people died in conflicts in recent decades than in most of the 20th century." Two World Wars account for roughly three-quarters of all war deaths since 1800' },
                            { label: 'Wikipedia. Democide (Rummel estimate)', url: 'https://en.wikipedia.org/wiki/Democide', relation: 'supports', note: '20th-century aggregate: Rummel estimates ~262M government-caused deaths ("democide"), with ~6× the battle death count. The overwhelming share falls in 1917–1953 (Stalin, Hitler, early Mao)' },
                            { heading: 'Pre-WWII' },
                            { label: 'USHMM. Documenting Holocaust victim numbers', url: 'https://encyclopedia.ushmm.org/content/en/article/documenting-numbers-of-victims-of-the-holocaust-and-nazi-persecution', relation: 'supports', note: 'Pre-WWII anchor. Holocaust (1941–45): 6M Jews killed + ~3.3M Soviet POWs, ~1.8M ethnic Poles, 250K+ Roma, 250K–300K people with disabilities' },
                            { label: 'Wikipedia. World War II casualties', url: 'https://en.wikipedia.org/wiki/World_War_II_casualties', relation: 'supports', note: 'WWII total: "60–75 million deaths" including battle, deprivation, famine, disease, and atrocities' },
                            { label: 'Wikipedia. Armenian genocide', url: 'https://en.wikipedia.org/wiki/Armenian_genocide', relation: 'supports', note: 'Pre-WWII: Armenian Genocide (1915–1923) killed ~1 million Armenians (range 600K–1.5M)' },
                            { label: 'Wikipedia. Holodomor', url: 'https://en.wikipedia.org/wiki/Holodomor', relation: 'supports', note: 'Pre-WWII: Holodomor (1932–33). "3.5 to 5 million victims" (recent scholarly range) of Stalin-era Ukrainian famine' },
                            { label: 'Wikipedia. Great Purge', url: 'https://en.wikipedia.org/wiki/Great_Purge', relation: 'supports', note: 'Pre-WWII: Great Purge (1936–38). "681,692 executions and 116,000 deaths in the Gulag"; scholarly estimates 700K–1.2M' },
                            { label: 'Wikipedia. Nanjing Massacre', url: 'https://en.wikipedia.org/wiki/Nanjing_Massacre', relation: 'supports', note: 'Pre-WWII: Nanjing (1937). IMTFE estimated "more than 200,000 people were killed"; newer estimates 100,000–200,000+' },
                            { heading: 'Post-WWII' },
                            { label: 'Wikipedia. Great Leap Forward / Great Chinese Famine', url: 'https://en.wikipedia.org/wiki/Great_Chinese_Famine', relation: 'qualifies', note: 'Post-WWII (the largest): Mao\'s Great Leap Forward (1958–62). "most death toll estimates range from 30 to 60 million." The single largest peacetime atrocity in history' },
                            { label: 'Wikipedia. Cultural Revolution', url: 'https://en.wikipedia.org/wiki/Cultural_Revolution', relation: 'qualifies', note: 'Post-WWII: Mao\'s Cultural Revolution (1966–76). "Estimates of the death toll vary widely, typically ranging from 1 to 2 million"' },
                            { label: 'Wikipedia. Population transfer in the Soviet Union', url: 'https://en.wikipedia.org/wiki/Population_transfer_in_the_Soviet_Union', relation: 'qualifies', note: 'Post-WWII: Late Stalinist deportations (Crimean Tatars 1944, Chechens, Volga Germans). Werth estimates "1 to 1.5 million perishing as a result of the deportations"' },
                            { label: 'Wikipedia. Cambodian genocide', url: 'https://en.wikipedia.org/wiki/Cambodian_genocide', relation: 'qualifies', note: 'Post-WWII: Khmer Rouge (1975–79). "1.5 to 2 million people, amounting to 20% to 25% of the country\'s 1975 population"' },
                            { label: 'Wikipedia. Indonesian mass killings of 1965–66', url: 'https://en.wikipedia.org/wiki/Indonesian_mass_killings_of_1965%E2%80%9366', relation: 'qualifies', note: 'Post-WWII: Indonesia 1965–66. "at least 500,000 to 1 million people were killed"' },
                            { label: 'Wikipedia. Genocides in history', url: 'https://en.wikipedia.org/wiki/Genocides_in_history', relation: 'qualifies', note: 'Post-WWII: Rwanda 1994. "at least 800,000 killed" (Human Rights Watch). Srebrenica 1995. "more than 8,000 Bosniaks" killed. Rohingya genocide ongoing' },
                            { label: 'Wikipedia. North Korean famine', url: 'https://en.wikipedia.org/wiki/North_Korean_famine', relation: 'qualifies', note: 'Post-WWII: North Korean famine (1994–99). "between 600,000 and 1 million people, or 3 to 5 percent of the pre-crisis population, died." Plus ongoing camp deaths' },
                            { label: 'Wikipedia. Casualties of the Syrian civil war', url: 'https://en.wikipedia.org/wiki/Casualties_of_the_Syrian_civil_war', relation: 'qualifies', note: 'Post-WWII: Syria (2011+). SOHR estimate ~656K killed by March 2025. Largest atrocity toll of the post-2000 era' }
                        ]
                    },
                    {
                        title: 'The 2020s reversal',
                        claimRelation: 'qualifies',
                        summary: 'Things are going back up in the 2020\'s but still much lower than pre-WWII.',
                        bullets: [
                            { label: 'SIPRI Yearbook 2024. Armed Conflicts', url: 'https://www.sipri.org/yearbook/2024/02', relation: 'qualifies', note: '"Conflict-related fatalities worldwide rose from 153,100 in 2022 to 170,700 in 2023, to reach the highest level since 2019."' }
                        ]
                    },
                ]
            },
            {
                heading: '3. Dawn of Everything. Power and well-being among hunter-gatherers',
                claim: 'Dawn of Everything overstates equality in pre-state hunter-gatherer society and overstates their well-being.',
                verdict: 'Largely true on both counts. Pre-state forager societies had real internal coercion, and forager material life was hard: ~50% pre-puberty mortality, life expectancy at birth ~30, lethal violence 5–25× modern levels. The book\'s challenge to the rigid "bands → states" narrative has merit; the romantic forager picture does not.',
                justification: [
                    { type: 'prose', text: 'Mainstream archaeology and anthropology have substantially disputed the book\'s empirical claims about pre-state egalitarianism and forager well-being. The ethnographic record documents real coercion inside foraging bands (gender hierarchy, ostracism, charismatic dominance); the demographic record documents real material hardship.' },
                    { type: 'prose', text: 'The book\'s contributions are real but do not overturn the claim:' },
                    { type: 'bullets', items: [
                        'The textbook "bands → tribes → chiefdoms → states" sequence is too rigid. Pre-state political variability was real and the book\'s challenge to the unilinear narrative has been broadly accepted.',
                        'Marshall Sahlins\'s "original affluent society" thesis on shorter forager work hours holds up empirically and is the strongest piece of the romantic case.',
                        'Indigenous critique of European society (especially via the Wendat statesman Kandiaronk) did influence the European Enlightenment, even if the book overstates how decisive that influence was.'
                    ]}
                ],
                subsectionsCollapsible: true,
                subsections: [
                    {
                        title: 'Power structures the book underplays',
                        claimRelation: 'supports',
                        summary: 'Forager coercion was real: gender hierarchies, ostracism, charismatic dominance.',
                        bullets: [
                            { label: 'Chris Knight. "Wrong About (Almost) Everything" (Focaal Blog)', url: 'https://www.focaalblog.com/2021/12/22/chris-knight-wrong-about-almost-everything/', relation: 'supports', note: 'Abandons egalitarian-baseline forager literature; misreads ethnographic record on internal coercion' },
                            { label: 'Camilla Power et al.. Special Issue', url: 'https://www.thetedkarchive.com/library/various-authors-special-issue-on-the-dawn-of-everything', relation: 'supports', note: 'Multiple anthropologists on what the book gets wrong about gender hierarchies and internal coercion in foragers' },
                        ]
                    },
                    {
                        title: 'Well-being',
                        claimRelation: 'supports',
                        summary: 'Mortality, violence, and material constraints among foragers.',
                        bullets: [
                            { label: 'Gurven & Kaplan. Longevity Among Hunter-Gatherers (PDR, 2007)', url: 'https://gurven.anth.ucsb.edu/sites/secure.lsit.ucsb.edu.anth.d7_gurven/files/sitefiles/papers/GurvenKaplan2007pdr.pdf', relation: 'supports', note: 'Life expectancy at birth ~30; ~50% died before puberty' },
                            { label: 'Our World in Data. Every second child died', url: 'https://ourworldindata.org/child-mortality-in-the-past', relation: 'supports', note: 'Forager infant mortality ~27%; pre-puberty ~49%' },
                            { label: 'Our World in Data. Life Expectancy (long-run)', url: 'https://ourworldindata.org/life-expectancy', relation: 'supports', note: 'Flat 30–40 year baseline across all pre-modern populations' },
                            { label: 'Karnofsky. Was life better in hunter-gatherer times?', url: 'https://www.cold-takes.com/was-life-better-in-hunter-gatherer-times/', relation: 'supports', note: 'Arguments for probably no pre-agriculture Eden' },
                            { label: 'Violence Trends. Violence Before Agriculture (Thomson & Halstead, 2024)', url: 'https://violencetrends.substack.com/p/violence-before-agriculture-full', relation: 'supports', note: 'Median ethnographic rate of ~124 violent deaths per 100,000 people per year among Late-Pleistocene-appropriate hunter-gatherers; argues Pinker\'s ~15% figure is too high; emphasizes high variability across time and place' }
                        ]
                    },
                    {
                        title: 'Specific scholarly critiques',
                        claimRelation: 'supports',
                        summary: 'On evidence selection and archaeological interpretation.',
                        bullets: [
                            { label: 'Appiah. Digging for Utopia (NYRB)', url: 'https://www.nybooks.com/articles/2021/12/16/david-graeber-digging-for-utopia/', relation: 'supports', note: '"A discordance between what the book says and what its sources say"' },
                            { label: 'NYRB. Wengrow exchange', url: 'https://www.nybooks.com/articles/2022/01/13/the-roots-of-inequality-an-exchange/', relation: 'supports', note: 'Wengrow\'s response and the back-and-forth' },
                            { label: 'Scheidel. Resetting History\'s Dial? (Cliodynamics)', url: 'https://escholarship.org/uc/item/9jj9j6z7', relation: 'supports', note: 'Materialist critique: over-emphasizes ideas; dismisses ecology, demography, technology' },
                            { label: 'Chicago Review. After Dawn', url: 'https://www.chicagoreview.org/david-graeber-the-dawn-of-everything/', relation: 'supports', note: 'Feinman & Smith on cherry-picked archaeology (Çatalhöyük, Ukrainian mega-sites)' }
                        ]
                    },
                    {
                        title: 'Pre-state violence. Contested literature',
                        claimRelation: 'supports',
                        summary: 'Pinker/Keeley/Gat say high; Fry/Ferguson say lower but still elevated.',
                        bullets: [
                            { label: 'Pinker. Better Angels FAQ', url: 'https://stevenpinker.com/frequently-asked-questions-about-better-angels-our-nature-why-violence-has-declined', relation: 'supports', note: '~14% prehistoric violent-death rate' },
                            { label: 'Wikipedia. War Before Civilization (Keeley, 1996)', url: 'https://en.wikipedia.org/wiki/War_Before_Civilization', relation: 'supports', note: 'Prehistoric war was more frequent and lethal per capita than modern war' },
                            { label: 'Wikipedia. Azar Gat — War in Human Civilization (2006)', url: 'https://en.wikipedia.org/wiki/Azar_Gat', relation: 'supports', note: '70–90% of forager societies at war in any 5-year window' },
                            { label: 'Ferguson. Pinker\'s List', url: 'https://academic.oup.com/book/12748/chapter/162857545', relation: 'qualifies', note: 'Pinker\'s 21-site sample cherry-picked; inflates the "before" baseline' },
                            { label: 'Fry (ed.). War, Peace, and Human Nature', url: 'https://www.goodreads.com/en/book/show/15856746', relation: 'qualifies', note: '20+ anthropologists arguing war has a beginning and is learned' }
                        ]
                    },
                    {
                        title: 'Defenses & favorable reviews',
                        claimRelation: 'qualifies',
                        summary: 'What is worth keeping from the book.',
                        bullets: [
                            { label: 'Deresiewicz. Human History Gets a Rewrite (Atlantic)', url: 'https://www.theatlantic.com/magazine/archive/2021/11/graeber-wengrow-dawn-of-everything-history-humanity/620177/', relation: 'qualifies', note: 'Most enthusiastic mainstream review. "brilliant" and "inspiring"' },
                            { label: 'Sahlins. The Original Affluent Society', url: 'https://en.wikipedia.org/wiki/Original_affluent_society', relation: 'qualifies', note: 'Hunter-gatherer work hours were lower than agricultural societies. Strongest empirical point in the romantic case' }
                        ]
                    },
                    {
                        title: 'North Sentinel Island. What we know and how fragile',
                        claimRelation: 'context',
                        summary: 'Brought up at the table because it is one of the last truly uncontacted peoples on Earth. Two things worth knowing: how little we actually know about its internal life, and how fragile that existence is to disease, contact, and natural disasters.',
                        bullets: [
                            { label: 'Wikipedia. North Sentinel Island', url: 'https://en.wikipedia.org/wiki/North_Sentinel_Island', relation: 'context', note: 'Geography: ~60 km² island in the Bay of Bengal, part of India\'s Andaman Islands. The 2004 earthquake lifted parts of it 1–2 m' },
                            { label: 'Wikipedia. Sentinelese', url: 'https://en.wikipedia.org/wiki/Sentinelese', relation: 'context', note: 'Population: "estimates ranging between 35 and 500 individuals" (50–200 central). Likely 30,000+ years of isolation; language unintelligible to other Andamanese speakers' },
                            { label: 'Wikipedia. Sentinelese (1956 contact ban)', url: 'https://en.wikipedia.org/wiki/Sentinelese', relation: 'context', note: 'Legal protection: India\'s 1956 Andaman & Nicobar Protection of Aboriginal Tribes Regulation made the island a tribal reserve, prohibiting travel within 5 km' },
                            { label: 'Survival International. Sentinelese', url: 'https://www.survivalinternational.org/peoples/sentinelese', relation: 'context', note: 'Disease fragility: "the entire people could be wiped out by diseases to which they have no immunity." After ~30,000 years of isolation, a single contact event could be catastrophic' },
                            { label: 'Wikipedia. North Sentinel Island (2004 tsunami)', url: 'https://en.wikipedia.org/wiki/North_Sentinel_Island', relation: 'context', note: '2004 tsunami survival: "Three days after the earthquake, an Indian government helicopter observed several islanders, who shot arrows and threw spears and stones at the helicopter". Confirmed alive' },
                            { label: 'Wikipedia. John Allen Chau', url: 'https://en.wikipedia.org/wiki/John_Allen_Chau', relation: 'context', note: 'Contact threat (2018): "Chau was fatally shot by Sentinelese arrows" while attempting an illegal Christian missionary visit. Encroachment by fishermen and missionaries is ongoing' }
                        ]
                    }
                ]
            },
            {
                heading: '4. Progress is mostly a Western value',
                claim: 'Progress (improving life through reason, science, and deliberate effort) is primarily a classical Western ideology.',
                verdict: 'Largely true once "Western" is read as the Greek → Hellenistic → Roman → Renaissance → Enlightenment lineage rather than "geographic Europe." Other civilizations had partial elements (Indian formal logic, Chinese technological lead) but never produced the full progress package.',
                justification: [
                    { type: 'prose', text: 'The systematic commitment to using reason to investigate nature and improve the human condition is not a generic civilizational feature. It traces specifically to the Greek metaphysical-rationalist posture, was transmitted through medieval Christian institutions, and crystallized in the Renaissance and Enlightenment as a unified doctrine. Modernity inherits and globalizes that package.' },
                    { type: 'prose', text: 'The qualifications are real but do not overturn the claim:' },
                    { type: 'bullets', items: [
                        'China held the longest technological lead in history (paper, printing, gunpowder, metallurgy, Song-Yuan algebra) without producing modern science. Joseph Needham\'s question — why not? — points to institutional rather than metaphysical limits.',
                        'India had formal logic (Nyāya), rigorous formal grammar (Pāṇini), and an early-modern reason-tradition (Navya-Nyāya, the Kerala school\'s pre-calculus). It never propagated institutionally. What Jonardon Ganeri calls "the lost age of reason."',
                        'Modern progress is now a global project drawing on contributions from many civilizations. But the unified ideology — reason + science + human improvement — emerged as a doctrine only once, in the post-Renaissance European tradition.'
                    ]}
                ],
                authorNote: '[The Needham Question](https://en.wikipedia.org/wiki/Science_and_Civilisation_in_China#The_Needham_Question) and beyond....\nNote: The per-tradition orientations below are reductionist. I didn\'t have time to go into more detail, but didn\'t want to ignore started to clarify and justify the claim.',
                subsectionsCollapsible: true,
                subsections: [
                    {
                        title: 'Western / Classical Greek',
                        claimRelation: 'context',
                        bullets: [
                            { relation: 'context', note: 'Orientation: humanity can use [reason](https://en.wikipedia.org/wiki/Reason) to improve understanding of reality, in turn improving [eudaimonia](https://en.wikipedia.org/wiki/Eudaimonia) (human flourishing).' },
                            { relation: 'context', note: 'Educational legacy: [Paideia](https://en.wikipedia.org/wiki/Paideia) → [eudaimonia](https://en.wikipedia.org/wiki/Eudaimonia) → classical [trivium](https://en.wikipedia.org/wiki/Trivium) → [quadrivium](https://en.wikipedia.org/wiki/Quadrivium) → [liberal arts](https://en.wikipedia.org/wiki/Liberal_arts_education) → [empiricism](https://en.wikipedia.org/wiki/Empiricism) → sciences and humanities. Institutionally embedded in [Plato\'s Academy](https://en.wikipedia.org/wiki/Platonic_Academy) → [medieval universitas](https://en.wikipedia.org/wiki/Medieval_university) → [Humboldt\'s research university](https://en.wikipedia.org/wiki/Humboldtian_model_of_higher_education). The infrastructure that enabled the [Enlightenment](https://en.wikipedia.org/wiki/Age_of_Enlightenment).' }
                        ]
                    },
                    {
                        title: 'Confucian',
                        claimRelation: 'context',
                        bullets: [
                            { relation: 'context', note: 'Orientation: maintaining the ideals of the [sage-kings](https://en.wikipedia.org/wiki/Three_Sovereigns_and_Five_Emperors) through becoming [jūnzǐ](https://en.wikipedia.org/wiki/Junzi).' },
                            { relation: 'context', note: 'Educational legacy: [Five Classics](https://en.wikipedia.org/wiki/Five_Classics) → [Four Books](https://en.wikipedia.org/wiki/Four_Books) → Neo-Confucian synthesis ([Zhu Xi](https://en.wikipedia.org/wiki/Zhu_Xi), ~1190) → [imperial examination canon](https://en.wikipedia.org/wiki/Imperial_examination) (605–1905).' }
                        ]
                    },
                    {
                        title: 'Daoist',
                        claimRelation: 'context',
                        bullets: [
                            { relation: 'context', note: 'Orientation: alignment with the [Dào](https://en.wikipedia.org/wiki/Tao) through [wú wéi](https://en.wikipedia.org/wiki/Wu_wei) and [zìrán](https://en.wikipedia.org/wiki/Ziran), flowing with the natural order rather than changing it.' },
                            { relation: 'context', note: 'Educational legacy: [Daodejing](https://en.wikipedia.org/wiki/Tao_Te_Ching) → [Zhuangzi](https://en.wikipedia.org/wiki/Zhuangzi_%28book%29) → [Daozang](https://en.wikipedia.org/wiki/Daozang) (Daoist canon, codified from ~5th c. CE) → monastic lineages ([Quanzhen](https://en.wikipedia.org/wiki/Quanzhen_School), [Zhengyi](https://en.wikipedia.org/wiki/Zhengyi_Dao)).' }
                        ]
                    },
                    {
                        title: 'Buddhist',
                        claimRelation: 'context',
                        bullets: [
                            { relation: 'context', note: 'Orientation: escaping from [saṃsāra](https://en.wikipedia.org/wiki/Sa%E1%B9%83s%C4%81ra) through the [Four ārya satya](https://en.wikipedia.org/wiki/Four_Noble_Truths).' },
                            { relation: 'context', note: 'Educational legacy: [Tripiṭaka](https://en.wikipedia.org/wiki/Tripi%E1%B9%ADaka) → [Mahayana sutras](https://en.wikipedia.org/wiki/Mahayana_sutras) → [Nalanda](https://en.wikipedia.org/wiki/Nalanda) monastic university (5th–12th c.), with structured curricula in logic, grammar, medicine, and astronomy. The closest pre-modern non-Western parallel to the European university; destroyed c. 1200 CE.' }
                        ]
                    },
                    {
                        title: 'Vedic / Hindu',
                        claimRelation: 'context',
                        bullets: [
                            { relation: 'context', note: 'Orientation: alignment with [ṛta](https://en.wikipedia.org/wiki/%E1%B9%9Ata), turning inward in the [Upaniṣads](https://en.wikipedia.org/wiki/Upanishads) toward [Brahman](https://en.wikipedia.org/wiki/Brahman) and [Ātman](https://en.wikipedia.org/wiki/%C4%80tman_%28Hinduism%29).' },
                            { relation: 'context', note: 'Educational legacy: [Vedas](https://en.wikipedia.org/wiki/Vedas) → [Upanishads](https://en.wikipedia.org/wiki/Upanishads) → six darśanas ([Nyāya](https://en.wikipedia.org/wiki/Ny%C4%81ya), Vaiśeṣika, Sāṃkhya, Yoga, Mīmāṃsā, [Vedānta](https://en.wikipedia.org/wiki/Vedanta)) → [śāstras](https://en.wikipedia.org/wiki/Shastra). Formal logic in Nyāya makes it structurally closer to the West than to China; the [Kerala school](https://en.wikipedia.org/wiki/Kerala_school_of_astronomy_and_mathematics) (14th–16th c.) produced pre-calculus results that didn\'t propagate.' }
                        ]
                    }
                ]
            },
            {
                heading: '5. China embraced the classical Greek era and progress',
                claim: 'China embraced Western progress, but rejected the liberal politics that came with it.',
                verdict: 'Substantially true. China imported the Western progressivist package wholesale (Marxism, post-1978 empiricism, the Four Modernizations, mass STEM education) while rejecting the liberal political package (multiparty democracy, free press, universal rights) that grew alongside it in the West.',
                justification: [
                    { type: 'prose', text: 'Marxism is Hegelian in deep structure: Western historicist-progressivism, inverted. The 1978 "Practice is the Sole Criterion of Truth" campaign is Greek empiricism in Chinese form. The Four Modernizations and the "great rejuvenation" frame are forward-directed teleologies. China today is among the most aggressively progressivist large states in the world, while institutionally non-liberal.' },
                    { type: 'prose', text: 'The qualifications are real but do not overturn the claim:' },
                    { type: 'bullets', items: [
                        'China has not abandoned all non-progressivist currents. Confucian restoration under Xi (state-endorsed Confucian revival, classics in school curricula) coexists alongside the progressivist program rather than replacing it.',
                        'A smaller intellectual current — the Strauss / classical-turn scholars (Gan Yang, Liu Xiaofeng) — engages the Greek classics directly rather than via their Enlightenment derivatives, complicating any simple "China only took the modern parts" reading.',
                        'Open question, flagged but not resolved here: whether progress and liberalism are a positive feedback loop in the long run. Whether sustained progressivism eventually requires liberal guardrails, or whether the Chinese model can sustain progress indefinitely without them.'
                    ]}
                ],
                subsectionsCollapsible: true,
                subsections: [
                    {
                        title: 'What China adopted',
                        claimRelation: 'supports',
                        summary: 'The adoption was thorough and explicit: in ideology, epistemology, industrial policy, and education.',
                        bullets: [
                            { label: 'SEP. Karl Marx', url: 'https://plato.stanford.edu/entries/marx/', relation: 'supports', note: 'Marx inherited (and inverted) Hegelian dialectic. China\'s founding ideology is Western in its deepest philosophical architecture' },
                            { label: 'Wikipedia. "Practice is the Sole Criterion for Testing Truth"', url: 'https://en.wikipedia.org/wiki/Practice_is_the_Sole_Criterion_for_Testing_Truth', relation: 'supports', note: '1978 Guangming Daily essay that catalyzed Reform and Opening. Empiricism over Maoist dogma; a structurally Greek epistemic move' },
                            { label: 'Britannica. Four Modernizations', url: 'https://www.britannica.com/topic/Four-Modernizations', relation: 'supports', note: 'Agriculture, industry, science & technology, defense. A forward-directed teleology, not a restoration' },
                            { label: 'Yicai Global. China\'s post-secondary enrollment rate exceeds 60%', url: 'https://www.yicaiglobal.com/news/chinas-higher-education-enrollment-rate-exceeds-60', relation: 'supports', note: 'Post-secondary enrollment: 0.26% (1949) → 60.2% (2023). Science and reason adopted as national method, at unprecedented scale' },
                            { label: 'Quincy Institute. China\'s Historic Rise to the Top of the Scientific Ladder', url: 'https://quincyinst.org/research/chinas-historic-rise-to-the-top-of-the-scientific-ladder/', relation: 'supports', note: 'China has overtaken the US in publications in the world\'s most prestigious scientific journals' }
                        ]
                    },
                    {
                        title: 'The classical turn among intellectuals',
                        claimRelation: 'supports',
                        summary: 'A smaller but philosophically sharper current: Chinese scholars engaging the Greek classics directly, not just their Enlightenment derivatives.',
                        bullets: [
                            { label: 'Mark Lilla. "Reading Strauss in Beijing" (The New Republic, 2010)', url: 'https://newrepublic.com/article/79747/reading-leo-strauss-in-beijing-china-marx', relation: 'supports', note: 'Why Chinese intellectuals have turned to Greek, Latin, and German.' },
                            { label: 'The New Yorker. "How China Learned to Love the Classics"', url: 'https://www.newyorker.com/news/annals-of-education/how-china-learned-to-love-the-classics', relation: 'supports', note: 'Long-form reporting on China\'s growing engagement with the Greek and Roman classics' },
                            { label: 'Bryn Mawr Classical Review. Strauss/Gan Yang/Liu Xiaofeng', url: 'https://bmcr.brynmawr.edu/2023/2023.11.41/', relation: 'supports', note: 'Academic review naming Gan Yang and Liu Xiaofeng as the "neo-conservative nationalists" reading Strauss and the Greeks' },
                            { label: 'LA Review of Books. China Channel (archive)', url: 'https://chinachannel.lareviewofbooks.org/2021/03/21/closing/', relation: 'supports', note: 'Farewell post linking to the full archive of essays on China\'s classical turn (Plato, Thucydides, the Strauss school)' }
                        ]
                    },
                    {
                        title: 'Residual non-progressivist currents',
                        claimRelation: 'qualifies',
                        summary: 'The adoption is not total. Confucian restoration and traditional currents coexist with the progressivist official ideology: alongside, not replacing.',
                        bullets: [
                            { label: 'Daniel A. Bell. China\'s New Confucianism (Princeton UP)', url: 'https://press.princeton.edu/books/paperback/9780691145853/chinas-new-confucianism', relation: 'qualifies', note: 'State-endorsed Confucian revival as "a compelling alternative to Western liberalism". Partial restoration alongside the progressivist program' },
                            { label: 'SCMP. How Xi Jinping is going back to Confucius', url: 'https://www.scmp.com/news/china/politics/article/3287846/how-xi-jinping-going-back-confucius-define-chinas-future', relation: 'qualifies', note: 'Under Xi, Confucianism has made "a dramatic comeback as the bedrock of imperial Chinese ethics and governance"' }
                        ]
                    }
                ]
            },
            {
                heading: '6. Dharma',
                resourcesCollapsible: true,
                subsections: [
                    {
                        title: 'Bhagavad Gita',
                        bullets: [
                            { label: 'Gita Supersite (IIT Kanpur)', url: 'https://www.gitasupersite.iitk.ac.in/', note: 'Sanskrit, transliteration, English translations, and classical commentaries side-by-side.' }
                        ]
                    },
                    {
                        title: 'Bhagavad Gita. Video series (Swami Sarvapriyananda)',
                        bullets: [
                            { label: 'YouTube. Verse-by-verse lectures (Vedanta Society of NY)', url: 'https://www.youtube.com/playlist?list=PL2imXor63HtS4ewIKryBL4ZVeiaH8Ij4R', note: 'The primary series discussed. Swami Sarvapriyananda teaches the Gita verse-by-verse.' }
                        ],
                        embed: {
                            type: 'youtube-playlist',
                            id: 'PL2imXor63HtS4ewIKryBL4ZVeiaH8Ij4R',
                            title: 'Bhagavad Gita. Swami Sarvapriyananda'
                        }
                    },
                    {
                        title: 'Project Shivoham',
                        bullets: [
                            { label: 'Project SHIVOHAM. YouTube channel', url: 'https://www.youtube.com/c/ProjectShivoham', note: 'Channel on ancient Indian philosophy, Shaivism, and scriptural history.' }
                        ]
                    },
                    {
                        title: 'Ashoka. Empire Podcast Ep. 129',
                        bullets: [
                            { label: 'Apple Podcasts. Ep. 129: Ashoka, The Great Buddhist Emperor of India', url: 'https://podcasts.apple.com/gb/podcast/129-ashoka-the-great-buddhist-emperor-of-india/id1639561921?i=1000647984408', note: 'Tried to find the episode that recommended "The Difficulty of Being Good", uncertain if this was it.' }
                        ]
                    },
                    {
                        title: '"The Difficulty of Being Good". Gurcharan Das',
                        bullets: [
                            { label: 'Gurcharan Das. Official book page', url: 'https://gurcharandas.org/book/difficulty-being-good-subtle-art-dharma' }
                        ]
                    }
                ]
            }
        ]
    }
];

function escapeHtmlAttr(str) {
    return String(str).replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function appendInlineMarkdown(parent, text) {
    const linkRegex = /\[([^\]]+)\]\(([^)]+)\)/g;
    let lastIndex = 0;
    let match;
    while ((match = linkRegex.exec(text)) !== null) {
        if (match.index > lastIndex) {
            parent.appendChild(document.createTextNode(text.slice(lastIndex, match.index)));
        }
        const a = document.createElement('a');
        a.href = match[2];
        a.target = '_blank';
        a.rel = 'noopener noreferrer';
        a.className = 'agora-link';
        a.textContent = match[1];
        parent.appendChild(a);
        lastIndex = match.index + match[0].length;
    }
    if (lastIndex < text.length) {
        parent.appendChild(document.createTextNode(text.slice(lastIndex)));
    }
}

function buildAgoraEntryElement(entry) {
    const root = document.createElement('div');
    root.className = 'doc-content agora-doc';
    root.dataset.type = 'agora';

    // Header
    const header = document.createElement('header');
    header.className = 'agora-header';

    const h1 = document.createElement('h1');
    h1.className = 'agora-title';
    h1.textContent = entry.location;
    header.appendChild(h1);

    const meta = document.createElement('div');
    meta.className = 'agora-meta';
    const dateLine = document.createElement('div');
    dateLine.className = 'agora-meta-line';
    dateLine.innerHTML = '<span class="agora-meta-label">Date</span><span class="agora-meta-value">' + escapeHtmlAttr(entry.date) + '</span>';
    meta.appendChild(dateLine);
    const participantsLine = document.createElement('div');
    participantsLine.className = 'agora-meta-line';
    participantsLine.innerHTML = '<span class="agora-meta-label">Participants</span><span class="agora-meta-value">' + entry.participants.map(escapeHtmlAttr).join(' · ') + '</span>';
    meta.appendChild(participantsLine);
    header.appendChild(meta);

    root.appendChild(header);

    // Sections
    entry.sections.forEach(section => {
        const sec = document.createElement('section');
        sec.className = 'agora-section';

        const h2 = document.createElement('h2');
        h2.className = 'agora-section-title';
        const h2Label = document.createElement('span');
        h2Label.className = 'agora-section-label';
        if (section.claim) {
            const numMatch = (section.heading || '').match(/^(\d+\.\s)/);
            const numberPrefix = numMatch ? numMatch[1] : '';
            h2Label.textContent = numberPrefix + section.claim;
            h2Label.classList.add('is-claim');
        } else {
            h2Label.textContent = section.heading;
        }
        h2.appendChild(h2Label);
        sec.appendChild(h2);

        const body = document.createElement('div');
        body.className = 'agora-section-body';

        // The claim is now rendered as the section title itself (see h2Label above).
        // No separate claim block is rendered to avoid duplication.

        const isClaimSection = !!(section.verdict || section.justification);
        let pendingAssess = null;

        // Assessment block (verdict + justification + attribution). Collapsible.
        // Built here, but appended to body AFTER the Justifications wrap so it renders below.
        if (isClaimSection) {
            const assess = document.createElement('div');
            assess.className = 'agora-assessment is-collapsible collapsed';

            const byline = document.createElement('div');
            byline.className = 'agora-assessment-byline';
            byline.setAttribute('role', 'button');
            byline.setAttribute('tabindex', '0');
            byline.setAttribute('aria-expanded', 'false');
            const bySparkle = document.createElement('span');
            bySparkle.className = 'agora-assessment-icon';
            bySparkle.setAttribute('aria-hidden', 'true');
            bySparkle.textContent = '✦';
            byline.appendChild(bySparkle);
            const byText = document.createElement('span');
            byText.className = 'agora-assessment-byline-text';
            byText.textContent = 'Claude\'s assessment. Treat as a starting point, not a conclusion.';
            byline.appendChild(byText);
            const bChev = document.createElement('span');
            bChev.className = 'agora-chev';
            bChev.setAttribute('aria-hidden', 'true');
            byline.appendChild(bChev);
            const toggleAssess = () => {
                assess.classList.toggle('collapsed');
                byline.setAttribute('aria-expanded', !assess.classList.contains('collapsed') ? 'true' : 'false');
            };
            byline.addEventListener('click', toggleAssess);
            byline.addEventListener('keydown', e => {
                if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggleAssess(); }
            });
            assess.appendChild(byline);

            const assessBody = document.createElement('div');
            assessBody.className = 'agora-assessment-body';

            if (section.verdict) {
                const v = document.createElement('div');
                v.className = 'agora-verdict';
                const vLabel = document.createElement('span');
                vLabel.className = 'agora-verdict-label';
                vLabel.textContent = 'Verdict';
                v.appendChild(vLabel);
                const vText = document.createElement('span');
                vText.className = 'agora-verdict-text';
                vText.textContent = section.verdict;
                v.appendChild(vText);
                assessBody.appendChild(v);
            }

            if (section.justification) {
                const blocks = Array.isArray(section.justification)
                    ? section.justification
                    : [{ type: 'prose', text: section.justification }];
                const jWrap = document.createElement('div');
                jWrap.className = 'agora-justification';
                blocks.forEach(block => {
                    if (block.type === 'prose') {
                        const p = document.createElement('p');
                        p.className = 'agora-justification-prose';
                        p.textContent = block.text;
                        jWrap.appendChild(p);
                    } else if (block.type === 'bullets') {
                        const ul = document.createElement('ul');
                        ul.className = 'agora-justification-bullets';
                        (block.items || []).forEach(item => {
                            const li = document.createElement('li');
                            li.textContent = item;
                            ul.appendChild(li);
                        });
                        jWrap.appendChild(ul);
                    }
                });
                assessBody.appendChild(jWrap);
            }

            assess.appendChild(assessBody);
            pendingAssess = assess;
        }

        // For claim sections, wrap everything below in a "Justifications for claim" collapsible.
        // For sections flagged resourcesCollapsible, wrap in a "Resources" collapsible (same style).
        // Otherwise render directly into the section body.
        let containerEl = body;
        const collapsibleLabel = isClaimSection ? 'Justifications for claim'
            : (section.resourcesCollapsible ? 'Resources' : null);
        if (collapsibleLabel) {
            const just = document.createElement('div');
            just.className = 'agora-justifications-wrap is-collapsible collapsed';

            const jTitle = document.createElement('div');
            jTitle.className = 'agora-justifications-title';
            jTitle.setAttribute('role', 'button');
            jTitle.setAttribute('tabindex', '0');
            jTitle.setAttribute('aria-expanded', 'false');
            const jLabel = document.createElement('span');
            jLabel.className = 'agora-justifications-title-text';
            jLabel.textContent = collapsibleLabel;
            jTitle.appendChild(jLabel);
            const jChev = document.createElement('span');
            jChev.className = 'agora-chev';
            jChev.setAttribute('aria-hidden', 'true');
            jTitle.appendChild(jChev);
            const toggleJust = () => {
                just.classList.toggle('collapsed');
                jTitle.setAttribute('aria-expanded', !just.classList.contains('collapsed') ? 'true' : 'false');
            };
            jTitle.addEventListener('click', toggleJust);
            jTitle.addEventListener('keydown', e => {
                if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggleJust(); }
            });
            just.appendChild(jTitle);

            const jBody = document.createElement('div');
            jBody.className = 'agora-justifications-body';
            just.appendChild(jBody);
            body.appendChild(just);
            containerEl = jBody;
        }

        if (pendingAssess) {
            body.appendChild(pendingAssess);
        }

        if (section.summary) {
            const p = document.createElement('p');
            p.className = 'agora-section-summary';
            p.textContent = section.summary;
            containerEl.appendChild(p);
        }

        if (section.authorNote) {
            const noteWrap = document.createElement('div');
            noteWrap.className = 'agora-author-note';
            const lines = section.authorNote.split('\n').map(s => s.trim()).filter(Boolean);
            lines.forEach((line, i) => {
                const el = i === 0 ? document.createElement('span') : document.createElement('p');
                el.className = 'agora-author-note-text';
                appendInlineMarkdown(el, line);
                noteWrap.appendChild(el);
            });
            containerEl.appendChild(noteWrap);
        }

        const flatFormat = !!section.subsectionsCollapsible;

        (section.subsections || []).forEach(sub => {
            const subEl = document.createElement('div');
            subEl.className = 'agora-subsection' + (flatFormat ? ' is-flat' : '');

            const h3 = document.createElement('h3');
            h3.className = 'agora-subsection-title';
            if (flatFormat) {
                const labelSpan = document.createElement('span');
                labelSpan.className = 'agora-subsection-label';
                labelSpan.textContent = sub.title;
                h3.appendChild(labelSpan);
                // Render relation tag only when it's a departure from the default ("supports" is implicit)
                if (sub.claimRelation && sub.claimRelation !== 'supports') {
                    const tag = document.createElement('span');
                    tag.className = 'agora-relation agora-relation-inline relation-' + sub.claimRelation;
                    tag.textContent = sub.claimRelation.toUpperCase();
                    h3.appendChild(tag);
                }
            } else {
                h3.textContent = sub.title;
            }
            subEl.appendChild(h3);

            if (sub.summary) {
                const summaryP = document.createElement('p');
                summaryP.className = 'agora-subsection-summary';
                summaryP.textContent = sub.summary;
                subEl.appendChild(summaryP);
            }

            if (sub.note) {
                const noteP = document.createElement('p');
                noteP.className = 'agora-subsection-note';
                noteP.textContent = sub.note;
                subEl.appendChild(noteP);
            }

            if (sub.bullets && sub.bullets.length) {
                if (flatFormat) {
                    // Flat format: fact-first bullet with inline source link.
                    // Bullets with a `heading` field break the list into named groups.
                    let ul = document.createElement('ul');
                    ul.className = 'agora-subsection-points';
                    sub.bullets.forEach(b => {
                        if (b.heading) {
                            if (ul.children.length > 0) subEl.appendChild(ul);
                            const h = document.createElement('div');
                            h.className = 'agora-bullet-heading';
                            h.textContent = b.heading;
                            subEl.appendChild(h);
                            ul = document.createElement('ul');
                            ul.className = 'agora-subsection-points';
                            return;
                        }
                        const li = document.createElement('li');
                        const factText = b.note || b.label;
                        appendInlineMarkdown(li, factText + ' ');
                        if (b.url) {
                            const sourceWrap = document.createElement('span');
                            sourceWrap.className = 'agora-point-source';
                            const shortSource = (b.label || '').split('. ')[0].trim() || 'source';
                            sourceWrap.appendChild(document.createTextNode('['));
                            const a = document.createElement('a');
                            a.href = b.url;
                            a.target = '_blank';
                            a.rel = 'noopener noreferrer';
                            a.className = 'agora-link';
                            a.textContent = shortSource;
                            sourceWrap.appendChild(a);
                            sourceWrap.appendChild(document.createTextNode(']'));
                            li.appendChild(sourceWrap);
                        }
                        ul.appendChild(li);
                    });
                    if (ul.children.length > 0) subEl.appendChild(ul);
                } else {
                    // Legacy format: labeled link + note
                    const ul = document.createElement('ul');
                    ul.className = 'agora-links';
                    sub.bullets.forEach(b => {
                        const li = document.createElement('li');
                        li.className = 'agora-link-item' + (b.relation ? ' relation-' + b.relation : '');

                        if (b.relation) {
                            const tag = document.createElement('span');
                            tag.className = 'agora-relation relation-' + b.relation;
                            tag.textContent = b.relation.toUpperCase();
                            li.appendChild(tag);
                        }

                        if (b.label && b.url) {
                            const head = document.createElement('div');
                            head.className = 'agora-link-head';
                            const a = document.createElement('a');
                            a.href = b.url;
                            a.target = '_blank';
                            a.rel = 'noopener noreferrer';
                            a.className = 'agora-link';
                            a.textContent = b.label;
                            head.appendChild(a);
                            li.appendChild(head);
                        }

                        if (b.note) {
                            const note = document.createElement('p');
                            note.className = 'agora-link-note';
                            appendInlineMarkdown(note, b.note);
                            li.appendChild(note);
                        }
                        ul.appendChild(li);
                    });
                    subEl.appendChild(ul);
                }
            }

            if (sub.embed && sub.embed.type === 'youtube-playlist' && sub.embed.id) {
                const wrap = document.createElement('div');
                wrap.className = 'agora-embed';
                const iframe = document.createElement('iframe');
                iframe.src = 'https://www.youtube.com/embed/videoseries?list=' + encodeURIComponent(sub.embed.id);
                iframe.title = sub.embed.title || 'YouTube playlist';
                iframe.loading = 'lazy';
                iframe.setAttribute('allow', 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture');
                iframe.setAttribute('allowfullscreen', '');
                iframe.setAttribute('referrerpolicy', 'strict-origin-when-cross-origin');
                wrap.appendChild(iframe);
                subEl.appendChild(wrap);
            }

            containerEl.appendChild(subEl);
        });

        sec.appendChild(body);
        root.appendChild(sec);
    });

    return root;
}

function registerAgoraEntries() {
    agoraEntries.forEach(entry => {
        const el = buildAgoraEntryElement(entry);
        contentElements[entry.title] = el;
        contentMeta[entry.title] = { link: null, type: 'agora', loaded: true };
    });
}
