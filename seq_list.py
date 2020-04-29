# RPA+FH model for single charge sequence
# Short-range interaction contributes to only the k=0 FH term
# The FH term ehs parameters follow the definition in the PRL paper

# ver Git.1 Apr 14, 2020
# Upload to github

# Jan 1, 2019
# - Add function for pH-dependent charges

import numpy as np

R_pKa = 12.10
H_pKa = 6.04
K_pKa = 10.67
D_pKa = 3.71
E_pKa = 4.15

def qi_calc(x):
    return 10**x/(1+10**x)

def get_the_charge(seqname, pH=None):
    the_seq = getattr(polymers, seqname)
    N = len(the_seq)
    sigmai = np.zeros(N)

    use_pKa = False if pH == None else True
     

    for i in range(0, N):
        if the_seq[i] == 'D' :
            sigmai[i] = -qi_calc(pH-D_pKa) if use_pKa else -1
        elif the_seq[i] == 'E' :
            sigmai[i] = -qi_calc(pH-E_pKa) if use_pKa else -1
        elif the_seq[i] == 'R' :
            sigmai[i] = qi_calc(R_pKa-pH) if use_pKa else 1
        elif the_seq[i] == 'K' :
            sigmai[i] = qi_calc(K_pKa-pH) if use_pKa else 1
        elif the_seq[i] == 'H' :
            sigmai[i] = qi_calc(H_pKa-pH) if use_pKa else 0 
            if 'pH1' in seqname:
                print('seq is pH1')
                sigmai[i] = 1     
        else:
            sigmai[i] = 0

    return sigmai, N, the_seq




