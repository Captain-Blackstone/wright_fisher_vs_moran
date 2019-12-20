# Inferring a demographic history of modern people populations using the Moran model

Demographic models based on genetic data take an important place in population genetic studies. They help to find
genetic regions that targeted by recent natural selection and therefore reveal genetic variation within and among
populations, explore population size changes, population splits and joins, migration and admixture. Complementing
archeological evidence of prehistorical events, demographic models may explain the expansion of humanity across the
globe. Besides it can be useful in medical genetic studies and can be applied in demographic inference of other species.

## Goal:
The goal of this project is the inference of a demographic history “Out of Africa” for African, European and Asian
populations using ∂a∂i and momi2 tools based on Wright-Fisher and Moran demographic models and comparison of the
results.

## Objectives:
- Study Wright-Fisher and Moran demographic models;
- Study the demographic history “Out of Africa” by Gutenkunst et al. [1];
- Install ∂a∂i  and learn to use it;
- Install momi2 and learn to use it;
- Implement the same demographic history;
- Compare the results.

## Materials and methods:
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

## Results:
We built six models. In ∂a∂i for two populations (YRI and CEU) with and without migration, and the same for three populations (YRI, CEU and CHB). In momi2 - model for two and three populations without migration because “pulse” migration in momi2 is not equivalent to migration in ∂a∂i and can’t be compared. (Table 2 and 3).


<h2>
Table 1. Model’s parameters
</h2>

| Parameter | Meaning                                                                                                                                                                                                                                                                                                                      |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Theta     | scaled mutation rate in ∂a∂i (4 * neutral mutation rate per generation * effective sequenced length * reference effective population size)                                                                                                                                                                                         |
| N_A       | reference effective population size                                                                                                                                                                                                                                                                                          |
| NAf       | population sizes for the African ancestral population after the growth                                                                                                                                                                                                                                                       |
| NB        | population sizes for the Eurasian ancestral population (between the divergence from the African ancestral population and the divergence of the European (CEU) and East Asian (CHB) populations for three populations model or in the time of the divergence from the African ancestral population for two populations model) |
| NEu0      | initial population sizes for European population                                                                                                                                                                                                                                                                             |
| NEu       | population sizes for European population after the exponential growth                                                                                                                                                                                                                                                        |
| NAs0      | initial population sizes for Asian population                                                                                                                                                                                                                                                                                |
| NAs       | population sizes for Asian population after the exponential growth                                                                                                                                                                                                                                                           |
| gj        | growth rate in j population per generation                                                                                                                                                                                                                                                                                   |
| Mi-j      | proportion of chromosomes per generation in population i and j that are new as a result of migration                                                                                                                                                                                                                         |
| TAf       | beginning of the growth in the African ancestral population (YRI), kya                                                                                                                                                                                                                                                       |
| TB        | divergence of the Eurasian ancestral population from the African ancestral population, kya                                                                                                                                                                                                                                   |
| TEu-As    | the European (CEU) and East Asian (CHB) divergence time, kya                                                                                                                                                                                                                                                                 |
| Tp        | time between ancestral population growth and the split (divergence of the Eurasian ancestral population from the African ancestral population), ky                                                                                                                                                                           |
| T         | populations split time (in two populations model), kya                                                                                                                                                                                                                                                                       |
|           | Tp+T = TAf for two populations model                                                                                                                                                                                                                                                                                         |


## References:
1. Gutenkunst R.N., Hernandez R.D., Williamson S.H., Bustamante C.D. (2009) Inferring the joint demographic history of multiple populations from multidimensional snp frequency data // PLoS Genet. 5: e1000695.
2. Livingston R.J., von Niederhausern A., Jegga A.G., Crawford D.C., Carlson C.S., et al. (2004) Pattern of sequence variation across 213 environmental response genes // Genome Res. Vol. 14. pp. 1821–1831.
3. https://github.com/yangjl/dadi
4. https://github.com/popgenmethods/momi2
5. https://momi2.readthedocs.io/en/latest/
6. Kamm J., Terhorst J., Durbin R., Song Y.S. (2019) Efficiently Inferring the Demographic History of Many Populations With Allele Count Data // Journal of the American Statistical Association.
7.  Bae C.J., Douka K., Petraglia M.D. (2017) On the origin of modern humans: Asian perspectives // Science.
8. A.-S. Malaspinas et al. (2016) A genomic history of Aboriginal Australia // Nature.
9. Rasmussen M. et al. (2011) An Aboriginal Australian Genome Reveals Separate Human Dispersals into Asia // Science.
