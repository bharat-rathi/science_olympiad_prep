"""Learning paths: Life, Personal & Social Science events."""

from app.content.learning_paths._base import lesson

ANATOMY_AND_PHYSIOLOGY = [
    lesson(
        "Cell Biology & Histology Fundamentals",
        "The cells and four tissue types every organ system is built from.",
        "CELL -- the smallest living unit. ORGANELLE -- a structure inside a cell with a job (nucleus, "
        "mitochondria, ribosomes, ER, Golgi, lysosomes). HISTOLOGY -- the study of tissues. TISSUE -- "
        "a group of similar cells working together.",
        "Every organ is made of the same four tissue types: epithelial (covers and lines), connective "
        "(supports and binds), muscle (moves), and nervous (signals). Learn to spot each, and the "
        "respiratory, digestive, and immune systems become much easier to read.",
        "Epithelium is named by layers and shape: simple (one layer) vs stratified (many); squamous "
        "(flat), cuboidal, columnar. Simple squamous lines the alveoli for fast diffusion; simple "
        "columnar with microvilli lines the small intestine for absorption; pseudostratified ciliated "
        "columnar with goblet cells lines the trachea and moves mucus. Connective tissue includes "
        "blood and the reticular tissue of lymph nodes. Muscle: skeletal (voluntary, striated), "
        "smooth (gut walls, airways), cardiac. Mitochondria make ATP by cellular respiration -- the "
        "reason you breathe.",
        "Which epithelium would you expect lining a structure built for gas exchange, and why? "
        "(Simple squamous -- one thin layer, short diffusion distance.)",
    ),
    lesson(
        "Respiratory System Anatomy",
        "The airway from nose to alveoli, at organ and microscopic level.",
        "UPPER TRACT -- nose, nasal cavity, pharynx, larynx. LOWER TRACT -- trachea, bronchi, "
        "bronchioles, alveoli. PLEURA -- the double membrane around each lung. DIAPHRAGM -- the main "
        "breathing muscle.",
        "Air travels nose -> pharynx -> larynx -> trachea -> left and right bronchi -> smaller "
        "bronchioles -> alveoli, tiny air sacs wrapped in capillaries where gas exchange happens. "
        "The airway warms, moistens, and filters air before it arrives.",
        "The conducting zone (nose through terminal bronchioles) moves air; the respiratory zone "
        "(respiratory bronchioles, alveolar ducts, alveoli) exchanges gas. C-shaped cartilage rings "
        "keep the trachea open; cartilage fades and smooth muscle increases toward the bronchioles. "
        "The epiglottis covers the larynx when you swallow. The right lung has 3 lobes, the left "
        "2 (room for the heart). Alveoli contain type I cells (thin, for diffusion), type II cells "
        "(make surfactant, which lowers surface tension so alveoli don't collapse), and alveolar "
        "macrophages (clean up debris).",
        "Why does an inhaled object more often lodge in the right main bronchus? (It is wider, "
        "shorter, and more vertical than the left.)",
    ),
    lesson(
        "Respiratory Physiology & Spirometry",
        "How air moves in and out, how gases cross into blood, and how lung volumes are measured.",
        "VENTILATION -- moving air in and out. PARTIAL PRESSURE -- each gas's share of total pressure. "
        "TIDAL VOLUME -- air per normal breath (~500 mL). VITAL CAPACITY -- the most air you can "
        "exhale after the deepest breath.",
        "Breathing works by changing pressure. The diaphragm contracts and flattens, the chest gets "
        "bigger, pressure inside drops below the air outside, and air flows in (Boyle's law: bigger "
        "volume, lower pressure). Relaxing reverses it.",
        "Gases diffuse from high to low partial pressure: O2 from alveoli (~104 mmHg) into blood "
        "(~40), CO2 from blood (~45) into alveoli (~40). Most O2 rides on hemoglobin; most CO2 travels "
        "as bicarbonate. Spirometry: Total Lung Capacity = Vital Capacity + Residual Volume; Vital "
        "Capacity = Tidal + Inspiratory Reserve + Expiratory Reserve. FEV1/FVC (the fraction exhaled "
        "in 1 second) is low in obstructive disease (asthma, COPD) and normal or high in restrictive "
        "disease (fibrosis). Breathing rhythm is set in the medulla and pons; chemoreceptors respond "
        "mostly to rising CO2 (falling blood pH). State/Nationals: blood chemistry and rhythm control.",
        "A patient's FEV1/FVC is 0.55. Obstructive or restrictive? (Obstructive -- they can't push air "
        "out fast.)",
    ),
    lesson(
        "Respiratory Disorders",
        "The common lung diseases, what goes wrong, and how they show up.",
        "OBSTRUCTIVE -- trouble getting air OUT (asthma, COPD). RESTRICTIVE -- trouble expanding the "
        "lungs (fibrosis). INFECTIOUS -- caused by a pathogen (pneumonia, TB).",
        "Most lung diseases either narrow the airways, stiffen the lung, fill the alveoli with fluid "
        "or pus, or damage the gas-exchange surface. Ask which one, and the symptoms follow.",
        "Asthma: reversible airway inflammation and bronchoconstriction (wheezing; treated with "
        "bronchodilators and inhaled steroids). COPD: emphysema (destroyed alveolar walls, less "
        "surface area) and chronic bronchitis (mucus, cough), mostly from smoking. Pneumonia: alveoli "
        "fill with fluid. Cystic fibrosis: a CFTR gene defect makes thick mucus. State/Nationals add "
        "tuberculosis (Mycobacterium tuberculosis), pulmonary edema, pleurisy, small cell vs non-small "
        "cell lung cancer, pulmonary fibrosis, and pneumoconioses (silicosis, coal worker's lung, "
        "asbestosis) -- plus treatments and prevention for every listed disease.",
        "Emphysema lowers gas exchange even with clear airways. Why? (Alveolar walls are destroyed, "
        "so there is less surface area for diffusion.)",
    ),
    lesson(
        "Digestive System Anatomy",
        "The alimentary canal from mouth to anus, plus the accessory organs.",
        "ALIMENTARY CANAL -- the continuous tube: mouth, pharynx, esophagus, stomach, small intestine, "
        "large intestine. ACCESSORY ORGANS -- teeth, tongue, salivary glands, liver, gallbladder, "
        "pancreas.",
        "Food passes through one long tube; the accessory organs sit outside it and send in "
        "secretions (saliva, bile, pancreatic juice) that help break food down.",
        "The gut wall has four layers: mucosa, submucosa, muscularis externa (two smooth-muscle "
        "layers for peristalsis; the stomach adds a third, oblique layer), and serosa. Small "
        "intestine: duodenum (receives bile and pancreatic juice), jejunum, ileum. Its surface area "
        "is huge thanks to circular folds, villi, and microvilli. Large intestine: cecum (with the "
        "appendix), ascending, transverse, descending, sigmoid colon, rectum. Sphincters control flow "
        "(lower esophageal, pyloric, ileocecal, anal). The liver makes bile; the gallbladder stores "
        "it; the pancreas makes enzymes and bicarbonate (and insulin/glucagon).",
        "List the three structures that multiply the small intestine's surface area. (Circular "
        "folds, villi, microvilli.)",
    ),
    lesson(
        "Digestive Physiology",
        "How food is moved, broken down, and absorbed.",
        "MOTILITY -- movement of food (peristalsis, segmentation). MECHANICAL DIGESTION -- physical "
        "breakdown. CHEMICAL DIGESTION -- enzymes breaking bonds. ABSORPTION -- nutrients crossing into "
        "blood or lymph.",
        "Chewing and churning break food into pieces; enzymes cut it into small molecules; the small "
        "intestine absorbs them. The large intestine mostly absorbs water.",
        "Carbohydrates: salivary and pancreatic amylase -> brush-border enzymes -> monosaccharides. "
        "Proteins: pepsin in the stomach (activated by HCl), then trypsin and chymotrypsin -> amino "
        "acids. Fats: bile salts emulsify, pancreatic lipase splits them into fatty acids and "
        "monoglycerides, which form micelles, are absorbed, packed into chylomicrons, and enter the "
        "lacteals (lymph). Hormones: gastrin (stimulates acid), secretin (bicarbonate release), CCK "
        "(bile and enzyme release). Peristalsis moves food forward; segmentation mixes it. "
        "State/Nationals: liver and pancreas function, including Kupffer cells (liver macrophages).",
        "Why do fats enter lymph instead of going straight into blood capillaries? (Chylomicrons "
        "are too large to cross capillary walls; they enter the lacteals.)",
    ),
    lesson(
        "Digestive Disorders",
        "What goes wrong along the gut and its accessory organs.",
        "INFLAMMATION -- the body's swelling/redness response. ULCER -- an open sore in a lining. "
        "MALABSORPTION -- nutrients not being absorbed.",
        "Most digestive disorders are a lining being damaged (by acid, infection, or the immune "
        "system), a blockage, or an organ not making what it should.",
        "Lactose intolerance: too little lactase. Gallstones: hardened bile that can block ducts. "
        "Hepatitis: liver inflammation (often viral). Cirrhosis: liver scarring. Appendicitis: "
        "inflamed appendix. State/Nationals list: diverticular disease (pouches in the colon wall), "
        "GERD (acid reflux through a weak lower esophageal sphincter), peptic ulcer disease (often "
        "H. pylori or NSAIDs), ulcerative colitis (continuous inflammation of the colon's mucosa) vs "
        "Crohn's disease (patchy, can affect any part of the tract, full wall thickness), and celiac "
        "disease (an immune reaction to gluten that flattens the villi) -- with treatments and "
        "prevention.",
        "Crohn's or ulcerative colitis: inflammation in patches from mouth to anus through the whole "
        "wall? (Crohn's.)",
    ),
    lesson(
        "Immune System Anatomy",
        "The organs and tissues where immune cells are made, trained, and meet invaders.",
        "PRIMARY LYMPHOID ORGANS -- where lymphocytes are made and mature: red bone marrow and thymus. "
        "SECONDARY LYMPHOID ORGANS -- where they meet antigens: lymph nodes, spleen, tonsils, MALT. "
        "LYMPH -- fluid in lymphatic vessels.",
        "Immune cells are born in bone marrow. T cells finish training in the thymus. Then they patrol "
        "the body and gather in lymph nodes and the spleen, which act like checkpoints that filter "
        "lymph and blood.",
        "Lymph nodes filter lymph and contain B-cell follicles and T-cell zones. The spleen filters "
        "blood (red pulp removes old red cells; white pulp holds lymphocytes). MALT (mucosa-associated "
        "lymphoid tissue) guards the gut and airways, including Peyer's patches in the ileum and the "
        "tonsils. Lymphatic vessels return fluid to the blood via the thoracic duct. The thymus is "
        "largest in childhood and shrinks with age.",
        "Which organ trains T cells, and which filters blood? (Thymus; spleen.)",
    ),
    lesson(
        "Innate Immunity",
        "The fast, non-specific first and second lines of defense.",
        "INNATE IMMUNITY -- defenses you're born with that respond the same way every time. PHAGOCYTE "
        "-- a cell that engulfs invaders (neutrophils, macrophages). INFLAMMATION. COMPLEMENT -- blood "
        "proteins that tag or punch holes in microbes.",
        "Barriers come first: skin, mucus, cilia, stomach acid, tears with lysozyme. If something gets "
        "through, innate cells attack within minutes to hours.",
        "Cells: neutrophils (most common white cell, first to arrive), macrophages (engulf and present "
        "antigen), dendritic cells (carry antigen to lymph nodes -- the bridge to adaptive immunity), "
        "natural killer cells (kill virus-infected and cancer cells), mast cells and basophils "
        "(histamine), eosinophils (parasites). Inflammation's signs: redness, heat, swelling, pain, "
        "loss of function -- from blood vessels dilating and leaking. Fever slows microbial growth. "
        "Interferons warn neighbor cells about viruses. Pattern-recognition receptors (e.g. "
        "toll-like receptors) detect common microbial molecules.",
        "Which innate cell links to adaptive immunity by presenting antigen in lymph nodes? "
        "(Dendritic cell.)",
    ),
    lesson(
        "Adaptive Immunity",
        "B cells, T cells, antibodies, and immune memory.",
        "ANTIGEN -- a molecule the immune system recognizes. ANTIBODY -- a Y-shaped protein from "
        "plasma cells that binds antigen. HUMORAL IMMUNITY -- antibody-based (B cells). CELL-MEDIATED "
        "-- T-cell based.",
        "Adaptive immunity is slower the first time (days) but specific, and it remembers. The second "
        "exposure is faster and stronger -- the idea behind vaccines.",
        "Helper T cells (CD4) recognize antigen on MHC II and coordinate the response; cytotoxic T "
        "cells (CD8) recognize antigen on MHC I and kill infected cells. B cells, helped by T cells, "
        "become plasma cells (make antibodies) or memory cells. Antibody classes: IgG (most common, "
        "crosses the placenta), IgA (in secretions and milk), IgM (first made, pentamer), IgE "
        "(allergies, parasites), IgD (on B cells). Antibodies neutralize, agglutinate, and tag "
        "microbes for phagocytes (opsonization) and complement. Active immunity (infection or "
        "vaccine) vs passive (antibodies received, e.g. from mother) -- passive is immediate but "
        "short-lived.",
        "Which antibody class shows up first in a new infection? (IgM.)",
    ),
    lesson(
        "Immune Disorders",
        "When the immune system is too weak, aims at self, or overreacts.",
        "IMMUNODEFICIENCY -- weak or missing immune function. AUTOIMMUNITY -- attacking your own "
        "tissues. HYPERSENSITIVITY -- an overreaction to a harmless antigen.",
        "There are three ways the immune system fails: too little (infections take hold), wrong "
        "target (autoimmune disease), or too much (allergies and other hypersensitivities).",
        "Immunodeficiency: primary (genetic, e.g. SCID) or acquired (HIV destroys CD4 helper T cells, "
        "leading to AIDS). Autoimmune: type 1 diabetes (insulin-making cells), rheumatoid arthritis, "
        "multiple sclerosis; State/Nationals add lupus, dermatomyositis, scleroderma, and "
        "psoriasis/psoriatic arthritis. Hypersensitivity types: I -- immediate, IgE and mast cells "
        "(allergies, anaphylaxis; treated with epinephrine); II -- antibodies against cell surfaces "
        "(transfusion reactions); III -- immune complexes deposit in tissues (lupus involves this); "
        "IV -- delayed, T-cell mediated (poison ivy, TB skin test).",
        "A bee sting causes swelling of the throat within minutes. Which hypersensitivity type? "
        "(Type I, IgE-mediated.)",
    ),
    lesson(
        "Advanced Immunology (State/Nationals)",
        "Transplants and rejection, and how the immune system is used against cancer.",
        "AUTOGRAFT -- tissue moved within the same person. ALLOGRAFT -- tissue from another person. "
        "MHC/HLA -- self-markers that must match for transplants. IMMUNOTHERAPY -- treatment that "
        "uses the immune system.",
        "Your immune system reads HLA proteins as name tags. Tissue with someone else's tags is "
        "attacked -- that's rejection -- so donors are matched and recipients take immunosuppressants.",
        "Rejection: hyperacute (minutes, pre-formed antibodies), acute (weeks to months, mainly T "
        "cells), chronic (months to years, gradual scarring). Graft-versus-host disease is the reverse "
        "-- donor immune cells (e.g. in a bone marrow transplant) attack the host. Autografts are not "
        "rejected. Cancer immunology: tumors evade the immune system by hiding antigens or using "
        "checkpoints like PD-1/PD-L1. Therapies: monoclonal antibodies (target tumor antigens, or "
        "checkpoint inhibitors that release the brakes on T cells) and CAR-T cells (a patient's own T "
        "cells engineered with a receptor for a tumor antigen). Cytokines are the signaling molecules "
        "(interleukins, interferons) that coordinate all of this.",
        "Why isn't a skin graft from your own thigh rejected? (It's an autograft -- same HLA, so the "
        "immune system reads it as self.)",
    ),
]