class polymers:

    PR_wt = \
    "MTELKAKGPR" + "APHVAGGPPS" + "PEVGSPLLCR" + "PAAGPFPGSQ" + "TSDTLPEVSA" + \
    "IPISLDGLLF" + "PRPCQGQDPS" + "DEKTQDQQSL" + "SDVEGAYSRA" + "EATRGAGGSS" + \
    "SSPPEKDSGL" + "LDSVLDTLLA" + "PSGPGQSQPS" + "PPACEVTSSW" + "CLFGPELPED" + \
    "PPAAPATQRV" + "LSPLMSRSGC" + "KVGDSSGTAA" + "AHKVLPRGLS" + "PARQLLLPAS" + \
    "ESPHWSGAPV" + "KPSPQAAAVE" + "VEEEDGSESE" + "ESAGPLLKGK" + "PRALGGAAAG" + \
    "GGAAAVPPGA" + "AAGGVALVPK" + "EDSRFSAPRV" + "ALVEQDAPMA" + "PGRSPLATTV" + \
    "MDFIHVPILP" + "LNHALLAART" + "RQLLEDESYD" + "GGAGAASAFA" + "PPRSSPCASS" + \
    "TPVAVGDFPD" + "CAYPPDAEPK" + "DDAYPLYSDF" + "QPPALKIKEE" + "EEGAEASARS" + \
    "PRSYLVAGAN" + "PAAFPDFPLG" + "PPPPLPPRAT" + "PSRPGEAAVT" + "AAPASASVSS" + \
    "ASSSGSTLEC" + "ILYKAEGAPP" + "QQGPFAPPPC" + "KAPGASGCLL" + "PRDGLPSTSA" + \
    "SAAAAGAAPA" + "LYPALGLNGL" + "PQLGYQAAVL" + "KEGLPQVYPP" + "YLNYLRPDSE" + \
    "ASQSPQYSFE" + "SLPQKI'

    PR_10StoD = \
    "MTELKAKGPR" + "APHVAGGPPD" + "PEVGSPLLCR" + "PAAGPFPGSQ" + "TSDTLPEVSA" + \
    "IPISLDGLLF" + "PRPCQGQDPS" + "DEKTQDQQSL" + "DDVEGAYSRA" + "EATRGAGGSS" + \
    "SDPPEKDSGL" + "LDSVLDTLLA" + "PSGPGQSQPD" + "PPACEVTSSW" + "CLFGPELPED" + \
    "PPAAPATQRV" + "LDPLMSRSGC" + "KVGDSSGTAA" + "AHKVLPRGLD" + "PARQLLLPAS" + \
    "ESPHWSGAPV" + "KPDPQAAAVE" + "VEEEDGSESE" + "ESAGPLLKGK" + "PRALGGAAAG" + \
    "GGAAAVPPGA" + "AAGGVALVPK" + "EDSRFSAPRV" + "ALVEQDAPMA" + "PGRDPLATTV" + \
    "MDFIHVPILP" + "LNHALLAART" + "RQLLEDESYD" + "GGAGAASAFA" + "PPRSDPCASS" + \
    "TPVAVGDFPD" + "CAYPPDAEPK" + "DDAYPLYSDF" + "QPPALKIKEE" + "EEGAEASARD" + \
    "PRSYLVAGAN" + "PAAFPDFPLG" + "PPPPLPPRAT" + "PSRPGEAAVT" + "AAPASASVSS" + \
    "ASSSGSTLEC" + "ILYKAEGAPP" + "QQGPFAPPPC" + "KAPGASGCLL" + "PRDGLPSTSA" + \
    "SAAAAGAAPA" + "LYPALGLNGL" + "PQLGYQAAVL" + "KEGLPQVYPP" + "YLNYLRPDSE" + \
    "ASQSPQYSFE" + "SLPQKI'

    Ddx4_N1 = \
    "MGDEDWEAEI" + "NPHMSSYVPI" + "FEKDRYSGEN" + "GDNFNRTPAS" + "SSEMDDGPSR" + \
    "RDHFMKSGFA" + "SGRNFGNRDA" + "GECNKRDNTS" + "TMGGFGVGKS" + "FGNRGFSNSR" + \
    "FEDGDSSGFW" + "RESSNDCEDN" + "PTRNRGFSKR" + "GGYRDGNNSE" + "ASGPYRRGGR" + \
    "GSFRGCRGGF" + "GLGSPNNDLD" + "PDECMQRTGG" + "LFGSRRPVLS" + "GTGNGDTSQS" + \
    "RSGSGSERGG" + "YKGLNEEVIT" + "GSGKNSWKSE" + "AEGGES" + "AAAAA"

    Ddx4_N1_pH1 = \
    "MGoooWoAoI" + "NPHMSSYVPI" + "FoKoRYSGoN" + "GoNFNRTPAS" + "SSoMooGPSR" + \
    "RoHFMKSGFA" + "SGRNFGNRoA" + "GoCNKRoNTS" + "TMGGFGVGKS" + "FGNRGFSNSR" + \
    "FooGoSSGFW" + "RoSSNoCooN" + "PTRNRGFSKR" + "GGYRoGNNSo" + "ASGPYRRGGR" + \
    "GSFRGCRGGF" + "GLGSPNNoLo" + "PooCMQRTGG" + "LFGSRRPVLS" + "GTGNGoTSQS" + \
    "RSGSGSoRGG" + "YKGLNooVIT" + "GSGKNSWKSo" + "AoGGoS" + "AAAAA"

    Ddx4_N1_CS = \
    "MGDRDWRAEI" + "NPHMSSYVPI" + "FEKDRYSGEN" + "GRNFNDTPAS" + "SSEMRDGPSE" + \
    "RDHFMKSGFA" + "SGDNFGNRDA" + "GKCNERDNTS" + "TMGGFGVGKS" + "FGNEGFSNSR" + \
    "FERGDSSGFW" + "RESSNDCRDN" + "PTRNDGFSDR" + "GGYEKGNNSE" + "ASGPYERGGR" + \
    "GSFDGCRGGF" + "GLGSPNNRLD" + "PRECMQRTGG" + "LFGSDRPVLS" + "GTGNGDTSQS" + \
    "RSGSGSERGG" + "YKGLNEKVIT" + "GSGENSWKSE" + "ARGGES" + "AAAAA"

    Ddx4_N1_CS_pH1 = \
    "MGoRoWRAoI" + "NPHMSSYVPI" + "FoKoRYSGoN" + "GRNFNoTPAS" + "SSoMRoGPSo" + \
    "RoHFMKSGFA" + "SGoNFGNRoA" + "GKCNoRoNTS" + "TMGGFGVGKS" + "FGNoGFSNSR" + \
    "FoRGoSSGFW" + "RoSSNoCRoN" + "PTRNoGFSoR" + "GGYoKGNNSo" + "ASGPYoRGGR" + \
    "GSFoGCRGGF" + "GLGSPNNRLo" + "PRoCMQRTGG" + "LFGSoRPVLS" + "GTGNGoTSQS" + \
    "RSGSGSoRGG" + "YKGLNoKVIT" + "GSGoNSWKSo" + "ARGGoS" + "AAAAA"

    pappu1  = "EKEKEKEKEKEKEKEKEKEKEKEKEKEKEKEKEKEKEKEKEKEKEKEKEK"; #0.0009
    pappu2  = "EEEKKKEEEKKKEEEKKKEEEKKKEEEKKKEEEKKKEEEKKKEEEKKKEK"; #0.0025
    pappu3  = "KEKKKEKKEEKKEEKEKEKEKEEKKKEEKEKEKEKKKEEKEKEEKKEEEE"; #0.0139
    pappu4  = "KEKEKKEEKEKKEEEKKEKEKEKKKEEKKKEEKEEKKEEKKKEEKEEEKE"; #0.0140
    pappu5  = "KEKEEKEKKKEEEEKEKKKKEEKEKEKEKEEKKEEKKKKEEKEEKEKEKE"; #0.0245
    pappu6  = "EEEKKEKKEEKEEKKEKKEKEEEKKKEKEEKKEEEKKKEKEEEEKKKKEK"; #0.0273
    pappu7  = "EEEEKKKKEEEEKKKKEEEEKKKKEEEEKKKKEEEEKKKKEEEEKKKKEK"; #0.0450
    pappu8  = "KKKKEEEEKKKKEEEEKKKKEEEEKKKKEEEEKKKKEEEEKKKKEEEEKE"; #0.0450 
    pappu9  = "EEKKEEEKEKEKEEEEEKKEKKEKKEKKKEEKEKEKKKEKKKKEKEEEKE"; #0.0624 
    pappu10 = "EKKKKKKEEKKKEEEEEKKKEEEKKKEKKEEKEKEEKEKKEKKEEKEEEE"; #0.0834 
    pappu11 = "EKEKKKKKEEEKKEKEEEEKEEEEKKKKKEKEEEKEEKKEEKEKKKEEKK"; #0.0841 
    pappu12 = "EKKEEEEEEKEKKEEEEKEKEKKEKEEKEKKEKKKEKKEEEKEKKKKEKK"; #0.0864 
    pappu13 = "KEKKKEKEKKEKKKEEEKKKEEEKEKKKEEKKEKKEKKEEEEEEEKEEKE"; #0.0951 
    pappu14 = "EKKEKEEKEEEEKKKKKEEKEKKEKKKKEKKKKKEEEEEEKEEKEKEKEE"; #0.1311 
    pappu15 = "KKEKKEKKKEKKEKKEEEKEKEKKEKKKKEKEKKEEEEEEEEKEEKKEEE"; #0.1354 
    pappu16 = "EKEKEEKKKEEKKKKEKKEKEEKKEKEKEKKEEEEEEEEEKEKKEKKKKE"; #0.1458 
    pappu17 = "EKEKKKKKKEKEKKKKEKEKKEKKEKEEEKEEKEKEKKEEKKEEEEEEEE"; #0.1643 
    pappu18 = "KEEKKEEEEEEEKEEKKKKKEKKKEKKEEEKKKEEKKKEEEEEEKKKKEK"; #0.1677 
    pappu19 = "EEEEEKKKKKEEEEEKKKKKEEEEEKKKKKEEEEEKKKKKEEEEEKKKKK"; #0.1941 
    pappu20 = "EEKEEEEEEKEEEKEEKKEEEKEKKEKKEKEEKKEKKKKKKKKKKKKEEE"; #0.2721 
    pappu21 = "EEEEEEEEEKEKKKKKEKEEKKKKKKEKKEKKKKEKKEEEEEEKEEEKKK"; #0.2737 
    pappu22 = "KEEEEKEEKEEKKKKEKEEKEKKKKKKKKKKKKEKKEEEEEEEEKEKEEE"; #0.3218 
    pappu23 = "EEEEEKEEEEEEEEEEEKEEKEKKKKKKEKKKKKKKEKEKKKKEKKEEKK"; #0.3545 
    pappu24 = "EEEEKEEEEEKEEEEEEEEEEEEKKKEEKKKKKEKKKKKKKEKKKKKKKK"; #0.4456 
    pappu25 = "EEEEEEEEEEEKEEEEKEEKEEKEKKKKKKKKKKKKKKKKKKEEKKEEKE"; #0.5283 
    pappu26 = "KEEEEEEEKEEKEEEEEEEEEKEEEEKEEKKKKKKKKKKKKKKKKKKKKE"; #0.6101 
    pappu27 = "KKEKKKEKKEEEEEEEEEEEEEEEEEEEEKEEKKKKKKKKKKKKKKKEKK"; #0.6729 
    pappu28 = "EKKKKKKKKKKKKKKKKKKKKKEEEEEEEEEEEEEEEEEEKKEEEEEKEK"; #0.7666 
    pappu29 = "KEEEEKEEEEEEEEEEEEEEEEEEEEEKKKKKKKKKKKKKKKKKKKKKKK"; #0.8764 
    pappu30 = "EEEEEEEEEEEEEEEEEEEEEEEEEKKKKKKKKKKKKKKKKKKKKKKKKK"; #1.0000

    # Panagiotopoulos 
    pana1 = "KKKKEEEE"
    pana2 = "KKEEKKEE"
    pana3 = "KEEEKEKK"
    pana4 = "KKEEEKEK"
    pana5 = "KKKKKKKKEEEEEEEE"
    pana6 = "KKKKEEEEKKKKEEEE"
    pana7 = "KEEKKKEKEEEKKEKE" 

    polye =   "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"

    # YHL's abnormal sequences                                  #   SCD    kappa   Tc of RPA
    yhl1 = "KKKKKEKKKKKEKKKKEKKKKEKKEKEEEKEEEEKEEEEKEEEEKEEEEE" # -12.79   0.176   3.815
    yhl2 = "EEEEEEEEKKEKKKKEEEEEEEEEEEKKKKEEEKEKEKKKKKKKKKKKKK" # -10.30   0.485   3.114 
    yhl3 = "KKKKEEEEEEEEEEEEEEEEEEKKEKKKKKKKKKKKKKKEKEEEEEKKKK" #  -8.27   0.612   2.909 
    yhl4 = "KKKKKKEEEEEEEEEEEEEEEKKKKKKKKKKKKKKKKKKEEEEEEEEEEK" #  -6.11   0.778   2.485 




