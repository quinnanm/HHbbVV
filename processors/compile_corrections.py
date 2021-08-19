#!/usr/bin/env python
import uproot 
import numpy as np
from coffea.lookup_tools import dense_lookup

corrections = {}

# note: it seems that 2016 UL has a preVBF - postVBF version too - find out what that is?
pu = {
    "2016": {"central": "data/PileupHistogram-goldenJSON-13tev-2016-69200ub-99bins.root",
             "up": "data/PileupHistogram-goldenJSON-13tev-2016-72400ub-99bins.root",
             "down": "data/PileupHistogram-goldenJSON-13tev-2016-66000ub-99bins.root",
         },
    "2017": {"central": "data/PileupHistogram-goldenJSON-13tev-2017-69200ub-99bins.root",
             "up": "data/PileupHistogram-goldenJSON-13tev-2017-72400ub-99bins.root",
             "down": "data/PileupHistogram-goldenJSON-13tev-2017-66000ub-99bins.root",
         },
    "2018": {"central": "data/PileupHistogram-goldenJSON-13tev-2018-69200ub-99bins.root",
             "up": "data/PileupHistogram-goldenJSON-13tev-2018-72400ub-99bins.root",
             "down": "data/PileupHistogram-goldenJSON-13tev-2018-66000ub-99bins.root",
         },
}

# from mix.input.nbPileupEvents.probValue: 
mc_pu = {}
# https://github.com/cms-sw/cmssw/blob/master/SimGeneral/MixingModule/python/mix_2016_25ns_UltraLegacy_PoissonOOTPU_cfi.py
mc_pu["2016"] = np.array([1.00402360149e-05, 5.76498797172e-05, 7.37891400294e-05, 0.000110932895295, 0.000158857714773,
                          0.000368637432599, 0.000893114107873, 0.00189700774575, 0.00358880167437, 0.00636052573486,
                          0.0104173961179, 0.0158122597405, 0.0223785660712, 0.0299186888073, 0.0380275944896,
                          0.0454313901624, 0.0511181088317, 0.0547434577348, 0.0567906239028, 0.0577145461461,
                          0.0578176902735, 0.0571251566494, 0.0555456541498, 0.053134383488, 0.0501519041462,
                          0.0466815838899, 0.0429244592524, 0.0389566776898, 0.0348507152776, 0.0307356862528,
                          0.0267712092206, 0.0229720184534, 0.0193388653099, 0.0159602510813, 0.0129310510552,
                          0.0102888654183, 0.00798782770975, 0.00606651703058, 0.00447820948367, 0.00321589786478,
                          0.0022450422045, 0.00151447388514, 0.000981183695515, 0.000609670479759, 0.000362193408119,
                          0.000211572646801, 0.000119152364744, 6.49133515399e-05, 3.57795801581e-05, 1.99043569043e-05,
                          1.13639319832e-05, 6.49624103579e-06, 3.96626216416e-06, 2.37910222874e-06, 1.50997403362e-06,
                          1.09816650247e-06, 7.31298519122e-07, 6.10398791529e-07, 3.74845774388e-07, 2.65177281359e-07,
                          2.01923536742e-07, 1.39347583555e-07, 8.32600052913e-08, 6.04932421298e-08, 6.52536630583e-08,
                          5.90574603808e-08, 2.29162474068e-08, 1.97294602668e-08, 1.7731096903e-08, 3.57547932012e-09,
                          1.35039815662e-09, 8.50071242076e-09, 5.0279187473e-09, 4.93736669066e-10, 8.13919708923e-10,
                          5.62778926097e-09, 5.15140589469e-10, 8.21676746568e-10, 0.0, 1.49166873577e-09,
                          8.43517992503e-09, 0.0, 0.0, 0.0, 0.0,
                          0.0, 0.0, 0.0, 0.0, 0.0,
                          0.0, 0.0, 0.0, 0.0, 0.0,
                          0.0, 0.0, 0.0, 0.0])