BOTANY = [
    lesson(
        "Plant Cell Structure",
        "The parts of a plant cell and what sets it apart from an animal cell.",
        "CELL WALL -- rigid layer outside the membrane, made of cellulose. CHLOROPLAST -- organelle of "
        "photosynthesis. CENTRAL VACUOLE -- large sac holding water and dissolved substances. "
        "PLASMODESMATA -- channels linking neighboring plant cells.",
        "Plant cells have everything animal cells have (nucleus, mitochondria, ER, Golgi, membrane) "
        "plus three extras: a cell wall, chloroplasts, and a large central vacuole.",
        "The central vacuole pushes against the wall to create turgor pressure, which keeps plants "
        "upright; losing water causes wilting (plasmolysis if severe). Primary walls are thin and "
        "flexible; some cells add a thick secondary wall with lignin (wood). Plant cells usually lack "
        "centrioles. Chloroplasts and mitochondria both have their own DNA and double membranes "
        "(evidence for endosymbiosis). Other plastids: chromoplasts (color) and amyloplasts (starch "
        "storage).",
        "A plant wilts on a hot day. What happened inside its cells? (Vacuoles lost water, turgor "
        "pressure dropped.)",
    ),
    lesson(
        "Tissue Systems & Organ Anatomy",
        "The three tissue systems and how roots, stems, and leaves are built.",
        "DERMAL TISSUE -- the protective outer layer (epidermis). VASCULAR TISSUE -- xylem and phloem. "
        "GROUND TISSUE -- everything else (parenchyma, collenchyma, sclerenchyma). MERISTEM -- a growth "
        "zone of dividing cells.",
        "Every plant organ -- root, stem, leaf -- is made of the same three tissue systems arranged "
        "differently. Growth happens at meristems: tips (length) and, in woody plants, a cambium "
        "(width).",
        "Ground tissue: parenchyma (living, thin walls -- photosynthesis, storage), collenchyma (uneven "
        "thick walls -- flexible support), sclerenchyma (thick lignified walls, often dead -- fibers "
        "and sclereids). Roots: root cap, root hairs, endodermis with the Casparian strip (forces water "
        "through cell membranes so the root controls what enters). Stems: vascular bundles in a ring "
        "(dicots) or scattered (monocots). Leaves: cuticle, upper epidermis, palisade mesophyll (most "
        "photosynthesis), spongy mesophyll (air spaces), lower epidermis with stomata and guard cells. "
        "Apical meristems lengthen; vascular and cork cambium thicken (secondary growth, tree rings).",
        "Which leaf layer does most photosynthesis? (Palisade mesophyll.)",
    ),
    lesson(
        "Photosynthesis & Plant Biochemistry",
        "How plants turn light, water, and CO2 into sugar.",
        "PHOTOSYNTHESIS: 6CO2 + 6H2O + light -> C6H12O6 + 6O2. CHLOROPHYLL -- the green pigment that "
        "absorbs red and blue light. STOMA -- leaf pore for gas exchange.",
        "Two stages: the light reactions capture light energy (making ATP and NADPH, and splitting "
        "water to release O2), and the Calvin cycle uses that energy to build sugar from CO2.",
        "Light reactions happen in the thylakoid membranes; the Calvin cycle in the stroma. Rubisco "
        "fixes CO2 but also grabs O2 (photorespiration, wasteful in heat). C4 plants (corn, sugarcane) "
        "fix CO2 first in mesophyll cells and pass it to bundle-sheath cells, cutting photorespiration. "
        "CAM plants (cacti, pineapple) open stomata at night and store CO2 as acids to save water. "
        "Plants also respire (in mitochondria) day and night. Accessory pigments (carotenoids) widen "
        "the light range. Limiting factors: light, CO2, temperature, and water.",
        "Why do CAM plants open their stomata at night? (To take in CO2 while it is cool and save "
        "water.)",
    ),
    lesson(
        "Water & Nutrient Transport",
        "How xylem pulls water up and phloem moves sugar around.",
        "XYLEM -- carries water and minerals up from roots (tracheids and vessel elements, dead at "
        "maturity). PHLOEM -- carries sugars (sieve-tube elements with companion cells, alive). "
        "TRANSPIRATION -- water evaporating from leaves.",
        "Water is pulled up, not pushed. As water evaporates from leaves, it tugs the water column "
        "behind it all the way from the roots, because water molecules stick together.",
        "Cohesion-tension theory: transpiration creates tension, cohesion (water to water) and "
        "adhesion (water to xylem walls) keep the column intact. Root pressure gives a small push "
        "(guttation). Guard cells open stomata when they take in K+ and water and swell; they close "
        "under drought (signaled by abscisic acid). Phloem follows the pressure-flow model: sugar is "
        "loaded at a source (leaf), water follows by osmosis, building pressure that pushes sap toward "
        "a sink (roots, fruits, growing tips). Minerals enter roots via the apoplast (walls) or "
        "symplast (cytoplasm), but must cross the endodermis membranes at the Casparian strip.",
        "A tree is girdled (a ring of bark and phloem removed). What eventually happens to the roots? "
        "(They starve -- sugar can no longer reach them.)",
    ),
    lesson(
        "Plant Reproduction",
        "Flowers, spores, seeds, fruits, and the difference between sexual and asexual reproduction.",
        "ALTERNATION OF GENERATIONS -- life cycle switching between a haploid gametophyte and a "
        "diploid sporophyte. STAMEN -- male part (anther + filament). CARPEL/PISTIL -- female part "
        "(stigma, style, ovary).",
        "All plants alternate between two forms. In mosses the gametophyte is the main plant; in ferns "
        "and seed plants the sporophyte dominates. Flowering plants use flowers, seeds, and fruits to "
        "reproduce.",
        "Pollination moves pollen to the stigma (wind, insects, birds). Angiosperms use double "
        "fertilization: one sperm fertilizes the egg (zygote -> embryo), the other fuses with two polar "
        "nuclei (triploid endosperm, food for the seed). The ovule becomes the seed; the ovary becomes "
        "the fruit. Seeds disperse by wind, water, animals, or bursting pods. Asexual (vegetative) "
        "reproduction: runners/stolons (strawberries), rhizomes, tubers (potatoes), bulbs, cuttings, "
        "grafting -- offspring are clones. Sexual reproduction adds genetic variety; asexual is fast "
        "and keeps a successful genotype.",
        "In a flowering plant, what does the ovary become after fertilization? (The fruit.)",
    ),
    lesson(
        "Plant Genetics & GMOs",
        "Inheritance in plants, breeding, and genetically modified crops.",
        "GENE -- a DNA segment coding for a trait. ALLELE -- a version of a gene. GMO -- an organism "
        "whose DNA was changed with genetic engineering. HYBRID -- offspring of two different parents "
        "or varieties.",
        "Mendel worked out inheritance with pea plants. People have shaped crops for thousands of "
        "years by selective breeding; genetic engineering changes genes directly and faster.",
        "Punnett squares predict offspring ratios (3:1 for a monohybrid cross, 9:3:3:1 for a "
        "dihybrid). Many plants tolerate polyploidy (extra chromosome sets -- wheat is hexaploid), "
        "which often gives larger plants. Genetic engineering tools: Agrobacterium tumefaciens carries "
        "genes into plant cells; the gene gun; CRISPR gene editing. Examples: Bt crops (make an "
        "insecticidal protein), herbicide-tolerant soybeans, Golden Rice (beta-carotene). Debated "
        "issues: gene flow to wild relatives, pest resistance, seed costs, and labeling, weighed "
        "against higher yields and less spraying.",
        "Why do Bt crops need less insecticide spraying? (They make their own insect-killing protein "
        "from a Bacillus thuringiensis gene.)",
    ),
    lesson(
        "Taxonomy & Monocots vs Dicots",
        "The major plant groups, the big evolutionary steps, and how to tell monocots from dicots.",
        "BRYOPHYTES -- nonvascular (mosses, liverworts, hornworts). PTERIDOPHYTES -- seedless vascular "
        "(ferns, horsetails, club mosses). GYMNOSPERMS -- naked seeds (conifers, cycads, ginkgo). "
        "ANGIOSPERMS -- flowering plants.",
        "Plant evolution added features in steps: first vascular tissue (to grow tall), then seeds "
        "(no need for water to reproduce), then flowers and fruit (helpers for pollination and "
        "dispersal).",
        "Key transitions: cuticle and stomata (life on land), vascular tissue, seeds, pollen, flowers. "
        "Monocots: one cotyledon, parallel leaf veins, scattered vascular bundles, flower parts in "
        "threes, fibrous roots (grasses, lilies, orchids). Dicots (eudicots): two cotyledons, net "
        "veins, vascular bundles in a ring, flower parts in fours or fives, often a taproot (roses, "
        "beans, oaks). Naming is binomial (Genus species, italicized, genus capitalized).",
        "A plant has parallel veins and flower parts in threes. Monocot or dicot? (Monocot.)",
    ),
    lesson(
        "Paleobotany & Plant Evolution",
        "What fossils tell us about how plants changed over time.",
        "PALEOBOTANY -- the study of fossil plants. CHAROPHYTES -- green algae most closely related to "
        "land plants. CARBONIFEROUS -- the period of great coal-forming swamp forests.",
        "Land plants evolved from green algae about 470 million years ago. Fossils show a sequence: "
        "small nonvascular plants, then vascular plants, then forests, seed plants, and finally "
        "flowering plants.",
        "Early vascular fossils such as Cooksonia (Silurian) and the Rhynie chert (Devonian) preserve "
        "simple branching stems. The Devonian saw the first trees (Archaeopteris). Carboniferous "
        "swamps of giant club mosses (Lepidodendron) and horsetails (Calamites) became coal. "
        "Gymnosperms dominated the Mesozoic; angiosperms spread rapidly in the Cretaceous. Fossil "
        "types: compressions, impressions, petrifactions (permineralized), casts, pollen and spores "
        "(palynology). Pollen records help reconstruct past climates.",
        "Which group of plants formed most Carboniferous coal swamps? (Giant seedless vascular "
        "plants -- club mosses and horsetails, plus tree ferns.)",
    ),
    lesson(
        "Plant Ecology & Diseases",
        "Nutrient cycles, competition, pollination, and plant diseases and deficiencies.",
        "NITROGEN FIXATION -- turning N2 gas into usable nitrogen. MYCORRHIZAE -- fungi partnering "
        "with roots. ALLELOPATHY -- one plant releasing chemicals that harm others. PATHOGEN -- a "
        "disease-causing organism.",
        "Plants depend on cycles of carbon, nitrogen, and water, compete for light and nutrients, and "
        "trade with animals and fungi for pollination and nutrients. They also get sick, and the 2027 "
        "list includes plant diseases and deficiencies.",
        "Rhizobium bacteria in legume root nodules fix nitrogen. Mycorrhizal fungi trade minerals "
        "(especially phosphorus) for sugar. Pollination syndromes: bees (blue/yellow, UV guides), "
        "hummingbirds (red, tubular, no scent), moths (white, night scent), wind (small, no petals, "
        "lots of pollen). Deficiencies: nitrogen -- yellowing of older leaves first; magnesium -- "
        "yellow between veins (chlorophyll's central atom); iron -- yellowing of young leaves; "
        "phosphorus -- purplish leaves, poor roots; potassium -- browned leaf edges. Diseases: fungal "
        "(rusts, powdery mildew, late blight of potato -- an oomycete), bacterial (fire blight), viral "
        "(tobacco mosaic virus).",
        "Older leaves turn yellow first while young leaves stay green. Likely deficiency? (Nitrogen -- "
        "it's mobile, so the plant moves it to new growth.)",
    ),
    lesson(
        "Applied Botany",
        "How people use plants for food, gardens, aquaculture, and medicine.",
        "HORTICULTURE -- growing fruits, vegetables, and ornamentals. AGRONOMY -- field crops. "
        "HYDROPONICS -- growing plants in nutrient water without soil. PHYTOCHEMICAL -- a "
        "plant-made compound.",
        "Nearly all human food traces back to plants. A few crops -- rice, wheat, and corn -- supply "
        "most calories worldwide.",
        "Food parts: roots (carrot), tubers (potato -- a stem), leaves (lettuce), seeds (grains, "
        "legumes), fruits (tomato is botanically a fruit). Horticulture techniques: grafting, "
        "cuttings, pruning, and plant hormones (auxin for rooting, ethylene to ripen fruit, "
        "gibberellins for growth). Hydroponics and aquaponics (fish waste feeds plants) save water. "
        "Aquaculture also uses seaweeds and algae. Medicines from plants: aspirin (from willow bark's "
        "salicin), quinine (cinchona bark, malaria), digoxin (foxglove, heart), morphine (opium "
        "poppy), taxol (Pacific yew, cancer). Fibers and materials: cotton, flax, wood, rubber.",
        "Which plant hormone is used to ripen bananas after shipping? (Ethylene.)",
    ),
    lesson(
        "Plant Diversity & Conservation",
        "Why plant diversity matters and how it is protected.",
        "BIODIVERSITY -- the variety of life. ENDEMIC -- found naturally in only one place. INVASIVE "
        "SPECIES -- a non-native species that spreads and causes harm. SEED BANK -- a stored collection "
        "of seeds.",
        "Plants make oxygen, food, medicine, and habitat. Losing species means losing those options -- "
        "and many plants are threatened by habitat loss, invasive species, and climate change.",
        "Threats: habitat destruction, invasive species (kudzu, purple loosestrife), overharvesting, "
        "pollinator decline, and climate change shifting ranges. Biodiversity hotspots hold many "
        "endemic species. Protection: in situ (in the wild -- parks, reserves) and ex situ (outside the "
        "wild -- botanic gardens, seed banks such as the Svalbard Global Seed Vault). Laws and lists: "
        "the U.S. Endangered Species Act, the IUCN Red List categories (Least Concern up to Extinct), "
        "and CITES for trade. Crop wild relatives keep genes for disease resistance.",
        "Storing seeds in a vault is in situ or ex situ conservation? (Ex situ.)",
    ),
    lesson(
        "Microscopy, Dichotomous Keys & Terminology",
        "The lab skills Botany tests: using a microscope, running a key, and naming parts correctly.",
        "DICHOTOMOUS KEY -- a series of two-choice steps that leads to an identification. "
        "MAGNIFICATION -- how much larger the image is. RESOLUTION -- how much detail can be told apart.",
        "Many stations ask you to identify a specimen or structure. A dichotomous key works like a "
        "flowchart: read both choices, pick the one that fits, follow it to the next step.",
        "Total magnification = ocular lens x objective lens (10x x 40x = 400x). Start on low power, "
        "focus with the coarse knob, then switch up and use only the fine knob. Leaf terms to know: "
        "simple vs compound (pinnate, palmate), arrangement (alternate, opposite, whorled), margin "
        "(entire, serrate, lobed), venation (parallel, pinnate, palmate). Flower terms: sepals, petals, "
        "stamens, carpels; superior vs inferior ovary; complete (all four parts) vs incomplete. Use "
        "binder pages for keys and labeled diagrams -- most of the points come from careful "
        "observation.",
        "With a 10x eyepiece and a 40x objective, what is the total magnification? (400x.)",
    ),
]

