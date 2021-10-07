# alzheimers-risk-loci
## Motivations

In a comprehensive [genome-wide association study](https://doi.org/10.1038/s41588-021-00921-z) published in _Nature Genetics_ this month, researchers resolved seven previously unidentified genetic loci associated with a high risk of late-onset Alzheimer’s disease in a sample of over 1,000,000 adult LOAD patients. The finding begs the question of what the functional roles of these seven genetic risk factors are in healthy individuals, and whether those functions might be related to Alzheimer’s disease progression. Identifying and studying the genetic underpinnings that predispose individuals to Alzheimer’s disease (and the corresponding proteins that those genes express) can enhance our understanding of the overall disease pathology.

This repository documents the methods and results of a bioinformatics data collection exercise aiming explore a selection of the genetic risk factors implicated in Alzheimer’s disease. We retrieve, parse and re-format genetic records from the NCBI-curated [GenBank](https://www.ncbi.nlm.nih.gov/nuccore/) nucleotide sequence database to construct a dataset suitable for subsequent analyses. 

## Contents
* .gb files - raw data files containing individual genetic records
* alzheimers_risk_loci.csv - final formatted data file
* parse_genbank_files.py - file parser to construct a csv from the raw data files


## Acknowledgements
* Original data source for all gene records: [GenBank server](https://www.ncbi.nlm.nih.gov/nuccore/)
  *  Benson DA, Cavanaugh M, Clark K, Karsch-Mizrachi I, Lipman DJ, Ostell J, Sayers EW. GenBank. Nucleic Acids Res. 2013 Jan;41(Database issue):D36-42. doi: 10.1093/nar/gks1195. Epub 2012 Nov 27. PMID: 23193287; PMCID: PMC3531190.
* Data parsing and manipulation: [BioPython](https://biopython.org/docs/1.75/api/index.html) 
* [Alzheimer's GWAS paper](https://doi.org/10.1038/s41588-021-00921-z)
  * Wightman, D.P., Jansen, I.E., Savage, J.E. et al. A genome-wide association study with 1,126,563 individuals identifies new risk loci for Alzheimer’s disease. Nat Genet 53, 1276–1282 (2021). https://doi.org/10.1038/s41588-021-00921-z

