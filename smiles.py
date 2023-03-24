import pandas as pd
import chemspipy
from chembl_webresource_client.new_client import new_client

lost_name = (['Ho2O3', 'Polyethylene', 'polystyrene', 'nan', 'Ge10Sb30S50Te10',
       'ChCL', 'Y2O3', 'SiC', 'PbF2-TeO2-B2O3-Eu2O3', 'BiZnBo–', 'CaBr2',
       'CaMn4Si5O15', 'SC-CO2', 'dimethylpolysiloxane', 'DMC', 'BBGE4',
       'trimethyl pentane', 'NICOMP', 'NaCl0.1KCl0.7KBr0.2', 'Al2O3',
       'DCF', 'SiOF', 'CoO', 'BaSiO3', 'P2VP', 'As-S', 'VBzOH', 'Si–O',
       'silicon oxide', 'alcohols', 'Au-PVP', 'HfO2', 'SiOx',
       'Polystyrene', 'Cu3Nb2O8', 'CuGaSe2', 'GaAs',
       'Na2O–B2O3–Bi2O3–Nd2O3', 'BBFC', 'PbO–', 'CN 104A80Z', 'AlN',
       'ITO', 'NO2−', 'Ga0.6Al0.4As', 'NaI', 'MgZO', 'Ge25As10Se65',
       'ZnS0.21Se0.79', 'aceticacid', 'Si–H(N3)', 'SrWO4', 'PMMA', 'C2H',
       'BBGA5', 'PTMC', 'PbF2–TeO2–B2O3–Eu2O3', 'Gd1.6Eu0.4O3', 'PPKTP',
       'As38S56Bi6', 'Polydimethylsiloxane', 'Ge20Sb20S50Te10', 'PSU',
       'As0.35Se0.58Te0.07', 'NdPb4', 'La–Yb', 'Li2O-SiO2', 'AMT',
       'ZnS-MPA', 'BaGdG', 'PVA', 'ZrO2–SnO2', 'Zinc selenide', 'SiDs',
       'NaGdF4', 'B80Bi20Sm0.5', 'SO4', 'Dipentylether', 'CuAlSe2',
       'DABA', 'LiNbO3', 'ZnSnP2', 'FeO', 'CsI', 'CdSnAs2', 'PPD',
       'BaGdGC', 'CuAlS2', 'Ge–Ga–S', 'La7.59Si10O22.95N5.62', 'AgInTe2',
       'WO3', 'ethanol–', 'ZrTiOx', 'As38.8Se61.2', 'tungstenoxide',
       'Y3Al5O12', 'APC', 'GeS2–As2S3', 'CdTe', 'DMA',
       'B2O3-(30-x)Bi2O3-xNiO', 'BPYb10', 'Siliconchloride', 'SiON',
       'NiTPP', 'CdGeAs2', 'C–Cl', 'ZnPc2', 'ZnAlBiBTb2.0', 'C9F20',
       'GaSb', 'Sc2O3', 'As45S55', 'Polyacrylate', 'PESu', 'C6H13',
       'ZnTe', 'MgF2', 'In2O3–Sc2O3', 'TiO2(25', 'CH3NH3Pb3-xClx',
       'Zn-IRMOF-14', 'K2CsSb', 'In2O3', 'Na2O·4TeO2', 'H-I-CGO',
       'SbNa2K', 'IPA', 'flavonoid', 'CuSO4·5H2O', 'PbO−Bi2O3−SiO2',
       'polypropylene', 'Zn0.43Cd0.57S0.10Se0.90', 'HfOCl2·nH2O',
       'H2Odipoles', 'Al2O3-C', 'Dy2O3', 'C8F18', 'ZrO2–MgO', 'Al6Ge2O13',
       'As2S3', 'chitin', 'La2S3', 'BTO', 'Cu2O', 'Ta7YO19',
       'PBMA425-b-PS490', 'NO3−', 'Kaolinite', 'MoO3–TeO2',
       'CBr4–C2Cl6calculated', 'SiOxNy', 'SiNa0.1Er', 'Fe2O3',
       'BSiCaLa25', 'La–Pr', 'IZO', 'BAP-CTM-2', 'NaSb3Br10',
       'polysulphone', 'MoS2 –', 'GeS2', 'BSiCaLa10', 'BaF2', 'Stilbite',
       '(−)-Sparteine', 'TiO2nanoparticles', 'Eu2O3', 'Se88Te4Ag8', 'PbO',
       'BSYCaEu1.5', 'Neosporin', 'Y3Sc2Ga3O12', 'CdBPr', 'Na2O', 'PtS2',
       'PbO–TeO2', 'sapphire', 'NdPb2', 'GaSe', 'Butanoylbromide',
       'LiMgLaAP', 'SrO2', 'Bi2O3.xSiO20.5Sm2O3', 'Butylethylether',
       'B-NIP-24h', 'HgSe', 'BaTiO3', 'Bi2O330SiO2xMF', 'ZnAlBiBTb1.0',
       'HfSiOx', 'CuAlGeSe4', 'CuInO2', 'ZnAlBiBTb3.0', 'ThF4', 'Si3N4',
       'YF3', 'Ca4GdB3O10', 'B36N36', 'Na2O·B2O3', 'PACG', 'TbFeCo',
       'SiN0.35', 'Nb40Er0.25', 'LiBGeO4', 'MgO', 'OCH2CH2 –', 'AlSb',
       'As39S58I3', 'ZnAlBiBEr10', 'AMO', 'SiO2·HC', 'CsCaF3', 'MgSe',
       'GaSbS', 'CdS', 'CdSi1-xGexAs2', 'olivine', 'germaniumsulphide',
       'MgWO4', 'Gd3SbO7', 'CuInTe2', 'Bu4NPh4B', 'Si0.032Ge0.899O0.069',
       'Al0.16Ga0.84As', 'BBFCEr0.5', 'InP', 'GaP0.5Sb0.5', 'Zn2N3',
       'BBT2', 'KDP', 'PB-COOH-328-B −', 'ZrO', 'SiO2(H)', 'LiBr-H2O',
       'UNIL088', 'CaF\\(_2\\)(Eu) 300 K', 'BaSe', 'C–H',
       'Y1−xErxAl3(BO3)4glassythin', 'As2S3 chalcogenide', 'Ge20As20Se60',
       'Au-Ta2O5', 'BBGA1', 'SN2002', 'Ca2MgSi2O7', 'SnOx', 'BSYCaEu1.0',
       'Rb3SbO3', 'Nafion', 'Polyvinyl Alcohol', 'Y2Te4O11', 'CuInSnSe4',
       'Cd0.50Se0.50', 'Ge31S63TI6', 'As30Se63Sb4Sn3', 'Rb2BiI5O15',
       'N-SF5', 'BaO', 'Si3N4-ARC', 'INP', 'B40BiCfSm1.0', 'PNIPAM',
       'KLa(MoO4)2', 'RhB', 'PAC', 'vanadium oxide', 'N–H', 'CsGeF3',
       '(±)-linalool', 'AgI–B2O3:V2O5', 'BaPF4', 'Polyacrylonitrile',
       'AlOxNy_4', 'CHOL', 'NO3', 'SiO2–Nb2O5', 'BBF2.5Er1.0',
       'Ge14As20Se66', 'fluoro–arsenate', 'Sb2O3–B2O3', 'PDAOPV',
       'As40S40Se20', 'CsCdBr3', 'ZrW2O8', 'AgGaS2', 'PVC',
       'Na4AlZnP3O12', 'Ge20Ga5Sb10S65', 'Polyurethane',
       'Aceticanhydride', 'PHA', 'BPTUA3-MMTDA', 'c10', 'CdO',
       'Pb0.8Sn0.2Te', 'PtBMA', 'BBGE0', 'CS2', 'GaSb0.96N0.04',
       'C60(OH)22–', 'SrO', 'silicate', 'DEA', 'AlF', 'K2O',
       'Butyricacid', 'SiO2–TiO2', 'ErO1.5', 'CuAlSnSe4', 'Gd3Sc2Al3O12',
       'SU-8', 'Bi12GeO20', 'Ta2O5', 'BBT1', 'PEG 400', 'Malicacid',
       'Te2Se3As4.5I0.5', 'MEA',
       'Quinolinium 2-carboxy-6-nitrophthalate monohydrate',
       'Methylacetate', 'CYTOP', 'Nd2O3', 'Lissamine', 'Ca3MgSi2O8',
       'Li2B6O9F2', 'ZrO2-SiO2', 'NPDR', 'PMSSQ-20', 'BPIE', 'CuCl2·2H20',
       'VO2', 'As40S60', 'Zn0.75Cd0.25S0.75Se0.25', 'TeO2–P2O5', 'GaPO4',
       'CuAlTe2', 'Al–Cu–O', 'Ge2Sm2O7', 'MCH', 'Tertiarybutylacetate',
       'LiTaO3', 'Ge25As12Se63', 'AlAs', 'PbO–Bi2O3', 'PVA–Ag',
       'Polycarbonate', 'TeO2–B2O3–ZnO', 'lanthanumfluoride', 'Ta3N5',
       'tinoxide', 'YbPb10', 'NMFA', 'SiAlON', 'NaCl0.4KCl0.1KBr0.5',
       'B25Ti30', 'ITO-80W', 'N-Tetradecyl-triethylammonium', 'Fe2SiO4',
       'AgAlGeSe4', 'WO3-xNd2O3', 'Cd0.60Se0.40', 'K2O–TiO2',
       'Ge25As15Se60', 'Mn2SiO4', 'N2 PDA', '(±)-Linalool', 'BaO·2SiO2',
       'Ga15Se85', 'Zn3N2', 'CdSiP2', 'VBCFs', 'PCHMTC', 'Mn1-xCuxFe2O4',
       'Cu2Zn0.05Sn0.95Se3', 'BBW3', 'B12N12', 'N3-RhB', 'BiVO4',
       'Ge33As12Se55', 'TeO2–', 'CaF2–Y2O3–ZnO', 'Aceticacid', 'NaI(Tl)',
       'LaSFN9', 'Sn–S0', 'CdGe', 'BBFBNd0.5', 'ZnO–Al2O3', 'ZnSb', 'TCB',
       'Nb2O3', 'YbF3', 'SRO', 'La12Ga28S60', 'leucite', 'Ca2SiO4',
       'CsGeCl3', 'NITRIDEC', 'PULFAS-20', 'polydimethylsiloxane', 'MBTA',
       'AgGaSe2', 'CdGeP2', 'ZnSiP2', 'LaOF', 'AgBr1−xClx', 'HDP',
       'BBS60', 'C4H4', 'PbF2-TeO2-B2O3-Sm2O3', 'BPRFQ', 'As30S70',
       'NiV2O6', 'Si3H', 'Ge3N4', 'AlxGayIn1−x−yAs',
       'NaCl0.1KCl0.1KBr0.8', 'Gd1.7Eu0.1Li0.20O3', 'Rb2SO4', 'ZrAlO',
       'Ni0.98Sr0.02O', 'ErYbAg', 'SiO2n', 'IFO-100', 'SnTe',
       'CF2–CF2]n[CF2', 'SrTiO3', 'CaC2', 'PrMn0.4', 'n-Hexylacetate',
       'PEDOT', 'As2Se3', 'CsGeBr3', 'YK48', 'Sm2O3', 'BaO–B2O3',
       'Cu3Ga5Se9', 'TeO2–Bi2O3', 'LiFe0.995Ni0.005PO4', 'BSiCaLa15',
       'Polypropylene', 'DAP', '1-Benzyl-3-methylimidazoliumchloride',
       'LiNb03', 'ACF', 'Li2O–MgO', 'Ca11.77Si10O16.30N10.31', 'CoFe2O4',
       'CuAlO2', 'ZnAlBiBTb0.1', 'BC408', 'Na2O–P2O5', 'CuInGeSe4',
       'BBCES', 'P2O5–SiO2', 'Ge14As32Se54', 'Olivine', 'Alcohols',
       'polycarbonate', 'Dimethyl butane', 'ZnO–TeO2', 'BBONd',
       'NaHCO3_aq_11', 'SrAl2B2O7', 'ZnPc1', 'NaPh4B', 'CuSO4·H2O',
       'C48H73N13O17S3', 'SiO2–ZrO2', 'Y2TeO6', 'YBO3', 'Sr2Ta2O7',
       'ZnMoO4', 'CsPbI3', 'THz', 'LaY', 'BiB3O6', 'Cu2Se', 'Tb(C)',
       'Se75S25', 'KI', 'golden yellow', 'SnS', 'TAC', 'CuInS2',
       'Na2SiO3', 'ZnO–P2O5', 'Li2O–CaF2–P2O5', 'RuGa2',
       'N-Methyl-2-hydroxyethylammonium isobutyrate',
       'Zn0.31Cd0.69S0.30Se0.70', 'HDPE', '1-Chloro-n-propane', 'C4H8O2',
       'As-Se', 'MoBi2S5', 'TRAP', 'LiFePO4', 'O–O', 'BSA-5-ASA', 'NaC',
       'ZnGeAs2', 'BST85', 'Cu(CH3COO)2·2Cu(OH)2', 'poly(ethylenimine)',
       'ZnBh2', 'COCH2CH2CH2 –', 'Sb2CO3', 'HeLa', 'Bi12TiO20',
       'BPbF-Sm-2', 'ZrOMc', 'Y2Sb2O7', 'Sn-Zno', 'Pb(II)', 'HPS',
       'InGaAsP', 'BPB', 'Ba0.8Sr0.2TiO3', 'InGaAs', 'C12H26', 'TeOx',
       'BBFBEu3', 'SiO2–Al2O3', 'C60[C(COOH)2]3', 'oxyfluoride',
       'In0.093Ga0.906N0.031As0.968', 'phosphate-borate', 'PFE-8',
       'PbO–TiO2', 'CdBNd', 'CaSe', 'BSb', 'PBLG', 'Tin oxide',
       'As20Se80', 'BBG-5', 'Sn4Sb6S13', 'SiCN', 'SiO2 F', 'MPa',
       'GeO2–SiO2', 'CuBr', 'TOC', 'ZnSb(wt', 'Pb0.94Sn0.12Te',
       'K2O–SiO2', 'BK10', 'CRSO', 'BS(B)', 'Ge12.5Sb25Se62.5',
       'Ge27As13S50Te10', 'SN2003', 'Propylammonium acetate', 'PMO2-III',
       'N-BK-7', 'Ge10As30S50Te10', 'polyurethane', 'LiF–Sb2O3',
       'C7H5CH3', 'K2O–B2O3–Bi2O3', 'PANI', 'PVK', 'InGaP',
       'polyethylene', 'BAP-T', 'TiO2nanoparticle', 'BAP-C',
       'Dimethylheptanol', 'RbTi0.977Yb0.004Nb0.013W0.006OPO4', 'CuGaS2',
       'Tm2O3', 'RbNO3', 'Magnesiumfluoride', 'K2Si2O5', 'DCM', 'BBFBNd2',
       'C8H17', 'Er BCR-2G LA-ICP-MS', 'Cs BCR-2G LA-ICP-MS',
       'silicone oil', 'Ho3Sb5O12', 'In2O3–ZrO2', 'VB08',
       'Propylethanoate', 'Ga28La12S60', 'Me', 'S-TIM28',
       'Si–(OSi)n–(OH)4–n', 'C9H10', 'LuVO4', 'NbOx-05',
       'Cu2Zn1−xCdxSnS4', 'BPYb15', 'AgGaTe2', 'As39S58TI3', 'BPEAU-4',
       'NH4NO3', 'BaO–M2O3–P2O5', 'AgEr-KZS-30', 'BiGaDyIG', 'ZnSe(Te)',
       'Ga0.2Al0.8As', 'Aurum', 'Zn(D4BrPC)2', 'K2O·2B2O3', 'Na2Dy2O4',
       'LiNb1−yTayO3', 'PTFE', 'As-Te', 'Red lead', 'Ethylethanoate',
       'TPP', 'lanthanum strontium', 'Zr BHVO-2G LA-ICP-MS', 'BID',
       'Al0.5In0.5FeO3', 'Arachidicacid', 'BBFBNd1', 'Li2CO3–K2CO3–H3BO3',
       'PbO–PbF2–B2O3', 'Ta-C:H', 'Ge31S59I10', 'GeTe', 'Ge20Se75Zn5',
       'H(TiO2)', 'PHSQ–VE1D', 'tungsten oxide', 'HfOxNy', 'CsGeI3',
       'PbTiO3', 'LiZnLaAP', 'K-BK7', '1-Chloro-n-decane', 'BaGd2ZnO5',
       'Ge0.2Te0.8', 'Na2O·SiO2', 'CmO1', 'La21.72Si10O10.11N28.32',
       'NAP-4', 'Ni0.96Sr0.04O', 'Dy2Ti2O7', 'Co-PAES',
       'Se84−xTe15Bi1.0Pbx', 'OCOCH2CH2 –', 'Dy2TeO6', 'MgO–TeO2',
       'Zn(D4MPC)2', 'SA-40N', 'BiOBr', 'CdSnP2', 'GaS0.5Se0.5',
       'SiO2·P2O5', 'Na4Zr2Si3O12', 'PIB', 'Na2O–TeO2', 'PHI-BCTi50',
       'Cd(CH3COO)2', 'CdSeP2', 'C2CN', 'Polyethylene glycol', 'MMA',
       'SiC1−xNx', 'B-C5-B', 'LiAc', 'zinc selenide', 'methylbutanoate',
       'stearin', 'MgAl2O4', 'B3P1', 'Gd1.75Eu0.1Li0.15O3',
       'molybdenumoxide', 'Li2O–SiO2', 'Maltopentaose', 'SiO2annealed',
       'pyridine-dicarboxamide', 'ethers', 'HxAc', 'Zn1−xBexO', 'LiYBSm',
       'Er3TaO7', 'K2Ce(NO3)5·2H2O', 'Ca9.94Si10O17.73N8.14', 'BBW0',
       'pfa', 'Cs2Hg3I8', 'POSS', 'ZnSiAs2', 'Sr2Si3O9', 'PNIPAAm',
       'BiBTEr2.5', 'Ge14As8Se78', 'MgO–PbF2–SiO2', 'Silicate', 'SixOyNz',
       'MEL', 'LiY5P2O13', 'YOME', 'PbSi', 'LiSi4AlO10', 'GdVO4',
       'Li2OPbO', 'CaWO4', 'Ga15Se83In2', 'GdmCl', 'Ge28Sb12Se60',
       'Hf BCR-2G LA-ICP-MS', 'BiBTEr0.5', 'Li2O–M2O3–ZrO2–SiO2',
       'PbO–Al2O3', 'BS(1,1)', 'P4448Cl', 'PPFPMA', 'PB1320', 'PcZn',
       'Ca2AlSOAlO7(G)', 'Gd2(MoO4)3', 'C5F12', 'TiO2-SiO2',
       'C18H35(OCH2CH2)nOH', 'N2Ac', 'CH2OC14H29', 'MgPo–C60', 'CoCl2',
       'Ag-PVP', 'Sn2N2(NH)', 'BaO–B2O3–Al2O3–P2O5', 'BiBaS3', 'Ca3Si3O9',
       'CsCl-PEG4000-H2O', 'CdO–Al2O3', 'Li2O–Al2O3', 'Lu3Al5O12', 'HbO2',
       'BBFBNd0.05', 'PVAc', 'AlGaAs', 'Gd1.7Eu0.3O3', 'Fe-Ti',
       'ZnF2–WO3–TeO2', 'C1SO4', 'CH3(CH2)2COOH',
       'Trimethylammonium hydrogen sulfate',
       'LiFe0.995Y0.0025Ag0.0025PO4', 'Ni0.5As1.5S3', 'CeCs2O3', 'C4F10',
       'Ge0.15Te0.78Cu0.07', 'Ag2Te', 'N-SF8', 'PHI-BC', 'Ga1.6As38.4S60',
       'Cu9Ge11Te80', 'Hexylacetoacetate', 'Na2CO3_aq_18', 'BBW1', 'TeLi',
       'CsSnBr3', 'Ni0.05Zn0.95O', 'SiO2-xFx', 'Methylethanoate',
       'PVC-COOH', 'La7.84Si10O26.17N3.73', 'ZnSe(CVD)', 'BaWO4',
       'Te20As40Se30I10', 'Sr(PO3)2', 'PHBV', 'NaCl0.3KCl0.1KBr0.6',
       'GeSi', 'NH-SOX', 'C6F13', 'VmKn', 'S.Y.', 'Chitin', 'Sn–Sb',
       'Al(III)TPP', 'AgAlS2', 'NiOx', 'ZnSiO3', 'AgCl-AgBr',
       'H(CH2)n(OCH2CH2)15O(CH2)nH', 'Silicone oil', 'CaAS20',
       'Bi2O3–B2O3', 'NMP-M', 'BaPF2', 'Sn2S3', 'CuSO4·3H2O', 'Ph-PPV',
       'PbWO4', 'NzPc', 'NaSb3F10', 'Sapphire', 'LiLaBSm', 'SiN20',
       'Ti0.5Si0.5Ox', 'Li2O–Nb2O5', 'Dimethylbutane', 'PZFX–',
       'NaCl0.2KCl0.4KBr0.4', 'C6H14', 'Cu(II)Pc', 'CdBh2', 'SiO2–Na2O',
       'ZrCe', 'HfMoN(L)', 'SiOC', 'Ge25Se75', 'YCa4O(BO3)3', 'B-NIP-12h',
       'SiO2–PEO', 'Ge27.5As12Se60.5', 'NO2–BF', 'Co3O4', 'CH3CO2C4H9',
       'SrSi2Al2O8', 'BBD40', 'La12.33Si10O9.42N19.38', 'Lu2O3', 'ZnS(4',
       'BiFeO3', 'CuGaGeSe4', 'BiO2-PCF', 'GNR', 'BORB', 'BSGdCaTb0.5',
       'O\ue5f8H', 'Rb2SnO3', 'P4VP', 'Ge20Sb15Se65', 'BK-7',
       'PbO–Sb2O3–B2O3', 'Ga10Se81Pb9chalcogenide', 'Cd–S', 'SN2005',
       'C4H8O', 'Pyrite', 'Se75S21Cd4', 'Cr2O3·2H2O', 'D-Limonène',
       'Se89Zn2Te5In4', 'HoPb8', 'Y2Ti2O7', 'Zn2S28Se70', 'PMSSQ',
       'Se75S19Cd6', 'ErVO4', 'Oxyfluoride', 'AlGaN', 'C4H2', 'BBGA4',
       'NaY0.975Yb0.02Er0.005(WO4)2', 'Lu(PcR8)2', 'Ca(Mo0.6W0.4)O4',
       'Si2H6', 'Na2Si2O5', 'YAS0823', 'poly(tetrafluoroethylene)',
       'C6H5', 'Bi4Ce3O12', 'As32S68', 'ZnSnxOy', 'Pb40B30', 'NaFl',
       'YVO4', 'LiLuF', 'Et', 'PAIs', 'SF-10', 'CPT', 'RbCaF3', 'BaClF',
       'C7H6Cl2', 'TiO2-PI', 'OCBTDy20', 'K2O', 'Sm2O3', 'P2O5',
       'Zn1−xMgxTe', 'Tetra-thiol', 'N-SF2', 'PbBh2', 'Al3(PO4)2(F',
       'N-methyl-2-hydroxyethylammonium butyrate', 'K2C2O4', 'Se75S23Cd2',
       'HgGa2S4', 'CuCl2·2H2O'])

def ChemSpiderSMILES(name):
    cs = chemspipy.ChemSpider('wyRGl2XVbXboA9tzibfVxL7gcyfIKpo2')
    smi = cs.search(name)
    try:
        smiles = smi[0].smiles
        return smiles
    except:
        return None


def ChemblSMILES(name):
    try:
        mol = new_client.molecule
        compound = mol.search(name)[0]
        smiles = compound['molecule_structures']['canonical_smiles']
        return smiles
    except:
        return None

lost_name['ChemSpider_SMILES'] = lost_name['Name'].apply(ChemSpiderSMILES)

# добавление столбца со значениями SMILES из ChEMBL
lost_name['ChEMBL_SMILES'] = lost_name['Name'].apply(ChemblSMILES)

# запись данных в файл
lost_name.to_csv('lost_name_smiles.csv', index=False)