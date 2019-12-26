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
In this study we inferred the demographic history - the history of evolution and development - of modern African, European, and East Asian populations and compared different approaches.
- African population - Yoruba from Ibadan, Nigeria (YRI)
- European population - Northern and western Europeans (CEU)
- East Asian population - Han Chinese from Beijing, China (CHB)

Genetic data were presented as multi-population allele frequency spectrum (AFS) - the joint distribution of allele frequencies across diallelic variants. It was calculated using single nucleotide polymorphism (SNP) data from the Environmental Genome Project (EGP). Effective sequenced length (accounts for losses in alignment and missed calls) was 4.04*106 Mb (exom) and the neutral mutation rate was 2.35*108 per generation [2].
For computation the demographic history we used two Python packages ∂a∂i [1,3] and momi2 [4,5,6], simulating the expected AFS and comparing it with observed AFS using the maximum likelihood model. ∂a∂i is based on a diffusion approximation to the one-locus, two-allele Wright-Fisher process, but momi2 uses lookdown construction of the continuous-time Moran model expended by admixture between population.


## Results:
We built six models. In ∂a∂i for two populations (YRI and CEU) with and without migration, and the same for three populations (YRI, CEU and CHB). In momi2 - model for two and three populations without migration because “pulse” migration in momi2 is not equivalent to migration in ∂a∂i and can’t be compared. (Table 2 and 3).


<h4 align="center">
Table 1. Models’ parameters
</h4>

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

<h4 align="center">
Table 2. Models we built for two (African and Eurasian) populations with and without migration
</h4>

| Parameters \ Package 	|     ∂a∂i    	|    momi2    	|     ∂a∂i    	|
|----------------------	|:-----------:	|:-----------:	|:-----------:	|
| Migration            	|      No     	|      No     	|     Yes     	|
| Theta                	|    2749.3   	|             	|    2749.3   	|
| N_A                  	|     7240    	|     7113    	|     7240    	|
| NAf                  	|    13748    	|    13481    	|    13618    	|
| NB                   	|     286     	|     279     	|     514     	|
| gEu                  	| 5.35 * 10-3 	| 5.58 * 10-3 	| 2.03 * 10-3 	|
| NEu                  	|    68665    	|    76027    	|    13357    	|
| Tp, ky               	|    144.8    	|    137.5    	|    128.5    	|
| T, kya               	|     25.7    	|     24.9    	|     40.2    	|
| Maf-b                	|      -      	|      -      	|  6.3 * 10-5 	|

Above (columns 2 and 3) we can see very close demographic histories for African and Eurasian populations without migrations inferred by ∂a∂i and momi2 packages. The initial African ancestral population of 7 thousand people grew about 138-145 ky to 13,5 thousand before the split. About 25 kya less than 300 people diverged from the African population and found the Eurasian ancestral population, that than grew exponentially. The small Eurasian population size at the moment of split meant that population went through bottlenecks.
The number of people is just effective population size - the number of individuals in a population who contribute offspring to the next generation.
According to other researches [7] people started to go outside Africa before 60 kya and did that many times therefore migration should be considered. For this reason in our models without migration the time of split was shortened – genetic differences between populations accumulated faster that if genes mixing between populations as a result of migration.

We couldn’t compare the implementations of migration in two packages, but in the demographic history for African and Eurasian populations with migrations inferred by ∂a∂i (column 4) almost all parameters were similar to models without migrations except the time of the split and the size of the Eurasian population. The divergence time increased to 40 kya, on the other hand maybe we didn’t have enough data to get even more realistic results. The exceedance of the European population size in the model without migration over the model with migration is logical. The observed polymorphism in the population can be reached or by huge effective population size or by the inflow of new alleles as a result of migration.

Thus, we found that migration should be considered for inferring more realistic demographic history and it is consistent with the fact of the multiple exits of sapiens from Africa. Then we added the third population - East Asian – and compare our results with two populations model and other researches. 

<h4 align="center">
Table 3. Models we built for three (African, European and East Asian) populations with and without migrations
</h4>

