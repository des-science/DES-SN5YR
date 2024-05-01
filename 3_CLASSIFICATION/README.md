## DES_classification.csv contains Probabilities of being SN Ia for the 1635 DES SMP lightcurve.


**Classification Probability Columns definition:**

- PROB_SNNV19* - Prob of being Ia from SuperNNova trained on sims generated using core-collapse templates from Vincenzi et al 2019 (*Nominal*)
- PROB_SNNDESCC - Prob of being Ia from SuperNNova trained on sims generated using core-collapse templates from Jones et al 2017
- PROB_SNNJ17 - Prob of being Ia from SuperNNova trained on sims generated using core-collapse templates from DES data
- PROB_SCONE - Prob of being Ia from SCONE trained on sims generated using core-collapse templates Vincenzi et al 2019
- PROB_SNIRFV19 - Prob of being Ia from SNIRF trained on sims generated using core-collapse templates from Vincenzi et al 2019
- PROBCC_BEAMS - BEAMS Prob of being core-collapse (see eq. 6 in Vincenzi et al 2024)

(*) PROB_SNNV19 is our Nominal


## DES_noredshift_classification_Moller2024.csv contains Probabilities of being SN Ia using only light-curves (no redshift information) for the sample in Moller et al. 2024. 

**Classification Probability Columns definition:**
- PROB_SNN_noz_singlemodel: Prob of being Ia from SuperNNova trained on sims generated using core-collapse templates from Vincenzi et al 2019. This model uses only light-curves for classification, no redshift information. (*Nominal: single model*)
- PROB_SNN_noz_ensemble: Prob of being Ia from SuperNNova trained on sims generated using core-collapse templates from Vincenzi et al 2019. This model uses only light-curves for classification, no redshift information. These probabilities are an average of 5 independet models (*Ensemble*).

### References:
- **SuperNNova:**
  - References: https://academic.oup.com/mnras/article-abstract/491/3/4277/5651173, https://arxiv.org/abs/2201.11142, https://arxiv.org/abs/2402.18690
  - Documentation: https://supernnova.readthedocs.io/en/latest/index.html
- **SCONE:**:
  - References: https://arxiv.org/abs/2106.04370
  - Documentation: https://github.com/helenqu/scone
- **SNIRF:**
  - Documentation: https://github.com/evevkovacs/ML-SN-Classifier
