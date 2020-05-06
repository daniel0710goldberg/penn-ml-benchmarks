# -*- coding: utf-8 -*-

"""
PMLB was primarily developed at the University of Pennsylvania by:
    - Randal S. Olson (rso@randalolson.com)
    - William La Cava (lacava@upenn.edu)
    - Weixuan Fu (weixuanf@upenn.edu)
    - and many more generous open source contributors

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

classification_dataset_names = [
    'GAMETES_Epistasis_2-Way_1000atts_0.4H_EDM-1_EDM-1_1',
    'GAMETES_Epistasis_2-Way_20atts_0.1H_EDM-1_1',
    'GAMETES_Epistasis_2-Way_20atts_0.4H_EDM-1_1',
    'GAMETES_Epistasis_3-Way_20atts_0.2H_EDM-1_1',
    'GAMETES_Heterogeneity_20atts_1600_Het_0.4_0.2_50_EDM-2_001',
    'GAMETES_Heterogeneity_20atts_1600_Het_0.4_0.2_75_EDM-2_001',
    'Hill_Valley_with_noise',
    'Hill_Valley_without_noise',
    'adult',
    'agaricus-lepiota',
    'allbp',
    'allhyper',
    'allhypo',
    'allrep',
    'analcatdata_aids',
    'analcatdata_asbestos',
    'analcatdata_authorship',
    'analcatdata_bankruptcy',
    'analcatdata_boxing1',
    'analcatdata_boxing2',
    'analcatdata_creditscore',
    'analcatdata_cyyoung8092',
    'analcatdata_cyyoung9302',
    'analcatdata_dmft',
    'analcatdata_fraud',
    'analcatdata_germangss',
    'analcatdata_happiness',
    'analcatdata_japansolvent',
    'analcatdata_lawsuit',
    'ann-thyroid',
    'appendicitis',
    'australian',
    'auto',
    'backache',
    'balance-scale',
    'banana',
    'biomed',
    'breast',
    'breast-cancer',
    'breast-cancer-wisconsin',
    'breast-w',
    'buggyCrx',
    'bupa',
    'calendarDOW',
    'car',
    'car-evaluation',
    'cars',
    'cars1',
    'chess',
    'churn',
    'clean1',
    'clean2',
    'cleve',
    'cleveland',
    'cleveland-nominal',
    'cloud',
    'cmc',
    'coil2000',
    'colic',
    'collins',
    'confidence',
    'connect-4',
    'contraceptive',
    'corral',
    'credit-a',
    'credit-g',
    'crx',
    'dermatology',
    'diabetes',
    'dis',
    'dna',
    'ecoli',
    'fars',
    'flags',
    'flare',
    'german',
    'glass',
    'glass2',
    'haberman',
    'hayes-roth',
    'heart-c',
    'heart-h',
    'heart-statlog',
    'hepatitis',
    'horse-colic',
    'house-votes-84',
    'hungarian',
    'hypothyroid',
    'ionosphere',
    'iris',
    'irish',
    'kddcup',
    'kr-vs-kp',
    'krkopt',
    'labor',
    'led24',
    'led7',
    'letter',
    'liver-disorder',
    'lupus',
    'lymphography',
    'magic',
    'mfeat-factors',
    'mfeat-fourier',
    'mfeat-karhunen',
    'mfeat-morphological',
    'mfeat-pixel',
    'mfeat-zernike',
    'mnist',
    'mofn-3-7-10',
    'molecular-biology_promoters',
    'monk1',
    'monk2',
    'monk3',
    'movement_libras',
    'mushroom',
    'mux6',
    'new-thyroid',
    'nursery',
    'optdigits',
    'page-blocks',
    'parity5',
    'parity5+5',
    'pendigits',
    'phoneme',
    'pima',
    'poker',
    'postoperative-patient-data',
    'prnn_crabs',
    'prnn_fglass',
    'prnn_synth',
    'profb',
    'promoters',
    'ring',
    'saheart',
    'satimage',
    'schizo',
    'segmentation',
    'shuttle',
    'sleep',
    'solar-flare_1',
    'solar-flare_2',
    'sonar',
    'soybean',
    'spambase',
    'spect',
    'spectf',
    'splice',
    'tae',
    'texture',
    'threeOf9',
    'tic-tac-toe',
    'titanic',
    'tokyo1',
    'twonorm',
    'vehicle',
    'vote',
    'vowel',
    'waveform-21',
    'waveform-40',
    'wdbc',
    'wine-quality-red',
    'wine-quality-white',
    'wine-recognition',
    'xd6',
    'yeast'
]

regression_dataset_names = [
    '1027_ESL',
    '1028_SWD',
    '1029_LEV',
    '1030_ERA',
    '1089_USCrime',
    '1096_FacultySalaries',
    '1191_BNG_pbc',
    '1193_BNG_lowbwt',
    '1196_BNG_pharynx',
    '1199_BNG_echoMonths',
    '1201_BNG_breastTumor',
    '1203_BNG_pwLinear',
    '1595_poker',
    '192_vineyard',
    '195_auto_price',
    '197_cpu_act',
    '201_pol',
    '207_autoPrice',
    '210_cloud',
    '215_2dplanes',
    '218_house_8L',
    '225_puma8NH',
    '227_cpu_small',
    '228_elusage',
    '229_pwLinear',
    '230_machine_cpu',
    '294_satellite_image',
    '344_mv',
    '4544_GeographicalOriginalofMusic',
    '485_analcatdata_vehicle',
    '503_wind',
    '505_tecator',
    '519_vinnie',
    '522_pm10',
    '523_analcatdata_neavote',
    '527_analcatdata_election2000',
    '529_pollen',
    '537_houses',
    '542_pollution',
    '547_no2',
    '556_analcatdata_apnea2',
    '557_analcatdata_apnea1',
    '560_bodyfat',
    '561_cpu',
    '562_cpu_small',
    '564_fried',
    '573_cpu_act',
    '574_house_16H',
    '579_fri_c0_250_5',
    '581_fri_c3_500_25',
    '582_fri_c1_500_25',
    '583_fri_c1_1000_50',
    '584_fri_c4_500_25',
    '586_fri_c3_1000_25',
    '588_fri_c4_1000_100',
    '589_fri_c2_1000_25',
    '590_fri_c0_1000_50',
    '591_fri_c1_100_10',
    '592_fri_c4_1000_25',
    '593_fri_c1_1000_10',
    '594_fri_c2_100_5',
    '595_fri_c0_1000_10',
    '596_fri_c2_250_5',
    '597_fri_c2_500_5',
    '598_fri_c0_1000_25',
    '599_fri_c2_1000_5',
    '601_fri_c1_250_5',
    '602_fri_c3_250_10',
    '603_fri_c0_250_50',
    '604_fri_c4_500_10',
    '605_fri_c2_250_25',
    '606_fri_c2_1000_10',
    '607_fri_c4_1000_50',
    '608_fri_c3_1000_10',
    '609_fri_c0_1000_5',
    '611_fri_c3_100_5',
    '612_fri_c1_1000_5',
    '613_fri_c3_250_5',
    '615_fri_c4_250_10',
    '616_fri_c4_500_50',
    '617_fri_c3_500_5',
    '618_fri_c3_1000_50',
    '620_fri_c1_1000_25',
    '621_fri_c0_100_10',
    '622_fri_c2_1000_50',
    '623_fri_c4_1000_10',
    '624_fri_c0_100_5',
    '626_fri_c2_500_50',
    '627_fri_c2_500_10',
    '628_fri_c3_1000_5',
    '631_fri_c1_500_5',
    '633_fri_c0_500_25',
    '634_fri_c2_100_10',
    '635_fri_c0_250_10',
    '637_fri_c1_500_50',
    '641_fri_c1_500_10',
    '643_fri_c2_500_25',
    '644_fri_c4_250_25',
    '645_fri_c3_500_50',
    '646_fri_c3_500_10',
    '647_fri_c1_250_10',
    '648_fri_c1_250_50',
    '649_fri_c0_500_5',
    '650_fri_c0_500_50',
    '651_fri_c0_100_25',
    '653_fri_c0_250_25',
    '654_fri_c0_500_10',
    '656_fri_c1_100_5',
    '657_fri_c2_250_10',
    '658_fri_c3_250_25',
    '659_sleuth_ex1714',
    '663_rabe_266',
    '665_sleuth_case2002',
    '666_rmftsa_ladata',
    '678_visualizing_environmental',
    '687_sleuth_ex1605',
    '690_visualizing_galaxy',
    '695_chatfield_4',
    '706_sleuth_case1202',
    '712_chscase_geyser1'
]