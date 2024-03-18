## DES_classification.csv contains Probabilities of being SN Ia for the 1635 DES SMP lightcurve.


**Classification Probability Columns definition:**

- PROB_SNNV19* - Prob of being Ia from SuperNNova trained on sims generated using core-collapse templates from Vincenzi et al 2019 (*Nominal*)
- PROB_SNNDESCC - Prob of being Ia from SuperNNova trained on sims generated using core-collapse templates from Jones et al 2017
- PROB_SNNJ17 - Prob of being Ia from SuperNNova trained on sims generated using core-collapse templates from DES data
- PROB_SCONE - Prob of being Ia from SCONE trained on sims generated using core-collapse templates Vincenzi et al 2019
- PROB_SNIRFV19 - Prob of being Ia from SNIRF trained on sims generated using core-collapse templates from Vincenzi et al 2019
- PROBCC_BEAMS - BEAMS Prob of being core-collapse (see eq. 6 in Vincenzi et al 2024)

(*) PROB_SNNV19 is our Nominal

### References:
- **SuperNNova:**
  - References: https://academic.oup.com/mnras/article-abstract/491/3/4277/5651173, https://arxiv.org/abs/2201.11142, https://arxiv.org/abs/2402.18690
  - Documentation: https://supernnova.readthedocs.io/en/latest/index.html
- **SCONE:**:
  - References: https://arxiv.org/abs/2106.04370
  - Documentation: https://github.com/helenqu/scone
- **SNIRF:**
  - Documentation: https://github.com/evevkovacs/ML-SN-Classifier
