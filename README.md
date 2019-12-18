Inferring a demographic history of modern people populations using the Moran model

Demographic models based on genetic data take an important place in population genetic studies. They help to find
genetic regions that targeted by recent natural selection and therefore reveal genetic variation within and among
populations, explore population size changes, population splits and joins, migration and admixture. Complementing
archeological evidence of prehistorical events, demographic models may explain the expansion of humanity across the
globe. Besides it can be useful in medical genetic studies and can be applied in demographic inference of other species.

Goal:
The goal of this project is the inference of a demographic history “Out of Africa” for African, European and Asian
populations using ∂a∂i and momi2 tools based on Wright-Fisher and Moran demographic models and comparison of the
results.

Objectives:
- Study Wright-Fisher and Moran demographic models;
- Study the demographic history “Out of Africa” by Gutenkunst et al. [1];
- Install ∂a∂i  and learn to use it;
- Install momi2 and learn to use it;
- Implement the same demographic history;
- Compare the results.

Materials and methods:
In this study we inferred the demographic history - the history of evolution and development - of modern African,
European, and East Asian populations and compared different approaches.
African population - Yoruba from Ibadan, Nigeria (YRI)
European population - Northern and western Europeans (CEU)
East Asian population - Han Chinese from Beijing, China (CHB)
Genetic data were presented as multi-population allele frequency spectrum (AFS) - the joint distribution of allele
frequencies across diallelic variants. It was calculated using single nucleotide polymorphism (SNP) data from the
Environmental Genome Project (EGP) [2].
For computation the demographic history we used two Python packages ∂a∂i [1,3] and momi2 [4,5,6], simulating the
expected AFS and comparing it with observed AFS using the maximum likelihood model. ∂a∂i is based on a diffusion
approximation to the one-locus, two-allele Wright-Fisher process, but momi2 uses lookdown construction of the
continuous-time Moran model expended by admixture between population.