DISEASE_DETECTIVES = [
    lesson(
        "Clinical vs Public Health Approach",
        "How public health looks at whole populations, and the jobs epidemiologists do.",
        "EPIDEMIOLOGY -- the study of how disease is distributed in populations and what determines "
        "it. CLINICAL MEDICINE -- care for one patient. POPULATION -- a defined group of people.",
        "A doctor asks, \"What's wrong with this patient?\" An epidemiologist asks, \"Why are these "
        "people getting sick, and how do we stop it?\" Public health's patient is the community.",
        "Clinical approach: diagnose and treat individuals. Public health approach: surveillance -> "
        "find risk factors -> develop interventions -> implement and evaluate. Epidemiology is "
        "described by person, place, and time (who, where, when), and analytic epidemiology asks why "
        "and how. Core functions include assessment (monitoring health), policy development, and "
        "assurance. Epidemiologists investigate outbreaks, run surveillance, design studies, and "
        "evaluate programs. Problem solving in Disease Detectives follows the same logic: define the "
        "problem, collect data, analyze, interpret, and recommend actions.",
        "A clinic treats 20 people for food poisoning. Which question is the public-health one: "
        "\"What antibiotic?\" or \"What food did they share?\" (The shared food.)",
    ),
    lesson(
        "History of Epidemiology",
        "The people and investigations that built the field.",
        "OBSERVATION -- noticing patterns. NATURAL EXPERIMENT -- a comparison that happens on its own "
        "rather than by design. GERM THEORY -- diseases are caused by microbes.",
        "Epidemiology grew from people who noticed patterns in who got sick and then tested their "
        "ideas -- often before anyone knew germs existed.",
        "Hippocrates linked disease to environment. John Graunt analyzed London's bills of mortality "
        "(1600s). James Lind ran an early controlled trial of citrus for scurvy (1747). Edward Jenner "
        "developed smallpox vaccination (1796). Ignaz Semmelweis cut childbirth fever with "
        "handwashing. John Snow mapped the 1854 Broad Street cholera outbreak and linked it to a water "
        "pump -- the father of field epidemiology. William Farr built vital statistics. Pasteur and "
        "Koch established germ theory. Later: Doll and Hill linked smoking to lung cancer (1950s); "
        "the Framingham Heart Study tracked heart-disease risk factors.",
        "What did John Snow do at Broad Street that still defines field epidemiology? (Mapped cases "
        "and linked them to a contaminated pump -- and had its handle removed.)",
    ),
    lesson(
        "Natural History & Spectrum of Disease",
        "How a disease develops over time, from exposure to outcome.",
        "INCUBATION PERIOD -- time from infection to symptoms (infectious disease). LATENCY PERIOD -- "
        "the same idea for chronic disease. SUBCLINICAL -- infected without symptoms. CARRIER -- can "
        "spread disease without being sick.",
        "Diseases follow a natural history: susceptibility -> exposure -> subclinical disease -> "
        "clinical disease -> recovery, disability, or death. Not everyone who is infected gets sick.",
        "Spectrum of disease runs from no symptoms, to mild, to severe, to fatal. The iceberg concept: "
        "visible cases are only the tip; many infections are unseen. Carriers: incubatory (during the "
        "incubation period), convalescent (after recovery), and chronic. Levels of prevention map onto "
        "the natural history: primary (prevent exposure or disease -- vaccines), secondary (detect "
        "early -- screening), tertiary (reduce disability once sick -- rehabilitation).",
        "A screening mammogram is which level of prevention? (Secondary -- early detection.)",
    ),
    lesson(
        "Infectious & Noninfectious Causes",
        "The epidemiologic triad, chains of infection, and causes beyond germs.",
        "AGENT -- the cause (microbe, chemical, physical force). HOST -- the person. ENVIRONMENT -- "
        "outside factors that bring them together. RESERVOIR -- where an agent normally lives.",
        "Disease happens when an agent, a susceptible host, and the right environment meet -- the "
        "epidemiologic triad. Break any link, and you prevent disease.",
        "Chain of infection: agent -> reservoir (humans, animals, environment) -> portal of exit -> "
        "mode of transmission -> portal of entry -> susceptible host. Transmission is direct (contact, "
        "droplet) or indirect (airborne, vehicle such as food or water, vector such as mosquitoes or "
        "ticks). Zoonoses jump from animals to people. Noninfectious causes: genetics, behavior "
        "(smoking, diet, inactivity), environmental exposures (lead, air pollution, radiation), and "
        "injuries. Chronic diseases usually have many contributing causes (the web of causation).",
        "Mosquitoes carrying West Nile virus are what kind of transmission? (Indirect -- vector-borne.)",
    ),
    lesson(
        "Epidemiological Terminology",
        "The vocabulary the test uses -- learn these precisely.",
        "ENDEMIC -- the usual, constant level in an area. EPIDEMIC/OUTBREAK -- more cases than "
        "expected (outbreak is usually local). PANDEMIC -- an epidemic across countries or "
        "continents. CLUSTER -- cases grouped in place and time.",
        "Many questions turn on one exact word. Learn the CDC glossary terms well enough to use them "
        "in a sentence.",
        "Incidence -- NEW cases in a time period. Prevalence -- ALL existing cases at a point in time "
        "(prevalence ~ incidence x average duration). Case definition -- standard criteria (clinical, "
        "plus person, place, time) for counting a case, sorted as confirmed, probable, or possible. "
        "Index case -- the first case to come to attention; primary case -- the one who brought the "
        "disease in; secondary cases -- those infected by them. Morbidity -- illness; mortality -- "
        "death. Sporadic -- irregular, occasional cases. Hyperendemic -- persistently high levels. "
        "Herd immunity, attack rate, and case-fatality rate get their own chapters.",
        "Diabetes in a town: 500 people have it now; 40 were diagnosed this year. Which is "
        "prevalence? (500 -- all existing cases.)",
    ),
    lesson(
        "Surveillance",
        "Ongoing collection and use of health data -- its purpose, steps, and types.",
        "PUBLIC HEALTH SURVEILLANCE -- the ongoing, systematic collection, analysis, interpretation, "
        "and sharing of health data for action. NOTIFIABLE DISEASE -- one doctors and labs must "
        "report.",
        "Surveillance is how health departments notice that something unusual is happening. Its "
        "purpose is action, not just counting.",
        "Five steps: (1) collect data, (2) compile and organize it, (3) analyze and interpret it, "
        "(4) disseminate results to those who need them, (5) use them for action and evaluation. "
        "Types: passive (providers report on their own -- cheap, often incomplete), active (the "
        "health department contacts providers -- more complete, costly), sentinel (selected sites "
        "report, e.g. flu clinics), and syndromic (tracks symptoms such as ER visits for fever before "
        "diagnoses are confirmed). Uses: detect outbreaks, track trends, set priorities, evaluate "
        "programs. Good systems are timely, sensitive, representative, and simple.",
        "A health department phones every hospital weekly to ask about measles cases. Active or "
        "passive? (Active.)",
    ),
    lesson(
        "Study Designs",
        "Experimental and observational studies, and when to use each.",
        "EXPERIMENTAL STUDY -- the investigator assigns the exposure (e.g. a randomized controlled "
        "trial). OBSERVATIONAL STUDY -- the investigator only observes. COHORT -- starts from "
        "exposure. CASE-CONTROL -- starts from disease.",
        "If you assign who gets the treatment, it's experimental. If you just watch what people "
        "already do, it's observational.",
        "Randomized controlled trial: the gold standard; randomization balances confounders; blinding "
        "reduces bias. Cohort: follow exposed and unexposed groups forward (prospective) or through "
        "records (retrospective); gives incidence and relative risk. Case-control: compare people "
        "with the disease to people without, looking back at exposures; fast and good for rare "
        "diseases; gives odds ratios. Cross-sectional: a snapshot at one time; gives prevalence, can't "
        "show which came first. Ecological: compares groups, not individuals (beware the ecological "
        "fallacy). State/Nationals: study design, bias, error, and confounding in depth.",
        "Researchers compare 50 people with a rare cancer to 100 without, asking about past "
        "exposures. Which design? (Case-control.)",
    ),
    lesson(
        "Steps of an Outbreak Investigation",
        "The standard sequence for investigating an outbreak.",
        "LINE LIST -- a table with one row per case. HYPOTHESIS -- a testable explanation. CONTROL "
        "MEASURE -- an action to stop spread.",
        "Investigators follow a checklist so nothing is missed. Control measures can start at any "
        "step -- you don't wait for proof if people are getting sick.",
        "CDC's steps: (1) prepare for field work, (2) establish the existence of an outbreak (compare "
        "to expected numbers), (3) verify the diagnosis, (4) construct a working case definition, "
        "(5) find cases systematically and record them in a line list, (6) do descriptive "
        "epidemiology (person, place, time; epi curve), (7) develop hypotheses, (8) evaluate them "
        "(analytic study -- cohort or case-control), (9) refine hypotheses and do more studies if "
        "needed, (10) implement control and prevention measures, (11) keep up surveillance, "
        "(12) communicate findings.",
        "Before doing anything else in step 2, what must you compare the case count to? (The "
        "expected, baseline number of cases.)",
    ),
    lesson(
        "Epi Curves, Line Lists & Cluster Maps",
        "Reading outbreak data from tables, graphs, and maps.",
        "EPI CURVE -- a histogram of cases by onset date. POINT SOURCE -- everyone exposed at once. "
        "PROPAGATED -- person-to-person spread. SPOT MAP -- cases plotted where they live or were "
        "exposed.",
        "The shape of an epi curve tells you how the disease spread. A single sharp peak means one "
        "shared exposure; several growing peaks mean people passed it to each other.",
        "Point-source: a sharp rise and fall within about one incubation period. Continuous common "
        "source: a plateau that ends when the source is removed. Propagated: successive peaks about "
        "one incubation period apart. Intermittent: irregular peaks. Use the epi curve to estimate the "
        "exposure time: count back one median incubation period from the peak (or the minimum period "
        "from the first case and the maximum from the last). Line lists show who (age, sex), what "
        "(symptoms), when (onset), and where. Spot maps reveal clustering near a source (as in Snow's "
        "cholera map).",
        "An epi curve shows peaks on days 2, 9, and 16 with rising height. Pattern? (Propagated -- "
        "person to person, about a 7-day incubation.)",
    ),
    lesson(
        "Measures of Frequency & Association",
        "Attack rates, risk, relative risk, and odds ratios -- the core calculations.",
        "RATE -- cases per population in a time period. ATTACK RATE -- the percentage of an exposed "
        "group who got sick. RELATIVE RISK (RR) -- risk in exposed / risk in unexposed. ODDS RATIO (OR) "
        "-- the odds of exposure among cases / among controls.",
        "Most outbreak calculations come from a 2x2 table: exposed or not, sick or not. Find which food "
        "has the highest attack rate among eaters and the biggest gap versus non-eaters.",
        "2x2 table: a = exposed and sick, b = exposed and well, c = unexposed and sick, d = unexposed "
        "and well. Attack rate (exposed) = a/(a+b); (unexposed) = c/(c+d). RR = [a/(a+b)] / [c/(c+d)] "
        "(cohort). OR = (a x d) / (b x c) (case-control). RR or OR = 1 means no association; > 1 means "
        "the exposure is a risk factor; < 1 means protective. Case-fatality rate = deaths / cases. "
        "Example: 40 of 50 who ate potato salad got sick (80%) vs 5 of 50 who didn't (10%): RR = "
        "0.80 / 0.10 = 8.",
        "Cases: 30 exposed, 10 unexposed; controls: 20 exposed, 40 unexposed. OR? ((30 x 40) / "
        "(10 x 20) = 6.)",
    ),
    lesson(
        "Causation Criteria",
        "Frameworks for deciding whether an association is truly causal.",
        "ASSOCIATION -- two things occurring together. CAUSATION -- one actually produces the other. "
        "TEMPORALITY -- the cause must come before the effect.",
        "A strong link isn't proof of cause. Epidemiologists use checklists to judge how convincing "
        "the evidence is.",
        "Bradford Hill criteria: strength, consistency, specificity, temporality (the only required "
        "one), biological gradient (dose-response), plausibility, coherence, experiment, and analogy. "
        "Koch's postulates (for microbes): the organism is found in all cases, can be isolated and "
        "grown, causes disease when introduced to a healthy host, and can be re-isolated from it -- "
        "limited because some microbes can't be cultured and some infections show no symptoms. Evans's "
        "postulates update Koch's for modern evidence, including immune responses and chronic "
        "disease. GRADE rates the quality of a body of evidence (high, moderate, low, very low), with "
        "randomized trials starting high and observational studies starting low.",
        "Which Bradford Hill criterion must always hold? (Temporality.)",
    ),
    lesson(
        "Bias, Confounding & Study Limits (State/Nationals)",
        "What can make a study's answer wrong, and how to guard against it.",
        "BIAS -- a systematic error. CONFOUNDER -- a third factor linked to both exposure and outcome. "
        "RANDOM ERROR -- chance variation, reduced by larger samples.",
        "A study can get the wrong answer because of who was chosen, how information was collected, "
        "or a hidden third factor. Spotting these is a big part of the State/Nationals test.",
        "Selection bias: the study groups differ in ways that matter (e.g. healthy-worker effect, "
        "loss to follow-up). Information bias: errors in measuring exposure or outcome -- recall bias "
        "(cases remember exposures better), interviewer bias, and misclassification. Confounding: "
        "e.g. coffee seems linked to lung cancer because coffee drinkers smoke more. Control "
        "confounding with randomization, restriction, matching, stratification, or statistical "
        "adjustment. Effect modification is different: the effect truly varies by group. Also know "
        "precision vs validity, and that confidence intervals and p-values describe random error, not "
        "bias.",
        "Mothers of babies with birth defects recall medications better than other mothers. What "
        "bias? (Recall bias.)",
    ),
    lesson(
        "Herd Immunity & Vaccine Effectiveness (State/Nationals)",
        "How immunity protects a community, and how to calculate vaccine effectiveness.",
        "HERD IMMUNITY -- protection of unvaccinated people because enough others are immune. "
        "VACCINE EFFICACY -- protection measured in a controlled trial. VACCINE EFFECTIVENESS -- "
        "protection in real-world use.",
        "If most people are immune, a disease can't find enough new hosts to keep spreading, so even "
        "people who can't be vaccinated are protected.",
        "Herd immunity threshold = 1 - 1/R0. Measles (R0 about 12-18) needs about 92-95% immunity; "
        "an R0 of 4 needs 75%. Vaccine efficacy/effectiveness = (ARU - ARV) / ARU x 100%, where ARU = "
        "attack rate in the unvaccinated and ARV = attack rate in the vaccinated. Equivalently VE = "
        "(1 - RR) x 100%. In case-control data, VE = (1 - OR) x 100%. Example: ARU = 20%, ARV = 2% -> "
        "VE = (20 - 2)/20 = 90%. Vaccinated cases can be common simply because most people are "
        "vaccinated -- always compare rates, not counts.",
        "Attack rate is 10% among the unvaccinated and 3% among the vaccinated. VE? ((10 - 3)/10 = "
        "70%.)",
    ),
    lesson(
        "Reproductive Numbers (R0 and Re)",
        "How many people one case infects, and why it matters.",
        "R0 (BASIC REPRODUCTION NUMBER) -- average new infections from one case in a fully susceptible "
        "population. Re or Rt (EFFECTIVE REPRODUCTION NUMBER) -- the same, in the real, partly immune "
        "population at a given time.",
        "If each case infects more than one other person (R > 1), the outbreak grows. Below 1, it "
        "shrinks. The goal of control measures is to push R below 1.",
        "R0 depends on contacts per unit time, the probability of transmission per contact, and how "
        "long a person is infectious (R0 = c x p x d). Re = R0 x the fraction still susceptible "
        "(roughly). Vaccination, isolation, masking, and treatment lower Re. Examples (approximate): "
        "measles 12-18, chickenpox 10-12, seasonal flu about 1-2. The serial interval (time between "
        "symptom onsets in successive cases) sets how fast generations of cases occur.",
        "R0 = 4 and half the population is immune. Approximate Re? (4 x 0.5 = 2 -- still growing.)",
    ),
    lesson(
        "Prevention & Disease Control",
        "The tools public health uses to stop disease.",
        "ISOLATION -- separating sick people. QUARANTINE -- separating exposed people who may become "
        "sick. PROPHYLAXIS -- preventive treatment.",
        "Control measures target a link in the chain of infection: remove the source, block "
        "transmission, or protect the susceptible host.",
        "Levels: primary (vaccination, clean water, food safety, health education), secondary "
        "(screening, early treatment, contact tracing), tertiary (rehabilitation, managing chronic "
        "disease). Infectious-disease control: isolation and quarantine, contact tracing, recalls of "
        "contaminated food, vector control (draining standing water, insecticides), handwashing and "
        "PPE, prophylactic antibiotics or antivirals. Chronic disease: tobacco control, nutrition "
        "policy, physical activity programs, and laws (seat belts, smoke-free air). Many measures are "
        "combined (\"layers\").",
        "Asking a healthy person exposed to measles to stay home for 21 days is isolation or "
        "quarantine? (Quarantine -- they are exposed, not yet sick.)",
    ),
    lesson(
        "Evaluating Interventions with Pre/Post Data",
        "Judging whether a prevention program actually worked.",
        "PRE/POST COMPARISON -- measuring before and after an intervention. COMPARISON GROUP -- a "
        "similar group that didn't get the intervention. SECULAR TREND -- a change that would have "
        "happened anyway.",
        "Cases going down after a program started doesn't prove the program worked. You need to rule "
        "out other explanations.",
        "Compare the percent change: (post - pre) / pre x 100%. Better: compare against a similar "
        "group without the intervention (difference-in-differences). Threats: secular trends, "
        "regression to the mean (programs often start when rates are unusually high), seasonal "
        "patterns, changes in case definitions or testing, and other simultaneous programs. Evaluate "
        "on outcomes (fewer cases), process (was it delivered as planned?), and cost. A clear "
        "conclusion states the change, the comparison, the limits, and a recommendation.",
        "Flu cases fell 30% after a school handwashing program, but also fell 25% in schools without "
        "it. How much of the drop is plausibly due to the program? (About 5 percentage points -- most "
        "was the seasonal trend.)",
    ),
]