# https://github.com/cms-sw/cmssw/blob/master/SimGeneral/MixingModule/python/mix_2017_25ns_UltraLegacy_PoissonOOTPU_cfi.py 
mc_pu["2017"] = np.array([1.1840841518e-05, 3.46661037703e-05, 8.98772521472e-05, 7.47400487733e-05, 0.000123005176624,
                          0.000156501700614, 0.000154660478659, 0.000177496185603, 0.000324149805611, 0.000737524009713,
                          0.00140432980253, 0.00244424508696, 0.00380027898037, 0.00541093042612, 0.00768803501793,
                          0.010828224552, 0.0146608623707, 0.01887739113, 0.0228418813823, 0.0264817796874,
                          0.0294637401336, 0.0317960986171, 0.0336645950831, 0.0352638818387, 0.036869429333,
                          0.0382797316998, 0.039386705577, 0.0398389681346, 0.039646211131, 0.0388392805703,
                          0.0374195678161, 0.0355377892706, 0.0333383902828, 0.0308286549265, 0.0282914440969,
                          0.0257860718304, 0.02341635055, 0.0213126338243, 0.0195035612803, 0.0181079838989,
                          0.0171991315458, 0.0166377598339, 0.0166445341361, 0.0171943735369, 0.0181980997278,
                          0.0191339792146, 0.0198518804356, 0.0199714909193, 0.0194616474094, 0.0178626975229,
                          0.0153296785464, 0.0126789254325, 0.0100766041988, 0.00773867100481, 0.00592386091874,
                          0.00434706240169, 0.00310217013427, 0.00213213401899, 0.0013996000761, 0.000879148859271,
                          0.000540866009427, 0.000326115560156, 0.000193965828516, 0.000114607606623, 6.74262828734e-05,
                          3.97805301078e-05, 2.19948704638e-05, 9.72007976207e-06, 4.26179259146e-06, 2.80015581327e-06,
                          1.14675436465e-06, 2.52452411995e-07, 9.08394910044e-08, 1.14291987912e-08, 0.0,
                          0.0, 0.0, 0.0, 0.0, 0.0,
                          0.0, 0.0, 0.0, 0.0, 0.0,
                          0.0, 0.0, 0.0, 0.0, 0.0,
                          0.0, 0.0, 0.0, 0.0, 0.0,
                          0.0, 0.0, 0.0, 0.0])
# https://github.com/cms-sw/cmssw/blob/master/SimGeneral/MixingModule/python/mix_2018_25ns_UltraLegacy_PoissonOOTPU_cfi.py
mc_pu["2018"] = np.array([8.89374611122e-07, 1.1777062868e-05, 3.99725585118e-05, 0.000129888015252, 0.000265224848687,
                          0.000313088635109, 0.000353781668514, 0.000508787237162, 0.000873670065767, 0.00147166880932,
                          0.00228230649018, 0.00330375581273, 0.00466047608406, 0.00624959203029, 0.00810375867901,
                          0.010306521821, 0.0129512453978, 0.0160303925502, 0.0192913204592, 0.0223108613632,
                          0.0249798930986, 0.0273973789867, 0.0294402350483, 0.031029854302, 0.0324583524255,
                          0.0338264469857, 0.0351267479019, 0.0360320204259, 0.0367489568401, 0.0374133183052,
                          0.0380352633799, 0.0386200967002, 0.039124376968, 0.0394201612616, 0.0394673457109,
                          0.0391705388069, 0.0384758587461, 0.0372984548399, 0.0356497876549, 0.0334655175178,
                          0.030823567063, 0.0278340752408, 0.0246009685048, 0.0212676009273, 0.0180250593982,
                          0.0149129830776, 0.0120582333486, 0.00953400069415, 0.00738546929512, 0.00563442079939,
                          0.00422052915668, 0.00312446316347, 0.00228717533955, 0.00164064894334, 0.00118425084792,
                          0.000847785826565, 0.000603466454784, 0.000419347268964, 0.000291768785963, 0.000199761337863,
                          0.000136624574661, 9.46855200945e-05, 6.80243180179e-05, 4.94806013765e-05, 3.53122628249e-05,
                          2.556765786e-05, 1.75845711623e-05, 1.23828210848e-05, 9.31669724108e-06, 6.0713272037e-06,
                          3.95387384933e-06, 2.02760874107e-06, 1.22535149516e-06, 9.79612472109e-07, 7.61730246474e-07,
                          4.2748847738e-07, 2.41170461205e-07, 1.38701083552e-07, 3.37678010922e-08, 0.0,
                          0.0, 0.0, 0.0, 0.0, 0.0,
                          0.0, 0.0, 0.0, 0.0, 0.0,
                          0.0, 0.0, 0.0, 0.0, 0.0,
                          0.0, 0.0, 0.0, 0.0])

pileup_corr = {}
norm = lambda x: x / x.sum()
for year,pdict in pu.items():
    pileup_corr[year] = {}
    data_pu = {}
    data_pu_edges = {}
    for var,pfile in pdict.items():
        with uproot.open(pfile) as ifile:
            data_pu[var] = norm(ifile["pileup"].values())
            data_pu_edges[var] = norm(ifile["pileup"].axis().edges())

    mask = mc_pu[year] > 0.
    for var in data_pu.keys():
        corr = data_pu[var].copy()
        corr[mask] /= mc_pu[year][mask]
        pileup_corr[year][var] = dense_lookup.dense_lookup(corr,data_pu_edges[var])

for year in pileup_corr.keys():
    pileup_corr[year]["central"]._values = np.minimum(5,pileup_corr[year]["central"]._values)
    pileup_corr[year]["up"]._values = np.minimum(5,pileup_corr[year]["up"]._values)
    pileup_corr[year]["down"]._values = np.minimum(5,pileup_corr[year]["down"]._values)

    corrections['%s_pileupweight'%year] = pileup_corr[year]["central"]
    corrections['%s_pileupweight_puUp'%year] = pileup_corr[year]["up"]
    corrections['%s_pileupweight_puDown'%year] = pileup_corr[year]["down"]

import pickle
import gzip
with gzip.open('data/corrections.pkl.gz', 'wb') as f:
    pickle.dump(corrections, f, -1)