| Parameters \ Package 	|     ∂a∂i    	|   momi2  	|     ∂a∂i    	|
|----------------------	|:-----------:	|:--------:	|:-----------:	|
| migration            	|      No     	|    No    	|     Yes     	|
| Theta                	|    2856.3   	|          	|    2788.2   	|
| N_A                  	|     7521    	|   7195   	|     7300    	|
| NAf                  	|    14078    	|   13364  	|    12300    	|
| NB                   	|     209     	|    146   	|     2100    	|
| NEu0                 	|     2264    	|   3584   	|     1000    	|
| gEu                  	| 1.03 * 10-3 	| 1 * 10-3 	| 3.98 * 10-3 	|
| NEu                  	|    15728    	|   9589   	|    27300    	|
| NAs0                 	|     972     	|   2458   	|     510     	|
| gAs                  	| 1.75 * 10-3 	| 1 * 10-3 	|  5.5 * 10-3 	|
| NAs                  	|    26325    	|   6576   	|    53220    	|
| TAf, kya             	|    280.4    	|   125.9  	|    221.6    	|
| TB, kya              	|     51.7    	|   26.2   	|    144.5    	|
| TEu-As, kya          	|     47.2    	|   24.6   	|     21.2    	|
| Maf-b                	|      -      	|     -    	|  25 * 10-5  	|
| Maf-eu               	|      -      	|     -    	|   3 * 10-5  	|
| Maf-as               	|      -      	|     -    	|  1.9 * 10-5 	|
| Meu-as               	|      -      	|     -    	|  9.6 * 10-5 	|

Above (columns 2 and 3) we can see two demographic histories for African, European and East Asian populations without migrations inferred by ∂a∂i and momi2 packages. The results more or less similar at the beginning, but the estimated time of prehistorical events were different. The initial African ancestral population of 7 thousand people grew to 13-14 thousand before the split. About 26-51 kya less than 150-200 people (bottlenecks) diverged from the African population and found the Eurasian ancestral population. The most probable time of this split is about 60 kya [7]. Split time of European and Asian populations also were different (52 vs. 26 kya). The latest estimation of time of this split is about 40 kya [7,8], but there were arguments for 25-38 kya [9]. Momi2 implies Moran model with overlapping generations and probably for this reason shorten the time.

The demographic history for African, European and East Asian populations with migrations inferred by ∂a∂i (column 4) shows divergence between West African and Eurasian populations 140 kya. This is earlier than other genetic studies, in part because incorporation of migration. The European (CEU) and East Asian (CHB) divergence time is about 21 kya, long after archeological evidence places modern humans in Europe [1].

Thus demographic histories for three populations inferred by ∂a∂i and momi2 packages gives contradictory results scarcely consistent with other researches. Maybe the interaction between three populations were more complicated and require more parameters. For example it is better to consider different waves of sapiens migration between the continents and admixture with Neandertals and Denisovans.
Comparing ∂a∂i and momi2 we think that Moran model with overlapping generations didn’t give more realistic results in comparison with Wright-Fisher model. However, momi2 substantially lowered the computational burden by replacing the coalescent with the continuous-time Moran model and allowed to infer the history for much more than three populations [6].
We can conclude that two approaches for inferring demographic history gave close results but both of them were sensitive to lacking of data and could take into account only limited demographic events. In this way demographic models could give quantitative evaluations of time for prehistorical events and sizes of populations but they should be verified by other methods of population genetics, paleontology, archeology and chronological dating methods.


## References:
1. Gutenkunst R.N., Hernandez R.D., Williamson S.H., Bustamante C.D. (2009) Inferring the joint demographic history of multiple populations from multidimensional snp frequency data // PLoS Genet. 5: e1000695.
2. Livingston R.J., von Niederhausern A., Jegga A.G., Crawford D.C., Carlson C.S., et al. (2004) Pattern of sequence variation across 213 environmental response genes // Genome Res. Vol. 14. pp. 1821–1831.
3. https://github.com/yangjl/dadi
4. https://github.com/popgenmethods/momi2
5. https://momi2.readthedocs.io/en/latest/
6. Kamm J., Terhorst J., Durbin R., Song Y.S. (2019) Efficiently Inferring the Demographic History of Many Populations With Allele Count Data // Journal of the American Statistical Association.
7. Bae C.J., Douka K., Petraglia M.D. (2017) On the origin of modern humans: Asian perspectives // Science.
8. Malaspinas A.-S. et al. (2016) A genomic history of Aboriginal Australia // Nature.
9. Rasmussen M. et al. (2011) An Aboriginal Australian Genome Reveals Separate Human Dispersals into Asia // Science.