HEREDITY = [
    lesson(
        "DNA Structure & Base Pairing",
        "The double helix and its pairing rules.",
        "NUCLEOTIDE -- a phosphate, a deoxyribose sugar, and a base. BASES -- adenine (A), thymine "
        "(T), guanine (G), cytosine (C). COMPLEMENTARY PAIRING -- A with T, G with C.",
        "DNA is a twisted ladder. The sides are sugar-phosphate backbones; the rungs are base pairs. "
        "Because A always pairs with T and G with C, one strand tells you the other.",
        "The two strands are antiparallel (one runs 5' to 3', the other 3' to 5'). A-T pairs have two "
        "hydrogen bonds; G-C pairs have three, so GC-rich DNA is more stable. Purines (A, G) have two "
        "rings; pyrimidines (C, T, and U in RNA) have one -- a purine always pairs with a pyrimidine. "
        "Chargaff's rules: %A = %T and %G = %C. Key history: Griffith (transformation), Avery-MacLeod-"
        "McCarty (DNA is the transforming factor), Hershey-Chase (DNA is the genetic material of "
        "phages), Franklin and Wilkins (X-ray data), Watson and Crick (the model, 1953). DNA wraps "
        "around histones to form chromatin.",
        "A DNA sample is 30% adenine. What percent is guanine? (A = T = 30%, so G + C = 40%, and G = "
        "20%.)",
    ),
    lesson(
        "DNA Replication",
        "How a cell copies its DNA accurately before dividing.",
        "SEMICONSERVATIVE -- each new DNA has one old and one new strand. HELICASE -- unzips. DNA "
        "POLYMERASE -- adds nucleotides. PRIMER -- a short RNA starter.",
        "The helix unzips, and each strand serves as a template for a new partner strand, so you end "
        "up with two identical copies.",
        "Meselson and Stahl proved replication is semiconservative. Steps: helicase unwinds at the "
        "origin; single-strand binding proteins hold strands apart; topoisomerase relieves twisting; "
        "primase lays an RNA primer; DNA polymerase III extends only in the 5' to 3' direction. The "
        "leading strand is made continuously; the lagging strand in Okazaki fragments, which DNA "
        "polymerase I (replacing primers) and ligase join. DNA polymerase proofreads, giving an error "
        "rate around 1 in a billion. Telomeres and telomerase protect chromosome ends in eukaryotes.",
        "Why is the lagging strand made in pieces? (Polymerase can only build 5' to 3', which runs "
        "away from the opening fork on that strand.)",
    ),
    lesson(
        "Transcription & RNA Processing",
        "Making an RNA copy of a gene, then preparing it for use.",
        "TRANSCRIPTION -- DNA -> RNA. RNA POLYMERASE -- the enzyme that builds RNA. PROMOTER -- the DNA "
        "start signal. mRNA -- messenger RNA, carrying the code to ribosomes.",
        "A gene is read like a recipe card. RNA polymerase copies one gene into mRNA, using U in place "
        "of T. In eukaryotes the mRNA is edited before it leaves the nucleus.",
        "RNA polymerase binds the promoter (in eukaryotes with transcription factors at the TATA box), "
        "reads the template strand 3' to 5', and builds RNA 5' to 3'. The mRNA matches the coding "
        "strand (with U for T). Eukaryotic processing: a 5' cap, a 3' poly-A tail, and splicing -- "
        "introns removed, exons joined (by the spliceosome). Alternative splicing lets one gene make "
        "several proteins. RNA types: mRNA, tRNA, rRNA. State/Nationals: the lac operon (bacterial "
        "genes switched on when lactose is present -- the repressor is released); Nationals: the trp "
        "operon (switched off when tryptophan is plentiful).",
        "Template strand 3'-TACGGA-5'. What mRNA is made? (5'-AUGCCU-3'.)",
    ),
    lesson(
        "Translation & Protein Synthesis",
        "How ribosomes read mRNA codons to build a protein.",
        "CODON -- three mRNA bases coding for one amino acid. ANTICODON -- the matching three bases on "
        "a tRNA. START CODON -- AUG (methionine). STOP CODONS -- UAA, UAG, UGA.",
        "The ribosome reads mRNA three letters at a time. Each tRNA brings the matching amino acid, "
        "and the ribosome links them into a chain until it hits a stop codon.",
        "Initiation: the small ribosomal subunit binds the mRNA, finds AUG, and the large subunit "
        "joins. Elongation: tRNAs enter the A site, peptide bonds form, the chain shifts from P to E "
        "sites. Termination: a release factor binds the stop codon. The code is redundant (64 codons, "
        "20 amino acids) and nearly universal. Use the codon wheel or table carefully: read from the "
        "center outward, 5' to 3'. Proteins then fold and may be modified in the ER and Golgi.",
        "mRNA 5'-AUG UUU GGC UAA-3'. How many amino acids in the protein? (3 -- UAA is a stop.)",
    ),
    lesson(
        "Mutations",
        "Types of DNA changes and what they do to proteins.",
        "POINT MUTATION -- a single base change. SILENT -- no change in amino acid. MISSENSE -- a "
        "different amino acid. NONSENSE -- an early stop codon. FRAMESHIFT -- an insertion or "
        "deletion not in multiples of three.",
        "A mutation is a change in DNA. Some do nothing, some change one amino acid, and some wreck "
        "the whole protein.",
        "Substitutions: transitions (purine to purine) and transversions. Sickle-cell anemia is a "
        "missense mutation (glutamic acid -> valine in hemoglobin). Frameshifts change every codon "
        "after them and usually cause early stops. Chromosomal mutations: deletion, duplication, "
        "inversion, translocation; nondisjunction causes aneuploidy (Down syndrome = trisomy 21). "
        "Causes: replication errors, chemical mutagens, radiation. State/Nationals: UV light makes "
        "thymine dimers, fixed by nucleotide excision repair (defective in xeroderma pigmentosum).",
        "Which is usually worse, a one-base substitution or a one-base deletion in the middle of a "
        "gene? (The deletion -- it shifts the reading frame.)",
    ),
    lesson(
        "Mendelian Genetics & Punnett Squares",
        "Dominant and recessive alleles and predicting offspring ratios.",
        "GENOTYPE -- the alleles (e.g. Aa). PHENOTYPE -- the trait you see. HOMOZYGOUS -- two same "
        "alleles; HETEROZYGOUS -- two different. DOMINANT -- shows with one copy.",
        "Each parent passes on one allele for each gene. A Punnett square lists every combination, "
        "which gives the chance of each genotype.",
        "Law of segregation: allele pairs separate in gametes. Law of independent assortment: genes "
        "on different chromosomes sort independently. Monohybrid Aa x Aa: 1 AA : 2 Aa : 1 aa, so 3:1 "
        "phenotypes. Dihybrid AaBb x AaBb: 9:3:3:1. Test cross: cross with aa to reveal an unknown "
        "genotype. Probability rules: multiply for \"and\" (independent events), add for \"or\" "
        "(mutually exclusive). Shortcut: P(aabb from AaBb x AaBb) = 1/4 x 1/4 = 1/16.",
        "AaBbCc x AaBbCc: chance of an aabbcc offspring? ((1/4)^3 = 1/64.)",
    ),
    lesson(
        "Pedigree Analysis",
        "Reading family trees to find how a trait is inherited.",
        "PEDIGREE -- a family chart. Squares = males, circles = females, shaded = affected. "
        "AUTOSOMAL -- on a non-sex chromosome. X-LINKED -- on the X chromosome. CARRIER -- has one "
        "recessive allele, unaffected.",
        "Look for clues: does the trait skip generations? Does it affect mostly males? Do two "
        "unaffected parents have an affected child?",
        "Autosomal recessive: skips generations; unaffected parents can have an affected child (both "
        "carriers); both sexes equally (cystic fibrosis). Autosomal dominant: every affected person "
        "has an affected parent; doesn't skip (Huntington's). X-linked recessive: mostly males; "
        "passed from carrier mothers; never father to son (hemophilia, red-green color blindness). "
        "X-linked dominant: affected fathers pass it to ALL daughters. Y-linked: father to every son. "
        "Mitochondrial: from the mother to all her children. Work out genotypes generation by "
        "generation and compute probabilities for new children.",
        "Two unaffected parents have an affected daughter. Dominant or recessive, autosomal or "
        "X-linked? (Autosomal recessive -- an X-linked recessive daughter would need an affected "
        "father.)",
    ),
    lesson(
        "Mitosis & Meiosis",
        "The two kinds of cell division and how they differ.",
        "MITOSIS -- one division making two identical diploid cells. MEIOSIS -- two divisions making "
        "four genetically different haploid gametes. HOMOLOGOUS CHROMOSOMES -- matching pairs, one "
        "from each parent.",
        "Mitosis is for growth and repair: copy and split. Meiosis is for making eggs and sperm: it "
        "halves the chromosome number and shuffles the genes.",
        "Interphase (G1, S -- DNA copied, G2) comes first. Mitosis: prophase, metaphase (chromosomes "
        "line up), anaphase (sister chromatids pull apart), telophase, then cytokinesis. Meiosis I "
        "separates homologous pairs (reductional); meiosis II separates sister chromatids. Variation "
        "comes from crossing over (prophase I, at chiasmata) and independent assortment (metaphase "
        "I). Humans: 2n = 46, n = 23. Nondisjunction (failure to separate) causes aneuploid gametes.",
        "In which phase of meiosis does crossing over happen? (Prophase I.)",
    ),
    lesson(
        "Non-Mendelian Inheritance",
        "Patterns that don't fit simple dominant/recessive ratios.",
        "INCOMPLETE DOMINANCE -- a blended heterozygote (red x white -> pink). CODOMINANCE -- both "
        "alleles show fully (AB blood). MULTIPLE ALLELES -- more than two versions (ABO). LINKAGE -- "
        "genes close together on a chromosome are inherited together.",
        "Mendel's ratios assume one gene, two alleles, complete dominance, and independent genes. Real "
        "traits often break those assumptions.",
        "ABO: I^A and I^B are codominant, i is recessive. Polygenic traits (height, skin color) give "
        "continuous variation -- State/Nationals call these additive alleles. Epistasis: one gene "
        "masks another; recessive epistasis gives 9:3:4 (Labrador coat color: ee is yellow regardless "
        "of the B gene). Complementation tests whether two mutations are in the same gene. Linked "
        "genes produce mostly parental types; recombination frequency = recombinants / total x 100% "
        "and 1% = 1 map unit (centimorgan). Sex-linked traits and pleiotropy (one gene, many effects) "
        "also fit here.",
        "A testcross gives 42 + 40 parental and 9 + 9 recombinant offspring. Map distance? (18/100 = "
        "18 map units.)",
    ),
    lesson(
        "Hardy-Weinberg & Population Genetics",
        "Tracking allele frequencies in a population.",
        "ALLELE FREQUENCY -- how common an allele is (p and q). HARDY-WEINBERG EQUILIBRIUM -- "
        "frequencies stay the same across generations if nothing is acting on them.",
        "If a population isn't evolving, you can predict genotype frequencies from allele frequencies "
        "with two equations.",
        "p + q = 1 and p^2 + 2pq + q^2 = 1 (p^2 = homozygous dominant, 2pq = heterozygous, q^2 = "
        "homozygous recessive). Start with what you can see: the recessive phenotype frequency is "
        "q^2. Example: 16% are aa -> q = 0.4, p = 0.6, carriers = 2(0.6)(0.4) = 48%. Equilibrium "
        "conditions: no mutation, random mating, no natural selection, a very large population (no "
        "genetic drift), no gene flow. Breaking any one causes evolution. Drift is strongest in small "
        "populations (bottleneck and founder effects).",
        "1 in 100 people has a recessive condition. What fraction are carriers? (q = 0.1, p = 0.9, "
        "2pq = 0.18, so 18%.)",
    ),
    lesson(
        "PCR, Gel Electrophoresis & Restriction Enzymes",
        "Core lab techniques for copying, cutting, and sorting DNA.",
        "PCR -- polymerase chain reaction, which copies DNA. RESTRICTION ENZYME -- cuts DNA at a "
        "specific sequence. GEL ELECTROPHORESIS -- separates DNA fragments by size.",
        "PCR makes millions of copies of a target sequence. Restriction enzymes cut DNA at set spots. "
        "A gel then sorts the pieces by size so you can compare samples.",
        "PCR cycle: denature (~95 C, strands separate), anneal (~50-65 C, primers bind), extend "
        "(~72 C, Taq polymerase builds). Each cycle doubles the target: n cycles -> 2^n copies. "
        "Restriction enzymes (e.g. EcoRI cuts G^AATTC) often cut palindromes and leave sticky ends. "
        "Electrophoresis: DNA is negative, so it moves toward the positive electrode; small fragments "
        "travel farther. Use a ladder to estimate sizes. Applications: DNA fingerprinting, paternity "
        "tests, and cloning genes into plasmids.",
        "After 10 PCR cycles starting from one molecule, how many copies (ideally)? (2^10 = 1,024.)",
    ),
    lesson(
        "Sanger Sequencing & CRISPR-Cas9",
        "Reading a DNA sequence, and editing it.",
        "SANGER SEQUENCING -- chain-termination sequencing using ddNTPs. ddNTP -- a nucleotide that "
        "stops chain growth. CRISPR-Cas9 -- a guide RNA steers the Cas9 enzyme to cut a chosen DNA "
        "sequence.",
        "Sanger sequencing makes copies of every possible length, each ending in a labeled letter, "
        "then sorts them by size to read the sequence. CRISPR is a programmable cutter for editing "
        "genes.",
        "Sanger: template + primer + DNA polymerase + normal dNTPs + a few fluorescent ddNTPs (no 3' "
        "OH, so chains stop). Fragments are separated by capillary electrophoresis; reading from the "
        "shortest fragment upward gives the new strand 5' to 3' (complementary to the template). "
        "State/Nationals list Sanger. CRISPR comes from a bacterial defense system against viruses. "
        "The guide RNA matches the target next to a PAM sequence (NGG for Cas9); Cas9 makes a "
        "double-strand break. Repair by non-homologous end joining tends to knock a gene out; "
        "homology-directed repair with a template can insert a precise change. Uses: research, crops, "
        "therapies such as an approved treatment for sickle-cell disease.",
        "Sanger fragments read from shortest to longest end in A, C, C, T. What is the template "
        "sequence that was copied (3' to 5')? (3'-TGGA-5'.)",
    ),
]

