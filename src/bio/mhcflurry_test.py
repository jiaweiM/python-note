from mhcflurry import Class1PresentationPredictor

predictor = Class1PresentationPredictor.load()


print(len(predictor.supported_alleles))

for item in predictor.supported_alleles:
    print(item)


# alleles = predictor.supported_alleles

# df = predictor.predict(
#     peptides=["SIINFEKL", "NLVPMVATV"],
#     alleles=["HLA-A0201", "HLA-A0301"],
#     verbose=0
# )
#
# print(df)
#
#
# def test_affinity():
#     from mhcflurry import Class1AffinityPredictor
#     affinity_predictor = Class1AffinityPredictor.load()
#     df = affinity_predictor.predict_to_dataframe(alleles="HLA-A0201", peptides=["SIINFEKL", "SIINFEQL"])
#     print(df)