WATER_QUALITY = [
    lesson(
        "Aquatic Ecology Fundamentals",
        "Food webs, energy flow, and the basic vocabulary of water ecosystems.",
        "PRODUCER -- makes food from light (phytoplankton, seaweed, seagrass). CONSUMER -- eats others. "
        "DECOMPOSER -- breaks down dead matter. TROPHIC LEVEL -- a feeding step.",
        "Energy flows from the sun into producers, then up through consumers; only about 10% passes "
        "from one level to the next, so there are many more producers than top predators.",
        "Plankton drift (phytoplankton and zooplankton); nekton swim (fish, squid); benthos live on "
        "the bottom. Primary productivity is limited by light and nutrients (nitrogen and "
        "phosphorus). Biomagnification: persistent toxins (mercury, PCBs) concentrate up food chains. "
        "Key cycles: carbon, nitrogen, and phosphorus. Keystone species have outsized effects (sea "
        "otters control urchins, which protects kelp). The 2027 focus is marine and estuary "
        "environments, not freshwater.",
        "Why is mercury higher in tuna than in sardines? (Biomagnification -- tuna eat many smaller "
        "fish over time.)",
    ),
    lesson(
        "Marine & Estuary Ecosystems",
        "Ocean zones, estuaries, and the habitats along the coast.",
        "ESTUARY -- where river freshwater mixes with seawater. BRACKISH -- salinity between fresh and "
        "sea water. INTERTIDAL ZONE -- between high and low tide. SALINITY -- dissolved salt, "
        "typically about 35 ppt in the open ocean.",
        "Estuaries are nurseries: shallow, nutrient-rich, and sheltered, so young fish and shellfish "
        "grow there. Organisms must handle changing salinity and tides.",
        "Ocean zones: by light (photic, aphotic) and by depth (pelagic open water; benthic bottom; "
        "neritic over the continental shelf; oceanic beyond). Estuary types by mixing: salt-wedge, "
        "partially mixed, well-mixed. Coastal habitats: salt marshes (cordgrass), mangroves "
        "(tropical, salt-tolerant trees with prop roots), seagrass beds, kelp forests, rocky "
        "intertidal zones (zonation by exposure), sandy beaches, and coral reefs. Euryhaline organisms "
        "tolerate wide salinity ranges; stenohaline organisms do not. Estuaries also filter pollutants "
        "and buffer storms.",
        "An oyster thrives where salinity swings daily from 10 to 25 ppt. Euryhaline or stenohaline? "
        "(Euryhaline.)",
    ),
    lesson(
        "Coral Reef Ecology",
        "How reefs are built, what they need, and what threatens them.",
        "CORAL POLYP -- a small animal (a cnidarian) that builds a calcium carbonate skeleton. "
        "ZOOXANTHELLAE -- symbiotic algae living in coral tissue. BLEACHING -- coral expelling its "
        "algae under stress.",
        "Reef-building corals are animals that farm algae inside their bodies. The algae make food by "
        "photosynthesis; the coral gives them shelter and nutrients. That's why reefs need clear, "
        "warm, shallow, sunlit water.",
        "Ideal conditions: about 23-29 C, clear water, normal salinity, low nutrients. Reef types: "
        "fringing (close to shore), barrier (separated by a lagoon -- the Great Barrier Reef), atoll "
        "(a ring around a sunken volcano). Threats: warming (bleaching), ocean acidification "
        "(less carbonate to build skeletons), nutrient runoff (algae overgrow coral), sediment, "
        "overfishing (removing grazers like parrotfish), disease, and physical damage. Reefs cover "
        "under 1% of the ocean floor but hold roughly a quarter of marine species.",
        "Why does nutrient pollution harm coral reefs even though nutrients help most plants grow? "
        "(It feeds algae that overgrow and smother corals.)",
    ),
    lesson(
        "Coral Reef Organism Identification",
        "Recognizing the reef organisms that are the 2027 ID focus.",
        "PHYLUM -- a major animal group. CNIDARIA -- corals, anemones, jellies (stinging cells). "
        "ECHINODERMATA -- sea stars, urchins, sea cucumbers (five-part symmetry). MOLLUSCA -- snails, "
        "clams, octopus.",
        "Identification stations show photos. Start with the big group (is it a coral, a fish, an "
        "echinoderm?) and narrow down using shape, color pattern, and body features.",
        "Corals: brain coral (grooved dome), staghorn and elkhorn (branching Acropora, important "
        "Caribbean builders), sea fans (soft gorgonians), fire coral (actually a hydrozoan). Fish: "
        "parrotfish (beak-like teeth, graze algae), butterflyfish, clownfish (living in anemones), "
        "groupers, moray eels, lionfish (an invasive in the Atlantic). Others: giant clams, crown-of-"
        "thorns sea star (a coral predator), long-spined sea urchins (algae grazers), sponges, "
        "Christmas tree worms, sea turtles (hawksbill eats sponges). Use the official ID list and "
        "binder photos; learn each organism's role (builder, grazer, predator).",
        "Which reef animal's population outbreaks strip coral cover on Indo-Pacific reefs? "
        "(Crown-of-thorns sea star.)",
    ),
    lesson(
        "Water Quality Parameters",
        "What each measurement means and what healthy marine values look like.",
        "DISSOLVED OXYGEN (DO) -- oxygen gas in water (mg/L). pH -- acidity (seawater about 8.1). "
        "TURBIDITY -- cloudiness. SALINITY -- dissolved salts (ppt or %).",
        "Water quality is a set of numbers that together tell you whether organisms can live in the "
        "water. Learn each one's units, normal range, and what changes it.",
        "Temperature: controls metabolism and oxygen solubility. DO: above about 5 mg/L is healthy; "
        "below 2 is hypoxic. pH: seawater about 8.0-8.3, falling with CO2 uptake. Salinity: open ocean "
        "about 35 ppt (3.5%); estuaries 0.5-30. Nutrients: nitrate and phosphate (excess -> "
        "eutrophication). Turbidity and total suspended solids (measured with a Secchi disk or NTU "
        "meter). Biochemical oxygen demand (BOD): oxygen used by decomposers. Fecal coliform/E. coli "
        "indicates sewage. Know the WQI idea: combining parameters into one quality score.",
        "Seawater salinity of 35 ppt equals what percent? (3.5%.)",
    ),
    lesson(
        "Relationships Among Parameters",
        "How the measurements push each other up and down.",
        "INVERSE RELATIONSHIP -- one rises as the other falls. EUTROPHICATION -- nutrient-driven algal "
        "growth. HYPOXIA -- low oxygen.",
        "Water parameters are linked. Warm water holds less oxygen. More nutrients mean more algae, "
        "and when the algae die, decomposers use up the oxygen.",
        "Temperature up -> DO down (gases are less soluble in warm water), and organisms need more "
        "oxygen. Salinity up -> DO down slightly. Photosynthesis raises DO and pH during the day; "
        "respiration lowers them at night (daily cycles). CO2 dissolving in water forms carbonic acid "
        "-> pH falls (ocean acidification). Eutrophication chain: nutrients -> algal bloom -> algae die "
        "-> bacteria decompose them (high BOD) -> DO crashes -> fish kills and dead zones (e.g. the "
        "Gulf of Mexico). Turbidity cuts light, lowering photosynthesis in seagrass and coral.",
        "Why is DO often lowest just before dawn? (All night, respiration used oxygen with no "
        "photosynthesis to replace it.)",
    ),
    lesson(
        "Human Impacts & Pollution",
        "The main ways people harm marine and estuary waters.",
        "POINT SOURCE -- pollution from one identifiable spot (a pipe). NONPOINT SOURCE -- diffuse "
        "runoff (farms, streets). RUNOFF -- water flowing over land into waterways.",
        "Most coastal pollution is nonpoint: fertilizer, oil, and trash washed off land when it "
        "rains. Point sources are easier to regulate.",
        "Nutrients from fertilizer and sewage -> eutrophication and harmful algal blooms (red tides). "
        "Sediment from construction and deforestation smothers reefs and seagrass. Oil spills coat "
        "organisms. Plastics and microplastics are ingested and entangle wildlife. Thermal pollution "
        "from power plants. Toxic metals and pesticides bioaccumulate. Overfishing and destructive "
        "fishing (bottom trawling, blast fishing). Coastal development destroys mangroves and "
        "marshes. Climate change: warming, acidification, sea-level rise. Laws: the Clean Water Act "
        "(regulates point-source discharges) and marine protected areas.",
        "Lawn fertilizer washing into a bay after rain is point or nonpoint source? (Nonpoint.)",
    ),
    lesson(
        "Water Treatment Processes",
        "How drinking water and wastewater are cleaned.",
        "COAGULATION -- adding chemicals that clump particles. FLOCCULATION -- gentle mixing that grows "
        "the clumps (floc). SEDIMENTATION -- floc settles. DISINFECTION -- killing pathogens.",
        "Drinking water treatment removes particles and then kills germs. Wastewater treatment cleans "
        "used water before it goes back to the environment.",
        "Drinking water: screening -> coagulation (alum) -> flocculation -> sedimentation -> filtration "
        "(sand, gravel, carbon) -> disinfection (chlorine, UV, ozone) -> storage. Wastewater: "
        "preliminary (screens, grit removal), primary (settling removes solids), secondary (bacteria "
        "digest organic matter -- activated sludge or trickling filters -- lowering BOD), tertiary "
        "(removes nitrogen and phosphorus, extra disinfection). Desalination (reverse osmosis or "
        "distillation) turns seawater into fresh water and leaves concentrated brine.",
        "Which wastewater stage uses bacteria to break down organic matter? (Secondary treatment.)",
    ),
    lesson(
        "Salinometer Design & Calibration",
        "Building a device that measures 1-10% salt water accurately.",
        "SALINOMETER -- a device that measures salinity. CALIBRATION CURVE -- a graph of known "
        "salinities vs your device's readings. CONDUCTIVITY -- how well a solution carries electric "
        "current (rises with salt).",
        "You build the salinometer ahead of time and calibrate it with salt solutions you make "
        "yourself. At the event you read an unknown and use your curve to estimate its salinity to "
        "0.1%.",
        "2027 rules: measure 1-10% (mass/volume) salt water in a 400-600 mL beaker filled with at "
        "least 400 mL; estimate to the nearest 0.1%; full credit within +/-1% at Regionals and "
        "+/-0.5% at State/Nationals. A simple electronic salinometer is allowed -- nothing programmable "
        "or Wi-Fi-capable, no laptops or tablets. Approaches: a hydrometer (floats higher in denser "
        "salt water), or a conductivity probe with a multimeter. Make standards precisely: 5% m/v = "
        "5.0 g salt dissolved to 100 mL total solution. Calibrate at several points (1, 2, 4, 6, 8, "
        "10%), repeat readings, and control temperature (conductivity rises with temperature). Graph "
        "and interpolate.",
        "How do you make 500 mL of a 4% (m/v) salt solution? (Dissolve 20 g of salt and add water to "
        "a total of 500 mL.)",
    ),
    lesson(
        "Traditional Ecological Knowledge & Life Histories",
        "Indigenous knowledge of marine systems and how organisms' life cycles shape their survival.",
        "TRADITIONAL ECOLOGICAL KNOWLEDGE (TEK) -- knowledge built by Indigenous and local peoples "
        "through long observation. LIFE HISTORY -- an organism's pattern of growth, reproduction, and "
        "survival. r- and K-SELECTION -- many cheap offspring vs few well-cared-for offspring.",
        "People who have fished and gathered along a coast for generations know its seasons, "
        "spawning times, and changes -- knowledge that now helps science and management.",
        "TEK examples: Hawaiian ahupua'a land-to-sea management and seasonal fishing closures (kapu); "
        "Pacific Northwest clam gardens (rock-walled terraces that boost clam growth); community "
        "monitoring of reef fish. TEK is long-term, place-based, and often combined with scientific "
        "data in co-management. Life histories: r-selected species (many small eggs, little care, "
        "high mortality -- most reef fish, broadcast-spawning corals) vs K-selected (few young, more "
        "care, long-lived -- sea turtles, sharks, marine mammals). K-selected species recover slowly "
        "from overfishing. Many reef organisms have planktonic larvae that disperse widely before "
        "settling.",
        "Which recovers faster from overfishing: a shark or a sardine? Why? (The sardine -- it "
        "matures fast and makes huge numbers of eggs.)",
    ),
    lesson(
        "Water Quality Data Interpretation",
        "Reading graphs and tables of water measurements.",
        "TREND -- a consistent change over time. CORRELATION -- two variables changing together. "
        "OUTLIER -- a value far from the rest.",
        "Many questions give you data. Read the axes and units first, describe the pattern, then "
        "explain it using what you know about how parameters affect each other.",
        "Daily DO/pH cycles: high in the afternoon, low before dawn (photosynthesis vs respiration). "
        "Seasonal temperature and DO: inverse. Salinity along an estuary rises toward the sea; a "
        "storm or heavy rain drops it. A spike in nitrate followed days later by a chlorophyll peak, "
        "then a DO drop, is the eutrophication sequence. Compare sites upstream and downstream of a "
        "discharge. Watch for units (mg/L vs ppm are equal for dilute water; ppt vs %), and don't "
        "claim causation from correlation alone.",
        "Salinity at a monitoring station drops from 28 to 12 ppt over two days. Likely cause? "
        "(Heavy rain or river flooding adding fresh water.)",
    ),
    lesson(
        "Ecological Impact Scenarios",
        "Predicting what happens to an ecosystem when something changes.",
        "CASCADE -- a chain of effects through a food web. RESILIENCE -- ability to recover. PHASE "
        "SHIFT -- an ecosystem flipping to a different state (coral reef to algae reef).",
        "Scenario questions ask \"what happens if...?\" Trace the effect step by step through the "
        "food web and the water chemistry.",
        "Overfishing parrotfish -> algae overgrow coral -> fewer young corals settle -> reef declines. "
        "A marine heat wave -> bleaching -> coral death if prolonged. Losing sea otters -> urchins "
        "boom -> kelp forests become urchin barrens. Draining a salt marsh -> less nursery habitat -> "
        "fewer young fish offshore; more flooding inland. Nutrient runoff -> algal blooms -> hypoxia. "
        "An invasive lionfish eats young reef fish. Answer with a clear chain: cause -> direct effect "
        "-> indirect effects -> long-term outcome, and note what monitoring data would confirm it.",
        "A reef loses most of its long-spined sea urchins to disease. Predict the next change. "
        "(Algae increase because a major grazer is gone, crowding out coral.)",
    ),
]
